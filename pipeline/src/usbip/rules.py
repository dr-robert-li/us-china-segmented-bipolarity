"""Registered transformation rules.

Every function here corresponds to an entry in pipeline/rules/README.md. A
derived figure produced by code that is not in this module, or by a function
whose ``RULE_ID``/``VERSION`` are not registered, is not publishable.

Rules are pure functions of their inputs and declared parameters. No rule reads
a clock, a filesystem, a network, or a random number generator, because
schema.md design rule 5 requires byte-identical output for identical inputs and
rule versions.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timezone
from typing import Iterable, Mapping

from .schema import (
    Basis,
    Derivation,
    Observation,
    PeriodType,
    SchemaError,
)

# Registry mirror. Checked against pipeline/rules/README.md by a test, so the
# two cannot drift silently.
REGISTERED: dict[str, str] = {
    "R001": "1.0.0",
    "R002": "1.1.0",  # 1.1.0: negative-numerator semantics, adapters/F1.md Amendment 2
    "R003": "0.1.0",  # sourced parameters; see rules/R003-nameplate-to-dispatchable.md
    "R004": "1.0.0",
    "R005": "1.0.0",
    "R006": "1.0.0",
    "R007": "1.0.0",
    "R008": "1.0.0",
    # Registered by amendment to model/SPECIFICATION.md during Phase 3. Below
    # 1.0 because two of its three constants are judgement calls with no
    # sensitivity run, and because its R5 branch is implicated in a failing
    # prior-predictive gate. See rules/R009-regime-classification.md.
    "R009": "0.1.0",
    # Registered 2026-08-20 by definitions/frontier-compute.md Amendment 1.
    # Below 1.0 because the coverage-error characterisation (R010) and the
    # band enumeration (R011) have not yet been exercised at a first ingest.
    "R010": "0.1.0",
    "R011": "0.1.0",
    # Registered 2026-08-20; rules/R012-naive-benchmark.md. Below 1.0 because
    # the innovation scales are specified by procedure but never yet computed.
    "R012": "0.1.0",
    # Registered 2026-08-21 at first ingest; adapters/F1.md Amendment 2 Decision 3.
    "R013": "1.0.0",
}


def _det_id(rule_id: str, version: str, inputs: Iterable[str]) -> str:
    """Deterministic derivation id.

    Not a UUID. A uuid4 here would violate design rule 5, since two runs over
    identical inputs would produce different derivation records and therefore
    non-identical output.
    """
    import hashlib

    payload = "|".join([rule_id, version, *sorted(inputs)])
    return "d" + hashlib.sha256(payload.encode()).hexdigest()[:24]


# Fixed epoch for derivation timestamps in deterministic mode. schema.md
# requires byte-identical derived output for identical inputs; a wall-clock
# ``computed_at`` breaks that. The run artifact carries the real wall-clock
# time, so nothing is lost.
DETERMINISTIC_EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)


# ---------------------------------------------------------------------------
# R001 -- net additions by differencing year-end totals
# ---------------------------------------------------------------------------

R001_ID, R001_VERSION = "R001", "1.0.0"


def r001_net_additions(
    totals: Mapping[int, Observation],
    *,
    code_sha: str,
) -> tuple[list[Observation], list[Derivation]]:
    """Annual net additions from consecutive year-end installed-capacity totals.

    ``A_t = C_t - C_{t-1}``, both from the same source, per adapters/F1.md
    Step 1. Output carries ``basis: differenced``.

    Differencing is preferred over reported addition figures because it is
    symmetric across the two countries and yields net additions on both sides by
    construction. That closes Hazard 2 in the adapter -- a gross numerator
    against a net denominator, whose bias direction is not constant across
    years.

    Where ``C_t`` and ``C_{t-1}`` come from different vintages the output raises
    ``vintage_conflict`` and the derivation parameters record both vintages.
    This is F1 adapter Test 2.
    """
    out_obs: list[Observation] = []
    out_der: list[Derivation] = []
    years = sorted(totals)
    for year in years:
        prev = year - 1
        if prev not in totals:
            continue
        c_t, c_prev = totals[year], totals[prev]
        if c_t.unit != c_prev.unit:
            raise SchemaError(
                f"R001: unit mismatch {c_t.unit} vs {c_prev.unit}; convert "
                f"before differencing"
            )
        if c_t.geography != c_prev.geography:
            raise SchemaError("R001: geography mismatch")
        if c_t.basis is not Basis.REPORTED or c_prev.basis is not Basis.REPORTED:
            raise SchemaError(
                "R001 consumes reported totals only; differencing a differenced "
                "series is not a registered operation"
            )

        flags: list[str] = []
        if c_t.vintage != c_prev.vintage:
            flags.append("vintage_conflict")
        # A break registered against either endpoint propagates. An addition
        # figure spanning a break is not comparable to one that does not.
        for endpoint in (c_t, c_prev):
            if "structural_break" in endpoint.flags:
                flags.append("structural_break")
            if "preliminary" in endpoint.flags:
                flags.append("preliminary")

        derived = Observation(
            series_id="cap_additions_net",
            geography=c_t.geography,
            period_start=date(year, 1, 1),
            period_end=date(year, 12, 31),
            period_type=PeriodType.ANNUAL,
            value=c_t.value - c_prev.value,
            unit=c_t.unit,
            vintage=max(c_t.vintage, c_prev.vintage),
            source_id=c_t.source_id,
            retrieved_at=c_t.retrieved_at,
            basis=Basis.DIFFERENCED,
            flags=tuple(sorted(set(flags))),
        )
        out_obs.append(derived)
        out_der.append(
            Derivation(
                derivation_id=_det_id(R001_ID, R001_VERSION, [c_t.obs_id, c_prev.obs_id]),
                rule_id=R001_ID,
                rule_version=R001_VERSION,
                inputs=(c_prev.obs_id, c_t.obs_id),
                output=derived.obs_id,
                parameters={
                    "year": year,
                    "vintage_t": c_t.vintage.isoformat(),
                    "vintage_t_minus_1": c_prev.vintage.isoformat(),
                    "unit": c_t.unit,
                },
                computed_at=DETERMINISTIC_EPOCH,
                code_sha=code_sha,
            )
        )
    return out_obs, out_der


# ---------------------------------------------------------------------------
# R002 -- ratio of three-year sums, with the mean-of-ratios sensitivity
# ---------------------------------------------------------------------------

# 1.1.0: negative-numerator semantics per adapters/F1.md Amendment 2 Decision 2.
# Minor bump: the change cannot alter any published verdict (none exists, and a
# negative numerator maps to not_triggered, which a negative ratio already did).
R002_ID, R002_VERSION = "R002", "1.1.0"


@dataclass(frozen=True)
class RatioResult:
    year: int
    committed: float | None  # ratio of three-year sums
    sensitivity: float | None  # mean of three annual ratios, clamped per Amendment 2
    straddles_threshold: bool
    note: str
    negative_numerator: bool = False
    sensitivity_undamped: float | None = None  # published alongside when clamping bit


def r002_rolling_ratio(
    additions_us: Mapping[int, float],
    additions_prc: Mapping[int, float],
    year: int,
    *,
    threshold: float = 0.40,
) -> RatioResult:
    """The committed F1 construction and its pre-registered sensitivity.

    Committed:   ``R_t  = sum(A_US, t-2..t) / sum(A_PRC, t-2..t)``
    Sensitivity: ``R'_t = mean(A_US,k / A_PRC,k for k in t-2..t)``

    The ratio of sums governs the verdict because it is robust to a single
    anomalous PRC year. The mean of ratios places large weight on any year with
    a small denominator, which over a decade of volatile build rates is a live
    risk rather than a theoretical one. Both are computed and published; this is
    the pre-commitment made in adapters/F1.md Step 2, and it is not revisited
    here.

    ``straddles_threshold`` implements F1 adapter Test 7: where the two
    constructions fall on opposite sides of the threshold, the honest verdict is
    ``indeterminate`` and both values are published, rather than relying on the
    committed choice silently.
    """
    window = [year - 2, year - 1, year]
    if not all(y in additions_us and y in additions_prc for y in window):
        return RatioResult(year, None, None, False, "incomplete three-year window")

    num = sum(additions_us[y] for y in window)
    den = sum(additions_prc[y] for y in window)
    if den <= 0:
        # Not a division guard for its own sake. A non-positive PRC three-year
        # net-addition sum would mean the fleet shrank, which would be a finding
        # in its own right and must not be silently expressed as a ratio.
        return RatioResult(
            year, None, None, False, "non-positive PRC three-year sum; ratio undefined"
        )
    committed = num / den
    negative_numerator = num < 0

    annual = []
    for y in window:
        if additions_prc[y] <= 0:
            annual = []
            break
        annual.append(additions_us[y] / additions_prc[y])
    # Amendment 2 Decision 2: negative annual ratios are clamped to zero for
    # the reported sensitivity, and the undamped mean is published alongside,
    # so a single negative year cannot dominate the mean while the sign
    # information stays visible.
    sensitivity_undamped = sum(annual) / len(annual) if annual else None
    clamped = [max(a, 0.0) for a in annual]
    sensitivity = sum(clamped) / len(clamped) if clamped else None

    straddles = (
        sensitivity is not None
        and (committed >= threshold) != (sensitivity >= threshold)
    )
    if negative_numerator:
        # "US additions were negative" is a different finding from "US
        # additions were X percent of China's", reported distinctly. The
        # negative committed ratio is published as computed, not floored.
        note = (
            "negative three-year numerator sum: US net additions were negative "
            "over the window; not_triggered with the negative_numerator flag "
            "per adapters/F1.md Amendment 2"
        )
    elif straddles:
        note = (
            "constructions straddle the threshold; verdict is indeterminate per "
            "adapters/F1.md Test 7"
        )
    else:
        note = "constructions agree on the side of the threshold"
    return RatioResult(
        year, committed, sensitivity, straddles, note,
        negative_numerator=negative_numerator,
        sensitivity_undamped=sensitivity_undamped,
    )


# ---------------------------------------------------------------------------
# R013 -- cap_total_installed by pinned-whitelist fuel-row summation
# ---------------------------------------------------------------------------

R013_ID, R013_VERSION = "R013", "1.0.0"

# The pinned whitelist, adapters/F1.md Amendment 2 Decision 3. Frozen: a new
# fuel variable in a future vintage must FAIL validation, not silently widen
# the definitional basis between vintages.
R013_FUEL_WHITELIST = frozenset(
    {
        "Bioenergy",
        "Coal",
        "Gas",
        "Hydro",
        "Nuclear",
        "Other Fossil",
        "Other Renewables",
        "Solar",
        "Wind",
    }
)
R013_AGGREGATE_TOLERANCE = 0.005  # within rounding: 0.5 percent of the sum


def r013_total_from_fuel_rows(
    fuel_values: Mapping[str, float],
    *,
    clean_plus_fossil: float | None,
    geography: str,
    year: int,
) -> float:
    """Sum the nine pinned fuel rows and validate against Clean + Fossil.

    Verified against the committed snapshot (sha256 259e1095...) across all 52
    country-years at specification time; this function makes the verification a
    standing property of every ingest rather than a one-off check.
    """
    seen = set(fuel_values)
    unknown = seen - R013_FUEL_WHITELIST
    missing = R013_FUEL_WHITELIST - seen
    if unknown:
        raise SchemaError(
            f"R013 {geography} {year}: fuel rows outside the pinned whitelist: "
            f"{sorted(unknown)}; a new fuel category is a definitional-basis "
            f"change and must be adjudicated, not summed"
        )
    # A whitelist member ABSENT is an implicit zero, permitted only because the
    # Clean+Fossil aggregate check below still binds -- Ember omits rows for
    # fuels a country has none of (first observed: CHN 2022 has no Other
    # Renewables row), and the dry-run verification that matched all 52
    # country-years summed present rows exactly this way. An absent member
    # with a FAILING aggregate check still fails. Correction note in
    # adapters/F1.md Amendment 2.
    total = float(sum(fuel_values.values()))
    if clean_plus_fossil is None:
        raise SchemaError(
            f"R013 {geography} {year}: Clean+Fossil aggregate unavailable; the "
            f"summation check cannot run and the total is not publishable"
        )
    if total <= 0:
        raise SchemaError(f"R013 {geography} {year}: non-positive total")
    if abs(total - clean_plus_fossil) / total > R013_AGGREGATE_TOLERANCE:
        raise SchemaError(
            f"R013 {geography} {year}: whitelist sum {total:.1f} disagrees with "
            f"Clean+Fossil {clean_plus_fossil:.1f} beyond rounding"
        )
    return total


# ---------------------------------------------------------------------------
# R003 -- nameplate to dispatchable
# ---------------------------------------------------------------------------

R003_ID, R003_VERSION = "R003", "0.1.0"


@dataclass(frozen=True)
class CapacityFactor:
    """A capacity factor with the provenance a sourced parameter must carry.

    ``rules/README.md`` prohibits a rule whose parameters are sourced but
    unversioned, so vintage and source are required rather than optional.
    """

    technology: str
    geography: str
    value: float  # fraction of nameplate, 0..1
    vintage: date
    source_id: str
    basis: str  # "published_capacity_factor" | "implied_from_utilisation_hours"
    comparable_across_geographies: bool

    def __post_init__(self) -> None:
        if not 0.0 <= self.value <= 1.0:
            raise SchemaError(
                f"R003: capacity factor {self.value} for {self.technology}/"
                f"{self.geography} outside [0,1]"
            )


def hours_to_capacity_factor(hours: float, *, denominator_hours: float = 8760.0) -> float:
    """Convert published utilisation hours to an implied capacity factor.

    PRC statistics publish utilisation hours (利用小时数) rather than capacity
    factors. Dividing by 8,760 gives an implied factor, but the result is NOT
    interchangeable with a published EIA capacity factor. The reasons are set out
    in rules/R003-nameplate-to-dispatchable.md section 4.

    CORRECTION, recorded rather than silently applied: an earlier draft of this
    docstring gave the denominator basis as the material reason -- year-end versus
    average installed capacity. That reason is wrong for the OFFICIAL figures.
    The published Chinese definition is explicitly an average: average utilisation
    hours equal generation divided by average equipment capacity, calendar-time
    weighted over the period. EIA's annual figure is likewise a time-weighted
    average of monthly values. On that dimension the two are comparable. The
    denominator error is real only in third-party recomputation from generation
    and year-end capacity, which is why this function consumes published hours
    and never recomputes them. The material reasons are instead gross-versus-net
    own-use, the 6,000 kW scope floor, and behind-the-meter asymmetry.

    Any factor produced by this function must be constructed with
    ``basis="implied_from_utilisation_hours"`` and
    ``comparable_across_geographies=False``.
    """
    if hours < 0 or hours > denominator_hours:
        raise SchemaError(
            f"R003: utilisation hours {hours} outside [0, {denominator_hours}]"
        )
    return hours / denominator_hours


# Own-use net adjustment for PRC gross installed capacity. Published LBNL
# factors, not this project's invention: PRC installed capacity is reported gross
# of generator own-use whereas an effective-capacity measure should be net.
# LBNL, Excess Capacity in China's Power System, section 3.4 and Table 8.
# https://eta-publications.lbl.gov/sites/default/files/lbnl1006638.pdf
OWN_USE_NET_FACTORS: Mapping[str, float] = {
    "thermal": 0.95,
    "coal": 0.95,
    "gas": 0.95,
    "nuclear": 0.95,
    "other": 0.95,
    "hydro": 0.99,
    "pumped_storage": 0.99,
    "wind": 0.99,
    "solar": 0.99,
}

OWN_USE_APPLIES_TO: frozenset[str] = frozenset({"CHN"})


def own_use_net_factor(technology: str, geography: str) -> float:
    """Net-of-own-use multiplier applied to nameplate before the capacity factor.

    Returns 1.0 for geographies whose reported capacity is already net. Applying
    the PRC adjustment to a US fleet would be an asymmetric standard: it would
    shrink one state's measured capacity on a basis that does not apply to it.
    """
    if geography not in OWN_USE_APPLIES_TO:
        return 1.0
    if technology not in OWN_USE_NET_FACTORS:
        raise SchemaError(
            f"R003: no own-use factor registered for {technology!r} in "
            f"{geography}; a missing own-use factor may not be defaulted to 1.0"
        )
    return OWN_USE_NET_FACTORS[technology]


def r003_dispatchable(
    nameplate_gw: Mapping[str, float],
    factors: Mapping[str, CapacityFactor],
    *,
    geography: str,
    allow_cross_geography_comparison: bool = False,
) -> tuple[float, dict[str, object]]:
    """Convert a technology-resolved nameplate fleet to dispatchable-equivalent GW.

    ``D = sum_over_technologies( nameplate_gw[tech] * cf[tech] )``

    Mandated by DATA-INTEGRITY.md for every series feeding ``Y_throughput``.
    F1 is explicitly exempt and must not call this. The exemption is bounded:
    F1 tests build-rate convergence and its threshold was pre-registered against
    nameplate capacity additions, so applying a dispatchable conversion there
    would silently move a pre-registered threshold.

    Refuses to run where any technology in the fleet has no registered factor.
    A missing factor treated as 1.0 would inflate the fleet; treated as 0.0 it
    would delete it. Both are wrong and neither would be visible in the output.

    ``allow_cross_geography_comparison`` must be set explicitly by a caller that
    intends to compare the result across states, and the call fails if any
    contributing factor is flagged non-comparable. The model consumes these
    figures within-state; the guard exists because the temptation to form a
    US/PRC dispatchable ratio is obvious and the ratio would not mean what it
    appears to mean.
    """
    missing = sorted(set(nameplate_gw) - set(factors))
    if missing:
        raise SchemaError(
            f"R003: no registered capacity factor for {missing} in {geography}; "
            f"a missing factor may not be defaulted"
        )
    wrong_geo = sorted(t for t, f in factors.items() if t in nameplate_gw and f.geography != geography)
    if wrong_geo:
        raise SchemaError(
            f"R003: factors for {wrong_geo} are not for geography {geography!r}; "
            f"borrowing another state's capacity factor is a substitution, not a "
            f"conversion"
        )

    noncomparable = sorted(
        t
        for t, f in factors.items()
        if t in nameplate_gw and not f.comparable_across_geographies
    )
    if allow_cross_geography_comparison and noncomparable:
        raise SchemaError(
            f"R003: cross-geography comparison requested but factors for "
            f"{noncomparable} are declared non-comparable; see "
            f"rules/R003-nameplate-to-dispatchable.md"
        )

    total = 0.0
    contributions: dict[str, float] = {}
    own_use: dict[str, float] = {}
    for tech, gw in nameplate_gw.items():
        net = own_use_net_factor(tech, geography)
        own_use[tech] = net
        contribution = gw * net * factors[tech].value
        contributions[tech] = contribution
        total += contribution

    params: dict[str, object] = {
        "geography": geography,
        "factors": {
            t: {
                "value": factors[t].value,
                "vintage": factors[t].vintage.isoformat(),
                "source_id": factors[t].source_id,
                "basis": factors[t].basis,
            }
            for t in sorted(nameplate_gw)
        },
        "contributions_gw": contributions,
        "own_use_net_factors": own_use,
        "own_use_source_id": (
            "LBNL-1006638" if geography in OWN_USE_APPLIES_TO else None
        ),
        "cross_geography_comparison_permitted": bool(
            allow_cross_geography_comparison and not noncomparable
        ),
        "noncomparable_technologies": noncomparable,
    }
    return total, params
