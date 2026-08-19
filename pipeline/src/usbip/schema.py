"""Canonical record types.

Direct implementation of pipeline/schema.md. Where this module and that file
disagree, the file governs and this module is a defect.

Design notes that are load-bearing rather than stylistic:

- Every record type is frozen. Design rule 2 in the schema says revisions
  append and nothing is mutated in place, ever. Immutability at the type level
  is the cheapest available enforcement of that.
- ``obs_id`` is derived, never supplied. Passing an identifier in would allow
  two different observations to claim the same identity, which defeats the
  idempotency property the schema depends on.
- ``definitional_boundary`` raises on empty. The schema calls it mandatory and
  most cross-national comparison errors are boundary errors, so the guard is
  worth the friction.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field, replace
from datetime import date, datetime
from enum import Enum
from typing import Any


class PeriodType(str, Enum):
    ANNUAL = "annual"
    QUARTERLY = "quarterly"
    MONTHLY = "monthly"
    POINT = "point"


class Basis(str, Enum):
    REPORTED = "reported"
    DIFFERENCED = "differenced"
    INTERPOLATED = "interpolated"
    ESTIMATED = "estimated"


class NetOrGross(str, Enum):
    NET = "net"
    GROSS = "gross"
    NOT_APPLICABLE = "not_applicable"


class Verdict(str, Enum):
    NOT_TRIGGERED = "not_triggered"
    TRIGGERED = "triggered"
    INDETERMINATE = "indeterminate"


class Clause(str, Enum):
    MET = "met"
    NOT_MET = "not_met"
    INDETERMINATE = "indeterminate"
    NOT_APPLICABLE = "n/a"


class AccessMethod(str, Enum):
    API = "api"
    BULK_DOWNLOAD = "bulk_download"
    PUBLISHED_TABLE = "published_table"
    MANUAL = "manual"


class VintageBasis(str, Enum):
    DECLARED = "declared"
    INFERRED_FROM_HEADER = "inferred_from_header"
    UNKNOWN = "unknown"


# Flag taxonomy. Closed set: an unregistered flag is a specification error,
# not a free-text note, because flags gate verdict emission.
FLAGS = frozenset(
    {
        "definitional_mismatch",
        "source_disagreement",
        "vintage_conflict",
        "structural_break",
        "leadership_transition",
        "basis_mixed",
        "interpolated",
        "preliminary",
        "partial_year",
        "band_applied",
        "psd_projected",
        # Registered by the 2026 F3 amendment. A vintage supersession of large
        # magnitude is not the same object as contemporaneous source
        # disagreement, and the 2026 review found the latter's tolerance does
        # not cover the former.
        "vintage_revision_large",
        # Raised where a quantity has no anchor and its source bias is
        # therefore fixed at the prior mean rather than estimated. See
        # model/IDENTIFICATION.md section 2.
        "anchor_absent",
    }
)


class SchemaError(ValueError):
    """Raised where a record cannot be expressed in the canonical schema.

    Per pipeline/schema.md, an adapter that cannot express its output in these
    structures has a condition that is not yet specified precisely enough. The
    error therefore names the specification defect, not just the bad value.
    """


def _check_flags(flags: tuple[str, ...]) -> None:
    unknown = sorted(set(flags) - FLAGS)
    if unknown:
        raise SchemaError(
            f"unregistered flag(s) {unknown}; add to the taxonomy in "
            f"pipeline/schema.md before use"
        )


# Canonical units per concept. Declared, never inferred from magnitude.
CANONICAL_UNITS = {
    "capacity": "GW",
    "energy": "TWh",
    "fiscal": "pct_gdp",
    "compute": "FLOP_s_dense_bf16",
    "count": "units",
    "ratio": "ratio",
    "hours": "h",
}

# Permitted conversions to canonical units, as multiplicative factors.
# "100 million kW" is the PRC statistical convention (yi qianwa) and is the
# specific conversion Test 1 of the F1 adapter exists to check.
UNIT_CONVERSIONS = {
    ("kW", "GW"): 1e-6,
    ("MW", "GW"): 1e-3,
    ("GW", "GW"): 1.0,
    ("TW", "GW"): 1e3,
    ("100_million_kW", "GW"): 100.0,
    ("10k_kW", "GW"): 0.01,
    ("GWh", "TWh"): 1e-3,
    ("TWh", "TWh"): 1.0,
    ("pct_gdp", "pct_gdp"): 1.0,
    ("h", "h"): 1.0,
    ("units", "units"): 1.0,
    ("ratio", "ratio"): 1.0,
}


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Convert between declared units.

    Refuses unregistered pairs. An unregistered conversion is more likely to be
    a units error than an omission from this table, and a wrong conversion
    produces a plausible number rather than a failure.
    """
    if (from_unit, to_unit) not in UNIT_CONVERSIONS:
        raise SchemaError(
            f"no registered conversion {from_unit!r} -> {to_unit!r}; "
            f"units are declared, never inferred"
        )
    return value * UNIT_CONVERSIONS[(from_unit, to_unit)]


@dataclass(frozen=True)
class Series:
    """Series descriptor. ``definitional_boundary`` may not be empty."""

    series_id: str
    name: str
    concept: str
    unit: str
    geography_scope: tuple[str, ...]
    definitional_boundary: str
    primary_source: str
    net_or_gross: NetOrGross | None = None
    coverage_caveats: tuple[str, ...] = ()
    crosscheck_sources: tuple[str, ...] = ()
    falsifiers: tuple[str, ...] = ()
    break_registry: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.definitional_boundary.strip():
            raise SchemaError(
                f"series {self.series_id!r}: definitional_boundary is mandatory "
                f"and may not be empty"
            )


@dataclass(frozen=True)
class Observation:
    """The atomic record. One quantity, geography, period, vintage, source."""

    series_id: str
    geography: str
    period_start: date
    period_end: date
    period_type: PeriodType
    value: float
    unit: str
    vintage: date
    source_id: str
    retrieved_at: datetime
    basis: Basis
    flags: tuple[str, ...] = ()
    supersedes: str | None = None

    def __post_init__(self) -> None:
        if self.period_end < self.period_start:
            raise SchemaError(
                f"{self.series_id}/{self.geography}: period_end precedes "
                f"period_start"
            )
        if len(self.geography) != 3 or not self.geography.isupper():
            raise SchemaError(
                f"geography {self.geography!r} is not ISO 3166-1 alpha-3"
            )
        _check_flags(self.flags)

    @property
    def obs_id(self) -> str:
        """SHA-256 over the canonical identity fields, per schema.md.

        Deliberately excludes ``retrieved_at``, ``basis``, ``flags`` and
        ``supersedes``. Re-fetching unchanged upstream data must produce an
        identical identifier, and a fetch timestamp inside the hash would defeat
        that. A changed value under an unchanged vintage produces a new id and
        the caller is expected to raise ``vintage_conflict``.
        """
        payload = "|".join(
            [
                self.series_id,
                self.geography,
                self.period_start.isoformat(),
                self.period_end.isoformat(),
                repr(float(self.value)),
                self.unit,
                self.vintage.isoformat(),
                self.source_id,
            ]
        )
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()

    def with_flags(self, *flags: str) -> "Observation":
        """Return a copy with flags added. Flags are additive, never subtractive.

        There is deliberately no method to remove a flag.
        """
        merged = tuple(sorted(set(self.flags) | set(flags)))
        _check_flags(merged)
        return replace(self, flags=merged)


@dataclass(frozen=True)
class Provenance:
    """Wraps every raw fetch. Written to data/raw/ and never modified."""

    fetch_id: str
    source_id: str
    resolved_url: str
    access_method: AccessMethod
    retrieved_at: datetime
    payload_sha256: str
    payload_path: str
    license: str
    source_vintage: date | None = None
    source_vintage_basis: VintageBasis = VintageBasis.UNKNOWN
    http_status: int | None = None
    notes: str = ""

    def __post_init__(self) -> None:
        if self.source_vintage is None and (
            self.source_vintage_basis is not VintageBasis.UNKNOWN
        ):
            raise SchemaError(
                "source_vintage_basis must be 'unknown' where no vintage is "
                "declared; a guessed vintage is worse than an absent one"
            )
        if "{" in self.resolved_url or "}" in self.resolved_url:
            raise SchemaError(
                f"resolved_url {self.resolved_url!r} looks like an unresolved "
                f"template; schema.md requires the exact URL used"
            )


@dataclass(frozen=True)
class Derivation:
    """Links a derived observation to a rule version and a code SHA."""

    derivation_id: str
    rule_id: str
    rule_version: str
    inputs: tuple[str, ...]
    output: str
    parameters: dict[str, Any]
    computed_at: datetime
    code_sha: str


@dataclass(frozen=True)
class VerdictRecord:
    """One per condition per evaluation year."""

    falsifier_id: str
    evaluation_year: int
    threshold: float | str
    verdict: Verdict
    condition_type: str
    observed_value: float | None = None
    distance_to_threshold: float | None = None
    quantitative_clause: Clause | None = None
    qualitative_clause: Clause | None = None
    adjudication_id: str | None = None
    inputs: tuple[str, ...] = ()
    sensitivity: dict[str, Any] = field(default_factory=dict)
    flags: tuple[str, ...] = ()
    prior_year_amendments: tuple[dict[str, Any], ...] = ()
    authored_by: str | None = None

    def __post_init__(self) -> None:
        if self.condition_type not in {"A", "B", "C", "D"}:
            raise SchemaError(f"condition_type {self.condition_type!r} invalid")
        _check_flags(self.flags)
        # Type B records both clauses separately and is triggered only if both
        # are met. Recording a compound condition as a single boolean discards
        # the information needed to review it.
        if self.condition_type == "B":
            if self.quantitative_clause is None or self.qualitative_clause is None:
                raise SchemaError(
                    f"{self.falsifier_id}: Type B requires both clauses recorded"
                )
            both_met = (
                self.quantitative_clause is Clause.MET
                and self.qualitative_clause is Clause.MET
            )
            if self.verdict is Verdict.TRIGGERED and not both_met:
                raise SchemaError(
                    f"{self.falsifier_id}: triggered requires both clauses met"
                )
        if self.condition_type == "D" and not self.sensitivity:
            raise SchemaError(
                f"{self.falsifier_id}: Type D requires a sensitivity object"
            )
        if self.adjudication_id is not None and self.authored_by is None:
            raise SchemaError(
                f"{self.falsifier_id}: adjudication requires an author"
            )
