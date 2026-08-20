"""F1 first ingest -- committed snapshots to derived series to verdict record.

Reads ONLY content-addressed snapshots committed under research/snapshots/store
(no network), applies the registered rules (R013 summation, R001 differencing,
R002 rolling ratio via the adapter), reconciles against the basis-matched
cross-check pair committed in adapters/F1.md Amendment 2, and writes
data/derived/f1/. Deterministic: identical snapshots and rule versions produce
byte-identical output; every constant that would otherwise be a clock read is a
named literal below.

Snapshot provenance (sha256, all in research/snapshots/INDEX.md):

- Ember yearly long format: 259e1095... (fetched 2026-08-20)
- EIA existcapacity_annual.xlsx (EIA-860, nameplate, 1990-2024): faefdee9...
- NEA year-end totals: end-2022 36851905..., end-2023 1d85498a...,
  end-2024 21a36b4d..., end-2025 59cf8553...

Capacity bases, per Amendment 2: Ember is a nameplate-family composite (GEM
coal/gas gross >50 MW + IRENA non-fossil; methodology snapshot 4044e49f...);
EIA nameplate is the EIA-860 "Nameplate Capacity" column; NEA is grid-connected
installed. All three carry ``capacity_basis=nameplate_family`` so the
reconciliation basis guard (F1 test 8) admits the pair and would reject a
net-summer series.
"""

from __future__ import annotations

import csv
import json
import re
from datetime import date, datetime, timezone
from pathlib import Path

from .adapters import f1
from .schema import Basis, Observation, PeriodType

REPO = Path(__file__).resolve().parents[3]
STORE = REPO / "research" / "snapshots" / "store"
OUT = REPO / "data" / "derived" / "f1"

EMBER_SHA = "259e1095ee8ffeaf0aff37ad557916ae1823a2da13312da50ba4cec6b4574c3b"
EIA_SHA = "faefdee9e0fade582bcde6c74634aff9406db6d577758fbb18ab2bb71e94c262"
NEA_SHAS = {
    2022: "36851905f66d2a4878650f6dece48968cb5695e8f7e382c3329afbb48c172bbf",
    2023: "1d85498a600b8201a138c068e6780a0e838a9d35cc0c22bed7ee0b45ba00b5ba",
    2024: "21a36b4d4addc64a641266c953870034573a43bb3a3dccb43d1e1b7a7cbeddcf",
    2025: "59cf855315b4150bde55dadb4586732985e9521def3c3c2182f8ad15c22f5eea",
}

# Snapshot fetch timestamps, from INDEX.md; named literals, not clock reads.
EMBER_RETRIEVED = datetime(2026, 8, 20, tzinfo=timezone.utc)
CROSS_RETRIEVED = datetime(2026, 8, 21, tzinfo=timezone.utc)

BASIS_FLAG = "capacity_basis=nameplate_family"

# Evaluation year: the latest year with a complete three-year additions window
# on the primary series. 2026 is incomplete; the 2026 annual determination in
# falsifiers/log/2026/F1.md remains the published determination, and its own
# text commits that first-ingest re-derivation supersedes its secondary basis.
EVALUATION_YEAR = 2025
TOTAL_YEARS = range(2022, 2026)  # totals 2022-2025 -> additions 2023-2025


def _obs(series, geo, year, value, source, vintage, retrieved, flags=()) -> Observation:
    return Observation(
        series_id=series,
        geography=geo,
        period_start=date(year, 1, 1),
        period_end=date(year, 12, 31),
        period_type=PeriodType.ANNUAL,
        value=value,
        unit="GW",
        vintage=vintage,
        source_id=source,
        retrieved_at=retrieved,
        basis=Basis.REPORTED,
        flags=(BASIS_FLAG, *flags),
    )


def load_ember_totals() -> dict[str, dict[int, Observation]]:
    """R013: pinned-whitelist fuel-row summation with Clean+Fossil validation."""
    from .rules import r013_total_from_fuel_rows

    fuel: dict[tuple[str, int], dict[str, float]] = {}
    agg: dict[tuple[str, int], dict[str, float]] = {}
    geo_map = {"China": "CHN", "United States of America": "USA"}
    with open(STORE / f"{EMBER_SHA}.csv", newline="") as fh:
        for row in csv.DictReader(fh):
            geo = geo_map.get(row["Area"])
            if geo is None or row["Category"] != "Capacity":
                continue
            year = int(row["Year"])
            if year not in range(min(TOTAL_YEARS), max(TOTAL_YEARS) + 1):
                continue
            key = (geo, year)
            if row["Subcategory"] == "Fuel":
                fuel.setdefault(key, {})[row["Variable"]] = float(row["Value"])
            elif row["Subcategory"] == "Aggregate fuel" and row["Variable"] in (
                "Clean",
                "Fossil",
            ):
                agg.setdefault(key, {})[row["Variable"]] = float(row["Value"])

    out: dict[str, dict[int, Observation]] = {"USA": {}, "CHN": {}}
    for (geo, year), fuels in sorted(fuel.items()):
        cpf = agg.get((geo, year))
        total = r013_total_from_fuel_rows(
            fuels,
            clean_plus_fossil=(
                cpf["Clean"] + cpf["Fossil"] if cpf and len(cpf) == 2 else None
            ),
            geography=geo,
            year=year,
        )
        out[geo][year] = _obs(
            "cap_total_installed", geo, year, total, "ember", date(2026, 8, 20),
            EMBER_RETRIEVED,
        )
    return out


def load_eia_nameplate() -> dict[int, Observation]:
    """US cross-check: EIA-860 nameplate annual totals (file ends at 2024)."""
    import openpyxl

    wb = openpyxl.load_workbook(STORE / f"{EIA_SHA}.xlsx", read_only=True)
    out: dict[int, Observation] = {}
    for r in wb.worksheets[0].iter_rows(values_only=True):
        if (
            r
            and r[0] in TOTAL_YEARS
            and r[1] == "US"
            and r[2] == "Total Electric Power Industry"
            and r[3] == "All Sources"
        ):
            out[int(r[0])] = _obs(
                "cap_total_installed", "USA", int(r[0]), float(r[6]) / 1000.0,
                "eia_860_existcapacity", date(2025, 10, 1), CROSS_RETRIEVED,
            )
    return out


def load_nea_totals() -> dict[int, Observation]:
    """PRC cross-check: NEA year-end totals, parsed from the snapshotted
    releases. NEA reports in units of 1e8 kW ("亿千瓦"), to one decimal --
    coarse precision, carried as a flag."""
    out: dict[int, Observation] = {}
    for year, sha in NEA_SHAS.items():
        if year not in TOTAL_YEARS:
            continue
        text = (STORE / f"{sha}.html").read_text(errors="ignore")
        m = re.search(r"全国累计发电装机容量约?([0-9.]+)亿千瓦", text)
        if not m:
            raise RuntimeError(f"NEA total not found in snapshot for {year}")
        out[year] = _obs(
            "cap_total_installed", "CHN", year, float(m.group(1)) * 100.0,
            "nea_annual_release", date(year + 1, 1, 28), CROSS_RETRIEVED,
            flags=("coarse_precision_1e8_kw",),
        )
    return out


def run(code_sha: str) -> f1.F1Result:
    primary = load_ember_totals()
    crosscheck = {"USA": load_eia_nameplate(), "CHN": load_nea_totals()}
    result = f1.evaluate(
        totals_primary=primary,
        totals_crosscheck=crosscheck,
        evaluation_year=EVALUATION_YEAR,
        code_sha=code_sha,
    )

    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / "cap_total_installed.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["series_id", "geography", "year", "value_gw", "source", "flags"])
        for geo in ("USA", "CHN"):
            for year, obs in sorted(primary[geo].items()):
                w.writerow([obs.series_id, geo, year, f"{obs.value:.1f}", obs.source_id, ";".join(obs.flags)])
            for year, obs in sorted(crosscheck[geo].items()):
                w.writerow([obs.series_id, geo, year, f"{obs.value:.1f}", obs.source_id, ";".join(obs.flags)])
    with open(OUT / "cap_additions_net.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["series_id", "geography", "year", "value_gw", "basis", "flags"])
        for obs in result.derived:
            w.writerow([obs.series_id, obs.geography, obs.period_end.year, f"{obs.value:.1f}", obs.basis.value, ";".join(obs.flags)])
    v = result.verdict
    with open(OUT / f"verdict-{EVALUATION_YEAR}.json", "w") as fh:
        json.dump(
            {
                "falsifier_id": v.falsifier_id,
                "evaluation_year": v.evaluation_year,
                "threshold": v.threshold,
                "verdict": v.verdict.value,
                "observed_value": v.observed_value,
                "distance_to_threshold": v.distance_to_threshold,
                "sensitivity": v.sensitivity,
                "flags": list(v.flags),
                "notes": result.notes,
                "disagreements": [d.message for d in result.disagreements],
                "blocked_years": result.blocked_years,
                "code_sha": code_sha,
                "snapshots": {
                    "ember": EMBER_SHA,
                    "eia": EIA_SHA,
                    "nea": NEA_SHAS,
                },
            },
            fh,
            indent=2,
        )
    return result


if __name__ == "__main__":
    import subprocess

    sha = subprocess.run(
        ["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=REPO
    ).stdout.strip()
    res = run(code_sha=sha)
    print(res.verdict.verdict.value, res.verdict.observed_value)
    for n in res.notes:
        print("-", n)
