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
