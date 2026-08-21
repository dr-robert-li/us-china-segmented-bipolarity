"""Two structural tests, both written because something got past the gates.

``TestRegistryMatchesDocumentation`` closes the class of defect that
``rules/README.md`` recorded in Phase 1: the schema referenced a rules registry
by ``rule_id`` and semver, and the registry did not exist. A registry that drifts
from its own documentation is the same failure in a quieter form.

``TestSamplerMatchesCommittedPriors`` closes defect C from
``model/PRIOR-PREDICTIVE-RUN-001.md``. Four priors were implemented as uniform
surrogates against the forms committed in ``PRIORS.md``. The error survived two
full prior-predictive runs and produced a plausible, quantitative, and false
diagnosis about a structural limitation of the model. None of PP1 to PP5 could
catch it, because every gate consumes the sampler's output and so inherits its
errors. The audit therefore has to compare the sampler against the committed
text, not against itself.

The test checks analytic moments rather than parsing prose. A moment check would
not catch every possible substitution -- two different families can share a mean
and a variance -- but it does catch the substitution that actually happened,
since a uniform surrogate chosen to span a plausible range does not reproduce the
committed family's moments.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

import numpy as np

from usbip import rules
from usbip.model import prior_predictive as pp

REPO = Path(__file__).resolve().parents[2]
N = 20_000
SEED = 20260819


class TestRegistryMatchesDocumentation(unittest.TestCase):
    def setUp(self) -> None:
        self.readme = (REPO / "pipeline" / "rules" / "README.md").read_text()

    def test_every_registered_rule_appears_in_the_readme_table(self) -> None:
        for rule_id, version in rules.REGISTERED.items():
            self.assertIn(
                rule_id, self.readme, f"{rule_id} is registered in code but not in README"
            )

    def test_every_readme_rule_is_registered_in_code(self) -> None:
        documented = set(re.findall(r"\bR0\d\d\b", self.readme))
        undocumented = documented - set(rules.REGISTERED)
        self.assertEqual(
            undocumented,
            set(),
            f"README documents {sorted(undocumented)} with no entry in rules.REGISTERED",
        )

    def test_every_registered_rule_has_a_specification_file(self) -> None:
        rules_dir = REPO / "pipeline" / "rules"
        specified = {m.group(0) for f in rules_dir.glob("R*.md") for m in [re.match(r"R0\d\d", f.name)] if m}
        missing = set(rules.REGISTERED) - specified
        # R001, R002 and R004 to R008 are specified inline in schema.md and the
        # adapter files rather than in standalone rule files. Only rules whose
        # parameters are sourced require their own file, per rules/README.md.
        self.assertTrue(
            {"R003", "R009"} <= specified,
            f"sourced-parameter rules must have standalone specifications; have {sorted(specified)}",
        )
        self.assertEqual(
            missing & {"R003", "R009"},
            set(),
            f"registered but unspecified: {sorted(missing)}",
        )

    def test_versions_are_semver(self) -> None:
        for rule_id, version in rules.REGISTERED.items():
            self.assertRegex(version, r"^\d+\.\d+\.\d+$", f"{rule_id}: {version!r}")

    def test_r009_is_registered(self) -> None:
        # Registered by amendment to SPECIFICATION.md during Phase 3.
        self.assertIn("R009", rules.REGISTERED)


class TestSamplerMatchesCommittedPriors(unittest.TestCase):
    """Empirical moments of the sampler against the analytic moments in PRIORS.md.

    Tolerances are loose enough that Monte Carlo error at n=20,000 will not trip
    them and tight enough to reject the surrogates that defect C actually used.
    Each case records the surrogate it is guarding against.
    """

    @classmethod
    def setUpClass(cls) -> None:
        rng = np.random.default_rng(SEED)
        cls.draws = [pp.sample_prior(rng) for _ in range(N)]

    def _scalar(self, attr: str) -> np.ndarray:
        return np.array([getattr(d, attr) for d in self.draws], dtype=float)

    def _vector(self, attr: str) -> np.ndarray:
        return np.concatenate([np.asarray(getattr(d, attr), dtype=float).ravel() for d in self.draws])

    def test_kappa_is_halfnormal_not_uniform(self) -> None:
        # kappa ~ HalfNormal(0.05): mean = 0.05*sqrt(2/pi) ~ 0.0399, unbounded above.
        # Surrogate guarded against: uniform(0, 0.06), mean 0.030, max 0.060.
        k = self._vector("kappa")
        self.assertAlmostEqual(k.mean(), 0.05 * np.sqrt(2 / np.pi), delta=0.002)
        self.assertGreater(
            k.max(), 0.06, "kappa must be unbounded above; a 0.06 cap is the run-002 defect"
        )
        self.assertGreaterEqual(k.min(), 0.0)

    def test_phi_is_gamma_not_uniform(self) -> None:
        # phi ~ Gamma(2, 1): mean 2, variance 2, positively skewed, unbounded.
        # Surrogate guarded against: uniform(1, 4), mean 2.5, variance 0.75.
        phi = self._vector("phi")
        self.assertAlmostEqual(phi.mean(), 2.0, delta=0.05)
        self.assertAlmostEqual(phi.var(), 2.0, delta=0.10)
        self.assertGreater(phi.max(), 4.0, "Gamma(2,1) has mass above 4")
        self.assertLess(phi.min(), 1.0, "Gamma(2,1) has mass below 1")

    def test_rho_g_is_beta_not_uniform(self) -> None:
        # rho_g ~ Beta(6, 2): mean 0.75, variance 6*2/(8^2*9) ~ 0.02083.
        # Surrogate guarded against: uniform(0.5, 0.95), mean 0.725, variance 0.0169.
        r = self._scalar("rho_g")
        self.assertAlmostEqual(r.mean(), 0.75, delta=0.01)
        self.assertAlmostEqual(r.var(), (6 * 2) / (8**2 * 9), delta=0.002)
        self.assertLess(r.min(), 0.5, "Beta(6,2) has mass below 0.5")

    def test_sigma_u_is_halfnormal_not_hardcoded(self) -> None:
        # sigma_u ~ HalfNormal(0.05), one scale per replicate shared by both
        # shock streams. Surrogate guarded against: fixed 0.004 and 0.010.
        s = self._scalar("sigma_u")
        self.assertAlmostEqual(s.mean(), 0.05 * np.sqrt(2 / np.pi), delta=0.002)
        self.assertGreater(s.std(), 0.01, "a hard-coded scale has zero variance")

    def test_sigma_v_is_halfnormal_at_the_derived_scale(self) -> None:
        # sigma_v ~ HalfNormal(S_V), S_V = 0.0191 from the procedure committed
        # in PRIORS.md Amendment 1 BEFORE computation. Surrogates guarded
        # against: sharing sigma_u's 0.05 scale (the run-003 PP3 runaway), and
        # any hard-coded scale (zero variance).
        s = self._scalar("sigma_v")
        self.assertAlmostEqual(s.mean(), pp.S_V * np.sqrt(2 / np.pi), delta=0.001)
        self.assertGreater(s.std(), 0.005, "a hard-coded scale has zero variance")
        self.assertLess(
            s.mean(), 0.03, "a 0.05-scale draw would mean the shared prior is back"
        )

    def test_delta_is_sign_free(self) -> None:
        # delta ~ Normal(0, 0.25). A sign restriction here would build the
        # direction of the result into the prior.
        v = self._scalar("delta")
        self.assertAlmostEqual(v.mean(), 0.0, delta=0.01)
        self.assertAlmostEqual(v.std(), 0.25, delta=0.01)
        self.assertGreater((v < 0).mean(), 0.45)
        self.assertGreater((v > 0).mean(), 0.45)

    def test_psi_is_sign_free(self) -> None:
        # psi ~ Normal(0, 0.10), drawn per state per input. PRIORS.md states the
        # sign is deliberately unrestricted: political stress could plausibly
        # accelerate or retard capability accumulation, and committing to one
        # direction would settle by assumption a question the model should answer.
        v = np.concatenate(
            [
                np.asarray(d.psi[s], dtype=float).ravel()
                for d in self.draws
                for s in pp.STATES
            ]
        )
        self.assertAlmostEqual(v.mean(), 0.0, delta=0.01)
        self.assertAlmostEqual(v.std(), 0.10, delta=0.01)
        self.assertGreater((v < 0).mean(), 0.45)
        self.assertGreater((v > 0).mean(), 0.45)

    def test_gstar_ai_is_per_state_folded_normal(self) -> None:
        # gstar_ai[i] ~ |Normal(0.03, 0.02)| iid per state, PRIORS.md
        # Amendment 3 (provisional). Folded-normal mean with mu/sigma = 1.5:
        # sigma*sqrt(2/pi)*exp(-mu^2/2sigma^2) + mu*(1 - 2*Phi(-mu/sigma))
        # = 0.031173. Surrogate guarded against: the superseded SHARED scalar
        # -- the two states must be independent draws, not one value copied.
        us = np.array([d.gstar_ai["US"] for d in self.draws])
        cn = np.array([d.gstar_ai["CN"] for d in self.draws])
        both = np.concatenate([us, cn])
        self.assertAlmostEqual(both.mean(), 0.031173, delta=0.002)
        self.assertGreaterEqual(both.min(), 0.0)
        self.assertTrue(
            np.all(us != cn),
            "gstar_ai must be drawn per state; equal values mean the shared "
            "scalar is back",
        )

    def test_sigma_ai_is_halfnormal_at_the_amendment_1_scale(self) -> None:
        # sigma_ai ~ HalfNormal(S_V), the seventh growth-innovation stream on
        # the Amendment 1 scale, per PRIORS.md Amendment 3 (provisional).
        # Surrogates guarded against: sharing sigma_u's 0.05 scale, and any
        # hard-coded scale (zero variance).
        s = self._scalar("sigma_ai")
        self.assertAlmostEqual(s.mean(), pp.S_V * np.sqrt(2 / np.pi), delta=0.001)
        self.assertGreater(s.std(), 0.005, "a hard-coded scale has zero variance")
        self.assertLess(
            s.mean(), 0.03, "a 0.05-scale draw would mean the shared prior is back"
        )

    def test_mirror_swaps_the_ai_stream_and_gstar_ai(self) -> None:
        # PP4 fails on noise if either swap is missed (run-001 failure mode),
        # but only diagnosably so; this pins each swap directly.
        rng = np.random.default_rng(SEED)
        d = pp.sample_prior(rng)
        m = pp.mirror_draw(d)
        self.assertEqual(m.gstar_ai["US"], d.gstar_ai["CN"])
        self.assertEqual(m.gstar_ai["CN"], d.gstar_ai["US"])
        sh = pp.sample_shocks(rng, 5, d.tau, d.sigma_u, d.sigma_v, sigma_ai=d.sigma_ai)
        sm = sh.mirrored()
        self.assertTrue(np.array_equal(sm.ai["US"], sh.ai["CN"]))
        self.assertTrue(np.array_equal(sm.ai["CN"], sh.ai["US"]))

    def test_sigma_top_2026_is_bounded_as_committed(self) -> None:
        # sigma_top[2026] ~ LogNormal(log 0.6, 0.55), bounded [0.15, 2.5].
        v = self._scalar("sigma_top0")
        self.assertGreaterEqual(v.min(), 0.15)
        self.assertLessEqual(v.max(), 2.5)

    def test_engineering_ceiling_table_is_the_declared_one(self) -> None:
        # Registered by amendment to SPECIFICATION.md. The values are a
        # pre-registered parameter and are named in PRIOR-PREDICTIVE-RUN-001.md
        # section 3.1 as a candidate remedy that was NOT taken.
        self.assertEqual(
            dict(pp.ENGINEERING_CEILING_MULTIPLE),
            {"D1": 4.0, "D2": 4.0, "D3": 5.0, "F1": 8.0, "F2": 6.0, "F3": 3.0},
        )

    def test_xbar_is_lognormal_around_the_declared_ceiling(self) -> None:
        # xbar[j] ~ LogNormal(log(multiple * baseline), 0.6). The median of the
        # ratio to baseline must be the declared multiple, not a uniform span.
        # Surrogate guarded against: uniform(3, 30) * baseline for every input.
        for j, inp in enumerate(pp.INPUTS):
            ratios = np.array(
                [d.xbar["US"][j] / pp.SYNTHETIC_BASELINE["US"][inp] for d in self.draws]
            )
            expected = pp.ENGINEERING_CEILING_MULTIPLE[inp]
            self.assertAlmostEqual(
                float(np.median(ratios)),
                expected,
                delta=0.15 * expected,
                msg=f"{inp}: median ceiling multiple should be {expected}",
            )


class TestClassifierInvariants(unittest.TestCase):
    """Rule R009 section 6, the invariants that do not need a full gate run."""

    def test_priority_order_is_frozen_in_code(self) -> None:
        src = (
            REPO / "pipeline" / "src" / "usbip" / "model" / "prior_predictive.py"
        ).read_text()
        # R5 must be tested before R3, and R3 before R4. Reordering is a major
        # version bump per rules/R009-regime-classification.md section 5.
        i5, i3, i4 = (src.index(f'return "R{n}"') for n in (5, 3, 4))
        self.assertLess(i5, i3)
        self.assertLess(i3, i4)

    def test_r0_bucket_exists_and_is_reachable(self) -> None:
        self.assertIn("R0_no_material_change", pp.regime_masses(50, SEED, horizon=2030))

    def test_horizon_beyond_window_raises(self) -> None:
        rng = np.random.default_rng(SEED)
        traj = pp.simulate(pp.sample_prior(rng), rng, end_year=2050)
        with self.assertRaises(ValueError):
            pp.classify(traj, 2075)

    def test_deadband_comparison_is_strict(self) -> None:
        self.assertEqual(pp.DEADBAND, 0.10)
        self.assertEqual(pp.REVERSAL_DEPTH, 0.15)
        self.assertEqual(pp.CONSTRAINT_RATIO, 0.60)


if __name__ == "__main__":
    unittest.main()


class TestPP1ClaimHorizons(unittest.TestCase):
    """PP1 checks each regime at its earliest claimed horizon.

    SPECIFICATION.md Amendment 02 restricts the output contract to report R5 at
    2075 only; IDENTIFICATION.md Amendment 1 makes the gate follow the claim.
    """

    def test_claim_horizon_map_matches_the_amended_contract(self) -> None:
        self.assertEqual(
            pp.PP1_CLAIM_HORIZON,
            {"R1": 2050, "R2": 2050, "R3": 2050, "R4": 2050, "R5": 2075},
        )

    def test_gate_evaluates_both_claimed_horizons(self) -> None:
        res = pp.pp1_regime_coverage(30, 7)
        self.assertEqual(sorted(res.values["masses"]), [2050, 2075])
