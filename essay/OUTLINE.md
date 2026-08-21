# Essay -- Consolidated long-form outline

**Working title.** Two Ledgers: Why the Argument About China's Trajectory Cannot Be Settled by Adding Up

**Audience.** Expert peer circulation. Readers who know the peaking-power debate, the composite-indicator literature, or the measurement-model literature, but generally not all three. No policy recommendations. No investment framing. The essay's job is to make a methodological disagreement legible to people who hold substantive positions in it.

**Length target.** 6,000--9,000 words.

**Relationship to the papers.** The essay is not a summary of Papers A and B. It carries one argument the papers cannot: that the disagreement about China's trajectory is substantially a disagreement about measurement conventions, and that the participants mostly do not describe it that way. Where the papers must qualify, the essay may argue -- but it may not assert anything the papers do not support.

---

## Movement 1 -- Two ledgers, both real

Open with the collision, not with a thesis.

One ledger: productivity falling 1.3 per cent a year from 2008 to 2019, debt past 300 per cent of GDP, 200 million working-age adults lost and 200 million pensioners gained by 2050, social spending required to triple to 30 per cent of GDP.

The other ledger, over largely the same decade: electricity demand at 10,573 TWh in 2025, roughly a third of world demand and nearly double 2015; 58 per cent of the world's solar installations and 72 per cent of its wind in a single year; coal's share of generation down from 70 to 54 per cent; USD 88 billion of transmission and distribution investment against roughly USD 400 billion spent on grids worldwide; a robot stock of 2,027,000 units, 43 per cent of the world's, taking 54 per cent of a year's global installations, with domestic suppliers' share of the home market moving from 47 to 57 per cent in one year.

Neither ledger is disputed. Both are drawn from the sources the other side cites for other purposes. The essay's opening move is to refuse the reconciliation: state plainly that anyone who reports a single directional verdict has applied an exchange rate between these ledgers, and that the exchange rate is almost never shown.

## Movement 2 -- What an index does when you are not looking

The technical heart, written for a reader who has never opened the composite-indicator literature and will not open it after.

- Weights in additive aggregations are substitution rates, not importances. This is a theorem, not a complaint: symmetrical importance "is incompatible with a linear aggregation rule", and the interpretation of weights as importance is "always completely inappropriate".
- What implied trade-offs look like when someone computes them: the Human Development Index valuing a life-year between about 0.50 dollars and nearly 9,000 dollars depending on the country; Luxembourg placing anywhere from 3rd to 113th under defensible alternative assumptions; 60 of 163 rankings in an environmental index dependent on assumptions rather than data.
- Normalisation carries part of the aggregation invisibly, demonstrable with a Celsius-and-Fahrenheit example that reorders results.
- The limit case: Arrow's theorem, and the working constraint it generates -- no component above 50 per cent weight, or it becomes a dictator.
- The candid admissions inside the field's own instruments. The Correlates of War capability index averages six components' system shares and its own codebook concedes the score "could then be computed on as few as one component". The Lowy Index publishes its weights and then reports that indicator count matters more than the weights. Global Firepower's formula page returns a 404.

End the movement by naming the field's most authoritative concession: a 2026 methods review holding that there is "no single aggregate quantity of national power" and that the search for one is a category error.

## Movement 3 -- The strongest argument against everything in Movement 2

Placed here on purpose, at full strength, before any conclusion is drawn. This is the essay's pivot and it must be the passage a hostile reader finds fairest.

Scalar reduction keeps working. Two variables multiplied -- GDP times GDP per capita -- predict 78 per cent of wars and 70 per cent of militarised disputes over 1816--2010, against 70 and 64 per cent for the six-component index. Power transition theory's single GNP proxy "performed as well as the more complex index of power". A replication of the six-component index finds a single component, the energy measure, carries 16.8 per cent out-of-sample importance while the whole aggregate adds 1.2 per cent over a naive predictor, calling the aggregation "entirely ad hoc" -- which is an argument for *fewer* variables, not for a vector.

The honest statement of the position: on the historical record, adding components did not help and multiplying two variables did. Anyone proposing a four-element vector with per-element posteriors is proposing something that has never outperformed a simpler thing, and cannot demonstrate that it will within the lifetime of the claim.

The essay does not resolve this. It states the ground on which it could be resolved, and concedes that ground lies decades away.

## Movement 4 -- Nesting rather than refuting

The peaking-power thesis treated as the best-specified position in the debate, and then located inside a parameter space rather than argued against.

Credit where due: an explicit quantitative case-selection rule from 1870 to 2018, nine cases, three set aside as overdetermined, a named behavioural mechanism, and named conditioning variables. Contrast with the Thucydides Trap case file, which claims immunity from selection bias because it covers "the entire universe of the cases" while conceding in the same document that the file "is open", and offers no operational definition of a rising or ruling power -- a critique that moves the war rate from 12 of 16 to 19 of 30, and to 1 of 8 after 1950.

Then the symmetry the essay owes the reader: the peaking thesis's load-bearing base of five to six cases is the same order as this programme's five to eight historical analogues. The essay says so in the same breath as the critique, not in a footnote.

The nesting: peaking is a reachable region of the parameter space with prior mass, not a rival. Its internal critics converge on the vector -- "China could peak in one area but advance in others" -- and one of them, working from historian-generated great-power lists for 1820--1990, concludes that "'catching up' or 'overtaking' are the wrong benchmarks", which is an objection to trajectory framing generally, including this programme's.

## Movement 5 -- Saying in advance what would make you wrong

Pre-registration in a field that does not use it, presented as a modest and contestable claim.

The purpose is narrow and worth quoting exactly: to distinguish prediction from postdiction, because "both are important, but conflating the two reduces credibility". The garden of forking paths is quantifiable -- ten binary analytical choices generate 59,049 defensible specifications -- and the discipline exists to close that space before the data are seen.

*Correction, 2026-08-22, recorded rather than made silently: "ten binary analytical choices generate 59,049" is internally inconsistent -- 59,049 is 3^10, and the Olken source describes a ten-table analysis tree implying 3^10 possible regressions (three-way choices, not binary; see `papers/paper-a-measurement/S5-pre-registration.md` section 5.2). The draft follows the source. Second correction, same date: Movement 4's "five to eight historical analogues" is superseded by the harmonised count in `S6-identification.md` ("six to eight -- five under the strictest inclusion rules"), which the Paper A cross-review fixed after this outline was written; the draft follows S6.*

The objections are given their weight rather than listed and dismissed: that pre-analysis plans are unenforceable, that they suppress unanticipated findings, that observational data are often already available to the analyst, and that a plan can be written after a peek. And the deepest one, which is empirical: registered pre-analysis plans have not been shown to improve accuracy, and in the largest social-science forecasting tournament to date experts beat naive benchmarks in 1 of 12 domains while their confidence bore no relation to their accuracy. Pre-registration makes a project auditable. It does not make it right, and the essay claims only the first.

Then the concrete instance, which is where the essay earns the movement. The programme's eight conditions were committed before any estimation code existed, with a commit history establishing the order. The resulting table is unflattering: two conditions within about a percentage point of their thresholds are also the two least directly measured; three cannot presently return their strongest verdict at all. The set is not well calibrated. That sentence appears in the project's own log, dated, and cannot now be removed.

## Movement 6 -- The model rejected its own priors

The essay's most useful passage for a sceptical reader, and the reason the programme is worth reading before it has an answer.

Five gates were specified before any prior was written. Two rejected the committed priors: one regime falls below the coverage floor at 0.025 mass against 0.05, and the trajectory-sanity gate returns a 2050 input multiple of 892.7 against a pre-registered ceiling of 20, with 5.8 per cent of draws breaching. Estimation is blocked. Nothing has been fitted.

Two details make the passage load-bearing rather than merely candid. First, the parameter whose adjustment would most cheaply pass the failing coverage gate is named in the file that contains it, precisely so that changing it later is visible. Second, an earlier run produced a plausible structural diagnosis that turned out to be an artefact of four priors implemented as uniform surrogates -- a wrong finding that looked exactly like a right one, caught by an audit rather than by intuition, and now guarded by a sampler moment check.

The general point, stated without moralising: the failure is of the intended kind, and a framework that had passed all five gates on the first attempt would have told us less about itself.

## Movement 7 -- What a vector costs, and what it refuses

Close on the price, not the payoff.

Four elements, posteriors per element, no cross-state scalar ratio emitted, composites permitted only with full weighting sensitivity beside them. The cost: the essay cannot answer the field's central question -- is the challenger overtaking, and when -- and it cannot populate the contingency table on which power transition theory staked its claim. `Y_net` is a composite in all but name and requires exactly the trade-off judgements Movement 2 objects to in others, which is a difference of degree.

The refusal that matters is not to aggregate. It is to convert measurement disagreement into substantive disagreement. Two analysts holding the same data and different exchange rates will report opposite verdicts and will describe themselves as disagreeing about China. The essay's claim is that they are mostly disagreeing about arithmetic conventions, and that the dashboard alternative -- monitoring components separately, with uncertainty carried through -- is less satisfying and more honest.

A last empirical caution to end on, so the essay does not close on its own preference. Propagating measurement error through a downstream analysis of democracy scores dropped explanatory power from .63 to .40 and dissolved a quadratic term that had been treated as a finding. Ignoring measurement error did not merely widen intervals; it manufactured a result. Capability measurement, built on statistics whose national definitions differ, is exposed to the same failure, and most published power indices report no uncertainty at all.

---

## Constraints on the drafting

- No policy recommendations, no investment framing.
- No teleological vocabulary. The three prohibited words listed in `README.md` do not appear, and no trajectory is described as settled in advance.
- No asymmetric epistemic standards: every critique applied to another literature is applied to this programme in the same passage where it appears.
- Every steel-man is placed where the supporting claim is made, not collected in a limitations section.
- Movements 3 and 6 are the passages a hostile expert reader should find fairest. If they read as concessions grudgingly made, the draft has failed.
- Every quantitative claim traces to a fetched source in `papers/paper-a-measurement/` or the falsifier log. The essay adds no numbers of its own.

---

## Sources

The essay draws on the source set assembled for Paper A and Paper B; see the `## Sources` sections of `papers/paper-a-measurement/OUTLINE.md`, `papers/paper-a-measurement/S3-capability-vector.md` and `papers/paper-b-application/OUTLINE.md`. Primary sources for claims appearing first in this outline:

- Correlates of War, National Material Capabilities -- https://correlatesofwar.org/data-sets/national-material-capabilities/
- NMC documentation -- https://correlatesofwar.org/wp-content/uploads/NMC_Documentation_v5_0.pdf
- Carroll and Kenkel, Prediction, Proxies, and Power -- https://www.sas.rochester.edu/psc/polmeth/papers/Kenkel_Carroll.pdf
- Beckley, The Power of Nations -- https://scispace.com/pdf/the-power-of-nations-measuring-what-matters-441eqyutp6.pdf
- Lowy Institute, Asia Power Index methodology -- https://power.lowyinstitute.org/methodology/
- Carnegie Endowment, Methods of National Power Analysis: Pitfalls and Best Practices -- https://carnegieendowment.org/research/2026/04/methods-of-national-power-analysis-pitfalls-and-best-practices
- Ravallion, Mashup Indices of Development -- https://openknowledge.worldbank.org/server/api/core/bitstreams/7c19b741-66e0-5e55-ba4d-bc7647aadb6b/content
- OECD/JRC Handbook on Constructing Composite Indicators -- https://knowledge4policy.ec.europa.eu/sites/default/files/jrc47008_handbook_final.pdf
- Munda and Nardo, EUR 21834 EN -- https://publications.jrc.ec.europa.eu/repository/bitstream/JRC32434/EUR%2021834%20EN.pdf
- Nosek, Ebersole, DeHaven and Mellor, The preregistration revolution, PNAS -- https://www.pnas.org/doi/10.1073/pnas.1708274114
- Olken, Promises and Perils of Pre-Analysis Plans, Journal of Economic Perspectives 29(3) -- https://economics.mit.edu/sites/default/files/publications/JEP%20Analysis%20Plans%20Final.pdf
- Monogan, Research Preregistration in Political Science, PS 48(3) -- https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/research-preregistration-in-political-science-the-case-counterarguments-and-a-response-to-critiques/E80124ED16BA47D0EA09F03D72B89EC7
- Forecasting Collaborative, Nature Human Behaviour 7:484--501 -- https://pmc.ncbi.nlm.nih.gov/articles/PMC10192018/
- Treier and Jackman, Democracy as a Latent Variable -- https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=61fb0ba9b2e3c6b8619a4aa493fa55f26ff6c10c
- Ember, Global Electricity Review 2026 -- https://ember-energy.org/latest-insights/global-electricity-review-2026/major-countries-and-regions/
- IEA, World Energy Investment 2025, China -- https://www.iea.org/reports/world-energy-investment-2025/china
- IFR, World Robotics 2025, China press release -- https://ifr.org/downloads/press_docs/2025-09-25-IFR_press_release_China_in_English.pdf
- Kugler and Organski, The Power Transition -- http://slantchev.ucsd.edu/courses/pdf/Kugler%20&%20Organski%20-%20The%20Power%20Transition.pdf
- Belfer Center, Thucydides's Trap case file -- https://www.belfercenter.org/programs/thucydidess-trap/thucydidess-trap-case-file
- Hanania, Strategic Studies Quarterly 15(4) -- https://www.airuniversity.af.edu/Portals/10/SSQ/documents/Volume-15_Issue-4/SC-Hanania.pdf
