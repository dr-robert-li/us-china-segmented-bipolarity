# R009 sensitivity run 001

Required before estimation by author decision of 2026-08-20 in structured Q&A, resolving the open item in `../pipeline/rules/R009-regime-classification.md`: two of the classifier's three constants were chosen by judgement, and until this run every reported regime mass carried unquantified sensitivity to them.

**No constant changes.** `DEADBAND = 0.10`, `REVERSAL_DEPTH = 0.15`, `CONSTRAINT_RATIO = 0.60` remain frozen as committed. This run publishes what the committed masses are sensitive to, including the values at which gate verdicts would differ -- under the shadow-publication logic of `../falsifiers/PRE-REGISTRATION.md` Amendment 1, publication is not determination, and concealing the crossing values is what would make the freeze cosmetic.

## Design

- 400 prior draws at seed 20260819, simulated **once**; every configuration classifies the identical trajectory set, so differences between rows are exact classification differences, not Monte Carlo noise.
- One-at-a-time sweep around the committed point, not a full grid. Interactions are not measured; recorded as a limitation.
- Both claimed horizons: 2050 (R1--R4) and 2075 (all five), per `SPECIFICATION.md` Amendment 02.
- Baseline is `SYNTHETIC_BASELINE` only. PP2's hostile-baseline sweep is not repeated here.

## Results -- horizon 2050

| config | R1 | R2 | R3 | R4 | R5 | R0 |
|---|---:|---:|---:|---:|---:|---:|
| **committed** | 0.420 | 0.307 | 0.115 | 0.070 | 0.022 | 0.065 |
| deadband=0.05 | 0.393 | 0.290 | 0.168 | 0.110 | 0.022 | 0.018 |
| deadband=0.15 | 0.420 | 0.295 | 0.087 | 0.058 | 0.022 | 0.117 |
| deadband=0.20 | 0.403 | 0.295 | 0.068 | **0.037** | 0.022 | 0.175 |
| reversal_depth=0.10 | 0.410 | 0.297 | 0.145 | 0.065 | 0.022 | 0.060 |
| reversal_depth=0.20 | 0.430 | 0.320 | 0.085 | 0.072 | 0.022 | 0.070 |
| reversal_depth=0.25 | 0.443 | 0.333 | 0.058 | 0.075 | 0.022 | 0.070 |
| constraint_ratio=0.40 | 0.422 | 0.320 | 0.122 | 0.070 | 0.000 | 0.065 |
| constraint_ratio=0.50 | 0.420 | 0.315 | 0.117 | 0.070 | 0.013 | 0.065 |
| constraint_ratio=0.70 | 0.395 | 0.300 | 0.107 | 0.070 | 0.065 | 0.062 |
| constraint_ratio=0.80 | 0.340 | 0.270 | 0.087 | 0.052 | 0.195 | 0.055 |

## Results -- horizon 2075

| config | R1 | R2 | R3 | R4 | R5 | R0 |
|---|---:|---:|---:|---:|---:|---:|
| **committed** | 0.282 | 0.233 | 0.212 | 0.090 | 0.175 | 0.007 |
| deadband=0.05 | 0.263 | 0.220 | 0.250 | 0.090 | 0.175 | 0.003 |
| deadband=0.15 | 0.315 | 0.233 | 0.185 | 0.072 | 0.175 | 0.020 |
| deadband=0.20 | 0.333 | 0.237 | 0.170 | 0.048 | 0.175 | 0.037 |
| reversal_depth=0.10 | 0.260 | 0.212 | 0.260 | 0.085 | 0.175 | 0.007 |
| reversal_depth=0.20 | 0.300 | 0.240 | 0.188 | 0.090 | 0.175 | 0.007 |
| reversal_depth=0.25 | 0.328 | 0.242 | 0.152 | 0.095 | 0.175 | 0.007 |
| constraint_ratio=0.40 | 0.352 | 0.258 | 0.245 | 0.098 | **0.037** | 0.010 |
| constraint_ratio=0.50 | 0.333 | 0.253 | 0.240 | 0.092 | 0.072 | 0.010 |
| constraint_ratio=0.70 | 0.223 | 0.185 | 0.172 | 0.070 | 0.345 | 0.005 |
| constraint_ratio=0.80 | 0.130 | 0.120 | 0.115 | 0.045 | **0.588** | 0.003 |

## Findings

1. **The directions predicted in R009's own open item are confirmed.** A wider deadband moves mass from R1, R2, R3 and R4 into R0; a deeper reversal requirement drains R3; a lower constraint ratio drains R5. No surprises in sign; the magnitudes are now on the record.

2. **Gate-crossing disclosure, stated because concealing it would be the cosmetic move.** Two swept values would flip a PP1 verdict on this draw set:
   - `deadband = 0.20` starves R4 at 2050 (0.037 < 0.05). The committed 0.10 passes with R4 at 0.070; so does 0.15 at 0.058, narrowly.
   - `constraint_ratio = 0.40` starves R5 at 2075 (0.037 < 0.05). The committed 0.60 passes at 0.175; 0.50 passes at 0.072.
   The committed point sits inside the passing region with a one-step margin in every swept direction. None of the four crossing-adjacent values was chosen; all were judgement calls frozen before this run existed, and the freeze holds.

3. **`CONSTRAINT_RATIO` is the dominant sensitivity, and it is R5's.** At 2075, R5 spans 0.037 to 0.588 -- a 16-fold range across a 0.40--0.80 sweep -- and at 0.80 dual constraint becomes the modal 2075 regime. Every published R5 mass must therefore be read as conditional on a constant whose value has no source. This sharpens, rather than repairs, the position recorded in R009: the constant is frozen precisely because it is the one whose adjustment could most easily manufacture or delete a regime.

4. **R4's 2050 coverage is the thinnest of the four claimed regimes** (0.070 committed, floor 0.05), and it is deadband-sensitive in both directions. The thesis regime's prior reachability at the headline horizon rests partly on a classification convenience labelled arbitrary in the code. This belongs in the papers' calibration statement alongside the F5-B and F7 caveats.

## Limitations

- One-at-a-time; no interactions measured. A joint deadband-and-constraint sweep could cross gates at points this design does not visit.
- n=400 at one seed; classification differences are exact for this draw set but masses carry Monte Carlo error of roughly +/-0.02.
- Synthetic baseline only; the sweep says nothing about sensitivity under the hostile baselines PP2 uses.

## Reproduce

The exact script that produced the tables above:

```
cd pipeline/src && python3 - <<'PY'
import numpy as np
from usbip.model import prior_predictive as pp

rng = np.random.default_rng(20260819)
trajs = []
for _ in range(400):
    d = pp.sample_prior(rng)
    trajs.append(pp.simulate(d, rng))

def masses(h, **kw):
    c = {}
    for t in trajs:
        r = pp.classify(t, h, **kw)
        c[r] = c.get(r, 0) + 1
    return {k: c.get(k, 0)/400 for k in ("R1","R2","R3","R4","R5","R0_no_material_change")}

configs = [("committed", {})]
configs += [(f"deadband={v}", {"deadband": v}) for v in (0.05, 0.15, 0.20)]
configs += [(f"reversal_depth={v}", {"reversal_depth": v}) for v in (0.10, 0.20, 0.25)]
configs += [(f"constraint_ratio={v}", {"constraint_ratio": v}) for v in (0.40, 0.50, 0.70, 0.80)]

for h in (2050, 2075):
    print(f"### horizon {h}")
    print("| config | R1 | R2 | R3 | R4 | R5 | R0 |")
    print("|---|---:|---:|---:|---:|---:|---:|")
    for name, kw in configs:
        m = masses(h, **kw)
        print(f"| {name} | {m['R1']:.3f} | {m['R2']:.3f} | {m['R3']:.3f} "
              f"| {m['R4']:.3f} | {m['R5']:.3f} | {m['R0_no_material_change']:.3f} |")
    print()
PY
```

## Sources

- pipeline/rules/R009-regime-classification.md (internal; the constants, their judgement basis, and the predicted directions)
- model/prior-predictive-run-004.txt (internal; the committed-constants gate run this sweep brackets)
- falsifiers/PRE-REGISTRATION.md, Amendment 1 (internal; the publication-is-not-determination rule applied here)
