# Paper A, section 5 -- Pre-registration for a long-horizon observational claim

**Status.** Draft, 2026-08-20. The section's claim is auditability, not accuracy, and subsection 5.6 contains the strongest available evidence against the enterprise the programme is engaged in -- placed here, in the methods section, rather than in a closing limitations paragraph.

---

## 5.1 The purpose, taken from the source that states it most carefully

"Preregistration distinguishes analyses and outcomes that result from predictions from those that result from postdictions", and -- decisively for this paper's framing -- "Preregistration does not favor prediction over postdiction; its purpose is to make clear which is which" ([Nosek, Ebersole, DeHaven and Mellor, *PNAS*](https://www.pnas.org/doi/10.1073/pnas.1708274114)). The same authors state that preregistration "does not eliminate the possibility of poor statistical practices, but it does make them detectable", and concede that "there is not yet sufficient experimental evidence establishing its superiority for reproducibility."

Everything this programme claims for its pre-registration is contained in those sentences. The falsification conditions were fixed, with thresholds, deadlines, sources and adjudication rules, before their outcomes exist. Whatever the conditions eventually return, a reader can verify from the commit history which statements were predictions. Nothing about that makes the predictions good.

## 5.2 The objections, at full strength

Three of these apply to this project specifically, and saying so is the point of the table.

| Objection | Source | Does it bite here? |
|---|---|---|
| Full pre-specification is infeasible -- a ten-table analysis tree implies 3^10 = 59,049 possible regressions, and plans have exceeded 50 pages | [Olken, *JEP* 29(3)](https://economics.mit.edu/sites/default/files/publications/JEP%20Analysis%20Plans%20Final.pdf) | Yes. Met only partially, by pre-registering falsification conditions and thresholds rather than a full analysis tree -- a weaker commitment, described as such |
| Pre-specification "prevents you from learning about your data as you analyze it" | [Olken](https://economics.mit.edu/sites/default/files/publications/JEP%20Analysis%20Plans%20Final.pdf) | Yes, and unresolved. Recorded as a cost accepted, not a cost denied |
| Pre-analysis plans "have quite limited upside" in most settings and "may discourage the use of novel research designs"; value concentrates in "costly, one-of-a-kind" studies | [Coffman and Niederle, *JEP* 29(3)](https://web.stanford.edu/~niederle/Coffman.Niederle.PAP.JEP.pdf) | Partly. A fifty-year single-run forecast is close to their one-of-a-kind category -- the only place they concede real value |
| With historical data "a scholar may have glimpsed the data before the study registration", so registration "cannot send as clear a signal" | Anderson (2013), quoted in [Monogan, *PS*](https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/research-preregistration-in-political-science-the-case-counterarguments-and-a-response-to-critiques/E80124ED16BA47D0EA09F03D72B89EC7) | Yes for the 2026 baseline, which uses published historical data. No for the 2030--2050 conditions, whose outcomes do not yet exist |
| Preregistration risks "robotic data analysis" at the expense of broader exploration | Gelman (2013), via [Monogan](https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/research-preregistration-in-political-science-the-case-counterarguments-and-a-response-to-critiques/E80124ED16BA47D0EA09F03D72B89EC7) | Partly. Answered by Monogan's own remedy: auxiliary findings are reported "as observations from data -- rather than hypothesis tests" |
| "Many of the most important developments in knowledge came from inductive findings", and non-registered work may come to be seen as inferior | Laitin (2013), via [Monogan](https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/research-preregistration-in-political-science-the-case-counterarguments-and-a-response-to-critiques/E80124ED16BA47D0EA09F03D72B89EC7) | Not against this paper, but the paper must not be read as prescribing the practice generally, and says so here |

## 5.3 The pivot

Monogan classes studies using "existing information" or "time series of economic data" as low-value candidates for registration, and studies where researchers "plan to study an upcoming election" as high-value ([Monogan](https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/research-preregistration-in-political-science-the-case-counterarguments-and-a-response-to-critiques/E80124ED16BA47D0EA09F03D72B89EC7)). A long-horizon forecast is in the second class on his own criterion: the glimpsing objection cannot apply to a value that does not exist yet. That is the whole argument for pre-registering this project, and it is one sentence long.

## 5.4 The operational template

The Forecasting Collaborative pre-registered forecasts with rationales on the Open Science Framework and, separately and earlier, lodged "an a priori specific document shared with the journal in April 2020" fixing the dependent variable, the benchmarks and the analytic procedure ([*Nature Human Behaviour* 7:484--501](https://pmc.ncbi.nlm.nih.gov/articles/PMC10192018/)). Fixing the evaluation rule before the forecast, in a separate document, is the part this project copies: adjudication rules, source commitments, and anchoring live in files whose diff history precedes the outcomes they will judge.

## 5.5 Calibration of the falsification set, tested before its outcomes exist

A registered condition is worth only as much as its counting rules, and counting rules can fail in both directions -- returning the committed verdict on cases where the answer is known and opposite. Before any live outcome existed to contaminate them, the eight registered conditions were put through calibration exercises against the historical record. **The exercises were not uniform in design, and their evidentiary weight is not uniform either**; the table separates them, because collapsing distinct evidentiary categories into one calibration story would overstate the record.

| Condition | Exercise type | Sequence disclosure | Outcome | Load-bearing flag |
|---|---|---|---|---|
| F1 | Paired discrimination test | Pair and expected outcomes declared before any series fetched; one follow-on comparison post hoc, labelled | **Passed** (expected-positive triggers, control does not, robust across constructions and numerator source) | Source-tolerance rule lacked a committed comparison basis; blocks automatic verdicts, fix registered |
| F2 | Characterisation exercise | Reconnaissance preceded registration, disclosed | Characterised, not tested: threshold at the bottom of a 64-year outturn range -- never left in-record | Evaluation-anchoring gap is verdict-determining; published shadow disagrees with binding verdict |
| F3 (Clause 2) | Paired discrimination test | **Blind-registered pair** -- the set's only one (pair fixed before any evidence gathered) | **Passed**, generically: the cascade rubric discriminates on the analogue pair; nothing PRC-specific tested | Seniority-criterion watch item |
| F4 | Could not be exercised | Reconnaissance preceded registration, disclosed | Untestable: the committed majority rule counts a cell no publication provides, including its own baseline study | `verdict_input_shape_unpublished` |
| F5-B | Paired discrimination test | Pair from the pre-registered design | **Failed**: same verdict on the archetypal positive case and the negative control | Demonstrated false-negative mode, flagged on every future F5 verdict |
| F6 | Could not be exercised | Reconnaissance preceded registration, disclosed | Untestable: threshold sits 7.8pp below the series' 36-year minimum -- never reached in-record | `threshold_outside_observed_range` |
| F7 | Not exercised at all | -- | Excluded: the committed series does not exist continuously; weakened-falsifier status accepted by dated amendment | No series |
| F8 | Characterisation exercise with demonstrated discrimination | Reconnaissance preceded registration, disclosed | The only measurand that visits both sides of its threshold in-record; classifies both sides correctly, wide margins | Spread between admissible constructions exceeds the live distance to threshold; near-threshold verdicts construction-determined |

Read as evidence, the table divides sharply: **three paired discrimination tests** (F1 passed, F3 passed generically on the one blind-registered pair, F5-B failed), **two characterisation exercises** (F2, F8 -- informative about the measurands, but reconnaissance preceded registration, so they are the weaker evidence class and are labelled as such), **two conditions that could not be exercised** because threshold or input shape sits outside anything the record supplies (F4, F6), and **one condition not exercised at all** (F7). The two untestable thresholds miss their measurands' observed ranges in opposite directions -- one never reached in 36 years, one never left in 64 -- making those conditions close to unfalsifiable in practice, in directions now individually quantified.

The set's effective size and independence are therefore materially below its nominal eight, and every verdict the programme eventually publishes carries that calibration record with it. The per-condition exercise files, their pre-named failure conditions, and the sequence disclosures above are committed in the falsifier log.

Two things follow. A reader who trusts none of the programme's substantive claims can still use the calibration record to weight the eventual verdicts clause by clause. And the exercise demonstrated its own value in the only way that counts: it found an unanticipated blocking defect in a rule written for auditability (F1's source-tolerance rule lacked a committed comparison basis and, as written, blocked automatic verdicts for the live evaluation window), on the second condition examined.

## 5.6 Scoring, and the hardest fact in the paper

Verdicts are categorical threshold crossings, not probability quotes, so no strictly proper scoring rule is currently applied. That is a deficiency and is named as one. Where probabilities are reported, propriety is the relevant property: a rule is strictly proper when the expected-score inequality "holds with equality if and only if P = Q, thereby encouraging honest quotes by the forecaster" ([Gneiting and Raftery, *JASA* 102(477)](https://sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jasa.pdf)). Whether the falsification conditions should be restated as probability forecasts is section 9's first open question, because restating them now would change pre-registered conditions after the fact.

The hardest fact: the Forecasting Collaborative found that "social scientists' forecasts were on average no more accurate than those of simple statistical models ... or the aggregate forecasts of a sample from the general public", beating all three naive benchmarks in 1 of 12 domains; at least one naive method matched or beat the experts in 11 of 12 domains in the first tournament and 8 of 12 in the second; winning teams remained worse than in-sample random walks in 8 of 12 domains; and "Experts' subjective confidence in their forecasts was not related to the accuracy of their estimates" ([*Nature Human Behaviour*](https://pmc.ncbi.nlm.nih.gov/articles/PMC10192018/)).

This is evidence against the enterprise this programme is engaged in. Two consequences are adopted rather than argued away: a naive benchmark is mandatory for every reported trajectory, and confidence statements are never offered as evidence of reliability. A third consequence is refused, with the reason stated: abandoning the forecast is not adopted, because the programme's output is not a point forecast but a falsification apparatus, and 5.1's auditability claim survives the accuracy evidence untouched.
