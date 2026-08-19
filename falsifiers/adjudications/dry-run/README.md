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

## Outcome of the F5 exercise

Sub-clauses A and C discriminate between the two episodes. **Sub-clause B does not**: it returns `not_met` on both, triggering failure conditions 1 and 3.

The identified mechanism is the removal-anchoring rule, which counts from the first official public announcement of expulsion. In 1976 that announcement fell outside the window containing the operation. The rule is therefore **anti-correlated with the property Sub-clause B measures**: the more irregular the removal, the later or more absent the official announcement, and the less likely the rubric registers it.

The rule has not been changed, because the better rule would move the live 2026 determination toward triggering. The defect is recorded against the clause instead, and a candidate replacement is registered for 2027 onward. Full reasoning in [`1976.md`](1976.md).

## Outcome of the F1 exercise -- added 2026-08-20

The F1 rubric **discriminates**: `triggered` on the 2003 gas-boom window, `not_triggered` on the 2022--2024 control, robust across both pre-committed ratio constructions and a substitution of the numerator source. None of the three failure conditions occurred.

The exercise surfaced a defect anyway, in the opposite direction from F5-B's: the adapter's 5 percent source-tolerance rule, written without a committed comparison basis, is breached by the definitional gap between installed and net-summer capacity in **both** episode windows and in the current live years -- so as written it blocks automatic verdict emission rather than permitting it. A false-alarm mode, conservative in effect, registered as `tolerance_basis_unspecified` in `pipeline/adapters/F1.md`, Amendment 1, with resolution required before first ingest while the condition sits ~30 points from threshold.

One condition of eight has now failed its dry run (F5-B), one has passed (F1), and six remain untested, not passed.

## Reading order

Each file places the **adverse case before the reasoning**, as `../adjudication.md` requires of determinations. In a dry run the adverse case is written against the exercise's own usefulness as well as against its verdicts, because the strongest objection to a dry run is that selecting the most extreme episode in the record guarantees the answer.
