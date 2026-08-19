# Paper A, section 3 -- The capability vector

**Status.** Draft, Phase 4. This is the first drafted prose in the programme. It is drafted before the other sections because it carries the paper's only genuinely contestable methodological claim, and exposing that claim to criticism first is more useful than exposing it last.

---

## 3.1 The object

Capability is reported as a vector of four elements, each estimated with a posterior distribution rather than a point value.

| Element | Content |
|---|---|
| `Y_throughput` | Dispatchable-adjusted electrical energy, grid delivery capacity, industrial robot stock and installations, manufacturing output |
| `Y_frontier` | Frontier-capable compute, semiconductor capability, advanced research output |
| `Y_net` | Net-resource efficiency, after deducting production, welfare and security costs |
| `Y_fin` | Capital-market depth, fiscal headroom, reserve-currency privilege |

`Y_throughput` is designated primary. Composites over the four are permitted in reporting only alongside a full weighting sensitivity, and changes in relative position are decomposed by element rather than aggregated.

Four is a choice and not a discovery. The number is small enough that a reader can hold the whole vector in mind, and large enough to separate the two mechanisms the research programme is about -- the frontier bundle and the deployment bundle -- from the two dimensions on which the incumbent's advantages are concentrated. Any of the four could be split. `Y_net` in particular is a composite in all but name, and section 3.5 concedes this.

The closest published precedent is Hanson and Sigman's state-capacity measure, which takes 21 indicators and deliberately retains three dimensions -- extractive, coercive and administrative -- rather than collapsing them ([Hanson and Sigman documentation](https://public.websites.umich.edu/~jkhanson/resources/StateCapac_v1_doc.pdf)). The architecture proposed here is the same shape applied to a different substantive domain.

---

## 3.2 Why aggregation is not a presentational choice

The argument against the scalar composite is usually made on the ground that the weights are arbitrary. That argument is weaker than it looks, and section 2 of the paper concedes as much: the Lowy Institute publishes its weights, concedes that other value judgements are possible, and then reports that its own "Sensitivity analysis has determined that the large number of indicators ... are quantitatively more important than our weighting scheme" ([Lowy methodology](https://power.lowyinstitute.org/methodology/)). If the weights barely matter, an argument resting on their arbitrariness barely matters either.

The stronger argument is formal, and it is not about arbitrariness at all. It is that in an additive or geometric aggregation, weights cannot mean what practitioners take them to mean.

The OECD and Joint Research Centre handbook states it directly: "In both linear and geometric aggregations, weights express trade-offs between indicators", and there is "an inconsistency between how weights are conceived ... and the actual meaning". Restated formally, "weights in additive aggregations necessarily take the meaning of substitution rates (trade-offs) and do not indicate the importance of the associated indicator" ([OECD/JRC Handbook, pp. 33, 112](https://knowledge4policy.ec.europa.eu/sites/default/files/jrc47008_handbook_final.pdf)). Munda and Nardo prove the incompatibility rather than asserting it: symmetrical importance "is incompatible with a linear aggregation rule"; "the estimation of weights is equivalent to that of substitution rates, implying a compensatory logic"; "trade-offs depend on the scales of measurement"; and therefore "the interpretation of weights as a measurement of the psychological concept of importance is always completely inappropriate" ([Munda and Nardo, EUR 21834 EN](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC32434/EUR%2021834%20EN.pdf)).

The consequence for a power index is concrete. A scalar composite of generation capacity, compute, market depth and manufacturing output asserts an exchange rate between terawatt-hours and dollars of market depth. That exchange rate is a substantive claim about the production function of geopolitical capability -- precisely the claim this research programme exists to interrogate. Aggregating first assumes the answer to the research question and then reports the assumption as a measurement.

The same handbook records what the trade-offs look like when someone works them out. In the Human Development Index, the implied value of a life-year ranges from about 0.50 dollars per year for Zimbabwe to almost 9,000 dollars per year in the richest countries, and the weights on the three components "have not changed in 20 years, and it is hard to believe that the HDI got it right first go" ([Ravallion, Mashup Indices of Development, pp. 14--16](https://openknowledge.worldbank.org/server/api/core/bitstreams/7c19b741-66e0-5e55-ba4d-bc7647aadb6b/content)). Ravallion's general charge is that the weights on components are usually explicit while "the weights attached to the underlying dimensions" are not, and that "little or no attention is given to the implied tradeoffs" (p. 12).

Normalisation is not neutral either. "Different normalisation methods will produce different results for the composite indicator", illustrated in the handbook with a Celsius-and-Fahrenheit example in which the choice of temperature scale reorders the result ([OECD/JRC Handbook, p. 83](https://knowledge4policy.ec.europa.eu/sites/default/files/jrc47008_handbook_final.pdf)). For capability measurement this is not a curiosity: generation capacity, compute throughput and market depth have no common scale, so the normalisation choice is doing part of the aggregation's work invisibly.

And there is a limit theorem at the end of the road. The handbook invokes it directly: "Arrow's impossibility theorem (Arrow, 1963) clearly shows that no perfect aggregation convention can exist", and converts it into a design constraint -- no indicator and no dimension may exceed 50 per cent of total weight, "otherwise ... this individual indicator would become a dictator in Arrow's terminology" ([OECD/JRC Handbook, pp. 52, 105, 111](https://knowledge4policy.ec.europa.eu/sites/default/files/jrc47008_handbook_final.pdf)).

---

## 3.3 The empirical demonstration -- the sign of movement is dimension-dependent

The formal argument would still be academic if the components moved together. They do not. Over roughly the same decade, the two most cited bodies of evidence about China's trajectory point in opposite directions, and each is measuring something real.

**The adverse direction.** The peaking-power literature assembles macro-financial and demographic indicators. Official growth fell from about 14 per cent in 2007 to about 6 per cent in 2019, with "rigorous studies" cited for a true rate "closer to 2 percent"; total factor productivity "declined 1.3 percent every year on average between 2008 and 2019" on Conference Board figures; capital efficiency deteriorated such that "it takes three times as many inputs to produce a unit of growth today as it did in the early 2000s" on DBS Bank figures; total debt "surged eight-fold between 2008 and 2019 and exceeded 300 percent of GDP"; and on the demographic projection, from 2020 to 2050 China "will lose an astounding 200 million working-age adults ... and gain 200 million senior citizens", with medical and social-security spending required to "triple as a share of GDP, from 10 percent to 30 percent, by 2050" ([Brands and Beckley, *Foreign Policy*](https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf); restated with a formal case-selection rule in [Beckley, *International Security* 48(1)](https://direct.mit.edu/isec/article/48/1/7/117122/The-Peril-of-Peaking-Powers-Economic-Slowdowns-and)).

**The favourable direction.** On the physical-capacity dimensions this programme designates primary, the direction over the same period is the opposite.

| Dimension | Measurement | Direction |
|---|---|---|
| Electricity demand | "10,573 TWh in 2025, accounting for a third of global electricity demand", "nearly doubled from 5,802 TWh in 2015" ([Ember, *Global Electricity Review 2026*](https://ember-energy.org/latest-insights/global-electricity-review-2026/major-countries-and-regions/)) | Rising |
| Build rate | "58% of global solar installations (378 GW (DC)) and 72% of global wind installations (119 GW)" in 2025 ([Ember](https://ember-energy.org/latest-insights/global-electricity-review-2026/major-countries-and-regions/)) | Rising |
| Generation mix | Coal share "fell from 70% in 2015 to 54% in 2025"; fossil generation declined 56 TWh in 2025, "the first year since 2015 without an increase" ([Ember](https://ember-energy.org/latest-insights/global-electricity-review-2026/major-countries-and-regions/)) | Improving |
| Grid capital formation | "USD 88 billion in transmission and distribution investment in 2025" against a global total where "some USD 400 billion is now spent on grids worldwide" ([IEA, *World Energy Investment 2025*, China](https://www.iea.org/reports/world-energy-investment-2025/china); [executive summary](https://www.iea.org/reports/world-energy-investment-2025/executive-summary)) | Rising |
| Robot stock | "a world record of 2,027,000 industrial robots working in factories", the stock having "doubled within three years" ([IFR, China release](https://ifr.org/downloads/press_docs/2025-09-25-IFR_press_release_China_in_English.pdf)) | Rising |
| Robot installations | "295,000 units in 2024 ... representing 54% of global demand" ([IFR](https://ifr.org/downloads/press_docs/2025-09-25-IFR_press_release_China_in_English.pdf)) | Rising |
| Robot supply localisation | Domestic manufacturers' domestic share "climbed to 57% across industries in 2024, up from 47% in 2023" ([IFR](https://ifr.org/downloads/press_docs/2025-09-25-IFR_press_release_China_in_English.pdf)) | Rising sharply |

A scalar index confronted with these two sets has exactly three options. It can average them under a weighting rule, in which case the weighting rule -- not the data -- determines the sign of the answer. It can drop one set, in which case the index reports the analyst's prior. Or it can report both, at which point it is a vector.

The robotics series makes a second point about what gets lost. China's 54 per cent share of global installations sits against a 43 per cent share of the global operational stock ([IFR executive summary](https://ifr.org/img/worldrobotics/Executive_Summary_WR_2025_Industrial_Robots.pdf)). Flow share exceeding stock share means the stock share is still converging upward, so any single-year snapshot understates the derivative. The vector therefore reports level, share and rate of change per dimension, with uncertainty, rather than one number per state.

---

## 3.4 The rival reading is nested, not opposed

The peaking-power reading is not treated as an error to be refuted. Its own author states the case-selection rule with unusual precision: "every case from 1870 to 2018 in which a great power's per capita gross domestic product (GDP) grew at least twice as fast as the global average for at least seven years and then suffered at least a 50 percent decline in growth rates over the next seven years", which "leaves nine cases" after excluding wartime downturns ([Beckley, *IS* 48(1)](https://direct.mit.edu/isec/article/48/1/7/117122/The-Peril-of-Peaking-Powers-Economic-Slowdowns-and)). That is a stated, checkable, quantitative rule, and it is more than most of the surrounding literature offers. Three of the nine cases are then set aside as overdetermined, which leaves a load-bearing base of roughly five to six cases -- the same order of magnitude as this programme's own analogue count, and the same limitation.

In this architecture the peaking reading corresponds to a region of the parameter space in which the challenger's trajectory turns down before the frontier and deployment bundles bind. It is a possible outcome of the model, assigned prior mass, and reachable. It is not a rival to be defeated in prose. The measurement consequence is that the vector must be capable of representing it: an index that cannot express "peaking on some dimensions while advancing on others" cannot adjudicate the disagreement at all.

That is not this paper's invention. The sharpest statement of it comes from a critic of the peaking thesis: "it is difficult to measure and understand what peak China means in practice. Is it an absolute term or a relative one -- and if the latter, relative to what?", followed by "China could peak in one area but advance in others, complicating the calculation", and "China peaking economically is not the same as China peaking geopolitically -- a distinction lost on many advocates of the peak China argument" ([Medeiros, *Foreign Affairs*](https://www.foreignaffairs.com/china/delusion-peak-china-united-states-evan-medeiros)). A vector is what that objection asks for.

A second critic reaches the vector conclusion from the opposite direction, and does the empirical work. Lind validates candidate metrics against historian-generated great-power lists for 1820--1990, derives normal ranges for great powers, and finds China at 130 per cent of the leading state's GDP against a great-power normal range of 17--45 per cent, and 36 per cent on the GDP-times-GDP-per-capita composite against a normal range of 8--28 per cent, while sitting at 32 per cent on military expenditure against a range of 23--105 per cent ([Lind, *IS* 49(2)](https://direct.mit.edu/isec/article/49/2/7/125214/Back-to-Bipolarity-How-China-s-Rise-Transformed)). Her conclusion -- "a key insight of this article is that 'catching up' or 'overtaking' are the wrong benchmarks" -- is a rejection of the scalar ranking question itself. Her verdict on GDP per capita, which is the multiplicand in the best-performing scalar index in the field, is blunter: it "is not a sound metric for this purpose", it "shows significant overlap among great powers, middle powers, and all non-great powers", and "the metric offers a national average, which obscures a country's highest level of technological performance".

---

## 3.5 What the vector costs

Three costs, stated rather than mitigated.

**It does not answer the question the field asks.** The literature's central question is comparative and scalar: is the challenger overtaking the incumbent, and when. Power transition theory operationalises power as "Economic Productivity per Capita x Population", proxies it with GNP, and stakes its empirical claim on a single contingency table -- twenty dyad-periods over 1860--1980, in which the signature cell of parity-plus-transition splits five wars to five non-wars ([Kugler and Organski, pp. 179, 190--191](http://slantchev.ucsd.edu/courses/pdf/Kugler%20&%20Organski%20-%20The%20Power%20Transition.pdf)). A vector cannot populate that table. Whether the right response is to build a vector or to answer the scalar question better is a live disagreement, and this paper takes one side of it without claiming the other side is unreasonable.

**It forfeits the one validation the scalar indices have.** Beckley's two-variable product predicts 78 per cent of wars and 70 per cent of militarised interstate disputes over 1816--2010, against CINC's 70 and 64 per cent and GDP alone at 68 and 64 per cent ([Beckley](https://scispace.com/pdf/the-power-of-nations-measuring-what-matters-441eqyutp6.pdf)). Kugler and Organski report that their scalar GNP proxy "performed as well as the more complex index of power developed by Singer et al. (1972)" ([Kugler and Organski, p. 191](http://slantchev.ucsd.edu/courses/pdf/Kugler%20&%20Organski%20-%20The%20Power%20Transition.pdf)). The historical record is therefore that adding components did not improve prediction and multiplying two variables did. The vector proposed here has no comparable validation and, because its outcome lies decades ahead, cannot acquire one on the same timescale. This is the strongest objection to the paper and it is not answered.

**`Y_net` is a composite wearing a different label.** Net-resource efficiency after deducting production, welfare and security costs requires exactly the trade-off judgements section 3.2 objects to in others. The programme's own defence -- that the vector keeps the number of such judgements to a minimum and reports each with sensitivity analysis -- is a difference of degree, not of kind. Beckley makes the corresponding concession about his own index, that it "does not measure net resources directly" and is "a primitive proxy" ([Beckley](https://scispace.com/pdf/the-power-of-nations-measuring-what-matters-441eqyutp6.pdf)); the same concession applies here with the same force.

---

## 3.6 The standard this section holds itself to

Ravallion's alternative to the mashup index is the dashboard: "nagging doubts remain about the value-added of mashup indices ... relative to the 'dashboard' alternative of monitoring the components separately", and "there are important aspects of development that cannot be captured in a single index" ([Ravallion](https://openknowledge.worldbank.org/server/api/core/bitstreams/7c19b741-66e0-5e55-ba4d-bc7647aadb6b/content)). The vector proposed here is a dashboard with two additions: a measurement model that reports uncertainty per element, and a pre-registered set of conditions under which the dashboard's owner has said in advance that he was wrong.

The uncertainty requirement is not decorative. Treier and Jackman show what happens without it: propagating measurement error through a downstream regression on democracy scores drops `r^2` from .63 on raw Polity values, to .57 on posterior means, to .40 with uncertainty carried through, at which point the quadratic term becomes indistinguishable from zero ([Treier and Jackman](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=61fb0ba9b2e3c6b8619a4aa493fa55f26ff6c10c)). Ignoring measurement error did not merely widen the intervals; it manufactured a substantive finding. A capability measure built on statistics whose national definitions differ is exposed to the same failure, and the vector's per-element posteriors exist to prevent it.

---

## Sources

- Hanson and Sigman, Leviathan's Latent Dimensions, documentation -- https://public.websites.umich.edu/~jkhanson/resources/StateCapac_v1_doc.pdf
- Lowy Institute, Asia Power Index methodology -- https://power.lowyinstitute.org/methodology/
- Nardo, Saisana, Saltelli and Tarantola, OECD/JRC Handbook on Constructing Composite Indicators -- https://knowledge4policy.ec.europa.eu/sites/default/files/jrc47008_handbook_final.pdf
- Munda and Nardo, Constructing Consistent Composite Indicators, EUR 21834 EN -- https://publications.jrc.ec.europa.eu/repository/bitstream/JRC32434/EUR%2021834%20EN.pdf
- Ravallion, Mashup Indices of Development, World Bank Policy Research Working Paper 5432 -- https://openknowledge.worldbank.org/server/api/core/bitstreams/7c19b741-66e0-5e55-ba4d-bc7647aadb6b/content
- Brands and Beckley, China Is a Declining Power, Foreign Policy, 24 September 2021 -- https://content.csbs.utah.edu/~mli/Economics%207004/Foreign%20Policy-China%20Is%20a%20Declining%20Power.pdf
- Beckley, The Peril of Peaking Powers, International Security 48(1) -- https://direct.mit.edu/isec/article/48/1/7/117122/The-Peril-of-Peaking-Powers-Economic-Slowdowns-and
- Beckley, The Power of Nations, full text -- https://scispace.com/pdf/the-power-of-nations-measuring-what-matters-441eqyutp6.pdf
- Ember, Global Electricity Review 2026, major countries and regions -- https://ember-energy.org/latest-insights/global-electricity-review-2026/major-countries-and-regions/
- IEA, World Energy Investment 2025, China -- https://www.iea.org/reports/world-energy-investment-2025/china
- IEA, World Energy Investment 2025, executive summary -- https://www.iea.org/reports/world-energy-investment-2025/executive-summary
- IFR, World Robotics 2025, China press release -- https://ifr.org/downloads/press_docs/2025-09-25-IFR_press_release_China_in_English.pdf
- IFR, World Robotics 2025 industrial robots executive summary -- https://ifr.org/img/worldrobotics/Executive_Summary_WR_2025_Industrial_Robots.pdf
- Medeiros, The Delusion of Peak China, Foreign Affairs -- https://www.foreignaffairs.com/china/delusion-peak-china-united-states-evan-medeiros
- Lind, Back to Bipolarity, International Security 49(2) -- https://direct.mit.edu/isec/article/49/2/7/125214/Back-to-Bipolarity-How-China-s-Rise-Transformed
- Kugler and Organski, The Power Transition -- http://slantchev.ucsd.edu/courses/pdf/Kugler%20&%20Organski%20-%20The%20Power%20Transition.pdf
- Treier and Jackman, Democracy as a Latent Variable -- https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=61fb0ba9b2e3c6b8619a4aa493fa55f26ff6c10c
