# Falsifier log -- 2026 baseline

First annual log. Recorded **before** any ingestion code exists, so every entry rests on figures read from published sources rather than on pipeline output.

That is a weakness and it is stated rather than concealed. The purpose of this baseline is not precision; it is to put the current position of all eight conditions on the public record with a timestamp, so that no later verdict can be suspected of having been fitted to a model built after the fact.

All entries here are **provisional** and are superseded by the first pipeline run. Supersession is recorded as an amendment, never as an overwrite.

---

## Summary

| ID | Verdict | Observed | Threshold | Distance | Note |
|---|---|---|---|---|---|
| F1 | `not_triggered` | ~9.8% (2025) | 40% | ~30pp | Moved away from threshold in 2025 |
| F2 | `not_triggered` | ~5.9% (2026 est.) | 6.0% | ~0.1pp | Estimate, not outturn; cannot trigger |
| F3 | `not_triggered` | 117.0% (2024) | 180% | ~63pp | Short-circuits; no Clause 2 adjudication required |
| F4 | `indeterminate` | none | -- | -- | Named source does not exist |
| F5 | `not_triggered` (provisional) | none | -- | -- | No formal adjudication authored yet |
| F6 | `not_triggered` | ~42% (Q2 2026) | <30% | ~12pp | Run length 0; moved away |
| F7 | `indeterminate` | not computed | -- | -- | Manufacturing TFP series unavailable |
| F8 | `indeterminate` | ~18.9% (proxy) | 20% | ~1.1pp **below** | Condition satisfied on proxy; band not established |

---

## What the distribution shows

Two conditions sit within roughly one percentage point of their thresholds. Two cannot presently resolve at all. One has no formal adjudication and is provisional. Three are far from triggering.

That is not a well-calibrated falsifier set, and the papers should say so. A set in which the two nearest conditions are also the two whose measurement is least direct -- F8 on estimated compute, F2 on a near-vacuous qualifier -- carries more of its weight on definitional choices than a reader would assume from the threshold table alone.

---

## Dependence-aware accounting

No threshold crossings. `n_eff` is zero and no gate has fired.

Recorded for completeness: the two conditions nearest their thresholds, F8 and F2, sit in **different clusters** -- AI-mechanism and US-resilience respectively -- with a cross-cluster correlation of 0.15. Were both to cross, `n_eff` would be 1.74, below the Gate 2 threshold of 1.8 but close to it. F8 crossing would also engage Gate 3 independently, since F8 maps to the load-bearing pillar.

---

## Amendments

None. This is the initial entry.
