# R009 -- Regime classification

```yaml
rule:
  rule_id: R009
  version: 0.1.0
  name: Trajectory to regime label
  applies_to: [model_output]
  inputs: [Y_trajectory, unconstrained_Y_trajectory, horizon]
  output: regime_label
  parameters:
    DEADBAND: 0.10
    REVERSAL_DEPTH: 0.15
    CONSTRAINT_RATIO: 0.60
    priority_order: [R5, R3, R4, R1_R2, R0]
  determinism: true
  supersedes: null
```

Registered by amendment to `SPECIFICATION.md`. Implementation: `pipeline/src/usbip/model/prior_predictive.py`, function `classify`.

Version **0.1.0**. The classifier runs and is frozen for the purposes of the prior-predictive record, and it is below 1.0 because two of its three constants were chosen by judgement without a sensitivity run, and because the R5 branch is implicated in a failing gate.

---

## 1. What the rule does

Maps one simulated trajectory to exactly one label. Six labels: the five regimes named in `SPECIFICATION.md` plus `R0_no_material_change`.

Position is measured in logs, by element, as change from the base year:

```
rel[t]  = log( Y_CN[t] / Y_US[t] )      # element-wise, 4 elements
move    = rel[horizon] - rel[base]
```

Logs so that a swap of the two states negates `move` exactly. That is the property PP4 tests and it would not hold for a ratio difference or a percentage change.

---

## 2. The branches, in their frozen order

**R5, dual systemic constraint.** Both states are below `CONSTRAINT_RATIO` of their own unconstrained counterfactual on the primary element. Tested first because a world where both states are hitting ceilings is a different kind of world from one where either is winning, and the relative measure cannot see it -- two constrained states can look like parity.

**R3, challenger peaking.** Whichever state is gaining in the first third of the window is the challenger. If the challenger's mean relative position later gives back at least `REVERSAL_DEPTH` in logs from its within-window peak, the trajectory is R3. Measured on the mean across elements, so a reversal in one domain while the other three continue does not qualify.

`SPECIFICATION.md` names R3 "PRC peaking". This rule defines it generically as **challenger** peaking. Under a state swap the specification's label would have to become "US peaking", which is not in the regime set, so the PRC-specific label breaks equivariance while the concept does not. The PRC reading is recovered by observing which state is the challenger in the actual data. This is a deliberate divergence from the specification's wording and it is registered as such rather than left as an implementation liberty.

**R4, segmented bipolarity.** At least one element beyond the deadband in each direction: no single hierarchy holds across the capability vector. This is the project's expected result and it is tested fourth, after the two regimes that could otherwise be absorbed into it.

**R1 and R2, concentration.** All movement beyond the deadband runs one way. R1 is PRC-favourable, R2 US-favourable.

Elements inside the deadband do not block concentration. A flat element establishes no competing hierarchy, so partial one-directional movement is concentration, not segmentation.

**R0, no material change.** Nothing moved beyond the deadband either way.

---

## 3. Two defects this rule was written to fix

Both were found by the prior-predictive gates and are recorded in `model/PRIOR-PREDICTIVE-RUN-001.md`.

**The R4 sink.** The original classifier sent any trajectory that was neither cleanly divergent nor cleanly peaking to R4. Mixed-with-flat cases therefore accumulated in the thesis regime. PP2 failed as a direct consequence: R4 could not be pushed below 0.2 mass by any adversarially chosen baseline, which meant the central claim was not refutable by the model, only asserted by the classifier. The fix reassigns partial one-directional movement to R1 or R2, and moves mass away from the thesis.

**The absence of R0.** `SPECIFICATION.md` presents five regimes as an exhaustive partition. It is not exhaustive: a world in which neither state moves materially is a possible world, and it is none of the five. Folding it into any substantive regime would overstate that regime. R0 is exempt from the PP1 coverage floor, since a residual is not a prediction.

R0 carries 0.385 mass at the 2030 horizon and 0.003 at 2075 in run 003, which is the expected shape -- twenty-four years of divergence is detectable and four years is mostly not. That the bucket is large at short horizons is itself worth stating: claims about relative position on a 2030 horizon are substantially claims about measurement noise.

---

## 4. The constants

| Constant | Value | Basis |
|---|---:|---|
| `DEADBAND` | 0.10 | Roughly 10.5% in relative position. Judgement. Below this, movement is not distinguishable from measurement bias given the definitional gaps documented in `DATA-INTEGRITY.md`. |
| `REVERSAL_DEPTH` | 0.15 | Judgement. Sized above the deadband so a reversal must exceed the threshold for movement to be recognised at all. |
| `CONSTRAINT_RATIO` | 0.60 | Judgement. A state producing under 60% of its unconstrained counterfactual is materially constrained. |

None of the three is sourced, and no sensitivity run over them has been performed. Regime masses will move with all three, and the direction is knowable in advance: a wider deadband moves mass from R1, R2 and R4 into R0; a deeper reversal requirement moves mass out of R3; a lower constraint ratio moves mass out of R5.

**Because R5 currently fails PP1 at 0.025 mass, `CONSTRAINT_RATIO` is a parameter whose adjustment would make a failing gate pass.** It is frozen at 0.60 and the failure is reported. Any later change requires a dated amendment with justification independent of the gate outcome. That constraint is stated here, in the file containing the parameter, rather than only in the disclosure document, because this is where someone would come to change it.

---

## 5. Priority order is part of the rule

A trajectory can satisfy more than one branch. Reported regime masses are conditional on the order `R5, R3, R4, R1/R2, R0`, which is frozen. Reordering is a major version bump, not a refactor.

The order is not neutral, and it is chosen against the project's interest: R4 is the expected result and is tested *after* R3 and R5, both of which can claim trajectories that would otherwise be R4. The reverse order would inflate the thesis regime.

---

## 6. Tests

1. **Swap equivariance.** For any trajectory, classifying the state-swapped mirror returns the mirrored label: R1 to R2, R2 to R1, R3 to R3, R4 to R4, R5 to R5, R0 to R0. PP4 runs this on 400 paired draws and requires exactness, not tolerance.
2. **Determinism.** Same trajectory, same horizon, same label.
3. **Priority.** A synthetic trajectory satisfying both the R5 and R4 tests returns R5. One satisfying both R3 and R4 returns R3.
4. **Deadband boundary.** Movement of exactly `DEADBAND` does not trigger; the comparison is strict.
5. **Horizon bound.** A horizon beyond the simulated window raises rather than clamping to the last year.
6. **R0 reachability.** A flat trajectory returns `R0_no_material_change` and never a substantive regime.

---

## 7. Open items

- No sensitivity run over the three constants. Until one exists, every reported regime mass carries unquantified sensitivity to three judgement calls.
- The R3 branch uses the mean across elements while R4 uses per-element tests. The inconsistency is deliberate -- a reversal should be a system-level phenomenon while segmentation is by definition per-domain -- but it has not been tested for cases where the two definitions disagree.
- The divergence from `SPECIFICATION.md` on the R3 label is registered but the specification text has not been rewritten. The amendment appends; it does not correct the original wording.

---

## Sources

- `model/SPECIFICATION.md` -- five-regime output contract and the R009 registration amendment
- `model/IDENTIFICATION.md` -- PP1 to PP5 gate definitions
- `model/PRIOR-PREDICTIVE-RUN-001.md` -- the two defects, and the PP1 R5 failure
- `pipeline/src/usbip/model/prior_predictive.py` -- implementation
- `DATA-INTEGRITY.md` -- definitional gaps underlying the deadband
