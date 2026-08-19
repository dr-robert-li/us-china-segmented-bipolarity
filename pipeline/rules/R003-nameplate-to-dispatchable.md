# R003 -- Nameplate to dispatchable

```yaml
rule:
  rule_id: R003
  version: 0.1.0
  name: Nameplate to dispatchable via published capacity factors
  applies_to: [D1, Y_throughput]
  inputs: [cap_installed_by_technology, capacity_factor_by_technology]
  output: cap_dispatchable_equivalent
  parameters:
    us_capacity_factors: EIA Electric Power Monthly Tables 6.7.A and 6.7.B
    prc_utilisation_hours: CEC / NEA, plants >= 6,000 kW
    own_use_adjustment: LBNL effective-capacity factors
    denominator_hours: 8760
  determinism: true
  supersedes: null
```

Version **0.1.0**, not 1.0.0. The rule is specified and executable, and it is deliberately below 1.0 because two of its four open items bear on the numbers it produces rather than only on its documentation. Section 7 lists them.

This rule closes the dangling reference recorded in `rules/README.md`. It does **not** feed any falsifier: F1 is explicitly exempt, per `adapters/F1.md`. R003 gates the model.

---

## 1. The transformation

```
D[i,t] = sum over technologies g of ( nameplate_GW[g,i,t] * cf[g,i] )
```

`cf[g,i]` is a technology- and state-specific fraction of nameplate. The sum is taken over a technology partition that must be exhaustive for the state's fleet; a technology present in the fleet with no registered factor **fails the run** rather than being defaulted. A missing factor treated as 1.0 inflates the fleet and treated as 0.0 deletes it, and neither error is visible in the output.

Mandated by `DATA-INTEGRITY.md` for every series entering `Y_throughput`. The mandate exists because nameplate capacity is not an energy quantity: a gigawatt of solar and a gigawatt of nuclear differ by roughly a factor of four in annual output, and the two fleets under study differ systematically in composition.

---

## 2. United States -- published capacity factors

EIA publishes annual average capacity factors for utility-scale generators, computed on a time-adjusted capacity basis where the annual figure is a time-weighted average of monthly values, excluding units that started or retired mid-month ([EIA Electric Power Monthly](https://www.eia.gov/electricity/monthly/)). Underlying collections are Forms EIA-923, EIA-860 and EIA-860M.

Fossil technologies, Table 6.7.A ([workbook](https://www.eia.gov/electricity/monthly/xls/table_6_07_a.xlsx), [table page](https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_a)):

| Technology | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|
| Coal, steam | 48.4% | 42.4% | 42.6% | 48.7% |
| Natural gas, combined cycle | 56.6% | 59.7% | 60.5% | 58.4% |
| Natural gas, gas turbine | 12.9% | 12.9% | 13.9% | 14.1% |
| Natural gas, steam turbine | 15.6% | 17.4% | 19.9% | 19.8% |
| Natural gas, internal combustion | 18.1% | 20.1% | 18.0% | 17.4% |

Non-fossil technologies, Table 6.7.B ([workbook](https://www.eia.gov/electricity/monthly/xls/table_6_07_b.xlsx), [table page](https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_b)):

| Technology | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|
| Nuclear | 92.7% | 93.0% | 90.8% | 91.0% |
| Geothermal | 69.0% | 69.4% | 64.6% | 65.9% |
| Other biomass | 60.2% | 60.4% | 59.5% | 59.0% |
| Wood biomass | 57.9% | 53.5% | 55.8% | 56.8% |
| Hydroelectric, conventional | 36.3% | 35.0% | 34.6% | 35.3% |
| Wind | 35.9% | 33.2% | 34.3% | 34.2% |
| Solar photovoltaic, utility-scale | 24.4% | 23.2% | 23.2% | 24.4% |
| Solar thermal | 23.1% | 22.1% | 25.0% | 23.6% |

2023 and earlier are marked final in the source workbook; 2024 and 2025 are marked preliminary and carry the `preliminary` flag. Independent reproduction of the 2022 column from an EIA-sourced third-party extract agrees to within 0.6pp on every technology checked ([extract](https://storage.googleapis.com/visualizingenergy_database/data/ve121.03_averageannualcapacityfactorselectricitygeneration2022.csv)).

Both series are constructed with `basis="published_capacity_factor"`.

---

## 3. People's Republic of China -- implied from utilisation hours

The PRC publishes utilisation hours (利用小时数), not capacity factors. The implied factor is `hours / 8760`. Coverage is plants of 6,000 kW and above unless stated otherwise, which is a scope restriction with no US analogue.

| Technology | 2023 (h) | 2024 (h) | Implied 2024 factor |
|---|---:|---:|---:|
| Nuclear | 7,670 | 7,683 | 87.7% |
| Coal-fired | 4,690 | 4,628 | 52.8% |
| Thermal, all | -- | 4,400 | 50.2% |
| Hydro, conventional | -- | 3,683 | 42.1% |
| Hydro, incl. pumped storage | 3,130 | 3,349 | 38.2% |
| All generating equipment | 3,599 | 3,442 | 39.3% |
| Gas-fired | 2,525 | 2,363 | 27.0% |
| Wind, grid-connected | 2,235 | 2,127 | 24.3% |
| Solar PV, grid-connected | 1,291 | 1,211 | 13.8% |
| Pumped storage | 1,176 | 1,217 | 13.9% |

Sources: [NEA 2024 full-year statistics](https://www.nea.gov.cn/20250121/097bfd7c1cd3498897639857d86d5dac/c.html), [CEC data via the China Electric Power Development and Reform Report 2025](https://www.ccpua.org/page116.html?article_id=6549), [China Electricity Statistical Yearbook 2024](https://pdf.dfcfw.com/pdf/H3_AP202512311811775347_1.pdf), [China Energy Transition Program bilingual summary](https://usercontent.one/wp/www.cet.energy/wp-content/uploads/2025/03/2025-03-CET_Summary-of-Chinas-energy-and-power-sector-statistics-in-2024.pdf). Preliminary CEC releases and the final Yearbook differ by a few hours on coal and solar -- 4,685 h versus 4,690 h for 2023 coal, 1,286 h versus 1,291 h for 2023 solar ([S&P Global citing CEC](https://www.spglobal.com/energy/en/news-research/latest-news/energy-transition/013124-coal-still-accounted-for-nearly-60-of-chinas-electricity-supply-in-2023-cec)) -- which is inside tolerance and is recorded rather than reconciled.

All PRC factors are constructed with `basis="implied_from_utilisation_hours"` and `comparable_across_geographies=False`.

### 3.1 The by-technology breakdown was discontinued mid-2024

NEA published cumulative by-technology utilisation hours monthly through the January-April 2024 release and stopped with the January-June 2024 release, which disclosed only the all-equipment figure ([NEA Jan-Mar 2024](https://www.nea.gov.cn/2024-04/22/c_1310772067.htm), [NEA Jan-Jun 2024](https://www.nea.gov.cn/2024-07/20/c_1310782235.htm)). The discontinuation is independently documented ([Dialogue Earth](https://dialogue.earth/en/digest/clean-energy-use-data-missing-from-gov-release/), [Environment+Energy Leader](https://www.environmentenergyleader.com/stories/lack-of-detailed-renewable-data-in-chinas-power-report-sparks-questions,44788)).

Consequence for this rule: PRC technology-resolved factors are available annually from the CEC yearbook cycle but not at higher frequency, and the most recent published national datapoints are all-equipment only -- 2,105 cumulative hours for January-August 2025, down 223 year on year, and 703 hours in Q1 2026, down 66 ([Q1 2026 via Xinhua](https://english.news.cn/20260423/766d32839b164738a5c1cc23ff5bb26a/c.html)).

This is a **live degradation in the observability of the PRC series**, and it runs against the direction the project would prefer. It is recorded here so that a future run producing a stale PRC factor set is understood as a source constraint rather than a pipeline defect.

---

## 4. Why the two are not interchangeable

Four mechanisms. The first is the one this rule was expected to be about, and the expectation turned out to be **wrong** in an instructive way.

### 4.1 The denominator basis, which is NOT the problem it is usually said to be

The standard objection is that PRC utilisation hours use a year-end capacity denominator, which in a fast-growing fleet understates the implied factor. The objection does not survive contact with the published Chinese methodology. The official definition is explicitly an average: 平均利用小时 = 发电量 / 发电设备平均容量, average utilisation hours equal generation divided by *average* equipment capacity, where average capacity is calendar-time weighted over the reporting period ([China Energy Portal translation of the NEA/CEC statistical reporting system](https://chinaenergyportal.org/statistical-reporting-system-for-renewable-energy/)). A Chinese methods paper states the same point directly, that the capacity used is the average and not the period-end figure ([Power System Technology methods paper](https://base4zgdl.xml-journal.net/cn/article/pdf/preview/10.11930/j.issn.1004-9649.202103120.pdf)).

EIA's annual figure is also a time-weighted average of monthly values. On this specific dimension the two countries' official headline figures are computed on comparable bases.

Where the error actually arises is in third-party recomputation. Normalising 2023 Chinese solar generation against year-end capacity of 609 GW gives roughly 11%, while a beginning-of-year basis gives roughly 17% -- a six-point swing from the denominator choice alone ([Marinelli](https://www.linkedin.com/posts/mattiamarinelli_i-got-my-feed-flooded-by-posts-claiming-that-activity-7209825909749514240-Ytd7)). That is the likely origin of circulating claims that PRC solar capacity factors are implausibly low.

**Committed consequence:** this rule consumes the officially published utilisation hours and never recomputes them from generation and capacity. Recomputation is where the known error lives.

That this rule's headline expected caveat was refuted by its own sourcing is recorded rather than quietly dropped, because the same reasoning would have been used to justify an adjustment factor that is not warranted.

### 4.2 Gross versus net of own-use -- this one is real

PRC installed capacity is reported gross of generator own-use, whereas an effective-capacity measure should be net. LBNL applies own-use adjustments of 5% for thermal, nuclear and other, and 1% for hydro, wind and solar, in converting Chinese gross installed capacity to effective capacity ([LBNL, Excess Capacity in China's Power System](https://eta-publications.lbl.gov/sites/default/files/lbnl1006638.pdf), section 3.4 and Table 8).

**Committed:** the LBNL own-use factors are applied to PRC nameplate before the capacity factor. They are a published third-party adjustment, not this project's invention, and they are versioned as parameters of this rule.

### 4.3 Scope -- the 6,000 kW floor and behind-the-meter asymmetry

PRC statistics cover plants of 6,000 kW and above. US utility-scale reporting excludes small-scale distributed solar. The two exclusions are not the same size and do not move the two fleets in the same direction. This is the same hazard the F1 adapter closes by using one harmonised source for both countries, and R003 cannot use that solution because no harmonised source publishes technology-resolved capacity factors on a common basis.

### 4.4 Curtailment scope

The PRC publishes national curtailment rates: wind 2.7% and solar 2.0% in 2023, rising to 4.1% and 3.2% in 2024 ([NEA 2024 renewable monitoring evaluation](https://www.nea.gov.cn/20251113/cc1fb0298a2944f8bd5441f67c9be9b3/20251113cc1fb0298a2944f8bd5441f67c9be9b3_54b6e6c1674e9c4bdca1cdfb4cbb16b477.doc), [NDRC on 2023](https://www.ndrc.gov.cn/wsdwhfz/202406/t20240621_1391234.html)), then 5.7% and 6.6% in the first half of 2025 with the national curtailment cap raised from 5% to 10% ([Reuters](https://www.reuters.com/sustainability/climate-energy/chinas-renewable-capacity-soars-utilisation-lags-data-show-2025-08-05/)), and 8.5% and 9.2% for January-February 2026 ([Bloomberg](https://www.bloomberg.com/news/articles/2026-04-08/china-s-wasting-too-much-renewable-power-as-curtailments-rise)). National averages conceal extreme provincial concentration: Tibet reached 30.2% wind and 33.9% solar in the first half of 2025 ([Sina Finance citing the Early Warning Center](https://finance.sina.com.cn/roll/2025-08-18/doc-infmmmiy1960581.shtml)).

A peer-reviewed re-estimate argues the official rates undercount, because published rates capture only power curtailed after generation and before grid connection, and because provincial curtailment-rate targets create an incentive to reduce reported utilisation hours instead ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13378348/)).

The US has **no national curtailment figure**. The closest is LBNL's seven-ISO weighted average wind curtailment of 4.6% for 2023, covering CAISO, ERCOT, MISO, ISO-NE, NYISO, PJM and SPP but excluding vertically integrated utilities outside those footprints, and covering wind only ([LBNL Land-Based Wind Market Report 2024](https://eta-publications.lbl.gov/sites/default/files/2024-09/land-based_wind_market_report_2024_edition.pdf)). Regional figures are available -- CAISO curtailed 3.4 million MWh in 2024, up 29%, 93% of it solar ([EIA](https://www.eia.gov/todayinenergy/detail.php?id=65364)); ERCOT curtailed over 8 TWh with more than 4% of wind and nearly 6% of solar output curtailed ([ERCOT Independent Market Monitor](https://www.potomaceconomics.com/wp-content/uploads/2025/06/2024-State-of-the-Market-Report.pdf)) -- but they are not a national aggregate and are not presented as one.

**Committed:** curtailment is **not** applied as a second multiplicative adjustment on top of the capacity factor, because both the EIA capacity factor and the PRC utilisation hours are computed from realised generation and therefore already embed curtailment. Applying a curtailment haircut on top would double-count it. Curtailment enters the model instead through `D2`, transmission capacity, where a rising curtailment rate is evidence about grid constraint rather than about fleet composition.

That commitment is the one most likely to be contested, because a reader who knows the PRC curtailment trend will expect to see it deducted. The reason it is not deducted is arithmetic, and it applies symmetrically to both states.

---

## 5. The prohibition this rule carries

Because PRC factors are implied from a differently scoped statistic and adjusted with third-party own-use factors, **a cross-state ratio of dispatchable capacity is not a meaningful quantity** and this rule refuses to produce one. The implementation requires an explicit opt-in and then fails if any contributing factor is declared non-comparable, which under section 3 is every PRC factor.

The model consumes `D1` within-state. Relative position enters through the capability vector, where the measurement block carries a source- and state-specific bias term, which is the correct place for a definitional gap to be represented as uncertainty rather than silently absorbed into a ratio.

---

## 6. Tests

1. **Missing factor.** A fleet containing a technology with no registered factor raises rather than defaulting.
2. **Borrowed factor.** A US factor supplied for a PRC technology raises. Borrowing another state's capacity factor is a substitution, not a conversion.
3. **Comparability gate.** A cross-geography comparison requested with any `comparable_across_geographies=False` factor raises.
4. **Hours conversion.** 7,683 hours converts to 0.877 and 1,211 hours to 0.138, and hours above 8,760 raise.
5. **F1 isolation.** The F1 adapter never calls this rule, and an observation whose `series_id` indicates dispatchable adjustment is rejected on entry to F1.
6. **Determinism.** Same fleet, same factor set, byte-identical output.

---

## 7. Open items

- **Bears on the numbers.** The technology partition for the PRC fleet is coarser than the US partition: PRC thermal resolves to coal and gas, while EIA resolves gas into combined cycle, gas turbine, steam turbine and internal combustion, whose factors span 14% to 60%. Aggregating the US fleet up to match loses information; disaggregating the PRC fleet down requires an assumption about gas plant mix. Neither has been committed, and the choice moves `D1` for the US.
- **Bears on the numbers.** Storage. The PRC reports pumped storage inside hydro at a 13.9% implied factor, and grid batteries are a large and growing share of US additions -- 24.3 GW projected for 2026 alone. Storage is not generation and a capacity factor is arguably the wrong instrument for it. Not committed.
- Documentation only: whether to carry the LBNL own-use factors at their published values indefinitely or seek a more recent vintage.
- Documentation only: whether the 6,000 kW floor materially changes the PRC implied factors, which cannot be checked without sub-threshold generation data.

The first two are why this rule is at 0.1.0. A rule whose partition choice can move a headline input is not at 1.0 merely because it runs.

---

## Sources

- EIA, Electric Power Monthly -- https://www.eia.gov/electricity/monthly/
- EIA, Table 6.7.A workbook -- https://www.eia.gov/electricity/monthly/xls/table_6_07_a.xlsx
- EIA, Table 6.7.B workbook -- https://www.eia.gov/electricity/monthly/xls/table_6_07_b.xlsx
- EIA, capacity factor methodology FAQ -- https://www.eia.gov/tools/faqs/faq.php?id=101&t=3
- EIA, Electric Power Annual -- https://www.eia.gov/electricity/annual/pdf/epa.pdf
- NEA, 2024 national electric power industry statistics -- https://www.nea.gov.cn/20250121/097bfd7c1cd3498897639857d86d5dac/c.html
- NEA, Jan-Mar 2024 statistics -- https://www.nea.gov.cn/2024-04/22/c_1310772067.htm
- NEA, Jan-Jun 2024 statistics -- https://www.nea.gov.cn/2024-07/20/c_1310782235.htm
- NEA, 2024 renewable energy power development monitoring and evaluation results -- https://www.nea.gov.cn/20251113/cc1fb0298a2944f8bd5441f67c9be9b3/20251113cc1fb0298a2944f8bd5441f67c9be9b3_54b6e6c1674e9c4bdca1cdfb4cbb16b477.doc
- NDRC, 2023 renewable utilisation notice -- https://www.ndrc.gov.cn/wsdwhfz/202406/t20240621_1391234.html
- CEC via China Electric Power Development and Reform Report 2025 -- https://www.ccpua.org/page116.html?article_id=6549
- China Electricity Statistical Yearbook 2024 -- https://pdf.dfcfw.com/pdf/H3_AP202512311811775347_1.pdf
- China Energy Transition Program, 2024 statistics summary -- https://usercontent.one/wp/www.cet.energy/wp-content/uploads/2025/03/2025-03-CET_Summary-of-Chinas-energy-and-power-sector-statistics-in-2024.pdf
- China Energy Portal, statistical reporting system for renewable energy -- https://chinaenergyportal.org/statistical-reporting-system-for-renewable-energy/
- Power System Technology, utilisation-hour methods paper -- https://base4zgdl.xml-journal.net/cn/article/pdf/preview/10.11930/j.issn.1004-9649.202103120.pdf
- LBNL, Excess Capacity in China's Power System -- https://eta-publications.lbl.gov/sites/default/files/lbnl1006638.pdf
- LBNL, Land-Based Wind Market Report 2024 Edition -- https://eta-publications.lbl.gov/sites/default/files/2024-09/land-based_wind_market_report_2024_edition.pdf
- Potomac Economics, 2024 State of the Market Report for ERCOT -- https://www.potomaceconomics.com/wp-content/uploads/2025/06/2024-State-of-the-Market-Report.pdf
- EIA, Solar and wind power curtailments are increasing in California -- https://www.eia.gov/todayinenergy/detail.php?id=65364
- Reuters, As China's renewable capacity soars, utilisation lags -- https://www.reuters.com/sustainability/climate-energy/chinas-renewable-capacity-soars-utilisation-lags-data-show-2025-08-05/
- Bloomberg, China's Wasting Too Much Renewable Power as Curtailments Rise -- https://www.bloomberg.com/news/articles/2026-04-08/china-s-wasting-too-much-renewable-power-as-curtailments-rise
- Sina Finance, H1 2025 provincial curtailment -- https://finance.sina.com.cn/roll/2025-08-18/doc-infmmmiy1960581.shtml
- Curtailment technical utilisation solutions, peer-reviewed re-estimate -- https://pmc.ncbi.nlm.nih.gov/articles/PMC13378348/
- Dialogue Earth, Clean energy use data missing from gov release -- https://dialogue.earth/en/digest/clean-energy-use-data-missing-from-gov-release/
- Environment+Energy Leader, Lack of detailed renewable data -- https://www.environmentenergyleader.com/stories/lack-of-detailed-renewable-data-in-chinas-power-report-sparks-questions,44788
- Xinhua, Q1 2026 installed capacity and utilisation hours -- https://english.news.cn/20260423/766d32839b164738a5c1cc23ff5bb26a/c.html
- S&P Global, CEC 2023 coal and solar utilisation hours -- https://www.spglobal.com/energy/en/news-research/latest-news/energy-transition/013124-coal-still-accounted-for-nearly-60-of-chinas-electricity-supply-in-2023-cec
- Marinelli, on the China solar capacity-factor denominator error -- https://www.linkedin.com/posts/mattiamarinelli_i-got-my-feed-flooded-by-posts-claiming-that-activity-7209825909749514240-Ytd7
