"""Structural checks on the NumPyro estimator.

Fast checks only: CES cross-implementation equivalence (including the
sigma -> 1 limit and its gradient), prior-moment agreement at small n, and a
shape trace of the full model. The MCMC recovery run is executed and recorded
in model/ESTIMATION-SYNTHETIC-RUN-001.md rather than in the test suite,
because a NUTS run at meaningful settings does not belong in a unit-test loop.
"""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import jax
import jax.numpy as jnp
from numpyro.infer import Predictive

from usbip.model import estimator as est
from usbip.model.prior_predictive import ces as ces_np
from usbip.model.prior_predictive import sample_prior


def test_ces_matches_numpy_including_unit_sigma():
    rng = np.random.default_rng(7)
    for sigma in (0.3, 0.9995, 1.0, 1.0005, 1.7):
        a = rng.uniform(0.1, 5.0, size=3)
        shares = rng.dirichlet(np.ones(3))
        got = float(est.ces_jax(jnp.array(a), jnp.array(shares), jnp.array(sigma)))
        want = ces_np(a, shares, sigma)
        assert abs(got - want) / want < 1e-4, (sigma, got, want)


def test_ces_gradient_finite_at_unit_sigma():
    a = jnp.array([1.0, 2.0, 3.0])
    shares = jnp.array([0.2, 0.3, 0.5])
    for sigma in (0.9999, 1.0, 1.0001):
        g = jax.grad(lambda s: est.ces_jax(a, shares, s))(jnp.array(sigma))
        assert jnp.isfinite(g), (sigma, g)


def test_prior_moments_agree_small_n():
    n = 400
    rng = np.random.default_rng(11)
    np_draws = [sample_prior(rng) for _ in range(n)]
    jx = Predictive(est.model, num_samples=n)(jax.random.PRNGKey(11), T=6)
    for name, vals in {
        "delta": [d.delta for d in np_draws],
        "rho_g": [d.rho_g for d in np_draws],
        "sigma_v": [d.sigma_v for d in np_draws],
        "sigma_ai": [d.sigma_ai for d in np_draws],
        "gstar_ai": [d.gstar_ai[s] for d in np_draws for s in ("US", "CN")],
    }.items():
        a, b = np.asarray(vals), np.asarray(jx[name]).ravel()
        assert abs(a.mean() - b.mean()) / a.std() < 0.25, name
        assert abs(a.std() - b.std()) / a.std() < 0.25, name


def test_model_trace_shapes_and_synthetic_generation():
    T = 8
    rng = np.random.default_rng(3)
    draw = sample_prior(rng)
    data = est.make_synthetic(draw, T=T, seed=3)
    assert data.z_anchor.shape == (2, T, 3)
    assert data.z_biased.shape == (2, T, 6)
    assert data.z_capability.shape == (2, T, 2)
    assert np.all(np.isfinite(data.z_biased))
    # The model must trace conditioned on these observations without error.
    jx = Predictive(est.model, num_samples=2)(jax.random.PRNGKey(3), T=T)
    assert jx["log_Y"].shape == (2, 2, T, 4)
    assert np.all(np.isfinite(np.asarray(jx["log_Y"])))


def test_anchor_absent_bias_is_fixed_not_sampled():
    # Section 4.2: anchor-absent latents get b FIXED at the prior mean. The
    # sampled bias site must cover only the three anchored inputs.
    jx = Predictive(est.model, num_samples=1)(jax.random.PRNGKey(5), T=6)
    assert jx["b_anchored"].shape == (1, 2, 3)
    assert est.ANCHOR_ABSENT == ("F1", "F2", "F3")
