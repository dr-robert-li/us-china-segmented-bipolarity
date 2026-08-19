# Identification and validation

What the model can and cannot learn from the available data, and what would establish that it is not merely fitting.

This file is written before estimation so that its admissions cannot be described as retrospective. It is the least flattering document in the repository, and that is its function.

---

## 1. The small-n problem, stated without softening

The model is fitted on great-power dyads. The number of comparable cases is approximately five to eight, depending on inclusion rules:

| Dyad | Period | Comparability |
|---|---|---|
| UK-Germany | 1890-1914 | High on industrial measures, low on institutional |
| UK-US | 1890-1945 | High, but the transition was non-conflictual |
| Germany-USSR | 1930-1945 | Compressed, war-dominated |
| US-USSR | 1945-1991 | Highest relevance, single case |
| US-Japan | 1975-1995 | Economic only, alliance-constrained |
| US-China | 1995-present | The case under study, cannot be used for validation |
| France-Germany | 1870-1914 | Marginal on scale |
| Netherlands-UK | 1650-1780 | Pre-industrial, arguably out of scope |

Six to eight cases, of which one is the case under study and at most four are usable for out-of-sample testing. Against that, the model in `SPECIFICATION.md` carries dozens of parameters.

The honest description of what follows is therefore **calibration, not validation**. The parameter posteriors are disciplined by priors from independent literatures and by within-case time-series variation, and the historical exercises test whether the structure produces sane behaviour on cases it did not see. They do not constitute out-of-sample validation in the sense that word carries in a large-n setting, and this file does not use the word that way.

### 1.1 There is no established method to appeal to here

A search of the literature did not locate political-science or international-relations work explicitly framing Bayesian calibration versus validation for small-n power-transition models with roughly five to eight cases. The extant empirical power-transition tradition is frequentist — logistic and probit regression on dyad-year panels — rather than Bayesian small-n. The closest methodological analogies come from general statistics rather than from this field ([A Generalized Bayesian Approach to Model Calibration](https://arxiv.org/abs/1911.11715)).

This is recorded as a gap rather than papered over with a citation that does not say what it would need to say. The practical consequence is that the validation protocol below is constructed rather than adopted, and being constructed, it is weaker evidence than an adopted standard would be. A reader is entitled to discount it on that basis.

### 1.2 The extant testing tradition, and what it found

The frequentist power-transition literature is worth stating because it establishes how sensitive results in this area are to measurement choices. Organski and Kugler's original tests found support for the theory ([Kugler and Organski retrospective](https://www.acsu.buffalo.edu/~fczagare/PSC%20346/Kugler%20and%20Organski.pdf)), but subsequent testing with alternative capability measures found that "the strength of the evidence depends importantly on how power is measured and the set of cases analyzed" ([de Soysa, Oneal and Park, *Journal of Conflict Resolution* 41(4), 1997](https://journals.sagepub.com/doi/10.1177/0022002797041004002)). Sixty years of hypothesis testing is surveyed in [DiCicco on power transition and revisionism](https://www.acsu.buffalo.edu/~fczagare/PSC%20504/DiCicco%20PT%20and%20Revisionism.pdf).

That finding — results turning on the capability measure and the case set — is the empirical justification for this project's two most basic commitments: capability as a vector rather than a scalar, and an explicit, published case set. Those choices are not stylistic preferences. They are responses to a documented failure mode in the closest existing literature.

---

## 2. What is identified

| Object | Identified | By what |
|---|---|---|
| Input trajectories `x[j,i,t]` for anchored series | Yes | Tier-1 and tier-2 series, multiple sources per quantity |
| `sigma_D`, `sigma_F` | Weakly | Within-case relative-price and quantity variation; priors do real work |
| `sigma_top[t]` level | Weakly | Cross-bundle substitution patterns; the weakest of the elasticities |
| `delta` | **Contingent** | Requires within-sample variation in AI-robotics intensity. That variation exists only after roughly 2015, giving about a decade of informative data |
| Nesting order | Yes, comparatively | Leave-one-decade-out predictive density; the comparison is identified even where levels are not |
| `psi[j,i]` | Weakly | Stress variation within case; see the 18%-of-variance problem in `POLITICAL-STRESS.md` |
| Element weights `w[m]` | Yes, under ordering constraints | The constraints are what make them identified |
| Source bias `b[k,i]` where an anchor exists | Yes | Multiple sources on one latent quantity |
| Source bias where no anchor exists | **No** | Fixed at prior mean, flagged `anchor_absent` |
| Saturation ceilings `xbar[j,i]` | **No, within horizon** | No case has saturated on the relevant inputs; priors carry this entirely |
| `R4` versus `R5` under simultaneous saturation | **No** | Structural degeneracy, section 5 |

### 2.1 The mechanism parameter has about a decade of data

This is the sharpest constraint in the project and it deserves to be stated in its own subsection. `delta` is identified only from variation in AI-robotics intensity, and meaningful variation in that quantity begins around 2015. Ten to eleven years of annual data, on two states, for a parameter governing a fifty-year projection.

The contraction gate in `PRIORS.md` section 2.1 exists because of this. The plausible outcome is not that `delta` is estimated precisely with the wrong sign; it is that `delta` is barely learned at all, and the gate forces that to be reported as "not learned" rather than as a directional finding with a wide interval. P2 then rests on F1 and F8, which is why the falsification architecture was built before the model.

---

## 3. Backtests

Four dyads, held out entirely from calibration. The model is fitted on the remaining cases plus the pre-2015 US-China period, and asked to produce regime posteriors for the held-out dyad at horizons matching its historical decision points.

| Dyad | Held-out horizons | Known outcome | Pass criterion |
|---|---|---|---|
| UK-Germany | 1900, 1910 | Industrial convergence, war, no transition of primacy | Must place non-trivial mass on convergence-without-succession |
| UK-US | 1900, 1930 | Successful transition, non-conflictual | Must not require conflict for transition |
| US-USSR | 1957, 1973, 1987 | No transition; Soviet collapse | See section 4 |
| US-Japan | 1985, 1990 | No transition; sustained stagnation | Must place substantial mass on a peaking regime |

Backtests are scored on **calibration of the posterior**, not on whether the modal regime matches history. A model that assigns 0.4 to the realised regime out of five regimes is performing well; one that assigns 0.95 is either extraordinary or overfitted, and given the case count, overfitting is the stronger prior.

### 3.1 The Japan test is the closest analogue and the most useful

US-Japan 1985-1990 is the best available analogue to the present case: a manufacturing and deployment-scale challenger with a frontier-innovation deficit, inside an alliance constraint, which converged sharply and then did not transition. A model that cannot place substantial posterior mass on the peaking regime for Japan in 1990 has no business producing a peaking-versus-segmentation posterior for China in 2040.

This is also the test most likely to fail, because the Japanese case turned on financial-system and demographic dynamics that the four-element capability vector captures only through `Y_fin` and the stress term.

---

## 4. The asymmetric pass criterion

The single most important test in this file, and the only one with an asymmetric bar.

**The model must not have forecast US decline in 1957, 1973, or 1987.**

Those three dates are the peaks of documented American declinist waves, each of which produced confident predictions of relative decline that did not occur on the predicted timeline:

- **1957.** The Sputnik launch on 4 October triggered a declinist panic that Soviet science and technology, and by extension Soviet national power, had overtaken the United States; this fed the missile-gap narrative, and the November 1957 National Intelligence Estimate later proved to have overstated the near-term Soviet ICBM buildout ([US Department of State, Office of the Historian](https://history.state.gov/milestones/1953-1960/sputnik)). The episode is conventionally read as the first of the modern declinist waves ([Histories of Decline](https://phenomenalworld.org/analysis/histories-of-decline/)).
- **1973.** The energy crisis and Vietnam-era retrenchment produced the second and third waves in Huntington's accounting ([The U.S. — Decline or Renewal?, *Foreign Affairs* 67(2)](https://contemporarythinkers.org/samuel-huntington/essay/the-u-s-decline-or-renewal/)).
- **1987.** Kennedy's *The Rise and Fall of the Great Powers* argued that imperial overstretch would produce relative US decline as productive power shifted toward Japan and the Pacific ([summary and citation trail](https://en.wikipedia.org/wiki/The_Rise_and_Fall_of_the_Great_Powers)). Huntington replied that declinism was a recurring five-decade phenomenon repeatedly proven wrong, writing that "in 1988 the United States reached the zenith of its fifth wave of declinism since the 1950s" ([*Foreign Affairs*](https://contemporarythinkers.org/samuel-huntington/essay/the-u-s-decline-or-renewal/)). Nye argued the United States retained sufficient hard and soft power and that decline was a question of political will rather than capability ([*Bound to Lead*, 1990](https://www.kropfpolisci.com/exceptionalism.nye.pdf)). Nau argued Kennedy's predictions "have not fared well" except regarding Russia, because a realist model ignoring national identity and domestic institutions could not capture the relevant dynamics ([Why 'The Rise and Fall of the Great Powers' was wrong](https://library.fes.de/libalt/journals/swetsfulltext/12119495.pdf)). The Kennedy-Nye exchange is available directly ([Is the US Declining?, *NYRB*, 11 October 1990](https://www.nybooks.com/articles/1990/10/11/is-the-us-declining/); [Fin-de-Siècle America, *NYRB*, 28 June 1990](https://www.nybooks.com/articles/1990/06/28/fin-de-siecle-america/)). A thirty-five-year retrospective notes the book's continued relevance while observing that it failed to foresee the USSR's collapse four years after publication ([LSE US Centre](https://blogs.lse.ac.uk/usappblog/2023/12/04/long-read-for-over-30-years-paul-kennedys-the-rise-and-fall-of-the-great-powers-has-been-the-backdrop-of-the-shifting-debate-over-american-power/)).

### 4.1 Why the bar is asymmetric

A model built in 2026 to analyse US-China divergence, by an author who has read the declinist literature, faces a specific and severe risk: that its structure encodes the reasoning of the 1987 declinists and would therefore have reproduced their error given 1987 data. If so, its 2050 output is a restatement of a repeatedly falsified argument in contemporary notation.

The test is asymmetric because the failure mode is asymmetric. There is no comparable history of confident predictions of US ascendancy that failed, so no symmetric test exists to construct. Applying a symmetric bar would mean applying no bar at all in the direction where the risk lies.

**Pass criterion.** At 1957, 1973 and 1987, run on data available at those dates, the model must place **less than 0.35** posterior mass on the US-unfavourable divergence regime `R2`-analogue at a twenty-year horizon. Above 0.35 at any of the three dates, the specification is rejected and the rejection is committed with the failing configuration.

Threshold frozen from this commit. It may not be raised after a run.

### 4.2 The obvious objection, and the answer

The objection: this hard-codes an anti-declinist prior, which is itself a substantive commitment about the world, and one that could be wrong precisely now.

The answer is that the test is applied to the model's behaviour **on historical data**, not to its output on current data. A specification that correctly reads 1957, 1973 and 1987 as non-transitions and nonetheless reads 2026-2050 as divergence is permitted and would be a strong result. What is excluded is a specification that reads every period of American anxiety as decline. The test disciplines structure, not conclusions.

The prohibition also runs in both directions per the first standing prohibition. If a comparable series of documented, confident, falsified predictions of PRC collapse can be assembled — and the literature on predicted Chinese economic crises is not thin — an equivalent test on that side is added by amendment. That is recorded here as an open commitment rather than claimed as already done.

---

## 5. Known degeneracies

Characterised rather than resolved. Each is checkable in the prior predictive.

### 5.1 `R4` versus `R5` under simultaneous saturation

When both bundles approach their saturation ceilings in both states, segmented bipolarity and dual systemic constraint produce nearly identical observable trajectories. The distinction is about whether capability is divided by domain or suppressed in both domains, and at the saturation boundary the data cannot separate them.

Committed treatment: where the posterior mass on `R4 ∪ R5` exceeds 0.5 and neither individually exceeds 0.3, the output reports the union and states that the two are not separated. It does not report whichever is marginally higher.

### 5.2 Bias and level under a missing anchor

Section 2. Handled by fixing `b` and flagging.

### 5.3 Saturation ceiling against growth persistence

A low ceiling with high persistence and a high ceiling with low persistence produce similar medium-horizon trajectories and divergent long-horizon ones. This is the primary reason the 2075 intervals are wide, and it is why sensitivity run S6 in `PRIORS.md` is mandatory.

### 5.4 The elasticity level against the nesting order

The 2019 German replication finding elasticities from near-Leontief to effectively unbounded depending on nesting structure ([Henningsen, Henningsen and van der Werf](https://backend.orbit.dtu.dk/ws/files/149724340/melju_1_s2.0_S0140988317304395_main.pdf)) is a direct warning about this pair. Nesting order and elasticity level trade off against each other. The model therefore reports the elasticity posterior **conditional on each nesting structure separately**, and does not marginalise over structures to produce a single headline elasticity.

---

## 6. Prior predictive checks, run before any data touches the model

Five checks. Failure of any one blocks estimation.

| # | Check | Failure condition |
|---|---|---|
| PP1 | Regime coverage | Any of `R1..R5` receives prior mass below 0.05 |
| PP2 | `R4` refutability | `R4` cannot receive mass below 0.2 for any admissible data — the check demanded in `SPECIFICATION.md` section 1 |
| PP3 | Trajectory sanity | Prior predictive generation-capacity paths exceed physical plausibility at 2050 |
| PP4 | Symmetry | Swapping the two states' data produces mirror-image regime posteriors. Asymmetry here means asymmetry was built in |
| PP5 | Declinism | The prior predictive assigns above 0.5 mass to any divergence regime absent informative data |

PP4 is the mechanical implementation of the first standing prohibition. It is a test that can actually fail, unlike a stated commitment to even-handedness.

---

## 7. What would falsify the model rather than the thesis

Distinguished because conflating them is how frameworks survive their own failures.

| Finding | Implication |
|---|---|
| Backtest posteriors uncalibrated across all four dyads | The model is wrong. The thesis is untested, not supported |
| Asymmetric criterion failed at any of 1957, 1973, 1987 | The specification is rejected. Commit the failing configuration |
| PP4 fails | Asymmetry is structural. Rebuild, do not adjust |
| `delta` contraction below 0.10 | The mechanism claim is not learnable from these data. P2 rests on F1 and F8 |
| Nesting comparison inconclusive by predictive density | The central empirical object is not resolvable at this data resolution. Report as such |
| Divergent transitions that will not clear on reparameterisation | Report the failure and the abandoned configurations |

The distinction matters most in the fourth row. A model that cannot learn `delta` is not evidence against P2 and not evidence for it. Reporting a wide posterior as "suggestive" would be the single most likely way this project ends up asserting more than it established.

---

## Sources

- Tohme, Vanslette and Youcef-Toumi, A Generalized Bayesian Approach to Model Calibration — https://arxiv.org/abs/1911.11715
- Kugler and Organski, power transition retrospective — https://www.acsu.buffalo.edu/~fczagare/PSC%20346/Kugler%20and%20Organski.pdf
- de Soysa, Oneal and Park, Testing Power-Transition Theory Using Alternative Measures of National Capabilities, *JCR* 41(4), 1997 — https://journals.sagepub.com/doi/10.1177/0022002797041004002
- DiCicco, Power Transition Theory and the Essence of Revisionism — https://www.acsu.buffalo.edu/~fczagare/PSC%20504/DiCicco%20PT%20and%20Revisionism.pdf
- US Department of State, Office of the Historian, Sputnik, 1957 — https://history.state.gov/milestones/1953-1960/sputnik
- Histories of Decline — https://phenomenalworld.org/analysis/histories-of-decline/
- Huntington, The U.S. — Decline or Renewal?, *Foreign Affairs* 67(2), Winter 1988/89 — https://contemporarythinkers.org/samuel-huntington/essay/the-u-s-decline-or-renewal/
- Kennedy, *The Rise and Fall of the Great Powers* (Random House, 1987) — https://en.wikipedia.org/wiki/The_Rise_and_Fall_of_the_Great_Powers
- Nye, *Bound to Lead* (Basic Books, 1990) — https://www.kropfpolisci.com/exceptionalism.nye.pdf
- Nau, Why 'The Rise and Fall of the Great Powers' was wrong — https://library.fes.de/libalt/journals/swetsfulltext/12119495.pdf
- Kennedy and Nye, Is the US Declining?, *NYRB*, 11 October 1990 — https://www.nybooks.com/articles/1990/10/11/is-the-us-declining/
- Kennedy, Fin-de-Siècle America, *NYRB*, 28 June 1990 — https://www.nybooks.com/articles/1990/06/28/fin-de-siecle-america/
- Cox, thirty-five-year retrospective on Kennedy, LSE US Centre — https://blogs.lse.ac.uk/usappblog/2023/12/04/long-read-for-over-30-years-paul-kennedys-the-rise-and-fall-of-the-great-powers-has-been-the-backdrop-of-the-shifting-debate-over-american-power/
- Henningsen, Henningsen and van der Werf, *Energy Economics* 82, 2019 — https://backend.orbit.dtu.dk/ws/files/149724340/melju_1_s2.0_S0140988317304395_main.pdf

---

## Amendment 1 -- 2026-08-20 -- PP1 checks coverage at the earliest claimed horizon

**Appended, not substituted.** Induced by `SPECIFICATION.md` Amendment 02, which restricts the output contract to report R5 at 2075 only. Selected by author decision of 2026-08-20 in structured Q&A.

### The change

PP1's failure condition, "any of `R1..R5` receives prior mass below 0.05", is restated: **each regime must receive prior mass of at least 0.05 at the earliest horizon at which the output contract claims it** -- `R1..R4` at 2050, `R5` at 2075. The `R0_no_material_change` bucket remains exempt and remains reported.

### Why this is not the horizon-conditional remedy rejected as contaminated

Candidate 1 in `PRIOR-PREDICTIVE-RUN-001.md` section 3.1 moved the gate's horizon while leaving the claim in place -- choosing the evaluation horizon while looking at which choice passes, as that file's own open note warned. Here the *claim* moved first, on the stated ground that the design cannot populate R5 at 2050, and the gate follows the claim because a gate testing a claim not made protects nothing. The distinction is procedural and it is the whole content of the selection: contract first, gate second.

The open weakness recorded in `PRIOR-PREDICTIVE-RUN-001.md` -- that the specification never said why PP1 evaluated at 2050 -- is closed by this restatement: the gate horizon per regime is now derived from the output contract rather than chosen freely.

### Sources for Amendment 1

- model/SPECIFICATION.md, Amendment 02 (internal)
- model/PRIOR-PREDICTIVE-RUN-001.md, section 3.1 and section 4 (internal)
