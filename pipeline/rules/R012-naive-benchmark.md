# R012 -- Naive benchmark: driftless per-element random walk

```yaml
rule:
  rule_id: R012
  version: 0.1.0
  name: Driftless per-element random walk benchmark for long-horizon trajectories
  applies_to: [model output, all reported horizons]
  inputs: [observed log relative capability per element, 1975-2025]
  output: benchmark predictive distribution per element per horizon
  parameters:
    innovation_scale: derived per element by the committed procedure below; vintage recorded at derivation
  determinism: true
  supersedes: null
```

Registered 2026-08-20 by author decision in structured Q&A, routed here from Paper A review action A5 (`papers/paper-a-measurement/REVIEWS.md`, Disposition): a benchmark named in a paper without a registered rule would be a commitment made outside the machinery, so the naming and the registration happen together, here.

---

## The rule

For each capability element m, the benchmark distribution for log relative capability `r[m,t] = log(Y_CN[m,t] / Y_US[m,t])` at horizon t is a **driftless random walk** from the last observed value:

```
r[m, t] ~ Normal( r[m, t_last],  s_m^2 * (t - t_last) )
```

No drift term. No cross-element structure. Nothing else.

**Why driftless, stated once.** A benchmark exists to be the least-structured admissible comparator. Estimated drift is trend extrapolation, which is half of what the model itself does; a benchmark that extrapolates trend is a competitor, not a floor. Hold-last-value-constant was declined as degenerate: a zero-width distribution cannot be scored probabilistically at all.

## Derivation procedure for s_m, named before computing

Same discipline as the `s_v` derivation in `model/PRIORS.md` Amendment 1: procedure committed before any value is computed.

1. **Data.** The observed `r[m,t]` series over the estimation window, as constructed by the estimation pipeline's Block M inputs at their committed definitional bases, from committed snapshots.
2. **Differences.** `d[m,t] = r[m,t] - r[m,t-1]` over all consecutive observed pairs.
3. **Scale.** `s_m = sd(d[m,t])`, per element, rounded to three significant figures.
4. **Commitment.** The values, their vintage, and the snapshot hashes are recorded in a follow-up amendment referencing this one. They are frozen per evaluation-year vintage; a revision to the underlying series produces a new dated derivation, both published.

The procedure cannot run until first ingest supplies the observed series; that ordering is the point -- the rule exists now, before any value or any model output it will be compared against.

## Scope and scoring

- **Prospective only.** The benchmark applies to evaluation years and horizons whose outcomes do not exist at registration. No retroactive scoring of the 2026 baseline against it.
- Scored on the same output-contract quantities as the model (element-wise ratios at the reported horizons), under whatever proper scoring rule the programme adopts if the section 9 question 1 restatement is ever made; until then, coverage comparison only.
- Reported alongside every model trajectory per the mandatory-benchmark consequence adopted in Paper A section 5.6.

## Version note

0.1.0, not 1.0.0: the innovation scales are specified by procedure but never yet computed, and a rule whose parameters have never been derived is not at 1.0 merely because it is written down.
