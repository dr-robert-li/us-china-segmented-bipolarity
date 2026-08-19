# Frontier-capable compute: boundary definition

Pre-registered. Prerequisite for `pipeline/adapters/F8.md`.

---

## Why this is a separate file

F8 asks whether PRC aggregate frontier-capable compute remains below 20 percent of the US total through 2032. On the best available public proxy the ratio currently sits at roughly 19 percent. The threshold is therefore inside the range that plausible definitional choices can move.

That is an unusual and uncomfortable position for a pre-registered condition, and it has one honest response: fix the boundary before looking, in a file whose diff history is visible, and accept the verdict the committed definition produces. A boundary chosen after observing the ratio would be worthless, and a boundary buried inside an adapter specification would be too easy to adjust quietly.

F8 bears on P2, the mechanism claim. It is the most damaging condition in the set. Its definition should be the most carefully constrained.

---

## The measurement problem

There is no authoritative public register of training compute. Regulators drafting compute thresholds have acknowledged that no official sources state the FLOP counts of specific frontier models, and thresholds were selected to capture the then-current generation rather than derived from measurement.

Every available construction is therefore an estimate. The task is not to find a true number but to choose the least-bad construction, declare it, and carry its uncertainty explicitly.

---

## Three candidate constructions

### Construction A -- Training-compute attribution from a notable-models database

Sum estimated training compute of frontier models by developer nationality, allocating multinational models across countries. Frontier models are conventionally defined as those in the running top ten by training compute at time of release, a definition preferred over earlier alternatives because it is less sensitive to outliers and to low-compute models.

**Strength.** Directly measures capability at the frontier. Peer-visible methodology.

**Weakness.** Measures a *flow* of publicised training runs, not the *stock* F8 asks about. Publication bias is severe and asymmetric: undisclosed runs are invisible, and disclosure norms differ by jurisdiction.

### Construction B -- Installed frontier-capable accelerator stock

Estimate the installed base of accelerators capable of participating in frontier-scale training, aggregated to national totals.

**Strength.** Matches F8's wording, which asks about aggregate compute rather than about models. Less sensitive to disclosure norms.

**Weakness.** Requires estimating shipments, utilisation, and generational obsolescence, none of which are directly observed.

### Construction C -- National aggregate compute from official statistics

**Rejected.** PRC official compute statistics sum general-purpose, intelligent, and supercomputing power into a single indicator, with published national targets in the low hundreds of EFLOPS. That aggregate is not frontier-capable compute; general-purpose server capacity dominates it.

The figures are also internally inconsistent across state publications: one state think-tank paper computes national total compute at 135 EFLOPS, while another白 paper reports 202 EFLOPS growing at 50 percent and claims 33 percent of the global total. Those are not reconcilable as measurements of the same quantity.

Under the tier rules in `DATA-INTEGRITY.md`, Construction C is inadmissible as the F8 numerator. It is ingested only as context, flagged, and never enters the ratio. The same exclusion applies symmetrically to any US aggregate that mixes general-purpose and frontier-capable capacity.

---

## Committed construction

**Primary: Construction B.** Installed frontier-capable accelerator stock, because F8's wording is about aggregate capacity rather than about published models.

**Cross-check: Construction A.** Training-compute attribution, using the running-top-ten frontier definition and the multinational allocation convention of the source database.

Where A and B disagree on the direction of the PRC/US ratio relative to 20 percent, the verdict is `indeterminate` and both are published. This is the same discipline applied to F1's two ratio constructions.

---

## What "frontier-capable" means

### Rolling, not fixed

A fixed FLOP threshold is rejected. Frontier training compute has grown roughly four to five times per year over the period 2010 to 2024. Regulatory anchors sit at 10^25 FLOP in the EU framework and 10^26 FLOP in California's, and the EU threshold is explicitly described as initial and revisable by delegated act.

Across a 2026 to 2032 evaluation window, any fixed threshold becomes vacuous: a bar set to capture the 2026 frontier would capture nearly everything by 2032, and the ratio would drift for reasons unrelated to relative capability.

**Committed rule.** Frontier-capable means accelerator hardware whose per-device effective throughput is within a factor of **eight** of the highest-throughput device in volume production at the evaluation date, on the declared precision basis below.

The factor of eight is a judgement, pre-registered here, chosen to span roughly two hardware generations. It is reported with sensitivity at factors of four and sixteen. It may not be changed after any evaluation.

### Regulatory thresholds as cross-reference only

The 10^25 and 10^26 FLOP anchors are recorded as external reference points and used to sanity-check that the rolling definition has not drifted into absurdity. They do not define the boundary, because they are model-training thresholds rather than hardware-capability thresholds and they serve a regulatory purpose rather than a measurement one.

---

## Precision basis

Headline vendor throughput figures are not comparable across generations, because successive architectures advertise at progressively lower numeric precision and with sparsity assumed. A ratio built on headline numbers measures marketing convention as much as capability.

**Committed rule.** All device throughput is expressed on a single declared dense precision basis, recorded in the series descriptor. Figures published at other precisions or with sparsity assumed are converted using a documented conversion, with the conversion recorded in the derivation record. Any device for which no conversion to the declared basis is available is excluded and the exclusion is logged.

This is the least glamorous rule in this file and probably the one most likely to change a verdict.

---

## Jurisdictional attribution

Four distinct facts can each be called "national compute", and they diverge materially:

1. **Physical location** of the hardware
2. **Operator nationality** of the entity running the facility
3. **Legal control**, meaning which jurisdiction can compel or restrict use
4. **Effective access**, meaning who can actually run workloads

These are not interchangeable. Analysis of non-US data-centre projects finds that US companies operate roughly 48 percent of them when weighted by investment value, so building capacity domestically does not establish national control of it.

**Committed rule.** Both physical location and operator nationality are recorded for every observation. The headline ratio is constructed on **legal control**, as the concept closest to strategic capability. Effective access through offshore or intermediated capacity is reported as an explicit **adjustment band** on the PRC figure, never folded into the point estimate.

The adjustment band is disclosed as a range because its magnitude is genuinely unknown. Reporting a point estimate for intermediated access would be false precision on the single most contested quantity in the condition.

---

## Uncertainty band

F8 carries a mandatory band rather than a point estimate, reflecting the following, none of which is directly observed:

- shipment estimates and their revision history
- utilisation and effective availability
- generational obsolescence within the rolling window
- precision-conversion assumptions
- offshore and intermediated access
- the difference between Constructions A and B

**Verdict rule.** Where the band straddles the 20 percent threshold, the verdict is `indeterminate`. Where the band lies wholly on one side, the verdict follows.

Given that the current proxy ratio sits close to the threshold, `indeterminate` is a likely outcome for early evaluation years. That is the correct output. A condition this close to its boundary, measured this indirectly, should not return a confident verdict.

---

## Illustrative proxy baseline

Not the committed metric. Recorded so the first pipeline run has something to be checked against, and so that the closeness of the ratio to the threshold is on the record from the outset.

| Quantity | Value | Basis |
|---|---|---|
| PRC share of global AI supercomputer performance | ~14.1% | Synthesis of third-party estimates |
| US share of same | ~74.5% | Same |
| Implied PRC/US ratio | **~18.9%** | Derived |
| F8 threshold | 20% | Pre-registered |

The implied ratio is **below** the threshold, meaning F8's condition is currently satisfied on this proxy. F8 asks whether it *remains* below through 2032, so the operative question is persistence rather than attainment.

Two cautions. The proxy measures AI supercomputer performance rather than frontier-capable stock on the committed definition, so it is indicative only. And a share-of-global construction is not the same as a bilateral ratio; the committed construction is bilateral.

---

## Prohibitions

- PRC official aggregate compute figures may not enter the numerator.
- Fixed FLOP thresholds may not be substituted for the rolling definition.
- Headline vendor throughput at undeclared precision may not be used.
- Intermediated access may not be reported as a point estimate.
- The factor of eight, and the 20 percent threshold, may not be changed after any evaluation.
- No point-estimate verdict where the band straddles the threshold.

---

## Open items

- Select and record the declared precision basis at first implementation.
- Establish the shipment and utilisation estimation method, and its own error characterisation.
- Determine whether a defensible bilateral construction is available from published sources, or whether share-of-global must be used with a stated conversion.
- Characterise the intermediated-access band. This is the largest single source of uncertainty in the condition and currently has no committed estimation method.
