# Phase 4 — Measurement Literature: National Capability, Composite Indices, and Bayesian Latent-Variable Measurement

**Purpose.** Source-cited evidence base for an academic methods paper that rejects scalar composite power indices in favour of a multi-dimensional capability vector carrying explicit measurement uncertainty.

**Grounding rule applied throughout.** Every value, quotation, formula and number below was extracted from a page fetched during the research session that produced this file. Each item ends with the full URLs of the sources fetched for it. Where a value could not be confirmed from a fetched page it is recorded as `n.a.` and listed in **Gaps and failures**. Aggregators are labelled *(secondary)*.

---

## SECTION 1 — Composite national-power indices

### 1.1 CINC / Correlates of War National Material Capabilities

**Full name.** Composite Index of National Capability (CINC), from the Correlates of War project's National Material Capabilities (NMC) data set. Current version **v7.0**, covering **1816–2022** ([Correlates of War](https://correlatesofwar.org/data-sets/national-material-capabilities/)).

**Components.** Six, in three domains ([Correlates of War](https://correlatesofwar.org/data-sets/national-material-capabilities/)):

| Domain | Component | Notes |
|---|---|---|
| Demographic | Total population | — |
| Demographic | Urban population | — |
| Industrial | Iron and steel production | Pig iron 1816–1899; steel 1900 onward ([NMC v5 codebook](https://correlatesofwar.org/wp-content/uploads/NMC_Documentation_v5_0.pdf)) |
| Industrial | Primary energy consumption | Measured in metric ton coal equivalent ([NMC v5 codebook](https://correlatesofwar.org/wp-content/uploads/NMC_Documentation_v5_0.pdf)) |
| Military | Military personnel | — |
| Military | Military expenditure | — |

**Aggregation and weighting rule.** The publisher's own statement: "This measure is generally computed by summing all observations on each of the 6 capability components for a given year, converting each state's absolute component to a share of the international system, and then averaging across the 6 components" ([Correlates of War](https://correlatesofwar.org/data-sets/national-material-capabilities/)). The codebook is explicit that weighting is equal and that the index degenerates gracefully: "The CINC reflects an average of a state's share of the system total of each element of capabilities in each year, weighting each component equally," and "Hypothetically, CINC could then be computed on as few as one component" ([NMC v5 codebook](https://correlatesofwar.org/wp-content/uploads/NMC_Documentation_v5_0.pdf)).

So, for state \(i\) in year \(t\) with components \(c \in \{1..6\}\): \(\mathrm{CINC}_{it} = \frac{1}{6}\sum_c \frac{x_{cit}}{\sum_j x_{cjt}}\) — i.e. an unweighted mean of six system shares. Two properties follow directly from that construction and matter for the methods argument: the denominator is the system total, so CINC is *relative by construction*, and the index is defined even when components are missing.

**Publisher's own data caution.** "the quality and quantity of the data vary greatly from state to state and from year to year... should do so with caution" ([Correlates of War](https://correlatesofwar.org/data-sets/national-material-capabilities/)).

**Published critique.** Carroll & Kenkel, "Capability Ratios Predict Nothing" (working paper), with a published version as "Prediction, Proxies, and Power," *AJPS* 63(3):577–593 (2019). Their core objections, verbatim: "the CINC function is sensitive to changes in state membership over time"; "the CINC function's equal weighting of all indicators is entirely ad hoc"; and it "assigns the same importance to military spending as it does to personal energy consumption." Empirically, capability ratios "fail to predict any outcome other than the modal category... and barely improve out-of-sample predictive performance (1.2%) over a null model," whereas their machine-learned Dispute Outcome Expectations (DOE) measure improves out-of-sample performance by **16.8%** and fits better in **15 of 18** replications ([Carroll & Kenkel working paper](https://www.sas.rochester.edu/psc/polmeth/papers/Kenkel_Carroll.pdf); published version landing page [Wiley/AJPS](https://onlinelibrary.wiley.com/doi/abs/10.1111/ajps.12442)).

Sources: https://correlatesofwar.org/data-sets/national-material-capabilities/ · https://correlatesofwar.org/wp-content/uploads/NMC_Documentation_v5_0.pdf · https://www.sas.rochester.edu/psc/polmeth/papers/Kenkel_Carroll.pdf · https://onlinelibrary.wiley.com/doi/abs/10.1111/ajps.12442

---

### 1.2 Beckley's GDP × GDP-per-capita measure

**Citation.** Michael Beckley, "The Power of Nations: Measuring What Matters," *International Security* 43(2), Fall 2018, pp. 7–44, doi:10.1162/ISEC_a_00328 ([MIT Press](https://direct.mit.edu/isec/article-abstract/43/2/7/12211); full text fetched via [SciSpace mirror](https://scispace.com/pdf/the-power-of-nations-measuring-what-matters-441eqyutp6.pdf) *(secondary host, primary text)*; also [Belfer Center](https://www.belfercenter.org/publication/power-nations-measuring-what-matters)).

**Components and aggregation.** Two variables, multiplicative, equally weighted: "I follow Bairoch's advice by simply multiplying GDP by GDP per capita, creating an index that gives equal weight to a nation's gross output and its output per person" (p. 18). The intellectual antecedent is Bairoch's claim that "strength of a nation could be found in a formula combining per capita and total GDP" (p. 17). Formally \(P_i = \mathrm{GDP}_i \times (\mathrm{GDP}_i/\mathrm{pop}_i)\).

**Beckley's theoretical claim.** Gross indicators "systematically exaggerate the wealth and military capabilities of poor, populous countries, because they tally countries' resources without deducting the costs countries pay to police, protect, and serve their people" (p. 8). He surveys "at least sixty-nine power measurement frameworks from 1936 to 2010, and forty-two of these frameworks were composed solely of some combination of the gross indicators" (p. 15).

**His critique of CINC.** "more than 1,000 peer-reviewed studies have used CINC to measure power," and CINC "suggests, nonsensically, that... China has dominated the world since 1996 and currently has twice the power resources of the United States" (p. 41).

**Predictive comparison (Table 2, p. 38; 1816–2010, 54 wars and 276 militarised interstate disputes).**

| Measure | Wars predicted correctly | MIDs predicted correctly |
|---|---:|---:|
| GDP | 68% | 64% |
| CINC | 70% | 64% |
| GDP × GDP per capita | 78% | 70% |

**Beckley's own caveats — important for steel-manning.** The index "does not measure net resources directly" and is "a primitive proxy" (p. 18). A published exchange followed: [Correspondence: Measuring Power in International Politics, *International Security* 44(1):197](https://direct.mit.edu/isec/article/44/1/197/12229/Correspondence-Measuring-Power-in-International).

Sources: https://direct.mit.edu/isec/article-abstract/43/2/7/12211 · https://scispace.com/pdf/the-power-of-nations-measuring-what-matters-441eqyutp6.pdf · https://www.belfercenter.org/publication/power-nations-measuring-what-matters · https://direct.mit.edu/isec/article/44/1/197/12229/Correspondence-Measuring-Power-in-International

---

### 1.3 Lowy Institute Asia Power Index

**Publisher and edition.** Lowy Institute; most recent edition fetched is the **2025 Asia Power Index**, covering **27 countries and territories** ([Lowy methodology](https://power.lowyinstitute.org/methodology/); [2025 key findings report](https://power.lowyinstitute.org/downloads/lowy-institute-2025-asia-power-index-key-findings-report.pdf)).

**Structure.** "eight measures of power, 30 thematic sub-measures and 131 indicators" ([Lowy methodology](https://power.lowyinstitute.org/methodology/)).

**Weighting.** Four "resources" measures and four "influence" measures ([Lowy methodology](https://power.lowyinstitute.org/methodology/)):

| Measure | Group | Weight |
|---|---|---:|
| Economic Capability | Resources | 17.5% |
| Military Capability | Resources | 17.5% |
| Resilience | Resources | 10% |
| Future Resources | Resources | 10% |
| Economic Relationships | Influence | 15% |
| Defence Networks | Influence | 10% |
| Diplomatic Influence | Influence | 10% |
| Cultural Influence | Influence | 10% |

**Normalisation.** Distance-to-frontier. **Definition of power used.** "the capacity of a state to direct or influence the behaviour of other states, non-state actors, and the course of international events." The Index states its own lineage: "The methodological framework of the Index is informed by the OECD's Handbook on Constructing Composite Indicators" ([Lowy methodology](https://power.lowyinstitute.org/methodology/); earlier detail in the [2019 methodology paper](https://power.lowyinstitute.org/downloads/lowy-institute-asia-power-index-2019-methodology.pdf)).

**The publisher's own concession on weights** — directly usable in a methods paper: "it is of course possible to reach other value judgements about the relative importance of the measures," and "Sensitivity analysis has determined that the large number of indicators... are quantitatively more important than our weighting scheme" ([Lowy methodology](https://power.lowyinstitute.org/methodology/)).

Sources: https://power.lowyinstitute.org/methodology/ · https://power.lowyinstitute.org/downloads/lowy-institute-2025-asia-power-index-key-findings-report.pdf · https://power.lowyinstitute.org/downloads/lowy-institute-asia-power-index-2019-methodology.pdf

---

### 1.4 Global Firepower Index (PwrIndx)

**Publisher and version.** GlobalFirepower.com; "For the 2025 GFP review, a total of 145 world powers are considered" ([Global Firepower countries listing](https://www.globalfirepower.com/countries-listing.php)).

**Methodology, as stated by the publisher.** The index is called the "PowerIndex ('PwrIndx')" and uses "over 60 individual factors." Aggregation is proprietary: "Our unique, in-house formula allows for smaller, more technologically-advanced, nations to compete with larger, lesser-developed powers and special modifiers, in the form of bonuses and penalties, are applied to further refine the list which is compiled annually." Scale: "A perfect PwrIndx score is 0.0000 which is realistically unattainable" ([Global Firepower countries listing](https://www.globalfirepower.com/countries-listing.php)).

**Stated limitations.** The publisher warns that year-on-year movement is not interpretable as capability change: "Trends do not necessarily indicate a declining power as changes to the GFP formula can also account for this" ([Global Firepower countries listing](https://www.globalfirepower.com/countries-listing.php)).

**No formula is published.** The dedicated methodology page `https://www.globalfirepower.com/pwrindx-explained.php` returned **404** during this session, so the exact list of factors, the modifier list, and the functional form are `n.a.` This is itself an evidentially useful fact: PwrIndx is a widely cited scalar power ranking whose aggregation rule is not publicly specified.

Sources: https://www.globalfirepower.com/countries-listing.php (attempted and failed: https://www.globalfirepower.com/pwrindx-explained.php)

---

### 1.5 Economic Complexity Index (Hausmann / Hidalgo; OEC and the Atlas)

**What it measures and method.** The OEC's own methods documentation defines ECI as the average complexity (PCI) of the activities present in a location, estimated by the *reflections* / eigenvector procedure ([OEC methods](https://oec.world/en/resources/methods)):

- Iterative reflections: \(K_c=\frac{1}{M_c}\sum_p M_{cp}K_p\) and \(K_p=\frac{1}{M_p}\sum_c M_{cp}K_c\).
- Equivalent eigenvector formulation: diagonalise \(\tilde M_{cc'}=\sum_p \frac{M_{cp}M_{c'p}}{M_c M_p}\).
- Binary specialisation matrix: \(M_{cp}=1\) iff \(R_{cp}\ge 1\), where \(R_{cp}=\frac{X_{cp}X}{X_c X_p}\) (revealed comparative advantage).
- Reported as a Z-score: \(ECI=\dfrac{K_c-\tilde K_c}{\sigma(K_c)}\).
- The OEC now publishes ECI across four dimensions: Trade, Technology, Research, and Software ([OEC methods](https://oec.world/en/resources/methods)).

**Published critique.** Eric Kemp-Benedict, Stockholm Environment Institute (MPRA 60705, 2014), shows the ECI is the eigenvector associated with the **second-largest** eigenvalue of a Markov-like matrix \(W\) with \(W_{cc'}=P(c'|c)\), that the complexity measure is "orthogonal to their country diversity score," and that "what that information might be is unclear." He also quantifies how much structure the leading eigenvector leaves behind: "u1c explains 56% of the variation... leaves unexplained another 44%" ([Kemp-Benedict, MPRA](https://mpra.ub.uni-muenchen.de/60705/1/MPRA_paper_60705.pdf)).

**Further primary sources located but not fetched in this session** (so no values are quoted from them): Hidalgo & Hausmann PNAS 2009 https://www.pnas.org/doi/10.1073/pnas.0900943106 ; *Atlas of Economic Complexity* 2013 https://www.hks.harvard.edu/sites/default/files/centers/cid/files/ATLAS_2013_Part1.pdf ; Tacchella et al., PLOS ONE https://journals.plos.org/plosone/article/file?type=printable&id=10.1371/journal.pone.0047278 ; Mealy, Farmer & Teytelboym https://oms-inet.files.svdcdn.com/production/files/main_feb4.pdf?dm=1553075540 .

Sources: https://oec.world/en/resources/methods · https://mpra.ub.uni-muenchen.de/60705/1/MPRA_paper_60705.pdf

---

### 1.6 Formal Bayesian / latent-variable measures of national power or state capacity

**(a) Hanson & Sigman, "Leviathan's Latent Dimensions: Measuring State Capacity for Comparative Political Research."** *Journal of Politics* 83(4):1495–1510 (2021), doi 10.1086/715066 ([University of Chicago Press](https://www.journals.uchicago.edu/doi/10.1086/715066)).

Method and scope, from the authors' own documentation: a "Bayesian latent variables model" over **21 indicators**, estimating **three** substantive dimensions — extractive, coercive, and administrative capacity — for "1960-2015... 177 different states and a total of 18,254 country-years" ([Hanson & Sigman documentation PDF](https://public.websites.umich.edu/~jkhanson/resources/StateCapac_v1_doc.pdf); [dataset page](https://public.websites.umich.edu/~jkhanson/state_capacity.html)).

This is the closest existing analogue to the paper's proposed architecture: a latent measurement model that deliberately refuses to collapse capacity to one number, instead reporting a small vector of dimensions with posterior uncertainty.

**(b) Carroll & Kenkel, Dispute Outcome Expectations (DOE).** *AJPS* 63(3):577–593 (2019) ([Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1111/ajps.12442); working paper [here](https://www.sas.rochester.edu/psc/polmeth/papers/Kenkel_Carroll.pdf)). DOE replaces CINC ratios with a predictive model of dispute outcomes; on the fetched working paper it improves out-of-sample performance by **16.8%** over a null model and fits better in **15 of 18** replications. **Caveat, flagged honestly:** the fetched text describes DOE as a machine-learning (ensemble/ordered-outcome) estimator, not a Bayesian latent-variable model. It qualifies as a formal, estimated, uncertainty-bearing alternative to a composite index, but should not be cited as "Bayesian."

**Additional peer-reviewed latent-variable measures in IR located this session** (methods confirmed only at abstract level, so cited as located rather than characterised in detail): Bayesian latent measurement of major-power support signals, *Journal of Peace Research* 56(3):364 https://academic.oup.com/jpr/article/56/3/364/8365318 ; "Continuous recognition" of sovereignty, *JPR* 57(6):789 https://academic.oup.com/jpr/article/57/6/789/8365303 ; Bayesian IRT measurement of peace-agreement strength, *Political Science Research and Methods* https://www.cambridge.org/core/journals/political-science-research-and-methods/article/latent-variable-approach-to-measuring-and-explaining-peace-agreement-strength/9184401C70859F5B4EB155F2671D7EBA .

**Framing source that states the paper's own thesis independently.** Carnegie Endowment, "Methods of National Power Analysis: Pitfalls and Best Practices" (2026): "power is multidimensional... The notion of a single aggregate quantity of national power existing in the abstract therefore makes little or no sense," and "Aggregated measures of power select and weight variables in an essentially arbitrary way" ([Carnegie](https://carnegieendowment.org/research/2026/04/methods-of-national-power-analysis-pitfalls-and-best-practices)). A related critique of China's Comprehensive National Power indices appears in *Chinese Journal of International Politics* 19(3):237 https://academic.oup.com/cjip/article/19/3/237/8711324 .

Sources: https://www.journals.uchicago.edu/doi/10.1086/715066 · https://public.websites.umich.edu/~jkhanson/resources/StateCapac_v1_doc.pdf · https://public.websites.umich.edu/~jkhanson/state_capacity.html · https://onlinelibrary.wiley.com/doi/abs/10.1111/ajps.12442 · https://www.sas.rochester.edu/psc/polmeth/papers/Kenkel_Carroll.pdf · https://carnegieendowment.org/research/2026/04/methods-of-national-power-analysis-pitfalls-and-best-practices

---

## SECTION 2 — Methodological critiques of composite indicators

### 2.1 Ravallion on "mashup indices of development"

**Core argument.** Ravallion defines a mashup index as "a composite index for which the producer is only constrained by the availability of data in choosing what variables to include and their weights," where "Neither the menu of the primary series nor the aggregation function is pre-determined from theory and practice, but are 'moving parts' of the index" (p. 3). His central methodological charge is that such indices embed trade-offs nobody has examined: "the weights attached to the component indices are typically explicit, this is almost never the case for the weights attached to the underlying dimensions," and "little or no attention is given to the implied tradeoffs" (p. 12). His bottom line: "A composite index is not essential for many of the purposes of evidence-based development policy-making... there are important aspects of development that cannot be captured in a single index" (p. 32), and "nagging doubts remain about the value-added of mashup indices... relative to the 'dashboard' alternative of monitoring the components separately" (abstract).

**Specific evidence he assembles** — the most directly reusable material for a paper that rejects scalar aggregation:

| Finding | Detail | Page |
|---|---|---|
| Implied value of a life-year in the HDI | ranges from "$0.50 per year... for Zimbabwe" (Liberia $5.51) to "almost $9,000 per year in the richest countries" | p. 14 |
| Weight inertia | "The weights on the three components of the HDI... have not changed in 20 years, and it is hard to believe that the HDI got it right first go" | p. 16 |
| Rank-averaging indices | for the Doing Business Index "the weights on any primary variable... are unknown, and difficult to determine"; "These aggregation methods are thus capable of building in perverse valuations" | p. 13 |
| Robustness practice | "Few robustness tests are provided"; the World Governance Indicators are "seemingly unique" in constructing confidence intervals | pp. 18–19 |
| Weight sensitivity (Slottje) | Luxembourg's rank ranges from 3 to 113 across weighting methods | pp. 18–19 |
| High correlation ≠ stable ranks | correlations of 0.95–0.997 remain consistent with sizeable re-rankings | pp. 20–23 |
| Data revisions | DBI revisions changed rankings by ≥10 places for 48 countries | pp. 20–23 |
| Rank uncertainty (Høyland et al.) | no country has >75% chance of being in the HDI top 10 | pp. 20–23 |
| DBI rank intervals | Georgia rank 18, 95% CI (11,59); Saudi Arabia 23, CI (12,63); Mauritius 27, CI (16,77) | pp. 20–23 |
| Consequence | "the index does not do a very good job in distinguishing between most of the regulatory environments in the world" | pp. 20–23 |
| Assumption-dependence (Saisana & Saltelli 2010, EPI) | rankings for 60 of 163 countries "depend strongly on the original methodological assumptions" | p. 23 |
| Weight-driven reordering | Finland's Newsweek rank moves 1 → 17 with all weight on health; China 66 → 13 with all weight on economic dynamism | p. 24 |

Citation: Martin Ravallion, "Mashup Indices of Development," World Bank Policy Research Working Paper 5432 (2010); journal version *World Bank Research Observer* 27(1):1–32 (2012). A companion paper is "Troubling Tradeoffs in the Human Development Index," WPS5484.

Sources: https://openknowledge.worldbank.org/server/api/core/bitstreams/7c19b741-66e0-5e55-ba4d-bc7647aadb6b/content · https://openknowledge.worldbank.org/entities/publication/0dc4084b-9566-5844-8cdf-ae03e53515a7 · https://openknowledge.worldbank.org/entities/publication/4fa16c40-5ad2-5b73-8420-02dcf0ddee7b · https://ideas.repec.org/p/wbk/wbrwps/5484.html *(secondary index page)*

---

### 2.2 OECD / EC-JRC *Handbook on Constructing Composite Indicators*

**Citation.** Nardo, Saisana, Saltelli & Tarantola (JRC) with Hoffmann & Giovannini (OECD), *Handbook on Constructing Composite Indicators: Methodology and User Guide*, OECD, 2008, ISBN 978-92-64-04345-9 ([EC Knowledge4Policy PDF](https://knowledge4policy.ec.europa.eu/sites/default/files/jrc47008_handbook_final.pdf); also hosted at [OECD](https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/08/handbook-on-constructing-composite-indicators-methodology-and-user-guide_g1gh9301/9789264043466-en.pdf)).

**Core argument.** Composite indicators are legitimate but only if the value judgements inside them are made explicit and their robustness is tested: "may send misleading policy messages if poorly constructed or misinterpreted" (p. 13), and "To minimise the risks of producing meaningless composite indicators, sensitivity and robustness analysis are required" (p. 49).

**The ten-step checklist (pp. 20–21).** 1 Theoretical framework · 2 Data selection · 3 Imputation · 4 Multivariate analysis · 5 Normalisation · 6 Weighting and aggregation · 7 Uncertainty and sensitivity analysis · 8 Back to the data · 9 Links to other indicators · 10 Visualisation.

**The statements a methods paper should quote directly:**

| Claim | Verbatim | Page |
|---|---|---|
| Weights are value judgements | "Regardless of which method is used, weights are essentially value judgements"; "equal weighting does not mean 'no weights'" | p. 31 |
| Weights are trade-offs, not importances | "In both linear and geometric aggregations, weights express trade-offs between indicators"; there is "an inconsistency between how weights are conceived... and the actual meaning" | p. 33 |
| Restated formally | "weights in additive aggregations necessarily take the meaning of substitution rates (trade-offs) and do not indicate the importance of the associated indicator" | p. 112 |
| Normalisation is not neutral | "Different normalisation methods will produce different results for the composite indicator" (illustrated with a Celsius/Fahrenheit worked example) | p. 83 |
| Required uncertainty analysis | robustness should be assessed "in terms of e.g., the mechanism for including or excluding an indicator, the normalisation scheme, the imputation of missing data, the choice of weights, the aggregation method" | pp. 16, 21 |
| Seven sources of uncertainty enumerated | — | p. 34 |
| Worked failure case | the UN Technology Achievement Index "is not a robust measure of countries' technology achievement" | p. 124 |

**Arrow-style impossibility, stated by the Handbook itself.** "Arrow's impossibility theorem (Arrow, 1963) clearly shows that no perfect aggregation convention can exist" (p. 52 / p. 105). The Handbook converts this into a design constraint: "no indicator weight constitute more than 50% of the total weights; otherwise... this individual indicator would become a dictator in Arrow's terminology," and "no dimension should weigh more than 50% of the total weights (Munda, 2005b)" (p. 111).

Sources: https://knowledge4policy.ec.europa.eu/sites/default/files/jrc47008_handbook_final.pdf · https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/08/handbook-on-constructing-composite-indicators-methodology-and-user-guide_g1gh9301/9789264043466-en.pdf

---

### 2.3 Sensitivity of composite index *rankings* to weighting and normalisation (Saisana, Saltelli, Tarantola)

**Core argument.** Saisana, Saltelli & Tarantola, "Uncertainty and Sensitivity Analysis Techniques as Tools for the Quality Assessment of Composite Indicators," *Journal of the Royal Statistical Society Series A* 168(2):307–323 (2005), doi 10.1111/j.1467-985X.2005.00350.x. From the fetched abstract: "doubts are often raised about the robustness of the resulting countries' rankings"; the paper proposes combined uncertainty and sensitivity analysis as a quality-assurance framework, and applies it to the UN technology achievement index ([OUP/JRSS-A abstract](https://academic.oup.com/jrsssa/article-abstract/168/2/307/7084307); JRC record [here](https://publications.jrc.ec.europa.eu/repository/handle/JRC24397)).

The strongest quantitative statement located this session comes from the same authors' later Environmental Performance Index application, reported inside Ravallion (§2.1, p. 23): rankings for **60 of 163** countries "depend strongly on the original methodological assumptions." The EPI report itself is at https://publications.jrc.ec.europa.eu/repository/bitstream/JRC56990/reqno_jrc56990_saisana_saltelli_2010epi_eur.pdf%5B1%5D.pdf .

Sources: https://academic.oup.com/jrsssa/article-abstract/168/2/307/7084307 · https://publications.jrc.ec.europa.eu/repository/handle/JRC24397 · https://openknowledge.worldbank.org/server/api/core/bitstreams/7c19b741-66e0-5e55-ba4d-bc7647aadb6b/content

---

### 2.4 The aggregation problem / Arrow-style impossibility for multidimensional indices

**Not `n.a.`** Two fetched sources establish it.

**(a) Munda & Nardo, "Constructing Consistent Composite Indicators: the Issue of Weights," EUR 21834 EN (2005), Office for Official Publications of the European Communities.** The argument is that the meaning practitioners assign to weights is formally incompatible with the aggregation rule they use ([JRC PDF](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC32434/EUR%2021834%20EN.pdf)):

| Claim | Verbatim | Location |
|---|---|---|
| The core inconsistency | "a theoretical inconsistency exists between the real theoretical meaning of weights and the meaning that is generally attributed to them by the standard practice" | abstract |
| Symmetric importance is incompatible with linearity | symmetrical importance "is incompatible with a linear aggregation rule" | p. 3 |
| Weights are substitution rates | "the estimation of weights is equivalent to that of substitution rates, implying a compensatory logic" | p. 4 |
| Trade-offs are scale-dependent | "trade-offs depend on the scales of measurement" | p. 6 |
| Verdict on "importance weights" | "the interpretation of weights as a measurement of the psychological concept of importance is always completely inappropriate" | p. 6 |
| Remedy | "If one wants the weights to be interpreted as 'importance coefficients'... non-compensatory aggregation procedures must be used" | pp. 7–8 |
| Social-choice route | quoting Arrow & Raynaud (1986, p.77): "The next highest ambition for an aggregation algorithm is to be Condorcet" | p. 8 |
| Conclusion 3 | linear aggregation implies "complete substitutability" | p. 9 |

**Honest scope note:** this report does *not* itself invoke Arrow's impossibility theorem by name; the explicit invocation is in the OECD/JRC Handbook (§2.2, pp. 52/105). The companion volume is Munda & Nardo, "Non-Compensatory Composite Indicators for Ranking Countries," EUR 21833 EN https://publications.jrc.ec.europa.eu/repository/bitstream/JRC32435/EUR%2021833%20EN.pdf . Related rank-robustness work: OPHI Working Paper 26 https://ophi.org.uk/sites/default/files/OPHI-wp26_vs5.pdf and https://ophi.org.uk/sites/default/files/OPHI-wp26b_vs4.pdf .

Sources: https://publications.jrc.ec.europa.eu/repository/bitstream/JRC32434/EUR%2021834%20EN.pdf · https://knowledge4policy.ec.europa.eu/sites/default/files/jrc47008_handbook_final.pdf · https://publications.jrc.ec.europa.eu/repository/bitstream/JRC32435/EUR%2021833%20EN.pdf

---

## SECTION 3 — Bayesian latent-variable measurement in political science

### 3.1 Treier & Jackman, "Democracy as a Latent Variable"

**Citation.** Published as *American Journal of Political Science* 52(1):201–217 (2008), doi 10.1111/j.1540-5907.2007.00308.x ([RePEc record](https://ideas.repec.org/a/wly/amposc/v52y2008i1p201-217.html) *(secondary)*). The version fetched and quoted here is the authors' Stanford working paper dated 17 July 2003 ([CiteSeerX PDF](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=61fb0ba9b2e3c6b8619a4aa493fa55f26ff6c10c)).

| Element | Content |
|---|---|
| Latent quantity | \(x_i\), the latent level of democracy of country \(i\) |
| Model class | Bayesian ordinal item-response model over 5 Polity indicators: \(l_{ij}=x_i b_j\), logistic CDF, \(K_j-1\) thresholds per item; a latent class model is also fitted |
| Identification | "the model parameters are not identified without further assumptions"; because \(l_{ij}=x_i b_j = x_i r\, b_j r^{-1}\), "For the special case of \(r=-1\) we obtain a 180 degree rotation... we lack global identification". Resolution: "we constrain the latent \(x_i\) to have mean zero and variance one... providing local identification" (pp. 10–11) |
| Uncertainty reported | posterior SD of \(x_i\); WinBUGS, 3,000 burn-in, 5,000 iterations thinned by 10 → 500 draws |
| Propagation | "treating the democracy measures as akin to missing data, and use the ordinal IRT measurement model to supply multiple imputations"; formally \(p(b\mid z)=\int_X p(b\mid z,x)\,g(x)\,dx\), correcting attenuation of \(\hat b\) (pp. 27–30) |

**The finding that matters most for a paper arguing for explicit uncertainty.** "this measurement error is considerable"; it is heteroskedastic and largest at the extremes; **34 of 153** countries had perfect Polity scores in 2000 and **36 of 153** were statistically indistinguishable from the United States. In their downstream GDP regression, \(r^2\) falls from **.63** using raw Polity, to **.57** using posterior means, to **.40** once measurement uncertainty is propagated — and the quadratic term becomes indistinguishable from zero. Ignoring measurement error therefore manufactured a substantive result.

Sources: https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=61fb0ba9b2e3c6b8619a4aa493fa55f26ff6c10c · https://ideas.repec.org/a/wly/amposc/v52y2008i1p201-217.html

---

### 3.2 Fariss's dynamic latent-variable human-rights work

**Citation.** Christopher J. Fariss, "Respect for Human Rights Has Improved Over Time: Modeling the Changing Standard of Accountability," *American Political Science Review* 108(2):297–318, doi 10.1017/S0003055414000070 ([author's PDF](http://cfariss.com/documents/Fariss2014APSR.pdf)).

| Element | Content |
|---|---|
| Latent quantity | \(\theta_{it}\), latent respect for physical integrity rights; 1949–2010, n = 9,267 |
| Model class | Dynamic ordinal item-response theory (DO-IRT), extending Schnakenberg & Fariss (2014), with dynamic cut-points \(\alpha_{tjk}\) and item discriminations \(\beta_j\) (equations 1–7) |
| Priors | \(\theta_{i1}\sim N(0,1)\); \(\theta_{it}\sim N(\theta_{i,t-1},\sigma)\); \(\sigma\sim U(0,1)\); \(\beta_j\sim \mathrm{Gamma}(4,3)\); \(\alpha_{tjk}\sim N(\alpha_{t-1,jk},4)\); \(\alpha_{1jk}\sim N(0,4)\) with ordering constraints |
| Estimation | JAGS, 2 chains × 100,000 iterations, 50,000 burn-in |
| Item structure | standards-based items (CIRI ×4, PTS ×2, Hathaway, ITT) receive **time-varying** cut-points; event-based items (Harff & Gurr, PITF, Rummel, UCDP, WHPSI) receive **constant** cut-points — this asymmetry *is* the identification of the changing standard of accountability |
| Uncertainty propagation | posterior predictive checks via \(S_{itj}\) sums of squares; credible intervals reported; missing data "only increase the uncertainty for the estimate of a given country-year"; lagged-latent uncertainty propagated by the Schnakenberg & Fariss method (Appendices L, N) |
| Explicit non-identification statement | p. 305, fn. 27: **"However, a model without this restriction is not identified with respect to rotation."** |

Companion: Fariss (2019), *APSR* http://cfariss.com/documents/Fariss2019APSR.pdf ; supplementary appendix http://cfariss.com/documents/Fariss2014APSR_SupplementaryAppendix.pdf .

Sources: http://cfariss.com/documents/Fariss2014APSR.pdf · http://cfariss.com/documents/Fariss2019APSR.pdf · http://cfariss.com/documents/Fariss2014APSR_SupplementaryAppendix.pdf

---

### 3.3 Pemstein, Meserve & Melton, "Democratic Compromise"

**Citation.** Daniel Pemstein, Stephen A. Meserve and James Melton, "Democratic Compromise: A Latent Variable Analysis of Ten Measures of Regime Type," *Political Analysis* 18(4):426–449 (2010), doi 10.1093/pan/mpq020 ([Cambridge PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2A6B2BBA6F80367644F2C5007E1CFC29/S1047198700012559a.pdf/democratic_compromise_a_latent_variable_analysis_of_ten_measures_of_regime_type.pdf); [article landing page](https://www.cambridge.org/core/journals/political-analysis/article/democratic-compromise-a-latent-variable-analysis-of-ten-measures-of-regime-type/2A6B2BBA6F80367644F2C5007E1CFC29)).

**Latent quantity.** "The quantity of interest in this business is \(z_i\), the true level of democracy in country-year \(i\)" (p. 432). "We model each indicator as an approximation to an unobserved—or latent—continuous unidimensional variable" (p. 431). Coverage: "We generated UDS for virtually all countries in the world from 1946 to 2000" (p. 437).

**Model class.** Multirater ordinal probit: "we use a technique, multirater ordinal probit, originally developed to compare the performance of multiple essay graders" (p. 433). Measurement equation (1): \(t_{ij}=z_i+e_{ij}\), \(e_{ij}\sim N(0,r_j^2)\) — "judge \(j\) perceives the true level of democracy accurately on average but makes stochastic mistakes based on her own personal error variance, \(r_j^2\)" (p. 431). Observation model (4): \(p(y_{ij}=c\mid z_i,c_j,r_j)=\Phi\!\left(\frac{c_{j,c}-z_i}{r_j}\right)-\Phi\!\left(\frac{c_{j,c-1}-z_i}{r_j}\right)\) (p. 434).

**The reliability-weighting result** — the single most transferable idea for a capability-vector paper. Conditional on ratings and error variances, \(z_i\) has posterior mean \(\dfrac{\sum_j t_{ij}/r_j^2}{1/r_0^2+\sum_j 1/r_j^2}\) (eq. 2) and variance \(\dfrac{1}{1/r_0^2+\sum_j 1/r_j^2}\) (eq. 3), so "our basic model incorporates information from every available rater but discounts the contributions of less reliable judges" and "our uncertainty about \(z_i\) is decreasing in the number of raters" (pp. 432–433). This is precision-weighted aggregation derived from the model, not weights chosen by the analyst — the direct methodological alternative to CINC's ad hoc equal weighting.

**Ten input scales** (Table 1, p. 429): Arat (1991); Bowman, Lehoucq & Mahoney (2005); Bollen (2001); Freedom House (2007); Hadenius (1992); Przeworski et al. (2000) (PACL, as extended by Cheibub & Gandhi 2010); Polity (Marshall, Jaggers & Gurr 2006); Polyarchy (Coppedge & Reinicke 1991); Gasiorowski's Political Regime Change (1996, extended by Reich 2002); Vanhanen (2003). Four continuous scales were discretised at stated cutpoints ("Arat: 50–100, by 10s; Bollen: 10–90, by 10s; Hadenius: 1, 2, 3, 4, 7, 8, 9; Vanhanen: 5–35, by 5s"), skipping Hadenius 5–6 "because of a dearth of observations" (p. 433).

**Identification.** "Following Johnson and Albert (1999), we identify the model using a Bayesian estimation approach and adopt proper prior distributions for \(z\) and \(s\)... we assume independent standard normal prior distributions for each latent trait \(z_i\)—note that this is equivalent to assuming \(r_0^2=1\)"; inverse-gamma priors on \(r_j^2\); uniform priors on ordered cutoffs with \(c_{j,0}=-\infty\), \(c_{j,K_j}=\infty\) (p. 434). MCMC: 1,000,000 iterations, first half burn-in, every hundredth draw retained → 5,000 posterior draws (p. 434).

**Uncertainty reporting and propagation.** "We accompany this new scale of democracy with quantitative estimates of measurement error" (p. 427). Point estimates are posterior means with 95% HPD regions (p. 437); posterior samples are released with a tutorial "that demonstrates how to use the UDS in applied analyses, taking measurement error into account" (p. 437). Comparisons are made probabilistically: \(\Pr(z_i<z_{US})\) gives p = .96 for Brazil and .94 for India, but only .73 for Brazil vs Honduras and .59 for Jordan vs Egypt (p. 440). Uncertainty scales with information: posterior SD is lowest in 1981 and 2000 when ratings are densest, and refitting with only Freedom House, PACL and Polity raises average posterior SD by **24%** (p. 441).

**Explicit statements of unidentified / weakly identified quantities.** "Fundamentally, we do not observe any of the quantities—\(z_i\), \(t_{ij}\), and \(r_j^2\)—that feature in equation (1)" (p. 433). The unbiasedness assumption is untestable: "our assumption that raters perceive democracy levels in a noisy but unbiased fashion is, admittedly, quite strong. Although we cannot directly test this assumption..." (p. 435). Cutoffs are weakly identified where data are thin: "the cutoff cannot be placed reliably on the underlying UDS. Larger error bars are primarily caused by a paucity of observations" (p. 442); "There is simply too much overlap in the true level of democracy in each of the categories in the middle of Polity for the model to distinguish cutoff locations effectively" (p. 442). And the ceiling problem: "Error bars for developed democracies are large, indicating our uncertainty about the point estimates and the UDS' limited ability to discriminate between developed democracies" (p. 440); "Recent research has shown that the error variability of popular measures is large enough to render all but the most dissimilar of regimes statistically indistinguishable" (p. 427).

Sources: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2A6B2BBA6F80367644F2C5007E1CFC29/S1047198700012559a.pdf/democratic_compromise_a_latent_variable_analysis_of_ten_measures_of_regime_type.pdf · https://www.cambridge.org/core/journals/political-analysis/article/democratic-compromise-a-latent-variable-analysis-of-ten-measures-of-regime-type/2A6B2BBA6F80367644F2C5007E1CFC29 · https://ideas.repec.org/a/cup/polals/v18y2010i04p426-449_01.html *(secondary)*

---

### 3.4 The V-Dem measurement model (V-Dem's own methodology documentation)

**Citation.** Daniel Pemstein, Kyle L. Marquardt, Eitan Tzelgov, Yi-ting Wang & Farhad Miri, "The V–Dem Measurement Model: Latent Variable Analysis for Cross-National and Cross-Temporal Expert-Coded Data," V-Dem Working Paper SERIES 2015:21 (NEW VERSION), December 2015. Fetched at [SciSpace mirror](https://scispace.com/pdf/the-v-dem-measurement-model-latent-variable-analysis-for-1997yaxojn.pdf) *(secondary host of the primary working paper; V-Dem's own URL `https://v-dem.net/media/publications/v-dem_working_paper_2016_21.pdf` returned 404 in this session)*.

| Element | Content |
|---|---|
| Latent quantity | \(z_{ct}\), the latent trait for country \(c\) at time \(t\), rated by roughly 5 experts per country-year |
| Model class | Ordinal IRT / multi-rater ordinal probit: \(\tilde y_{ctr}=z_{ct}+e_{ctr}\), \(e_{ctr}\sim F(e_{ctr}/\sigma_r)\), rater thresholds \(\tau_{r,k}\), reparameterised as discrimination \(\beta_r=1/\sigma_r\) and \(\gamma_{r,k}=\tau_{r,k}/\sigma_r\) (Eq. 3) |
| Precision weighting | conditional posterior \(z_{ct}\sim N(a_{ct}/b_{ct},\,1/b_{ct})\) with \(b_{ct}=1+\sum_r\beta_r\) — the posterior mean is a discrimination-weighted average of rater perceptions |
| Priors | \(\beta_r\sim N(1,1)\) truncated at 0; hierarchical thresholds \(\gamma_{r,k}\sim N(\gamma^c_k,0.2)\), \(\gamma^c_k\sim N(\gamma^\mu_k,0.2)\), \(\gamma^\mu_k\sim U(-2,2)\); informative latent prior \(z_{ct}\sim N(\bar{\bar y}_{ct},1)\) built from confidence-weighted coder averages |
| Uncertainty | MCMC with 4 chains, 5,000 iterations, 500 burn-in, thinned by 10 → 450 draws per chain (1,800 total), escalating to 10k/20k/40k/80k if more than 5% of parameters fail \(\hat r\ge1.1\). Public release provides posterior **median**, posterior **SD**, and **68% HPD** bounds; full posterior samples are archived on CurateND (http://curate.nd.edu) |
| Identification strategy | bridge coders and lateral coders, plus planned anchoring vignettes (King & Wand 2007) |

Sources: https://scispace.com/pdf/the-v-dem-measurement-model-latent-variable-analysis-for-1997yaxojn.pdf · http://curate.nd.edu (attempted and failed: https://v-dem.net/media/publications/v-dem_working_paper_2016_21.pdf)

---

### 3.5 A published latent-variable model whose authors explicitly report a quantity is not, or only weakly, identified

**Not `n.a.` — three independent instances, all quoted verbatim from fetched primary texts.**

| Source | Statement | Location |
|---|---|---|
| V-Dem measurement model | "we currently lack the necessary overlapping observations to completely identify the scale of the latent trait cross-nationally" | p. 8 |
| V-Dem measurement model | "It also assures that the model is weakly identified when a country is completely unconnected from the rest of the rating network" (roughly 7 countries) | p. 9 |
| V-Dem measurement model | "this approach will not identify or adjust for DIF where bridging information is sparse"; "This lack of DIF identification in certain cases is a weakness of the current analysis" | p. 11 |
| V-Dem measurement model | "we lack sufficient data to fully model DIF cross-nationally, weakening the cross-national comparability of the V–Dem measures" | p. 20 |
| V-Dem measurement model | linearized estimates "are not uniquely identified" | p. 16 |
| Fariss 2014, *APSR* | "However, a model without this restriction is not identified with respect to rotation." | p. 305, fn. 27 |
| Treier & Jackman working paper | "the model parameters are not identified without further assumptions"; "For the special case of \(r=-1\) we obtain a 180 degree rotation... we lack global identification" | pp. 10–11 |
| Pemstein, Meserve & Melton 2010 | untestable assumption: "Although we cannot directly test this assumption..." (p. 435); weakly identified cutoffs: "the cutoff cannot be placed reliably on the underlying UDS" (p. 442) | pp. 435, 442 |

The disciplinary norm this establishes is precise and directly usable: in the best latent-measurement work in political science, non-identification is *declared in the text*, and the identifying restriction is named rather than buried. A capability-vector paper can hold itself to exactly that standard.

Sources: https://scispace.com/pdf/the-v-dem-measurement-model-latent-variable-analysis-for-1997yaxojn.pdf · http://cfariss.com/documents/Fariss2014APSR.pdf · https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=61fb0ba9b2e3c6b8619a4aa493fa55f26ff6c10c · https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2A6B2BBA6F80367644F2C5007E1CFC29/S1047198700012559a.pdf/democratic_compromise_a_latent_variable_analysis_of_ten_measures_of_regime_type.pdf

---

## SECTION 4 — Pre-registration outside experiments

### 4.1 Nosek, Ebersole, DeHaven & Mellor, "The preregistration revolution"

**Citation.** *PNAS* 115(11):2600–2606 (2018) ([PNAS](https://www.pnas.org/doi/10.1073/pnas.1708274114)).

**Stated purpose and the prediction/postdiction distinction.** "Preregistration distinguishes analyses and outcomes that result from predictions from those that result from postdictions." Crucially, the authors do not claim prediction is superior: "Preregistration does not favor prediction over postdiction; its purpose is to make clear which is which." They adopt general terminology deliberately: "We use the more general terms––postdiction and prediction––to capture this important distinction." The inferential cost of conflating them: "Mistaking postdiction as prediction underestimates the uncertainty of outcomes," and "In exploratory or discovery research, P values have unknown diagnosticity."

**Their claim about what preregistration achieves.** "Preregistration does not eliminate the possibility of poor statistical practices, but it does make them detectable" — a transparency claim, not an efficacy claim.

**Their own stated caveat, worth quoting in a steel-manning section.** "there is not yet sufficient experimental evidence establishing its superiority for reproducibility." They also cite Franco et al.'s 40% / 70% non-reporting figures and discuss cross-validation and sealed-data approaches as complements.

Sources: https://www.pnas.org/doi/10.1073/pnas.1708274114

---

### 4.2 A published argument FOR pre-registration in observational / non-experimental research

**(a) Dal-Ré, Ioannidis, Bracken, Buffler, Chan, Franco, La Vecchia & Weiderpass, "Making Prospective Registration of Observational Research a Reality," *Science Translational Medicine* 6(224):224cm1 (2014), doi 10.1126/scitranslmed.3007513** ([Science](https://www.science.org/doi/10.1126/scitranslmed.3007513); indexed at [PubMed](https://pubmed.ncbi.nlm.nih.gov/24553383/) *(secondary)*).

Core position, verbatim: "We suggest that there is an ethical and scientific imperative to publicly preregister key information from newly approved protocols, which should be required by funders." Benefits: "There are several postulated benefits in systematically registering all OSs: increasing transparency and credibility, improving the peer-review process and ethical conduct of studies, and ensuring that the totality of evidence is publicly available." They further argue registration "may enhance communication regarding explored, but not published, hypotheses," "may facilitate systematic reviews and research collaborations," "may reduce redundancy and funding committed to research questions for which adequate studies have already been conducted," creates "a publicly available audit trail," and "allows others to fully understand and openly debate the nature and merit of the analyses."

Their evidence on the scale of the gap:

| Statistic | Value |
|---|---|
| Observational studies registered on ClinicalTrials.gov as of 29 Jan 2014 | 29,826 ("18.6% among more than 160,000") |
| Eligible PubMed papers, 2011 | 400,601 |
| Tagged as RCTs | 23,350 (6%) |
| Not RCT-tagged | 377,251 |
| Random sample of 50 non-RCT-tagged papers | 36 (72%) nonrandomised; "Only two listed a registration number" |
| Annual publication ratio | "almost 300,000 versus 20,000 publications" (observational vs RCT) |
| Overall | "Registration numbers still accompany only ~20% of RCTs, and registration of OSs is distinctly uncommon" |

**(b) Hardwicke & Wagenmakers, "Reducing bias, increasing transparency and calibrating confidence with preregistration," *Nature Human Behaviour* 7:15–26 (2023), doi 10.1038/s41562-022-01497-2** ([Nature](https://www.nature.com/articles/s41562-022-01497-2)). Their two stated pragmatic functions: preregistration "reduces the risk of bias by encouraging outcome-independent decision-making" and "increases transparency, enabling others to assess the risk of bias and calibrate their confidence in research outcomes." The second function is the one that transfers cleanly to non-experimental work: it is an auditability claim that does not depend on random assignment. **Honest limitation:** the fetched page did not surface the article's treatment of secondary/existing data, its preregistration-vs-registered-reports distinction, or its stated limitations, so those are `n.a.` here.

**(c) Monogan (2015) also belongs here** — see §4.4 — since he explicitly addresses registering observational and inductive designs.

Sources: https://www.science.org/doi/10.1126/scitranslmed.3007513 · https://pubmed.ncbi.nlm.nih.gov/24553383/ · https://www.nature.com/articles/s41562-022-01497-2

---

### 4.3 Published arguments AGAINST / sceptical of pre-registration and pre-analysis plans

Two distinct, fully fetched critiques from economics, plus the discipline-internal critiques catalogued by Monogan.

**(a) Benjamin A. Olken, "Promises and Perils of Pre-Analysis Plans," *Journal of Economic Perspectives* 29(3):61–80** ([MIT](https://economics.mit.edu/sites/default/files/publications/JEP%20Analysis%20Plans%20Final.pdf)).

| Argument | Verbatim / detail |
|---|---|
| Complete pre-specification is infeasible | "fully specifying papers in advance is close to impossible"; a 10-table analysis tree implies \(3^{10}=59{,}049\) possible regressions |
| Practical bloat | early PAPs "exceeding 50 pages" |
| Cost to research quality | "papers following rigorous pre-specified analysis plans may miss the nuance that categorizes social science research"; it "prevents you from learning about your data as you analyze it" |
| The problem may be smaller than assumed | Brodeur et al.: 10–20% of significant tests misallocated, but "no evidence of this problem arising in randomized trials" (92.75% vs 95%); Klein et al.: 10–11 of 13 replicate |
| Descriptive baseline | a sample of 18 RCT papers in top-5 journals, none with PAPs, median 4 treatment arms, 4 main outcomes, 6.5 secondary outcomes, average z-statistic 3.18 |
| Bottom line | "Forcing all papers to be fully pre-specified from start to end would likely result in simpler papers, which could potentially lose some of the nuance of current work... we would be losing more than we would gain" (p. 78) |

**(b) Lucas C. Coffman & Muriel Niederle, "Pre-Analysis Plans Have Limited Upside, Especially Where Replications Are Feasible," *Journal of Economic Perspectives* 29(3):81–98, doi 10.1257/jep.29.3.81** ([Stanford PDF](https://web.stanford.edu/~niederle/Coffman.Niederle.PAP.JEP.pdf)).

Their three-part case, verbatim (p. 82): "First, recent empirical literature suggests the behavioral problems that pre-analysis plans attenuate are not a pervasive problem in experimental economics. Second, pre-analysis plans have quite limited value in cases where more than one hypothesis is tested, piloted, or surveyed, and also where null results may not be reported. However, in very costly one-of-a-kind field experiments... they can be valuable. Third, pre-analysis plans may discourage the use of novel research designs and hence inhibit studies of robustness of previous findings."

Supporting statements: "Contrary to popular belief, pre-analysis plans do not always offer dramatic decreases in the false positive rate" (p. 96); "Without the autonomy to reoptimize research after it has begun, working in areas with many unknowns becomes a risky endeavor" (p. 88); "Results from known designs will be less surprising on average, lending themselves more readily to a pre-committed analysis plan, but also reducing what we learn about the context-specificity of the original result" (p. 89); on p-hacking evidence, "With 122 papers in their dataset for experimental papers, they are not able conclude at a suitable level of statistical significance that this group of papers exhibits signs of p-hacking" (p. 83). Their scope conclusion (p. 96): "if pre-analysis plans have a downside, like inhibiting exploratory work, or placing a greater burden on young and less-experienced researchers, the results suggest pre-analysis plans should be limited to costly, one-time studies," while "pre-analysis plans are likely a great tool for replication studies."

Note their own caveats, which cut the other way (p. 84): "the dataset comes from the top three journals in economics. Perhaps p-hacking is more pervasive elsewhere," and "experimental economists may have other tools at their disposal for producing false positives, just not the tools that are targeted by pre-analysis plans."

**(c) Discipline-internal critiques in political science**, quoted by Monogan (2015) and therefore attributable via a fetched source: Anderson (2013) — registration "is most useful for studies that collect original data; however, in the analysis of historical data, preregistering cannot send as clear a signal," and "With historical data, a scholar may have glimpsed the data before the study registration"; Gelman (2013) — "it would be problematic if preregistration led to robotic data analysis in which the simple evaluation of hypotheses came at the expense of broader data exploration"; Laitin (2013) — "many of the most important developments in knowledge came from inductive findings," and he "is concerned that overzealous support for preregistration might lead to the perception that nonregistered studies are inferior" ([Cambridge / *PS*](https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/research-preregistration-in-political-science-the-case-counterarguments-and-a-response-to-critiques/E80124ED16BA47D0EA09F03D72B89EC7)).

**Further critiques located but not fetched** (not quoted anywhere above): qualitative-research critique https://pmc.ncbi.nlm.nih.gov/articles/PMC6840388/ ; Haven & Van Grootel https://repository.tilburguniversity.edu/server/api/core/bitstreams/a48f413d-6c68-4e53-965d-fa8672104020/content ; "Preregistration Is Neither Sufficient nor Necessary for Good Science" https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3747616 ; PAP stocktaking https://eprints.lse.ac.uk/112747/1/pre_analysis_plans_an_early_stocktaking.pdf ; "In Praise of Moderation" https://economics.mit.edu/sites/default/files/publications/InPraise.pdf .

Sources: https://economics.mit.edu/sites/default/files/publications/JEP%20Analysis%20Plans%20Final.pdf · https://web.stanford.edu/~niederle/Coffman.Niederle.PAP.JEP.pdf · https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/research-preregistration-in-political-science-the-case-counterarguments-and-a-response-to-critiques/E80124ED16BA47D0EA09F03D72B89EC7

---

### 4.4 Political science / IR specific guidance (Monogan; journal and registry practice)

**(a) James E. Monogan III, "A Case for Registering Studies of Political Outcomes: An Application in the 2010 House Elections," *Political Analysis* 21(1):21–37, Winter 2013** (Symposium on Research Registration; Copyright © The Author 2013, published by Oxford University Press on behalf of the Society for Political Methodology) ([Cambridge Core](https://www.cambridge.org/core/journals/political-analysis/article/case-for-registering-studies-of-political-outcomes-an-application-in-the-2010-house-elections/770DCBB446A520A9DF17395E94901E27)). The fetched landing page confirms the citation but did not expose the abstract or body, so the paper's specific argument and the details of the 2010 House elections application are `n.a.` from primary text here; the substantive positions are recoverable from Monogan (2015), which restates them.

**(b) James E. Monogan III, "Research Preregistration in Political Science: The Case, Counterarguments, and a Response to Critiques," *PS: Political Science and Politics* (2015)** ([Cambridge Core](https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/research-preregistration-in-political-science-the-case-counterarguments-and-a-response-to-critiques/E80124ED16BA47D0EA09F03D72B89EC7)). Volume/issue/pages/DOI were not stated on the fetched page (`n.a.`).

Definition: "Registering a study means that before observing outcome data, researchers craft and publicly release their plan for data analysis that they believe will offer the most honest means of testing a hypothesis."

The four causes of publication bias preregistration can restrain, after Gerber and Malhotra (2008, 314): "a journal's rejection of null findings, an author's self-selecting to submit only those studies with significant results, an author's expansion of samples after failing significance tests, and an author's search for specifications that generate significant results."

Enumerated concerns and Monogan's responses:

| Concern | Monogan's response |
|---|---|
| Less informative for historical/existing data — "In any study using existing information, whether past surveys, time series of economic data, or historical records, authors unfortunately cannot provide proof that they did not glance at the information beforehand" | "it is critical in any registration regime that scholars have the option to briefly explain why preregistering their study would not be effective" |
| Could reduce data exploration (Gelman) | "it does not necessarily preclude such activity"; "reporting auxiliary findings from data should be encouraged—provided that the central hypothesis is evaluated using the registered design"; describe extra results "as observations from data—rather than hypothesis tests" |
| Cannot substitute for replication materials (Anderson) | "Study registration should not replace the sharing of replication data but rather enhance it"; "preregistration symbiotically supports the sharing of replication information" |
| Field research faces unforeseen contextual problems; "Requiring political scientists to anticipate all contingencies could be unreasonable" | "there may be legitimate reasons why the initial plan was altered"; registries could "rate a study's compliance with its design," and "it would be essential for studies with well-reasoned justifications for deviation to be regarded as highly as those with no deviation whatsoever" |
| May make finding true positives harder — a preregistered linear specification whose diagnostics demand nonlinearity yields misleading results, and "inaccurate functional forms can produce false-negative findings" | "registration is not a permit to work wearing blinders"; deviations acceptable "if the findings of the original design are reported with justification for the changes (Monogan 2013, 24–5)"; put "the original estimates and the justification on the registry page" |
| Non-registered studies may be seen as inferior (Laitin) | "No policy should threaten the diversity of the discipline's studies" |

Monogan's own scope judgement — directly relevant to a long-horizon IR forecasting paper. **Low value:** "Theory-building projects, whether positive or normative"; "Studies using big data," particularly using "existing information" or aiming "to learn inductively"; studies using "past surveys," "time series of economic data," or "historical records." **High value:** "Deductive studies that test one or a few hypotheses using original data"; "Policy studies"; "Studies of election returns"; lab studies; and cases where researchers "plan to study an upcoming election."

That last category is the pivot for this project: a study whose outcome variable has *not yet been realised* — a forecast — sits in Monogan's high-value class even though its data are observational, because the glimpsing objection does not apply to the future.

**(c) Journal policy / EGAP.** No journal preregistration policy document or EGAP registry page was fetched in this session, so those specifics are `n.a.` Monogan (2015) does note that "For journals that implement preregistration procedures, the online appendix accompanying this article lists several proto-registries," that editors "could give authors the option of submitting a research design before the outcome variable is observed, which would allow *pre-acceptance* of an article before seeing the results," and that "some third-party registries allow investigators' names to remain temporarily anonymous" under double-blind review.

Sources: https://www.cambridge.org/core/journals/political-analysis/article/case-for-registering-studies-of-political-outcomes-an-application-in-the-2010-house-elections/770DCBB446A520A9DF17395E94901E27 · https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/research-preregistration-in-political-science-the-case-counterarguments-and-a-response-to-critiques/E80124ED16BA47D0EA09F03D72B89EC7

---

### 4.5 Pre-registering FORECASTS, and how forecast pre-registration is judged

**(a) A worked precedent: the Forecasting Collaborative.** "Insights into the accuracy of social scientists' forecasts of societal change," *Nature Human Behaviour* 7(4):484–501, 9 Feb 2023, doi 10.1038/s41562-022-01517-1 ([PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC10192018/); journal record via [Monash](https://research.monash.edu/en/publications/insights-into-the-accuracy-of-social-scientists-forecasts-of-soci/) *(secondary)*).

How the forecasts were preregistered — the operational template: "The forecasts of all participating teams along with their rationales were pre-registered on the Open Science Framework (https://osf.io/6wgbj/registrations)." The *evaluation rule* was also fixed in advance, separately and earlier: "in an a priori specific document shared with the journal in April 2020, we outlined the operationalization of the key dependent variable (MASE), the operationalization of the covariates and benchmarks (that is, the use of naive forecasting methods), and the key analytic procedures... (https://osf.io/7ekfm)." Teams lodged forecast values, models, "the type of model computed, such as time series, game theoretic models or other algorithms," model parameters, exogenous variables, "underlying assumptions," and team composition.

Design: Tournament 1, N = 86 teams / 359 forecasts, 12 monthly forecasts May 2020–April 2021 against 39 months of history (Jan 2017–Mar 2020); Tournament 2, N = 120 teams / 546 forecasts over 6 months against 45 months of history.

Scoring rule: "to determine forecasting accuracy across domains, we examined the mean absolute scaled error (MASE) across forecasted time points for each domain." Definition and interpretation, verbatim: "The MASE is an asymptotically normal, scale-independent scoring rule that compares predicted values against the predictions of a one-step random walk"; "Because it is scale independent, it is an adequate measure when comparing accuracy across domains on different scales"; "A MASE of 1 reflects a forecast that is as good out of sample as the naive one-step random walk forecast is in sample"; "A MASE below 1.76 is superior to median performance in prior large-scale data science competitions." Log-transformed MASE was used "to correct for right skew." The explicit algebraic formula was not on the fetched page (`n.a.`; deferred to Supplementary Information).

Benchmarks, all pre-specified: (1) historical mean by resampling; (2) "a naive random walk, calculated by randomly resampling historical change in the time series data with an autoregressive component"; (3) "extrapolation from linear regression, based on a randomly selected interval of the historical time series data"; plus a lay-crowd benchmark (N = 802) and the M4-competition median (MASE 1.76).

Headline results — the reason this is the right precedent to cite: "social scientists' forecasts were on average no more accurate than those of simple statistical models... or the aggregate forecasts of a sample from the general public." In Tournament 1 they beat all three naive benchmarks in only **1 of 12** domains, and "in most domains, at least one naive forecasting method produced errors comparable to or less than those of social scientists" — **11 of 12** domains in Tournament 1 and **8 of 12** in Tournament 2. Winning teams were still worse than in-sample random walks in **8 of 12** domains in Tournament 1. And on calibration: "Experts' subjective confidence in their forecasts was not related to the accuracy of their estimates"; "publication track record on a topic, rather than subjective confidence in domain expertise or confidence in the forecast, contributed to greater accuracy"; "It is possible that subjective confidence in domain expertise conflates expertise and overconfidence (versus intellectual humility)." Updating did not help: "This observation suggests that updating did not lead to more accurate forecasts."

**(b) Scoring rules, formally.** Tilmann Gneiting & Adrian E. Raftery, "Strictly Proper Scoring Rules, Prediction, and Estimation," *Journal of the American Statistical Association*, March 2007, Vol. 102, No. 477, Review Article, pp. 359–378, doi 10.1198/016214506000001437 ([author PDF](https://sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jasa.pdf)).

| Concept | Definition (verbatim / formula) | Page |
|---|---|---|
| Scoring rule | "A scoring rule is any extended real-valued function \(S:\mathcal{P}\times\Omega\to\mathbb{R}\) such that \(S(P,\cdot)\) is \(\mathcal{P}\)-quasi-integrable for all \(P\in\mathcal{P}\)." Expected score \(S(P,Q)=\int S(P,\omega)\,dQ(\omega)\) | pp. 359–360 |
| Proper | "The scoring rule \(S\) is proper relative to \(\mathcal{P}\) if \(S(Q,Q)\ge S(P,Q)\) for all \(P,Q\in\mathcal{P}\)" | p. 360 |
| Strictly proper | "It is strictly proper relative to \(\mathcal{P}\) if (1) holds with equality if and only if \(P=Q\), thereby encouraging honest quotes by the forecaster" | p. 360 |
| Brier / quadratic score | \(S(p,i)=-\sum_{j=1}^{m}(\delta_{ij}-p_j)^2=2p_i-\sum_j p_j^2-1\), with divergence \(d(p,q)=\sum_j (p_j-q_j)^2\). "This well-known scoring rule was proposed by Brier (1950)." | p. 363 |
| Logarithmic score | \(S(p,i)=\log p_i\), from negative Shannon entropy \(G(p)=\sum_j p_j\log p_j\), divergence = Kullback–Leibler \(d(p,q)=\sum_j q_j\log(q_j/p_j)\). "This scoring rule dates back at least to Good (1952)." | p. 363 |
| CRPS | \(\mathrm{CRPS}(F,x)=-\int_{-\infty}^{\infty}\left(F(y)-\mathbf{1}\{y\ge x\}\right)^2 dy\), "corresponds to the integral of the Brier scores for the associated binary probability forecasts at all real-valued thresholds" | p. 367 |

The propriety property is the load-bearing one for a pre-registered forecast: a strictly proper rule makes honest reporting of the predictive distribution the unique optimum, which is exactly what a pre-registered threshold-crossing claim needs if it is to be more than rhetoric.

Sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC10192018/ · https://research.monash.edu/en/publications/insights-into-the-accuracy-of-social-scientists-forecasts-of-soci/ · https://sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jasa.pdf

---

## SECTION 5 — Peaking-power / power-transition literature

### 5.1 Beckley & Brands on the "peaking power trap" — exact claim and mechanism

The peaking-power trap is presented explicitly as a *replacement* for the Thucydides Trap, and the substitution is definitional, not decorative. Brands and Beckley write: "The idea of a Thucydides Trap, popularized by Harvard political scientist Graham Allison, holds that the danger of war will skyrocket as a surging China overtakes a sagging America," and then: "The only problem with this familiar formula is that it's wrong." Their alternative: "It's best thought of instead as a 'peaking power trap.'" ([Brands & Beckley, *Foreign Policy*, 24 Sep 2021](https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf))

| Element | Verbatim claim | Source |
|---|---|---|
| Population of cases | "Over the past 150 years, peaking powers—great powers that had been growing dramatically faster than the world average and then suffered a severe, prolonged slowdown—usually don't fade away quietly. Rather, they become brash and aggressive." | [Foreign Policy](https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf) |
| Core mechanism claim | "The most dangerous trajectory in world politics is a long rise followed by the prospect of a sharp decline." | [Foreign Policy](https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf) |
| Formal definition | Peaking powers are "rising powers whose economic booms have slowed but not yet stopped." | [Beckley, *International Security* 48(1)](https://direct.mit.edu/isec/article/48/1/7/117122/The-Peril-of-Peaking-Powers-Economic-Slowdowns-and) |
| Why peaking beats rising or declining | "Peaking powers, by contrast, have the means and the motive to expand aggressively." | [Beckley, *IS* 48(1)](https://direct.mit.edu/isec/article/48/1/7/117122/The-Peril-of-Peaking-Powers-Economic-Slowdowns-and) |
| Behavioural channel | "The most common reaction to slowing growth is mercantilist expansion: the use of state power to carve out economic spheres of influence"; psychological channel is "threat inflation, loss aversion, and overconfidence in one's own capabilities." | [Beckley, *IS* 48(1)](https://direct.mit.edu/isec/article/48/1/7/117122/The-Peril-of-Peaking-Powers-Economic-Slowdowns-and) |
| Conditioning variables | "two main factors shape the extent to which a rising power resorts to mercantilist expansion during an economic slowdown: (1) the rising power's regime type, and (2) its prospects for future trade"; "The most aggressive mercantilist expanders were stagnating autocracies confronted by growing international protectionism"; democratic institutions are "shock absorbers for aggressive urges." | [Beckley, *IS* 48(1)](https://direct.mit.edu/isec/article/48/1/7/117122/The-Peril-of-Peaking-Powers-Economic-Slowdowns-and) |

**The coding rule is the methodologically important part**, and it is unusually explicit for this literature — a quantitative, pre-stated case-selection criterion of exactly the kind Allison's project lacks (see 5.5):

> "I analyze every case from 1870 to 2018 in which a great power's per capita gross domestic product (GDP) grew at least twice as fast as the global average for at least seven years and then suffered at least a 50 percent decline in growth rates over the next seven years." — wartime downturns excluded; "This exclusion leaves nine cases" ([Beckley, *IS* 48(1)](https://direct.mit.edu/isec/article/48/1/7/117122/The-Peril-of-Peaking-Powers-Economic-Slowdowns-and))

| # | Case (onset year of slowdown) |
|---|---|
| 1 | United States 1882 |
| 2 | Russia 1899 |
| 3 | Japan 1922 |
| 4 | France 1925 |
| 5 | USSR 1926 |
| 6 | Germany 1927 |
| 7 | Japan 1970 |
| 8 | Russia 2007 |
| 9 | China 2012 |

Three of the nine (interwar France, Germany, USSR) are not examined in detail because "mercantilist expansion was arguably overdetermined in those cases" ([Beckley, *IS* 48(1)](https://direct.mit.edu/isec/article/48/1/7/117122/The-Peril-of-Peaking-Powers-Economic-Slowdowns-and)). So the load-bearing evidentiary base is **n≈5–6 cases**, which is directly relevant to the identification/power problem recorded in the Phase 2 file: a nine-case universe cannot discipline a multi-parameter causal claim, and the author's own exclusions cut it further.

Full citation: Michael Beckley, "The Peril of Peaking Powers: Economic Slowdowns and Implications for China's Next Decade," *International Security* 48, no. 1 (Summer 2023), 7–46, https://doi.org/10.1162/isec_a_00463 ([Belfer Center recommended citation](https://www.belfercenter.org/publication/peril-peaking-powers-economic-slowdowns-and-implications-chinas-next-decade)). Replication material: [Harvard Dataverse doi:10.7910/DVN/PDYVY2](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/PDYVY2).

Sources: https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf · https://direct.mit.edu/isec/article/48/1/7/117122/The-Peril-of-Peaking-Powers-Economic-Slowdowns-and · https://www.belfercenter.org/publication/peril-peaking-powers-economic-slowdowns-and-implications-chinas-next-decade · https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/PDYVY2

### 5.2 The specific indicators used to argue China is a peaking power

Every number below is drawn from the two Beckley/Brands primaries. Note the measurement heterogeneity: official statistics, a private-sector productivity estimate, a bank's incremental-capital-output ratio, UN-style demographic projections, and a market-capitalisation event study are pooled into a single directional verdict without any stated aggregation rule or uncertainty interval.

| Dimension | Indicator and value | Source of the number as stated | URL |
|---|---|---|---|
| Headline growth | Official growth fell from "14 percent" (2007) to "6 percent" (2019) | Official Chinese statistics | [FP 2021](https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf) |
| Growth (adjusted) | "rigorous studies suggest the true growth rate is now closer to 2 percent" | unnamed "rigorous studies" | [FP 2021](https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf) |
| Productivity | Total factor productivity "declined 1.3 percent every year on average between 2008 and 2019" | The Conference Board | [FP 2021](https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf) |
| Productivity (restated) | "productivity turned negative" | — | [IS 48(1)](https://direct.mit.edu/isec/article/48/1/7/117122/The-Peril-of-Peaking-Powers-Economic-Slowdowns-and) |
| Capital efficiency | "it takes three times as many inputs to produce a unit of growth today as it did in the early 2000s" | DBS Bank | [FP 2021](https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf) |
| Debt | "total debt surged eight-fold between 2008 and 2019 and exceeded 300 percent of GDP prior to COVID-19" | — | [FP 2021](https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf) |
| Debt (restated) | "debt ballooned more than eight-fold"; "Chinese firms and local governments took out an astounding $29 trillion in new credit" (2008–2018) | — | [IS 48(1)](https://direct.mit.edu/isec/article/48/1/7/117122/The-Peril-of-Peaking-Powers-Economic-Slowdowns-and) |
| Demography (dividend) | Historic ratio of "10 working-age adults for every senior citizen" vs roughly 5 for most major economies | — | [FP 2021](https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf) |
| Demography (projection) | "From 2020 to 2050, it will lose an astounding 200 million working-age adults … and gain 200 million senior citizens" | — | [FP 2021](https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf) |
| Fiscal consequence | Medical and social-security spending must "triple as a share of GDP, from 10 percent to 30 percent, by 2050" | — | [FP 2021](https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf) |
| Industrial capacity | "substantial excess industrial capacity" | — | [IS 48(1)](https://direct.mit.edu/isec/article/48/1/7/117122/The-Peril-of-Peaking-Powers-Economic-Slowdowns-and) |
| Tech-sector valuation | ">$1 trillion erased from market capitalization of China's leading tech firms" | — | [FP 2021](https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf) |
| Strategic encirclement | Taiwan, Japan, Vietnam/Indonesia, Australia, India, EU as "systemic rival", the Quad, AUKUS | — | [FP 2021](https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf) |
| Chinese elite perception | Yan Xuetong quoted that the US "multilateral club strategy" is "isolating China" | Yan Xuetong | [FP 2021](https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf) |
| Growth (IS restatement) | Growth "dropped by roughly half" in the 2010s | — | [IS 48(1)](https://direct.mit.edu/isec/article/48/1/7/117122/The-Peril-of-Peaking-Powers-Economic-Slowdowns-and) |

Sources: https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf · https://direct.mit.edu/isec/article/48/1/7/117122/The-Peril-of-Peaking-Powers-Economic-Slowdowns-and

### 5.3 Published rebuttals and sceptical responses

Three distinct lines of attack, of which the third is the one that matters most for a measurement paper.

**(a) The measurement critique — "peak" is undefined.** Evan S. Medeiros, "The Delusion of Peak China," *Foreign Affairs*: "First, it is difficult to measure and understand what peak China means in practice. Is it an absolute term or a relative one—and if the latter, relative to what? It is unclear whether the term takes into account U.S. power or Xi's perception of it." He adds the multi-dimensionality point directly: "Also, China could peak in one area but advance in others, complicating the calculation," and "Is Chinese power waning if its economy underperforms but its military modernizes and its diplomacy generates influence? China peaking economically is not the same as China peaking geopolitically—a distinction lost on many advocates of the peak China argument." His summary judgement: "In short, either China is not peaking—or the idea of peak China doesn't explain much about the challenges posed by China in the twenty-first century." ([Medeiros, *Foreign Affairs*](https://www.foreignaffairs.com/china/delusion-peak-china-united-states-evan-medeiros)) This is a scalar-index critique in all but name: a single "peak" verdict is not well defined over a vector of heterogeneous capability dimensions.

**(b) The mechanism critique — the causal channel requires unobserved elite beliefs.** Ryan Hass, "Organizing American Policy Around 'Peak China' is a Bad Bet": "Proponents of 'peak China theory' treat the country as an inanimate object that is being blown off course by immutable historic forces … Such analyses overlook the fact that China has agency." The falsification demand is stated crisply: "If any forecast of China acting as a peaking power is to hold explanatory value, there must be evidence that China's leaders accept the diagnosis of their current condition and feel an urgency to act before their moment at the apex of national power passes. In the case of China today, no such evidence is available, at least not in the public record." Hass lists five policy risks: skewed forecasts of Chinese behaviour ("presuming that virtually every Chinese action represents a prelude to war"), provoking aggression by exploiting perceived weakness (citing M. Taylor Fravel), a Taiwan policy dilemma, inducing public pushback that produces a rally-round-the-flag effect, and "overreaction to current challenges and underweight preparation for the long-term nature of U.S.-China competition." ([Hass, prcleader.org](https://www.prcleader.org/post/organizing-american-policy-around-peak-china-is-a-bad-bet))

**(c) The "irrelevant to polarity" critique — thresholds, not trajectories.** Jennifer Lind, "Back to Bipolarity: How China's Rise Transformed the Balance of Power," *International Security* 49, no. 2, p. 7: "I argue that regardless of slowing growth, and regardless of whether it overtakes the United States, China is already capable of engaging in a serious security competition with it," and "Barring domestic political upheaval, China will remain a great power and a formidable geopolitical competitor into the foreseeable future." On the middle-income-trap version of the peaking argument: "China's future as a great power does not depend on a successful transition to the high-income category," and "The Soviet Union never reached the high-income level but was nonetheless a profoundly dangerous superpower competitor." On the growth slowdown itself: "China's economic slowdown was both predictable and predicted … Such a transition would reflect a success, not a failure, for China," with the relevant question being "whether China will successfully settle into a sustainable range of 1–2 percent growth." Her diagnosis of the framing error: "a key insight of this article is that 'catching up' or 'overtaking' are the wrong benchmarks." ([Lind, *IS* 49(2)](https://direct.mit.edu/isec/article/49/2/7/125214/Back-to-Bipolarity-How-China-s-Rise-Transformed))

Lind's paper is doubly useful here because it is *also* a rebuttal to Section 1's indices, and it does the empirical work rather than asserting it. She validates metrics against historian-generated great-power lists for 1820–1990, generating 76 economic and 92 military dyad-decades, and derives "normal ranges" (2nd–3rd quartiles) and medians:

| Metric | Normal range for great powers | Median | China's 2023 value |
|---|---|---|---|
| GDP ratio to leading state | 17–45% | 27% | 130% |
| GDP per capita ratio | 38–70% | 59% | n.a. (reported as "low", value not stated on page) |
| Composite (GDP × GDP p.c.) ratio | 8–28% | 15% | 36% |
| Military expenditure ratio | 23–105% | 48% | 32% |
| Military personnel ratio | 88–267% | 175% | 153% |

All values from [Lind, *IS* 49(2)](https://direct.mit.edu/isec/article/49/2/7/125214/Back-to-Bipolarity-How-China-s-Rise-Transformed). Her verdict on GDP per capita — the multiplicand in Beckley's own index (§1.2) — is the sharpest measurement finding in the set: "GDP per capita, which is commonly referenced in debates about great power, is not a sound metric for this purpose"; "GDP per capita shows significant overlap among great powers, middle powers, and all non–great powers"; "the metric offers a national average, which obscures a country's highest level of technological performance"; "GDP per capita is a flawed metric both logically and (as this article shows) empirically." Her CINC critique is quoted in full in §1.1's counterpart material: "CINC codes the Soviet Union as overtaking U.S. power in the 1970s—just as the Soviet Union's failure to keep up with the technological cutting edge was accelerating its decline"; "CINC also ranks India in 2007 as the world's third-largest power, far ahead of France, Germany, and the United Kingdom; again, few experts would endorse this coding."

Sources: https://www.foreignaffairs.com/china/delusion-peak-china-united-states-evan-medeiros · https://www.prcleader.org/post/organizing-american-policy-around-peak-china-is-a-bad-bet · https://direct.mit.edu/isec/article/49/2/7/125214/Back-to-Bipolarity-How-China-s-Rise-Transformed

### 5.4 Power transition theory foundations: Organski and Kugler

Primary text fetched: Jacek Kugler & A.F.K. Organski, "The Power Transition: A Retrospective and Prospective Evaluation," *Handbook of War Studies*, pp. 172–194 ([full text PDF](http://slantchev.ucsd.edu/courses/pdf/Kugler%20&%20Organski%20-%20The%20Power%20Transition.pdf)). Editor, publisher and year are not stated on the fetched pages → **n.a.** *The War Ledger* (Organski & Kugler 1980) itself was not obtained, so no claim below is sourced to that volume.

**Core propositions.** The theory posits a hierarchy — dominant nation, great powers, middle powers, small powers — with two determinants of war: relative power and satisfaction. "Satisfaction with the way goods are distributed in the international order is the second critical determinant" (p. 173); "dissatisfaction with the status quo is an essential precondition for conflict" (p. 186). On the distribution of power: "instability is likely only during periods of relative parity" (p. 175), and the central conjunction claim, "the necessary but not sufficient conditions for major war emerge only in the rare instances when power parity is accompanied by a challenger overtaking a dominant nation" (p. 179). On sequencing: "the challenger did not attack before but only after it had surpassed the power of the dominant country" (p. 183); "in each case the conflict started after and not before the parity point" (p. 183). And on the null side, "Major war, however, was never waged in the past 100 years when the dominant power was preponderant" (p. 180). All page-cited to [Kugler & Organski](http://slantchev.ucsd.edu/courses/pdf/Kugler%20&%20Organski%20-%20The%20Power%20Transition.pdf).

**The entire empirical base — Table 7.1, "Great Powers, Power Distribution, and Major War, 1860–1980" (p. 179):**

| Condition | No war | War | % no war | % war |
|---|---:|---:|---:|---:|
| Preponderance | 4 | 0 | 100% | 0% |
| Parity, no transition | 6 | 0 | 100% | 0% |
| Parity **and** transition | 5 | 5 | 50% | 50% |

Twenty dyad-periods, of which the theory's signature cell contains ten. A 5/5 split in a ten-observation cell is the whole quantitative warrant. Source: [Kugler & Organski, p. 179](http://slantchev.ucsd.edu/courses/pdf/Kugler%20&%20Organski%20-%20The%20Power%20Transition.pdf).

**How power is operationalised.** Explicitly, and scalar:

| Formulation | Verbatim | Page |
|---|---|---|
| Original | "Power = Economic Productivity per Capita x Population" | p. 190 |
| Chosen proxy | "The gross national product (GNP) was the measure chosen because it combined the demographic and economic aspects of a nation's productivity" | pp. 190–191 |
| Comparison to CINC-type index | "In empirical tests this parsimonious and robust measure performed as well as the more complex index of power developed by Singer et al. (1972), which included demographic, industrial, and military components" | p. 191 |
| Reformulation | "Power = (Economic Production per Capita x Population) X Relative Political Capacity" | p. 191 |
| RPC definition | RPC "measures the difference between the revenues a government is expected to extract … and the revenues a government is capable of extracting" | p. 191 |

Note the multiplicative structure: Organski & Kugler's product is the direct ancestor of Beckley's GDP × GDP-per-capita (§1.2), and Lind labels that same product the "composite" metric (§5.3). All three are scalar reductions of a two- or three-dimensional vector, and none carries an uncertainty interval. Source: [Kugler & Organski, pp. 190–191](http://slantchev.ucsd.edu/courses/pdf/Kugler%20&%20Organski%20-%20The%20Power%20Transition.pdf).

**Not confirmed from the primary text:** an "80 percent of the dominant nation's GNP" contender threshold, any numerical definition of "parity", and any stated length for the transition window. These are widely attributed to the tradition but do not appear on the fetched pages → **n.a.** (See Gaps.)

Sources: http://slantchev.ucsd.edu/courses/pdf/Kugler%20&%20Organski%20-%20The%20Power%20Transition.pdf

### 5.5 Allison's "Thucydides Trap" and a published methodological critique of case selection

**The project's own statement of scope and method.** The Belfer Center case file states: "The Case File includes all the instances we have been able to find in the past 500 years in which a major rising power threatened to displace a ruling power." Sixteen cases, twelve wars: "In fact, four of the sixteen cases in the Case File did not result in war." On selection bias, the project's defence is a universe-of-cases claim: "Because this includes the entire universe of the cases (as opposed to a representative sample), the Case File is immune to charges of selection bias." It simultaneously concedes the case list is not closed: "The Thucydides's Trap Case File is open … this website has invited readers to suggest additional cases." It disclaims determinism — "Thucydides's Trap does not claim that war is inevitable" — and disclaims any timing prediction: "The Thucydides's Trap hypothesis makes no claim about a moment when war will most likely occur." ([Belfer Center case file](https://www.belfercenter.org/programs/thucydidess-trap/thucydidess-trap-case-file)) Critically, the page **provides no operational definition of "rising power" or "ruling power"** beyond that prose.

**The critique.** Richard Hanania, "Graham Allison and the Thucydides Trap Myth," *Strategic Studies Quarterly* 15, no. 4 (Winter 2021): 14–24 ([PDF](https://www.airuniversity.af.edu/Portals/10/SSQ/documents/Volume-15_Issue-4/SC-Hanania.pdf)). Hanania quotes Allison's criterion — "a rising power threatened to displace a major ruling power," where "these histories use 'rise' and 'rule' as conventionally defined, along with synonyms emphasizing rapid shifts in relative economic and military strength" (p. 18) — and then dismantles it.

| Defect | Verbatim critique | Page |
|---|---|---|
| Undefined terms | "Nearly every substantive word in these sentences is ill-defined." / "We are not told what the 'conventional' definitions of 'rise' and 'rule' are." | p. 18 |
| No time window | "The term 'rapid shift' in the context of geopolitics can mean anything from one or two years to several decades." | p. 18 |
| No measurement specification | "how exactly are economic and military strength measured, and how large does the shift have to be?" / "Is economic strength measured by GDP, or does the calculation also consider the production of militarily important sectors such as steel?" / "is military strength actual or potential?" | p. 18 |
| No stated data source | "Scholars have compiled empirical measures of these things, but Allison provides no details about which measures he used, if any." | p. 18 |
| Threshold indeterminacy | "We have no way of determining whether a 20 percent reduction in the GDP gap between two powers over 10 years would count as one of his cases or whether the same reduction over 20 or even 50 years would." | p. 18 |
| Unmeasured intentions | "what does 'threaten to displace' mean? … Does it account for the intentions of each side, and if so, how are those measured?" | p. 18 |
| Ad hoc selection | "The selection process seems to be completely anecdotal." / "Throughout his data set, it is unclear why Allison includes certain cases but omits others." | p. 18 |
| Universe not determinate | "The Thucydides's Trap Project website indicates 14 more cases are being considered for inclusion in the data set." / "Without clearer definitions of what is being measured, the lesson is that one cannot determine which cases should be included." | p. 20 |
| Endogeneity | "Allison collects cases based on one side threatening another; consequently, his analysis is biased by the fact he selects countries that are antagonists and then checks how often they find themselves at war." | p. 21 |
| No controls | "Allison conducts a bivariate analysis in which one independent variable predicts a dependent variable." / "Nor is there any attempt to account for omitted variables, even in the simple form of dividing the data by historical era." | pp. 19, 22 |
| Time as omitted variable | "Perhaps the most important omitted variable Allison does not consider is time." / "Do international relations in the sixteenth century have anything to say to the twenty-first century …?" | p. 19 |

Hanania's quantitative counter-analysis is a robustness exercise on the case set rather than a new model:

| Specification | War / total | Implied rate | Page |
|---|---:|---:|---|
| Allison's published set | 12 / 16 | 75% ("around a 75 percent chance the United States and China will go to war") | p. 16 |
| Including the 14 cases under consideration | 19 / 30 | 63% ("the results would have looked much less impressive") | p. 20 |
| Second half of the 20th century onward | 1 / 7 | 14% | p. 20 |
| Same, adding the US–China dyad | 1 / 8 | 12.5% | p. 20 |

He concedes the sample size is not itself the problem — "a study with 16 observations can be valuable if it is well designed … if the methodology were sound, 12 cases of armed conflict out of 16 observations would pass conventional tests of significance" (p. 17) — which localises the failure precisely in coding rules and case selection, not in n. His prescription is the pre-registration-shaped one: any such analysis "must clarify the standards of inclusion; consider other variables that might influence the likelihood of war; and avoid endogeneity problems that conflate the dependent variable and the independent variable of interest" (p. 22). All from [Hanania, *SSQ* 15(4)](https://www.airuniversity.af.edu/Portals/10/SSQ/documents/Volume-15_Issue-4/SC-Hanania.pdf).

Sources: https://www.belfercenter.org/programs/thucydidess-trap/thucydidess-trap-case-file · https://www.airuniversity.af.edu/Portals/10/SSQ/documents/Volume-15_Issue-4/SC-Hanania.pdf

### 5.6 Techno-industrial dimensions: is China's relative position rising or falling?

The peaking-power indicators in §5.2 are macro-financial and demographic. On techno-industrial dimensions measured directly, the direction of travel over the same period is the opposite. This divergence is the empirical case for a capability *vector*: a scalar index must either average these against the debt and demography series — with an unstated weighting rule — or suppress one of them.

| Dimension | Metric | Value | Direction | Source |
|---|---|---|---|---|
| Electricity generation (scale) | China's electricity demand, 2025 | "10,573 TWh in 2025, accounting for a third of global electricity demand"; "nearly doubled from 5,802 TWh in 2015" | Rising | [Ember, *Global Electricity Review 2026*](https://ember-energy.org/latest-insights/global-electricity-review-2026/major-countries-and-regions/) |
| Electricity (build rate) | Share of global additions, 2025 | "China accounted for 58% of global solar installations (378 GW (DC)) and 72% of global wind installations (119 GW)" | Rising | [Ember GER 2026](https://ember-energy.org/latest-insights/global-electricity-review-2026/major-countries-and-regions/) |
| Electricity (mix quality) | Coal share of Chinese generation | "fell from 70% in 2015 to 54% in 2025"; fossil share 58% in 2025 vs global average 57% | Improving / converging | [Ember GER 2026](https://ember-energy.org/latest-insights/global-electricity-review-2026/major-countries-and-regions/) |
| Electricity (inflection) | Fossil generation change, 2025 | "China's fossil generation declined by 56 TWh (-0.9%) in 2025"; "the first year since 2015 without an increase"; coal −71 TWh (−1.2%), gas +14 TWh (+4.3%) | Structural shift | [Ember GER 2026](https://ember-energy.org/latest-insights/global-electricity-review-2026/major-countries-and-regions/) |
| Electricity (residual scale of coal) | China's share of global coal generation | coal generation "remained high at 5,757 TWh in 2025, accounting for 55% of global coal generation" | Still dominant | [Ember GER 2026](https://ember-energy.org/latest-insights/global-electricity-review-2026/major-countries-and-regions/) |
| Grid / transmission | China T&D investment | "USD 88 billion in transmission and distribution investment in 2025" | Rising | [IEA, *World Energy Investment 2025* — China](https://www.iea.org/reports/world-energy-investment-2025/china) |
| Grid (global denominator) | Global grid investment | "Each year, some USD 400 billion is now spent on grids worldwide" — i.e. China ≈ 22% of the global total on these two IEA figures | Rising share | [IEA WEI 2025 — Executive summary](https://www.iea.org/reports/world-energy-investment-2025/executive-summary) |
| Clean-energy investment | China's clean-energy investment | "In 2024 China's clean energy investment was more than USD 625 billion, almost doubling since 2015" | Rising | [IEA WEI 2025 — China](https://www.iea.org/reports/world-energy-investment-2025/china) |
| Energy investment (relative) | China's global position | "China is the largest global energy investor by a wide margin, and its share of global clean energy investment has risen from a quarter ten years ago to almost one-third today" | Rising | [IEA WEI 2025 — Executive summary](https://www.iea.org/reports/world-energy-investment-2025/executive-summary) |
| Industrial robotics (stock) | Operational stock, 2024 | "China recorded a world record of 2,027,000 industrial robots working in factories"; "The robot stock doubled within three years, surpassing 1 million units in 2021" | Rising | [IFR, *World Robotics 2025* — China release](https://ifr.org/downloads/press_docs/2025-09-25-IFR_press_release_China_in_English.pdf) |
| Industrial robotics (flow) | Installations, 2024 | "Annual installations hit 295,000 units in 2024. This was up 7% … representing 54% of global demand" | Rising | [IFR press release](https://ifr.org/downloads/press_docs/2025-09-25-IFR_press_release_China_in_English.pdf) |
| Robotics (supply-chain localisation) | Domestic supplier share | "For the first time, Chinese manufacturers sold more than foreign manufacturers at home: The share climbed to 57% across industries in 2024, up from 47% in 2023" | Rising sharply | [IFR press release](https://ifr.org/downloads/press_docs/2025-09-25-IFR_press_release_China_in_English.pdf) |
| Robotics (sectoral dominance) | Sector shares of *global* installations | Textiles/leather/apparel: "China accounted for 95% of installations in this category", all units domestically supplied; wood products: "China represented 91% of global installations" | Rising | [IFR press release](https://ifr.org/downloads/press_docs/2025-09-25-IFR_press_release_China_in_English.pdf) |
| Robotics (global stock share) | China's share of world operational stock | "2,027,190 units represented 43% of the global stock" | Rising | [IFR, *Executive Summary World Robotics 2025 — Industrial Robots*](https://ifr.org/img/worldrobotics/Executive_Summary_WR_2025_Industrial_Robots.pdf) |

Two observations for the methods argument. First, the *sign* of China's trend is dimension-dependent within the same years: debt/GDP and dependency ratios move adversely while electricity, grid capital formation and robot density move favourably. Any scalar index resolves that conflict by fiat. Second, the robotics series shows why level-versus-share matters: China's 54% installation share against a 43% stock share means the stock share is still converging upward, so a snapshot understates the trajectory — an argument for reporting a dimension's level, share and derivative with uncertainty rather than folding it into one number.

Sources: https://ember-energy.org/latest-insights/global-electricity-review-2026/major-countries-and-regions/ · https://www.iea.org/reports/world-energy-investment-2025/china · https://www.iea.org/reports/world-energy-investment-2025/executive-summary · https://ifr.org/downloads/press_docs/2025-09-25-IFR_press_release_China_in_English.pdf · https://ifr.org/img/worldrobotics/Executive_Summary_WR_2025_Industrial_Robots.pdf

---

## Gaps and failures

Every item recorded as `n.a.` or partially confirmed, with what was attempted.

| Item | What is missing | What was tried |
|---|---|---|
| §1.4 Global Firepower | Exact factor list, modifier list and the PwrIndx formula | The methodology page https://www.globalfirepower.com/pwrindx-explained.php returned **404**. Only the country listing page https://www.globalfirepower.com/countries-listing.php was retrievable; it gives ranks and PwrIndx scores but no formula. Recorded `n.a.` |
| §1.5 ECI primaries | No values are quoted from Hidalgo & Hausmann (PNAS 2009), the *Atlas of Economic Complexity* 2013, Tacchella et al. (PLOS ONE) or Mealy et al. | URLs located but the documents were not fetched in this session, so nothing is quoted from them. Listed as located-not-fetched: https://www.pnas.org/doi/10.1073/pnas.0900943106 · https://www.hks.harvard.edu/sites/default/files/centers/cid/files/ATLAS_2013_Part1.pdf · https://journals.plos.org/plosone/article/file?type=printable&id=10.1371/journal.pone.0047278 · https://oms-inet.files.svdcdn.com/production/files/main_feb4.pdf?dm=1553075540 |
| §1.6 / §3 Carroll & Kenkel | Published *AJPS* version consulted at abstract level only | All quoted values come from the working paper https://www.sas.rochester.edu/psc/polmeth/papers/Kenkel_Carroll.pdf ; the published record https://onlinelibrary.wiley.com/doi/abs/10.1111/ajps.12442 was abstract-only |
| §1.6 latent-variable IR measures | Three further candidates confirmed only at abstract level, so not used for values | https://academic.oup.com/jpr/article/56/3/364/8365318 · https://academic.oup.com/jpr/article/57/6/789/8365303 · https://www.cambridge.org/core/journals/political-science-research-and-methods/article/latent-variable-approach-to-measuring-and-explaining-peace-agreement-strength/9184401C70859F5B4EB155F2671D7EBA |
| §3.4 V-Dem measurement model | V-Dem's own hosted PDF unavailable | https://v-dem.net/media/publications/v-dem_working_paper_2016_21.pdf returned **404**; quotations were taken from a SciSpace mirror and are labelled as a secondary host: https://scispace.com/pdf/the-v-dem-measurement-model-latent-variable-analysis-for-1997yaxojn.pdf |
| §4.4 Monogan 2013 | The argument itself and the 2010 House application | The *Political Analysis* landing page https://www.cambridge.org/core/journals/political-analysis/article/case-for-registering-studies-of-political-outcomes-an-application-in-the-2010-house-elections/770DCBB446A520A9DF17395E94901E27 supplied the citation but no abstract or body text. Recorded `n.a.` |
| §4.4 Monogan 2015 (*PS*) | Volume, issue, pages, DOI | Not stated on the fetched page https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/research-preregistration-in-political-science-the-case-counterarguments-and-a-response-to-critiques/E80124ED16BA47D0EA09F03D72B89EC7 . Recorded `n.a.` |
| §4 Hardwicke & Wagenmakers | Treatment of secondary-data/observational research, the preregistration-vs-registered-reports distinction, and stated limitations | Not surfaced by the fetched page https://www.nature.com/articles/s41562-022-01497-2 . Recorded `n.a.` |
| §4.5 Grossmann et al. 2023 | The explicit MASE algebraic formula | Not present on https://pmc.ncbi.nlm.nih.gov/articles/PMC10192018/ . Recorded `n.a.` |
| §4.3 Coffman & Niederle | Publication year | Not stated on the fetched PDF https://web.stanford.edu/~niederle/Coffman.Niederle.PAP.JEP.pdf . Recorded `n.a.` |
| §4 Dal-Ré et al. | Authors, volume, pages, year | Not on the publisher page https://www.science.org/doi/10.1126/scitranslmed.3007513 ; recovered from PubMed and labelled secondary: https://pubmed.ncbi.nlm.nih.gov/24553383/ |
| §4.3 pre-registration critiques | Five further critique documents located but not fetched, so nothing is quoted from them | https://pmc.ncbi.nlm.nih.gov/articles/PMC6840388/ · https://repository.tilburguniversity.edu/server/api/core/bitstreams/a48f413d-6c68-4e53-965d-fa8672104020/content · https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3747616 · https://eprints.lse.ac.uk/112747/1/pre_analysis_plans_an_early_stocktaking.pdf · https://economics.mit.edu/sites/default/files/publications/InPraise.pdf |
| §4.4 EGAP / journal policy | No registry page or journal preregistration policy document was fetched | Recorded `n.a.` |
| §5.1 Beckley *IS* 2023 DOI | DOI is not printed on the MIT Press article page | Resolved from the Belfer Center recommended-citation page: https://doi.org/10.1162/isec_a_00463 via https://www.belfercenter.org/publication/peril-peaking-powers-economic-slowdowns-and-implications-chinas-next-decade |
| §5.3 Medeiros | Author name and publication date are not printed in the fetched page body; the page also returned a mismatched subtitle ("Why America Stands to Lose If It Resumes Nuclear Testing"), indicating template contamination | Author taken from the page metadata (Evan S. Medeiros). Date recorded `n.a.` from the fetched text. URL: https://www.foreignaffairs.com/china/delusion-peak-china-united-states-evan-medeiros |
| §5.3 Hass | Publication name, volume/issue and date not stated in the fetched page content | Recorded `n.a.`; only author and title confirmed. https://www.prcleader.org/post/organizing-american-policy-around-peak-china-is-a-bad-bet |
| §5.3 Lind | Author name, page range, publication year and DOI not stated in the fetched page body | Author (Jennifer Lind) taken from page metadata; year, page range and DOI recorded `n.a.` https://direct.mit.edu/isec/article/49/2/7/125214/Back-to-Bipolarity-How-China-s-Rise-Transformed |
| §5.3 Lind, China GDP-per-capita ratio | The numeric 2023 value for China's GDP-per-capita ratio | Described qualitatively as low on the fetched page but no figure stated. Recorded `n.a.` |
| §5.4 Kugler & Organski | Editor, publisher and year of the *Handbook of War Studies* volume | Not stated on the fetched PDF pages. Recorded `n.a.` |
| §5.4 power-transition thresholds | The "80 percent of GNP" contender threshold, any numerical definition of parity, and the length of the transition window | Not present in the fetched chapter. An 80% figure appears only in a student thesis (https://academicos.uprrp.edu/preh/wp-content/uploads/sites/6/2024/06/Manuel-Mas-Cabrera_Tesis-1-1.pdf) which is **not** cited as primary. Recorded `n.a.` |
| §5.4 *The War Ledger* | Organski & Kugler (1980) itself | Not obtained; no claim is attributed to it. Recorded `n.a.` |
| §5.5 Belfer case file | Operational definitions of "rising power" and "ruling power", and the 16-case list with dates in a citable form | The page states only prose criteria; no measurement rule is given. This absence is itself reported as the finding |
| §5.6 electricity/grid | A single primary figure for China's share of *global grid investment* | The IEA China page gives China's USD 88 bn T&D figure and the executive summary gives the ~USD 400 bn global total; the ~22% share is a derived ratio of two IEA figures, not an IEA-stated share. Flagged as derived |

## Full source list

Every URL fetched in the course of building this report.

**Composite indices and national power**
- https://correlatesofwar.org/data-sets/national-material-capabilities/
- https://correlatesofwar.org/wp-content/uploads/NMC_Documentation_v5_0.pdf
- https://scispace.com/pdf/the-power-of-nations-measuring-what-matters-441eqyutp6.pdf
- https://www.belfercenter.org/publication/power-nations-measuring-what-matters
- https://direct.mit.edu/isec/article-abstract/43/2/7/12211
- https://direct.mit.edu/isec/article/44/1/197/12229/Correspondence-Measuring-Power-in-International
- https://direct.mit.edu/isec/article/49/2/7/125214/Back-to-Bipolarity-How-China-s-Rise-Transformed
- https://power.lowyinstitute.org/methodology/
- https://power.lowyinstitute.org/downloads/lowy-institute-asia-power-index-2019-methodology.pdf
- https://power.lowyinstitute.org/downloads/lowy-institute-2025-asia-power-index-key-findings-report.pdf
- https://www.globalfirepower.com/countries-listing.php
- https://www.globalfirepower.com/pwrindx-explained.php (404)
- https://oec.world/en/resources/methods
- https://academic.oup.com/cjip/article/19/3/237/8711324
- https://carnegieendowment.org/research/2026/04/methods-of-national-power-analysis-pitfalls-and-best-practices
- https://public.websites.umich.edu/~jkhanson/state_capacity.html
- https://public.websites.umich.edu/~jkhanson/resources/StateCapac_v1_doc.pdf
- https://www.sas.rochester.edu/psc/polmeth/papers/Kenkel_Carroll.pdf
- https://onlinelibrary.wiley.com/doi/abs/10.1111/ajps.12442
- https://academic.oup.com/jpr/article/56/3/364/8365318
- https://academic.oup.com/jpr/article/57/6/789/8365303
- https://www.cambridge.org/core/journals/political-science-research-and-methods/article/latent-variable-approach-to-measuring-and-explaining-peace-agreement-strength/9184401C70859F5B4EB155F2671D7EBA

**Composite-indicator methodology and critique**
- https://ideas.repec.org/p/wbk/wbrwps/5484.html
- https://openknowledge.worldbank.org/entities/publication/0dc4084b-9566-5844-8cdf-ae03e53515a7
- https://openknowledge.worldbank.org/entities/publication/4fa16c40-5ad2-5b73-8420-02dcf0ddee7b
- https://openknowledge.worldbank.org/server/api/core/bitstreams/7c19b741-66e0-5e55-ba4d-bc7647aadb6b/content
- https://www.journals.uchicago.edu/doi/10.1086/715066
- https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/08/handbook-on-constructing-composite-indicators-methodology-and-user-guide_g1gh9301/9789264043466-en.pdf
- https://knowledge4policy.ec.europa.eu/sites/default/files/jrc47008_handbook_final.pdf
- https://publications.jrc.ec.europa.eu/repository/handle/JRC24397
- https://publications.jrc.ec.europa.eu/repository/bitstream/JRC32434/EUR%2021834%20EN.pdf
- https://publications.jrc.ec.europa.eu/repository/bitstream/JRC32435/EUR%2021833%20EN.pdf
- https://publications.jrc.ec.europa.eu/repository/bitstream/JRC56990/reqno_jrc56990_saisana_saltelli_2010epi_eur.pdf%5B1%5D.pdf
- https://academic.oup.com/jrsssa/article-abstract/168/2/307/7084307
- https://ophi.org.uk/sites/default/files/OPHI-wp26_vs5.pdf
- https://ophi.org.uk/sites/default/files/OPHI-wp26b_vs4.pdf
- https://mpra.ub.uni-muenchen.de/60705/1/MPRA_paper_60705.pdf
- https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=61fb0ba9b2e3c6b8619a4aa493fa55f26ff6c10c

**Bayesian latent-variable measurement**
- https://ideas.repec.org/a/wly/amposc/v52y2008i1p201-217.html
- http://cfariss.com/documents/Fariss2014APSR.pdf
- http://cfariss.com/documents/Fariss2014APSR_SupplementaryAppendix.pdf
- http://cfariss.com/documents/Fariss2019APSR.pdf
- https://ideas.repec.org/a/cup/polals/v18y2010i04p426-449_01.html
- https://www.cambridge.org/core/journals/political-analysis/article/democratic-compromise-a-latent-variable-analysis-of-ten-measures-of-regime-type/2A6B2BBA6F80367644F2C5007E1CFC29
- https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2A6B2BBA6F80367644F2C5007E1CFC29/S1047198700012559a.pdf/democratic_compromise_a_latent_variable_analysis_of_ten_measures_of_regime_type.pdf
- https://scispace.com/pdf/the-v-dem-measurement-model-latent-variable-analysis-for-1997yaxojn.pdf
- https://v-dem.net/media/publications/v-dem_working_paper_2016_21.pdf (404)

**Pre-registration**
- https://www.pnas.org/doi/10.1073/pnas.1708274114
- https://www.nature.com/articles/s41562-022-01497-2
- https://osf.io/7ekfm
- https://osf.io/6wgbj/registrations
- https://economics.mit.edu/sites/default/files/publications/JEP%20Analysis%20Plans%20Final.pdf
- https://web.stanford.edu/~niederle/Coffman.Niederle.PAP.JEP.pdf
- https://www.science.org/doi/10.1126/scitranslmed.3007513
- https://pubmed.ncbi.nlm.nih.gov/24553383/
- https://www.cambridge.org/core/journals/political-analysis/article/case-for-registering-studies-of-political-outcomes-an-application-in-the-2010-house-elections/770DCBB446A520A9DF17395E94901E27
- https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/research-preregistration-in-political-science-the-case-counterarguments-and-a-response-to-critiques/E80124ED16BA47D0EA09F03D72B89EC7
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10192018/
- https://research.monash.edu/en/publications/insights-into-the-accuracy-of-social-scientists-forecasts-of-soci/
- https://sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jasa.pdf

**Peaking power, power transition, Thucydides Trap**
- https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf
- https://direct.mit.edu/isec/article/48/1/7/117122/The-Peril-of-Peaking-Powers-Economic-Slowdowns-and
- https://www.belfercenter.org/publication/peril-peaking-powers-economic-slowdowns-and-implications-chinas-next-decade
- https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/PDYVY2
- https://www.foreignaffairs.com/china/delusion-peak-china-united-states-evan-medeiros
- https://www.prcleader.org/post/organizing-american-policy-around-peak-china-is-a-bad-bet
- http://slantchev.ucsd.edu/courses/pdf/Kugler%20&%20Organski%20-%20The%20Power%20Transition.pdf
- https://www.belfercenter.org/programs/thucydidess-trap/thucydidess-trap-case-file
- https://www.airuniversity.af.edu/Portals/10/SSQ/documents/Volume-15_Issue-4/SC-Hanania.pdf

**Techno-industrial dimensions**
- https://ember-energy.org/latest-insights/global-electricity-review-2026/major-countries-and-regions/
- https://www.iea.org/reports/world-energy-investment-2025/china
- https://www.iea.org/reports/world-energy-investment-2025/executive-summary
- https://ifr.org/downloads/press_docs/2025-09-25-IFR_press_release_China_in_English.pdf
- https://ifr.org/img/worldrobotics/Executive_Summary_WR_2025_Industrial_Robots.pdf

**Located but not fetched (no values drawn from these)**
- https://www.pnas.org/doi/10.1073/pnas.0900943106
- https://www.hks.harvard.edu/sites/default/files/centers/cid/files/ATLAS_2013_Part1.pdf
- https://journals.plos.org/plosone/article/file?type=printable&id=10.1371/journal.pone.0047278
- https://oms-inet.files.svdcdn.com/production/files/main_feb4.pdf?dm=1553075540
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6840388/
- https://repository.tilburguniversity.edu/server/api/core/bitstreams/a48f413d-6c68-4e53-965d-fa8672104020/content
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3747616
- https://eprints.lse.ac.uk/112747/1/pre_analysis_plans_an_early_stocktaking.pdf
- https://economics.mit.edu/sites/default/files/publications/InPraise.pdf
