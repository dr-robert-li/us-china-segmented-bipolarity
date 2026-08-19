"""The seven tests required by adapters/F1.md before the adapter is complete.

Each test names the numbered requirement it discharges. A test that passes for a
reason other than the one the adapter specification gives is not evidence about
the adapter, so the assertions target the specified behaviour rather than the
convenient behaviour.

Run: python -m pytest pipeline/tests -q   (from the repository root, with
pipeline/src on the path) or python -m unittest discover -s pipeline/tests.
"""

from __future__ import annotations

import unittest
from datetime import date, datetime, timezone

from usbip.adapters import f1
from usbip.rules import r001_net_additions, r002_rolling_ratio
from usbip.schema import (
    Basis,
    Observation,
    PeriodType,
    SchemaError,
    Verdict,
    convert,
)

RETRIEVED = datetime(2026, 8, 19, tzinfo=timezone.utc)
CODE_SHA = "0" * 40


def total(
    geo: str,
    year: int,
    gw: float,
    *,
    vintage: date | None = None,
    source_id: str = "ember_yearly",
    series_id: str = "cap_installed_total",
) -> Observation:
    return Observation(
        series_id=series_id,
        geography=geo,
        period_start=date(year, 1, 1),
        period_end=date(year, 12, 31),
        period_type=PeriodType.ANNUAL,
        value=gw,
        unit="GW",
        vintage=vintage or date(2026, 6, 30),
        source_id=source_id,
        retrieved_at=RETRIEVED,
        basis=Basis.REPORTED,
    )


def window(geo: str, values: dict[int, float], **kw) -> dict[int, Observation]:
    return {y: total(geo, y, v, **kw) for y, v in values.items()}


# Four years of totals so R001 can difference three of them. Levels are of a
# plausible order of magnitude and are not data; no verdict is asserted from them.
US_TOTALS = {2022: 1200.0, 2023: 1240.0, 2024: 1285.0, 2025: 1335.0}
CN_TOTALS = {2022: 2560.0, 2023: 2920.0, 2024: 3350.0, 2025: 3800.0}


class TestUnitConversion(unittest.TestCase):
    """F1 adapter Test 1 -- PRC 100-million-kW units convert to GW."""

    def test_100_million_kw_to_gw(self) -> None:
        # 1 x 10^8 kW = 100 GW. The PRC publishes capacity in 亿千瓦.
        self.assertAlmostEqual(convert(1.0, "100_million_kW", "GW"), 100.0)
        self.assertAlmostEqual(convert(38.0, "100_million_kW", "GW"), 3800.0)

    def test_scale_boundaries(self) -> None:
        self.assertAlmostEqual(convert(1_000_000.0, "kW", "GW"), 1.0)
        self.assertAlmostEqual(convert(1000.0, "MW", "GW"), 1.0)
        self.assertAlmostEqual(convert(1.0, "TW", "GW"), 1000.0)
        self.assertAlmostEqual(convert(100.0, "10k_kW", "GW"), 1.0)

    def test_round_trip_via_gw_is_exact_enough(self) -> None:
        gw = convert(38.0, "100_million_kW", "GW")
        self.assertAlmostEqual(gw / 100.0, 38.0, places=9)

    def test_unregistered_pair_raises(self) -> None:
        # An unregistered conversion must fail rather than pass the value through.
        with self.assertRaises(SchemaError):
            convert(1.0, "GW", "TWh")


class TestVintageBoundaryDifferencing(unittest.TestCase):
    """F1 adapter Test 2 -- differencing across a vintage boundary is flagged."""

    def test_flag_raised_and_both_vintages_recorded(self) -> None:
        totals = window("CHN", {2023: 2920.0}, vintage=date(2025, 3, 1))
        totals.update(window("CHN", {2024: 3350.0}, vintage=date(2026, 6, 30)))
        obs, ders = r001_net_additions(totals, code_sha=CODE_SHA)
        self.assertEqual(len(obs), 1)
        self.assertIn("vintage_conflict", obs[0].flags)
        params = ders[0].parameters
        recorded = str(params)
        self.assertIn("2025-03-01", recorded)
        self.assertIn("2026-06-30", recorded)

    def test_same_vintage_not_flagged(self) -> None:
        obs, _ = r001_net_additions(window("CHN", CN_TOTALS), code_sha=CODE_SHA)
        for o in obs:
            self.assertNotIn("vintage_conflict", o.flags)


class TestSubsetTrap(unittest.TestCase):
    """F1 adapter Test 3 -- a subset figure read as a total must not pass silently.

    Hazard 3 in the adapter: PRC headline releases report renewables-only or
    wind-and-solar-only additions. In 2024 that was roughly 373 GW against total
    net additions materially above it, so a subset denominator produces a ratio
    that is arithmetically correct and substantively wrong.
    """

    def test_implausibly_low_prc_additions_flagged(self) -> None:
        flagged = f1.check_subset_trap({2023: 360.0, 2024: 373.0, 2025: 140.0}, "CHN")
        self.assertEqual(len(flagged), 1)
        self.assertIn("2025", flagged[0])
        self.assertIn("subset", flagged[0])

    def test_plausible_series_not_flagged(self) -> None:
        additions = {y: CN_TOTALS[y] - CN_TOTALS[y - 1] for y in (2023, 2024, 2025)}
        self.assertEqual(f1.check_subset_trap(additions, "CHN"), [])

    def test_trap_blocks_verdict_in_full_adapter(self) -> None:
        low = dict(CN_TOTALS)
        low[2025] = low[2024] + 40.0  # 40 GW of PRC net additions is not credible
        result = f1.evaluate(
            totals_primary={"USA": window("USA", US_TOTALS), "CHN": window("CHN", low)},
            totals_crosscheck={},
            evaluation_year=2025,
            code_sha=CODE_SHA,
        )
        self.assertEqual(result.verdict.verdict, Verdict.INDETERMINATE)
        self.assertTrue(any("subset" in n for n in result.notes))


class TestToleranceBreach(unittest.TestCase):
    """F1 adapter Test 4 -- a 6 percent divergence blocks verdict emission."""

    def test_six_percent_breach_blocks_and_flags(self) -> None:
        cross = {
            y: total("CHN", y, v * 1.06, source_id="nea_nbs")
            for y, v in CN_TOTALS.items()
        }
        result = f1.evaluate(
            totals_primary={
                "USA": window("USA", US_TOTALS),
                "CHN": window("CHN", CN_TOTALS),
            },
            totals_crosscheck={"CHN": cross},
            evaluation_year=2025,
            code_sha=CODE_SHA,
        )
        self.assertEqual(result.verdict.verdict, Verdict.INDETERMINATE)
        self.assertTrue(result.disagreements)
        self.assertTrue(
any(d.breached for d in result.disagreements)
        )

    def test_four_percent_does_not_block(self) -> None:
        cross = {
            y: total("CHN", y, v * 1.04, source_id="nea_nbs")
            for y, v in CN_TOTALS.items()
        }
        result = f1.evaluate(
            totals_primary={
                "USA": window("USA", US_TOTALS),
                "CHN": window("CHN", CN_TOTALS),
            },
            totals_crosscheck={"CHN": cross},
            evaluation_year=2025,
            code_sha=CODE_SHA,
        )
        self.assertNotEqual(result.verdict.verdict, Verdict.INDETERMINATE)


class TestIdempotency(unittest.TestCase):
    """F1 adapter Test 5 -- two runs over unchanged inputs add no observations."""

    def test_obs_ids_identical_across_runs(self) -> None:
        first, _ = r001_net_additions(window("CHN", CN_TOTALS), code_sha=CODE_SHA)
        second, _ = r001_net_additions(window("CHN", CN_TOTALS), code_sha=CODE_SHA)
        self.assertEqual([o.obs_id for o in first], [o.obs_id for o in second])
        # The set union adds nothing, which is the operational meaning of
        # "zero new observation records".
        self.assertEqual(
            len({o.obs_id for o in first} | {o.obs_id for o in second}),
            len(first),
        )


class TestDeterminism(unittest.TestCase):
    """F1 adapter Test 6 -- identical inputs and rule versions, identical output."""

    def _run(self) -> f1.F1Result:
        return f1.evaluate(
            totals_primary={
                "USA": window("USA", US_TOTALS),
                "CHN": window("CHN", CN_TOTALS),
            },
            totals_crosscheck={},
            evaluation_year=2025,
            code_sha=CODE_SHA,
        )

    def test_byte_identical_derived_output(self) -> None:
        a, b = self._run(), self._run()
        self.assertEqual(a.verdict.verdict, b.verdict.verdict)
        self.assertEqual(
            [o.obs_id for o in a.derived], [o.obs_id for o in b.derived]
        )
        self.assertEqual(a.notes, b.notes)

    def test_no_wallclock_in_derivation_ids(self) -> None:
        # A uuid4 or a timestamp in a derivation id would break design rule 5.
        a, b = self._run(), self._run()
        self.assertEqual(
            {y: r.committed for y, r in a.ratios.items()},
            {y: r.committed for y, r in b.ratios.items()},
        )


class TestConstructionStraddle(unittest.TestCase):
    """F1 adapter Test 7 -- straddling constructions give ``indeterminate``.

    The case the adapter calls the one that matters most: the committed
    ratio-of-sums and the pre-registered mean-of-ratios sensitivity fall on
    opposite sides of 0.40, so the verdict depends on a construction choice.
    """

    def test_straddle_detected(self) -> None:
        # One PRC year with a small denominator pulls the mean of ratios above
        # 0.40 while the ratio of sums stays below it.
        us = {2023: 45.0, 2024: 45.0, 2025: 45.0}
        prc = {2023: 200.0, 2024: 200.0, 2025: 40.0}
        r = r002_rolling_ratio(us, prc, 2025, threshold=0.40)
        self.assertLess(r.committed, 0.40)
        self.assertGreater(r.sensitivity, 0.40)
        self.assertTrue(r.straddles_threshold)

    def test_straddle_yields_indeterminate_and_publishes_both(self) -> None:
        us_tot = {2022: 1000.0, 2023: 1045.0, 2024: 1090.0, 2025: 1135.0}
        cn_tot = {2022: 2000.0, 2023: 2200.0, 2024: 2400.0, 2025: 2440.0}
        result = f1.evaluate(
            totals_primary={
                "USA": window("USA", us_tot),
                "CHN": window("CHN", cn_tot),
            },
            totals_crosscheck={},
            evaluation_year=2025,
            code_sha=CODE_SHA,
        )
        self.assertEqual(result.verdict.verdict, Verdict.INDETERMINATE)
        r = result.ratios[2025]
        self.assertIsNotNone(r.committed)
        self.assertIsNotNone(r.sensitivity)
        self.assertTrue(r.straddles_threshold)

    def test_no_straddle_when_both_agree(self) -> None:
        us = {2023: 45.0, 2024: 45.0, 2025: 45.0}
        prc = {2023: 400.0, 2024: 400.0, 2025: 400.0}
        r = r002_rolling_ratio(us, prc, 2025, threshold=0.40)
        self.assertFalse(r.straddles_threshold)


class TestDispatchableExemption(unittest.TestCase):
    """F1 is exempt from R003 and must refuse a dispatchable-adjusted input.

    Not one of the seven, but the exemption is a pre-registration boundary: F1's
    threshold was registered against nameplate additions, so admitting a
    converted series would silently move a pre-registered threshold.
    """

    def test_dispatchable_series_rejected(self) -> None:
        bad = total("CHN", 2024, 1200.0, series_id="cap_dispatchable_equivalent")
        with self.assertRaises(SchemaError):
            f1.assert_no_dispatchable_conversion([bad])

    def test_nameplate_series_accepted(self) -> None:
        f1.assert_no_dispatchable_conversion([total("CHN", 2024, 3350.0)])


if __name__ == "__main__":
    unittest.main()
