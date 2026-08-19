# Dry runs -- rubric exercises against closed historical episodes

**Nothing in this directory is a finding about the present.** These files apply the project's adapters and adjudication framework to historical episodes whose outcomes are independently known, for the single purpose of testing whether a rubric discriminates. They are not determinations, they do not appear in the annual index, and they do not bind any live verdict.

## Why they exist

A rubric exercised only on the live case it was written for has not been tested. It has been applied. The distinction matters because the failure mode a pre-registered threshold is most exposed to is not a threshold set at the wrong level -- that is visible and arguable -- but a **counting rule that systematically fails to see the thing the clause describes**. That failure is invisible from inside the live case, because there is no known answer to compare against.

A dry run supplies the known answer.

## The design rule

Every dry run must pair an **expected-positive** episode with a **negative control**, and must state its failure conditions before computing anything. A rubric that fires on the positive case alone has demonstrated sensitivity, not discrimination. The failure conditions are:

1. The rubric returns the negative verdict on the expected-positive episode.
2. The rubric returns the positive verdict on the negative control.
3. The rubric returns the **same** verdict on both. This is the most serious, because a rubric that cannot separate the two is not measuring anything.

## What may and may not follow from a dry run

**May follow:** recording a demonstrated false-negative or false-positive mode against the clause; discounting the weight of future verdicts on that clause; registering a candidate replacement rule to take effect **prospectively**, in a later evaluation year.

**May not follow:** changing a rule that applies to a window whose outcome is already visible. A rubric that is revised whenever a dry run embarrasses it has no rules, and the revision will always seem substantively defensible to the person making it -- which is precisely why the prohibition cannot be discretionary. See `../../PRE-REGISTRATION.md`.

The pre-registration's prohibition on moving a threshold as it is approached applies with equal force to a counting rule, and in **both** directions. A change that makes a live clause easier to satisfy is not more acceptable than one that makes it harder simply because the project's thesis is the one predicting a trigger.

## Contents

| File | Falsifier | Episode | Role | Result |
|---|---|---|---|---|
| [`1976.md`](1976.md) | F5 | Succession after the death of Mao Zedong | Expected-positive | A `met`, B `not_met` (**rubric failure**), C `met` |
| [`2012.md`](2012.md) | F5 | Hu Jintao to Xi Jinping transition | Negative control | All three `not_met` (correct negative) |
| [`F1-2003-2024.md`](F1-2003-2024.md) | F1 | US gas-boom build, window 2001--2003 | Expected-positive | `triggered` at R = 2.35 (correct positive) |
| [`F1-2003-2024.md`](F1-2003-2024.md) | F1 | PRC record expansion, window 2022--2024 | Negative control | `not_triggered` at R = 0.094 (correct negative) |
| [`F6-2001-2010.md`](F6-2001-2010.md) | F6 | Dot-com graduate-market peak, 1999--2003 | Favourable episode | Zero qualifying years; **discrimination untestable** -- no known positive exists |
| [`F6-2001-2010.md`](F6-2001-2010.md) | F6 | Post-crisis trough, 2009--2013 | Adverse episode | Zero qualifying years (correct negative) |
| [`F4-2014-2018.md`](F4-2014-2018.md) | F4 | Baseline study window, 2014--2018 | Sole constructible (expected-negative) | **Discrimination untestable**; verdict machinery unevaluable from any publication |
| [`F3-1997-japan.md`](F3-1997-japan.md) | F3 (Clause 2) | Korea 1997 chaebol-banking collapse | Expected-positive | Analogue `met`, all six criteria engaged (correct positive) |
| [`F3-1997-japan.md`](F3-1997-japan.md) | F3 (Clause 2) | Japan 1990s managed absorption | Negative control | Analogue `not_met` (correct negative, incl. contained Nov-1997 mini-cascade) |
| [`F2-1962-2025.md`](F2-1962-2025.md) | F2 (Clause 1) | Full outturn record 1962--2025 | Characterisation (flag-only) | Qualifying state obtains in 63 of 64 years; **anchoring gap is verdict-determining**; shadow `triggered` published |
| [`F8-2021-2025.md`](F8-2021-2025.md) | F8 | PRC public-HPC leadership era, 2021 | Expected-negative | Ratio 109.6%, condition not satisfied (correct negative) |
| [`F8-2021-2025.md`](F8-2021-2025.md) | F8 | Post-export-control buildout, 2025 | Expected-positive | Ratio 17.3%, condition satisfied (correct positive); construction spread exceeds live margin |

## Outcome of the F5 exercise

Sub-clauses A and C discriminate between the two episodes. **Sub-clause B does not**: it returns `not_met` on both, triggering failure conditions 1 and 3.

The identified mechanism is the removal-anchoring rule, which counts from the first official public announcement of expulsion. In 1976 that announcement fell outside the window containing the operation. The rule is therefore **anti-correlated with the property Sub-clause B measures**: the more irregular the removal, the later or more absent the official announcement, and the less likely the rubric registers it.

The rule has not been changed, because the better rule would move the live 2026 determination toward triggering. The defect is recorded against the clause instead, and a candidate replacement is registered for 2027 onward. Full reasoning in [`1976.md`](1976.md).

## Outcome of the F1 exercise -- added 2026-08-20

The F1 rubric **discriminates**: `triggered` on the 2003 gas-boom window, `not_triggered` on the 2022--2024 control, robust across both pre-committed ratio constructions and a substitution of the numerator source. None of the three failure conditions occurred.

The exercise surfaced a defect anyway, in the opposite direction from F5-B's: the adapter's 5 percent source-tolerance rule, written without a committed comparison basis, is breached by the definitional gap between installed and net-summer capacity in **both** episode windows and in the current live years -- so as written it blocks automatic verdict emission rather than permitting it. A false-alarm mode, conservative in effect, registered as `tolerance_basis_unspecified` in `pipeline/adapters/F1.md`, Amendment 1, with resolution required before first ingest while the condition sits ~30 points from threshold.

One condition of eight has now failed its dry run (F5-B), one has passed (F1), and six remain untested, not passed.

## Outcome of the F6 exercise -- added 2026-08-20

**A third outcome category: `discrimination_untestable`.** The committed series has never produced a qualifying year in its 1990--2026 span -- the 30 percent threshold sits 7.8 points below the lowest annual mean ever recorded -- and no source establishes that the condition (a reversal of elite overproduction) occurred within the span. There is no known positive to test against; unlike F5-B, no event was missed. The measurand itself validates on ordering (it ranks the known best and worst graduate markets correctly), and the counting machinery ran without defect.

The substantive product is a calibration finding registered as `threshold_outside_observed_range` in `pipeline/adapters/F6.md`, Amendment 1: F6 is close to unfalsifiable in practice on the observed behaviour of its own series, and the papers must carry that alongside the F5-B and F7 caveats.

Score: one failed (F5-B), one passed (F1), one untestable (F6), five untested.

## Outcome of the F4 exercise -- added 2026-08-20

**`discrimination_untestable`, second instance -- and a defect beneath it.** F4's committed measurand exists only inside the baseline study's 2014--2018 window; no positive episode is documented anywhere on it. Sharper: the six-of-ten majority rule counts per-country exposure-conditional p90/p10 cells that **no publication provides, including the baseline itself** -- registered as `verdict_input_shape_unpublished`. The committed sample rule was found decision-fragile at the deciding rank (0.6 percent between ranks 9 and 10) and was completed -- source, age band, vintage, tie rule -- while provably inert. First successor-monitoring check recorded: Jaccoud (2025) located, headline running toward the trigger, **not substituted** (methodology break, no US, no per-country cells) -- the favourable-source-substitution prohibition's first live application to F4.

Score: one failed (F5-B), one passed (F1), two untestable (F6, F4), four untested.

## Outcome of the F3 exercise -- added 2026-08-20

**The Clause 2 unmanaged-cascade rubric discriminates on the analogue pair** -- the pair pre-registered before any evidence was gathered, making this the set's first blind-registered exercise. Korea 1997 engages all six criteria (`met` analogue); Japan 1990s returns `not_met` despite containing a genuine contained mini-cascade, failing decisively on intervention, disorder, and persistence. Validation is generic only: nothing LGFV-specific is tested, Clause 1 was not exercised. One watch item registered: the public-bond seniority criterion was the weakest discriminator on the archetype (Korea's cascade ran through bank credit and court bankruptcies), an F5-B-pattern risk recorded before it can matter.

Score: one failed (F5-B), two passed (F1, F3-C2 generic), two untestable (F6, F4), two remaining (F2, F8 -- flag-only).

## Outcome of the F2 exercise -- added 2026-08-20

**The mirror image of F6, with a live edge.** Clause 1's qualifying state has obtained in 63 of 64 outturn years since 1962 (1999 sits exactly at the non-exceeding boundary); the threshold lies at the bottom of the observed range, so the clause measures whether the projected decline has arrived, not whether capacity recovered. Sharper: the adapter never specified **which** outturn an evaluation year tests, and the choice is currently verdict-determining -- the latest-elapsed-outturn reading gives FY2025 = 6.2 percent (cross-check basis), Clause 1 `met`, and with Clause 2 already adjudicated `met`, **F2 `triggered`**. The F5-B defect class, running in the opposite direction: the unstated choice currently protects the thesis. Candidate rule `F2-ANCHOR-2` registered not-in-force (earliest 2027); shadow verdict published in the 2026 log under the standing rule -- the only clause in the set where binding and shadow verdicts disagree outright.

Score: one failed (F5-B), two passed (F1, F3-C2 generic), two untestable (F6, F4), one characterised with a live anchoring gap (F2), one remaining (F8 -- flag-only).

## Outcome of the F8 exercise -- added 2026-08-20

**The share arithmetic discriminates**, and F8 is the only condition in the set whose measurand demonstrably visits both sides of its threshold in the observed record: PRC/US 109.6 percent in 2021 (correct negative), 17.3 percent in 2025 (correct positive) on the public Epoch tracked-cluster construction. The flag is quantitative: the spread between admissible constructions (~1.6 points) exceeds the live distance to threshold (~1.1 points), so any near-threshold verdict is construction-determined until the adapter's open method items are closed -- registered as `construction_spread_exceeds_margin`, direction-neutral.

**Final score, all eight conditions examined:** F5-B failed; F1, F3-C2 (generic), and F8 passed; F6 and F4 untestable; F2 characterised with a verdict-determining anchoring gap and a disagreeing shadow verdict; F7 excluded (no series exists -- weakened-falsifier status accepted by amendment). The programme's Priority 1 is complete: every clause has now been either discrimination-tested, shown untestable with the reason registered, or excluded with the reason published.

## Reading order

Each file places the **adverse case before the reasoning**, as `../adjudication.md` requires of determinations. In a dry run the adverse case is written against the exercise's own usefulness as well as against its verdicts, because the strongest objection to a dry run is that selecting the most extreme episode in the record guarantees the answer.

## Registered exercises, not yet run -- added 2026-08-20

Registered here before computation, per the design rule above and `../../PRE-REGISTRATION.md` Amendment 2. Episode pairs and failure conditions are fixed at registration; the failure conditions are the three standard ones above unless a narrower one is added at the head of the exercise file.

| Falsifier | Expected-positive | Negative control | Registered | Status |
|---|---|---|---|---|
| F6 | Dot-com peak 1999--2003 | Post-crisis trough 2009--2013 | 2026-08-20 | **run** -- see `F6-2001-2010.md`; discrimination untestable |
| F4 | Baseline study window 2014--2018 (sole constructible) | -- | 2026-08-20 | **run** -- see `F4-2014-2018.md`; discrimination untestable |
| F3 | Republic of Korea, 1997 chaebol-banking collapse | Japan, 1990s managed debt-overhang absorption | 2026-08-20 | **run** -- see `F3-1997-japan.md`; discriminates |

**The F3 pair is fixed now** because it was selected by author decision of 2026-08-20 in structured Q&A, on the criterion of known-answer clarity first, structural analogy second. Its limitation is registered with it: no closed PRC positive episode exists, so the exercise tests the *unmanaged-cascade rubric* generically and cannot test the PRC-specific LGFV counting rules. It is a partial discrimination test and will be labelled one. The Argentina-2001/Brazil-1997 pair (closer structural analogy, blurrier known answer) was considered and declined; the 2021--2024 PRC property episode was excluded because its outcome is contested, which disqualifies it as a known answer.

F6 and F4 are queued with pairs deliberately unfixed: fixing an episode pair requires the series reconnaissance that is the first step of each exercise, and naming a pair here without it would be registration theatre. Each exercise file must fix its pair and failure conditions at its head before computing, and the sequence F6, F4, F3, then flag-only F2 and F8, is the committed order.
