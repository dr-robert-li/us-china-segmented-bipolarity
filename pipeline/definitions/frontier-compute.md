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

**Status note, 2026-08-20.** The first item was resolved by `precision-basis.md` (dense BF16/FP16 tensor, governing R004). The remaining three are resolved by Amendment 1 below.

---

## Amendment 1 -- 2026-08-20 -- the three remaining open items resolved: Construction B estimation method, intermediated-access band, bilateral construction

**Appended, not substituted. No threshold, factor, precision-basis, attribution-rule, or verdict-rule changes.** All selections were made by author decision of 2026-08-20 in structured Q&A; candidates and grounds recorded below.

### Scope: why this is permissible while the F8 fix window is shut

The F8 dry run of the same date was flag-only, because the live proxy sits ~1 point from the threshold. That scope bound the *dry-run exercise*: defects it found are flagged, not fixed. This amendment is the separate authored-decision path -- it completes items this file pre-registered as pending selection "at first implementation", before any F8 verdict has ever been emitted. No published figure exists to recompute; the registry's recomputation obligation is not in play.

**Post-observation acknowledgment.** These selections are made with the ratio path known -- the ~19 percent proxy and the 17.3 percent tracked-cluster value for 2025 alike. That was equally true when this file was first committed ("the ratio currently sits at roughly 19 percent" is in the original text), and the remedy is the same one the file itself prescribes: commitment in a diff-visible file, the mandatory sensitivity grid, and `indeterminate` wherever constructions or bands disagree. None of those guards is touched here, and all remain binding.

**Direction disclosure.** Committing the tracked-cluster construction moves the live position from the ~19 percent proxy to 17.3 percent -- further below the threshold, in the thesis-favourable direction (margin ~1.0 point to ~2.7 points). This direction was disclosed in the Q&A text *before* the author selected, and the selection grounds below are statable without reference to any verdict. The A-versus-B direction-disagreement rule (verdict `indeterminate`, both published) is the standing guard against this choice ever suppressing a contrary construction.

### Resolution 1 -- Construction B is the tracked-cluster stock

**Committed.** Construction B is estimated as the cumulative installed 16-bit OP/s of tracked AI clusters from the third-party AI-supercomputers dataset family the adapter already names as primary -- concretely, the Epoch AI supercomputers dataset construction demonstrated end-to-end in the dry run (`falsifiers/adjudications/dry-run/F8-2021-2025.md`, snapshot sha256 3c158f22...): clusters flagged for standard analysis, status Existing or Decommissioned, operational by year-end, decommissioned clusters removed from later years, throughput on the R004 declared dense basis.

**Verdict-blind grounds.** The stock is *enumerated rather than estimated*: no shipment volume, destination attribution, or utilisation rate needs to be modelled, which removes the three least observable quantities in the alternative. The dataset is public, snapshot-able byte-exactly under the standing snapshot rule, country-attributed at cluster level, and records decommission dates.

**Error characterisation.** The dominant error source is coverage asymmetry -- tracked clusters are a subset of installed capacity, and tracking completeness differs by jurisdiction and era (documented in the dry run for 2019--2021). Coverage uncertainty **replaces** shipment-and-utilisation uncertainty as the first component of the Step 4 band in `adapters/F8.md`. At first ingest, the dataset's own published coverage estimates are snapshotted and carried as the coverage component of the band; if the publisher states none for a period, the coverage component is bounded by the Construction A comparison and the bound is logged as such.

**Candidates declined.** Shipment-flow accumulation (analyst vendor-shipment estimates by destination x depreciation x assumed utilisation): destination attribution is unverifiable in the export-control era, utilisation is unobserved, and the error is uncharacterisable -- it fails the requirement this item exists to satisfy. A hybrid with a shipment-flow upper-bound check: adds machinery without need, since Construction A is already the mandated cross-check in the sensitivity grid.

**Persistence-clock consequence, stated rather than left implicit.** On the committed construction the condition first holds in **2025** (2024 = 20.6 percent, 2025 = 17.3 percent). The "remains below" clock therefore starts at 2025, resolving dry-run Finding 3 (clock start was construction-dependent) by commitment. The clock is still recomputed from scratch at every evaluation per the adapter's persistence semantics.

### Resolution 2 -- the intermediated-access band is estimated by bounded enumeration

**Committed.** The band on the PRC figure is `[0, U]`, where:

- The **lower bound is zero**, coinciding with mandated sensitivity setting 5 (no adjustment).
- The **upper bound U** is the sum of *citable public reporting only*: documented PRC-linked offshore and intermediated cloud capacity, and documented diversion reporting, each converted to the R004 declared dense basis. A component with no citable quantity is **excluded and logged**, never guessed at. Each component in U carries its source, snapshot hash, and conversion record.
- U is re-enumerated at every evaluation year; revisions to prior components are logged, not silently absorbed.

**Grounds.** This is the only candidate whose every component is auditable to a source. It contains no modelled parameter, so it cannot smuggle a point estimate in through an assumption -- the prohibition on point estimates for this quantity is preserved structurally, not just procedurally.

**Candidates declined.** A proportional band (fixed percentage of US-operated offshore capacity assumed PRC-accessible): the percentage is an arbitrary modelled parameter, exactly the false precision the prohibition targets. Deferral (zero-adjustment lower bound only, provisional monitoring output indefinitely): leaves the condition unable to publish a verdict through 2032, which converts F8 into a second F7 by inaction rather than by argument.

**Known ceiling, stated.** Bounded enumeration undercounts by construction -- unreported intermediated access is invisible to it. That bias is one-directional and disclosed: U is a floor on the true upper bound, and the band is reported with that caveat wherever F8 figures appear.

### Resolution 3 -- the bilateral construction is available and committed

**Committed.** The bilateral ratio is computed directly from cluster-level country attribution aggregated to national totals. No share-of-global conversion enters the primary construction. The dry run demonstrated this end-to-end: national aggregates for both countries from one dataset, no global denominator.

**Grounds.** A share-of-global construction imports rest-of-world coverage error into a bilateral quantity. The direct bilateral is strictly less exposed and was demonstrated feasible on the committed source.

**Candidate declined.** Share-of-global with stated conversion (the ~14.1/74.5 proxy style): retained only as the historical context of the illustrative baseline above; never the primary.

### What this amendment does not do

- It does **not** close `construction_spread_exceeds_margin` (registered against `adapters/F8.md`). Committing one construction does not shrink the spread across the mandated sensitivity grid -- settings 1 through 5 are still all reported, and the flag closes only when a first-ingest grid shows the committed construction's near-threshold verdicts survive the alternatives.
- It does **not** permit publication yet. The specification-level block ("F8 should not emit a published verdict until...") is closed, but publication waits on first ingest actually running: the five-setting grid computed, coverage estimates snapshotted, U enumerated. The block moved from "method unspecified" to "first ingest not yet run".
- It does **not** alter the reclassification note's direction constraint, the prohibitions list, or any persistence semantics.

### Registry

The two derivations committed here are registered as **R010** (tracked-cluster stock construction, feeding `compute_frontier_stock`) and **R011** (intermediated-access bounded-enumeration band, feeding `compute_intermediated_band`) in `pipeline/rules/README.md`, both at 0.1.0: specified, but their error characterisation and enumeration are not yet exercised at a first ingest, and a rule whose coverage component has never been computed is not at 1.0 merely because it is written down.

### Sources for Amendment 1

- Author Q&A of 2026-08-20 (structured; three selections, all recommended options adopted; direction of the Construction B selection disclosed in the question text before selection)
- falsifiers/adjudications/dry-run/F8-2021-2025.md (internal; the demonstrated construction, the ratio path, Findings 2 and 3)
- https://epoch.ai/data/charts/supercomputers/insights/gpu_clusters.csv (snapshot sha256 3c158f22fff0c55816b7235e909d6994c51d27a84469955d326289c71224237a)
- pipeline/definitions/precision-basis.md (internal; the R004 basis and conversion table)
