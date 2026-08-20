# Paper A -- Measurement and method

**Working title.** Capability as a Vector: Measuring Techno-Industrial Position Without a Composite Index

**Status.** Outline committed at Phase 4. No section drafted except section 3, which is committed alongside this file as `S3-capability-vector.md`. Nothing in this outline may be read as a result.

**Target.** A methods-and-measurement journal or the methods section of an international-relations journal. Audience is academic peers, not investors and not policy planners. The paper's value if the substantive thesis in Paper B turns out to be wrong must be positive, and this outline is written so that it is.

---

## 1. What this paper claims, and what it does not

Four claims. Each is stated here with the strongest published objection to it attached, because a claim whose opposition is not engaged where the claim is made is not being tested.

| # | Claim | Strongest published objection |
|---|---|---|
| C1 | Techno-industrial capability should be reported as a small vector with explicit posterior uncertainty, not as a scalar composite | Scalar composites have demonstrated out-of-sample predictive validity on conflict outcomes; a vector has none, and declining to aggregate declines to answer the question the field asks |
| C2 | The scalar-versus-vector choice is empirically consequential, not stylistic, because the sign of relative movement is dimension-dependent within the same years | If component series are highly correlated, aggregation is nearly lossless and the objection is academic |
| C3 | Definitional non-comparability between two states' published statistics should enter as measurement uncertainty, not be absorbed into a ratio | This inflates intervals to the point of vacuity, and an interval wide enough to contain every hypothesis has no content |
| C4 | A long-horizon claim can be pre-registered even though its data are observational, because the outcome has not yet been realised | Pre-analysis plans have limited upside outside costly one-off experiments, discourage novel design, and cannot be verified against prior glimpsing in historical-data settings |

**What the paper does not claim.** It does not claim the vector predicts conflict better than a scalar index. It does not claim pre-registration improves accuracy. It does not claim the measurement model is identified in every parameter -- section 6 names the parameters it is not identified in. And it makes no claim about which state is stronger, which is a question the paper argues is not well posed as asked.

---

## 2. Introduction -- the problem the field has, stated with its own literature

The opening does not assert that scalar power indices are bad. It shows that the field's own practitioners say so, in print, while continuing to use them.

- CINC aggregates six components -- total population, urban population, iron and steel production, primary energy consumption, military personnel, military expenditure -- as an unweighted mean of system shares, currently at version 7.0 covering 1816--2022 ([Correlates of War](https://correlatesofwar.org/data-sets/national-material-capabilities/)). The codebook states the equal weighting explicitly, and states that the index "could then be computed on as few as one component" ([NMC v5 codebook](https://correlatesofwar.org/wp-content/uploads/NMC_Documentation_v5_0.pdf)).
- Carroll and Kenkel find that the equal weighting "is entirely ad hoc" and that the index "assigns the same importance to military spending as it does to personal energy consumption", with capability ratios improving out-of-sample prediction over a null model by 1.2 per cent ([Carroll and Kenkel](https://www.sas.rochester.edu/psc/polmeth/papers/Kenkel_Carroll.pdf)).
- Lind shows CINC "codes the Soviet Union as overtaking U.S. power in the 1970s" and "ranks India in 2007 as the world's third-largest power" ([Lind, *International Security* 49(2)](https://direct.mit.edu/isec/article/49/2/7/125214/Back-to-Bipolarity-How-China-s-Rise-Transformed)).
- Beckley counts "at least sixty-nine power measurement frameworks from 1936 to 2010", of which forty-two used gross indicators alone, and reports that "more than 1,000 peer-reviewed studies have used CINC to measure power" ([Beckley, *International Security* 43(2)](https://direct.mit.edu/isec/article-abstract/43/2/7/12211)).
- A survey commissioned outside the academy reaches the same conclusion independently: "The notion of a single aggregate quantity of national power existing in the abstract therefore makes little or no sense", and "Aggregated measures of power select and weight variables in an essentially arbitrary way" ([Carnegie Endowment](https://carnegieendowment.org/research/2026/04/methods-of-national-power-analysis-pitfalls-and-best-practices)).

**The introduction then concedes the two hardest facts against its own position, before proceeding.**

First, scalar reduction has repeatedly been found to lose little. Kugler and Organski operationalise power as "Economic Productivity per Capita x Population", proxy it with GNP, and report that this "parsimonious and robust measure performed as well as the more complex index of power developed by Singer et al. (1972)" ([Kugler and Organski, pp. 190--191](http://slantchev.ucsd.edu/courses/pdf/Kugler%20&%20Organski%20-%20The%20Power%20Transition.pdf)). Beckley's two-variable product predicts 78 per cent of wars and 70 per cent of militarised disputes over 1816--2010 against CINC's 70 and 64 per cent ([Beckley](https://scispace.com/pdf/the-power-of-nations-measuring-what-matters-441eqyutp6.pdf)). Adding components did not help; multiplying two did.

Second, the arbitrary-weights critique is weaker than it is usually stated. The Lowy Institute publishes its weights -- Economic Capability 17.5 per cent, Military Capability 17.5 per cent, Resilience 10, Future Resources 10, Economic Relationships 15, and Defence, Diplomatic and Cultural Influence 10 each -- concedes that "it is of course possible to reach other value judgements about the relative importance of the measures", and then reports that its own "Sensitivity analysis has determined that the large number of indicators ... are quantitatively more important than our weighting scheme" ([Lowy methodology](https://power.lowyinstitute.org/methodology/)). That is a publisher volunteering evidence against the standard critique of its own product, and this paper does not get to ignore it.

So the paper's case cannot be that a vector predicts better or that weights are the fatal flaw. The case has to be narrower and it is made in section 3: the aggregation step destroys the specific information this research programme is about.

---

## 3. The capability vector -- drafted

Drafted in full in `S3-capability-vector.md`. Summarised here for outline completeness:

- The four elements `Y_throughput`, `Y_frontier`, `Y_net`, `Y_fin`, and why four rather than one or twenty.
- The formal result that makes the choice non-cosmetic: in additive aggregation, weights are substitution rates, not importances ([Munda and Nardo](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC32434/EUR%2021834%20EN.pdf); [OECD/JRC Handbook, p. 112](https://knowledge4policy.ec.europa.eu/sites/default/files/jrc47008_handbook_final.pdf)).
- The empirical demonstration that the sign of relative movement is dimension-dependent over 2015--2025.
- What the vector refuses to do, and the cost of refusing.

---

## 4. Measurement model

The model class is not novel and the paper says so. The contribution is the application domain and the discipline around it, not the estimator.

**4.1 The tradition being joined.** Bayesian latent-variable measurement in political science, with four precedents cited for four distinct reasons:

| Precedent | Cited for |
|---|---|
| [Treier and Jackman](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=61fb0ba9b2e3c6b8619a4aa493fa55f26ff6c10c) | The demonstration that ignoring measurement error manufactures results: downstream `r^2` falls from .63 on raw Polity to .57 on posterior means to .40 once uncertainty is propagated, and the quadratic term becomes indistinguishable from zero |
| [Pemstein, Meserve and Melton](https://www.cambridge.org/core/journals/political-analysis/article/democratic-compromise-a-latent-variable-analysis-of-ten-measures-of-regime-type/2A6B2BBA6F80367644F2C5007E1CFC29) | Precision-weighted aggregation derived from the model rather than chosen by the analyst -- posterior mean `sum_j(t_ij / r_j^2) / (1/r_0^2 + sum_j 1/r_j^2)` -- the direct alternative to CINC's ad hoc equal weighting |
| [Fariss](http://cfariss.com/documents/Fariss2014APSR.pdf) | Dynamic latent traits with time-varying cut-points, and the practice of stating non-identification in a footnote rather than burying it |
| [Hanson and Sigman](https://public.websites.umich.edu/~jkhanson/resources/StateCapac_v1_doc.pdf) | The closest existing analogue: 21 indicators, three retained dimensions -- extractive, coercive, administrative -- deliberately not collapsed to one number |

**4.2 What is measured versus what is latent.** Observed series are noisy, definitionally divergent indicators of latent capability on each element. The measurement block carries a bias term and a scale term per state per element, and the identification of each is stated separately, per element, in section 6.

**4.3 Rules as versioned objects.** Every transformation from published statistic to model input is a registered rule with a semantic version, an author, and a source list. Nine were registered when this outline was committed; the registry has since grown and the drafted `S4-measurement-model.md` carries the current count. The load-bearing one for this paper is the conversion from nameplate generation capacity to dispatchable capacity, which is where the definitional-divergence argument becomes concrete rather than rhetorical.

**4.4 The refusal, stated as a property of the rule.** The dispatchable-capacity rule refuses to emit a cross-state ratio, because United States capacity factors and PRC capacity factors are computed from differently scoped statistics. Relative position on that element enters through the measurement block as uncertainty. The objection -- that this produces intervals too wide to be informative -- is answered by reporting the interval and letting the reader judge, not by narrowing it.

**4.5 One expectation refuted while specifying the rule, recorded rather than deleted.** The standard objection to comparing PRC utilisation hours with United States capacity factors is that the PRC denominator is year-end capacity. The published Chinese methodology is explicitly an average over calendar time ([China Energy Portal](https://chinaenergyportal.org/statistical-reporting-system-for-renewable-energy/)), and the EIA annual figure is likewise a time-weighted average of monthly values ([EIA Table 6.7.A](https://www.eia.gov/electricity/monthly/xls/table_6_07_a.xlsx)). The error is real only in third-party recomputation. The expectation was wrong, the adjustment it would have justified is not applied, and the refutation is reported because the same reasoning is in wide circulation.

---

## 5. Pre-registration for a long-horizon observational claim

**5.1 The purpose, taken from the source that states it most carefully.** "Preregistration distinguishes analyses and outcomes that result from predictions from those that result from postdictions", and, decisively for this paper's framing, "Preregistration does not favor prediction over postdiction; its purpose is to make clear which is which" ([Nosek, Ebersole, DeHaven and Mellor, *PNAS*](https://www.pnas.org/doi/10.1073/pnas.1708274114)). The same authors state that preregistration "does not eliminate the possibility of poor statistical practices, but it does make them detectable", and concede that "there is not yet sufficient experimental evidence establishing its superiority for reproducibility". The claim being made here is therefore auditability, not accuracy.

**5.2 The objections, given at their full strength.** This subsection is not a formality; three of these objections apply to this project specifically.

| Objection | Source | Does it bite here? |
|---|---|---|
| Full pre-specification is infeasible -- a ten-table analysis tree implies `3^10 = 59,049` possible regressions, and plans have exceeded 50 pages | [Olken, *JEP* 29(3)](https://economics.mit.edu/sites/default/files/publications/JEP%20Analysis%20Plans%20Final.pdf) | Yes. Partially met by pre-registering falsification conditions and thresholds rather than a full analysis tree, which is a weaker commitment and is described as such |
| Pre-specification "prevents you from learning about your data as you analyze it" and may cost the nuance that characterises social science | [Olken](https://economics.mit.edu/sites/default/files/publications/JEP%20Analysis%20Plans%20Final.pdf) | Yes, and unresolved. Recorded as a cost accepted, not a cost denied |
| Pre-analysis plans "have quite limited upside" where many hypotheses are tested, and "may discourage the use of novel research designs"; value concentrates in "costly, one-of-a-kind" studies | [Coffman and Niederle, *JEP* 29(3)](https://web.stanford.edu/~niederle/Coffman.Niederle.PAP.JEP.pdf) | Partly. A fifty-year single-run forecast is close to their one-of-a-kind category, which is the only place they concede real value |
| With historical data "a scholar may have glimpsed the data before the study registration", so registration "cannot send as clear a signal" | Anderson (2013), quoted in [Monogan, *PS*](https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/research-preregistration-in-political-science-the-case-counterarguments-and-a-response-to-critiques/E80124ED16BA47D0EA09F03D72B89EC7) | Yes for the 2026 baseline, which uses published historical data. No for the 2030--2050 conditions, whose outcomes do not yet exist |
| Preregistration might lead to "robotic data analysis in which the simple evaluation of hypotheses came at the expense of broader data exploration" | Gelman (2013), via [Monogan](https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/research-preregistration-in-political-science-the-case-counterarguments-and-a-response-to-critiques/E80124ED16BA47D0EA09F03D72B89EC7) | Partly. Answered by Monogan's own remedy: report auxiliary findings "as observations from data -- rather than hypothesis tests" |
| "Many of the most important developments in knowledge came from inductive findings", and non-registered studies may come to be seen as inferior | Laitin (2013), via [Monogan](https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/research-preregistration-in-political-science-the-case-counterarguments-and-a-response-to-critiques/E80124ED16BA47D0EA09F03D72B89EC7) | Not against this paper, but the paper should not be read as prescribing the practice generally, and says so |

**5.3 The pivot.** Monogan classes studies using "existing information" or "time series of economic data" as low-value candidates for registration, and studies where researchers "plan to study an upcoming election" as high-value ([Monogan](https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/research-preregistration-in-political-science-the-case-counterarguments-and-a-response-to-critiques/E80124ED16BA47D0EA09F03D72B89EC7)). A long-horizon forecast is in the second class on his own criterion, because the glimpsing objection cannot apply to a value that does not exist yet. That is the whole argument for pre-registering this project, and it is one sentence long.

**5.4 The operational template already exists and is followed.** The Forecasting Collaborative pre-registered forecasts with rationales on the Open Science Framework and, separately and earlier, lodged "an a priori specific document shared with the journal in April 2020" fixing the dependent variable, the benchmarks and the analytic procedure ([*Nature Human Behaviour* 7:484--501](https://pmc.ncbi.nlm.nih.gov/articles/PMC10192018/)). Fixing the evaluation rule before the forecast, in a separate document, is the part this project copies.

**5.5 Scoring.** Verdicts are categorical threshold crossings, not probability quotes, so no strictly proper scoring rule is currently applied. That is a deficiency and is named as one. Where probabilities are reported, propriety is the relevant property: a rule is strictly proper when the expected-score inequality "holds with equality if and only if `P = Q`, thereby encouraging honest quotes by the forecaster" ([Gneiting and Raftery, *JASA* 102(477)](https://sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jasa.pdf)). Whether the falsification conditions should be restated as probability forecasts scored by log or Brier score is an open question this paper poses and does not settle, because restating them now would change pre-registered conditions after the fact.

**5.6 The hardest fact in the paper.** The Forecasting Collaborative found that "social scientists' forecasts were on average no more accurate than those of simple statistical models ... or the aggregate forecasts of a sample from the general public", beating all three naive benchmarks in 1 of 12 domains, with at least one naive method matching or beating the experts in 11 of 12 domains in the first tournament and 8 of 12 in the second; winning teams remained worse than in-sample random walks in 8 of 12 domains, and "Experts' subjective confidence in their forecasts was not related to the accuracy of their estimates" ([*Nature Human Behaviour*](https://pmc.ncbi.nlm.nih.gov/articles/PMC10192018/)). This is evidence against the enterprise this programme is engaged in, and it is placed in the paper's own methods section rather than in a limitations paragraph at the end. Two consequences are adopted rather than argued away: a naive benchmark is mandatory for every reported trajectory, and confidence statements are not offered as evidence of reliability.

---

## 6. Identification, stated per quantity

The disciplinary norm being met is specific: in the best latent-measurement work, non-identification is declared in the running text and the identifying restriction is named. Examples, all verbatim from the primary sources -- "the model parameters are not identified without further assumptions" and "we lack global identification" ([Treier and Jackman](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=61fb0ba9b2e3c6b8619a4aa493fa55f26ff6c10c)); "a model without this restriction is not identified with respect to rotation" ([Fariss, p. 305 n. 27](http://cfariss.com/documents/Fariss2014APSR.pdf)); "we currently lack the necessary overlapping observations to completely identify the scale of the latent trait cross-nationally" and "we lack sufficient data to fully model DIF cross-nationally, weakening the cross-national comparability of the V-Dem measures" ([V-Dem measurement model](https://scispace.com/pdf/the-v-dem-measurement-model-latent-variable-analysis-for-1997yaxojn.pdf)); and, on untestable assumptions, "Although we cannot directly test this assumption" ([Pemstein, Meserve and Melton](https://www.cambridge.org/core/journals/political-analysis/article/democratic-compromise-a-latent-variable-analysis-of-ten-measures-of-regime-type/2A6B2BBA6F80367644F2C5007E1CFC29)).

This section reproduces, in paper form, the per-quantity identification statements already committed in `model/IDENTIFICATION.md`, including the four known degeneracies and the small-`n` problem. The small-`n` problem is not softened: the programme has on the order of five to eight historical analogues, which is fewer than the number of parameters that would need disciplining.

---

## 7. Prior-predictive checking, reported including its failures

**Superseded by the drafted section (2026-08-20).** The paragraphs below describe the state at outline time -- two gates failing, estimation blocked -- and are retained for the record. The gates now pass at run 004 after dated amendments selected on gate-independent grounds, and `S7-prior-predictive.md` reports the full failure-remedy-pass arc, which is the section's content.

Five prior-predictive gates were specified before estimation and run before any data entered the model. Two reject the committed priors. The failing configuration is committed rather than replaced, and estimation is blocked pending a dated amendment. Full disclosure is in `model/PRIOR-PREDICTIVE-RUN-001.md`.

This section also reports three implementation defects found while running the gates, one of which produced a quantitatively specific and entirely false diagnosis that would have justified widening a pre-registered prior in the direction that made a failing gate pass. The remedy adopted was a moment audit of the sampler against the priors file. The reason to publish this is that it is the failure mode a pre-registration regime is least protected against: the registered object was correct and the code implementing it was not.

---

## 8. What this paper cannot establish

- It cannot show the vector predicts anything better than a scalar index, because it makes no predictive comparison. Whether it should is section 9's question.
- It cannot rule out that the four elements are correlated tightly enough that aggregation would lose little. That is an empirical question about the estimated posterior, and it belongs to Paper B.
- It cannot verify that no author glimpsed the historical data before the 2026 baseline was registered. The objection is unanswerable in principle for the baseline year, and only the future-dated conditions escape it.
- It cannot claim pre-registration improved this project's accuracy, and on the available evidence should not.

## 9. Open questions the paper poses without answering

1. Should categorical falsification conditions be restated as probability forecasts under a strictly proper scoring rule, given that doing so now would alter pre-registered conditions after the fact?
2. Is there a non-compensatory aggregation that answers the practitioner's ranking question without smuggling in substitution rates? The Handbook's own constraint -- no indicator or dimension exceeding 50 per cent of total weight, on pain of becoming "a dictator in Arrow's terminology" ([OECD/JRC Handbook, p. 111](https://knowledge4policy.ec.europa.eu/sites/default/files/jrc47008_handbook_final.pdf)) -- suggests the answer is partial at best.
3. What is the correct naive benchmark for a fifty-year capability trajectory, given that the random-walk benchmark that defeated expert forecasters was defined over months?
4. Does the vector's refusal to rank make it unusable for the field that asked the question, and if so, is that a defect of the vector or of the question?

---

## Drafting order and status

| Section | Status |
|---|---|
| 1 Claims and non-claims | **Drafted** -- `S1-claims.md` (2026-08-20) |
| 2 Introduction | **Drafted** -- `S2-introduction.md` (2026-08-20) |
| 3 The capability vector | **Drafted** -- `S3-capability-vector.md` |
| 4 Measurement model | **Drafted** -- `S4-measurement-model.md` (2026-08-20) |
| 5 Pre-registration | **Drafted** -- `S5-pre-registration.md` (2026-08-20); adds 5.5, the falsifier calibration record from the dry-run programme |
| 6 Identification | **Drafted** -- `S6-identification.md` (2026-08-20) |
| 7 Prior-predictive checking | **Drafted** -- `S7-prior-predictive.md` (2026-08-20); supersedes this outline's section 7 text, which was written while the gates were failing -- the drafted section reports the full failure-remedy-pass arc through run 004 |
| 8 Cannot establish | **Drafted** -- `S8-cannot-establish.md` (2026-08-20) |
| 9 Open questions | **Drafted** -- `S9-open-questions.md` (2026-08-20) |

Section 3 was drafted first deliberately. It carries the paper's only genuinely contestable methodological claim, so drafting it first exposes the weakest point to criticism earliest rather than latest.

---

## Sources

- Correlates of War, National Material Capabilities -- https://correlatesofwar.org/data-sets/national-material-capabilities/
- Correlates of War, NMC v5 documentation -- https://correlatesofwar.org/wp-content/uploads/NMC_Documentation_v5_0.pdf
- Carroll and Kenkel, Capability Ratios Predict Nothing -- https://www.sas.rochester.edu/psc/polmeth/papers/Kenkel_Carroll.pdf
- Carroll and Kenkel, Prediction, Proxies, and Power, AJPS 63(3) -- https://onlinelibrary.wiley.com/doi/abs/10.1111/ajps.12442
- Lind, Back to Bipolarity, International Security 49(2) -- https://direct.mit.edu/isec/article/49/2/7/125214/Back-to-Bipolarity-How-China-s-Rise-Transformed
- Beckley, The Power of Nations, International Security 43(2) -- https://direct.mit.edu/isec/article-abstract/43/2/7/12211
- Beckley, The Power of Nations, full text -- https://scispace.com/pdf/the-power-of-nations-measuring-what-matters-441eqyutp6.pdf
- Carnegie Endowment, Methods of National Power Analysis -- https://carnegieendowment.org/research/2026/04/methods-of-national-power-analysis-pitfalls-and-best-practices
- Kugler and Organski, The Power Transition -- http://slantchev.ucsd.edu/courses/pdf/Kugler%20&%20Organski%20-%20The%20Power%20Transition.pdf
- Lowy Institute, Asia Power Index methodology -- https://power.lowyinstitute.org/methodology/
- Munda and Nardo, Constructing Consistent Composite Indicators, EUR 21834 EN -- https://publications.jrc.ec.europa.eu/repository/bitstream/JRC32434/EUR%2021834%20EN.pdf
- Nardo, Saisana, Saltelli and Tarantola, OECD/JRC Handbook on Constructing Composite Indicators -- https://knowledge4policy.ec.europa.eu/sites/default/files/jrc47008_handbook_final.pdf
- Treier and Jackman, Democracy as a Latent Variable -- https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=61fb0ba9b2e3c6b8619a4aa493fa55f26ff6c10c
- Pemstein, Meserve and Melton, Democratic Compromise, Political Analysis 18(4) -- https://www.cambridge.org/core/journals/political-analysis/article/democratic-compromise-a-latent-variable-analysis-of-ten-measures-of-regime-type/2A6B2BBA6F80367644F2C5007E1CFC29
- Fariss, Respect for Human Rights Has Improved Over Time, APSR 108(2) -- http://cfariss.com/documents/Fariss2014APSR.pdf
- Pemstein, Marquardt, Tzelgov, Wang and Miri, The V-Dem Measurement Model -- https://scispace.com/pdf/the-v-dem-measurement-model-latent-variable-analysis-for-1997yaxojn.pdf
- Hanson and Sigman, Leviathan's Latent Dimensions, documentation -- https://public.websites.umich.edu/~jkhanson/resources/StateCapac_v1_doc.pdf
- Nosek, Ebersole, DeHaven and Mellor, The preregistration revolution, PNAS 115(11) -- https://www.pnas.org/doi/10.1073/pnas.1708274114
- Olken, Promises and Perils of Pre-Analysis Plans, JEP 29(3) -- https://economics.mit.edu/sites/default/files/publications/JEP%20Analysis%20Plans%20Final.pdf
- Coffman and Niederle, Pre-Analysis Plans Have Limited Upside, JEP 29(3) -- https://web.stanford.edu/~niederle/Coffman.Niederle.PAP.JEP.pdf
- Monogan, Research Preregistration in Political Science, PS -- https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/research-preregistration-in-political-science-the-case-counterarguments-and-a-response-to-critiques/E80124ED16BA47D0EA09F03D72B89EC7
- Forecasting Collaborative, Insights into the accuracy of social scientists' forecasts of societal change, Nature Human Behaviour 7:484--501 -- https://pmc.ncbi.nlm.nih.gov/articles/PMC10192018/
- Gneiting and Raftery, Strictly Proper Scoring Rules, Prediction, and Estimation, JASA 102(477) -- https://sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jasa.pdf
- China Energy Portal, statistical reporting system for renewable energy -- https://chinaenergyportal.org/statistical-reporting-system-for-renewable-energy/
- EIA, Electric Power Monthly Table 6.7.A -- https://www.eia.gov/electricity/monthly/xls/table_6_07_a.xlsx
