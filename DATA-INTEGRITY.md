# Data integrity protocol

This protocol is binding on every series entering the model. It exists because the comparison at the centre of this programme is between two states whose official statistics have different, but both non-trivial, reliability problems -- and because scrutinising one side while accepting the other uncritically would be a methodological error serious enough to discredit the result.

---

## Preferred-series hierarchy

Where a choice exists, prefer in this order:

1. **Physically measurable** -- electricity generation and installed capacity, satellite luminosity, robot installation counts
2. **Independently audited or multilaterally compiled** -- IMF and BIS external accounts, customs-mirror trade statistics, UN population projections
3. **National official statistics with published methodology** -- admissible with the adjustments below
4. **National official statistics without published methodology** -- admissible only with an explicit uncertainty band and a flag

The load-bearing claims of this programme are deliberately built on tier 1 and tier 2 series, so that they do not depend on contested national accounts on either side.

---

## PRC series

### Falsification band

Chinese official statistics are **not admissible unadjusted**. This is not a rhetorical caution; it rests on a specific peer-reviewed literature.

The established findings are that provincial GDP figures are systematically more likely to be inflated in years coinciding with provincial leadership turnover, because career advancement is tied to quantified performance metrics that officials have both the means and the incentive to manipulate; that nighttime-lights satellite luminosity studies imply authoritarian regimes systematically overstate reported growth relative to physical light emission, with the magnitude varying by regime type; and that a tax-and-revenue reconstruction estimated growth overstatement of roughly 1.7 percentage points annually between 2008 and 2016, while a separate satellite-only exercise arrived at a materially smaller correction.

**That disagreement is preserved as a parameter range, not resolved by analyst preference.**

Operational rule: apply an explicit falsification band of approximately **0.5 to 2.0 percentage points** on GDP-linked annual growth series, and report results across the full band rather than at a point estimate. The band enters as an estimated drag parameter inside net-resource efficiency, not as a footnote caveat.

### Observation-window flags

Any observation window coinciding with a provincial leadership transition is flagged in the normalised layer and carries a widened band.

### The reflexivity problem

The same quantified-performance system that incentivises falsification also supplies the inputs any centralised planning apparatus would ingest. A planning system trained on systematically distorted data cannot straightforwardly function as a stabilising mechanism. This is treated as a first-order modelling problem: the stabilisation-capacity coefficient is **estimated**, not assumed positive, and is permitted to take a negative value.

---

## US series

Symmetric scepticism is mandatory.

- **Fiscal projections** carry the projecting agency's own published historical projection-error record as an explicit error band. Long-horizon fiscal paths are not treated as point forecasts.
- **Income inequality** is carried as a **range** spanning the major competing measurement approaches, whose disagreement is well known and unresolved. Collapsing that disagreement into a single figure is prohibited.
- **Labour underemployment** definitions vary across sources; the definitional choice is committed in advance and its sensitivity reported.

Any American structural pathology entered into the model must have its Chinese analogue assessed on the same scale, and vice versa.

---

## Mandatory transformations

### Nameplate to dispatchable

Installed generation capacity is never used directly. Recent Chinese capacity additions have been overwhelmingly wind and solar, so capacity factors and curtailment losses materially reduce effective available energy relative to headline gigawatt figures. All energy inputs are converted to **expected dispatchable output using published capacity factors** before entering any production function. The conversion factors and their vintage are recorded in the derived layer.

### Frontier compute is not energy

Frontier-scale training compute and bulk deployment power are **distinct inputs with separate trajectories**. Export-control regimes on advanced semiconductors mean the two are governed by different constraints. Folding them into a single undifferentiated technology-capacity variable is prohibited, and doing so would beg precisely the question the programme is testing.

### Augmented over headline fiscal measures

Comparative fiscal-constraint modelling uses augmented debt measures -- those including local government financing vehicle liabilities and off-budget funds -- rather than headline general-government figures. The gap between the two is large enough that the choice determines the result.

---

## Known structural breaks

Breaks are registered here before they are encountered in analysis. A series is never spliced across a break without an explicit, committed bridging rule.

| Series | Break | Consequence |
|---|---|---|
| PRC urban youth unemployment, ages 16-24 | Methodology revised in December 2023 to exclude students from the denominator | Pre- and post-2023 values are **not directly comparable**. Longitudinal analysis must treat this as a structural break, not a level shift. |
| Occupational AI-exposure measures | Successive revisions to the underlying exposure index | F4 coding rule must name the index vintage |
| Robot-density series | Periodic reclassification of industry categories | Recorded per vintage in the normalised layer |

Additional breaks are appended as discovered, with the discovery date recorded.

---

## Layer discipline

| Layer | Rule |
|---|---|
| `data/raw/` | **Append-only.** Never edited in place. Each fetch records source URL, retrieval timestamp, and series vintage. |
| `data/normalised/` | Schema-conformed, unit-harmonised, provenance-tagged. No judgement applied. |
| `data/derived/` | Transformations only, each traceable to a committed rule: dispatchable adjustment, rolling averages, ratios, band application. |
| `data/adjudicated/` | Human verdicts on compound and qualitative conditions, each with named author and dissent record. |

A revision to an upstream source produces a **new** raw record and a re-derivation, never a mutation of the existing one. The purpose is that a stranger can reconstruct any published figure from the raw layer and the committed rules alone.
