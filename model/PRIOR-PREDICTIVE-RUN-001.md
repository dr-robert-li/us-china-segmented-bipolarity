# Prior predictive checks -- runs 001 to 003

Required by `SPECIFICATION.md` section 10, which commits that the prior predictive gates are run before estimation and that failures are reported rather than resolved by adjusting priors until they pass.

**Outcome: two of five gates fail at the committed priors. Estimation is blocked.** No parameter has been changed to make a gate pass. Two implementation defects and one prior-transcription defect were fixed, each on grounds stated below and each independent of its effect on gate outcomes.

| Gate | Run 001 | Run 002 | Run 003 |
|---|---|---|---|
| PP1 regime coverage | FAIL, R3 and R5 | FAIL, R3 and R5 | **FAIL, R5 only** |
| PP2 R4 refutability | FAIL | PASS | PASS |
| PP3 trajectory sanity | PASS | PASS | **FAIL** |
| PP4 swap symmetry | PASS, approximate | PASS, exact | PASS, exact |
| PP5 declinism | PASS | PASS | PASS |

Run 003 is the canonical result: it is the first run whose sampler matches `PRIORS.md` as committed. Runs 001 and 002 used uniform surrogates for three priors and their results are recorded because the reasoning built on them was in one place wrong, and that matters more than the numbers.

Raw run-003 output: `model/prior-predictive-run-003.txt`. Reproduce with `python -c "from usbip.model import prior_predictive as pp; print(pp.run_all(n_draws=400))"` from `pipeline/src`.

---

## 1. Run 001

n=200, seed 20260819.

- **PP1 FAIL.** R3 challenger peaking at 0.010 prior mass, R5 dual systemic constraint at 0.000. Both below the 0.05 floor.
- **PP2 FAIL.** R4 never fell below 0.2 mass under any of the three hostile baselines: 0.465 at parity, 0.455 PRC-dominant, 0.460 US-dominant. A regime that cannot be pushed below 20% by an adversarially chosen baseline is not being predicted by the model, it is being produced by the classifier.
- PP3, PP4, PP5 pass.

PP2's failure is the more serious of the two, because R4 segmented bipolarity is the thesis. A gate designed to check whether the central claim is refutable returned that it was not.

### 1.1 Defect A -- the ceiling prior was not the one committed

`PRIORS.md` section 4 commits `xbar[j] ~ LogNormal(log(ENGINEERING_CEILING_MULTIPLE[j] * baseline), 0.6)`. The implementation drew `uniform(3, 30) * baseline` for every input.

Fixed to the committed form, with the declared multiple table registered in `SPECIFICATION.md` by amendment: D1 4.0, D2 4.0, D3 5.0, F1 8.0, F2 6.0, F3 3.0.

**Independent justification:** the implementation contradicted a written commitment. It would have been fixed on discovery regardless of gate consequences, and the fix was made before its effect on any gate was measured. A uniform draw to 30x also assigns equal density to a 3x and a 29x ceiling for the same input, which is not a defensible statement about engineering limits.

### 1.2 Defect B -- the classifier made R4 a sink

The regime classifier had a catch-all: any trajectory that was neither cleanly divergent nor cleanly peaking fell to R4. Mixed-with-flat cases therefore accumulated in R4 whatever they contained.

Fixed by two changes to R009: partial one-directional movement now classifies as concentration, R1 or R2, and total flatness gets its own bucket `R0_no_material_change`, exempt from the PP1 coverage floor.

**Independent justification:** a catch-all bucket is a specification defect on its own terms. `SPECIFICATION.md` names five regimes as an exhaustive and mutually exclusive partition of a substantive output space; a residual bucket collecting everything unclassified is not one of the five, and labelling it R4 asserted the thesis by default. The `R0` bucket is also honest about something the five-regime partition omitted: a world where nothing moves much is a possible world, and it is not segmented bipolarity.

This fix is the one most vulnerable to the charge of gate-driven tuning, since it directly caused PP2 to pass. Three things are on the record against that charge. The defect is describable without reference to any gate. The fix moves mass *away* from the thesis regime, which is the direction adverse to the project. And R0 was given an explicit exemption from PP1 rather than being counted toward coverage, which is the conservative choice.

---

## 2. Run 002

n=250, seed 20260819. Both fixes applied.

- **PP2 PASS.** R4 reaches 0.068 under the most hostile baseline. Refutable.
- **PP4 initially FAIL at 0.072**, then exact after refactor. The gate compares a world against its state-swapped mirror. The original implementation ran the two worlds through independent random streams, so the comparison measured Monte Carlo noise alongside genuine asymmetry. Refactored to pre-draw shock streams held separately from the sampler, so the mirror consumes the identical numbers with states exchanged. Result: exact mirror on all paired draws, largest aggregate deviation 0.0000. This is a strictly stronger test than the one that failed, and it was strengthened rather than loosened.
- **PP1 still FAIL.** 2050 masses: R1 0.452, R2 0.376, R3 0.004, R4 0.108, R5 0.000, R0 0.060.

### 2.1 The run-002 diagnosis was wrong, and the error is instructive

The diagnosis recorded at run 002 was that the saturation mechanism was too weak to generate reversal: `kappa` capped the attainable drag at about 0.06 while unconstrained growth `|gstar|` reached 0.077, giving `P(kappa > gstar)` of roughly 0.694, so Block E's saturation term could not turn a trajectory over.

The arithmetic was right and the attribution was wrong. `kappa` was capped at 0.06 because the implementation drew `uniform(0, 0.06)`, and `PRIORS.md` commits `kappa ~ HalfNormal(0.05)`, which has no upper bound. The cap was an implementation artefact, not a property of the committed prior. The same audit found `phi` drawn as `uniform(1, 4)` against a committed `Gamma(2, 1)`, `rho_g` drawn as `uniform(0.5, 0.95)` against a committed `Beta(6, 2)`, and the innovation scale hard-coded at 0.004 and 0.010 against a committed `sigma_u ~ HalfNormal(0.05)` shared by both shock streams.

**Independent justification for the fix:** four transcription errors against a written commitment. Recorded here as defect C.

The reason this matters beyond bookkeeping: the run-002 diagnosis was a plausible, well-formed, quantitative story about a structural limitation of the model, and it was an artefact of a typo in a sampler. Had estimation proceeded on that basis, the natural next step would have been to argue that `kappa` should be widened -- adjusting a committed prior to fix a problem that did not exist, and doing so in the direction that made a failing gate pass. The prior predictive did not catch this. An audit of the sampler against `PRIORS.md` caught it. That is a gap in the gate design and it is recorded as such.

---

## 3. Run 003 -- the canonical result

n=400, seed 20260819, sampler matching `PRIORS.md` with no surrogates.

Regime mass by horizon:

| Horizon | R1 | R2 | R3 | R4 | R5 | R0 |
|---|---:|---:|---:|---:|---:|---:|
| 2030 | 0.343 | 0.245 | 0.005 | 0.022 | 0.000 | 0.385 |
| 2040 | 0.440 | 0.290 | 0.138 | 0.072 | 0.003 | 0.058 |
| 2050 | 0.395 | 0.223 | 0.230 | 0.098 | 0.025 | 0.030 |
| 2075 | 0.290 | 0.172 | 0.275 | 0.052 | 0.207 | 0.003 |

Correcting the priors moved R3 from 0.004 to 0.230 at 2050, which confirms the defect-C attribution: reversal was unreachable because the sampler had truncated the saturation prior, not because the mechanism was too weak.

### 3.1 PP1 fails on R5

R5 dual systemic constraint carries 0.025 mass at 2050, below the 0.05 floor. It is not unreachable -- it carries 0.207 at 2075.

**Diagnosis.** R5 requires both states simultaneously constrained, which under `ENGINEERING_CEILING_MULTIPLE` and the committed growth priors does not typically occur until the 2060s. The gate evaluates at 2050. So the failure is a statement about the interaction of the ceiling table with the gate's evaluation horizon, and it admits at least three different readings.

**Candidate remedies, none chosen:**

1. Make PP1 horizon-conditional, requiring 0.05 coverage of R5 at 2075 rather than 2050. Defensible on the grounds that dual saturation is intrinsically a long-horizon regime and the gate as written asks for something the theory does not claim. Also the remedy most obviously fitted to the observed failure.
2. Lower the `ENGINEERING_CEILING_MULTIPLE` values, bringing ceilings within reach by 2050. Changes a table registered by amendment and would move F1's and F2's ceilings, which bear on falsifier-adjacent quantities.
3. Accept that R5 is not usefully identified at the project's stated 2050 horizon and say so in the output contract, restricting reported regimes to four at 2050. Costly, and the honest reading if R5 turns out to be a regime the design cannot speak to.

**The choice is deferred to a dated amendment and will be made on grounds independent of which option makes the gate pass.** Recording three options and picking none is the point: the option that passes the gate most cheaply is option 1, and it is named as such.

### 3.2 PP3 fails, and this is the more serious failure

The 2050 input multiple reaches 892.7x at n=400, against a pre-registered ceiling of 20x. 5.8% of draws breach it. The distribution:

| Percentile of state-input pairs | 2050 multiple |
|---|---:|
| p50 | 1.32x |
| p75 | 2.28x |
| p90 | 4.12x |
| p95 | 6.73x |
| p99 | 17.49x |
| max | 1,598.32x |

7.5% of draws contain at least one breaching pair; the median per-draw maximum is 4.59x. So the central mass is unobjectionable and the tail is absurd -- a Chinese transmission fleet 1,598 times its 2026 level by 2050.

**Diagnosis, and it is unambiguous.** The runaway is produced by the interaction of two committed priors. `sigma_u ~ HalfNormal(0.05)` is applied to the growth innovation as well as the level innovation, and `rho_g ~ Beta(6, 2)` centres persistence near 0.75 with mass above 0.9. A growth innovation of scale 0.06 persisting at 0.91 compounds over 24 years. The worst draw had `sigma_u = 0.063` and `rho_g = 0.906`.

Pinning `sigma_u` at 0.01 and changing nothing else removes every breach: maximum 16.64x, zero draws above the ceiling.

That counterfactual is a diagnostic, **not** a proposed fix. Pinning a prior at the value that makes a gate pass is the exact move the pre-registration exists to prevent, and the fact that it works cleanly makes it more tempting rather than less.

**Candidate remedies, none chosen:**

1. Separate the innovation scales, so that `sigma_v` on the growth innovation is drawn tighter than `sigma_u` on the level innovation. Arguably what `PRIORS.md` should have said in the first place, since a shock to a growth rate and a shock to a level are not the same kind of quantity and there is no reason their scales should share a prior. This is a real argument that exists independently of the gate, which is also what makes it the most dangerous option -- a good independent argument for the change that passes the gate is hard to distinguish from motivated reasoning.
2. Truncate the joint prior, rejecting draws whose implied 2050 multiple exceeds the ceiling. Transparent, and it makes the 20x figure a hard constraint on the prior rather than a check on it. Changes what the prior is.
3. Accept the tail and widen the PP3 ceiling. Rejected in advance: 20x was pre-registered and the tail reaches 1,598x, so no defensible ceiling accommodates it.

Option 3 is named and rejected here rather than silently omitted, because it is the option that would make the problem disappear with a single number.

### 3.3 What the two failures have in common

Both localise to `PRIORS.md` section 4 rather than to the structural blocks. Nothing in Blocks E, P or the R009 classifier is implicated. That is mildly reassuring about the model's architecture and it is not evidence for the thesis: PP2, the gate that tests whether the thesis is refutable, passes at 0.048 mass under the most hostile baseline, which is a narrow margin above nothing.

PP5 passes: no divergence regime exceeds 0.5 prior mass, R1 at 0.395 and R2 at 0.223. The prior does not encode declinism. It does tilt toward PRC-favourable divergence by roughly 17 points, which is a property of `SYNTHETIC_BASELINE` -- a labelled non-datum that exists only so PP4 has something asymmetric to swap -- and not an inference.

---

## 4. Consequence

**Estimation is blocked** until the PP1 and PP3 remedies are chosen by dated amendment. The failing configuration is committed as-is so that the amendment can be read against it.

The alternative sequence -- fix the priors first, then commit only the passing run -- would have produced a cleaner repository and destroyed the evidence that the gates ever bound. Two prior-predictive gates rejecting a committed prior before any data was touched is the system working. A repository in which all five gates passed on the first recorded run would be less credible, not more.

One weakness in the gate design was found and closed. One remains open.

**Closed.** No gate audited the sampler against `PRIORS.md`. Defect C survived two full runs and produced a plausible false diagnosis precisely because every gate consumes the sampler's output and therefore inherits its errors. `pipeline/tests/test_registry_and_priors.py` now checks the empirical moments of each committed prior against its analytic moments, with each case naming the surrogate it guards against -- the `kappa` cap at 0.06, `phi` as uniform(1, 4), `rho_g` as uniform(0.5, 0.95), the hard-coded innovation scale, and `xbar` as uniform(3, 30). A moment check would not catch every possible substitution, since two families can share a mean and a variance, but it catches the substitution that actually happened, because a uniform surrogate chosen to span a plausible range does not reproduce the committed family's moments.

**Open.** PP1 evaluates at a single horizon and the specification does not state why 2050 rather than 2075. That silence is what makes remedy 1 in section 3.1 available so cheaply, and it is not fixed here, because fixing it now would mean choosing the horizon while looking at which choice passes.

---

## Sources

Internal specification and priors:

- `model/SPECIFICATION.md` -- output contract, five-regime partition, section 10 gate commitment
- `model/PRIORS.md` -- section 4, the committed prior forms
- `model/IDENTIFICATION.md` -- PP1 to PP5 definitions
- `pipeline/rules/R009-regime-classification.md` -- classifier, constants, frozen priority order
- `model/prior-predictive-run-003.txt` -- raw run output

---

## Amendment 1 -- 2026-08-20 -- both remedies selected; grounds recorded before results

**Appended, not substituted.** The deferral in section 4 is closed. Both selections were made by author decision of 2026-08-20 in structured Q&A, on the grounds below, each statable without reference to which option makes a gate pass. Gate effects are stated openly alongside, per this file's own practice of naming the cheapest-passing option as such.

### PP1: candidate 3, restrict the output contract

R5 is not reported at 2050; it is reported at 2075 only, where run 003 gives it 0.207 prior mass. Ground: the design cannot populate dual systemic constraint by 2050 under the committed ceilings, so a 2050 posterior for R5 would be a number the prior structure cannot inform; the contract should claim only what the design can speak to. Candidate 1 was declined as procedurally contaminated by this file's own open note (choosing the gate horizon while looking); candidate 2 was declined because it moves falsifier-adjacent ceilings with no independent ground on record. PP1 is restated to check each regime at its earliest claimed horizon: `SPECIFICATION.md` Amendment 02, `IDENTIFICATION.md` Amendment 1.

### PP3: candidate 1, separate innovation scales with the derivation pre-named

`sigma_v` on the growth innovation gets its own prior, `HalfNormal(s_v)`, with `s_v` produced by a procedure committed in `PRIORS.md` Amendment 1 **before** being computed: AR(1) residual scale, pooled across both states, from the snapshotted Ember capacity series. The value is whatever the procedure yields, and PP3's re-run is reported pass or fail. Candidate 2 was declined because rejection-sampling at the ceiling makes PP3 unfailable by construction. The section 3.2 warning stands: the dimensional argument for separate scales is also the argument that passes the gate, which is why the scale is procedure-derived rather than judgement-chosen, and why the commit order (procedure, then value) is verifiable in history.

### Run 004 follows

Run 004 executes the amended gates with the derived `sigma_v`. Its results are appended below this amendment once computed, whatever they are. The section 4 estimation block remains in force until run 004 is on file and every gate passes.

### Sources for Amendment 1

- model/PRIORS.md, Amendment 1 (internal; the pre-named procedure)
- model/SPECIFICATION.md, Amendment 02; model/IDENTIFICATION.md, Amendment 1 (internal)
