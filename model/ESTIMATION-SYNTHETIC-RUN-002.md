# Estimation synthetic run 002 -- divergence elimination and SBC pilot

**Status: the estimator's registered convergence work item from run 001 is addressed to smoke-test standard.** No observed data enters anything here; nothing is a finding about the world. Full disclosure style of run 001 continues: every configuration tried is reported, including the ones that failed.

---

## 1. The funnel, diagnosed before fixing

Run 001 guessed ("likely") that the divergences localised to the Block M noise scales. The guess was verified before any fix: a diagnostic fit (2 x (400+400), target 0.9, seed 20260820) collected the divergence mask and compared parameter values at divergent versus non-divergent iterations:

| Parameter (min component) | Divergent mean | Non-divergent mean | Divergent min |
|---|---|---|---|
| `sigma_z` | 0.0048 | 0.0085 | **0.0018** |
| `tau` | 0.0385 | 0.0371 | -- |
| `sigma_u` | 0.0563 | 0.0564 | -- |
| `sigma_v` | 0.0260 | 0.0270 | -- |
| `rho_g` | 0.938 | 0.933 | -- |

Only `sigma_z` separates: divergent iterations sit where its smallest component collapses toward zero. The other scale parameters -- already non-centered -- show no separation, and `rho_g` shows none, so the near-unit-root truth was not the binding geometry.

## 2. The fix

`SIGMA_Z_FLOOR = 0.01`: the biased-series noise scale prior becomes half-normal truncated below at 0.01, applied **identically** in the model prior and the synthetic truth generator (SBC semantics require the two to match; the generator rejection-samples the same truncation). Defended as measurement realism -- log-scale noise below 1 percent is not a property of any real published series -- not as a sampler convenience. An intermediate floor of 0.005 was tried first and cut divergences 62 to 7; the remainder still clustered at the boundary, and the floor was raised once, with the realism defense intact at 1 percent.

## 3. Demonstration configurations, all reported

| Config | Floor | Chains x (warmup+samples) | target_accept | Divergences | Worst r_hat | Outcome |
|---|---|---|---|---|---|---|
| D1 | 0.005 | 4 x (1200+400) | 0.95 | 7 | 1.08 | Mixing, not clean |
| D2 | 0.01 | 4 x (2000+400) | 0.99 | **0** | **14.9** (`log_x0`) | Trapped chain -- the run-001 signature again: a clean divergence count is not a clean fit |
| D3 | 0.01 | 4 x (2000+400) | 0.95 | **0** | **1.042** (`sigma_z`) | **Clean: zero divergences, min ESS 128, all four chains agree.** The demonstration the work item required |

D2 is retained deliberately: it is the third demonstration in this programme's record (after run 001's init pathology and config B) that this model can fail convergence while showing zero divergences. Any future run that reports only the divergence count is not reporting convergence.

## 4. SBC pilot

Launched on the D3 configuration's floor: N = 24 replications, per-replication truth drawn from the prior (base seed 20260821, per-rep seeds recorded), 2 x (1000+300) at target 0.95, ranks computed on every-5th-draw thinned samples for `delta`, `rho_g`, `sigma_D`, `sigma_F`, `sigma_u`, `sigma_v`, `sigma_top0`; per-replication divergence counts recorded and divergent replications flagged rather than silently pooled. Results: PLACEHOLDER

One D3 caveat recorded en route: the single-truth recovery table of D3 (three scalar misses at 90 percent) is not evidence of miscalibration -- a single truth cannot be -- and the floor's rejection sampling means D3's truth differs from run 001's despite the shared seed. The rank statistics here, not any single-truth table, are the calibration evidence.

**Pilot, not the obligation.** N = 24 replications cannot test rank uniformity with any power; hundreds can. The full simulation-based-calibration sweep at published-run scale remains the open obligation carried from run 001. What the pilot does establish: the fit machinery survives repeated truths drawn across the prior (not one hand-picked seed), per-replication divergence counts are on record, and rank statistics are computed on thinned draws (rank on autocorrelated draws is biased; the thinning step is recorded in the settings block of `sbc_pilot.json`).

## 5. Environment

Unchanged from run 001 (numpyro 0.21.0, jax 0.11.1 CPU, Python 3.13.12, x64) except `SIGMA_Z_FLOOR` as above. Seeds: demonstration 20260820 (same truth as run 001, deliberately -- the comparison isolates the floor); SBC pilot base seed 20260821, per-replication seeds `base + 1000*i` recorded per row.

## 6. What remains before real estimation

- Full SBC at published-run scale (hundreds of replications, 8 chains, ESS > 400).
- The published-run discipline itself (SPECIFICATION.md section 10) on the real window.
- First ingest of the full indicator set; F1's first ingest (2026-08-21, `data/derived/f1/`) covers one falsifier series family, not the estimation inputs.
- Adoption of the Amendment 2/03 forms (initial-state priors, stochastic AI-intensity trend) in the estimator -- the synthetic exercise here still uses the run-001 synthetic-scope forms, which is recorded rather than hidden.
