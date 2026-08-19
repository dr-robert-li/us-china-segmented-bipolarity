# Phase 2 Model Sources — US-China Capability Divergence (Bayesian Model Specification)

Compiled evidence for academic Bayesian model specification. Each entry gives: exact claim/number, author/institution, year, venue, and URL. Primary sources prioritized; critiques and data-availability gaps noted explicitly.

---

## 1. Peter Turchin's Political Stress Indicator (PSI / Ψ)

### 1.1 Canonical multiplicative specification

**Claim:** The Political Stress Indicator combines three components multiplicatively:
\[ \Psi = MMP \times EMP \times SFD \]
where MMP = Mass Mobilization Potential, EMP = Elite Mobilization Potential, SFD = State Fiscal Distress. Turchin attributes the original PSI concept to Jack Goldstone (1991, *Revolution and Rebellion in the Early Modern World*, pp. 141–145), but reformulates the functional forms.

- **Source:** Peter Turchin, *Ages of Discord: A Structural-Demographic Analysis of American History* (Beresta Books, 2016). Full PDF: https://sackett.net/turchin_ages-of-discord.pdf
- **Source:** Peter Turchin, "A Structural-Demographic Analysis of American History" (working paper, precursor chapter to *Ages of Discord*), https://peterturchin.com/wp-content/uploads/2013/09/SDAAS_Sep17.pdf
- **Source:** Peter Turchin, "Modeling Periodic Waves of Integration in the Afro-Eurasian World-System" / structural-demographic methods paper, eScholarship, https://escholarship.org/content/qt6qp8x28p/qt6qp8x28p.pdf (cites Turchin 2013: 246 for the Ψ = MMP×EMP×SFD formula)

### 1.2 MMP (Mass Mobilization Potential) — exact formula

**Claim:**
\[ MMP = w^{-1} \cdot \frac{N_{urb}}{N} \cdot A_{20-29} \]
where \(w^{-1}\) is the inverse relative wage (relative wage = median/typical worker wage divided by GDP per capita — the "misery index" / immiseration term), \(N_{urb}/N\) is the urbanization rate (proportion of population in cities), and \(A_{20-29}\) is the proportion of population aged 20–29 (youth-bulge term).

- **Source:** Turchin, *Ages of Discord* (2016), PDF pp. as above: https://sackett.net/turchin_ages-of-discord.pdf
- **Source:** Turchin, "A Structural-Demographic Analysis of American History," https://peterturchin.com/wp-content/uploads/2013/09/SDAAS_Sep17.pdf
- **Source:** "Modeling Social Pressures Toward Political Instability in the United Kingdom, 1500 to 2015" (equation set reproducing Turchin 2013's formula for MMP with equal weighting of the three subcomponents), eScholarship, https://escholarship.org/content/qt72g2v469/qt72g2v469_noSplash_2f49fef4c4c76f194b0ffa61f0fbc4cf.pdf

### 1.3 EMP (Elite Mobilization Potential) — exact formula

**Claim:**
\[ EMP = \varepsilon^{-1} \cdot \frac{E}{sN} \]
where \(\varepsilon^{-1}\) is the inverse relative elite income (average elite income scaled by GDP per capita — the elite-immiseration analog to \(w^{-1}\)), \(E\) is total elite numbers, \(s\) is the number of government employee positions per total population (proxy for available elite "slots"), and \(N\) is total population. The youth-cohort term is deliberately omitted from EMP to avoid double-counting (it is already in MMP).

- **Source:** Turchin, *Ages of Discord* (2016), https://sackett.net/turchin_ages-of-discord.pdf
- **Source:** Turchin, eScholarship structural-demographic methods paper, https://escholarship.org/content/qt6qp8x28p/qt6qp8x28p_noSplash_c3d0ac79e973d3c6029f872002050fcd.pdf — gives the simplification: relative elite income \(\varepsilon\) is calculated by assuming elites divide the economic surplus (GDP minus labor's share) among themselves, divided by elite numbers \(E\) and scaled by GDP per capita; this simplifies to an expression in relative wage \(w\), relative elite numbers \(e\), and labor-force share \(\lambda\).
- **Proxies used for elite numbers/elite overproduction (per Turchin, discussed across sources):** number of law degrees conferred, numbers of millionaire households, ratio of elite aspirants (e.g. lawyers, PhDs) to available elite positions. Explicitly named in: Bio-protocol methods write-up, https://bio-protocol.org/exchange/minidetail?id=7031301&type=30, and the Guardian review of *End Times*, https://www.theguardian.com/books/2023/may/28/end-times-by-peter-turchin-review-elites-counter-elites-and-path-of-political-disintegration-can-we-identify-cyclical-trends-in-narrative-of-human-hope-and-failure (cites Turchin's data point: US households worth $10m+ rose from 66,000 in 1983 to 693,000 in 2019, inflation-adjusted).

### 1.4 SFD (State Fiscal Distress) — exact formula

**Claim:**
\[ SFD = \frac{Y}{G} \cdot T \quad \text{(or, per variant notation)} \quad SFD = \frac{Y}{G \cdot D} \]
where \(Y\) is total state/public debt, \(G\) is GDP, and \(T\) is the proportion of the population expressing trust in state institutions (so \(1-T\) is distrust). Some derivative papers write the trust term as \(D\) (distrust) in the denominator; Turchin's original formulation multiplies debt/GDP by the distrust proxy.

- **Source:** Turchin, *Ages of Discord* (2016): "where Y is the total state debt, G is the GDP, and T is the proportion of the population expressing trust in the state institutions" — https://sackett.net/turchin_ages-of-discord.pdf
- **Source:** Modeling Social Pressures paper (UK application) gives \(SFD = Y/(GD)\), where D is a measure of public distrust: https://escholarship.org/content/qt72g2v469/qt72g2v469_noSplash_2f49fef4c4c76f194b0ffa61f0fbc4cf.pdf
- **Data sources Turchin uses for SFD in the US case:** national debt/GDP from the US Department of the Treasury; public trust in government from long-run Gallup/ANES-type survey series. Confirmed in the Bio-protocol methods description: https://bio-protocol.org/exchange/minidetail?id=7031301&type=30

### 1.5 Empirical implementation / rewritten combined form

**Claim:** Combining all three components yields the full estimating equation (as used in a 2023 PLOS ONE empirical replication):
\[ PSI_{model,t} = w_{rel,t}^{-1} \cdot N_{urb,t} \cdot N_{20\_29,t} \cdot \epsilon_t^{-1} \cdot e_t \cdot D_t \cdot (1-T_t) \]
where \(w_{rel}\) = ratio of median wage to GDP per capita, \(e\) and \(\epsilon\) = elite numbers and elite income respectively, \(D\) = public-debt-to-GDP ratio, \(N_{urb}\) = urbanization rate, \(N_{20\_29}\) = share of population aged 20–29, \(T\) = share of population trusting government.

- **Source:** Vlad Tarko / or similarly-authored, "The structural-demographic theory revisited: An empirical test of the effect of relative wages, elite numbers and debt on the Political Stress Index," *PLOS ONE* / PMC, 2023, https://pmc.ncbi.nlm.nih.gov/articles/PMC10621949/ (also cites Turchin 2016, *Ages of Discord*, eq. 13.2, as the original source of this combined equation)
- **Source:** Turchin & Korotayev, "The 2010 Structural-Demographic Forecast for the 2010–2020 Decade: A Retrospective Assessment," *PLOS ONE*, 17 Aug 2020, https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0237458 — reports empirically that anti-government demonstrations and riots increased dramatically 2010–2020 in the US, UK, and Western Europe, consistent with the rising PSI forecast made in 2010.

### 1.6 Later refinements — stripped-down "MPF" (Mediated Population Feedback) version

**Claim:** In a 2021 SocArXiv/agent-based implementation, Turchin uses a simplified, parsimonious version of PSI tracking only three factors — immiseration (inverse relative income), youth-bulge age structure, and intra-elite overproduction — with an explicit weighted-sum radicalization propensity function:
\[ \alpha(t) = \alpha_0 + \alpha_w(w_0 - w) + \alpha_e(e - e_0) + A_{20} \]
with calibrated weights \(\alpha_0 = 0.1\), \(\alpha_w = 1\), \(\alpha_e = 0.5\).

- **Source:** Peter Turchin, "MPF2100" model documentation, SocArXiv/SFI, 9 March 2021, https://sfieducation.s3.amazonaws.com/2022+Complexity-GAINs/readings/Turchin_SocArxiv2021.pdf

### 1.7 Application to non-US cases (Qing Dynasty, Poland) — different variable operationalizations

**Claim:** In the Qing Dynasty (1644–1912) application, MMP is operationalized as the inverse of arable land per capita (not relative wage, since wage data are unavailable); SFD is operationalized as the inverse of the fiscal surplus/deficit ratio (revenue minus expenditure, divided by revenue).

- **Source:** "Structural-demographic analysis of the Qing Dynasty (1644–1912): Testing the Fiscal Component," *PLOS ONE*/PMC, 18 Aug 2023, https://pmc.ncbi.nlm.nih.gov/articles/PMC10437944/

**Claim:** In a Poland application, the model shows extreme sensitivity to parameter choices ("hallmark of chaos") and the elite-fraction dynamical equations cannot, by construction, describe elite share for long time periods without modification.

- **Source:** "Political Stress Index of Poland," arXiv preprint, https://arxiv.org/html/2405.01163v1

### 1.8 Published critiques of PSI construction

**Critique 1 — Circularity / tautological construction:** The arXiv Poland paper explicitly argues: "it would lead to a vicious circle if anything other than direct public opinion were to be used here — we would be predicting unrest by measuring unrest," and concludes "there are too many independent problems with the implementation of the Goldstone model as proposed by Turchin (2013) to silently accept the apparent agreement with history. A fundamental revision and testing are needed to fully erase the impression of a just-so story."
- **Source:** arXiv, "Political Stress Index of Poland," https://arxiv.org/html/2405.01163v1

**Critique 2 — Elite-income/elite-number terms are algebraic restatements of relative wage, so EMP adds no independent explanatory content; no external validity benchmark for the elite variables; and the theory's core predictions fail empirically for the US 1960–2020:** A 2023 empirical test finds that (a) labor oversupply cannot explain wage polarization (automation explains most of the variance), (b) elite income rises as relative wage falls — contradicting the theory's predicted hump-shaped pattern, and (c) elite overproduction does not predict US political instability over 1960–2020; PSI model variables explain only ~18% of variance in political instability.
- **Source:** "The structural-demographic theory revisited: An empirical test of the effect of relative wages, elite numbers and debt on the Political Stress Index," PMC, 2 Nov 2023, https://pmc.ncbi.nlm.nih.gov/articles/PMC10621949/
- **Companion/earlier version:** SSRN working paper, "The 2010 Structural-Demographic Forecast for the 2010–2020 Decade: A Retrospective Assessment" commentary, 16 March 2023, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4391019 — states plainly: "no empirical benchmark is used to assess the external validity of the two main components of the elite mobilisation potential... Both variables are an algebraic manipulation of the relative wage."

**Critique 3 — Model transfers poorly outside the US case (external validity):** Applying the SDT/PSI model to Chile produces "rather poor results when forecasting Chile's political instability... many variables seem to be weak predictors of political stress, such as institutional distrust and national debt."
- **Source:** Ascui & Gac, "Hypotheses Testing for the Structural-Demographic Model for Political Instability and Social Unrest," Cliodynamics/Sociostudies almanac, https://www.sociostudies.org/upload/socionauki.ru/book/files/iim_11_en/07%20Ascui%20Gac.pdf (also mirrored at https://www.sociostudies.org/almanac/articles/hypotheses_testing_for_the_structural-demographic_mo-_del_for_political_instability_and_social_unres/)

**Critique 4 — Methodological/qualitative skepticism (softer, non-technical):** Peter J. Richerson's review in *Cliodynamics* (the journal Turchin himself edits) is broadly favorable but flags concerns about parameter sensitivity and interpretation of the rapid post-2000 PSI rise.
- **Source:** Peter J. Richerson, "A Dynamic Analysis of American Socio-Political History. A Review of *Ages of Discord*," *Cliodynamics* 8(2), 2017, DOI: 10.21237/C7clio8237156, https://escholarship.org/uc/item/3861g21r ; full PDF: http://www.des.ucdavis.edu/faculty/richerson/Ages%20of%20Discord%20review.pdf

---

## 2. Elasticity of Substitution — Energy/Capital and Nested CES Structures

### 2.1 GTAP-E assumed values

**Claim:** In GTAP-E, the inner-nest elasticity of substitution between capital and the energy composite (\(\sigma_{KE}\)) is assumed to be **0.5** for most industries (including electricity), and set to **0.0** for coal, oil, gas, petroleum/coal products, and agriculture/forestry/fishery. The top-level energy-capital substitution elasticity \(\sigma_{EK}\) is derived as \(0.5/S_{EF}\) (where \(S_{EF}\) is the cost share of aggregate energy-primary-factors), which is necessarily greater than 0.5. Inter-fuel substitution elasticities: electricity vs. non-electricity \(\sigma_{GEN} = 1\); the aggregation of non-electric energy sources uses \(\sigma_{GENNE} = 0.5\). Long-run inter-fuel substitution elasticities can be as high as 2.0; short-run as low as 0.25.
- **Source:** Truong Truong (or GTAP team), "GTAP-E: An Energy-Environmental Version of the GTAP Model," DIW Berlin Discussion Paper 668, https://www.diw.de/documents/publikationen/73/55787/dp668.pdf
- **Source (identical content, alternate host):** "GTAP-E: An Energy-Environmental Version of the GTAP Model," technical paper, LEDS GP, https://ledsgp.org/app/uploads/2015/09/gtap-e-technical-paper.pdf
- **Related GTAP resource on re-estimating these values:** O'Reilly, Humphreys & Prendiville, "Estimating Energy Substitution Parameters in GTAP-E" (using OECD panel data 2005–2016, across 32 countries and 16 sectors, finding that GTAP-E's default same-value-across-all-sectors-and-countries assumption is empirically unsupported), GTAP Resource, https://www.gtap.agecon.purdue.edu/resources/res_display.asp?RecordID=6561

### 2.2 Germany — nested CES estimates

**Claim:** For West German industry, capital, energy, and labour are found to be substitutes in the long run; substitution opportunities between capital and energy lie in the range **0.4 to 0.8** in most nesting specifications.
- **Source:** Claudia Kemfert, "Estimated substitution elasticities of a nested CES production function approach for Germany," *Energy Economics* 20(3), 1998, pp. 249–264, DOI: 10.1016/S0140-9883(97)00014-5, https://www.sciencedirect.com/science/article/pii/S0140988397000145

**Claim:** A 2019 replication/update of Kemfert (1998) using new German industry data (1991–2014) finds elasticities of substitution ranging from close to zero (Leontief-like) to effectively infinite depending on nesting structure and sub-sector, with large standard errors; the authors conclude that none of the estimated elasticities (old or new dataset) are reliable enough for policy modeling use.
- **Source:** Arne Henningsen, Géraldine Henningsen & Edwin van der Werf, "Capital-labour-energy substitution in a nested CES framework: A replication and update of Kemfert (1998)," *Energy Economics* 82, 2019, pp. 16–25, https://backend.orbit.dtu.dk/ws/files/149724340/melju_1_s2.0_S0140988317304395_main.pdf

### 2.3 UK — nested CES estimates

**Claim:** In the same Henningsen, Henningsen & van der Werf (2019) replication, for the (KL)E nesting structure, the elasticity of substitution between energy and other inputs found in prior UK-focused studies ranges as low as **0.0061** (near-Leontief) for the UK — indicating energy and the capital-labour composite are close to perfect complements in that specification.
- **Source:** Henningsen, Henningsen & van der Werf (2019), *Energy Economics* 82, https://backend.orbit.dtu.dk/ws/files/149724340/melju_1_s2.0_S0140988317304395_main.pdf

**Claim:** A UK Energy Research Centre technical review concludes that for the UK, capital (K) and energy (E) generally appear as substitutes, with the average overall estimated elasticity of substitution between K and E of about **0.5 to 0.6** across the small number of available CES estimates; more broadly, energy and capital "typically appear to be either complements (AES<0) or weak substitutes (0<AES<0.5)."
- **Source:** UK Energy Research Centre, "Review of evidence for the rebound effect — Technical Report 3: Elasticity of Substitution Studies," https://d2e1qxpsswcpgz.cloudfront.net/uploads/2020/03/ukerc-review-of-evidence-for-the-rebound-effect-technical-report-3-elasticity-of-substitution-studies.pdf

### 2.4 United States — nested CES / manufacturing sector estimates

**Claim:** A US manufacturing sector (2-digit SIC industries, 1971–1976 data) study finds the elasticity of substitution between capital and energy (\(\sigma_{K,E}\)) ranging from **–0.57 to 0.47** across industries, and between the capital-energy composite and labour (\(\sigma_{KE,L}\)) ranging from **0.21 to 1.58**; capital and energy are found to be slight engineering substitutes but economic complements.
- **Source:** M. Prywes, "A nested CES approach to capital-energy substitution," *Energy Economics*, 1986, cited and reproduced in Kiel Institute working paper "Production Functions for Climate Policy Modeling," https://www.kielinstitut.de/fileadmin/Dateiverwaltung/IfW-Publications/fis-import/1f1b4ac5-5bbb-4f1b-b161-af3180a9c2ee-kap1316.pdf

**Claim:** A meta-regression analysis of capital-labor elasticity of substitution estimates (3,186 estimates from 121 studies) finds a mean reported estimate across the literature of **0.9**, but a best-practice-corrected (conditional on no publication bias, disaggregated data, and inclusion of the capital first-order condition) meta-analytic estimate of only **0.3**.
- **Source:** Sebastian Gechert, Tomás Havránek, Zuzana Iršová & Dominika Kolcunová, "Measuring Capital-Labor Substitution: The Importance of Method Choices and Publication Biases," *Review of Economic Dynamics* 45, 2022, https://meta-analysis.cz/sigma/ ; full paper PDF: http://meta-analysis.cz/sigma/sigma.pdf

**Claim:** A separate meta-regression on the long-run, aggregate-economy elasticity of substitution between capital and labour finds a meta-elasticity range of **0.45–0.87**, rejecting a unitary (Cobb-Douglas) elasticity.
- **Source:** Andreas Knoblach, Fabian Roßner et al. (exact authorship per PDF), "The Elasticity of Substitution Between Capital and Labour in the US Economy: A Meta-Regression Analysis," http://groupelavigne.free.fr/knoblach2019.pdf

### 2.5 China — nested CES estimates (capital-labor-energy)

**Claim:** For China 1979–2006, using normalized nested CES production functions, all estimated substitution elasticities are positive. For the widely used (K,L)E structure, the substitution elasticity between capital and labor for China is estimated **below unity**; when human-capital-adjusted labor is used instead of raw labor, the capital-labor elasticity becomes even lower. The paper concludes the (E,L)K nesting structure is statistically more appropriate for China than (K,L)E.
- **Source:** Keting Shen & John Whalley, "Capital-Labor-Energy Substitution in Nested CES Production Functions for China," NBER Working Paper 19104, June 2013, https://www.nber.org/papers/w19104 ; full text: https://www.nber.org/system/files/working_papers/w19104/w19104.pdf

### 2.6 Meta-analysis of capital-energy substitution and shifts in factor demand

**Claim:** A meta-regression analysis distinguishing Morishima elasticities (technological substitution potential) from cross-price elasticities (actual factor-demand response) finds technological substitution potential is large — especially in the long run for North America — but cross-price elasticities suggesting actual capital-energy substitutability are smaller and, in the short/medium run, not statistically different from zero.
- **Source:** David Koetse, Henri de Groot & Raymond Florax, "Capital-Energy Substitution and Shifts in Factor Demand: A Meta-Analysis," Tinbergen Institute Discussion Paper 2006-061, https://ideas.repec.org/p/tin/wpaper/20060061.html ; published version: *Energy Economics* 30(5), 2008, pp. 2236–2251, https://ideas.repec.org/a/eee/eneeco/v30y2008i5p2236-2251.html ; full PDF: https://www.econstor.eu/bitstream/10419/86262/1/06-061.pdf

### 2.7 Three-level CES nesting structure comparison (general survey)

**Claim:** A review of nested CES energy-substitution studies (van der Werf 2008; 12-country OECD industry panel, 1978–1996) finds the (KL)E nesting structure (capital and labor combined first, then combined with energy) fits the OECD industry data best, with country-level estimates of the energy/(capital-labor) elasticity of substitution ranging from **0.12 to 0.77**, and capital-labor elasticities ranging from **0.35 to 0.63** across countries (0.27–0.65 across industries).
- **Source:** Edwin van der Werf, "Production Functions for Climate Policy Modeling: An Empirical Analysis," Kiel Institute working paper / published in *Energy Economics* 30(6), 2008, pp. 2964–2979, https://d-nb.info/1128231875/34
- **Source (survey citing the same결과):** Nathaniel Mark / Wan et al., "Estimating elasticities of substitution with nested CES production functions: Where do we stand?" *Energy Economics* 88, 2020, https://www3.nd.edu/~nmark/Climate/NestedCES.pdf

---

## 3. Robot Density (IFR World Robotics) and China Manufacturing TFP Data Availability

### 3.1 Latest published IFR robot density figures

**Claim (2023 data, published World Robotics 2024 report, Sept 2024):**
- South Korea: **1,012** robots per 10,000 manufacturing employees (world's highest)
- Singapore: **730** units
- China: **470** units (3rd place — surpassed Germany and Japan for the first time; up from 392 in 2022)
- Germany: **429** units
- Japan: **419** units
- United States: **295** units (ranked 10th worldwide)
- World average: **162** units (more than double the 74 units recorded seven years earlier)
- **Source:** IFR, "Global Robot Density in Factories Doubled in Seven Years," press release, 20 Nov 2024, https://ifr.org/ifr-press-releases/news/global-robot-density-in-factories-doubled-in-seven-years
- **Source:** IFR, World Robotics 2024 press conference deck, https://ifr.org/img/worldrobotics/Press_Conference_2024.pdf

**Claim (updated 2024 data, published World Robotics 2025 report, per IFR April 2026 press release — most recent figures available):**
- South Korea: **1,220** robots per 10,000 employees (growing 7% CAGR since 2019)
- Singapore: **818** units
- Western Europe average: **267** units
- North America average: **204** units
- United States: **307** units (ranked 8th worldwide)
- China: **166** robots per 10,000 employees, +17% YoY — NOTE: this figure reflects a **methodology revision** by China's National Bureau of Statistics to the manufacturing employment denominator, causing China's density ranking to fall to 22nd worldwide / 6th in Asia despite continued absolute robot stock growth. (This is a large discontinuity vs. the 470/2023 figure above — flagged explicitly for cross-checking.)
- Asia average: **131** units per 10,000 (2024)
- China's annual installations 2024: **295,000** units (54% of global total; world record)
- China's total operational robot stock end-2024: exceeds **2,027,000** units (a world record, more than any other single country)
- **Source:** IFR, "Robot Density Surges in Europe, Asia, and Americas," press release, https://ifr.org/news/robot-density-surges-in-europe-asia-and-americas/ (also mirrored at https://ifr.org/ifr-press-releases/news/robot-density-surges-in-europe-asia-and-americas)
- **Source:** IFR, "China Tops World Record of 2 Million Factory Robots," press release, 25 Sept 2025, https://ifr.org/downloads/press_docs/2025-09-25-IFR_press_release_China_in_English.pdf
- **Source:** IFR, World Robotics 2025 Executive Summary — Industrial Robots, https://ifr.org/img/worldrobotics/Executive_Summary_WR_2025_Industrial_Robots.pdf
- **Source:** IFR, World Robotics 2025 report landing page, https://ifr.org/worldrobotics/report-2025

**Note on data discontinuity:** The China robot-density figure dropped sharply between the two IFR releases (470/2023 vs. 166/2024) due to an NBS denominator revision, not a real decline in automation. Any Bayesian model using this series as an input must treat 2023 and 2024+ density figures as **methodologically non-comparable** without adjustment. This is an important caveat for model specification.

### 3.2 China manufacturing-specific TFP data availability

**Finding: No single, continuously updated, official NBS manufacturing-sector-specific TFP index exists that is directly comparable to US BLS/BEA multifactor productivity series.** What is available:

1. **Penn World Table (PWT) 10.01/11.0** — provides an *aggregate national* (not manufacturing-specific) TFP index for China ("Total Factor Productivity at Constant National Prices"), maintained by University of Groningen/UC Davis, republished via FRED.
   - **Source:** FRED series RTFPNACNA632NRUG, "Total Factor Productivity at Constant National Prices for China," Penn World Table 11.0 release, https://fred.stlouisfed.org/series/RTFPNACNA632NRUG (index 2021=1; annual; covers 1956–2023 as of latest vintage)
   - **Source:** Penn World Table 11.0 release notes, https://alfred.stlouisfed.org/release?rid=285

2. **Academic reconstructions using NBS firm-level microdata** — several papers construct manufacturing TFP series from NBS's Annual Industrial Enterprise Survey (firms with sales above RMB 5m before 2010, RMB 20m thereafter), but these are academic one-off reconstructions, not an official ongoing published series:
   - Bin Xu / muse.jhu.edu, "Recent Productivity Trends in China: Evidence from Macro and Micro Data," using NBS Annual Industrial Enterprise Survey panel, https://muse.jhu.edu/pub/43/article/848481/pdf — reports manufacturing TFP growth slowing from an earlier period to **1.1% per year in 2007–2013**.
   - "Total Factor Productivity in China's Manufacturing Sector in the Aftermath of the Global Financial Crisis," *China & World Economy* 31(2), 2023, pp. 1–25, DOI via Wiley: https://onlinelibrary.wiley.com/doi/abs/10.1111/cwe.12466 (IDEAS/RePEc record: https://ideas.repec.org/a/bla/chinae/v31y2023i2p1-25.html)
   - "Total factor productivity of Chinese industrial firms: evidence from 2007 to 2017," using the National Taxation Survey Database (NTSD), *Applied Economics*, 26 Dec 2021, reports weighted TFP rising from 3.65 (2007) to 4.69 (2017), average growth 2.58%/year, https://www.tandfonline.com/doi/full/10.1080/00036846.2021.1954592
   - "Where has all the dynamism gone? Productivity growth in China's [manufacturing]," *Journal of Development Economics* 181, 2026, finds a marked slowdown in revenue-based TFP growth across all industries, ownership types, and regions, flagging **data quality concerns (missing value-added/intermediate-input information, over-reporting)** in official Chinese firm-level statistics, https://ideas.repec.org/a/eee/deveco/v181y2026ics0304387826000039.html

3. **APO (Asian Productivity Organization) Productivity Database** — was referenced as a possible source in the task brief; searches did not surface a currently maintained, publicly accessible APO manufacturing-TFP series specifically isolating China's manufacturing sector at the level of granularity needed. **This should be flagged as a gap**: no confirmed, freely accessible APO manufacturing-specific China TFP series was located in this research pass.

**Bottom line for model specification:** A *manufacturing-sector-specific*, officially published, continuously updated PRC TFP series comparable to US series does **not** appear to exist. The best available options are (a) PWT's aggregate national TFP (not manufacturing-specific), or (b) episodic academic reconstructions from NBS/NTSD firm microdata that are not update-consistent across years and carry documented data-quality caveats. Any Bayesian model requiring a manufacturing TFP input for China should treat this as a **structurally uncertain / proxy-only input** and consider explicitly modeling this uncertainty (e.g., via a wide prior or by using firm-level reconstructions with quality caveats stated).

---

## 4. Small-N Validation Literature and Historical Retrodiction Failures of Power-Transition/Declinism Models

### 4.1 Small-n calibration vs. validation — general Bayesian methodology (not history-specific)

No literature was found specifically merging Bayesian calibration/validation methodology with small-n (~5–8 case) macro-historical power-transition modeling as a named subfield. The closest generically relevant methodological sources on Bayesian calibration-vs-validation trade-offs are drawn from general statistics/model-validation literature (not historical political science), and should be treated as methodological analogies rather than direct precedent:
- Tohme, Vanslette & Youcef-Toumi, "A Generalized Bayesian Approach to Model Calibration," arXiv:1911.11715, 2019, https://arxiv.org/abs/1911.11715 (frames calibration and validation as complementary, distinguishes least-squares/likelihood/Bayesian calibration).
- General Bayesian sample-size/validation framework paper (biomedical context, illustrative of the calibration-vs-validation distinction under small samples), arXiv:2504.15923, https://arxiv.org/html/2504.15923v1

**Gap noted:** No direct political-science or IR-specific literature was found explicitly framing "small-n Bayesian calibration vs. validation" for power-transition-style models with ~5–8 great-power cases. This appears to be a genuine gap in the published literature — the field instead relies on frequentist statistical testing (logistic/probit regression on dyad-year panels) rather than explicit Bayesian small-n frameworks. This should be stated explicitly as "not locatable" rather than invented.

### 4.2 Power Transition Theory — empirical testing literature (frequentist, not small-n Bayesian, but the closest extant validation tradition)

**Claim:** Organski & Kugler's original empirical tests (1980) found support for power transition theory predicting major war, but the theory has been tested and re-tested with mixed results depending on capability measure and case selection (Correlates of War composite index vs. GDP) and on which "major powers" are included in the sample.
- **Source:** Jacek Kugler & A.F.K. Organski, Chapter 7 (untitled paper on power transition, 30-year retrospective), https://www.acsu.buffalo.edu/~fczagare/PSC%20346/Kugler%20and%20Organski.pdf
- **Source:** Indra de Soysa, John R. Oneal & Yong-Hee Park, "Testing Power-Transition Theory Using Alternative Measures of National Capabilities," *Journal of Conflict Resolution* 41(4), 1997, pp. 509–528, DOI: 10.1177/0022002797041004002, https://journals.sagepub.com/doi/10.1177/0022002797041004002 — explicitly finds "the strength of the evidence depends importantly on how power is measured and the set of cases analyzed."
- **Source:** Jacek Kugler (or similar), "Power Transition Theory and the End of the Cold War," *Journal of Peace Research* 34(1), 1997, https://journals.sagepub.com/doi/10.1177/0022343397034001003
- **Source:** Jonathan M. DiCicco, "Power Transition Theory and the Essence of Revisionism," survey paper reviewing 60 years of PTT hypothesis-testing, https://www.acsu.buffalo.edu/~fczagare/PSC%20504/DiCicco%20PT%20and%20Revisionism.pdf

### 4.3 Historical episodes of predicted-but-not-realized US decline

**Episode 1 — Sputnik, 1957:** The Soviet launch of Sputnik I (4 October 1957) triggered a US "declinist" panic that Soviet science/technology and by extension Soviet national power had overtaken the US; this fed the "missile gap" political narrative used in the 1960 election, even though a Nov 1957 National Intelligence Estimate later proved to have overstated the near-term Soviet ICBM buildout.
- **Source:** US Department of State, Office of the Historian, "Sputnik, 1957," https://history.state.gov/milestones/1953-1960/sputnik
- **Source:** Wikipedia summary with citations, "Sputnik crisis," https://en.wikipedia.org/wiki/Sputnik_crisis
- **Source (academic historiographical framing explicitly tying Sputnik to the declinism cycle Huntington later catalogued):** Tim Barker, "Histories of Decline," *Phenomenal World*, 29 May 2026, https://phenomenalworld.org/analysis/histories-of-decline/ — explicitly frames Sputnik as the first of Huntington's "waves of declinism."

**Episode 2 — 1970s stagflation / Japan challenge:** Huntington identifies the 1970s energy crisis and Vietnam-era retrenchment debates, and later the "Japan as No. 1" narrative, as the second and (with Kennedy's book) culminating waves of US declinism.
- **Source:** Samuel P. Huntington, "The U.S.—Decline or Renewal?" *Foreign Affairs* 67(2), Winter 1988/89, pp. 76–96, https://contemporarythinkers.org/samuel-huntington/essay/the-u-s-decline-or-renewal/ (also JSTOR stable URL cited in secondary sources: http://www.jstor.org/stable/20043774). Huntington's key claim, directly quotable: "In 1988 the United States reached the zenith of its fifth wave of declinism since the 1950s."

**Episode 3 — Late-1980s declinism debate (Kennedy vs. Nye/Huntington/Nau):**

**Claim:** Paul Kennedy's *The Rise and Fall of the Great Powers: Economic Change and Military Conflict from 1500 to 2000* (Random House, 1987) argued that "imperial overstretch" would produce relative US decline as productive/economic power shifted toward Japan and the Pacific region, and predicted decline for both the US and USSR.
- **Source:** Wikipedia summary with extensive citation trail, "The Rise and Fall of the Great Powers," https://en.wikipedia.org/wiki/The_Rise_and_Fall_of_the_Great_Powers
- **Primary bibliographic reference:** Paul Kennedy, *The Rise and Fall of the Great Powers: Economic Change and Military Conflict from 1500 to 2000* (New York: Random House, 1987).

**Claim (direct rebuttal, published concurrently):** Joseph S. Nye Jr.'s *Bound to Lead: The Changing Nature of American Power* (Basic Books, 1990) directly rebutted Kennedy, arguing the US retained sufficient "hard" and "soft" power resources and that decline was a matter of political will ("wallet"), not capability.
- **Primary bibliographic reference:** Joseph S. Nye Jr., *Bound to Lead: The Changing Nature of American Power* (New York: Basic Books, 1990); full text hosted at https://www.kropfpolisci.com/exceptionalism.nye.pdf and https://archive.org/stream/AmericanPowerAndWorldOrderCHRISTIANREUSSMIT/Bound%20to%20lead%20%20the%20changing%20nature%20of%20American%20power%20-%20%20Joseph%20Nye_djvu.txt

**Claim (direct rebuttal, published concurrently):** Samuel P. Huntington's "The U.S.—Decline or Renewal?" (*Foreign Affairs*, Winter 1988/89) argued the declinism narrative was a recurring five-decade cyclical phenomenon that had repeatedly proven wrong, and that declinism itself served a useful political function by mobilizing renewal efforts.
- **Primary bibliographic reference:** Samuel P. Huntington, "The U.S.—Decline or Renewal?" *Foreign Affairs* 67(2), Winter 1988/89, pp. 76–96, https://contemporarythinkers.org/samuel-huntington/essay/the-u-s-decline-or-renewal/

**Claim (direct rebuttal, published concurrently):** Henry R. Nau's *The Myth of America's Decline: Leading the World Economy into the 1990s* (Oxford University Press, 1990) and his later retrospective article argue Kennedy's predictions "have not fared well" except regarding Russia, because Kennedy's realist model ignored the role of national identity/domestic institutions.
- **Source:** Henry R. Nau, "Why 'The Rise and Fall of the Great Powers' was wrong," retrospective journal article, https://library.fes.de/libalt/journals/swetsfulltext/12119495.pdf

**Retrospective academic assessment (post-hoc, confirming the retrodiction-failure pattern):** A 2023 LSE US Centre blog retrospective by Michael Cox notes the book "has remained relevant" for 35+ years precisely because its 1987 predictions about near-term US/USSR decline did not play out as forecast on the original timeline, while noting Kennedy failed to foresee the USSR's 1991 collapse just four years after publication.
- **Source:** Michael Cox, "For over 30 years, Paul Kennedy's *The Rise and Fall of the Great Powers* has been the backdrop of the shifting debate over American power," LSE US Centre blog, 4 Dec 2023, https://blogs.lse.ac.uk/usappblog/2023/12/04/long-read-for-over-30-years-paul-kennedys-the-rise-and-fall-of-the-great-powers-has-been-the-backdrop-of-the-shifting-debate-over-american-power/

**Direct Kennedy-Nye exchange (contemporaneous critique-and-response, primary source):**
- **Source:** Paul Kennedy & Joseph S. Nye, "Is the US Declining?" (exchange of letters/reviews), *The New York Review of Books*, 11 Oct 1990, https://www.nybooks.com/articles/1990/10/11/is-the-us-declining/
- **Source:** Paul Kennedy, "Fin-de-Siècle America," *The New York Review of Books*, 28 June 1990 (reviewing Nye's *Bound to Lead*), https://www.nybooks.com/articles/1990/06/28/fin-de-siecle-america/

---

## 5. Latest (2025–2026) Baseline Figures for Cross-Checking

### 5.1 US electricity generation capacity additions

**Claim:** US utility-scale electric generating capacity additions reached **53 GW in 2025** (largest single-year increase since 2002), with a **record 86 GW projected for 2026** — solar accounting for 51% (43.4 GW), battery storage 28% (24.3 GW), and wind 14% (11.8 GW) of the 2026 total.
- **Source:** US EIA, "New U.S. electric generating capacity expected to reach a record high in 2026," *Today in Energy*, 13 Aug 2026 (report date as indexed), https://www.eia.gov/todayinenergy/detail.php?id=67205
- **Source:** EIA, "Electric Power Annual" / Table 4.5, "Planned Utility-Scale Generating Capacity Changes, by Energy Source, 2025–2029," https://www.eia.gov/electricity/annual/html/epa_04_05.html
- **Claim:** Total US electricity generation reached a record **4,260 billion kWh (2025)**, with 2026 forecast growth of 1.1% and 2027 growth of 2.6% (reaching 4,423 BkWh).
- **Source:** EIA, "Solar power generation drives electricity generation growth over the next two years," *Today in Energy*, https://www.eia.gov/todayinenergy/detail.php?id=67005

### 5.2 China electricity generation capacity additions

**Claim:** China added a record **543 GW of new power generation capacity of all types in 2025** (net additions ~540 GW, pushing total installed capacity from ~3.35 TW end-2024 to **3.89 TW end-2025**, +16.1% YoY), including **315 GW of new solar** and **119 GW of new wind** capacity (both new annual records). Combined wind+solar installed capacity surpassed **1.84 billion kW (1.84 TW)**, exceeding thermal (coal+gas) generating capacity for the first time in China's history, and accounting for 47.3% of total installed capacity. Including hydro and nuclear, non-fossil sources reached 60.4% of total installed capacity vs. 39.6% for thermal.
- **Source:** China's State Council / National Energy Administration (NEA), "China's newly installed wind, solar power capacity up 22 pct in 2025," 12 Feb 2026, https://english.www.gov.cn/archive/statistics/202602/12/content_WS698d93cbc6d00ca5f9a091bb.html
- **Source:** pv magazine, "China adds 315 GW of solar in 2025," 28 Jan 2026 (citing NEA data release), https://www.pv-magazine.com/2026/01/28/china-adds-315-gw-of-solar-in-2025/
- **Source:** Carbon Credits, "China Adds Power 8x More Than the US in 2025," 4 Feb 2026, https://carboncredits.com/china-adds-power-7x-more-than-the-us-in-2025-with-500b-energy-build-out-in-a-single-year/
- **Source (Ember cross-check):** Ember, *Global Electricity Review 2026*, "Major Countries and Regions" chapter, 22 June 2026, https://ember-energy.org/latest-insights/global-electricity-review-2026/major-countries-and-regions/ — reports China's electricity demand grew 5% (+503 TWh) in 2025 to 10,573 TWh (a third of global demand); clean generation growth (+561 TWh, +15%) fully met demand growth; wind+solar reached 22% of China's generation mix; China accounted for 58% of global solar installations (378 GW DC) and 72% of global wind installations (119 GW) in 2025; China's fossil generation fell for the first time in a decade (-56 TWh, -0.9%).
- **Source (Ember, US cross-check):** same Ember report — US electricity demand grew 3% (+131 TWh) in 2025; solar met 65% of the demand increase (+85 TWh, +28% growth); wind+solar together met 74% of US demand growth; US coal generation rose 13% (+85 TWh) while gas fell 3.4%.

### 5.3 China augmented fiscal debt as % of GDP (IMF Article IV)

**Claim (most recent IMF Article IV, 2025 consultation, published ~Feb 2026):** China's Augmented Debt (which includes local government financing vehicle/LGFV debt and other off-budget government funds) is projected/estimated at:
- 2023: **126.6%** of GDP
- 2024: **135.3%** of GDP
- 2025: **141.5%** of GDP
- 2026 (projected): **146.2%** of GDP
- Later years in the IMF's projection path: **150.0%**, then **153.7%** of GDP
Additionally, China's official headline fiscal deficit widened to **4% of GDP in 2025** (from 3% in 2024), and the augmented cyclically-adjusted primary balance (CAPB) is expected to decline by 0.9 percentage points relative to 2024.
- **Source:** IMF, "People's Republic of China: 2025 Article IV Consultation," IMF Country Report No. 2026/001, https://www.imf.org/-/media/files/publications/cr/2026/english/1chnea2026001-source-pdf.pdf

**Cross-check / alternative estimate (independent think-tank analysis, using a different "augmented deficit" definition covering central+local government spending):** Rhodium Group estimates China's overall government deficit (central + local, on a broader cash basis) reached **9.0% of GDP for full-year 2025**, with a possible widening to **9.5–10.0% of GDP in 2026** if revenue declines continue. Note: this figure is not directly comparable to the IMF's augmented-debt-stock percentages above — it is a flow (deficit) measure using a different methodology, not the debt-stock figure.
- **Source:** Rhodium Group, "China's Financial and Fiscal Decay," 3 March 2026, https://rhg.com/research/chinas-financial-and-fiscal-decay/

**Earlier data point (prior-year IMF Article IV, for trend context):** As of the 2024 IMF Article IV consultation, China's general government (non-augmented) debt was estimated at 60.5% of GDP in 2024 (up from 38.5% in 2019); augmented debt (incl. LGFVs) was 124% of GDP (up from 86.3% in 2019); overall non-financial-sector debt reached 312% of GDP (up from 245% in 2019).
- **Source:** OMFIF, "China has just raised its debt ceiling," 11 March 2025, citing IMF Article IV mid-2024 consultation data, https://www.omfif.org/2025/03/china-has-just-raised-its-debt-ceiling/

### 5.4 AI compute share estimates (Epoch AI / CSET / Federal Reserve)

**Claim (most current, Epoch AI, May 2025 dataset — the standard reference figure cited across multiple secondary sources as of 2025–2026):** The United States hosts approximately **74.5%** of global AI-supercomputer/GPU-cluster performance; China holds **14.1%**; the EU **4.8%**; Norway **1.8%**; Japan **1.4%**.
- **Source:** Epoch AI, "The US hosts the majority of GPU cluster performance, followed by China," data insight, https://epoch.ai/data-insights/ai-supercomputers-performance-share-by-country
- **Source:** Epoch AI, "Trends in AI supercomputers," https://epoch.ai/publications/trends-in-ai-supercomputers — additionally reports that private industry's share of total AI-supercomputer computing power rose from ~40% (2019) to ~80% (2025).

**Cross-check (Federal Reserve, using same underlying Epoch-style methodology):** The Federal Reserve's FEDS Notes report the US controls an estimated **74%** of global high-end AI compute, China **14%**, and the EU **4.8%** — consistent with the Epoch AI figures.
- **Source:** Federal Reserve Board, "The State of AI Competition in Advanced Economies," FEDS Notes, 10 June 2025 (indexed), https://www.federalreserve.gov/econres/notes/feds-notes/the-state-of-ai-competition-in-advanced-economies-20251006.html

**Cross-check (CSET/RAND-adjacent estimate):** RAND's 2025 analysis on China's AI industrial policy states China controls "about 15 percent of total AI compute, while the United States controls about 75 percent" — consistent with Epoch AI figures.
- **Source:** RAND Corporation, "Full Stack: China's Evolving Industrial Policy for AI," RAND Perspective PEA4012-1, 26 June 2025, https://www.rand.org/pubs/perspectives/PEA4012-1.html

**Cross-check (CSIS compute-accelerator-count methodology, a different metric — accelerator units rather than FLOPs/cluster performance):** CSIS estimates that by end of 2025, the US will hold approximately **14.31 million AI accelerators** vs. China's approximately **4.6–4.8 million**, a roughly threefold numerical advantage that widens further when accounting for higher per-chip performance of US-deployed accelerators.
- **Source:** CSIS, "Securing the AGI Laurel: Export Controls, the Compute Gap, and China's Counterstrategy," 26 Feb 2025, https://www.csis.org/analysis/securing-agi-laurel-export-controls-compute-gap-and-chinas-counterstrategy

**Additional recent data point (Epoch AI, chip-smuggling estimate, most recent as of the search date):** Epoch AI estimates that between 290,000 and 1.6 million H100-equivalent GPUs (median estimate: 660,000) were smuggled into China through 2025, representing roughly **one-third of China's total AI compute stock** and about 3% of global compute — meaning China's true effective compute share (including smuggled/undetected chips) is likely somewhat higher than the ~14% "observed" figure, though Epoch AI explicitly cautions its dataset covers only 10–20% of total global AI compute and detects only ~2% of China's export-controlled chips.
- **Source:** Epoch AI, "The Geopolitics of AI: Data & Research" hub page, updated 29 April 2026, https://epoch.ai/topics/geopolitics
- **Source:** Epoch AI, "How much AI compute has been smuggled to China?" research note / X thread, 30 April 2026, https://x.com/EpochAIResearch/status/2049924785153638761

**Ownership-based cross-check (Epoch AI Chip Owners Explorer):** As of end-2025, Chinese companies collectively own only about **5%** of the cumulative computing power of leading AI chips sold globally (excluding smuggled/offshore-rented compute) — a declining share over time due to export controls — while the top five US hyperscalers (Amazon, Google, Meta, Microsoft, Oracle) collectively own an estimated **71%** of world cumulative AI compute as of Q4 2025 (up from 63% in Q1 2024).
- **Source:** Epoch AI, "Introducing the AI Chip Owners Explorer," Substack post, 6 April 2026, https://epochai.substack.com/p/introducing-the-ai-chip-owners-explorer

**Note on CSET specifically:** Georgetown's Center for Security and Emerging Technology (CSET) was named in the task brief as a target source, but this research pass did not surface a distinct, dated 2025/2026 CSET compute-share estimate independent of the Epoch AI/RAND/Federal Reserve figures cited above (several secondary sources reference "Epoch AI, CSET" jointly without a separately attributable CSET number). This should be flagged: **no standalone, distinctly-sourced CSET compute-share figure for 2025–2026 was independently located and verified in this pass** — the figures above should be attributed to Epoch AI (and cross-checked via Federal Reserve/RAND/CSIS), not CSET, unless a specific CSET publication is separately located.

---

## Summary of What Was Found vs. Not Found

**Found with high confidence (primary/near-primary sources, multiple corroborating citations):**
- Full Turchin PSI specification (MMP, EMP, SFD formulas, exact variable definitions) from *Ages of Discord* and multiple derivative Cliodynamics/PLOS papers, plus four distinct published critiques (circularity, algebraic non-independence of EMP from relative wage, poor external validity in non-US cases, empirical failure of core SDT predictions for the US 1960–2020).
- A rich set of point estimates for energy-capital(-labor) elasticity of substitution: GTAP-E's assumed values (0.5 inner nest, sector exceptions at 0.0), Germany (Kemfert 1998: 0.4–0.8; Henningsen et al. 2019 replication showing instability of estimates), UK (near-zero to ~0.5–0.6 depending on study), US (meta-analytic capital-labor elasticity 0.3–0.9 depending on correction; industry-specific energy-capital range −0.57 to 1.58), China (Shen & Whalley 2013 NBER, capital-labor elasticity below unity, (E,L)K nesting preferred), plus two meta-analyses (Gechert et al. 2022; Koetse et al. 2008).
- IFR World Robotics figures for China, US, South Korea (both 2023 and 2024 report vintages), with an important flagged discontinuity in China's density figure due to an NBS denominator/methodology revision.
- Extensive historical sourcing for the Sputnik (1957), 1970s, and late-1980s (Kennedy/Nye/Huntington/Nau) declinism episodes, including primary bibliographic references and direct contemporaneous rebuttal texts.
- Current (2025–2026) figures for US and China electricity capacity additions (EIA, NEA/State Council, Ember), China's IMF Article IV augmented debt trajectory (126.6% of GDP in 2023 rising to a projected 153.7%), and AI compute share (Epoch AI: US ~74.5%, China ~14.1%, cross-checked via Federal Reserve, RAND, and CSIS).

**Explicitly not found / could not be located (stated rather than invented):**
1. No continuously updated, officially published, manufacturing-sector-specific PRC TFP series comparable to US series — only an aggregate national PWT TFP index and episodic, non-continuous academic reconstructions from NBS/NTSD firm microdata (with documented data-quality caveats) exist.
2. No confirmed, accessible APO Productivity Database series isolating China manufacturing TFP was located.
3. No political-science/IR-specific literature explicitly framing "Bayesian calibration vs. validation for small-n (~5–8 case) power-transition models" was found; the extant empirical power-transition-theory testing literature is frequentist (regression-based), not Bayesian small-n in the sense implied by the task.
4. No standalone, independently attributable CSET (Georgetown) 2025/2026 AI compute-share estimate distinct from Epoch AI's figures was located — secondary sources cite "Epoch AI, CSET" together without a separable CSET number.
