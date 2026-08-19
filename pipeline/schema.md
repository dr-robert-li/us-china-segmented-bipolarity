# Canonical pipeline schema

Shared by all eight falsifier adapters. An adapter that cannot express its output in these structures is an adapter whose condition has not yet been specified precisely enough.

The governing requirement is reconstruction: a stranger holding only `data/raw/` and the committed transformation rules must be able to reproduce every published figure. Everything below exists to serve that.

---

## Design rules

1. **Vintage is a first-class field, not metadata.** Every source series has a publication vintage. Two observations of the same quantity from different vintages are two records, not one record updated.
2. **Revisions append.** An upstream revision produces a new raw record and a re-derivation. Nothing is mutated in place, ever.
3. **Judgement is confined to one layer.** `normalised/` applies no judgement. `derived/` applies only committed rules. `adjudicated/` is the only layer where a human verdict enters, and it carries an author.
4. **Reconciliation fails loud.** Where two sources disagree beyond tolerance, the pipeline emits a flag and refuses to pick a winner. Silent selection of the more convenient source is the specific failure this rule exists to prevent.
5. **Determinism.** Given the same raw inputs and the same rule version, a run produces byte-identical derived output. Non-deterministic steps are prohibited.

---

## Observation

The atomic record. One quantity, one geography, one period, one vintage, one source.

```yaml
observation:
  obs_id: string            # content hash of the canonical fields below
  series_id: string         # FK to series descriptor
  geography: string         # ISO 3166-1 alpha-3: USA, CHN
  period_start: date        # inclusive
  period_end: date          # inclusive
  period_type: enum         # annual | quarterly | monthly | point
  value: number
  unit: string              # FK to unit registry; never inferred
  vintage: date             # publication date of the source release
  source_id: string         # FK to source registry
  retrieved_at: timestamp   # UTC, when this pipeline fetched it
  basis: enum               # reported | differenced | interpolated | estimated
  flags: [string]           # FK to flag taxonomy; empty list is valid
  supersedes: string|null   # obs_id of the prior-vintage record, if any
```

`basis` matters more than it looks. A total-capacity figure taken directly from a release is `reported`. Annual net additions computed by differencing two consecutive year-end totals are `differenced`. The two must never be pooled in one series without the distinction being visible.

## Series descriptor

```yaml
series:
  series_id: string
  name: string
  concept: string           # what is being measured, in prose
  unit: string
  geography_scope: [string]
  definitional_boundary: string   # REQUIRED. See below.
  net_or_gross: enum|null   # net | gross | not_applicable
  coverage_caveats: [string]
  primary_source: string
  crosscheck_sources: [string]
  falsifiers: [string]      # which conditions consume this series
  break_registry: [string]  # FK to entries in DATA-INTEGRITY.md
```

`definitional_boundary` is mandatory free text and may not be empty. It records what the series includes and excludes. Most cross-national comparison errors are boundary errors rather than arithmetic errors, and a required field is the cheapest available guard against them.

## Provenance envelope

Wraps every raw fetch. Written to `data/raw/` and never modified.

```yaml
provenance:
  fetch_id: string
  source_id: string
  resolved_url: string      # the exact URL used, not a template
  access_method: enum       # api | bulk_download | published_table | manual
  retrieved_at: timestamp
  payload_sha256: string
  payload_path: string      # path within data/raw/
  source_vintage: date|null # as declared by the source
  source_vintage_basis: enum # declared | inferred_from_header | unknown
  http_status: integer|null
  license: string
  notes: string
```

Where a source declares no vintage, `source_vintage_basis` records `unknown` rather than a guess. Endpoint paths are resolved at fetch time and recorded here; they are not hardcoded in specifications, because they change and a stale hardcoded path produces a silent wrong answer rather than a failure.

## Derivation record

```yaml
derivation:
  derivation_id: string
  rule_id: string           # FK to a committed rule in pipeline/rules/
  rule_version: string      # semver; bumped on any behavioural change
  inputs: [string]          # obs_ids
  output: string            # obs_id
  parameters: object        # e.g. capacity factors used, with their vintage
  computed_at: timestamp
  code_sha: string          # git SHA of the pipeline at execution
```

Every derived number is traceable to a rule version and a code SHA. A derived figure whose `rule_version` is not committed is not publishable.

## Verdict record

One per condition per evaluation year.

```yaml
verdict:
  falsifier_id: string      # F1 .. F8
  evaluation_year: integer
  observed_value: number|null
  threshold: number|string
  distance_to_threshold: number|null
  verdict: enum             # not_triggered | triggered | indeterminate
  condition_type: enum      # A | B | C | D
  quantitative_clause: enum|null   # met | not_met | indeterminate
  qualitative_clause: enum|null     # met | not_met | indeterminate | n/a
  adjudication_id: string|null
  inputs: [string]          # obs_ids and derivation_ids
  sensitivity: object       # required for Type D; see adapter specs
  flags: [string]
  prior_year_amendments: [object]
  authored_by: string|null  # required where adjudication applies
```

For Type B conditions both clauses are recorded separately and the verdict is `triggered` only if both are `met`. Recording a compound condition as a single boolean discards the information needed to review it.

---

## Flag taxonomy

Flags are additive and never suppress a record.

| Flag | Meaning |
|---|---|
| `definitional_mismatch` | Cross-source comparison spans differing boundaries |
| `source_disagreement` | Cross-checks diverge beyond the series tolerance |
| `vintage_conflict` | Same quantity, same period, materially different values across vintages |
| `structural_break` | Observation spans or abuts a registered break |
| `leadership_transition` | PRC observation window coincides with a provincial leadership transition |
| `basis_mixed` | Series contains both reported and differenced records |
| `interpolated` | Value not directly observed |
| `preliminary` | Source labels the figure provisional |
| `partial_year` | Period shorter than the nominal series frequency |
| `band_applied` | A falsification or error band has been applied |
| `psd_projected` | Correlation matrix required PSD projection at load |

---

## Unit registry

Units are declared, never inferred from magnitude. The registry records the canonical unit per concept and the permitted conversions.

Capacity is canonically **GW**. Sources publishing in kW, MW, or 100 million kW are converted at ingest with the conversion recorded in the derivation record. Energy is canonically **TWh**. Fiscal stocks and flows are canonically **percent of GDP**, with the GDP denominator's own source and vintage recorded, since a ratio inherits two provenance chains rather than one.

---

## Layer transitions

| From | To | Permitted operations |
|---|---|---|
| source | `raw/` | Fetch and hash only. No parsing that discards information. |
| `raw/` | `normalised/` | Parse, unit-convert, map to canonical schema, attach flags. No selection between conflicting sources. |
| `normalised/` | `derived/` | Committed rules only: differencing, rolling averages, ratios, dispatchable adjustment, band application. |
| `derived/` | `adjudicated/` | Human verdicts on qualitative and compound clauses, with author and dissent. |

Selection between conflicting sources is **not** a normalisation operation. Where it is unavoidable it is an adjudication, with an author attached.

---

## Idempotency

`obs_id` is the SHA-256 of the concatenation of `series_id`, `geography`, `period_start`, `period_end`, `value`, `unit`, `vintage`, and `source_id`. Re-fetching unchanged upstream data therefore produces identical identifiers and no new records. A changed value under an unchanged vintage produces a new `obs_id` and raises `vintage_conflict`, which is the intended behaviour: upstream data changing without a vintage bump is a condition the analyst must see.

---

## Run artifact

Each pipeline execution writes a single artifact recording the code SHA, rule versions in force, every `fetch_id`, every flag raised, the verdicts emitted, and any PSD projection applied to the dependence matrix. The annual falsifier log references the run artifact rather than restating it.
