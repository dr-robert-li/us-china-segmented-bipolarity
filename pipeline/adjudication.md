# Adjudication framework

Governs every clause that cannot be evaluated by arithmetic alone: the qualitative halves of Type B compound conditions, all of Type C, and the sustained-condition semantics that F7 and F6 depend on.

Committed before the adapters that consume it.

---

## What adjudication means here, stated plainly

This is a single-author research programme. "Adjudication" therefore does not mean a panel, a committee, or an independent referee. It means a **written, dated, source-cited determination that a third party can contest on the record**.

That is a weaker guarantee than institutional review and the framework should not pretend otherwise. Its strength comes from three properties rather than from independence:

1. The determination is written **before** its consequences are known to be favourable or unfavourable, because the trigger rules were fixed in advance.
2. The reasoning is public, so a reader who disagrees can identify precisely where.
3. The evidentiary standard is symmetric between triggering and non-triggering, which removes the most obvious channel for motivated reasoning.

Where an adjudication is genuinely contestable, that fact is recorded in the determination rather than resolved by assertion.

---

## The asymmetry hazard

An analyst with a thesis to defend has an obvious incentive to set a high evidentiary bar for `met` and a low one for `not_met`. Qualitative clauses are where that incentive can operate undetected, because there is no series to check the reasoning against.

Three rules close it.

### Rule 1 -- Symmetric bar

The evidentiary standard for `met` and for `not_met` is identical. Both require affirmative evidence. "Insufficient evidence that the condition occurred" yields `indeterminate`, **not** `not_met`.

This distinction does real work. Under the trigger rules, `not_met` protects the thesis while `indeterminate` does not — an indeterminate qualitative clause on a Type B condition blocks a clean verdict and must be carried forward as unresolved.

### Rule 2 -- Adverse-interest requirement

Before writing the determination, the adjudicator writes the **strongest available case that the clause is met**, with named sources, as though arguing for it. That case is published as part of the adjudication record whether or not the determination follows it.

This mirrors the standing prohibition on unengaged opponents, applied to the analyst's own verdicts rather than to the literature.

### Rule 3 -- Indeterminate must be earned

`indeterminate` is not a default. A determination of `indeterminate` must state what specific evidence would resolve it and whether that evidence could plausibly become available. An `indeterminate` that cannot name its own resolution condition is a failure to adjudicate, not an adjudication.

---

## Evidence standards

| Requirement | Rule |
|---|---|
| Minimum sources | Three independent, for any determination other than `indeterminate` |
| Contemporaneity | Sources dated within the evaluation window, or explicitly retrospective and flagged as such |
| Contrary sources | At least one source arguing against the determination must be cited where any exists |
| Source standing | Peer-reviewed, multilateral-institution, or primary official sources preferred over commentary; standing recorded per source |
| Official PRC or US statements | Admissible as evidence of a position, never as evidence of a fact |
| Anonymous or single-outlet reporting | Insufficient alone for `met` on any clause |

The last two matter for F5 and for F3's cascade clause specifically, where much of the available reporting is of exactly the kind these rules discount.

---

## Adjudication record

```yaml
adjudication:
  adjudication_id: string
  falsifier_id: string        # F3, F5, F7 ...
  clause: string              # which clause of a compound condition
  evaluation_year: integer
  determination: enum         # met | not_met | indeterminate
  adverse_case: string        # REQUIRED. The strongest case for `met`.
  reasoning: string
  sources: [object]           # citation, date, standing, supports_or_opposes
  resolution_condition: string|null  # REQUIRED where determination is indeterminate
  contestable: boolean
  contestable_note: string|null
  authored_by: string
  authored_at: timestamp
  dissent: [object]           # third-party challenges received, with responses
  amendments: [object]        # appended only; never overwrites
```

`adverse_case` may not be empty. A record submitted with an empty `adverse_case` fails validation, in the same way a series descriptor with an empty `definitional_boundary` does.

---

## Sustained-condition semantics

Three pre-registered conditions require a state to persist: F6 over five consecutive years, and F7 over five consecutive years on **both** of its clauses. The semantics below are fixed here so that no discretion enters at evaluation time.

### Recompute, never increment

The run length is **recomputed from scratch at every evaluation**, from the full history of per-year qualification. It is never stored as a counter and incremented.

This is the single most important rule in this section. A stateful counter cannot be corrected when an upstream revision changes a prior year's qualification; a recomputed run can, and does so automatically.

### Per-year qualification

Each year independently qualifies or does not. For conjunctive clauses of the form "X despite Y" -- F7's structure -- **both** sub-conditions must hold within the **same** year for that year to qualify. A year in which TFP growth is negative but robot-density growth has stalled does not qualify, because the condition tests failure of automation to offset, not failure in general.

### Gaps suspend, they do not break

A year with no admissible observation is `indeterminate` for that year. Its effect:

- The run does not advance.
- The run is **not** reset.
- The overall condition verdict becomes `indeterminate` if and only if the gap year is load-bearing, meaning the condition would trigger were the gap year to qualify.

Treating gaps as breaks would let a data outage protect the thesis. Treating gaps as qualifying years would let an outage refute it. Suspension is the only treatment that does neither.

### Revisions can break a run retroactively

If an upstream revision causes a prior year to stop qualifying, the run breaks at that year and the current verdict is recomputed. The prior published verdict is amended, not overwritten, per the annual-log rules.

Runs can therefore shorten as well as lengthen. An adapter that cannot produce a shorter run than it reported last year is implemented incorrectly.

### Consecutiveness spans the deadline

A run that would complete after the pre-registered deadline does not trigger. F7's five-year requirement with a 2040 deadline means the latest qualifying window is 2036 through 2040. A run beginning in 2037 cannot trigger F7 regardless of what follows, and this is a consequence of the pre-registration rather than a defect to be patched.

---

## Compound-condition assembly

For Type B conditions the two clauses are evaluated and recorded separately, then combined:

| Quantitative | Qualitative | Verdict |
|---|---|---|
| met | met | `triggered` |
| met | not_met | `not_triggered` |
| met | indeterminate | `indeterminate` |
| not_met | any | `not_triggered` |
| indeterminate | met | `indeterminate` |
| indeterminate | not_met | `not_triggered` |
| indeterminate | indeterminate | `indeterminate` |

A quantitative `not_met` short-circuits, because the condition is conjunctive and no qualitative finding can rescue it. Nothing else short-circuits.

---

## Timing and freezing

- Adjudications are dated at authoring and published in the annual log for their evaluation year.
- Once published, an adjudication is frozen. Changes are appended as amendments carrying their own date and reasoning.
- An adjudication may not be authored retrospectively for a year whose log has already been published, except as an amendment.
- Where a determination changes on amendment, both the original and the amended determination remain visible.

---

## Prohibitions

- No determination without a written `adverse_case`.
- No `not_met` on absence of evidence alone.
- No `indeterminate` without a stated resolution condition.
- No stateful run counters.
- No adjudication of a quantitative clause. If a clause can be computed, it is computed.
- No substitution of a more favourable source set after a determination has been drafted.

The last prohibition is the hardest to enforce technically and is recorded here so that a reader can at least ask whether it was observed.
