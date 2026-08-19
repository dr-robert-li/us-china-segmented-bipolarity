# Pre-registered falsification conditions

A thesis that cannot specify what would prove it wrong is not defensible regardless of its internal coherence.

The eight conditions below are pre-registered. Their presence in this repository's commit history, prior to the existence of any estimation code, is the pre-registration record. Thresholds may be revised only by commit, with the reason stated in the commit message; the diff is the audit trail.

Status is logged annually in `falsifiers/log/` against the named sources.

---

## The eight conditions

| ID | Condition | Threshold | By | Source |
|---|---|---|---|---|
| **F1** | US generation-capacity additions converge on China's | US annual additions reach 40% of PRC annual additions, 3-year rolling average | 2035 | EIA; NEA / Ember |
| **F2** | US federal discretionary fiscal capacity recovers | Non-interest discretionary outlays exceed 6.0% of GDP without a debt crisis | 2036 | CBO Long-Term Budget Outlook |
| **F3** | PRC debt forces disorderly adjustment | IMF augmented debt exceeds 180% of GDP **with** an unmanaged LGFV default cascade | 2035 | IMF Article IV |
| **F4** | AI raises rather than lowers within-occupation wage dispersion | p90/p10 ratio rises in high-AI-exposure occupations across 10 countries | 2032 | OECD, successor to Georgieff 2024 |
| **F5** | PRC succession fails destructively | Extra-constitutional leadership transfer, a purge exceeding 15% of the Politburo, or military intervention in succession | 2040 | Contemporaneous scholarly consensus |
| **F6** | US elite overproduction reverses | Graduate underemployment falls below 30% for 5 consecutive years | 2035 | NY Fed; BLS |
| **F7** | PRC robotics fails to offset labour contraction | Manufacturing TFP growth turns negative for 5 consecutive years despite continued IFR-recorded robot-density growth | 2040 | IFR World Robotics; Conference Board TED |
| **F8** | Frontier compute gap persists decisively | PRC aggregate frontier-capable compute remains below 20% of the US total | 2032 | Epoch AI; CSET |

---

## Classification by evidence type

The eight conditions are not homogeneous, and coding them as if they were would overstate the automation achievable. Each is classified before any adapter is written.

### Type A -- Direct quantitative

Single measurable series against a numeric threshold. Fully automatable. Ingestion adapters are **audience-invariant** and structurally identical.

- **F1** -- capacity additions, physically measurable
- **F8** -- frontier-capable compute, independently estimated

### Type B -- Compound

A quantitative threshold conjoined with a qualitative event. The numeric clause automates; the event clause requires adjudication. Both clauses must be satisfied; neither alone triggers.

- **F3** -- augmented debt exceeding 180% of GDP **and** an unmanaged LGFV default cascade
- **F7** -- sustained negative manufacturing TFP **and** continued robot-density growth

### Type C -- Expert-adjudicated

No automatable series exists. Resolution depends on documented scholarly assessment. Requires a written adjudication with named sources and a dissent record.

- **F5** -- destructive succession failure

### Type D -- Methodology-sensitive

The threshold is defined on a series whose construction is itself contested or subject to revision. Coding rules must be fixed in advance and the sensitivity of the verdict to those rules reported alongside the verdict.

- **F2** -- depends on the definitional boundary of non-interest discretionary outlays and on what counts as "without a debt crisis"
- **F4** -- depends on the occupational AI-exposure measure, the country sample, and the choice of dispersion statistic
- **F6** -- depends on the underemployment definition and the graduate cohort boundary

Type D adapters are **blocked** until their coding rules are written and committed. Building them first would embed arguable choices as though they were data.

---

## Trigger rules

### Single threshold crossing

A single falsifier crossing its threshold triggers **mandatory revision of its associated pillar**. This rule is retained unchanged.

### Multiple crossings -- dependence-aware review

The original formulation held that any two falsifiers trigger rejection of the core thesis. **That rule is amended**, for a stated statistical reason rather than convenience.

The conditions are not independent evidence. F3 and F7 are plausibly correlated: a disorderly fiscal adjustment and a failure of automation to offset labour contraction share common macroeconomic causes. Two correlated triggers do not constitute two independent refutations, and treating them as such would overstate the evidential weight of the joint event.

The amended rule:

1. Any two threshold crossings trigger **mandatory formal review**, not automatic rejection.
2. Rejection depends on **posterior evidence** evaluated under an explicit dependence structure over the eight conditions.
3. The assumed dependence structure is committed in advance, in `falsifiers/dependence.md`, before any crossing occurs.
4. A review that declines to reject must state, in writing, which parameter regions survive and why.

This amendment makes rejection harder to reach by accident and harder to avoid by argument. It is not a weakening of the falsification commitment; a review that concludes the thesis survives is itself a public, auditable document.

### What may not be done

- A threshold may not be moved in response to its own approach.
- A source may not be substituted for a more favourable one without a committed methodological justification.
- A deadline may not be extended.
- A condition may not be reclassified from Type A to Type C to avoid an unwelcome automated verdict.

---

## Annual logging

One file per condition per year in `falsifiers/log/<year>/F<n>.md`, each recording:

- observed value and the vintage of the series used
- distance to threshold
- verdict: not triggered / triggered / indeterminate
- for Types B, C and D: the adjudication, its author, and any dissent
- data revisions affecting prior-year verdicts, and whether those verdicts change

Retrospective revision of a prior-year verdict is permitted and expected, since sources revise. It must be recorded as an amendment, never as an overwrite.

---

## Amendment 1 -- 2026-08-20 -- shadow publication of registered candidate rules

**Appended, not substituted. This amendment changes what is published, not what is determined.** No binding rule, threshold, window, or anchoring moves. The prohibition on changing a rule as its threshold is approached binds the **determination**; it says nothing against publishing, alongside the binding value, what a registered-but-not-in-force candidate rule would have computed. Concealing that second number is what would make a registered defect flag cosmetic.

### The rule, committed

Any clause carrying a candidate replacement rule with status `registered_not_in_force` publishes, in each annual log entry from registration until the candidate is adopted or its registration is closed:

1. The **binding value**, computed under the rule in force, labelled as binding. This value alone feeds the verdict, and it carries every flag the adapter attaches to it.
2. The **shadow value**, computed under the registered candidate, labelled `shadow -- not_in_force -- feeds nothing`.

The shadow value binds nothing, feeds no gate, and appears in no verdict arithmetic. Where computing it requires a judgement the candidate rule itself defines (for example, establishing effective loss of office from reporting), the judgement already recorded in the candidate's registration is applied as registered; shadow publication is not an occasion to re-adjudicate.

### Why this is safe to commit now

The one live instance is F5 Sub-clause B, where the binding rule gives 2 counted removals and the candidate `F5-B-ANCHOR-2` gives 3, both below the threshold of 4. Both values return `not_met`; the shadow changes no verdict. The rule is committed while that is true.

### Sources for Amendment 1

- pipeline/adapters/F5.md, Amendment 3 (internal; the registered candidate and its recorded numerator effect)
- falsifiers/adjudications/dry-run/1976.md (internal; the false-negative mode that motivates publication)

---

## Amendment 2 -- 2026-08-20 -- discrimination testing required prospectively

**Appended, not substituted. Prospective only.** This amendment binds evaluation years 2027 onward and any falsifier registered after this date. It does not apply retrospectively to the 2026 determinations: they were authored under the rules then in force, and retro-applying a new admissibility bar would invalidate determinations the framework has already published, which is not the intent and is recorded as not the intent.

### The rule, committed

From evaluation year 2027, no clause is reported as a determination unless **paired dry runs are on file** for it, following `falsifiers/adjudications/dry-run/README.md`:

- one **expected-positive** historical episode and one **negative control**, both with independently known outcomes;
- failure conditions named **before** computing anything;
- results published regardless of outcome, including rubric failures.

A newly registered falsifier's adapter must have its dry runs on file before its first determination. A clause whose dry run demonstrates a failure mode is not thereby retired: the failure is registered as a flag, per the dry-run directory's rules, and the clause continues to be reported carrying it.

### Why

F5 Sub-clause B was pre-registered and then exercised for the first time against the live case it was written for. Its first paired dry run -- run only after the live determination -- demonstrated a false-negative mode on the archetypal positive episode. A rubric exercised only on its live case has been applied, not tested, and the failure mode a pre-registered threshold is most exposed to is a counting rule that cannot see the thing the clause describes. That failure is invisible from inside the live case.

### Sources for Amendment 2

- falsifiers/adjudications/dry-run/README.md (internal; the paired design and failure conditions)
- falsifiers/adjudications/dry-run/1976.md (internal; the demonstrated failure)
- pipeline/adapters/F5.md, Amendment 3 (internal; the registered flag)
