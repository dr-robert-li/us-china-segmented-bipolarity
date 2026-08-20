# Paper A, section 6 -- Identification, stated per quantity

**Status.** Draft, 2026-08-20. This section reproduces, in paper form, the per-quantity identification statements committed in the programme's identification file before estimation, so that its admissions cannot be described as concessions extracted by referees.

---

## 6.1 The disciplinary norm being met

The best latent-measurement work declares non-identification in the running text and names the identifying restriction. Verbatim, from the primary sources: "the model parameters are not identified without further assumptions" and "we lack global identification" ([Treier and Jackman](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=61fb0ba9b2e3c6b8619a4aa493fa55f26ff6c10c)); "a model without this restriction is not identified with respect to rotation" ([Fariss, p. 305 n. 27](http://cfariss.com/documents/Fariss2014APSR.pdf)); "we currently lack the necessary overlapping observations to completely identify the scale of the latent trait cross-nationally" and "we lack sufficient data to fully model DIF cross-nationally, weakening the cross-national comparability of the V-Dem measures" ([V-Dem measurement model](https://scispace.com/pdf/the-v-dem-measurement-model-latent-variable-analysis-for-1997yaxojn.pdf)); and, on untestable assumptions, "Although we cannot directly test this assumption" ([Pemstein, Meserve and Melton](https://www.cambridge.org/core/journals/political-analysis/article/democratic-compromise-a-latent-variable-analysis-of-ten-measures-of-regime-type/2A6B2BBA6F80367644F2C5007E1CFC29)). This section holds itself to that standard, per quantity.

## 6.2 The small-n problem, without softening

The model is fitted on great-power dyads, of which six to eight exist -- five under the strictest inclusion rules, since two of the listed dyads are marginal (one on scale, one arguably pre-industrial and out of scope) -- one is the case under study, and at most four are usable for held-out testing, against a specification carrying dozens of parameters. The honest description of the historical exercises is therefore **calibration, not validation**: they test whether the structure produces sane behaviour on cases it did not see, and they do not constitute out-of-sample validation in the large-n sense of the word. No established method exists to appeal to -- the extant power-transition testing tradition is frequentist regression on dyad-year panels, not Bayesian small-n -- so the protocol is constructed rather than adopted, which makes it weaker evidence than an adopted standard would be. A reader is entitled to discount it on that basis.

The same tradition supplies the empirical justification for the programme's basic commitments: subsequent testing of power-transition theory with alternative capability measures found that "the strength of the evidence depends importantly on how power is measured and the set of cases analyzed" ([de Soysa, Oneal and Park, *JCR* 41(4)](https://journals.sagepub.com/doi/10.1177/0022002797041004002)). Results turning on the capability measure and the case set is a documented failure mode; the explicit vector and the published case set are responses to it.

The count is also the discipline's, not only this programme's. Section 3.4 records that the leading peaking-power argument's own stated selection rule yields nine cases, three of which its author sets aside as overdetermined -- a load-bearing base of roughly five to six. The programme's analogue count is the field's actual evidentiary standard stated openly, not an unusually thin base confessed to; what distinguishes the treatments is that here the count constrains the vocabulary ("calibration, not validation"), which is a constraint the surrounding literature does not usually accept from the same arithmetic.

## 6.3 What is identified, and by what

| Object | Identified | By what |
|---|---|---|
| Input trajectories, anchored series | Yes | Physically-measurable and audited series, multiple sources per quantity |
| Bundle elasticities `sigma_D`, `sigma_F` | Weakly | Within-case relative variation; priors do real work |
| Top-level elasticity level `sigma_top[t]` | Weakly | Cross-bundle substitution patterns; the weakest of the elasticities |
| Mechanism parameter `delta` | **Contingent** | Requires within-sample variation in AI-robotics intensity, which exists only from roughly 2015 -- about a decade of informative data |
| Nesting order | Yes, comparatively | Leave-one-decade-out predictive density; the comparison is identified even where levels are not |
| Stabilisation coefficients `psi[j,i]` | Weakly | Stress variation within case |
| Element weights `w[m]` | Yes, under ordering constraints | The constraints are what make them identified |
| Source bias, anchored quantities | Yes | Multiple sources on one latent quantity |
| Source bias, anchor-absent quantities | **No** | Fixed at prior mean, flagged `anchor_absent` in every consuming output |
| Saturation ceilings `xbar[j,i]` | **No, within horizon** | No case has saturated on the relevant inputs; priors carry this entirely |
| `R4` versus `R5` under simultaneous saturation | **No** | Structural degeneracy, 6.5 |

The sharpest constraint deserves its own sentence: `delta`, the parameter that carries the mechanism proposition, has ten to eleven years of informative annual data, on two states, for a fifty-year projection. The plausible outcome is not a precise estimate with the wrong sign; it is that `delta` is barely learned at all, and the pre-registered contraction gate forces that outcome to be reported as "not learned" rather than as a directional finding with a wide interval.

The consequence for the companion paper is stated here rather than discovered there. If `delta` and its weakly identified neighbours remain prior-dominated, the long-horizon regime posterior is, to first order, a sensitivity analysis of the committed priors rather than an empirical finding, and it will be reported under that description. This is anticipated as the likely primary result, not feared as a failure mode: a fifty-year projection whose data-informed content is honestly separated from its prior-driven content is the deliverable, and the contraction diagnostics in the output contract are the instrument that performs the separation.

## 6.4 The asymmetric backtest

One historical test carries an asymmetric bar, and the asymmetry needs defending in a measurement paper. The model must not have forecast US decline at 1957, 1973, or 1987 -- the peaks of documented declinist waves, each of which produced confident predictions of relative decline that did not occur on the predicted timeline. Run on data available at those dates, the specification must place less than 0.35 posterior mass on the US-unfavourable divergence regime at a twenty-year horizon, or be rejected with the failing configuration committed. The threshold is frozen and may not be raised after a run.

The bar is asymmetric because the failure mode is asymmetric: a model built in 2026 by an author who has read the declinist literature risks encoding the 1987 reasoning, and there is no comparable history of confident falsified predictions of US ascendancy from which to construct the mirror test. The objection that this hard-codes an anti-declinist prior is answered by what the test disciplines: behaviour on historical data, not conclusions on current data. A specification that correctly reads 1957, 1973 and 1987 as non-transitions and nonetheless reads 2026--2050 as divergence is permitted and would be a strong result. And the prohibition on asymmetric standards runs both ways: if a comparable series of documented, confident, falsified predictions of PRC collapse is assembled, an equivalent test on that side is added by amendment -- recorded as an open commitment, not claimed as done.

## 6.5 Known degeneracies, characterised rather than resolved

1. **`R4` versus `R5` under simultaneous saturation.** At the saturation boundary, segmentation by domain and suppression in both domains produce nearly identical observables. Committed treatment: where posterior mass on the union exceeds 0.5 and neither member exceeds 0.3, the output reports the union and states that the two are not separated -- it does not report whichever is marginally higher.
2. **Bias against level under a missing anchor.** Handled by fixing and flagging (6.3).
3. **Saturation ceiling against growth persistence.** A low ceiling with high persistence and a high ceiling with low persistence produce similar medium-horizon trajectories and divergent long-horizon ones. This is the primary reason the 2075 intervals are wide, and the reason the ceiling sensitivity run is mandatory.
4. **Elasticity level against nesting order.** A published replication found elasticities from near-Leontief to effectively unbounded depending on nesting structure ([Henningsen, Henningsen and van der Werf](https://backend.orbit.dtu.dk/ws/files/149724340/melju_1_s2.0_S0140988317304395_main.pdf)). The model therefore reports the elasticity posterior conditional on each nesting structure separately and never marginalises over structures to produce a single headline elasticity.
