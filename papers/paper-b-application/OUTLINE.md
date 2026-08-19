# Paper B -- Application

**Working title.** Segmented Bipolarity as a Parameter Region: Estimating Whether the AI-Robotics Transition Changes the Production Function of Geopolitical Capability

**Status.** Outline only. **No section of this paper may be drafted beyond outline while estimation is blocked.** Two of five prior-predictive gates reject the committed priors, so there is no posterior, and a draft written now would be a draft of the conclusion rather than of the analysis. The blocking condition is recorded in `model/PRIOR-PREDICTIVE-RUN-001.md` and the release condition is in section 9 below.

**Relationship to Paper A.** Paper A defends the measurement architecture and can stand if this paper's substantive answer is wrong. Paper B is the only place a substantive claim about the United States and the PRC is made. The separation is deliberate: it prevents the measurement contribution from being hostage to the empirical one, and it makes the empirical one easier to reject cleanly.

---

## 1. The question, and the three propositions it decomposes into

The programme interrogates a conditional hypothesis, not a forecast. Conditional on a specified set of parameter ranges holding to roughly 2050, does relative position diverge in the PRC's favour on selected physical-capacity dimensions while diverging in the United States' favour on others, and are the dimensions on which the PRC is gaining precisely those the AI-robotics transition disproportionately rewards.

| ID | Proposition | Scored by |
|---|---|---|
| P1 | Relative position diverges in the PRC's favour on generation, transmission and robotics deployment | Posterior mass on `R1`, and on the early phase of `R3` |
| P2 | Those are the dimensions the AI-robotics transition disproportionately rewards | The sign of the complementarity parameter `delta` |
| P3 | Capability divides by domain rather than resolving into a single hierarchy | Posterior mass on `R4` |

The three are scored separately because the eight pre-registered falsification conditions do not bear on them equally, and because the interesting failure mode of this project is P1 falling while P3 survives.

**The net direction of overall divergence is indeterminate a priori** and is not what the paper argues for. The paper's expected result, segmented bipolarity, is horizon-robust in a way no directional claim is, which is a reason to trust it less as a discriminating prediction rather than more: a result that survives many parameterisations is also a result that few parameterisations could have refuted.

---

## 2. The output object

Six labels, five substantive plus a residual, with posterior mass reported per horizon.

| Label | Content |
|---|---|
| `R1` | PRC-favourable divergence across the capability vector |
| `R2` | US-favourable divergence across the capability vector |
| `R3` | Challenger peaking -- early gain followed by structural reversal |
| `R4` | Segmented bipolarity -- divergence by domain, no single hierarchy |
| `R5` | Dual systemic constraint -- both states below their own unconstrained trajectories |
| `R0` | No material change beyond the deadband either way |

Three features of the classifier belong in the paper rather than in an appendix, because each was chosen against the thesis.

- **The priority order is frozen at `R5, R3, R4, R1/R2, R0`.** `R4` is the expected result and it is adjudicated *after* the two regimes that could otherwise absorb trajectories belonging to them. The reverse order would inflate the thesis regime.
- **`R3` is defined generically as challenger peaking, not as PRC peaking.** The specification names it "PRC peaking"; the implemented rule generalises it so that the state-swap symmetry test is well posed, and the divergence is registered rather than silently harmonised.
- **`R0` exists because the five regimes are not an exhaustive partition.** It carried 0.385 prior mass at 2030 in the canonical prior-predictive run, which is a substantive finding in its own right and belongs in the paper: on a 2030 horizon, claims about relative position are to a large extent claims about measurement noise.

---

## 3. The central empirical object -- complementarity, not levels

The paper's mechanism claim reduces to the sign of one parameter. Whether the frontier bundle -- frontier-capable compute, capital depth, human capital -- and the deployment bundle -- dispatchable-adjusted electrical energy, grid transmission capacity, deployed industrial robotics -- are complements, substitutes, or alternating bottlenecks in a two-level nested production structure.

Three commitments constrain the section before any estimate exists.

1. The nesting order is determined by the data, not assumed. The elasticity level against the nesting order is a known degeneracy and is reported as one.
2. The substitution elasticity is a time-varying state, not a constant, over a fifty-year horizon.
3. `delta` is centred at zero in the priors. P2 is therefore not built into the model; it is a sign test the model can fail.

**The steel-man belongs here, not in a later limitations section.** If `delta` is indistinguishable from zero, the correct reading is not that the mechanism is weak but that this design cannot see it. The programme has on the order of five to eight usable historical analogues against a multi-parameter mechanism, which is fewer observations than parameters requiring discipline. That is stated in `model/IDENTIFICATION.md` and must be restated in the paper at the point the sign test is reported, not after it.

---

## 4. The rival reading, nested

The peaking-power thesis is represented as `R3`, a reachable region of the parameter space with prior mass, not as an opposing position to be defeated.

The paper engages it at its strongest. Its case-selection rule is explicit and checkable -- "every case from 1870 to 2018 in which a great power's per capita gross domestic product (GDP) grew at least twice as fast as the global average for at least seven years and then suffered at least a 50 percent decline in growth rates over the next seven years", leaving nine cases, of which three are set aside as overdetermined ([Beckley, *International Security* 48(1)](https://direct.mit.edu/isec/article/48/1/7/117122/The-Peril-of-Peaking-Powers-Economic-Slowdowns-and)). Its mechanism is specific: "The most dangerous trajectory in world politics is a long rise followed by the prospect of a sharp decline", with mercantilist expansion as the behavioural channel and regime type and trade prospects as the conditioning variables ([Brands and Beckley, *Foreign Policy*](https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf)).

Two things follow, and the second is uncomfortable.

First, the indicators marshalled for the peaking reading are real and adverse: total factor productivity "declined 1.3 percent every year on average between 2008 and 2019"; total debt "surged eight-fold between 2008 and 2019 and exceeded 300 percent of GDP"; and from 2020 to 2050 the PRC "will lose an astounding 200 million working-age adults ... and gain 200 million senior citizens", with health and pension spending required to "triple as a share of GDP, from 10 percent to 30 percent, by 2050" ([Brands and Beckley](https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf)). None of this is disputed by this programme. The disagreement is about whether those series and the physical-capacity series can be reconciled into a single directional verdict, and the answer offered is that they cannot.

Second, the load-bearing evidence base for the peaking mechanism is roughly five to six cases -- **the same order as this programme's own analogue count**. The paper does not get to cite small-`n` against the rival and stay silent about its own. Both claims rest on too few observations, and the paper says so in the same paragraph.

The rival literature's own internal critics are cited where they help, not only where they help this paper. Medeiros asks "Is it an absolute term or a relative one -- and if the latter, relative to what?" and notes that "China could peak in one area but advance in others" ([*Foreign Affairs*](https://www.foreignaffairs.com/china/delusion-peak-china-united-states-evan-medeiros)) -- which supports the vector. Hass demands evidence "that China's leaders accept the diagnosis of their current condition", of which "no such evidence is available" ([prcleader.org](https://www.prcleader.org/post/organizing-american-policy-around-peak-china-is-a-bad-bet)) -- which cuts against `R3` having a behavioural mechanism at all, and therefore against treating `R3` mass as evidence about conduct. Lind argues that "regardless of slowing growth, and regardless of whether it overtakes the United States, China is already capable of engaging in a serious security competition" and that "'catching up' or 'overtaking' are the wrong benchmarks" ([*International Security* 49(2)](https://direct.mit.edu/isec/article/49/2/7/125214/Back-to-Bipolarity-How-China-s-Rise-Transformed)) -- which is an objection to the whole trajectory framing, including this programme's, and is engaged as such.

**The methodological contrast that the paper draws, and its limit.** The Thucydides Trap case file claims immunity from selection bias on universe-of-cases grounds -- "Because this includes the entire universe of the cases (as opposed to a representative sample), the Case File is immune to charges of selection bias" -- while simultaneously stating that the file "is open" and inviting further cases ([Belfer Center](https://www.belfercenter.org/programs/thucydidess-trap/thucydidess-trap-case-file)), and provides no operational definition of a rising or ruling power. Hanania's critique establishes that the failure is in the coding rules, not in the sample size: "Nearly every substantive word in these sentences is ill-defined", "The selection process seems to be completely anecdotal", "Allison provides no details about which measures he used, if any", and the war rate moves from 12 of 16 to 19 of 30 with the cases under consideration and to 1 of 8 for the post-1950 period ([*Strategic Studies Quarterly* 15(4)](https://www.airuniversity.af.edu/Portals/10/SSQ/documents/Volume-15_Issue-4/SC-Hanania.pdf)). He also concedes that "a study with 16 observations can be valuable if it is well designed". The limit of the contrast is that pre-registered coding rules make a project auditable, not correct, and this paper claims only the first.

---

## 5. Falsification conditions, and the 2026 baseline as the paper's spine

Eight conditions, with thresholds committed before any estimation code existed and a commit history that establishes the ordering. The baseline verdicts are the paper's most durable asset because they were recorded in a state of ignorance.

| ID | 2026 verdict | Distance to threshold |
|---|---|---|
| F1 | `not_triggered` | ~30pp, moving away |
| F2 | `not_triggered` | ~0.1pp |
| F3 | `not_triggered` | ~38.5pp on outturn, revised vintage |
| F4 | `indeterminate` | Named source does not exist |
| F5 | `not_triggered` (provisional) | Not adjudicated |
| F6 | `not_triggered` | ~12pp, moving away |
| F7 | `indeterminate` | Series unavailable in continuous published form |
| F8 | `indeterminate` | ~1.1pp below |

The paper must report the uncomfortable structure of this table rather than the reassuring summary. Two conditions sit within about a percentage point of their thresholds and those same two are the least directly measured. Three cannot presently return their strongest verdict at all. **The set is not well calibrated**, more of the architecture's weight rests on definitional choices than the threshold table suggests, and none of that may be repaired retrospectively.

Trigger rules are dependence-aware rather than a simple count, with three rejection gates and a positive-semi-definiteness requirement on the prior correlation matrix. What may not be done is enumerated in the pre-registration: thresholds may not move as they approach, sources may not be substituted for more favourable ones, deadlines may not be extended, and no condition may be reclassified to avoid a verdict.

---

## 6. Backtests and the asymmetric pass criterion

The closest analogue is Japan from 1970, which appears in the peaking literature's own nine-case set. The paper reports the backtest against a criterion that is deliberately harder to pass in the thesis-favourable direction than against it, with the justification for the asymmetry given at the point the result is reported and the obvious objection to it answered there rather than in an appendix.

A naive benchmark is mandatory for every reported trajectory. The reason is external and specific: in the largest published forecasting tournament in social science, "social scientists' forecasts were on average no more accurate than those of simple statistical models ... or the aggregate forecasts of a sample from the general public", experts beat all three naive benchmarks in 1 of 12 domains, and "Experts' subjective confidence in their forecasts was not related to the accuracy of their estimates" ([*Nature Human Behaviour* 7:484--501](https://pmc.ncbi.nlm.nih.gov/articles/PMC10192018/)). A fifty-year capability model that cannot beat a random walk should be reported as not beating a random walk. What the correct naive benchmark is at a fifty-year horizon, when the tournament's was defined over months, is an open question carried from Paper A.

---

## 7. What the paper will report, in fixed form

Committed here so that the reporting format cannot be selected after the posterior is seen.

1. Posterior mass on each of `R0` through `R5`, at 2030, 2040, 2050 and 2075, with 2075 labelled low-confidence in every output containing it.
2. The posterior for `delta`, with the sign test for P2 stated as a probability, not as a verdict.
3. Per-element decomposition of relative movement. No scalar composite without full weighting sensitivity alongside.
4. Prior-versus-posterior contraction diagnostics per parameter, to show the posterior learns from data rather than reproducing the prior.
5. All ten pre-registered sensitivity runs, reported whether or not they change the conclusion.
6. Every falsification condition's current verdict, including the indeterminate ones and the reason each is indeterminate.
7. The naive benchmark comparison for every trajectory.

---

## 8. What this paper cannot establish

- It cannot deliver a defensible 2075 point estimate. The 2075 outputs exist to show how fast the intervals widen, which is an argument for humility rather than a forecast.
- It cannot distinguish `R4` from `R5` where both bundles saturate simultaneously. The degeneracy is characterised, not resolved.
- It cannot resolve the counterfactual of policy response. The reflexivity term absorbs feedback in reduced form and does not model decisions.
- It has no mechanism for military conflict, and will not be read as pricing war outcomes.
- It cannot establish that the mechanism exists if `delta` is indistinguishable from zero, because with five to eight analogues a null is uninformative rather than negative.
- It cannot claim its pre-registration made it more accurate. On the available evidence, no such claim is supportable.

---

## 9. Release condition

Drafting begins when, and only when, all five prior-predictive gates pass under a prior configuration recorded in a dated amendment whose justification is independent of gate outcomes. The two currently failing gates are PP1, regime coverage, with `R5` at 0.025 mass against a 0.05 floor at the 2050 horizon, and PP3, trajectory sanity, with a maximum 2050 input multiple of 892.7 against a pre-registered ceiling of 20 and 5.8 per cent of draws breaching.

Three candidate remedies exist for each and none has been selected. The remedy that would pass each gate most cheaply is named as such in the disclosure document, precisely so that choosing it later is visible.

---

## Sources

- Beckley, The Peril of Peaking Powers, International Security 48(1) -- https://direct.mit.edu/isec/article/48/1/7/117122/The-Peril-of-Peaking-Powers-Economic-Slowdowns-and
- Brands and Beckley, China Is a Declining Power, Foreign Policy, 24 September 2021 -- https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf
- Medeiros, The Delusion of Peak China, Foreign Affairs -- https://www.foreignaffairs.com/china/delusion-peak-china-united-states-evan-medeiros
- Hass, Organizing American Policy Around Peak China is a Bad Bet -- https://www.prcleader.org/post/organizing-american-policy-around-peak-china-is-a-bad-bet
- Lind, Back to Bipolarity, International Security 49(2) -- https://direct.mit.edu/isec/article/49/2/7/125214/Back-to-Bipolarity-How-China-s-Rise-Transformed
- Belfer Center, Thucydides's Trap case file -- https://www.belfercenter.org/programs/thucydidess-trap/thucydidess-trap-case-file
- Hanania, Graham Allison and the Thucydides Trap Myth, Strategic Studies Quarterly 15(4) -- https://www.airuniversity.af.edu/Portals/10/SSQ/documents/Volume-15_Issue-4/SC-Hanania.pdf
- Forecasting Collaborative, Insights into the accuracy of social scientists' forecasts of societal change, Nature Human Behaviour 7:484--501 -- https://pmc.ncbi.nlm.nih.gov/articles/PMC10192018/
