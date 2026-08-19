# Political stress

The stress term `stress[i,t]` in `SPECIFICATION.md` adopts Turchin's published Political Stress Indicator **verbatim**, with no bespoke reformulation, no added terms, and no re-weighting.

The reason is narrow and procedural. Any equation constructed here would be constructed by an author who already knows the baseline positions of all eight falsification conditions and the expected headline result. A stress function invented under those circumstances is unfalsifiable in practice regardless of its internal logic, because the reader cannot distinguish a principled construction from a reverse-engineered one. Adopting a specification published in 2016, by an author with no stake in this thesis, removes that charge entirely.

Adopting it verbatim also means adopting its criticism verbatim. The published record against PSI is substantial, and section 4 sets it out at greater length than the specification itself. This is required by the third standing prohibition in `README.md`: the strongest counter-position must appear wherever the supporting claim is made.

---

## 1. The specification, as published

Turchin's structural-demographic Political Stress Indicator is multiplicative in three components ([Ages of Discord](https://sackett.net/turchin_ages-of-discord.pdf), following the original concept in Goldstone 1991):

```
Psi = MMP * EMP * SFD
```

| Component | Meaning |
|---|---|
| `MMP` | Mass mobilisation potential |
| `EMP` | Elite mobilisation potential |
| `SFD` | State fiscal distress |

The multiplicative form is itself substantive. It means each component is a necessary condition: any one near zero suppresses `Psi` regardless of the other two. A state with immiserated masses, elite overproduction, and a healthy fiscal position scores low. That is a strong claim and it is Turchin's, not this project's.

### 1.1 Mass mobilisation potential

```
MMP = w^(-1) * (N_urb / N) * A_20_29
```

| Term | Definition |
|---|---|
| `w` | Relative wage: median or typical worker wage divided by GDP per capita. `w^(-1)` is the immiseration term |
| `N_urb / N` | Urbanisation rate — share of population in cities |
| `A_20_29` | Share of population aged 20-29 — the youth-bulge term |

Sources: [Ages of Discord](https://sackett.net/turchin_ages-of-discord.pdf); [A Structural-Demographic Analysis of American History](https://peterturchin.com/wp-content/uploads/2013/09/SDAAS_Sep17.pdf); the UK application reproducing the formula with equal weighting of the three subcomponents ([Modeling Social Pressures Toward Political Instability in the United Kingdom, 1500 to 2015](https://escholarship.org/content/qt72g2v469/qt72g2v469_noSplash_2f49fef4c4c76f194b0ffa61f0fbc4cf.pdf)).

### 1.2 Elite mobilisation potential

```
EMP = epsilon^(-1) * E / (s * N)
```

| Term | Definition |
|---|---|
| `epsilon` | Relative elite income: average elite income scaled by GDP per capita |
| `E` | Elite numbers |
| `s` | Government employee positions per head of population — proxy for available elite positions |
| `N` | Total population |

The youth-cohort term is deliberately absent from `EMP` to avoid double-counting it with `MMP` ([Ages of Discord](https://sackett.net/turchin_ages-of-discord.pdf)). Turchin's simplification derives `epsilon` by assuming elites divide the economic surplus — GDP minus labour's share — among themselves, which reduces the expression to a function of relative wage `w`, relative elite numbers `e`, and labour-force share `lambda` ([structural-demographic methods paper](https://escholarship.org/content/qt6qp8x28p/qt6qp8x28p.pdf)).

That reduction is the origin of critique 2 in section 4, and it is not a minor technicality.

Turchin's operational proxies for elite numbers include law degrees conferred and counts of high-net-worth households; the reported rise in US households worth $10m or more, from 66,000 in 1983 to 693,000 in 2019 in inflation-adjusted terms, is the headline elite-overproduction series ([Guardian review of End Times](https://www.theguardian.com/books/2023/may/28/end-times-by-peter-turchin-review-elites-counter-elites-and-path-of-political-disintegration-can-we-identify-cyclical-trends-in-narrative-of-human-hope-and-failure)).

### 1.3 State fiscal distress

```
SFD = (Y / G) * (1 - T)
```

where `Y` is total state debt, `G` is GDP, and `T` is the share of the population expressing trust in state institutions ([Ages of Discord](https://sackett.net/turchin_ages-of-discord.pdf)). Derivative applications write the trust term as a distrust measure `D` in the denominator, `SFD = Y / (G * D)` ([UK application](https://escholarship.org/content/qt72g2v469/qt72g2v469_noSplash_2f49fef4c4c76f194b0ffa61f0fbc4cf.pdf)).

**Committed:** this project uses the `(Y/G) * (1 - T)` form from *Ages of Discord*, not the `Y/(G*D)` variant, and treats the difference as a sensitivity rather than a matter of taste. The two forms are not monotone transforms of each other and can order states differently.

### 1.4 Combined estimating form

The full combined equation, as used in the 2023 empirical replication and traced there to *Ages of Discord* eq. 13.2:

```
PSI[t] = w_rel[t]^(-1) * N_urb[t] * N_20_29[t] * epsilon[t]^(-1) * e[t] * D[t] * (1 - T[t])
```

Source: [The structural-demographic theory revisited](https://pmc.ncbi.nlm.nih.gov/articles/PMC10621949/).

---

## 2. Cross-state application: the hard part

PSI was developed and calibrated on the United States. Applying it to the PRC requires operationalising four terms for which the US data conventions do not transfer, and every one of those decisions must be committed here rather than made during estimation.

| Term | US operationalisation | PRC operationalisation | Committed status |
|---|---|---|---|
| `w` relative wage | Median wage / GDP per capita, BLS and BEA | Urban average wage / GDP per capita, NBS — **not a median**, and urban-only | Committed with a `basis_mismatch` flag on every output that consumes it |
| `A_20_29` | Census and projections | UN WPP and NBS census | Committed, comparable |
| `N_urb / N` | Census urban definition | NBS urban definition includes hukou-ineligible residents inconsistently across vintages | Committed with a registered break |
| `E` elite numbers | Law degrees, high-net-worth households | Party membership is **not** an elite-aspirant proxy; committed proxy is tertiary graduates entering credentialed professions against establishment posts | Committed, weak, flagged |
| `s` elite positions | Government employees per capita | Establishment posts (bianzhi) per capita where published | Committed, coverage gaps |
| `T` institutional trust | Long-run Gallup and ANES series | No independent long-run series exists | **Not committed — see 2.1** |

### 2.1 The trust term has no PRC analogue and this is not soluble

There is no independent, long-run, cross-nationally comparable measure of institutional trust for the PRC. Survey instruments that exist are subject to preference falsification in precisely the direction that matters, and using them would import a bias whose sign is known and whose magnitude is not.

Three options were considered and two rejected:

| Option | Assessment |
|---|---|
| Use available survey series | **Rejected.** Known-sign bias of unknown magnitude, in the term that most directly drives `SFD` |
| Substitute a behavioural proxy — protest counts, capital flight | **Rejected.** Circular. Predicting unrest from a measure of unrest is the specific failure the Poland critique names |
| Set `T` to a constant and report `SFD` as debt-to-GDP alone for the PRC, with the asymmetry declared | **Committed** |

The third option is unsatisfying and is adopted because the alternatives are worse. Its consequence is stated explicitly: **PRC `SFD` is not comparable in level to US `SFD`**, only in trend. Every published comparison of `Psi` between the two states must carry that statement. Cross-state level comparison of `Psi` is therefore prohibited in this project's outputs; only within-state trajectories and their changes are reported.

This is a real limitation on what the stress block can support, and it is recorded before any estimate exists rather than appearing as a caveat after one.

### 2.2 The symmetry requirement cuts the other way too

The first standing prohibition requires that each American pathology be paired with its Chinese analogue on the same scale. Where the scale does not exist — as with `T` — the honest response is to decline the comparison, not to construct a scale that permits it. The US `Psi` will therefore be reported with its trust term active and the PRC `Psi` with its trust term inert, and no summary statistic combining them is permitted.

---

## 3. How stress enters the model

Two channels only, both stated in `SPECIFICATION.md`.

1. **Block E feedback.** `psi[j,i]` maps stress onto input growth, with a sign-free prior centred at zero. Stress may suppress or mobilise.
2. **`Y_net` deduction.** Stress raises the internal cost of maintaining capability, reducing net resources available after production, welfare and security costs.

Stress does **not** enter Block P. Political stress is not an input to the production function of capability, and modelling it as one would confuse a constraint on realising capability with a factor of production.

Stress is also **not** used to generate a collapse or discontinuity term. No threshold in `Psi` triggers a regime change in the model. The reason is section 4: the evidence that `Psi` predicts instability at all is weak, and building a discontinuity on a weakly predictive index would manufacture drama the data cannot support.

---

## 4. The case against PSI

Four published critiques. All four are load-bearing and none is answered by this project.

### 4.1 Circularity in the trust and instability terms

The Poland application argues that any operationalisation of the trust or distrust term other than direct public opinion creates a vicious circle — "we would be predicting unrest by measuring unrest" — and concludes that "there are too many independent problems with the implementation of the Goldstone model as proposed by Turchin (2013) to silently accept the apparent agreement with history. A fundamental revision and testing are needed to fully erase the impression of a just-so story" ([Political Stress Index of Poland](https://arxiv.org/html/2405.01163v1)). The same paper reports extreme sensitivity to parameter choices, describing it as a hallmark of chaos, and finds the elite-fraction dynamics cannot by construction describe elite share over long periods without modification.

This project's response: the circularity critique is the direct reason the behavioural-proxy option was rejected in section 2.1. The parameter-sensitivity finding is not answered and is the reason no discontinuity is built on `Psi`.

### 4.2 EMP may add no independent content

The most serious critique. Because Turchin derives relative elite income from the surplus identity, both main components of elite mobilisation potential reduce to algebraic manipulations of the relative wage. The retrospective assessment states it plainly: "no empirical benchmark is used to assess the external validity of the two main components of the elite mobilisation potential... Both variables are an algebraic manipulation of the relative wage" ([SSRN working paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4391019)).

If that is right, `Psi` is closer to a transformed immiseration index with a fiscal multiplier than to a three-mechanism composite, and the multiplicative structure conveys less independent information than it appears to.

**Committed diagnostic:** the correlation between the estimated `EMP` and `MMP` series is computed and published for both states. If it exceeds 0.9, the outputs must report `Psi` as an immiseration-and-fiscal index and drop the three-mechanism language. This is a pre-registered concession, and it can only be triggered against the more interesting reading.

### 4.3 The core predictions fail on US data 1960-2020

The 2023 empirical test finds three failures: labour oversupply cannot explain wage polarisation, with automation explaining most of the variance; elite income **rises** as relative wage falls, contradicting the theory's predicted hump-shaped pattern; and elite overproduction does not predict US political instability over 1960-2020, with PSI model variables explaining roughly 18% of the variance in political instability ([The structural-demographic theory revisited](https://pmc.ncbi.nlm.nih.gov/articles/PMC10621949/)).

Eighteen percent is the number that governs how stress is used here. It is why stress enters as a modest feedback with a sign-free prior rather than as a driver, and why no regime transition depends on it.

Against this stands Turchin and Korotayev's retrospective claim that the 2010 forecast was borne out by the observed rise in anti-government demonstrations and riots across the US, UK and Western Europe over 2010-2020 ([PLOS ONE, 2020](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0237458)). Both findings are reported. They are not reconciled here, because reconciling them is a research contribution in its own right and is not this project's contribution.

### 4.4 External validity outside the US is poor

Applying the structural-demographic model to Chile produces "rather poor results when forecasting Chile's political instability... many variables seem to be weak predictors of political stress, such as institutional distrust and national debt" ([Ascui and Gac, Cliodynamics](https://www.sociostudies.org/upload/socionauki.ru/book/files/iim_11_en/07%20Ascui%20Gac.pdf)). The Qing Dynasty application requires substituting inverse arable land per capita for relative wage and an inverse fiscal-surplus ratio for `SFD`, because the US operationalisations do not exist for that case ([Qing Dynasty structural-demographic analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC10437944/)).

That the specification requires re-operationalisation on every new case is directly relevant, because this project is doing exactly that for the PRC. The Chile result is the closest available estimate of how well such a transfer performs, and it performs badly. This is the strongest available argument that the PRC stress series should be treated as weakly informative at best, and the model's use of it is scaled accordingly.

A more favourable review, from the journal Turchin edits, is broadly positive while flagging parameter sensitivity and the interpretation of the rapid post-2000 rise ([Richerson, Cliodynamics 8(2)](https://escholarship.org/uc/item/3861g21r)).

---

## 5. What would make this section wrong

Pre-registered, in the same spirit as `falsifiers/PRE-REGISTRATION.md` though not part of the eight conditions.

| Condition | Consequence |
|---|---|
| `corr(MMP, EMP) > 0.9` in either state | `Psi` reported as an immiseration-and-fiscal index; three-mechanism language withdrawn |
| `psi[j,i]` posterior indistinguishable from prior for all `j` in a state | Stress reported as not learned for that state; the feedback channel is reported as unidentified rather than as zero |
| PRC `Psi` trend sign flips under the `Y/(G*D)` variant of `SFD` | Both variants published; the PRC stress series is downgraded to qualitative |
| A long-run independent PRC institutional-trust series becomes available | `T` activated, prior specification amended **by commit**, both versions published |

The last row is the only permitted amendment to this file's substance, and it requires the new series to be named and its provenance recorded before activation.

---

## 6. Simplified variant, recorded but not used

Turchin's later stripped-down implementation tracks only immiseration, youth-bulge age structure, and intra-elite competition, with an explicit weighted radicalisation propensity:

```
alpha(t) = alpha_0 + alpha_w * (w_0 - w) + alpha_e * (e - e_0) + A_20
alpha_0 = 0.1,  alpha_w = 1,  alpha_e = 0.5
```

Source: [MPF2100 model documentation](https://sfieducation.s3.amazonaws.com/2022+Complexity-GAINs/readings/Turchin_SocArxiv2021.pdf).

It is recorded here for completeness and **not adopted**, because its calibrated weights were fitted for a different purpose on US data and adopting fitted weights is a weaker form of verbatim adoption than adopting a functional form. If the diagnostic in 4.2 fires, this variant becomes the natural fallback, and that path is noted now so that taking it later is not a discovery.

---

## Sources

- Turchin, *Ages of Discord* (Beresta Books, 2016) — https://sackett.net/turchin_ages-of-discord.pdf
- Turchin, A Structural-Demographic Analysis of American History — https://peterturchin.com/wp-content/uploads/2013/09/SDAAS_Sep17.pdf
- Turchin, structural-demographic methods paper, eScholarship — https://escholarship.org/content/qt6qp8x28p/qt6qp8x28p.pdf
- Modeling Social Pressures Toward Political Instability in the United Kingdom, 1500 to 2015 — https://escholarship.org/content/qt72g2v469/qt72g2v469_noSplash_2f49fef4c4c76f194b0ffa61f0fbc4cf.pdf
- The structural-demographic theory revisited (PLOS ONE / PMC, 2023) — https://pmc.ncbi.nlm.nih.gov/articles/PMC10621949/
- Retrospective assessment commentary (SSRN, 2023) — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4391019
- Turchin and Korotayev, The 2010 Structural-Demographic Forecast: A Retrospective Assessment (PLOS ONE, 2020) — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0237458
- Political Stress Index of Poland (arXiv) — https://arxiv.org/html/2405.01163v1
- Structural-demographic analysis of the Qing Dynasty (PMC, 2023) — https://pmc.ncbi.nlm.nih.gov/articles/PMC10437944/
- Ascui and Gac, Hypotheses Testing for the Structural-Demographic Model — https://www.sociostudies.org/upload/socionauki.ru/book/files/iim_11_en/07%20Ascui%20Gac.pdf
- Richerson, review of *Ages of Discord*, *Cliodynamics* 8(2), 2017 — https://escholarship.org/uc/item/3861g21r
- Turchin, MPF2100 model documentation (SocArXiv, 2021) — https://sfieducation.s3.amazonaws.com/2022+Complexity-GAINs/readings/Turchin_SocArxiv2021.pdf
- Guardian review of *End Times* — https://www.theguardian.com/books/2023/may/28/end-times-by-peter-turchin-review-elites-counter-elites-and-path-of-political-disintegration-can-we-identify-cyclical-trends-in-narrative-of-human-hope-and-failure
