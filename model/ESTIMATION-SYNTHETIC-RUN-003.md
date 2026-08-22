# Estimation, synthetic scope -- run 003: adoption of the Amendment 2 + Amendment 03 forms

Date: 2026-08-22. Closes the adoption item recorded at the end of `ESTIMATION-SYNTHETIC-RUN-002.md` section 6: the estimator and the prior-predictive harness now carry the committed forms, not the run-001 synthetic-scope stand-ins.

## 1. What changed

**Initial states (PRIORS.md Amendment 2).** `log x0` location scales are now per-input: 0.5 for the anchored series (D1-D3), 1.0 for the anchor-absent (F1-F3), replacing the uniform 0.3 synthetic-scope choice. The initial growth states take their AR(1) stationary distribution, non-centered: `g0 = gstar + sigma_v / sqrt(max(1 - rho_g^2, 1e-4)) * z_g0`. The clamp is load-bearing -- the Beta(6,2) upper tail otherwise explodes the scale factor and reopens the trapped-chain trap recorded in run 002 (config D2).

**AI intensity (SPECIFICATION.md Amendment 03 + follow-up note; PRIORS.md Amendment 3, provisional).** The deterministic exponential is replaced in both implementations by the committed per-state local linear trend on `log(1 + AI)`: `gstar_ai[i] ~ |N(0.03, 0.02)|` iid per state, `sigma_ai ~ HalfNormal(0.0191)`, persistence shared with `rho_g`, no saturation term, stationary `g_ai0` in the estimator. The cross-state MEAN of `log(1 + AI)` drives the shared `sigma_top` increments (the only simple swap-invariant pooling; follow-up note to Amendment 03).

**Gate re-run (run 005).** All five gates pass at n=400, seed 20260819; `model/prior-predictive-run-005.txt`, report appended to SPECIFICATION.md Amendment 03. PP3 is verbatim identical to run 004 -- the pre-committed strict regression check that AI feeds `sigma_top` and never the x-paths. Strictness is implemented by drawing all AI variates from a spawned child generator and preserving the superseded scalar's main-stream slot (consume-and-discard) so every pre-existing draw keeps its run-004 stream position; a ten-iteration bit-equality fingerprint against the HEAD module confirmed it before the gate run.

## 2. Delta's information path, stated in advance of the fit

AI intensity is **unobserved** in synthetic scope -- the section 7 indicator block does not exist until first ingest -- so `delta`'s information now runs through an unmeasured stochastic latent rather than a deterministic path. Weaker `delta` behaviour than run 001's (already "barely learned", per IDENTIFICATION.md section 2.1) is therefore expected and is not a defect. The recovery table carries `gstar_ai` and `sigma_ai` rows to show how little the data inform them, not because coverage there is informative.

## 3. Smoke check -- D3 configuration re-fit

D3 convention (run 002): floor 0.01, 4 x (2000+400), target_accept 0.95, seeds 20260820 (truth) / 20260821 (data) / 20260822 (sampler), T = 20. The new AI stream adds ~2(T-1) latent dimensions and one new scale.

**Result (`model/smoke-run-005.json`; 525 s): zero divergences, worst r_hat 1.037 (`sigma_z`), min ESS 104.** The D3 convergence standard holds under the new forms with the ~2(T-1) added AI dimensions. The truth draw is bit-identical to the run-001/002 truth (rho_g 0.9866, sigma_D 0.7727) -- the stream-preservation design means the smoke re-fit is a controlled comparison, same truth, new model.

Recovery at 90 percent: covered -- `delta` (truth 0.286), `sigma_top0`, all six `lam`, all six `b_anchored`, both `gstar_ai`, `sigma_ai`. The AI-parameter coverage is prior-domination, not learning, per section 2. Not covered -- `rho_g` (truth 0.987, the same deep-tail miss recorded in run 001), `sigma_D`, `sigma_F`, 2 of 12 `gstar` components. Single-truth misses at this rate are not evidence of miscalibration (run-002 section 4 caveat applies verbatim); the SBC sweep is the calibration instrument.

## 4. Registered for item 3 (full SBC), not fixed here

The synthetic truth generator (`make_synthetic` + numpy `simulate`) fixes `x0` at the baseline, `g0` at `gstar`, and `g_ai0` at `gstar_ai`, while the model now samples all three from their Amendment 2/3 priors. For a single-truth recovery smoke this is a benign prior-wider-than-generator mismatch; **for SBC it is invalidating** -- rank uniformity requires the generator to draw from exactly the model's prior. The run-002 pilot (N=24) generated through this same path and could not have detected the mismatch at pilot power. Requirement registered for the full sweep: a generator path that draws initial states (and the AI latent's initial growth) from the model prior. The gates' own record is unaffected -- `simulate`'s init conventions are frozen precisely so PP3 remains a regression check.

## 5. Environment

numpyro 0.21.0, jax 0.11.1 CPU, Python 3.13.12, x64, `SIGMA_Z_FLOOR = 0.01`. Tests: 53 passing from `pipeline/` (`python3 -m pytest tests/ -q`), including new moment-audit rows for `gstar_ai` (folded-normal mean 0.031173, per-state independence) and `sigma_ai` (HalfNormal at the Amendment 1 scale), and direct mirror-swap pins on the AI stream.

## 6. Full SBC sweep -- protocol, registered before results

The section 4 requirement is implemented: `make_sbc_synthetic` samples every initial state (`log x0` at the Amendment 2 scales, stationary `g0` and `g_ai0` with the model's own 1e-4 clamp) from exactly the model prior and runs the model's recursion in numpy (parameters from the numpy `sample_prior`, CES from the numpy `ces` -- cross-implementation preserved). `simulate` untouched, per section 4. Dispersion of the generator's first-year states is pinned by test (54 passing).

Sweep protocol, committed at launch, 2026-08-22, before any result was seen:

- N = 300 replications, T = 20, demonstration-grade adaptation (D3 config: 4 x (2000+400), target 0.95, floor 0.01).
- Seeds: base 20260822; per-replication data seed `base + 1000*i`, sampler seed `+2` (run-002 convention).
- Ranks on every-5th-draw thinned samples (320 of 1600) for `delta`, `rho_g`, `sigma_D`, `sigma_F`, `sigma_u`, `sigma_v`, `sigma_top0`, `sigma_ai` -- the pilot's seven plus the new AI scale.
- Any replication with divergences is excluded from the rank table and reported, not pooled (run-002 commitment).
- Incremental record `model/sbc-run-003.jsonl` (one row per replication, resumable); summary `model/sbc-full-run-003.json`.
- Compute: 16 CPU worker processes (20-core machine; CUDA jaxlib declined -- the model is committed x64 and consumer-Blackwell FP64 throughput would not beat 16 CPU workers; the arithmetic, ~300 x ~600 s / 16 ≈ 3-4 h, made GPU installation moot).

### Results (`model/sbc-full-run-003.json`, per-replication `model/sbc-run-003.jsonl`; 300 replications, 11,542 s wall on 16 workers)

**Divergences: 169 of 300 replications ran clean (56%); 131 diverged (44%).** The distribution is heavy at the bottom -- most divergent replications carry 1-9 divergences out of 1,600 post-warmup draws (0.06-0.6%) -- with two catastrophic outliers (378 and 216 divergences, replications 158 and 286) and a handful in the tens. Per the pre-committed rule, divergent replications are excluded from the rank table and reported, not pooled. **The 44% divergent fraction is an author-attention item**: it is far above the run-002 pilot's 5/24, and the difference is attributable to the harder truth population -- the run-003 generator draws initial states from the full Amendment 2/3 priors (x0 at scales 0.5/1.0, stationary g0/g_ai0) where the pilot fixed them at point values. Whatever adaptation the published real-data run uses must clear a stricter bar than D3's (zero divergences, section 10), and this sweep says D3-grade adaptation does not reliably deliver that across the prior; expect the published run to need higher target_accept or reparameterisation, and treat that as a known cost, not a surprise.

**Conditioning check (`model/sbc-run-003-divergence-analysis.json`).** Excluding 44% of replications conditions the rank table on the clean subset, so the truth-region dependence of divergence was measured directly (truths regenerated from seeds). The dependence is weak: the largest point-biserial correlation between the divergence indicator and any truth parameter is 0.17 (`sigma_u`, higher-noise truths diverge slightly more often), with `rho_g` at -0.15 -- divergent replications have LOWER-persistence truths on average, the opposite of the near-unit-root hypothesis. Clean-only versus all-replication rank means differ by at most 0.017 on any parameter. The exclusion is therefore not carving out an identifiable pathological truth region at these correlations, though 44% exclusion remains a power and interpretation cost stated as such.

**Rank uniformity (clean subset, N=169; normalised rank u = rank/320; uniform implies mean 0.50, sd 0.289, expected extreme count -- u below 0.05 or above 0.95 -- 16.9 with binomial sd 3.9):**

| Parameter | mean u | sd u | extremes |
|---|---|---|---|
| `delta` | 0.534 | 0.298 | 25 |
| `rho_g` | 0.523 | 0.301 | 18 |
| `sigma_D` | 0.497 | 0.303 | 17 |
| `sigma_F` | 0.548 | 0.296 | 22 |
| `sigma_u` | 0.496 | 0.289 | 12 |
| `sigma_v` | 0.489 | 0.304 | 24 |
| `sigma_top0` | 0.473 | 0.290 | 14 |
| `sigma_ai` | 0.500 | 0.290 | 14 |

**No decisive miscalibration.** Every sd sits at the uniform 0.289 within noise. Two statistics reach roughly two sigma uncorrected -- `sigma_F`'s mean at 0.548 (+2.2 sigma against se 0.022) and `delta`'s extreme count at 25 (+2.1 sigma) -- and neither survives an eight-parameter multiplicity correction; they are recorded here so that if either recurs in a later sweep it reads as a pattern, not a first appearance. `sigma_ai`, the new AI scale, is as uniform as anything in the table (mean 0.500, sd 0.290): the machinery handles the parameter it cannot learn, which is what SBC tests. **The run-002 full-sweep obligation is closed**: hundreds of replications, demonstration-grade adaptation, thinned ranks, divergent replications excluded-and-reported, generator drawing from exactly the model prior.
