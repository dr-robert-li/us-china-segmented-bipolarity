"""Joint estimator for Blocks M, E and P -- NumPyro NUTS.

Implements the committed default nest ``(D)(F)`` from ``model/SPECIFICATION.md``
sections 4-6, as a joint state-space model. This file is the estimator the
specification's section 10 commits; the three-structure nesting comparison, the
Stan cross-check, and the leave-one-decade-out machinery bind only at real
estimation and are deliberately absent here.

Scope at first build: **synthetic validation only**. No ingested data exists
(``data/derived/`` has not been created by any first ingest), so the estimator
is validated by cross-implementation parameter recovery: synthetic data are
generated from the independent numpy implementation in ``prior_predictive.py``
plus the measurement layer below, and fitted with this JAX implementation.
Recovery across two implementations is a stronger check than a model fitting
its own simulator, because a shared transcription error cannot cancel.

Single source of truth: every prior constant is imported from
``prior_predictive.py`` rather than re-transcribed from ``model/PRIORS.md``.
Two transcriptions of one prior can diverge; one cannot.

Both gaps registered at first build are now closed by authored commitments and
adopted here: initial-state priors per ``PRIORS.md`` Amendment 2 (anchored
0.5 / anchor-absent 1.0 location scales; stationary AR(1) initial growth
states), and the stochastic AI-intensity process per ``SPECIFICATION.md``
Amendment 03 with its follow-up note (per-state local linear trend on
``log(1+AI)``, no saturation term, cross-state MEAN driving ``sigma_top``) and
``PRIORS.md`` Amendment 3 (``gstar_ai``, ``sigma_ai``, stationary ``g_ai0``;
provisional pending author ratification). In synthetic scope AI intensity is
UNOBSERVED -- no section 7 indicator block exists yet -- so delta's
information path runs through an unmeasured latent and weaker delta behaviour
is expected, not a defect. Recorded in ``model/ESTIMATION-SYNTHETIC-RUN-003.md``.
"""

from __future__ import annotations

from dataclasses import dataclass

import jax
import jax.numpy as jnp
import numpy as np
import numpyro
import numpyro.distributions as dist
from numpyro.infer import MCMC, NUTS, init_to_sample

# Double precision, module-wide. The CES unit-elasticity branch evaluates
# inner**(1/r) at |r| down to 1e-6 (the same threshold as the numpy
# implementation), which float32 cannot represent, and SPECIFICATION.md
# section 10 commits bit-for-bit reproducibility, which float32 NUTS on this
# model does not reliably deliver.
numpyro.enable_x64()

from .prior_predictive import (
    ENGINEERING_CEILING_MULTIPLE,
    INPUTS,
    S_V,
    STATES,
    SYNTHETIC_BASELINE,
    PriorDraw,
    ces,
    sample_prior,
    simulate,
)

# Measurement design for the synthetic exercise. Mirrors the anchor structure
# of SPECIFICATION.md section 4.1 rather than bypassing it: the deployment
# inputs are "physically measurable" and carry a tier-1 anchor with b fixed at
# 0; the frontier inputs are anchor-absent, so their bias terms are FIXED at
# the prior mean (0.0) per section 4.2 rather than estimated, and the list of
# anchor-absent quantities is exported with every fit.
ANCHORED = ("D1", "D2", "D3")
ANCHOR_ABSENT = ("F1", "F2", "F3")
ANCHOR_SIGMA = 0.02  # tier-1: no bias term, small fixed noise scale
BIAS_PRIOR_SD = 0.10
# Initial-state location scales per PRIORS.md Amendment 2: 0.5 for anchored
# series, 1.0 for anchor-absent. Order follows INPUTS = (D1,D2,D3,F1,F2,F3).
X0_PRIOR_SD = (0.5, 0.5, 0.5, 1.0, 1.0, 1.0)
# Floor on the biased-series noise scale, applied IDENTICALLY in the model
# prior and the synthetic truth generator (SBC semantics require the two to
# match). Divergence diagnosis (run 002) localised the funnel to sigma_z
# components collapsing toward zero; the floor is defended as measurement
# realism -- log-scale noise below 1 percent is not a property of any real
# published series -- not as a sampler convenience.
SIGMA_Z_FLOOR = 0.01

# Capability elements observed in the synthetic measurement block. Observing
# only the inputs would leave Block P without any likelihood contribution and
# the recovery test would not exercise it.
OBSERVED_ELEMENTS = (0, 1)  # Y_throughput, Y_frontier
Y_OBS_SIGMA = 0.05

# Same unit-elasticity threshold as the numpy ces(); requires x64 above.
_EPS_UNIT_SIGMA = 1e-6


def ces_jax(a: jnp.ndarray, shares: jnp.ndarray, sigma: jnp.ndarray) -> jnp.ndarray:
    """CES aggregate along the last axis, safe at ``sigma -> 1``.

    The numpy implementation branches with ``if``; under JAX a naive
    ``jnp.where`` still propagates NaN *gradients* from the unselected power
    branch, so the power form is evaluated at a safe exponent (r = 1) wherever
    the Cobb-Douglas branch is selected. This is the double-where pattern.
    """
    log_a = jnp.log(jnp.maximum(a, 1e-12))
    sigma_b = jnp.broadcast_to(jnp.asarray(sigma, dtype=log_a.dtype), log_a.shape)
    r = (sigma_b - 1.0) / sigma_b
    near_one = jnp.abs(r) < _EPS_UNIT_SIGMA
    r_safe = jnp.where(near_one, 1.0, r)
    inner = jnp.sum(shares * jnp.exp(r_safe * log_a), axis=-1)
    power = inner ** (1.0 / r_safe[..., 0])
    cobb_douglas = jnp.exp(jnp.sum(shares * log_a, axis=-1))
    return jnp.where(near_one[..., 0], cobb_douglas, power)


def model(
    T: int,
    z_anchor: jnp.ndarray | None = None,  # (n_states, T, 3) log-scale
    z_biased: jnp.ndarray | None = None,  # (n_states, T, 6) log-scale
    z_capability: jnp.ndarray | None = None,  # (n_states, T, 2) log-scale
    stress: jnp.ndarray | None = None,  # (n_states, T)
) -> None:
    n_s, n_j = len(STATES), len(INPUTS)
    if stress is None:
        stress = jnp.zeros((n_s, T))
    baseline = jnp.array(
        [[SYNTHETIC_BASELINE[s][j] for j in INPUTS] for s in STATES]
    )
    ceiling = jnp.array([ENGINEERING_CEILING_MULTIPLE[j] for j in INPUTS])

    # ---- Block P parameters, priors as committed in PRIORS.md ----
    sigma_D = numpyro.sample("sigma_D", dist.LogNormal(jnp.log(0.5), 0.45))
    sigma_F = numpyro.sample("sigma_F", dist.LogNormal(jnp.log(0.7), 0.50))
    log_s0 = numpyro.sample(
        "log_sigma_top0",
        dist.TruncatedNormal(
            jnp.log(0.6),
            0.55,
            low=jnp.log(PriorDraw.SIGMA_TOP_MIN),
            high=jnp.log(PriorDraw.SIGMA_TOP_MAX),
        ),
    )
    sigma_top0 = numpyro.deterministic("sigma_top0", jnp.exp(log_s0))
    delta = numpyro.sample("delta", dist.Normal(0.0, 0.25))
    tau = numpyro.sample("tau", dist.HalfNormal(0.05))
    alpha_D = numpyro.sample("alpha_D", dist.Dirichlet(jnp.ones(3) * 4.0))
    alpha_F = numpyro.sample("alpha_F", dist.Dirichlet(jnp.ones(3) * 4.0))
    w = numpyro.sample(
        "w",
        dist.Uniform(
            jnp.array([0.60, 0.10, 0.35, 0.30]), jnp.array([0.90, 0.40, 0.65, 0.60])
        ).to_event(1),
    )
    # AI-intensity latent parameters, SPECIFICATION.md Amendment 03 +
    # PRIORS.md Amendment 3 (provisional): per-state long-run growth, own
    # innovation scale, persistence shared with rho_g below.
    gstar_ai = numpyro.sample(
        "gstar_ai",
        dist.FoldedDistribution(dist.Normal(0.03, 0.02)).expand([n_s]).to_event(1),
    )
    sigma_ai = numpyro.sample("sigma_ai", dist.HalfNormal(S_V))

    # ---- Block E parameters ----
    kappa = numpyro.sample("kappa", dist.HalfNormal(0.05).expand([n_j]).to_event(1))
    phi = numpyro.sample("phi", dist.Gamma(2.0, 1.0).expand([n_j]).to_event(1))
    xbar = numpyro.sample(
        "xbar",
        dist.LogNormal(jnp.log(ceiling[None, :] * baseline), 0.6).to_event(2),
    )
    gstar = numpyro.sample(
        "gstar", dist.Normal(0.02, 0.02).expand([n_s, n_j]).to_event(2)
    )
    rho_g = numpyro.sample("rho_g", dist.Beta(6.0, 2.0))
    psi = numpyro.sample("psi", dist.Normal(0.0, 0.10).expand([n_s, n_j]).to_event(2))
    sigma_u = numpyro.sample("sigma_u", dist.HalfNormal(0.05))
    sigma_v = numpyro.sample("sigma_v", dist.HalfNormal(S_V))

    # ---- Block E latent paths, non-centered ----
    x0_sd = jnp.array(X0_PRIOR_SD)
    log_x0 = numpyro.sample(
        "log_x0", dist.Normal(jnp.log(baseline), x0_sd[None, :]).to_event(2)
    )
    z_u = numpyro.sample("z_u", dist.Normal(0, 1).expand([n_s, T - 1, n_j]).to_event(3))
    z_v = numpyro.sample("z_v", dist.Normal(0, 1).expand([n_s, T - 1, n_j]).to_event(3))
    z_w = numpyro.sample("z_w", dist.Normal(0, 1).expand([T - 1]).to_event(1))

    # Initial growth states at their AR(1) stationary distribution, PRIORS.md
    # Amendment 2, non-centered. The clamp on 1 - rho_g^2 matters: the
    # Beta(6, 2) upper tail otherwise explodes the scale factor and reopens
    # the trapped-chain trap recorded in run 002.
    stationary = jnp.sqrt(jnp.maximum(1.0 - rho_g**2, 1e-4))
    z_g0 = numpyro.sample("z_g0", dist.Normal(0, 1).expand([n_s, n_j]).to_event(2))
    g0 = gstar + sigma_v / stationary * z_g0

    gstar_t = gstar[:, None, :] + psi[:, None, :] * stress[:, :, None]  # (n_s,T,n_j)

    def step(carry, t):
        log_x_prev, g_prev = carry
        g = rho_g * g_prev + (1.0 - rho_g) * gstar_t[:, t, :] + sigma_v * z_v[:, t - 1, :]
        drag = kappa[None, :] * jnp.exp(
            phi[None, :] * (log_x_prev - jnp.log(xbar))
        )
        log_x = jnp.clip(
            log_x_prev + g - drag + sigma_u * z_u[:, t - 1, :], -30.0, 30.0
        )
        return (log_x, g), log_x

    (_, _), log_x_rest = jax.lax.scan(
        step, (log_x0, g0), jnp.arange(1, T)
    )  # (T-1, n_s, n_j)
    log_x = jnp.concatenate(
        [log_x0[None, :, :], log_x_rest], axis=0
    ).transpose(1, 0, 2)  # (n_s, T, n_j)

    # ---- sigma_top walk, stochastic AI intensity per Amendment 03 ----
    # Per-state local linear trend on log(1+AI), same form as the Block E
    # inputs, no saturation term (Amendment 03 follow-up note). UNOBSERVED in
    # synthetic scope: no indicator block exists yet, so the latent is
    # informed only through sigma_top's effect on the capability observations.
    z_gai0 = numpyro.sample("z_gai0", dist.Normal(0, 1).expand([n_s]).to_event(1))
    g_ai0 = gstar_ai + sigma_ai / stationary * z_gai0
    z_ai = numpyro.sample("z_ai", dist.Normal(0, 1).expand([n_s, T - 1]).to_event(2))

    def ai_step(g_prev, t):
        g = rho_g * g_prev + (1.0 - rho_g) * gstar_ai + sigma_ai * z_ai[:, t - 1]
        return g, g

    _, g_ai_rest = jax.lax.scan(ai_step, g_ai0, jnp.arange(1, T))  # (T-1, n_s)
    log1p_ai = jnp.concatenate(
        [jnp.zeros((1, n_s)), jnp.cumsum(g_ai_rest, axis=0)], axis=0
    )  # (T, n_s)
    # Cross-state MEAN of log(1+AI) drives the shared sigma_top -- the only
    # simple swap-invariant pooling, per the Amendment 03 follow-up note.
    mean_log1p_ai = jnp.mean(log1p_ai, axis=1)  # (T,)
    span = PriorDraw.SIGMA_TOP_MAX - PriorDraw.SIGMA_TOP_MIN
    p0 = (sigma_top0 - PriorDraw.SIGMA_TOP_MIN) / span
    p0 = jnp.clip(p0, 1e-4, 1 - 1e-4)
    ls0 = jnp.log(p0 / (1 - p0))
    incr = delta * jnp.diff(mean_log1p_ai) + tau * z_w
    ls = jnp.concatenate([ls0[None], ls0 + jnp.cumsum(incr)])
    sigma_top = PriorDraw.SIGMA_TOP_MIN + span / (1.0 + jnp.exp(-ls))  # (T,)

    # ---- Block P: capability elements ----
    x = jnp.exp(log_x)
    q_d = ces_jax(x[:, :, :3], alpha_D, sigma_D)  # (n_s, T)
    q_f = ces_jax(x[:, :, 3:], alpha_F, sigma_F)
    q = jnp.stack([q_d, q_f], axis=-1)[:, :, None, :]  # (n_s, T, 1, 2)
    shares = jnp.stack([w, 1.0 - w], axis=-1)[None, None, :, :]  # (1,1,4,2)
    Y = ces_jax(q, shares, sigma_top[None, :, None, None])  # (n_s, T, 4)
    log_Y = jnp.log(jnp.maximum(Y, 1e-12))
    numpyro.deterministic("log_Y", log_Y)

    # ---- Block M ----
    # Tier-1 anchors on the deployment inputs: lambda = 1, b = 0 by rule.
    numpyro.sample(
        "z_anchor",
        dist.Normal(log_x[:, :, :3], ANCHOR_SIGMA).to_event(3),
        obs=z_anchor,
    )
    # Biased series on all six inputs. Anchored latents: b estimated.
    # Anchor-absent latents: b FIXED at the prior mean (0.0), per section 4.2.
    lam = numpyro.sample(
        "lam", dist.Normal(1.0, 0.05).expand([n_j]).to_event(1)
    )
    b_anchored = numpyro.sample(
        "b_anchored", dist.Normal(0.0, BIAS_PRIOR_SD).expand([n_s, 3]).to_event(2)
    )
    b = jnp.concatenate([b_anchored, jnp.zeros((n_s, 3))], axis=-1)  # (n_s, n_j)
    sigma_z = numpyro.sample(
        "sigma_z",
        dist.TruncatedNormal(0.0, 0.05, low=SIGMA_Z_FLOOR).expand([n_j]).to_event(1),
    )
    numpyro.sample(
        "z_biased",
        dist.Normal(
            lam[None, None, :] * log_x + b[:, None, :], sigma_z[None, None, :]
        ).to_event(3),
        obs=z_biased,
    )
    # Capability observations, anchor-style, on the two observed elements.
    numpyro.sample(
        "z_capability",
        dist.Normal(log_Y[:, :, jnp.array(OBSERVED_ELEMENTS)], Y_OBS_SIGMA).to_event(3),
        obs=z_capability,
    )


# ---------------------------------------------------------------------------
# Synthetic data from the INDEPENDENT numpy implementation
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class SyntheticData:
    z_anchor: np.ndarray
    z_biased: np.ndarray
    z_capability: np.ndarray
    truth: dict[str, object]


def _measure(
    log_x: np.ndarray, log_Y: np.ndarray, rng: np.random.Generator
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Block M measurement layer shared by both synthetic generators."""
    lam = rng.normal(1.0, 0.05, size=len(INPUTS))
    b = np.concatenate(
        [rng.normal(0.0, BIAS_PRIOR_SD, size=(2, 3)), np.zeros((2, 3))], axis=-1
    )
    # Truncated half-normal above SIGMA_Z_FLOOR, matching the model prior
    # exactly (rejection sampling; acceptance ~0.92 so this terminates fast).
    sigma_z = np.empty(len(INPUTS))
    for j in range(len(INPUTS)):
        while True:
            draw_val = abs(rng.normal(0.0, 0.05))
            if draw_val >= SIGMA_Z_FLOOR:
                sigma_z[j] = draw_val
                break

    z_anchor = log_x[:, :, :3] + rng.normal(0, ANCHOR_SIGMA, size=log_x[:, :, :3].shape)
    z_biased = (
        lam[None, None, :] * log_x
        + b[:, None, :]
        + rng.normal(0, 1, size=log_x.shape) * sigma_z[None, None, :]
    )
    z_capability = log_Y + rng.normal(0, Y_OBS_SIGMA, size=log_Y.shape)
    return z_anchor, z_biased, z_capability, lam, b


def make_synthetic(draw, T: int, seed: int) -> SyntheticData:
    """Generate observations from prior_predictive.simulate plus Block M noise.

    ``draw`` is a numpy ``PriorDraw``; the latent paths come from the numpy
    simulator so that recovery is cross-implementation.

    NOT suitable for SBC: ``simulate`` fixes x0 at the baseline and both
    initial growth states at their long-run means, while the model samples all
    three from the Amendment 2/3 priors. Fine for single-truth recovery
    (prior wider than generator); rank-uniformity requires ``make_sbc_synthetic``.
    """
    rng = np.random.default_rng(seed)
    traj = simulate(draw, rng, end_year=2026 + T - 1)
    log_x = np.stack([np.log(traj.x[s]) for s in STATES])  # (n_s, T, n_j)
    log_Y = np.stack([np.log(traj.Y[s][:, :2]) for s in STATES])  # (n_s, T, 2)

    z_anchor, z_biased, z_capability, lam, b = _measure(log_x, log_Y, rng)
    truth = {
        "sigma_D": draw.sigma_D,
        "sigma_F": draw.sigma_F,
        "delta": draw.delta,
        "rho_g": draw.rho_g,
        "sigma_top0": draw.sigma_top0,
        "lam": lam,
        "b_anchored": b[:, :3],
        "gstar": np.stack([draw.gstar[s] for s in STATES]),
        # AI intensity is unobserved in synthetic scope; these truths exist so
        # the recovery report can show how little the data inform them.
        "gstar_ai": np.array([draw.gstar_ai[s] for s in STATES]),
        "sigma_ai": draw.sigma_ai,
    }
    return SyntheticData(z_anchor, z_biased, z_capability, truth)


def make_sbc_synthetic(T: int, seed: int) -> SyntheticData:
    """Generate one SBC replication: truth drawn from EXACTLY the model prior.

    Registered in ``model/ESTIMATION-SYNTHETIC-RUN-003.md`` section 4:
    ``make_synthetic`` fixes x0/g0/g_ai0 while the model samples them, which is
    SBC-invalidating. This generator samples every initial state from the
    Amendment 2/3 priors and runs the model's own recursion in numpy
    (cross-implementation is preserved -- parameters come from the numpy
    ``sample_prior`` and the CES aggregation is the numpy ``ces``).
    ``prior_predictive.simulate`` is deliberately NOT touched: its frozen init
    conventions are the gates' record and the PP3 regression baseline.
    """
    rng = np.random.default_rng(seed)
    draw = sample_prior(rng)
    n_s, n_j = len(STATES), len(INPUTS)
    baseline = np.array([[SYNTHETIC_BASELINE[s][j] for j in INPUTS] for s in STATES])
    x0_sd = np.array(X0_PRIOR_SD)
    gstar = np.stack([draw.gstar[s] for s in STATES])
    stationary_scale = np.sqrt(max(1.0 - draw.rho_g**2, 1e-4))  # model's clamp, exactly

    log_x = np.zeros((n_s, T, n_j))
    log_x[:, 0, :] = rng.normal(np.log(baseline), x0_sd[None, :])
    g = rng.normal(gstar, draw.sigma_v / stationary_scale)  # stationary g0
    xbar = np.stack([draw.xbar[s] for s in STATES])
    for t in range(1, T):
        g = (
            draw.rho_g * g
            + (1.0 - draw.rho_g) * gstar
            + rng.normal(0.0, draw.sigma_v, size=(n_s, n_j))
        )
        drag = draw.kappa[None, :] * np.exp(
            draw.phi[None, :] * (log_x[:, t - 1, :] - np.log(xbar))
        )
        log_x[:, t, :] = np.clip(
            log_x[:, t - 1, :]
            + g
            - drag
            + rng.normal(0.0, draw.sigma_u, size=(n_s, n_j)),
            -30.0,
            30.0,
        )

    # AI latent, stationary g_ai0, same recursion as the model.
    gstar_ai = np.array([draw.gstar_ai[s] for s in STATES])
    g_ai = rng.normal(gstar_ai, draw.sigma_ai / stationary_scale)
    log1p_ai = np.zeros((n_s, T))
    for t in range(1, T):
        g_ai = (
            draw.rho_g * g_ai
            + (1.0 - draw.rho_g) * gstar_ai
            + rng.normal(0.0, draw.sigma_ai, size=n_s)
        )
        log1p_ai[:, t] = log1p_ai[:, t - 1] + g_ai
    mean_log1p_ai = log1p_ai.mean(axis=0)

    span = PriorDraw.SIGMA_TOP_MAX - PriorDraw.SIGMA_TOP_MIN
    p0 = np.clip((draw.sigma_top0 - PriorDraw.SIGMA_TOP_MIN) / span, 1e-4, 1 - 1e-4)
    ls = np.empty(T)
    ls[0] = np.log(p0 / (1 - p0))
    z_w = rng.normal(0.0, draw.tau, size=T - 1)
    for t in range(1, T):
        ls[t] = ls[t - 1] + draw.delta * (mean_log1p_ai[t] - mean_log1p_ai[t - 1]) + z_w[t - 1]
    sigma_top = PriorDraw.SIGMA_TOP_MIN + span / (1.0 + np.exp(-ls))

    x = np.exp(log_x)
    log_Y = np.zeros((n_s, T, 2))
    for i in range(n_s):
        for t in range(T):
            q_d = ces(x[i, t, :3], draw.alpha_D, draw.sigma_D)
            q_f = ces(x[i, t, 3:], draw.alpha_F, draw.sigma_F)
            for m, weight in enumerate(draw.w[:2]):
                log_Y[i, t, m] = np.log(
                    max(
                        ces(
                            np.array([q_d, q_f]),
                            np.array([weight, 1.0 - weight]),
                            sigma_top[t],
                        ),
                        1e-12,
                    )
                )

    z_anchor, z_biased, z_capability, lam, b = _measure(log_x, log_Y, rng)
    truth = {
        "sigma_D": draw.sigma_D,
        "sigma_F": draw.sigma_F,
        "delta": draw.delta,
        "rho_g": draw.rho_g,
        "sigma_top0": draw.sigma_top0,
        "sigma_u": draw.sigma_u,
        "sigma_v": draw.sigma_v,
        "sigma_ai": draw.sigma_ai,
        "lam": lam,
        "b_anchored": b[:, :3],
        "gstar": gstar,
        "gstar_ai": gstar_ai,
    }
    return SyntheticData(z_anchor, z_biased, z_capability, truth)


# ---------------------------------------------------------------------------
# Fit and diagnostics
# ---------------------------------------------------------------------------


def fit(
    data: SyntheticData,
    T: int,
    *,
    seed: int,
    num_warmup: int = 500,
    num_samples: int = 500,
    num_chains: int = 4,
    target_accept: float = 0.9,
) -> MCMC:
    # init_to_sample rather than the default init_to_uniform: a uniform
    # unconstrained init can place xbar below the current level, at which point
    # the saturation drag exp(phi * (log x - log xbar)) saturates the log-path
    # clip and its zero gradient strands the chain at its starting point.
    kernel = NUTS(
        model, target_accept_prob=target_accept, init_strategy=init_to_sample
    )
    mcmc = MCMC(
        kernel,
        num_warmup=num_warmup,
        num_samples=num_samples,
        num_chains=num_chains,
        chain_method="sequential",
        progress_bar=False,
    )
    mcmc.run(
        jax.random.PRNGKey(seed),
        T=T,
        z_anchor=jnp.asarray(data.z_anchor),
        z_biased=jnp.asarray(data.z_biased),
        z_capability=jnp.asarray(data.z_capability),
        extra_fields=("diverging",),
    )
    return mcmc


def diagnostics(mcmc: MCMC) -> dict[str, object]:
    """Convergence per SPECIFICATION.md section 10, plus recovery inputs."""
    from numpyro.diagnostics import summary

    samples = mcmc.get_samples(group_by_chain=True)
    stats = summary(samples, prob=0.9)
    worst_rhat, worst_name = 0.0, ""
    min_ess = float("inf")
    for name, s in stats.items():
        r = float(np.max(s["r_hat"]))
        if r > worst_rhat:
            worst_rhat, worst_name = r, name
        min_ess = min(min_ess, float(np.min(s["n_eff"])))
    divergences = int(np.sum(mcmc.get_extra_fields()["diverging"]))
    return {
        "worst_rhat": worst_rhat,
        "worst_rhat_param": worst_name,
        "min_ess": min_ess,
        "divergences": divergences,
        "anchor_absent": list(ANCHOR_ABSENT),
    }


def recovery_report(mcmc: MCMC, truth: dict[str, object], prob: float = 0.9) -> dict:
    """Is each named truth inside its central posterior interval?"""
    samples = mcmc.get_samples()
    lo_q, hi_q = (1 - prob) / 2, 1 - (1 - prob) / 2
    out = {}
    for name, true_val in truth.items():
        if name not in samples:
            continue
        s = np.asarray(samples[name])
        lo = np.quantile(s, lo_q, axis=0)
        hi = np.quantile(s, hi_q, axis=0)
        t = np.asarray(true_val)
        out[name] = {
            "covered": bool(np.all((t >= lo) & (t <= hi))),
            "n_outside": int(np.sum((t < lo) | (t > hi))),
            "n_total": int(t.size),
        }
    return out
