# Dependence structure over F1-F8

Pre-registered. Committed before any threshold crossing has occurred.

---

## Why this file exists

`PRE-REGISTRATION.md` amends the original rule that any two falsifiers reject the core thesis, replacing it with dependence-aware review. That amendment is only defensible if the assumed dependence structure is fixed **in advance**. Otherwise the structure could be chosen after a crossing to produce whichever verdict is convenient, and the amendment would function as an escape hatch rather than as a correction.

This file therefore does three things:

1. Separates what the eight conditions are evidence *about*, since they do not all bear on the same claim.
2. Fixes a prior dependence structure over the conditions, with the mechanism for each dependency stated.
3. Specifies the arithmetic and the gates by which crossings translate into revision or rejection.

---

## Status of the numbers below

The correlation values in this file are **elicited judgements about mechanism, not empirical estimates**. There is no sample of great-power dyads from which they could be estimated, and pretending otherwise would be a worse error than stating them openly as priors.

They are pre-registered for one reason: so that they cannot be adjusted after a crossing. Their function is to constrain the analyst, not to describe the world precisely.

Every verdict that depends on them must be reported alongside the sensitivity re-runs specified below. A verdict that survives only at the elicited values, and flips under a 0.5x or 1.5x rescaling, is reported as **indeterminate** rather than as a verdict.

---

## Three propositions, not one

The programme advances three claims of decreasing specificity. Conflating them would allow evidence against one to be scored as evidence against all three.

| ID | Proposition | Character |
|---|---|---|
| **P1** | Conditional on specified parameter ranges holding through roughly 2050, relative position diverges in China's favour on electricity generation, grid transmission, and industrial robotics deployment | Directional and conditional |
| **P2** | The dimensions on which China is gaining ground are precisely the dimensions the AI-robotics transition disproportionately rewards | The mechanism claim; the sharper and more falsifiable of the three |
| **P3** | Capability divides by domain rather than resolving into a single hierarchy -- segmented bipolarity | Structural, horizon-robust, the expected headline result |

### What each condition is evidence about

| Condition | Primary target | Secondary | Note |
|---|---|---|---|
| F1 | P1, P3 | -- | US convergence on physical build rates undermines both the directional claim and the segmentation |
| F2 | Pillar A (US self-correction) | P1 | Does not bear on P2 or P3 |
| F3 | P1 | -- | Consistent with P3; see below |
| F4 | AI wealth-pump mechanism | -- | Bears on a conditional sub-claim, not on P1-P3 directly |
| F5 | P1 | -- | Consistent with P3 |
| F6 | Pillar A | -- | Does not bear on P2 or P3 |
| F7 | P1, P2 | -- | Failure of robotics to offset contraction attacks the mechanism as well as the direction |
| F8 | **P2** | P3 | The single most damaging condition, because P2 is the load-bearing mechanism claim |

### The asymmetry that must not be lost

Crossings in the PRC-fragility cluster (F3, F5, F7) shift posterior mass toward the peaking-power reading -- that China's window of relative strength is closing rather than opening. That reading is **nested within this programme as a parameter region**, not opposed by it.

Consequently a cluster of PRC-fragility crossings refutes **P1** while leaving **P3** largely intact, and may even strengthen the case that the two theses differ definitionally rather than substantively. Scoring such crossings as refutations of the headline result would be a category error. The accounting below tracks propositions separately for this reason.

---

## Clusters and mechanisms

### Cluster I -- US resilience: F1, F2, F6

All three would be produced, in substantial part, by the same underlying state of the world: a sustained, broad-based US expansion with restored fiscal and administrative capacity.

- **F2-F6** is the strongest dependency in the matrix. Both non-interest discretionary recovery and a durable reversal of graduate underemployment require sustained growth with broad-based labour demand. They are close to two measurements of one condition.
- **F1-F2** is mechanistically direct: large-scale generation and transmission build-out is gated by fiscal room, permitting throughput, and administrative execution capacity.
- **F1-F6** is weaker and runs through labour demand in construction, electrical trades, and engineering.

### Cluster II -- PRC fragility: F3, F5, F7

- **F3-F7** is the dependency named in `PRE-REGISTRATION.md` as the reason for amending the original rule. It is both common-cause and causal: disorderly deleveraging compresses industrial capital expenditure, which directly impairs the automation-offset mechanism F7 tests.
- **F3-F5** runs through elite conflict. Fiscal crisis raises the stakes of intra-elite competition, though the direction of causation is genuinely ambiguous and the magnitude is set low accordingly.
- **F5-F7** runs through industrial-policy continuity: a destructive succession disrupts the sustained execution that the robotics build-out depends on.

### Cluster III -- AI mechanism: F4, F8

These are the least correlated with anything else, which is precisely what makes them valuable. F8 in particular is close to a clean test of P2.

- **F4-F8** is weak and its sign is ambiguous. Persistent compute concentration could slow the diffusion that would produce between-occupation displacement, arguing for a negative relationship; or shared exposure to the pace of AI capability growth could produce a positive one.
- **F4-F6** is the one clearly **negative** entry in the matrix. If AI raises within-occupation wage dispersion, a durable reversal of elite overproduction becomes less likely, not more. The structure is not uniformly positive, and a matrix that were uniformly positive should be treated as a sign of insufficiently examined mechanism.

---

## Pairwise prior correlation matrix

Over latent trigger propensities, under a Gaussian copula. Symmetric; diagonal is unity.

|  | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 |
|---|---|---|---|---|---|---|---|---|
| **F1** | 1.00 | 0.35 | 0.05 | 0.00 | 0.00 | 0.20 | 0.05 | 0.25 |
| **F2** | 0.35 | 1.00 | 0.05 | 0.10 | 0.00 | 0.55 | 0.00 | 0.15 |
| **F3** | 0.05 | 0.05 | 1.00 | 0.00 | 0.25 | 0.00 | 0.45 | 0.10 |
| **F4** | 0.00 | 0.10 | 0.00 | 1.00 | 0.00 | -0.25 | 0.15 | 0.10 |
| **F5** | 0.00 | 0.00 | 0.25 | 0.00 | 1.00 | 0.00 | 0.20 | 0.05 |
| **F6** | 0.20 | 0.55 | 0.00 | -0.25 | 0.00 | 1.00 | 0.00 | 0.10 |
| **F7** | 0.05 | 0.00 | 0.45 | 0.15 | 0.20 | 0.00 | 1.00 | 0.20 |
| **F8** | 0.25 | 0.15 | 0.10 | 0.10 | 0.05 | 0.10 | 0.20 | 1.00 |

Mean within-cluster correlation: Cluster I 0.37, Cluster II 0.30, Cluster III 0.10. Mean cross-cluster correlation: 0.07. That contrast is the substantive content of the matrix -- within a cluster, crossings are close to redundant; across clusters, they are close to independent.

### Machine-readable

```yaml
# falsifiers/dependence.yaml equivalent - consumed by pipeline/threshold_eval
elicited: true
estimated: false
basis: mechanism judgement, pre-registered
copula: gaussian
clusters:
  us_resilience: [F1, F2, F6]
  prc_fragility: [F3, F5, F7]
  ai_mechanism:  [F4, F8]
correlations:
  F1_F2: 0.35
  F1_F3: 0.05
  F1_F4: 0.00
  F1_F5: 0.00
  F1_F6: 0.20
  F1_F7: 0.05
  F1_F8: 0.25
  F2_F3: 0.05
  F2_F4: 0.10
  F2_F5: 0.00
  F2_F6: 0.55
  F2_F7: 0.00
  F2_F8: 0.15
  F3_F4: 0.00
  F3_F5: 0.25
  F3_F6: 0.00
  F3_F7: 0.45
  F3_F8: 0.10
  F4_F5: 0.00
  F4_F6: -0.25
  F4_F7: 0.15
  F4_F8: 0.10
  F5_F6: 0.00
  F5_F7: 0.20
  F5_F8: 0.05
  F6_F7: 0.00
  F6_F8: 0.10
  F7_F8: 0.20
```

### Positive semi-definiteness

The matrix must be checked for positive semi-definiteness at pipeline load. If it fails, it is projected to the nearest PSD matrix by eigenvalue clipping, and **both** the original and projected matrices are recorded in the run artifact. The projection is never applied silently.

---

## Effective-evidence accounting

For a set of k triggered conditions with mean pairwise correlation rho_bar drawn from the matrix above:

```
n_eff = k / (1 + (k - 1) * rho_bar)
```

This is the standard effective-count adjustment for correlated indicators. It has the properties required here: independent crossings count fully, perfectly correlated crossings count once, and the intermediate cases interpolate.

Worked values for two crossings:

| Pair | rho | n_eff | Reading |
|---|---|---|---|
| F2, F6 | 0.55 | 1.29 | Close to a single observation. Not two refutations. |
| F3, F7 | 0.45 | 1.38 | The pair that motivated the amendment. |
| F1, F2 | 0.35 | 1.48 | Substantially redundant. |
| F1, F8 | 0.25 | 1.60 | Redundant, but see the pillar-concentration gate. |
| F1, F3 | 0.05 | 1.90 | Effectively two independent refutations. |
| F4, F5 | 0.00 | 2.00 | Fully independent. |

---

## Rejection gates

Three gates operate in parallel. Any one of them firing is sufficient to trigger its stated consequence.

### Gate 1 -- Pillar revision (unchanged)

Any single threshold crossing triggers mandatory revision of its associated pillar. No dependence adjustment applies, because no aggregation is being performed.

### Gate 2 -- Dependence-aware rejection review

Fires when **both** conditions hold:

- `n_eff >= 1.8` over the set of crossings mapped to the proposition under test, and
- posterior probability of that proposition falls below **0.25** under the estimated model

The threshold of 0.25 is pre-registered here and may not be lowered after a crossing. Accounting is performed **separately for P1, P2 and P3**, since the conditions do not bear on them equally.

A review that fires Gate 2 and nonetheless declines to reject must publish which parameter regions survive and why.

### Gate 3 -- Pillar concentration

Fires when two or more crossings map to the **same load-bearing pillar**, regardless of `n_eff`.

This gate exists because Gate 2 would otherwise under-react to the most damaging possible evidence. F1 and F8 both attack the resource-scale and mechanism claims that carry the primary weight of the argument; their correlation of 0.25 yields `n_eff = 1.60`, below the Gate 2 threshold. Yet both crossing would mean the load-bearing pillar had failed on two distinct measurements.

Consequence: the pillar is reconstructed or abandoned as load-bearing. If Pillar D is abandoned as load-bearing, the programme has no remaining load-bearing pillar and the core thesis is withdrawn rather than revised.

---

## Worked scenarios

Illustrative only. These are not predictions and carry no probability assignment.

| Crossings | n_eff | Gates fired | Consequence |
|---|---|---|---|
| F2 alone | -- | 1 | Revise Pillar A |
| F2 and F6 | 1.29 | 1 | Revise Pillar A. Gate 2 not reached: these are near-duplicate measurements of US resilience. |
| F3 and F7 | 1.38 | 1 | Revise the PRC-stress treatment. P1 weakened; **P3 untouched** -- consistent with the peaking-power region. |
| F3, F5 and F7 | 1.61 | 1 | Full PRC-fragility cluster. P1 likely rejected on posterior evidence; P3 survives; the peaking-power reading becomes the dominant parameter region. |
| F1 and F8 | 1.60 | 1, **3** | Pillar D reconstructed or abandoned as load-bearing. Highest-severity outcome in the scheme. |
| F1 and F3 | 1.90 | 1, 2 | Rejection review on P1 with effectively two independent refutations. |
| F8 alone | -- | 1 | Revise P2. Because P2 is the mechanism claim, a single F8 crossing is more damaging than most pairs elsewhere. |

Note that F8 alone is treated as more serious than F2 and F6 together. That ordering is deliberate: severity tracks which proposition is hit, not how many boxes are ticked.

---

## Mandatory sensitivity re-runs

Every verdict invoking Gate 2 is reported at four settings:

1. Elicited matrix as committed above
2. All off-diagonal entries scaled by **0.5**
3. All off-diagonal entries scaled by **1.5**, with PSD projection as needed
4. **Independence** -- the original unamended rule, as the reference case

Setting 4 is included so that a reader can see exactly what the amendment changed. If the amended rule and the original rule disagree, both verdicts are published side by side and the disagreement is the finding.

A verdict stable across all four settings is reported as a verdict. A verdict that flips is reported as **indeterminate**, with the flip point stated.

---

## Revision rules

- Correlation values may be revised **only** with a committed mechanism argument in the commit message, and **only** where no relevant condition has yet crossed its threshold.
- Once any condition in a cluster has crossed, correlations involving that condition are frozen.
- Adding a dependency is permitted; removing one requires the same standard as adding.
- The Gate 2 posterior threshold of 0.25 and the `n_eff` threshold of 1.8 are frozen from this commit and may not be changed at all.
- No condition may be moved between clusters after any crossing.

The purpose of the freeze rules is narrow and worth stating plainly: to remove the analyst's ability to change the scoring after seeing the score.

---

## Amendment 1 -- 2026-08-20 -- caveat: `n_eff` assumes every falsifier is a live test

**Appended, not substituted. Nothing frozen moves.** The Gate 2 posterior threshold of 0.25 and the `n_eff` threshold of 1.8 are frozen by the revision rules above and are not changed, recomputed, or reinterpreted by this amendment. This is a recorded caveat on how much the gates can be read as guaranteeing, and it runs **against** the project's falsifiability claim, which is why it must be recorded rather than left implicit.

### The assumption, made explicit

```
n_eff = k / (1 + (k - 1) * rho_bar)
```

treats each of the `k` crossings as one unit of evidence, discounted only for correlation with the others. That presupposes each falsifier is a **live test**: that its counting rules can actually register the event class its condition describes.

### Why the assumption is now known to fail for one clause

F5 Sub-clause B carries a demonstrated false-negative mode, registered 2026-08-19 (`../pipeline/adapters/F5.md`, Amendment 3): its committed anchoring rule returns `not_met` on the archetypal historical positive case, because the rule is anti-correlated with the irregularity the clause measures. A clause that can fail to see its own event class contributes **less than one** live test to the set -- and, symmetrically, its *non*-crossing contributes less than one unit of corroboration.

The consequence runs in one direction. F5 is less able to cross than the arithmetic assumes, so the set's effective independence is overstated and the rejection gates are **harder to fire than `n_eff` implies**. The gates cannot err toward rejecting the thesis through this defect; they can only err toward sparing it.

### What follows, and what does not

- Every Gate 2 report in which F5 participates carries this caveat alongside the `n_eff` arithmetic.
- The papers state it wherever the eight-condition architecture is described.
- **No recomputation follows.** Down-weighting F5 inside `n_eff` would require choosing a discount factor after observing the defect, which is scoring-after-seeing-the-score -- the exact move the freeze rules exist to prevent. The honest treatment is the arithmetic as committed plus this caveat in the open.
- If `F5-B-ANCHOR-2` is adopted for 2027 under its registered conditions, the caveat narrows to evaluation years 2026 and earlier; it is not deleted.

### Sources for Amendment 1

- pipeline/adapters/F5.md, Amendment 3 (internal; the registered false-negative mode and its directionality note)
- falsifiers/adjudications/dry-run/1976.md (internal; the demonstration)
