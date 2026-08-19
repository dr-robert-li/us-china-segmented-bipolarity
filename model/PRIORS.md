# Priors

Every prior in the model, with its source, its justification, and the sensitivity check that establishes whether the posterior depends on it.

Committed before estimation. A prior chosen after seeing a posterior is not a prior.

Two rules govern this file:

1. **No prior is chosen for convenience.** Where a prior is weakly informative because the literature offers nothing better, it is labelled as such rather than dressed as substantive.
2. **Every prior that could plausibly determine a headline result carries a mandatory sensitivity run.** The list of such priors is fixed in section 7 and may not be shortened.

---

## 1. The elasticity priors and why they are sub-unitary

The substitution elasticities are the parameters on which the central empirical question turns, and the published literature is unusually clear about their location: estimates cluster **below unity**, which is to say the Cobb-Douglas assumption of unit elasticity is empirically rejected in most careful work.

| Estimate | Context | Source |
|---|---|---|
| 0.5 | Capital-energy inner nest, assumed value for most industries including electricity; 0.0 for coal, oil, gas, petroleum products, agriculture | [GTAP-E technical paper](https://www.diw.de/documents/publikationen/73/55787/dp668.pdf) |
| 0.4-0.8 | Capital-energy substitution, West German industry, most nesting specifications | [Kemfert, *Energy Economics* 20(3), 1998](https://www.sciencedirect.com/science/article/pii/S0140988397000145) |
| 0.0061 to effectively unbounded | Energy against the capital-labour composite, `(KL)E` nesting, replication of Kemfert on 1991-2014 German data; authors conclude none of the estimates old or new is reliable enough for policy modelling | [Henningsen, Henningsen and van der Werf, *Energy Economics* 82, 2019](https://backend.orbit.dtu.dk/ws/files/149724340/melju_1_s2.0_S0140988317304395_main.pdf) |
| 0.5-0.6 | Capital-energy, UK average across the small number of available CES estimates; broader finding that energy and capital are complements or weak substitutes | [UKERC, Review of evidence for the rebound effect, Technical Report 3](https://d2e1qxpsswcpgz.cloudfront.net/uploads/2020/03/ukerc-review-of-evidence-for-the-rebound-effect-technical-report-3-elasticity-of-substitution-studies.pdf) |
| -0.57 to 0.47 (`sigma_KE`), 0.21 to 1.58 (`sigma_KE,L`) | US manufacturing, 2-digit SIC; capital and energy slight engineering substitutes but economic complements | Prywes 1986, reproduced in [Kiel Institute, Production Functions for Climate Policy Modeling](https://www.kielinstitut.de/fileadmin/Dateiverwaltung/IfW-Publications/fis-import/1f1b4ac5-5bbb-4f1b-b161-af3180a9c2ee-kap1316.pdf) |
| 0.12-0.77 (energy against KL), 0.35-0.63 (capital-labour) | Twelve-country OECD industry panel, 1978-1996; `(KL)E` fits best | [van der Werf, *Energy Economics* 30(6), 2008](https://d-nb.info/1128231875/34) |
| Below unity for capital-labour; lower still with human-capital-adjusted labour; `(E,L)K` nesting statistically preferred over `(K,L)E` | China, 1979-2006, normalised nested CES | [Shen and Whalley, NBER WP 19104](https://www.nber.org/system/files/working_papers/w19104/w19104.pdf) |
| Mean reported 0.9; best-practice-corrected **0.3** | Meta-regression of capital-labour elasticity, 3,186 estimates from 121 studies, correcting for publication bias | [Gechert, Havránek, Iršová and Kolcunová, *Review of Economic Dynamics* 45, 2022](http://meta-analysis.cz/sigma/sigma.pdf) |
| 0.45-0.87 | Meta-regression, long-run aggregate capital-labour elasticity; unitary elasticity rejected | [Knoblach et al., meta-regression analysis](http://groupelavigne.free.fr/knoblach2019.pdf) |
| Large technological substitution potential; cross-price elasticities smaller and not statistically distinguishable from zero in the short and medium run | Meta-analysis distinguishing Morishima from cross-price elasticities | [Koetse, de Groot and Florax, *Energy Economics* 30(5), 2008](https://www.econstor.eu/bitstream/10419/86262/1/06-061.pdf) |

### 1.1 Committed priors

```
sigma_D    ~ LogNormal(log(0.5), 0.45)     within-deployment substitution
sigma_F    ~ LogNormal(log(0.7), 0.50)     within-frontier substitution
sigma_min  = 0.15                          floor on the top elasticity
sigma_max  = 2.5                           ceiling on the top elasticity
sigma_top[2026] ~ LogNormal(log(0.6), 0.55)  initial state
```

The `sigma_D` prior centres on the GTAP-E assumed value of 0.5 and on the Kemfert and UKERC ranges, which agree to a striking degree given they were produced by different methods on different data. Its dispersion is set so that the 90% interval spans roughly 0.24 to 1.05 — wide enough to contain the near-Leontief UK estimate at the lower tail and to admit unit elasticity at the upper.

`sigma_F` is centred higher, at 0.7, because the frontier bundle contains capital depth and human capital, and the capital-labour literature sits above the capital-energy literature: 0.45-0.87 in the long-run meta-regression, 0.3 in the publication-bias-corrected estimate, 0.9 uncorrected. Centring at 0.7 sits between the corrected and uncorrected meta-analytic values. This is a judgement and it is labelled as one.

The two-and-a-half ceiling on `sigma_top` exceeds anything in the table above. It is deliberately generous, because the ceiling has to admit the possibility that AI-robotics substitution behaves unlike any historically estimated factor pair. A ceiling set at the literature's maximum would foreclose the P2-undermining outcome by construction.

### 1.2 Why the Henningsen replication matters more than its numbers

The 2019 replication finds elasticities ranging from near-Leontief to effectively infinite depending on nesting structure and sub-sector, with large standard errors, and the authors conclude that none of the estimates — from the original or the updated data — is reliable enough for policy modelling use. That is a finding about the **identifiability** of nested CES elasticities, not about their values.

Its consequence here is not a wider prior. It is the requirement in `IDENTIFICATION.md` that the elasticity posteriors be reported with contraction diagnostics and that a posterior which has not contracted be reported as **not learned**. A literature in which careful estimates on good data span three orders of magnitude is a literature warning that this parameter may not be recoverable, and the honest response is to make non-recovery a reportable outcome rather than to hide it behind a credible interval that looks decisive because the prior was tight.

### 1.3 Nesting-order prior

Uniform over the three candidate structures in `SPECIFICATION.md` section 6.2. No structure is favoured.

This is a real commitment against interest. The `(D3 F1)(D1 D2)(F2 F3)` embodied-AI structure is the one under which P2 is most naturally true, and a uniform prior gives it equal footing rather than making it earn its way in. Shen and Whalley's finding that the intuitively standard `(K,L)E` ordering loses to `(E,L)K` for China is the reason a uniform prior is defensible: nesting intuitions transfer badly.

---

## 2. The mechanism parameter

```
delta ~ Normal(0, 0.25)
```

Centred at **exactly zero**, symmetric, and the single most consequential prior in the model. P2 is the claim that `delta < 0`. A prior centred at zero means the data must supply the sign.

Any asymmetric prior on `delta` would be indefensible: it would place prior mass on the project's own hypothesis, and every subsequent posterior statement about P2 would be contaminated by it. The scale of 0.25 is chosen so that the prior 90% interval spans roughly -0.41 to 0.41, which in the `logit_s` transition permits `sigma_top` to travel most of its admissible range over fifty years but not to traverse it in a decade.

### 2.1 Contraction gate

```
contraction(delta) = 1 - sd(posterior) / sd(prior)
```

| Contraction | Report |
|---|---|
| `>= 0.30` | `delta` reported as estimated; sign statement permitted |
| `0.10` to `0.30` | Reported as weakly identified; sign statement permitted only with the contraction figure adjacent |
| `< 0.10` | **`delta` reported as not learned.** No sign statement. P2 is reported as untested by the estimation, and rests on F1/F8 alone |

The 0.30 and 0.10 thresholds are frozen from this commit and may not be adjusted after a posterior is computed. This mirrors the freeze discipline in `falsifiers/dependence.md`.

---

## 3. Measurement bias priors

Implementing `SPECIFICATION.md` section 4.

| Series family | Prior | Source |
|---|---|---|
| PRC GDP-linked growth | `b ~ Normal(-1.25pp, 0.45pp)` on annual growth, truncated to [-2.0, -0.5] | The 0.5-2.0pp falsification band in `DATA-INTEGRITY.md`, carried as a range with competing overstatement estimates preserved |
| US fiscal projection paths | `b ~ Normal(0, published error band / 1.645)` | CBO published projection-error bands, so that the prior 90% interval reproduces the published band |
| US inequality measures | `b ~ Normal(0, half the competing-approach spread)` | The Piketty-Saez-Zucman versus Auten-Splinter range, carried rather than resolved |
| PRC augmented debt construction | `b ~ Normal(0, 5pp)` | Observed 7pp spread between augmented constructions, recorded in `falsifiers/log/2026/F3.md` |
| Generation capacity, physically measurable | `b = 0`, `sigma` small | Tier 1 of the `DATA-INTEGRITY.md` hierarchy |
| Independently audited series | `b ~ Normal(0, 0.5 * official-series sd)` | Audit evidences small bias, not zero bias |
| AI compute share estimates | `b ~ Normal(0, 4pp)` on share | Coverage limitation declared by the estimating source, section 4.1 below |
| PRC manufacturing TFP proxy | `b ~ Normal(0, 1.5pp)` on growth, plus a `proxy_only` flag | Section 5 below |

The PRC growth bias prior is the one a hostile reader will check first. It is centred at the midpoint of the pre-registered band and truncated to the band, so it cannot wander outside a range that was fixed before this file existed. Its US counterparts are constructed from published error bands by the same mechanical procedure, which is how the symmetry requirement is met without either side receiving a hand-tuned term.

### 3.1 The compute-share prior is wide for a documented reason

The standard reference figures place the US at roughly 74.5% of global AI-supercomputer performance and China at 14.1% ([Epoch AI](https://epoch.ai/data-insights/ai-supercomputers-performance-share-by-country)), corroborated at 74% and 14% by the Federal Reserve ([FEDS Notes](https://www.federalreserve.gov/econres/notes/feds-notes/the-state-of-ai-competition-in-advanced-economies-20251006.html)) and at roughly 75% and 15% by RAND ([Full Stack: China's Evolving Industrial Policy for AI](https://www.rand.org/pubs/perspectives/PEA4012-1.html)).

Those three agree closely, which is less reassuring than it appears, because they may share a methodology rather than independently confirm a quantity. Two facts widen the prior:

- The estimating source states that its dataset covers only 10-20% of total global AI compute and detects roughly 2% of China's export-controlled chips ([Epoch AI, geopolitics hub](https://epoch.ai/topics/geopolitics)).
- Smuggled capacity is estimated at 290,000 to 1.6 million H100-equivalents through 2025, median 660,000, on the order of one third of China's total AI compute stock ([Epoch AI](https://epoch.ai/topics/geopolitics)).

A different metric — accelerator counts rather than cluster performance — gives roughly 14.31 million US units against 4.6-4.8 million Chinese units, a threefold rather than fivefold ratio ([CSIS](https://www.csis.org/analysis/securing-agi-laurel-export-controls-compute-gap-and-chinas-counterstrategy)). An ownership-based cut gives Chinese companies roughly 5% of cumulative leading-chip compute, with the top five US hyperscalers at roughly 71% ([Epoch AI Chip Owners Explorer](https://epochai.substack.com/p/introducing-the-ai-chip-owners-explorer)).

Three metrics giving 5%, 14%, and 24-33% for the same country is not measurement noise. It is three different definitions of the quantity. The 4pp bias prior handles the noise; the definitional spread is handled by `pipeline/definitions/frontier-compute.md`, and this file does not pretend a prior can substitute for a definition.

### 3.2 Correction to the source attribution in the pre-registration

`falsifiers/PRE-REGISTRATION.md` names "Epoch AI; CSET" as F8's sources. No standalone, separately attributable CSET compute-share estimate for 2025-2026 could be located; secondary sources cite the two jointly without a separable CSET figure.

**This is recorded, not repaired.** The pre-registered source list is not edited, because editing a source list after registration is one of the four prohibited moves in `falsifiers/PRE-REGISTRATION.md`. The correct treatment is that F8's operative source is Epoch AI, cross-checked against the Federal Reserve, RAND and CSIS figures above, and that the CSET naming was aspirational. Any future CSET publication may be added as a cross-check but may not displace the operative source.

---

## 4. Input evolution priors

```
rho_g       ~ Beta(6, 2)                     growth persistence, centred near 0.75
gstar[j,i]  ~ Normal(historical mean, 1.5 * historical sd)   per input, per state
kappa[j]    ~ HalfNormal(0.05)               saturation strength
phi[j]      ~ Gamma(2, 1)                    saturation curvature
xbar[j,i]   ~ LogNormal(log(engineering ceiling estimate), 0.6)
psi[j,i]    ~ Normal(0, 0.10)                stress feedback, SIGN-FREE
u, v        ~ Normal(0, sigma_u^2), sigma_u ~ HalfNormal(0.05)
```

`psi` is centred at zero with no sign restriction, per `SPECIFICATION.md` section 5.1 and `DATA-INTEGRITY.md`. This is the second prior deliberately centred against the possibility of a convenient result.

`xbar` priors are the least defensible in the file. They are engineering ceiling estimates — grid interconnection limits, plausible saturation of robot density, thermal and land constraints on generation — and they are educated guesses with a wide log-scale dispersion. They are labelled `weakly_informative_engineering` in the code and they carry a mandatory sensitivity run, because a saturation ceiling that binds inside the horizon can determine a headline result on its own.

### 4.1 Baseline calibration anchors

The evolution priors are anchored to the current position, which is documented for cross-checking rather than fitted:

| Quantity | Value | Source |
|---|---|---|
| US utility-scale capacity additions, 2025 | 53 GW, largest single-year increase since 2002 | [EIA](https://www.eia.gov/todayinenergy/detail.php?id=67205) |
| US additions, 2026 projected | 86 GW record; solar 43.4 GW, storage 24.3 GW, wind 11.8 GW | [EIA](https://www.eia.gov/todayinenergy/detail.php?id=67205) |
| PRC additions, 2025 | 543 GW all types; 315 GW solar, 119 GW wind | [NEA via State Council](https://english.www.gov.cn/archive/statistics/202602/12/content_WS698d93cbc6d00ca5f9a091bb.html) |
| PRC total installed capacity | ~3.35 TW end-2024 to ~3.89 TW end-2025 | [NEA via State Council](https://english.www.gov.cn/archive/statistics/202602/12/content_WS698d93cbc6d00ca5f9a091bb.html) |
| PRC wind plus solar exceeds thermal capacity for the first time | 1.84 TW, 47.3% of installed capacity; non-fossil 60.4% | [NEA via State Council](https://english.www.gov.cn/archive/statistics/202602/12/content_WS698d93cbc6d00ca5f9a091bb.html) |
| PRC clean generation growth fully met demand growth; fossil generation fell for the first time in a decade | +561 TWh clean, -56 TWh fossil | [Ember, Global Electricity Review 2026](https://ember-energy.org/latest-insights/global-electricity-review-2026/major-countries-and-regions/) |
| US coal generation rose 13% while gas fell 3.4% | +85 TWh coal | [Ember, Global Electricity Review 2026](https://ember-energy.org/latest-insights/global-electricity-review-2026/major-countries-and-regions/) |
| PRC robot installations 2024 | 295,000 units, 54% of global total | [IFR](https://ifr.org/downloads/press_docs/2025-09-25-IFR_press_release_China_in_English.pdf) |
| PRC operational robot stock end-2024 | over 2,027,000 units | [IFR](https://ifr.org/downloads/press_docs/2025-09-25-IFR_press_release_China_in_English.pdf) |

The F1 ratio implied by the 2025 figures is roughly 9.8%, consistent with the baseline log and still far from the 40% threshold. Note what the last two rows of the generation table do to a naive reading: the US is adding fossil generation while the PRC is retiring it, which cuts against the framing in which US capacity growth is the more modern. The dispatchable-adjustment rule R003, still unspecified, is where that distinction becomes quantitative — and its absence is now a live constraint on `Y_throughput`, not a housekeeping item.

---

## 5. The manufacturing TFP prior, and a disclosure

F7 requires PRC manufacturing TFP. `pipeline/adapters/F7.md` already records that the named source is economy-wide rather than manufacturing-specific and pre-commits that the strongest available verdict on proxy data is `indeterminate`.

Independent search confirms the position is worse than a source mismatch. **No continuously updated, officially published, manufacturing-sector-specific PRC TFP series comparable to US multifactor productivity series appears to exist.** What exists:

- An aggregate national TFP index from the Penn World Table, not manufacturing-specific ([FRED series RTFPNACNA632NRUG](https://fred.stlouisfed.org/series/RTFPNACNA632NRUG)).
- Episodic academic reconstructions from NBS Annual Industrial Enterprise Survey or National Taxation Survey microdata, not update-consistent across years: manufacturing TFP growth of 1.1% per year for 2007-2013 ([Recent Productivity Trends in China](https://muse.jhu.edu/pub/43/article/848481/pdf)); weighted TFP rising from 3.65 in 2007 to 4.69 in 2017, averaging 2.58% per year ([Applied Economics, 2021](https://www.tandfonline.com/doi/full/10.1080/00036846.2021.1954592)); a marked slowdown in revenue-based TFP growth across all industries, ownership types and regions, with explicit data-quality concerns including missing value-added and intermediate-input information and over-reporting ([Journal of Development Economics 181, 2026](https://ideas.repec.org/a/eee/deveco/v181y2026ics0304387826000039.html)).
- No accessible APO Productivity Database series isolating PRC manufacturing TFP was located.

Committed treatment:

```
PRC manufacturing TFP is a PROXY-ONLY input.
Prior on the proxy-to-target gap: Normal(0, 1.5pp) on growth, with a proxy_only flag.
Every output consuming it carries the flag.
F7 cannot return `triggered` on proxy data. That pre-commitment stands.
```

And the disclosure, which the papers must carry: **F7 may be structurally unfalsifiable for the duration of the programme.** Not because the world declined to produce the evidence, but because the measurement instrument the condition names does not exist for the country it names. A falsifier that cannot fire is a weakened falsifier, and combined with F4's non-existent successor study and F6's horizon problem, the pre-registered set may be effectively five conditions rather than eight. That must be stated in Paper B rather than left for a reader to notice.

---

## 6. Political stress priors

Deferred to `POLITICAL-STRESS.md`, which carries the component definitions, the PRC operationalisation table, the inert-trust-term commitment, and the four published critiques.

One prior belongs here. Given that PSI model variables explain roughly 18% of the variance in US political instability over 1960-2020 ([The structural-demographic theory revisited](https://pmc.ncbi.nlm.nih.gov/articles/PMC10621949/)), the `psi[j,i]` prior scale of 0.10 in section 4 is set small deliberately. A prior that let stress drive input growth strongly would be a prior asserting more predictive content for `Psi` than its own literature supports.

---

## 7. Mandatory sensitivity runs

Frozen list. May be extended, never shortened.

| # | Prior varied | Alternative | Why it could determine a result |
|---|---|---|---|
| S1 | `sigma_D` centre | 0.3 and 0.8 | Spans the publication-bias-corrected meta-estimate and the Kemfert upper range |
| S2 | `sigma_F` centre | 0.3 and 0.9 | Spans corrected and uncorrected meta-analytic capital-labour values |
| S3 | `delta` scale | 0.10 and 0.50 | Determines whether P2 can be resolved at all |
| S4 | Nesting structure | Each of the three, forced | The embodied-AI structure favours P2 |
| S5 | PRC growth bias | Both endpoints of the 0.5-2.0pp band | The pre-registered band's own extremes |
| S6 | `xbar` saturation ceilings | 0.7x and 1.5x | A binding ceiling inside the horizon can produce a regime by itself |
| S7 | Compute-share definition | Cluster performance, accelerator count, ownership basis | Three definitions give 5%, 14%, 24-33% |
| S8 | Stress channel | `psi` fixed at zero | Tests whether any result depends on a 18%-of-variance index |
| S9 | `SFD` variant | `(Y/G)*(1-T)` versus `Y/(G*D)` | The two are not monotone transforms |
| S10 | Robot series basis | Density with break adjustment versus stock only | The IFR denominator revision makes density non-comparable across the break |

A headline result that flips under any of S1 through S10 is reported as **prior-dependent** in the abstract, not in an appendix.

---

## Sources

- GTAP-E technical paper — https://www.diw.de/documents/publikationen/73/55787/dp668.pdf
- Kemfert, *Energy Economics* 20(3), 1998 — https://www.sciencedirect.com/science/article/pii/S0140988397000145
- Henningsen, Henningsen and van der Werf, *Energy Economics* 82, 2019 — https://backend.orbit.dtu.dk/ws/files/149724340/melju_1_s2.0_S0140988317304395_main.pdf
- UKERC, Elasticity of Substitution Studies — https://d2e1qxpsswcpgz.cloudfront.net/uploads/2020/03/ukerc-review-of-evidence-for-the-rebound-effect-technical-report-3-elasticity-of-substitution-studies.pdf
- Kiel Institute, Production Functions for Climate Policy Modeling — https://www.kielinstitut.de/fileadmin/Dateiverwaltung/IfW-Publications/fis-import/1f1b4ac5-5bbb-4f1b-b161-af3180a9c2ee-kap1316.pdf
- van der Werf, *Energy Economics* 30(6), 2008 — https://d-nb.info/1128231875/34
- Shen and Whalley, NBER WP 19104 — https://www.nber.org/system/files/working_papers/w19104/w19104.pdf
- Gechert, Havránek, Iršová and Kolcunová, *Review of Economic Dynamics* 45, 2022 — http://meta-analysis.cz/sigma/sigma.pdf
- Knoblach et al., meta-regression on US capital-labour substitution — http://groupelavigne.free.fr/knoblach2019.pdf
- Koetse, de Groot and Florax, *Energy Economics* 30(5), 2008 — https://www.econstor.eu/bitstream/10419/86262/1/06-061.pdf
- Epoch AI, AI supercomputer performance share by country — https://epoch.ai/data-insights/ai-supercomputers-performance-share-by-country
- Epoch AI, geopolitics of AI hub — https://epoch.ai/topics/geopolitics
- Epoch AI, AI Chip Owners Explorer — https://epochai.substack.com/p/introducing-the-ai-chip-owners-explorer
- Federal Reserve, The State of AI Competition in Advanced Economies — https://www.federalreserve.gov/econres/notes/feds-notes/the-state-of-ai-competition-in-advanced-economies-20251006.html
- RAND, Full Stack: China's Evolving Industrial Policy for AI — https://www.rand.org/pubs/perspectives/PEA4012-1.html
- CSIS, Securing the AGI Laurel — https://www.csis.org/analysis/securing-agi-laurel-export-controls-compute-gap-and-chinas-counterstrategy
- EIA, New US electric generating capacity expected to reach a record high in 2026 — https://www.eia.gov/todayinenergy/detail.php?id=67205
- NEA via State Council, China's newly installed wind and solar capacity up 22 pct in 2025 — https://english.www.gov.cn/archive/statistics/202602/12/content_WS698d93cbc6d00ca5f9a091bb.html
- Ember, Global Electricity Review 2026 — https://ember-energy.org/latest-insights/global-electricity-review-2026/major-countries-and-regions/
- IFR, China tops world record of 2 million factory robots — https://ifr.org/downloads/press_docs/2025-09-25-IFR_press_release_China_in_English.pdf
- Penn World Table via FRED, TFP at constant national prices for China — https://fred.stlouisfed.org/series/RTFPNACNA632NRUG
- Recent Productivity Trends in China — https://muse.jhu.edu/pub/43/article/848481/pdf
- Total factor productivity of Chinese industrial firms, 2007-2017, *Applied Economics* — https://www.tandfonline.com/doi/full/10.1080/00036846.2021.1954592
- Where has all the dynamism gone?, *Journal of Development Economics* 181, 2026 — https://ideas.repec.org/a/eee/deveco/v181y2026ics0304387826000039.html
- The structural-demographic theory revisited — https://pmc.ncbi.nlm.nih.gov/articles/PMC10621949/

---

## Amendment 1 -- 2026-08-20 -- separate innovation scales; derivation procedure committed before computation

**Appended, not substituted.** Selected by author decision of 2026-08-20 in structured Q&A, from the two live candidates recorded in `PRIOR-PREDICTIVE-RUN-001.md` section 3.2. Candidate 3 (widen the PP3 ceiling) was rejected in advance and was not offered. Candidate 2 (truncate the joint prior) was declined on a ground independent of any outcome: rejection-sampling at the 20x ceiling converts PP3 from a check on the prior into a constraint of the prior, making the gate unfailable by construction, and a gate that cannot fail is not a gate.

### The change

The committed line

```
u, v ~ Normal(0, sigma_u^2), sigma_u ~ HalfNormal(0.05)
```

is superseded prospectively by

```
u ~ Normal(0, sigma_u^2),  sigma_u ~ HalfNormal(0.05)     level innovation, unchanged
v ~ Normal(0, sigma_v^2),  sigma_v ~ HalfNormal(s_v)      growth innovation, own scale
```

**Ground, statable without reference to any gate:** a shock to a growth rate and a shock to a level are not the same kind of quantity, and there was never a substantive reason for their scales to share a prior. The shared scale was a drafting economy, not a modelling claim. This is recorded together with its hazard: the same argument passes the failing gate cheaply, which is exactly why the scale `s_v` is not chosen by judgement but by the pre-named procedure below, committed **before** the computation is run.

### The derivation procedure for s_v, named before computing

1. **Data.** Ember yearly total installed generation capacity for the United States and China, 2000--2025, computed by summing the nine fuel-level capacity rows per country-year from the content-addressed snapshot already committed to this repository (`research/snapshots/store/259e1095ee8ffeaf0aff37ad557916ae1823a2da13312da50ba4cec6b4574c3b.csv`). This is the only input-adjacent series in the repository with a committed snapshot; it is D1-adjacent, covers both states from a single harmonised source, and its byte-identity is verifiable.
2. **Growth rates.** `g_t = ln(C_t) - ln(C_{t-1})` per state, 2001--2025.
3. **AR(1) fit.** Per state, ordinary least squares on `g_t = c + rho * g_{t-1} + v_t`, t = 2002--2025.
4. **Pooled scale.** `s_v = sqrt( (SSR_US + SSR_CN) / (n_US + n_CN - 4) )`, rounded to three significant figures.
5. **Commitment.** `sigma_v ~ HalfNormal(s_v)` at whatever value step 4 yields. PP3 is re-run and the result is reported, **pass or fail**. If PP3 still fails, the failure is reported and estimation remains blocked; the procedure is not re-run with a different series or a different estimator.

The procedure is committed to the repository before step 2 is executed. The computed value and the re-run results are recorded in a follow-up amendment referencing this one, so a reader can verify the order from the commit history.

### Limitation, recorded now

`s_v` is elicited from one series -- generation capacity -- and applied to the growth innovations of all six inputs. Capacity growth is smoother than plausible paths for frontier compute or robot density, so `s_v` may understate growth-shock scale for the frontier bundle. That asymmetry is accepted because the alternative -- one elicited scale per input -- would require five more series the repository does not hold to snapshot standard, and it is recorded here so the sensitivity-run schedule can test it.

### Sources for Amendment 1

- research/snapshots/store/259e1095ee8ffeaf0aff37ad557916ae1823a2da13312da50ba4cec6b4574c3b.csv (internal snapshot; Ember yearly full release)
- model/PRIOR-PREDICTIVE-RUN-001.md, section 3.2 (internal; the candidate list and the diagnostic counterfactual)
