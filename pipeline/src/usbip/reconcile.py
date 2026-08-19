"""Cross-source reconciliation.

Implements schema.md design rule 4: where two sources disagree beyond tolerance,
the pipeline emits a flag and refuses to pick a winner. Silent selection of the
more convenient source is the specific failure this module exists to prevent.

There is deliberately no ``resolve()`` function. Selection between conflicting
sources is not a normalisation operation; where it is unavoidable it is an
adjudication with a named author, and that lives in the adjudicated layer.
"""

from __future__ import annotations

from dataclasses import dataclass

from .schema import Observation, SchemaError


@dataclass(frozen=True)
class Disagreement:
    series_id: str
    geography: str
    year: int
    primary_value: float
    crosscheck_value: float
    crosscheck_source: str
    relative_gap: float
    tolerance: float
    breached: bool

    @property
    def message(self) -> str:
        verb = "exceeds" if self.breached else "within"
        return (
            f"{self.series_id}/{self.geography} {self.year}: primary "
            f"{self.primary_value:.4g} vs {self.crosscheck_source} "
            f"{self.crosscheck_value:.4g}, gap {self.relative_gap:.2%} {verb} "
            f"tolerance {self.tolerance:.2%}"
        )


def compare(
    primary: Observation,
    crosscheck: Observation,
    *,
    tolerance: float,
) -> Disagreement:
    """Compare a primary observation against a cross-check.

    The gap is expressed relative to the **cross-check** value, not the primary.
    The F1 adapter states the tolerance as a percentage "of the national figure",
    and the national source is the cross-check under that adapter's deliberately
    inverted source design. Using the primary as the denominator would be a
    different and looser test whenever the primary is the larger figure.
    """
    if primary.unit != crosscheck.unit:
        raise SchemaError(
            f"reconcile: unit mismatch {primary.unit} vs {crosscheck.unit}"
        )
    if primary.geography != crosscheck.geography:
        raise SchemaError("reconcile: geography mismatch")
    if crosscheck.value == 0:
        raise SchemaError("reconcile: cross-check value is zero; gap undefined")

    gap = abs(primary.value - crosscheck.value) / abs(crosscheck.value)
    return Disagreement(
        series_id=primary.series_id,
        geography=primary.geography,
        year=primary.period_end.year,
        primary_value=primary.value,
        crosscheck_value=crosscheck.value,
        crosscheck_source=crosscheck.source_id,
        relative_gap=gap,
        tolerance=tolerance,
        breached=gap > tolerance,
    )


def detect_vintage_conflict(
    a: Observation, b: Observation, *, material_threshold: float = 0.01
) -> str | None:
    """Distinguish a vintage conflict from a large vintage revision.

    Two cases, and the 2026 F3 review established that they are different
    objects:

    - Same vintage, materially different value: ``vintage_conflict``. Upstream
      data changed without a vintage bump, which the analyst must see.
    - Different vintage, revision above 10 percent of the earlier value:
      ``vintage_revision_large``. This is a legitimate supersession, but the F3
      amendment recorded that a roughly 18-point revision passed unflagged
      because the source-disagreement tolerance was calibrated for construction
      spread rather than supersession. The flag closes that gap.

    Returns the flag name or ``None``.
    """
    if a.series_id != b.series_id or a.geography != b.geography:
        raise SchemaError("vintage check: records are not the same quantity")
    if (a.period_start, a.period_end) != (b.period_start, b.period_end):
        raise SchemaError("vintage check: records cover different periods")
    if a.value == 0 and b.value == 0:
        return None

    earlier, later = sorted([a, b], key=lambda o: o.vintage)
    base = abs(earlier.value) or abs(later.value)
    relative = abs(later.value - earlier.value) / base

    if a.vintage == b.vintage:
        return "vintage_conflict" if relative > material_threshold else None
    return "vintage_revision_large" if relative > 0.10 else None
