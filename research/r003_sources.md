# R003 — Capacity Factor / Utilisation Hour Sources: United States vs. People's Republic of China

Compiled for a pre-registered academic pipeline converting nameplate generation capacity to dispatchable/effective output. Every figure below is drawn from a named published source with a full URL, publisher, and vintage. All statements about data availability are verified against the pages actually fetched — where a requested figure does not exist in published official form, this is stated explicitly in Section 6.

---

## 1. United States — EIA average annual capacity factors by technology

**Primary source:** U.S. Energy Information Administration (EIA), *Electric Power Monthly*, Table 6.7.A "Capacity Factors for Utility Scale Generators Primarily Using Fossil Fuels" and Table 6.7.B "Capacity Factors for Utility Scale Generators Not Primarily Using Fossil Fuels."

- Table landing page (all tables, current release **data month May 2026, released July 23, 2026**): https://www.eia.gov/electricity/monthly/
- Table 6.7.A direct grapher page: https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_a
- Table 6.7.B direct grapher page: https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_b
- Downloadable workbook (Table 6.7.A), used to extract the exact figures below: https://www.eia.gov/electricity/monthly/xls/table_6_07_a.xlsx
- Downloadable workbook (Table 6.7.B), used to extract the exact figures below: https://www.eia.gov/electricity/monthly/xls/table_6_07_b.xlsx
- EIA methodology note (definition of capacity factor and time-adjusted capacity): https://www.eia.gov/tools/faqs/faq.php?id=101&t=3 and https://www.eia.gov/tools/faqs/faq.php?id=104&t=3
- Equivalent annual table also published in EIA *Electric Power Annual* as Table 4.8.A / 4.8.B, most recent full edition (2023 data, released 2024): https://www.eia.gov/electricity/annual/pdf/epa.pdf and HTML version: https://www.eia.gov/electricity/annual/html/epa_04_08_b.html

**Underlying data source for both tables:** EIA Form EIA-923 ("Power Plant Operations Report"), EIA Form EIA-860 ("Annual Electric Generator Report"), and EIA Form EIA-860M ("Monthly Update to the Annual Electric Generator Report") — cited on both table pages above.

**Note on data status:** In the vintage retrieved, 2023 and earlier years are marked "final"; 2024 and 2025 rows are marked "preliminary" in the source workbook. Annual capacity factor = time-weighted average of monthly values on a "time-adjusted capacity" basis (summer capacity of generators operating the full month, excluding units that started or retired mid-month).

### 1.1 Table 6.7.A — Coal and natural gas technologies (annual average capacity factor, %)

| Technology | 2022 | 2023 | 2024 (preliminary) | 2025 (preliminary, partial year) |
|---|---:|---:|---:|---:|
| Coal (steam) | 48.4% | 42.4% | 42.6% | 48.7% |
| Natural gas — Combined Cycle | 56.6% | 59.7% | 60.5% | 58.4% |
| Natural gas — Gas Turbine | 12.9% | 12.9% | 13.9% | 14.1% |
| Natural gas — Steam Turbine | 15.6% | 17.4% | 19.9% | 19.8% |
| Natural gas — Internal Combustion | 18.1% | 20.1% | 18.0% | 17.4% |

Source: https://www.eia.gov/electricity/monthly/xls/table_6_07_a.xlsx (Table 6.07.A, EIA Electric Power Monthly, accessed release with data through 2025)

### 1.2 Table 6.7.B — Non-fossil technologies (annual average capacity factor, %)

| Technology | 2022 | 2023 | 2024 (preliminary) | 2025 (preliminary, partial year) |
|---|---:|---:|---:|---:|
| Geothermal | 69.0% | 69.4% | 64.6% | 65.9% |
| Hydroelectric (conventional) | 36.3% | 35.0% | 34.6% | 35.3% |
| Nuclear | 92.7% | 93.0% | 90.8% | 91.0% |
| Other Biomass (wood/other biomass combined per table structure) | 60.2% | 60.4% | 59.5% | 59.0% |
| Solar Photovoltaic (utility-scale) | 24.4% | 23.2% | 23.2% | 24.4% |
| Solar Thermal | 23.1% | 22.1% | 25.0% | 23.6% |
| Wind | 35.9% | 33.2% | 34.3% | 34.2% |
| Wood (biomass) | 57.9% | 53.5% | 55.8% | 56.8% |

Source: https://www.eia.gov/electricity/monthly/xls/table_6_07_b.xlsx (Table 6.07.B, EIA Electric Power Monthly, accessed release with data through 2025)

*Note: EIA's Table 6.07.A does not separately break out a "natural gas combustion turbine" category distinct from "Gas Turbine" — the Gas Turbine row is the combustion-turbine (peaker) technology requested. There is no separate "geothermal" line in the fossil-fuel table; geothermal is correctly reported in Table 6.07.B (non-fossil table) as shown above.*

### 1.3 Cross-check / independent confirmation of 2022 EIA figures

A third-party visualization dataset sourced explicitly from EIA's Electric Power Monthly independently reproduces most of the same 2022 figures (coal 47.8%, NGCC 56.7%, nuclear 92.6%, wind 36.1%, solar PV 23.1%), confirming the EIA table extraction above: https://storage.googleapis.com/visualizingenergy_database/data/ve121.03_averageannualcapacityfactorselectricitygeneration2022.csv (sourced from https://www.eia.gov/electricity/monthly/)

### 1.4 Related EIA commentary (context, not primary data)

- EIA *Today in Energy*, "Use of natural gas-fired generation differs in the United States by technology and region," reports CCGT fleetwide capacity factor of ~56% in 2022, and ~66% for the newest CCGT units (2014–2023 vintage): https://www.eia.gov/todayinenergy/detail.php?id=61444
- EPA "Power Sector Trends Technical Support Document" (May 23, 2023) cites EIA Electric Power Monthly Table 6.07.A directly for coal capacity factor distributions 2005–2021: https://www.epa.gov/system/files/documents/2023-05/Power%20Sector%20Trends%20TSD.pdf

---

## 2. China — average annual utilisation hours (利用小时数) by technology

**Primary/near-primary sources:** China Electricity Council (CEC) data as reproduced in the China Coal Processing and Utilization Association's summary of "China Electric Power Development and Reform Report (2025)," and National Energy Administration (NEA) monthly/annual statistical releases. Coverage is plants with installed capacity ≥ 6,000 kW (6 MW) unless stated otherwise — this is a material scope caveat noted in Section 5.

### 2.1 National utilisation hours by technology, 2023 vs. 2024 (hours/year, ≥6,000 kW plants)

| Technology | 2023 (hours) | 2024 (hours) | YoY change | Implied capacity factor 2024 (hours ÷ 8,760) |
|---|---:|---:|---:|---:|
| All generating equipment (national average) | 3,599 (per CEC Electricity Statistical Yearbook 2024, table below) | 3,442 | −157 h | 39.3% |
| Thermal (火电) | — | 4,400 | −76 h | 50.2% |
| — of which coal-fired (煤电) | 4,690 (per Electricity Statistical Yearbook table for national coal) | 4,628 | −62 h | 52.8% |
| — of which gas-fired (气电) | 2,525 | 2,363 | −162 h | 27.0% |
| Hydro (水电, total incl. pumped storage) | 3,130 | 3,349 | +219 h | 38.2% |
| — Conventional hydro (常规水电) | — | 3,683 | +272 h | 42.1% |
| — Pumped storage (抽水蓄能) | 1,176 | 1,217 | +40 h | 13.9% |
| Nuclear (核电) | 7,670 | 7,683 | +13 h | 87.7% |
| Grid-connected wind (并网风电) | 2,235 | 2,127 | −107 h | 24.3% |
| Grid-connected solar PV (并网太阳能发电) | 1,291 (per Electricity Statistical Yearbook regional table, national row) | 1,211 | −81 h | 13.8% |

Sources for this table:
- China Coal Processing and Utilization Association, republishing China Electricity Council data, "我国电力发展与改革报告（2025）" ["China Electric Power Development and Reform Report (2025)"], published 26 March 2025, author 王雪辰 (Zhongneng Media Energy Security New Strategy Research Institute): https://www.ccpua.org/page116.html?article_id=6549 (mirror: https://www.ccpua.org/page210.html?article_id=6549)
- China Energy News Network (中国能源新闻网), republishing the same NEA full-year 2024 statistical release, 21 January 2025: https://www.cpnn.com.cn/news/xwtt/202501/t20250121_1768557.html
- NEA official release, "国家能源局发布2024年全国电力工业统计数据" [NEA releases 2024 national electric power industry statistics], 21 January 2025 (confirms national all-equipment figure of 3,442 hours, down 157 h from 2023): https://www.nea.gov.cn/20250121/097bfd7c1cd3498897639857d86d5dac/c.html
- "中国电力统计年鉴—2024" [*China Electricity Statistical Yearbook 2024*], scanned/reproduced PDF, gives 2023 national all-equipment figure of 3,598–3,599 hours (source shows both 3,598 and 3,599 in different table cross-references) and provincial/technology breakdowns for 2019–2023, including coal 4,690 h (2023) vs 4,593 h (2022), wind national row, and solar national row 1,291 h (2023): https://pdf.dfcfw.com/pdf/H3_AP202512311811775347_1.pdf
- China Energy Transition Program (CET) "Summary of China's Energy and Power Sector Statistics in 2024," March 2025 (consolidates NEA/CEC/NBS data into one bilingual English/Chinese table with footnoted primary sources; explicitly cites underlying government releases in bracketed footnotes [4], [10]): https://usercontent.one/wp/www.cet.energy/wp-content/uploads/2025/03/2025-03-CET_Summary-of-Chinas-energy-and-power-sector-statistics-in-2024.pdf
- S&P Global Commodity Insights, "Coal still accounted for nearly 60% of China's electricity supply in 2023," 31 January 2024 — cites CEC directly for coal utilisation hour of 4,685 h in 2023 (up 92 h YoY) and solar PV utilisation hour of 1,286 h in 2023 (down 54 h YoY); these figures are close to but not identical to the Electricity Statistical Yearbook figures above, reflecting revisions between preliminary CEC releases and the final Yearbook: https://www.spglobal.com/energy/en/news-research/latest-news/energy-transition/013124-coal-still-accounted-for-nearly-60-of-chinas-electricity-supply-in-2023-cec

### 2.2 NEA monthly cumulative releases (for verification / trend granularity, 2024)

NEA publishes cumulative-year-to-date utilisation hours monthly; figures below are cumulative, not annualized, and by technology breakdown was **discontinued mid-2024** (see Section 5.2 for the data-availability gap this creates):

| Period (2024, cumulative) | All-equipment (h) | Hydro (h) | Thermal (h) | Nuclear (h) | Wind (h) | Solar (h) |
|---|---:|---:|---:|---:|---:|---:|
| Jan–Feb | 563 | 369 | 763 | 1,216 | 373 | 168 |
| Jan–Mar | 844 | 555 | 1,128 | 1,828 | 596 | 279 |
| Jan–Apr | 1,097 | 785 | 1,448 | 2,471 | 789 | 373 |
| Jan–Jun | 1,666 | not disclosed after this release | not disclosed | not disclosed | not disclosed | not disclosed |

Sources:
- NEA, "国家能源局发布1-2月份全国电力工业统计数据," 25 March 2024: https://www.nea.gov.cn/2024-03/25/c_1310768833.htm
- NEA, "国家能源局发布1-3月份全国电力工业统计数据," 22 April 2024: https://www.nea.gov.cn/2024-04/22/c_1310772067.htm
- Huafu Securities Research (华福证券研究所) note "数说电力" reproducing NEA Jan–Apr 2024 breakdown by technology (hydro 785 h, thermal 1,448 h, nuclear 2,471 h, wind 789 h, solar 373 h): https://pdf.dfcfw.com/pdf/H3_AP202406171636462381_1.pdf
- NEA, "国家能源局发布2024年1-6月份全国电力工业统计数据," 20 July 2024 (only all-equipment cumulative figure of 1,666 h disclosed; no by-technology breakdown published from this release onward): https://www.nea.gov.cn/2024-07/20/c_1310782235.htm
- Dialogue Earth / China Dialogue, "Clean energy use data missing from gov release" — documents and explains this discontinuation explicitly: https://dialogue.earth/en/digest/clean-energy-use-data-missing-from-gov-release/
- Environment+Energy Leader, "Lack of Detailed Renewable Data in China's Power Report Sparks Questions," 25 April 2025 — corroborates the same gap: https://www.environmentenergyleader.com/stories/lack-of-detailed-renewable-data-in-chinas-power-report-sparks-questions,44788

### 2.3 Most recent partial-year 2025/2026 data point (trend confirmation, not full-year)

- NEA data reported via Xinhua: national average utilisation hours of power generation equipment were **703 hours** in Q1 2026, down 66 hours YoY: https://gulfnews.com/business/energy/chinas-installed-power-generation-capacity-climbs-155-by-end-march-2026-1.500517430 (23 April 2026); English mirror at Xinhua: https://english.news.cn/20260423/766d32839b164738a5c1cc23ff5bb26a/c.html
- Metal.com report of NEA data: cumulative Jan–Aug 2025 all-equipment utilisation hours were 2,105 hours, down 223 hours YoY (confirms continuation of the declining trend; no by-technology breakdown published): https://news.metal.com/newscontent/103555031/nea-data-installed-wind-emsolarem-capacity-hits-around-17-billion-kw-as-of-august-31-emsolarem-surges-485-yoy

---

## 3. China — wind and solar curtailment / utilisation rates (弃风率, 弃光率)

**Publisher of the primary national figures:** National Renewable Energy Consumption Monitoring and Early Warning Center (全国新能源消纳监测预警中心), an NEA-affiliated body, publishing quarterly and annual national and provincial curtailment/utilisation-rate data. Figures are also reproduced by NEA and by NDRC.

### 3.1 National annual figures

| Year | Wind curtailment rate (弃风率) | Solar curtailment rate (弃光率) | Wind utilisation rate | Solar utilisation rate |
|---|---:|---:|---:|---:|
| 2023 | 2.7% | 2.0% | 97.3% | 98.0% |
| 2024 | 4.1% | 3.2% | 95.9% | 96.8% |

Sources:
- NDRC (国家发展和改革委员会) official notice citing 2023 national figures (wind utilisation 97.3%, solar utilisation 98%): https://www.ndrc.gov.cn/wsdwhfz/202406/t20240621_1391234.html
- China Coal Processing and Utilization Association / CEC report reproducing 2024 figures (wind utilisation 95.9%, down 1.4 pct; solar utilisation 96.8%, down 1.1 pct — note this document states the *decrease* as 1.2 pct for solar in one instance and 1.1 pct in the NEA source document; see next line for the NEA original): https://www.ccpua.org/page116.html?article_id=6549
- NEA official document, "2024年度全国可再生能源电力发展监测评价结果" [2024 Annual National Renewable Energy Power Development Monitoring and Evaluation Results] — the primary NEA document, states national 2024 wind utilisation rate 95.9% (down 1.4 pct YoY) and solar utilisation rate 96.8% (down 1.1 pct YoY), with full provincial breakdown: https://www.nea.gov.cn/20251113/cc1fb0298a2944f8bd5441f67c9be9b3/20251113cc1fb0298a2944f8bd5441f67c9be9b3_54b6e6c1674e9c4bdca1cdfb4cbb16b477.doc
- Xinhua-syndicated NewEnergy report on the same official Early Warning Center release, 7 February 2025 (national wind utilisation 95.9%, solar 96.8%, listing provinces at 100% utilisation): https://newenergy.in-en.com/html/newenergy-2438688.shtml
- China Energy Transition (CET) bilingual summary, converting to curtailment-rate terms explicitly (wind curtailment 4.1%, up 1.4 pct; solar curtailment 3.2%, up 1.2 pct): https://usercontent.one/wp/www.cet.energy/wp-content/uploads/2025/03/2025-03-CET_Summary-of-Chinas-energy-and-power-sector-statistics-in-2024.pdf

### 3.2 Provincial detail, 2023–2024 (illustrating the concentration of curtailment)

| Province/Region | Wind curtailment 2023 | Solar curtailment 2023 |
|---|---:|---:|
| Qinghai | 5.8% | 8.6% |
| Hebei | 5.7% | — |
| Inner Mongolia (蒙西) | 6.8% (per one source) / 5.1% (per another) | — |
| Gansu | 5.0% | 5.0% |
| Tibet | — | 22% |

Source (2023 provincial detail): Zhejiang provincial government energy/environment portal reproducing National Renewable Energy Consumption Monitoring and Early Warning Center data: https://zjic.zj.gov.cn/ywdh/nyhj/202408/t20240812_22695794.shtml

### 3.3 Most recent published figures (H1 2025 and early 2026) — confirms a reversal of the prior improving trend

| Period | Wind curtailment | Solar curtailment | Publisher |
|---|---:|---:|---|
| H1 2024 | 3.9%–4.0% | 3.0% | National Renewable Energy Consumption Monitoring and Early Warning Center, cited via Reuters |
| H1 2025 | 5.7% | 6.6% | Same, via Reuters/Bloomberg |
| Jan–Feb 2025 | 6.2% | 6.1% | Same, via Bloomberg |
| Jan–Feb 2026 | 8.5% | 9.2% | Same, via Bloomberg |
| H1 2025, Tibet only | 30.2% (wind) | 33.9% (solar) | Same, via Sina Finance |

Sources:
- Reuters, "As China's renewable capacity soars, utilisation lags, data show," 5 August 2025 (H1 2025: wind curtailment 5.7% vs 3% year earlier; solar 6.6% vs 3.9% year earlier; national curtailment cap raised from 5% to 10%): https://www.reuters.com/sustainability/climate-energy/chinas-renewable-capacity-soars-utilisation-lags-data-show-2025-08-05/
- Bloomberg, "China Curtails More Renewables as Record Additions Stress Grid," 2 April 2025 (Jan–Feb 2025: wind 6.2%, solar 6.1%, vs 4.0%/4.3% in the same period of 2024): https://www.bloomberg.com/news/articles/2025-04-02/china-curtails-more-renewables-as-record-additions-stress-grid
- Bloomberg, "China's Wasting Too Much Renewable Power as Curtailments Rise," 8 April 2026 (Jan–Feb 2026: solar curtailment 9.2% vs 6.1% year earlier; wind 8.5% vs 6.2% year earlier): https://www.bloomberg.com/news/articles/2026-04-08/china-s-wasting-too-much-renewable-power-as-curtailments-rise
- Bloomberg, "China's Record Renewables Buildout Is Wasting Power as Grid Lags," 5 August 2025 (H1 2025 figures, corroborating Reuters): https://www.bloomberg.com/news/articles/2025-08-05/china-s-record-renewables-buildout-is-wasting-power-as-grid-lags
- Sina Finance, provincial H1 2025 breakdown incl. Tibet 30.2% wind / 33.9% solar curtailment, citing the National New Energy Consumption Monitoring and Early Warning Center release of 4 August 2025: https://finance.sina.com.cn/roll/2025-08-18/doc-infmmmiy1960581.shtml
- IEA, *Renewables 2024*, notes Q1 2024 VRE curtailment below 3% for both technologies nationally, and H1 2023 vs H1 2024 wind curtailment jumping from 3.1% to 6.7% (a somewhat higher figure than the NEA-sourced press figures above, reflecting a different measurement window/methodology): https://iea.blob.core.windows.net/assets/88a07dd9-42fe-4232-842e-9015b4b647f8/Renewables2024.pdf

**Coverage note:** All of the above are **national averages**; the Early Warning Center and NEA simultaneously publish full provincial breakdowns (31 provinces), which show far higher curtailment in Xinjiang, Gansu, Qinghai, Inner Mongolia, and especially Tibet than the national figure implies. Any national single figure materially understates curtailment exposure in renewable-rich provinces.

### 3.4 Independent academic re-estimate suggesting official curtailment rates are understated

A 2026 peer-reviewed article argues that officially published curtailment rates (弃风率/弃光率) undercount true curtailment because local governments can require generators to reduce reported utilisation hours to stay under provincial curtailment-rate targets, and because published rates only capture power curtailed *after generation but before grid connection*, not shortfalls from plants prevented from operating normally. The paper's alternative bottom-up estimate (theoretical vs. actual utilisation hours) finds higher implied curtailment than the official published rate, particularly for solar: "the currently published figures for wind and PV curtailment, particularly PV curtailment, may be somewhat underestimated." — Source: "The technical utilization solutions for curtailment during China's..." PMC, 7 July 2026: https://pmc.ncbi.nlm.nih.gov/articles/PMC13378348/

---

## 4. United States — wind and solar curtailment (regional; no single national figure exists)

**Confirmed gap:** There is no single published EIA (or other federal) figure for a national U.S. wind/solar curtailment rate analogous to China's national 弃风率/弃光率. EIA, LBNL, and NREL all publish curtailment data at the **balancing-authority/ISO level only**. This is stated explicitly below with the best available regional figures.

### 4.1 CAISO (California)

| Year | Wind + solar curtailed (MWh) | YoY change | Solar share of curtailment |
|---|---:|---:|---:|
| 2021 | 1.47 million MWh | — | — |
| 2023 | ~2.64 million MWh (implied from 2024 figure and the stated 29% YoY increase) | — | — |
| 2024 | 3.4 million MWh | +29% vs. 2023 | 93% |

Sources:
- EIA *Today in Energy*, "Solar and wind power curtailments are increasing in California," 31 March 2026 (states CAISO curtailed 3.4 million MWh in 2024, a 29% increase from 2023, with solar accounting for 93%; also notes the Western Energy Imbalance Market avoided 274,000 MWh, ~8%, of curtailment in 2024): https://www.eia.gov/todayinenergy/detail.php?id=65364
- Reuters, "Rising curtailments in California underline US grid ordeal," 4 August 2026 (gives the full CAISO annual series: 1.47 million MWh in 2021 rising to 3.4 million MWh in 2024, and notes April 2026 alone saw 1.46 TWh curtailed, ~18% of grid-scale solar and wind generation that month; also cites CAISO's Mark Rothleder stating curtailment is "typically" under 5% of declared available capacity): https://www.reuters.com/business/energy/rising-curtailments-california-underline-us-grid-ordeal--reeii-2026-08-04/
- CAISO 2024 Annual Report on Market Issues and Performance (official CAISO publication, 7 August 2025): total downward dispatch of wind and solar in 2024 — economic downward dispatch ~4,230 GWh (97% of curtailment), self-scheduled curtailment ~46 GWh (1%), exceptional dispatch curtailment ~3.5 GWh (<1%), "other" curtailment ~94 GWh (2.4%): https://www.caiso.com/documents/2024-annual-report-on-market-issues-and-performance-aug-07-2025.pdf
- CAISO daily/monthly curtailment report library (raw data underlying the above; CAISO stopped generating this specific report format as of 1 June 2025): https://www.caiso.com/library/daily-wind-solar-real-time-dispatch-curtailment-reports
- CAISO year-end 2024 cumulative curtailment report (year-to-date total 3,423,377 MWh through 31 December 2024 — closely matches the EIA-cited 3.4 million MWh): https://www.caiso.com/documents/wind-solar-real-time-dispatch-curtailment-report-dec-31-2024.pdf

### 4.2 ERCOT (Texas)

| Year | Wind curtailment (% of wind generation) | Solar curtailment (% of solar generation) | Combined wind+solar curtailed |
|---|---:|---:|---:|
| 2024 | >4% (curtailed due to congestion) | ~6% | >8 TWh |

Sources:
- Potomac Economics, *2024 State of the Market Report for the ERCOT Electricity Markets* (official ERCOT Independent Market Monitor report): wind generation grew 3.9% 2023→2024 with "more than 4% of output curtailed due to congestion"; solar generation grew 62% with "nearly 6% of that output curtailed": https://www.potomaceconomics.com/wp-content/uploads/2025/06/2024-State-of-the-Market-Report.pdf (also mirrored at https://www.potomaceconomics.com/wp-content/uploads/2025/05/2024-SoM-Report-Revision-Jul2025.pdf)
- FactSet Insight, "ERCOT Curtailments Persist as Load Rises," 25 February 2025 (2024 West zone alone: 3.1 TWh wind + 2.2 TWh solar curtailed; average curtailment ~1.2 GW/hour across ERCOT for the year): https://insight.factset.com/ercot-curtailments-persist-as-load-rises
- Modo Energy, "Saving wind and solar investments in ERCOT," 3 October 2025 (states ERCOT curtailed over 8 TWh of wind and solar energy in 2024): https://modoenergy.com/research/en/ercot-curtailment-crisis-solar-wind-data-battery-colocated-trends-maps-texas
- S&P Global Market Intelligence, 4 May 2026 (ERCOT wind+solar curtailment CAGR of 14.6% from 2020–2025, reaching 9.8 TWh by 2025): https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/05/renewable-energy-curtailment-offers-a-surplus-opportunity-for-texas-data-centers-1

### 4.3 Multi-ISO comparison (LBNL Land-Based Wind Market Report — the closest thing to a national wind-curtailment figure)

| ISO/RTO | 2023 wind curtailment rate |
|---|---:|
| SPP | 8.3% |
| ERCOT | 4.2% |
| NYISO | 3.3% |
| MISO | 3.2% |
| ISO-NE | 1.1% |
| CAISO | 0.6% |
| PJM | ≥0.1% (PJM likely under-reports; RTO does not regularly report full curtailment) |
| **All seven ISOs, weighted average** | **4.6%** |

Source: Lawrence Berkeley National Laboratory (LBNL), *Land-Based Wind Market Report: 2024 Edition*, published September 2024 — explicitly states "The overall wind power curtailment rate in 2023 across all seven regions was 4.6%," and gives the above regional breakdown: https://eta-publications.lbl.gov/sites/default/files/2024-09/land-based_wind_market_report_2024_edition.pdf

**Note on national coverage:** The 4.6% LBNL figure explicitly covers only wind (not solar) and only the seven ISO/RTO regions with published curtailment reporting (CAISO, ERCOT, MISO, ISO-NE, NYISO, PJM, SPP), which together cover most but not all U.S. wind capacity (vertically-integrated utilities outside RTO/ISO footprints, e.g. much of the Southeast, are excluded). There is no equivalent LBNL national solar-curtailment aggregate figure in this report.

### 4.4 Earlier NREL/multi-country academic comparison

NREL's cross-country PV curtailment study estimated 2018 solar curtailment at "more than 1%" of potential PV output in Arizona, California, Hawaii, and Texas combined, alongside comparisons to Chile, China, and Germany, but stops short of a single national U.S. figure: O'Shaughnessy, Cruce, and Xu, "Solar PV Curtailment in Changing Grid and Technological Contexts," NREL preprint, 2021: https://docs.nrel.gov/docs/fy21osti/74176.pdf

---

## 5. Methodological non-comparability of US EIA capacity factors and Chinese utilisation hours

This is the central caveat the pipeline must encode. Four distinct, separately documented reasons make a raw comparison of "EIA capacity factor" to "Chinese utilisation hours ÷ 8,760" invalid without adjustment.

### 5.1 China's official utilisation-hour formula uses *average* installed capacity for the period, not year-end (or start-of-period) capacity — this differs from EIA's method and matters enormously in a fast-growing fleet

- The official Chinese statistical definition, as published on China Energy Portal's translation of NEA/CEC reporting-system documentation, states plainly: "平均设备容量：指发电机组在报告期内按日历时间平均计算的容量" [Average equipment capacity: capacity calculated as a calendar-time-weighted average during the reporting period] and "平均利用小时：...发电设备平均利用小时 = 发电量 / 发电设备平均容量" [Average utilisation hours = generation ÷ average equipment capacity]: https://chinaenergyportal.org/statistical-reporting-system-for-renewable-energy/
- An academic methods paper on Chinese utilisation-hour benchmarking states explicitly: "这里的发电设备容量是计算利用小时的平均容量，而不是（统计期的）期末容量" [The generation equipment capacity used here is the average capacity used to calculate utilisation hours, not the period-end capacity]: https://base4zgdl.xml-journal.net/cn/article/pdf/preview/10.11930/j.issn.1004-9649.202103120.pdf
- Baidu Baike's technical definition entry for "发电设备平均利用小时" [Average utilisation hours of power generation equipment] confirms the same formula (generation ÷ average installed capacity for the period), and gives the standard thermal-plant decomposition formula (8760h × equipment availability rate × annual load factor × (1 − reserve/outage rate)): https://baike.baidu.com/item/%E5%8F%91%E7%94%B5%E8%AE%BE%E5%A4%87%E5%B9%B3%E5%9D%87%E5%88%A9%E7%94%A8%E5%B0%8F%E6%97%B6/6028653

**Why this matters for cross-country comparability:** EIA's capacity factor also uses a *time-adjusted (average) capacity* basis for the annual figure ("Time adjusted capacity for year rows is a time-weighted average of the month rows" — https://www.eia.gov/electricity/monthly/xls/table_6_07_a.xlsx technical note), so on this specific dimension the two countries' *headline annual* figures are actually computed on a similarly-averaged basis. The comparability risk instead arises from (a) how far into the year new capacity was added, since a plant added in December contributes ~0 generation but is included in some simplified year-end-capacity calculations that outside analysts sometimes perform on China when the average-capacity data is unavailable or not used correctly, and (b) the scope/frequency differences below. A vivid illustration of an analyst getting this wrong when using year-end capacity instead of average capacity for China's solar fleet: a LinkedIn analysis found that "normalizing against the [year-end] capacity of 609 GW" gives 2023 China solar capacity factor of only ~11%, while "normalizing with reference to the beginning of 2023" (i.e., closer to an average-capacity basis) gives ~17% — a 6-percentage-point swing purely from the choice of capacity denominator in a fast-growing fleet: https://www.linkedin.com/posts/mattiamarinelli_i-got-my-feed-flooded-by-posts-claiming-that-activity-7209825909749514240-Ytd7 (Mattia Marinelli, 21 June 2024). This is exactly the failure mode point 5 warns against, and it is a common error made by outside commentators (not by CEC/NEA's own official average-capacity-based figures) — so the pipeline should flag that misapplication of China's officially-averaged utilisation-hour statistic, or substitution of year-end capacity by a third party, is the likely source of "China solar capacity factor is absurdly low" claims circulating outside the primary statistics.

### 5.2 Installed capacity is reported gross of generator own-use (self-consumption), not net — while EIA's basis is net generation

Lawrence Berkeley National Laboratory's *Excess Capacity in China's Power System: A Regional Analysis* states directly: "installed capacity data in China is reported as gross, rather than net, of generator own-use, whereas effective capacity should be net of own-use." LBNL applies own-use adjustment factors of 1% (hydro), 5% (thermal), 5% (nuclear), 1% (wind), 1% (solar), 5% (other) to convert Chinese gross installed capacity to net "effective capacity" for its own reserve-margin analysis. Source: LBNL, published version at https://eta-publications.lbl.gov/sites/default/files/lbnl1006638.pdf (Section 3.4, "Effective Generation Resources," and Table 8).

EIA's net generation basis (Form EIA-923, "net generation") is *already* net of station/auxiliary power use, so a raw ratio of Chinese gross-capacity-based utilisation hours to EIA's net-generation-based capacity factor compares a gross-denominator statistic to a net-numerator/net-denominator statistic — not like-for-like.

### 5.3 Behind-the-meter and captive generation are excluded from grid-connected utilisation-hour statistics in China, in a way that is not symmetric with the EIA utility-scale definition

LBNL's same report notes: "China has a significant amount of behind-the-meter thermal generation, and the extent to which this generation is able to contribute to resource adequacy is unclear," and assumes (for lack of official data) that behind-the-meter generation was 8% of the total in 2014, with a 90% load factor, only half of which is assumed available at peak: https://eta-publications.lbl.gov/sites/default/files/lbnl1006638.pdf (Section 3.4). This means official Chinese utilisation-hour figures (which are collected from grid-connected plants ≥6,000 kW reporting to CEC/NEA) omit an amount of self-generated, behind-the-meter industrial capacity that has no single clean EIA analogue, since EIA's "utility-scale" (≥1 MW) definition also excludes small/behind-the-meter generation but at a much lower size threshold (1 MW vs. 6 MW) and with different ownership-reporting incentives.

### 5.4 China's grid-connected wind/solar utilisation-rate denominator specifically nets out only "system cause"-restricted curtailment, and independent researchers argue the official curtailment rate is likely understated

The 2024 official NEA figures are explicitly computed "仅考虑系统原因受限电量" [only considering electricity restricted for grid-system reasons] per NEA's own notice 国能发电力〔2024〕44号, as stated in the source news release: https://newenergy.in-en.com/html/newenergy-2438688.shtml. This means non-system-cause reasons a plant might not generate (e.g., a developer voluntarily limiting hours to stay under a provincial curtailment cap; see Section 3.4) are excluded from the numerator, producing what one 2026 peer-reviewed paper calls a probable underestimate, particularly for solar: https://pmc.ncbi.nlm.nih.gov/articles/PMC13378348/. No equivalent, single "system-cause-only" carve-out exists in the U.S. ISO curtailment figures cited in Section 4, which generally report all economic and reliability-driven downward dispatch (see the CAISO breakdown in Section 4.1, which explicitly itemizes "economic," "self-scheduled," and "exceptional dispatch" categories together).

### 5.5 Summary table of the four non-comparability mechanisms

| Mechanism | US/EIA basis | China/CEC-NEA basis | Direction of bias if unadjusted |
|---|---|---|---|
| Capacity denominator timing | Time-weighted average capacity within year (official) | Time-weighted average capacity within year (official) — but analysts sometimes substitute year-end capacity | Substituting year-end capacity for China understates its true average-basis capacity factor in fast-growing years (solar/wind) |
| Gross vs. net of own-use | Net generation (EIA-923) over net-of-auxiliary-use implicit basis | Gross installed capacity, not net of generator own-use (LBNL) | Overstates apparent installed base, understating implied Chinese capacity factor by a few percentage points |
| Behind-the-meter/captive generation | Utility-scale ≥1 MW threshold, excludes small/BTM | Grid-connected reporting threshold ≥6,000 kW (6 MW), excludes captive/BTM industrial generation (LBNL: ~8% of total in 2014) | Different exclusion thresholds mean the two "fleets" being measured are not the same population |
| Curtailment-rate scope | ISO-reported curtailment generally includes economic + reliability causes | Official 弃风率/弃光率 only counts "system cause"-restricted power; independent estimates suggest under-statement | Chinese official curtailment rate is a lower bound, not a full accounting, of foregone renewable output |

---

## 6. Gaps and non-existent sources

The following items were explicitly searched for and **could not be found in a published, official, primary-source form** meeting the task's citation bar. Each entry states what was searched.

1. **A single U.S. national wind or solar curtailment rate (EIA/national analogue to China's 弃风率/弃光率).** Searched EIA Electric Power Monthly/Annual, EIA Today in Energy archive, and LBNL/NREL curtailment literature. **Finding: no such single national figure is published.** EIA and LBNL both report only at ISO/balancing-authority level (CAISO, ERCOT, and the LBNL seven-ISO wind aggregate at 4.6% for 2023 — see Section 4.3). This gap is stated in Section 4 with the best available regional substitutes and their coverage explicitly noted.

2. **A U.S. national *solar* curtailment aggregate analogous to the LBNL wind aggregate.** Searched LBNL publications (Land-Based Wind Market Report covers wind only), NREL solar reports, and EIA. **Finding: no equivalent multi-ISO national solar curtailment aggregate was located.** Only CAISO (Section 4.1) and ERCOT (Section 4.2) solar-specific figures exist among the sources found; other ISOs (MISO, PJM, SPP, NYISO, ISO-NE) do not appear to separately/consistently publish solar curtailment percentages in the sources reviewed.

3. **China's 2023 national utilisation hours by every individual technology, in one single official document, matching the granularity of the 2024 NEA release.** The full 2023 national breakdown had to be reconstructed from multiple secondary compilations of the *China Electricity Statistical Yearbook 2024* (coal 4,690 h, gas 2,525 h, hydro-total 3,130 h, pumped storage 1,176 h, nuclear 7,670 h, and a solar figure of 1,291 h drawn from a different regional table in the same Yearbook) rather than one clean summary table, because **NEA itself stopped publishing the full by-technology monthly utilisation-hour breakdown partway through 2024** (confirmed by Dialogue Earth and Environment+Energy Leader, both cited in Section 2.2). This is a genuine, documented reduction in official Chinese data granularity, not a research shortfall — flagged explicitly for the pipeline.

4. **A single, unambiguous, citable "official" statement from CEC/NEA that directly and explicitly says "our utilisation-hours figure is not comparable to a Western capacity factor for reasons X, Y, Z."** No such self-critical methodological statement from the Chinese statistical authorities themselves was found. All the non-comparability analysis in Section 5 is necessarily drawn from **third-party researchers (LBNL, academic authors, and one independent analyst)** analyzing the official Chinese data, not from a Chinese-government-published methodological caveat. This should be understood as the nature of the available literature, not a search failure — the underlying statistical bureaus (CEC, NEA, NBS) publish the numbers and formula definitions (Section 5.1) but not a comparative critique of their own international comparability.

5. **A single EIA table that reports "natural gas combustion turbine" as a distinct line separate from EIA's own "Gas Turbine" category.** No separate line exists; EIA's Table 6.07.A "Gas Turbine" category is the closest match and is used as such in Section 1.1 — flagged so the pipeline does not treat this as a missing data point but as a labeling equivalence.

6. **Provincial-level Chinese utilisation-hours or curtailment broken out specifically for offshore wind versus onshore wind at the national level for 2023/2024.** NEA's monthly statistical reporting system template does include separate codes for 陆上风电 (onshore wind, code 14) and 海上风电 (offshore wind, code 15) per the China Energy Portal methodology page (https://chinaenergyportal.org/statistical-reporting-system-for-renewable-energy/), confirming the reporting *category* exists, but a populated **national annual onshore-vs-offshore utilisation-hours split for 2023 or 2024 was not located** in the sources reviewed for this task. The wind figures reported in Sections 2.1–2.2 above are combined onshore+offshore ("并网风电").

---

## Source list (deduplicated, by section)

**Section 1 (US EIA):**
- https://www.eia.gov/electricity/monthly/
- https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_a
- https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_b
- https://www.eia.gov/electricity/monthly/xls/table_6_07_a.xlsx
- https://www.eia.gov/electricity/monthly/xls/table_6_07_b.xlsx
- https://www.eia.gov/tools/faqs/faq.php?id=101&t=3
- https://www.eia.gov/tools/faqs/faq.php?id=104&t=3
- https://www.eia.gov/electricity/annual/pdf/epa.pdf
- https://www.eia.gov/electricity/annual/html/epa_04_08_b.html
- https://storage.googleapis.com/visualizingenergy_database/data/ve121.03_averageannualcapacityfactorselectricitygeneration2022.csv
- https://www.eia.gov/todayinenergy/detail.php?id=61444
- https://www.epa.gov/system/files/documents/2023-05/Power%20Sector%20Trends%20TSD.pdf

**Section 2 (China utilisation hours):**
- https://www.ccpua.org/page116.html?article_id=6549
- https://www.ccpua.org/page210.html?article_id=6549
- https://www.cpnn.com.cn/news/xwtt/202501/t20250121_1768557.html
- https://www.nea.gov.cn/20250121/097bfd7c1cd3498897639857d86d5dac/c.html
- https://pdf.dfcfw.com/pdf/H3_AP202512311811775347_1.pdf
- https://usercontent.one/wp/www.cet.energy/wp-content/uploads/2025/03/2025-03-CET_Summary-of-Chinas-energy-and-power-sector-statistics-in-2024.pdf
- https://www.spglobal.com/energy/en/news-research/latest-news/energy-transition/013124-coal-still-accounted-for-nearly-60-of-chinas-electricity-supply-in-2023-cec
- https://www.nea.gov.cn/2024-03/25/c_1310768833.htm
- https://www.nea.gov.cn/2024-04/22/c_1310772067.htm
- https://pdf.dfcfw.com/pdf/H3_AP202406171636462381_1.pdf
- https://www.nea.gov.cn/2024-07/20/c_1310782235.htm
- https://dialogue.earth/en/digest/clean-energy-use-data-missing-from-gov-release/
- https://www.environmentenergyleader.com/stories/lack-of-detailed-renewable-data-in-chinas-power-report-sparks-questions,44788
- https://gulfnews.com/business/energy/chinas-installed-power-generation-capacity-climbs-155-by-end-march-2026-1.500517430
- https://english.news.cn/20260423/766d32839b164738a5c1cc23ff5bb26a/c.html
- https://news.metal.com/newscontent/103555031/nea-data-installed-wind-emsolarem-capacity-hits-around-17-billion-kw-as-of-august-31-emsolarem-surges-485-yoy

**Section 3 (China curtailment):**
- https://www.ndrc.gov.cn/wsdwhfz/202406/t20240621_1391234.html
- https://www.nea.gov.cn/20251113/cc1fb0298a2944f8bd5441f67c9be9b3/20251113cc1fb0298a2944f8bd5441f67c9be9b3_54b6e6c1674e9c4bdca1cdfb4cbb16b477.doc
- https://newenergy.in-en.com/html/newenergy-2438688.shtml
- https://zjic.zj.gov.cn/ywdh/nyhj/202408/t20240812_22695794.shtml
- https://www.reuters.com/sustainability/climate-energy/chinas-renewable-capacity-soars-utilisation-lags-data-show-2025-08-05/
- https://www.bloomberg.com/news/articles/2025-04-02/china-curtails-more-renewables-as-record-additions-stress-grid
- https://www.bloomberg.com/news/articles/2026-04-08/china-s-wasting-too-much-renewable-power-as-curtailments-rise
- https://www.bloomberg.com/news/articles/2025-08-05/china-s-record-renewables-buildout-is-wasting-power-as-grid-lags
- https://finance.sina.com.cn/roll/2025-08-18/doc-infmmmiy1960581.shtml
- https://iea.blob.core.windows.net/assets/88a07dd9-42fe-4232-842e-9015b4b647f8/Renewables2024.pdf
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13378348/

**Section 4 (US curtailment):**
- https://www.eia.gov/todayinenergy/detail.php?id=65364
- https://www.reuters.com/business/energy/rising-curtailments-california-underline-us-grid-ordeal--reeii-2026-08-04/
- https://www.caiso.com/documents/2024-annual-report-on-market-issues-and-performance-aug-07-2025.pdf
- https://www.caiso.com/library/daily-wind-solar-real-time-dispatch-curtailment-reports
- https://www.caiso.com/documents/wind-solar-real-time-dispatch-curtailment-report-dec-31-2024.pdf
- https://www.potomaceconomics.com/wp-content/uploads/2025/06/2024-State-of-the-Market-Report.pdf
- https://insight.factset.com/ercot-curtailments-persist-as-load-rises
- https://modoenergy.com/research/en/ercot-curtailment-crisis-solar-wind-data-battery-colocated-trends-maps-texas
- https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/05/renewable-energy-curtailment-offers-a-surplus-opportunity-for-texas-data-centers-1
- https://eta-publications.lbl.gov/sites/default/files/2024-09/land-based_wind_market_report_2024_edition.pdf
- https://docs.nrel.gov/docs/fy21osti/74176.pdf

**Section 5 (methodological critique):**
- https://eta-publications.lbl.gov/sites/default/files/lbnl1006638.pdf
- https://chinaenergyportal.org/statistical-reporting-system-for-renewable-energy/
- https://base4zgdl.xml-journal.net/cn/article/pdf/preview/10.11930/j.issn.1004-9649.202103120.pdf
- https://baike.baidu.com/item/%E5%8F%91%E7%94%B5%E8%AE%BE%E5%A4%87%E5%B9%B3%E5%9D%87%E5%88%A9%E7%94%A8%E5%B0%8F%E6%97%B6/6028653
- https://www.linkedin.com/posts/mattiamarinelli_i-got-my-feed-flooded-by-posts-claiming-that-activity-7209825909749514240-Ytd7
