"""Prior-predictive gates PP1-PP5.

Executable implementation of the five checks in ``model/IDENTIFICATION.md``
section 6. Failure of any one blocks estimation.

This module deliberately touches no observed data. It samples from the priors
committed in ``model/PRIORS.md``, pushes the draws through the structure
committed in ``model/SPECIFICATION.md``, classifies the resulting trajectories
into the five regimes, and asks whether the structure behaves acceptably before
it has seen anything.

The point of running these before estimation is that they can fail. PP4 in
particular is the mechanical implementation of the first standing prohibition:
it tests whether even-handedness is a property of the code rather than a
statement in a README.

Determinism: every sampler call takes an explicit seed and the module holds no
module-level random state. Two runs at the same seed produce identical output.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Mapping

import numpy as np

# Input ordering, fixed by SPECIFICATION.md section 5.
DEPLOYMENT = ("D1", "D2", "D3")
FRONTIER = ("F1", "F2", "F3")
INPUTS = DEPLOYMENT + FRONTIER

# Capability vector ordering, fixed by README.md and restated in
# SPECIFICATION.md section 2.
ELEMENTS = ("Y_throughput", "Y_frontier", "Y_net", "Y_fin")

STATES = ("US", "CN")

BASE_YEAR = 2026
HORIZONS = (2030, 2040, 2050, 2075)

# Synthetic asymmetric baseline, in arbitrary normalised units.
#
# NOT DATA. These values exist only so that PP4 has something asymmetric to
# swap; a prior-predictive run against a symmetric baseline would satisfy the
# symmetry test vacuously. The asymmetry direction is taken from the qualitative
# pattern in the baseline falsifier log -- PRC ahead on deployment inputs, US
# ahead on frontier compute -- and the magnitudes are round numbers, not
# estimates. Estimation reads data/derived/ and never this table.
SYNTHETIC_BASELINE: dict[str, dict[str, float]] = {
    "US": {"D1": 1.00, "D2": 1.00, "D3": 1.00, "F1": 1.00, "F2": 1.00, "F3": 1.00},
    "CN": {"D1": 2.50, "D2": 2.00, "D3": 3.00, "F1": 0.20, "F2": 0.80, "F3": 1.50},
}

# PP3 plausibility ceiling: multiple of the 2026 level that a single input may
# not exceed by 2050. Twenty-four years at a sustained 8 percent compound rate
# is roughly 6.3x, which no national generation fleet has ever done at scale;
# 20x is therefore a generous ceiling chosen to catch structural runaway rather
# than to encode a growth forecast.
PP3_CEILING_2050 = 20.0

# Engineering ceiling estimates, as multiples of each state's 2026 baseline
# level for that input. PRIORS.md commits xbar[j,i] ~ LogNormal(log(engineering
# ceiling estimate), 0.6) but does not table the ceilings, so they are declared
# here and inherit that file's own verdict on them: these are the least
# defensible numbers in the project, they are educated guesses about grid
# interconnection limits, plausible robot-density saturation, and thermal and
# land constraints, and they carry mandatory sensitivity run S6.
#
# They are lower for the deployment bundle than the frontier bundle because
# physical build-out faces siting and interconnection limits that capital depth
# and human capital do not.
ENGINEERING_CEILING_MULTIPLE = {
    "D1": 4.0,
    "D2": 4.0,
    "D3": 5.0,
    "F1": 8.0,
    "F2": 6.0,
    "F3": 3.0,
}

# Deadband on log relative change, below which an element is treated as having
# no directional movement. Arbitrary, and labelled arbitrary: it is a
# classification convenience, not a substantive claim, and PP results are
# reported alongside it.
DEADBAND = 0.10

# Reversal depth for the peaking regime: the challenger's relative position must
# fall by at least this much in logs from its within-window peak.
REVERSAL_DEPTH = 0.15

# Dual-constraint trigger: both states' primary capability element growing at
# less than this multiple of its own unconstrained-trend counterfactual.
CONSTRAINT_RATIO = 0.60


# ---------------------------------------------------------------------------
# Priors, transcribed from model/PRIORS.md
# ---------------------------------------------------------------------------


# Growth-innovation scale hyperparameter, PRIORS.md Amendment 1. Derived by the
# procedure committed there BEFORE computation: pooled AR(1) residual scale of
# log capacity growth, both states, 2002-2025, from the snapshotted Ember series
# (sha256 259e1095...). Per-state residual SDs 0.0247 (CN) and 0.0109 (US);
# pooled 0.0191 to three significant figures. Not a tuning parameter: changing
# it requires re-running the committed procedure on new snapshotted data.
S_V = 0.0191


@dataclass(frozen=True)
class PriorDraw:
    sigma_D: float
    sigma_F: float
    sigma_top0: float
    delta: float
    tau: float
    alpha_D: np.ndarray  # CES shares within the deployment bundle
    alpha_F: np.ndarray
    w: np.ndarray  # element weights on Q_D, shape (4,)
    kappa: np.ndarray  # saturation strength per input
    phi: np.ndarray  # saturation sharpness per input
    xbar: dict[str, np.ndarray]  # saturation scale per state per input
    gstar: dict[str, np.ndarray]  # long-run growth per state per input
    rho_g: float
    psi: dict[str, np.ndarray]
    ai_intensity_growth: float
    sigma_u: float = 0.01
    sigma_v: float = 0.01

    SIGMA_TOP_MIN = 0.15
    SIGMA_TOP_MAX = 2.50


def sample_prior(rng: np.random.Generator) -> PriorDraw:
    """One draw from the joint prior in model/PRIORS.md.

    Every distribution here is the one committed in that file. Where PRIORS.md
    fixes a bound, the bound is enforced by truncation rather than by clipping
    after the fact, because clipping piles prior mass on the boundary.
    """
    sigma_D = float(rng.lognormal(np.log(0.5), 0.45))
    sigma_F = float(rng.lognormal(np.log(0.7), 0.50))

    # sigma_top[2026] ~ LogNormal(log 0.6, 0.55), bounded to [0.15, 2.5].
    for _ in range(64):
        s0 = float(rng.lognormal(np.log(0.6), 0.55))
        if PriorDraw.SIGMA_TOP_MIN <= s0 <= PriorDraw.SIGMA_TOP_MAX:
            break
    else:  # pragma: no cover - truncation failure would be a prior defect
        raise RuntimeError("sigma_top initial-state truncation failed to accept")

    # delta ~ Normal(0, 0.25). Centred at exactly zero. An asymmetric prior here
    # would place prior mass on the project's own hypothesis.
    delta = float(rng.normal(0.0, 0.25))

    return PriorDraw(
        sigma_D=sigma_D,
        sigma_F=sigma_F,
        sigma_top0=s0,
        delta=delta,
        tau=float(abs(rng.normal(0.0, 0.05))),
        alpha_D=rng.dirichlet(np.ones(3) * 4.0),
        alpha_F=rng.dirichlet(np.ones(3) * 4.0),
        # Element weights on the deployment aggregate. Ordering constraint from
        # SPECIFICATION.md 6.1: throughput loads primarily on Q_D, frontier
        # primarily on Q_F, the other two in between. Enforced by construction
        # so the constraint cannot be violated by a draw.
        w=np.array(
            [
                float(rng.uniform(0.60, 0.90)),  # Y_throughput
                float(rng.uniform(0.10, 0.40)),  # Y_frontier
                float(rng.uniform(0.35, 0.65)),  # Y_net
                float(rng.uniform(0.30, 0.60)),  # Y_fin
            ]
        ),
        # kappa ~ HalfNormal(0.05), phi ~ Gamma(2, 1), exactly as PRIORS.md
        # section 4 commits them. Run 001 and 002 used uniform surrogates,
        # which truncated the kappa tail at 0.06 and so understated the
        # attainable saturation drag. Recorded in PRIOR-PREDICTIVE-RUN-001.md.
        kappa=np.abs(rng.normal(0.0, 0.05, size=len(INPUTS))),
        phi=rng.gamma(2.0, 1.0, size=len(INPUTS)),
        xbar={
            s: np.array(
                [
                    rng.lognormal(
                        np.log(
                            ENGINEERING_CEILING_MULTIPLE[j] * SYNTHETIC_BASELINE[s][j]
                        ),
                        0.6,
                    )
                    for j in INPUTS
                ]
            )
            for s in STATES
        },
        gstar={s: rng.normal(0.02, 0.02, size=len(INPUTS)) for s in STATES},
        rho_g=float(rng.beta(6.0, 2.0)),  # centred near 0.75, per PRIORS.md
        # psi ~ Normal(0, 0.10), sign-free, scale kept small because the PSI
        # literature supports roughly 18 percent of variance explained.
        psi={s: rng.normal(0.0, 0.10, size=len(INPUTS)) for s in STATES},
        ai_intensity_growth=float(abs(rng.normal(0.03, 0.02))),
        # u ~ Normal(0, sigma_u^2), sigma_u ~ HalfNormal(0.05): level innovation,
        # unchanged. v ~ Normal(0, sigma_v^2), sigma_v ~ HalfNormal(S_V): growth
        # innovation, own scale per PRIORS.md Amendment 1. Runs 001-003 shared
        # one scale across both streams; the growth stream compounding under
        # rho_g produced the PP3 runaway recorded in PRIOR-PREDICTIVE-RUN-001.md.
        sigma_u=float(abs(rng.normal(0.0, 0.05))),
        sigma_v=float(abs(rng.normal(0.0, S_V))),
    )


# ---------------------------------------------------------------------------
# Structure, transcribed from model/SPECIFICATION.md sections 5 and 6
# ---------------------------------------------------------------------------


def ces(a: np.ndarray, shares: np.ndarray, sigma: float) -> float:
    """CES aggregate. ``sigma -> 1`` degenerates to Cobb-Douglas.

    The limit is handled explicitly because ``r = (sigma-1)/sigma`` is zero at
    unit elasticity and the power form is undefined there. A draw landing near
    1.0 is not rare under the committed priors, so this branch is load-bearing
    rather than defensive.
    """
    if abs(sigma - 1.0) < 1e-6:
        return float(np.exp(np.sum(shares * np.log(np.maximum(a, 1e-12)))))
    r = (sigma - 1.0) / sigma
    return float(np.sum(shares * np.maximum(a, 1e-12) ** r) ** (1.0 / r))


def inv_logit(x: float) -> float:
    return 1.0 / (1.0 + np.exp(-x))


def logit(p: float) -> float:
    return float(np.log(p / (1.0 - p)))


@dataclass
class Trajectory:
    years: np.ndarray
    x: dict[str, np.ndarray]  # state -> (n_years, n_inputs)
    Y: dict[str, np.ndarray]  # state -> (n_years, 4)
    sigma_top: np.ndarray
    unconstrained_Y: dict[str, np.ndarray]


@dataclass(frozen=True)
class Shocks:
    """Pre-drawn shock streams, held separately from the sampler.

    Separation exists so that a state swap can be made EXACT. PP4 compares a
    world against its mirror image; if the two runs consume different random
    numbers, the comparison measures Monte Carlo noise as well as asymmetry, and
    at any feasible draw count the noise dominates. With paired shocks the
    expected deviation is zero to floating-point precision, so any deviation at
    all is structural. Run 001 made this mistake and PP4 failed on noise.
    """

    growth: dict[str, np.ndarray]  # state -> (n_years, n_inputs)
    level: dict[str, np.ndarray]
    sigma_top: np.ndarray

    def mirrored(self) -> "Shocks":
        return Shocks(
            growth={"US": self.growth["CN"], "CN": self.growth["US"]},
            level={"US": self.level["CN"], "CN": self.level["US"]},
            sigma_top=self.sigma_top,
        )


def sample_shocks(
    rng: np.random.Generator,
    n_years: int,
    tau: float,
    sigma_u: float = 0.01,
    sigma_v: float = 0.01,
) -> Shocks:
    n_j = len(INPUTS)
    return Shocks(
        growth={s: rng.normal(0.0, sigma_v, size=(n_years, n_j)) for s in STATES},
        level={s: rng.normal(0.0, sigma_u, size=(n_years, n_j)) for s in STATES},
        sigma_top=rng.normal(0.0, tau, size=n_years),
    )


def mirror_draw(draw: PriorDraw) -> PriorDraw:
    """Exchange every state-indexed parameter between the two states.

    A data swap alone is not a mirror image: it would leave each state's own
    growth, ceiling and stress-feedback parameters attached to the other state's
    data. The mirror has to exchange both.
    """
    from dataclasses import replace as _replace

    return _replace(
        draw,
        xbar={"US": draw.xbar["CN"], "CN": draw.xbar["US"]},
        gstar={"US": draw.gstar["CN"], "CN": draw.gstar["US"]},
        psi={"US": draw.psi["CN"], "CN": draw.psi["US"]},
    )


def simulate(
    draw: PriorDraw,
    rng: np.random.Generator | None = None,
    *,
    baseline: Mapping[str, Mapping[str, float]] = SYNTHETIC_BASELINE,
    end_year: int = 2075,
    stress: Mapping[str, float] | None = None,
    shocks: Shocks | None = None,
) -> Trajectory:
    """Push one prior draw through Blocks E and P.

    Block M is not simulated here. The prior predictive concerns whether the
    structural core can produce all five regimes and behaves symmetrically;
    adding measurement noise would widen every distribution without changing
    which regimes are reachable, and would make PP4 harder to interpret.

    ``unconstrained_Y`` re-runs the same draw with the saturation term switched
    off. PP-level detection of the dual-constraint regime needs a counterfactual
    to compare against, and a state's own unconstrained trajectory is the only
    counterfactual available that does not import the other state's parameters.
    """
    years = np.arange(BASE_YEAR, end_year + 1)
    n_t, n_j = len(years), len(INPUTS)
    stress = stress or {s: 0.0 for s in STATES}
    if shocks is None:
        if rng is None:
            raise ValueError("simulate requires either an rng or pre-drawn shocks")
        shocks = sample_shocks(rng, n_t, draw.tau, draw.sigma_u, draw.sigma_v)

    x: dict[str, np.ndarray] = {}
    xu: dict[str, np.ndarray] = {}
    for s in STATES:
        x0 = np.array([baseline[s][j] for j in INPUTS], dtype=float)
        for target, saturating in ((x, True), (xu, False)):
            path = np.zeros((n_t, n_j))
            path[0] = x0
            g = draw.gstar[s].copy()
            for t in range(1, n_t):
                gstar_t = draw.gstar[s] + draw.psi[s] * stress[s]
                g = draw.rho_g * g + (1.0 - draw.rho_g) * gstar_t
                g = g + shocks.growth[s][t]
                drag = (
                    draw.kappa * (path[t - 1] / draw.xbar[s]) ** draw.phi
                    if saturating
                    else 0.0
                )
                log_next = np.log(path[t - 1]) + g - drag + shocks.level[s][t]
                path[t] = np.exp(np.clip(log_next, -30.0, 30.0))
            target[s] = path

    # sigma_top[t] transition. AI intensity is a normalised latent scalar
    # growing from a common base; it is deliberately not measured from any
    # AI-exposure occupation index, per SPECIFICATION.md section 7.
    ai = np.exp(draw.ai_intensity_growth * (years - BASE_YEAR)) - 1.0
    span = PriorDraw.SIGMA_TOP_MAX - PriorDraw.SIGMA_TOP_MIN
    p0 = (draw.sigma_top0 - PriorDraw.SIGMA_TOP_MIN) / span
    ls = np.zeros(n_t)
    ls[0] = logit(min(max(p0, 1e-4), 1 - 1e-4))
    for t in range(1, n_t):
        ls[t] = ls[t - 1] + draw.delta * (ai[t] - ai[t - 1]) + shocks.sigma_top[t]
    sigma_top = PriorDraw.SIGMA_TOP_MIN + span * np.array([inv_logit(v) for v in ls])

    def capability(path: np.ndarray) -> np.ndarray:
        out = np.zeros((n_t, len(ELEMENTS)))
        for t in range(n_t):
            q_d = ces(path[t, :3], draw.alpha_D, draw.sigma_D)
            q_f = ces(path[t, 3:], draw.alpha_F, draw.sigma_F)
            for m, weight in enumerate(draw.w):
                out[t, m] = ces(
                    np.array([q_d, q_f]),
                    np.array([weight, 1.0 - weight]),
                    sigma_top[t],
                )
        return out

    return Trajectory(
        years=years,
        x=x,
        Y={s: capability(x[s]) for s in STATES},
        sigma_top=sigma_top,
        unconstrained_Y={s: capability(xu[s]) for s in STATES},
    )


# ---------------------------------------------------------------------------
# Regime classification -- rule R009
# ---------------------------------------------------------------------------

R009_ID, R009_VERSION = "R009", "1.0.0"


def classify(
    traj: Trajectory,
    horizon: int,
    *,
    deadband: float = DEADBAND,
    reversal_depth: float = REVERSAL_DEPTH,
    constraint_ratio: float = CONSTRAINT_RATIO,
) -> str:
    """Map one simulated trajectory to one of R1..R5. Rule R009.

    The classifier is **state-swap equivariant**, which is the property PP4
    tests. Two consequences follow, and both are commitments rather than
    implementation details:

    1. ``R3`` is defined as **challenger peaking**, where the challenger is
       whichever state is gaining relative position in the first third of the
       window. SPECIFICATION.md names ``R3`` "PRC peaking". Under a state swap
       that label would have to become "US peaking", which is not in the regime
       set, so the label would break equivariance while the concept does not.
       The generic definition is adopted and the PRC reading is recovered by
       noting which state is the challenger in the actual data.
    2. Priority order is fixed and is applied before any tie-breaking:
       ``R5`` (both constrained), then ``R3`` (reversal), then ``R4`` (split by
       domain), then ``R1``/``R2`` (concentration). The order matters -- a
       trajectory can satisfy more than one test -- and reported regime masses
       are conditional on it. Reordering the priority would change the masses,
       so the order is frozen here and any change is a major version bump.
    """
    t_idx = int(np.searchsorted(traj.years, horizon))
    if t_idx >= len(traj.years):
        raise ValueError(f"horizon {horizon} beyond simulated window")

    # Relative position by element, in logs, as change from the base year.
    rel = np.log(traj.Y["CN"][:, :] / traj.Y["US"][:, :])
    move = rel[t_idx] - rel[0]

    # R5 first. Both states materially below their own unconstrained
    # counterfactual on the primary element.
    ratio = {
        s: float(
            traj.Y[s][t_idx, 0] / max(traj.unconstrained_Y[s][t_idx, 0], 1e-12)
        )
        for s in STATES
    }
    if all(ratio[s] < constraint_ratio for s in STATES):
        return "R5"

    # R3. The challenger gains early, then gives back at least REVERSAL_DEPTH in
    # logs from its within-window peak. Measured on the mean across elements so
    # a reversal on one element alone does not qualify.
    third = max(2, t_idx // 3)
    early = float(np.mean(rel[third] - rel[0]))
    mean_rel = np.mean(rel[: t_idx + 1], axis=1)
    if abs(early) > deadband:
        sign = 1.0 if early > 0 else -1.0
        signed = sign * mean_rel
        peak = int(np.argmax(signed))
        if peak < t_idx and (signed[peak] - signed[t_idx]) >= reversal_depth:
            return "R3"

    # R4. Divergence by domain: at least one element beyond the deadband in each
    # direction, so no single hierarchy holds across the vector.
    if np.any(move > deadband) and np.any(move < -deadband):
        return "R4"

    # R1 / R2. Concentration in one direction. Elements inside the deadband do
    # not block concentration: a flat element establishes no competing
    # hierarchy, so partial one-directional movement is concentration, not
    # segmentation.
    #
    # Run 001 assigned this case to R4 and PP2 failed as a direct result -- R4
    # became a sink that could not fall below 0.2 under any admissible baseline.
    # See PRIOR-PREDICTIVE-RUN-001.md.
    if np.any(move > deadband):
        return "R1"
    if np.any(move < -deadband):
        return "R2"

    # Nothing moved beyond the deadband in either direction. This is not
    # segmentation and it is not concentration; it is the absence of material
    # relative change. It gets its own bucket rather than being folded into a
    # substantive regime.
    return "R0_no_material_change"


# ---------------------------------------------------------------------------
# The five gates
# ---------------------------------------------------------------------------


@dataclass
class GateResult:
    gate: str
    passed: bool
    detail: str
    values: dict[str, object] = field(default_factory=dict)

    def __str__(self) -> str:
        return f"{self.gate}: {'PASS' if self.passed else 'FAIL'} -- {self.detail}"


def regime_masses(
    n_draws: int,
    seed: int,
    *,
    horizon: int = 2050,
    baseline: Mapping[str, Mapping[str, float]] = SYNTHETIC_BASELINE,
) -> dict[str, float]:
    """Prior-predictive regime masses at one horizon."""
    rng = np.random.default_rng(seed)
    counts = dict.fromkeys(
        ("R1", "R2", "R3", "R4", "R5", "R0_no_material_change"), 0
    )
    for _ in range(n_draws):
        draw = sample_prior(rng)
        traj = simulate(draw, rng, baseline=baseline)
        counts[classify(traj, horizon)] += 1
    return {k: v / n_draws for k, v in counts.items()}


def swap_baseline(
    baseline: Mapping[str, Mapping[str, float]]
) -> dict[str, dict[str, float]]:
    return {"US": dict(baseline["CN"]), "CN": dict(baseline["US"])}


# Earliest horizon at which the output contract claims each regime.
# SPECIFICATION.md Amendment 02: R5 is reported at 2075 only; R1..R4 at 2050.
# PP1 checks coverage where the claim is made (IDENTIFICATION.md Amendment 1).
PP1_CLAIM_HORIZON = {"R1": 2050, "R2": 2050, "R3": 2050, "R4": 2050, "R5": 2075}


def pp1_regime_coverage(n_draws: int, seed: int) -> GateResult:
    """Each regime must have >= 0.05 prior mass at its earliest claimed horizon."""
    masses = {
        h: regime_masses(n_draws, seed, horizon=h)
        for h in sorted(set(PP1_CLAIM_HORIZON.values()))
    }
    # The no-material-change bucket is not a regime and is exempt from the
    # coverage floor. It is reported so that it cannot quietly absorb draws.
    starved = {
        f"{k}@{h}": masses[h][k]
        for k, h in PP1_CLAIM_HORIZON.items()
        if masses[h][k] < 0.05
    }
    return GateResult(
        "PP1",
        not starved,
        (
            f"all five regimes reachable at their claimed horizons; masses {masses}"
            if not starved
            else f"regimes below 0.05 prior mass at their claimed horizon: {starved}"
        ),
        {"masses": masses},
    )


def pp2_r4_refutability(n_draws: int, seed: int) -> GateResult:
    """R4 must be able to receive mass below 0.2 for some admissible data.

    The demand in SPECIFICATION.md section 1: a specification under which R4
    cannot receive posterior mass below 0.2 for ANY admissible data is
    misspecified and must be rejected. Tested by sweeping baselines that are
    admissible but hostile to segmentation -- near-parity, and strong
    single-direction leads -- and asking whether any drives R4 mass below the
    bar.
    """
    parity = {s: dict.fromkeys(INPUTS, 1.0) for s in STATES}
    cn_dominant = {
        "US": dict.fromkeys(INPUTS, 1.0),
        "CN": {j: 3.0 for j in INPUTS},
    }
    us_dominant = swap_baseline(cn_dominant)
    candidates = {
        "parity": parity,
        "cn_dominant_all_inputs": cn_dominant,
        "us_dominant_all_inputs": us_dominant,
    }
    results = {
        name: regime_masses(n_draws, seed, baseline=b)["R4"]
        for name, b in candidates.items()
    }
    achieved = min(results.values())
    return GateResult(
        "PP2",
        achieved < 0.2,
        (
            f"R4 reaches mass {achieved:.3f} under the most hostile admissible "
            f"baseline, so R4 is refutable"
            if achieved < 0.2
            else f"R4 never falls below 0.2 across admissible baselines "
            f"({results}); the specification asserts its own conclusion and "
            f"must be rejected"
        ),
        {"by_baseline": results},
    )


def pp3_trajectory_sanity(n_draws: int, seed: int) -> GateResult:
    """No prior-predictive input path may exceed the 2050 plausibility ceiling."""
    rng = np.random.default_rng(seed)
    worst, worst_where = 0.0, ""
    breaches = 0
    idx_2050 = 2050 - BASE_YEAR
    for _ in range(n_draws):
        draw = sample_prior(rng)
        traj = simulate(draw, rng)
        for s in STATES:
            mult = traj.x[s][idx_2050] / traj.x[s][0]
            top = float(np.max(mult))
            if top > worst:
                worst, worst_where = top, f"{s}/{INPUTS[int(np.argmax(mult))]}"
            if top > PP3_CEILING_2050:
                breaches += 1
                break
    rate = breaches / n_draws
    # A ceiling breach in a small tail is expected from a diffuse growth prior
    # and is not itself a defect; a systematic breach is. The 2 percent bar is
    # arbitrary and labelled arbitrary.
    return GateResult(
        "PP3",
        rate <= 0.02,
        f"max 2050 input multiple {worst:.1f}x ({worst_where}); "
        f"{rate:.1%} of draws breach the {PP3_CEILING_2050:.0f}x ceiling",
        {"breach_rate": rate, "worst_multiple": worst},
    )


def pp4_symmetry(n_draws: int, seed: int, *, tolerance: float = 0.05) -> GateResult:
    """Swapping the two states' data must produce mirror-image regime posteriors.

    The mechanical implementation of the first standing prohibition. R1 and R2
    must exchange, and R3, R4 and R5 must be invariant. Asymmetry here means
    asymmetry was built into the structure, and the committed remedy in
    IDENTIFICATION.md is to rebuild rather than to adjust.
    """
    rng = np.random.default_rng(seed)
    keys = ("R1", "R2", "R3", "R4", "R5", "R0_no_material_change")
    base_counts = dict.fromkeys(keys, 0)
    swapped_counts = dict.fromkeys(keys, 0)
    mismatches: list[tuple[str, str]] = []
    horizon = 2050
    swapped_baseline = swap_baseline(SYNTHETIC_BASELINE)
    for _ in range(n_draws):
        draw = sample_prior(rng)
        shocks = sample_shocks(
            rng, 2075 - BASE_YEAR + 1, draw.tau, draw.sigma_u, draw.sigma_v
        )
        a = classify(simulate(draw, shocks=shocks), horizon)
        b = classify(
            simulate(
                mirror_draw(draw),
                baseline=swapped_baseline,
                shocks=shocks.mirrored(),
            ),
            horizon,
        )
        base_counts[a] += 1
        swapped_counts[b] += 1
        mirror_of_a = {"R1": "R2", "R2": "R1"}.get(a, a)
        if b != mirror_of_a:
            mismatches.append((a, b))
    base = {k: v / n_draws for k, v in base_counts.items()}
    swapped = {k: v / n_draws for k, v in swapped_counts.items()}
    expected = {
        "R1": swapped["R2"],
        "R2": swapped["R1"],
        "R3": swapped["R3"],
        "R4": swapped["R4"],
        "R5": swapped["R5"],
        "R0_no_material_change": swapped["R0_no_material_change"],
    }
    deviations = {k: abs(base[k] - expected[k]) for k in base}
    worst = max(deviations, key=deviations.get)
    # Paired shocks make the expected deviation exactly zero, so the tolerance
    # is a floating-point allowance rather than a noise budget. Draw-level
    # mismatches are reported because an aggregate that happens to balance is
    # not evidence of a symmetric classifier.
    ok = deviations[worst] <= tolerance and not mismatches
    return GateResult(
        "PP4",
        ok,
        (
            f"exact mirror on all {n_draws} paired draws; largest aggregate "
            f"deviation {deviations[worst]:.4f}"
            if ok
            else f"{len(mismatches)} of {n_draws} paired draws do not mirror "
            f"(e.g. {mismatches[:3]}); largest aggregate deviation "
            f"{deviations[worst]:.4f} on {worst}. Asymmetry is structural and "
            f"the committed remedy is to rebuild, not to adjust."
        ),
        {
            "base": base,
            "swapped": swapped,
            "deviations": deviations,
            "draw_level_mismatches": len(mismatches),
        },
    )


def pp5_declinism(n_draws: int, seed: int) -> GateResult:
    """No divergence regime may take above 0.5 prior mass absent informative data.

    A structure that reaches for divergence before it has seen anything would
    make its eventual divergence finding uninformative. Applied to R1 and R2
    alike; a prior-predictive lean toward US-favourable divergence would fail
    this gate on the same terms.
    """
    mass = regime_masses(n_draws, seed)
    offenders = {k: v for k, v in mass.items() if k in ("R1", "R2") and v > 0.5}
    return GateResult(
        "PP5",
        not offenders,
        (
            f"no divergence regime above 0.5 prior mass; R1={mass['R1']:.3f}, "
            f"R2={mass['R2']:.3f}"
            if not offenders
            else f"divergence regime(s) above 0.5 prior mass: {offenders}"
        ),
        {"masses": mass},
    )


GATES: dict[str, Callable[[int, int], GateResult]] = {
    "PP1": pp1_regime_coverage,
    "PP2": pp2_r4_refutability,
    "PP3": pp3_trajectory_sanity,
    "PP4": pp4_symmetry,
    "PP5": pp5_declinism,
}


def run_all(n_draws: int = 400, seed: int = 20260819) -> list[GateResult]:
    return [fn(n_draws, seed) for fn in GATES.values()]
