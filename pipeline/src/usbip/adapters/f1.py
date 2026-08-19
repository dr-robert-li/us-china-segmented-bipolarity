"""F1 adapter -- executable.

Condition: US generation-capacity additions converge on China's.
Threshold: US annual additions reach 40 percent of PRC annual additions,
three-year rolling average. Deadline 2035. Type A.

Specification: pipeline/adapters/F1.md. Rules: R001, R002.

This module contains no capacity data. It consumes normalised observations and
emits a verdict record. The separation matters because the adapter must be
testable against synthetic inputs -- including inputs designed to make it fail --
without a network fetch.

F1 does NOT call R003. The adapter specification grants F1 an explicit exemption
from the dispatchable conversion because F1 tests build-rate convergence and its
threshold was pre-registered against nameplate additions. Applying the
conversion here would silently move a pre-registered threshold, which the
pre-registration exists to prevent. ``assert_no_dispatchable_conversion`` makes
the exemption checkable rather than merely stated.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, Sequence

from ..reconcile import Disagreement, compare
from ..rules import (
    R001_ID,
    R001_VERSION,
    R002_ID,
    R002_VERSION,
    RatioResult,
    r001_net_additions,
    r002_rolling_ratio,
)
from ..schema import (
    Basis,
    Clause,
    Observation,
    SchemaError,
    Series,
    Verdict,
    VerdictRecord,
)

THRESHOLD = 0.40
DEADLINE = 2035
TOLERANCE = 0.05  # 5 percent of the national figure, per adapters/F1.md

# Sanity band on a single country's annual net additions, in GW. Purpose is
# Hazard 3 -- a PRC renewables-only or wind-and-solar-only additions figure
# supplied as total additions. Such a figure is smaller than the true total and
# would deflate the denominator, inflating the ratio toward the threshold. The
# band is a floor test on plausibility, not an estimate.
SUBSET_TRAP_FLOOR_GW = {"CHN": 150.0, "USA": 10.0}

SERIES = {
    "cap_total_installed": Series(
        series_id="cap_total_installed",
        name="Total installed generation capacity, year-end",
        concept=(
            "Installed electrical generating capacity of all technologies at "
            "year end, nameplate basis"
        ),
        unit="GW",
        geography_scope=("USA", "CHN"),
        definitional_boundary=(
            "All generating technologies, nameplate rating, at year end. "
            "Harmonised across both geographies by the primary source so that "
            "numerator and denominator of the F1 ratio share one methodology. "
            "Whether the PRC series is grid-connected or installed is an OPEN "
            "ITEM in adapters/F1.md and must be resolved and recorded here at "
            "first fetch; the two differ and the difference is not negligible. "
            "US utility-scale-only coverage would exclude behind-the-meter "
            "solar, which is Hazard 1 in the adapter and is the reason a single "
            "harmonised source is primary for both countries rather than each "
            "national agency being authoritative for its own half."
        ),
        net_or_gross=None,
        coverage_caveats=(
            "Harmonised datasets typically lag national releases for some "
            "geographies; most-recent-year PRC coverage completeness is an open "
            "item",
            "Partial-year national releases are excluded from the verdict and "
            "ingested for monitoring only, flagged partial_year and preliminary",
        ),
        primary_source="ember",
        crosscheck_sources=("eia", "nea_nbs"),
        falsifiers=("F1",),
    ),
    "cap_additions_net": Series(
        series_id="cap_additions_net",
        name="Net additions to installed generation capacity",
        concept="Annual change in year-end installed capacity",
        unit="GW",
        geography_scope=("USA", "CHN"),
        definitional_boundary=(
            "Net of retirements by construction, since it is the difference of "
            "two year-end totals. Not comparable to a published gross additions "
            "figure. The US retires materially more thermal capacity than "
            "historically and the PRC fleet is younger, so the gross-versus-net "
            "gap is not a constant across years or across the two states."
        ),
        net_or_gross="net",
        primary_source="derived",
        falsifiers=("F1",),
    ),
    "cap_additions_reported": Series(
        series_id="cap_additions_reported",
        name="Additions to installed generation capacity, as published",
        concept="Additions as reported by the national source",
        unit="GW",
        geography_scope=("USA", "CHN"),
        definitional_boundary=(
            "As published, therefore frequently gross and frequently covering a "
            "subset of the fleet. Ingested to make the gross-versus-net gap "
            "measurable rather than assumed. Does NOT feed the verdict."
        ),
        net_or_gross="gross",
        primary_source="eia_nea",
        falsifiers=("F1",),
    ),
}


@dataclass
class F1Result:
    verdict: VerdictRecord
    ratios: dict[int, RatioResult]
    disagreements: list[Disagreement]
    derived: list[Observation]
    blocked_years: list[int] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


def assert_no_dispatchable_conversion(observations: Sequence[Observation]) -> None:
    """Guard the bounded F1 exemption from R003.

    F1 consumes nameplate capacity. An observation reaching this adapter that
    has already been dispatchable-adjusted would mean the exemption has leaked
    in the wrong direction, and the resulting ratio would be tested against a
    threshold that was pre-registered on a different quantity.
    """
    for obs in observations:
        if "dispatchable" in obs.series_id:
            raise SchemaError(
                f"F1 received dispatchable-adjusted series {obs.series_id!r}; "
                f"F1 is pre-registered on nameplate additions and is exempt "
                f"from R003. See adapters/F1.md."
            )


def check_subset_trap(additions: Mapping[int, float], geography: str) -> list[str]:
    """Hazard 3. A subset release read as a total must fail, not pass quietly.

    F1 adapter Test 3. Published 2024 PRC renewable additions of roughly 373 GW
    and 2025 wind-and-solar additions above 430 GW are both subsets, and either
    supplied as a total would deflate the denominator.
    """
    floor = SUBSET_TRAP_FLOOR_GW.get(geography)
    if floor is None:
        return []
    return [
        f"{geography} {year}: net additions {value:.1f} GW below the "
        f"plausibility floor of {floor:.0f} GW; possible subset-read-as-total. "
        f"Verdict emission blocked for the affected window."
        for year, value in sorted(additions.items())
        if value < floor
    ]


def evaluate(
    *,
    totals_primary: Mapping[str, Mapping[int, Observation]],
    totals_crosscheck: Mapping[str, Mapping[int, Observation]],
    evaluation_year: int,
    code_sha: str,
) -> F1Result:
    """Run the adapter for one evaluation year.

    ``totals_primary`` and ``totals_crosscheck`` are keyed by geography then by
    year. Both must contain the three-year window ending at ``evaluation_year``
    plus the year before it, since R001 differences consecutive totals.
    """
    for geo_map in totals_primary.values():
        assert_no_dispatchable_conversion(list(geo_map.values()))

    notes: list[str] = []
    disagreements: list[Disagreement] = []
    derived: list[Observation] = []
    blocked: list[int] = []

    additions: dict[str, dict[int, float]] = {}
    for geo in ("USA", "CHN"):
        if geo not in totals_primary:
            raise SchemaError(f"F1: no primary totals for {geo}")
        obs, ders = r001_net_additions(dict(totals_primary[geo]), code_sha=code_sha)
        derived.extend(obs)
        additions[geo] = {o.period_end.year: o.value for o in obs}
        for o in obs:
            if "vintage_conflict" in o.flags:
                notes.append(
                    f"{geo} {o.period_end.year}: differenced across a vintage "
                    f"boundary; both vintages recorded in the derivation"
                )

        # Cross-source reconciliation on the totals, not the differences. The
        # adapter states the tolerance against total installed capacity.
        for year, primary in sorted(totals_primary[geo].items()):
            cross = totals_crosscheck.get(geo, {}).get(year)
            if cross is None:
                notes.append(
                    f"{geo} {year}: no cross-check observation; "
                    f"source_disagreement cannot be evaluated for this year"
                )
                continue
            d = compare(primary, cross, tolerance=TOLERANCE)
            disagreements.append(d)
            if d.breached:
                blocked.append(year)
                notes.append(d.message)

        for msg in check_subset_trap(additions[geo], geo):
            notes.append(msg)
            blocked.append(evaluation_year)

    ratio = r002_rolling_ratio(
        additions["USA"], additions["CHN"], evaluation_year, threshold=THRESHOLD
    )

    flags: list[str] = []
    if any(y in blocked for y in (evaluation_year, evaluation_year - 1, evaluation_year - 2)):
        flags.append("source_disagreement")
    if any("vintage_conflict" in o.flags for o in derived):
        flags.append("vintage_conflict")

    # Verdict logic, in the order the specification imposes.
    if ratio.committed is None:
        verdict = Verdict.INDETERMINATE
        clause = Clause.INDETERMINATE
        notes.append(f"{evaluation_year}: {ratio.note}")
    elif "source_disagreement" in flags:
        # Tolerance breach blocks automatic verdict emission pending
        # adjudication. It does not become not_triggered by default, because a
        # blocked year defaulting to the thesis-favourable verdict is exactly
        # the asymmetry the standing prohibitions forbid.
        verdict = Verdict.INDETERMINATE
        clause = Clause.INDETERMINATE
        notes.append(
            f"{evaluation_year}: verdict emission blocked; cross-source "
            f"tolerance breached in the rolling window, pending adjudication"
        )
    elif ratio.straddles_threshold:
        verdict = Verdict.INDETERMINATE
        clause = Clause.INDETERMINATE
        notes.append(f"{evaluation_year}: {ratio.note}")
    elif evaluation_year > DEADLINE:
        verdict = Verdict.NOT_TRIGGERED
        clause = Clause.NOT_MET
        notes.append(
            f"{evaluation_year}: past the {DEADLINE} deadline; the condition can "
            f"no longer trigger and this must be stated in the annual log rather "
            f"than the deadline being extended"
        )
    elif ratio.committed >= THRESHOLD:
        verdict = Verdict.TRIGGERED
        clause = Clause.MET
    else:
        verdict = Verdict.NOT_TRIGGERED
        clause = Clause.NOT_MET

    record = VerdictRecord(
        falsifier_id="F1",
        evaluation_year=evaluation_year,
        threshold=THRESHOLD,
        verdict=verdict,
        condition_type="A",
        observed_value=ratio.committed,
        distance_to_threshold=(
            None if ratio.committed is None else THRESHOLD - ratio.committed
        ),
        quantitative_clause=clause,
        qualitative_clause=Clause.NOT_APPLICABLE,
        inputs=tuple(sorted(o.obs_id for o in derived)),
        sensitivity={
            "mean_of_annual_ratios": ratio.sensitivity,
            "committed_construction": "ratio_of_three_year_sums",
            "constructions_straddle_threshold": ratio.straddles_threshold,
            "rules": {R001_ID: R001_VERSION, R002_ID: R002_VERSION},
        },
        flags=tuple(sorted(set(flags))),
    )

    return F1Result(
        verdict=record,
        ratios={evaluation_year: ratio},
        disagreements=disagreements,
        derived=derived,
        blocked_years=sorted(set(blocked)),
        notes=notes,
    )
