# Model specification

Hierarchical Bayesian nonlinear state-space model for the relative techno-industrial trajectories of the United States and the People's Republic of China, 2026-2075.

Committed **before** any estimation code exists. This file states what will be estimated, not what was found. Its commit timestamp precedes the first line of model code in this repository, and that ordering is checkable from the history.

The specification is written to be refutable at the level of structure, not only of parameters. Where a modelling choice could plausibly go the other way, the alternative is named and the reason for the committed choice is given. Where a choice is arbitrary, it is labelled arbitrary.

---

## 1. What the model is for

The model does **not** forecast a winner. It estimates the posterior distribution over a small set of structural parameters, and reports which of five outcome regimes those parameters imply, with mass on each.

| Regime | Description |
|---|---|
| `R1` | PRC-favourable divergence across the capability vector |
| `R2` | US-favourable divergence across the capability vector |
| `R3` | PRC peaking — early gain followed by structural reversal |
| `R4` | **Segmented bipolarity** — divergence by domain, no single hierarchy |
| `R5` | Dual systemic constraint — both states constrained below their own trajectories |

`R4` is the expected result. It is expected because it is the regime consistent with the observed data pattern at baseline, not because it is preferred, and the model must be able to place low mass on it. A specification under which `R4` cannot receive posterior mass below 0.2 for any admissible data is misspecified and must be rejected; this is checked in `IDENTIFICATION.md` under the prior-predictive test.

The three propositions from `README.md` are scored separately against the regime posterior:

- **P1** is supported when mass concentrates on `R1` or on the early phase of `R3`.
- **P2** is supported when the estimated elasticity and weighting parameters imply that AI-robotics intensity raises the marginal capability return to deployment-bundle inputs.
- **P3** is supported when mass concentrates on `R4`.

P1 and P3 can both be false, both true, or dissociated. That dissociation is the analytically interesting case and the specification is built to expose it rather than to average over it.

---

## 2. Notation

All notation is plain text. LaTeX is avoided in this repository so that specifications remain greppable and diffable.

```
i           state index, i in {US, CN}
t           year index, 2026..2075 for projection; 1975..2025 for estimation
x[i,t]      latent input vector for state i at time t
Y[i,t]      latent capability vector for state i at time t, four elements
z[i,t]      observed indicator vector, many-to-one onto x and Y
theta       time-invariant structural parameters
s[t]        time-varying states: elasticity, AI-robotics intensity, stress
```

The capability vector `Y` has the four elements fixed in `README.md`, in this order:

```
Y[1] = Y_throughput   (primary)
Y[2] = Y_frontier
Y[3] = Y_net
Y[4] = Y_fin
```

No scalar collapse of `Y` appears anywhere in the estimation. Where a scalar is required for exposition, it is produced post hoc by an explicit weighting and reported only with the full weighting sensitivity surface, per `README.md`.

---

## 3. Three-block structure

The model has three blocks, estimated jointly.

```
  Block M -- measurement:   z[i,t]  <- x[i,t], Y[i,t], source bias, source noise
  Block E -- evolution:     x[i,t]  <- x[i,t-1], s[t], shocks
  Block P -- production:    Y[i,t]  <- x[i,t], s[t], theta
```

Joint estimation is a commitment, not a convenience. Estimating Block M separately and passing point estimates into Block P would suppress measurement uncertainty exactly where it is largest — the PRC series carrying the falsification band from `DATA-INTEGRITY.md` — and would make the resulting credible intervals dishonest. The cost is a harder sampler; the cost is accepted.

---

## 4. Block M — measurement with source-specific bias

Every observed series is treated as a noisy, possibly biased view of a latent quantity. No series is treated as the quantity itself.

```
z[k,i,t] = lambda[k] * f_k(x[i,t], Y[i,t]) + b[k,i] + eps[k,i,t]

eps[k,i,t] ~ Normal(0, sigma[k]^2)
```

where `k` indexes source-series pairs, `lambda[k]` is a loading, `b[k,i]` is a **source- and state-specific** bias term, and `f_k` is the committed mapping from latent inputs to what that series purports to measure.

### 4.1 Bias terms are symmetric by construction

The prohibition on asymmetric epistemic standards in `README.md` is implemented here rather than asserted. Every observed series carries a bias term. PRC series are not the only ones granted one.

| Series family | Bias term | Prior source |
|---|---|---|
| PRC GDP-linked | `b` estimated, informative prior | 0.5-2.0pp falsification band, `DATA-INTEGRITY.md` |
| US fiscal projections | `b` estimated, informative prior | Published CBO projection-error bands |
| US inequality measures | `b` estimated, wide prior | Competing-approach range carried, not resolved |
| Physically measurable (generation capacity) | `b` fixed at 0, `sigma` small | Rule: physically measurable series get no bias term |
| Independently audited | `b` estimated, tight prior | Audit is evidence of small bias, not of none |

A series is granted `b = 0` only if it is physically measurable in the sense of `DATA-INTEGRITY.md` tier 1. That is the single asymmetry in the block, and it is an asymmetry between **measurement types**, not between countries.

### 4.2 The identification problem this creates, stated plainly

A free bias term per source-state pair is not identified from a single series. Identification comes from **multiple sources on the same latent quantity** with at least one tier-1 or tier-2 anchor. Where no anchor exists, the bias and the latent level are not separately identified and the model must not pretend otherwise.

Committed consequence: for any latent quantity lacking an anchored series, `b` is **fixed** at its prior mean rather than estimated, and the affected posterior is flagged `anchor_absent` in every output that consumes it. The list of anchor-absent quantities is published with the estimates, not buried.

### 4.3 Structural breaks enter the measurement block

The break registry in `DATA-INTEGRITY.md` is consumed here. A registered break splits the affected series into two series with separate loadings and separate bias terms. Pre-break and post-break observations are never pooled under one `lambda`.

Two breaks are live and known at time of writing:

- The December 2023 PRC youth-unemployment methodology change, already registered.
- **New, registered by this commit:** the IFR robot-density discontinuity for China between the World Robotics 2024 and 2025 vintages, arising from a National Bureau of Statistics revision to the manufacturing-employment denominator. Reported density falls from 470 per 10,000 (2023 data) to 166 per 10,000 (2024 data) while absolute robot stock rises past 2,027,000 units and 2024 installations reach 295,000 units ([IFR World Robotics 2024 press release](https://ifr.org/ifr-press-releases/news/global-robot-density-in-factories-doubled-in-seven-years), [IFR World Robotics 2025 executive summary](https://ifr.org/img/worldrobotics/Executive_Summary_WR_2025_Industrial_Robots.pdf), [IFR China 2 million robots release](https://ifr.org/downloads/press_docs/2025-09-25-IFR_press_release_China_in_English.pdf)).

The second break vindicates the denominator decomposition already committed in `pipeline/adapters/F7.md`. It also means the raw density series is unusable across the break, and the model consumes the **stock** term rather than the density ratio. Rule `R008` is registered for this adjustment.

---

## 5. Block E — input evolution

Six inputs, three per bundle, as fixed in `README.md`.

```
Deployment bundle:  D1 dispatchable-adjusted electrical energy
                    D2 grid transmission capacity
                    D3 deployed industrial robot stock

Frontier bundle:    F1 frontier-capable compute
                    F2 capital depth
                    F3 human capital
```

Each input follows a local-linear-trend state-space process with a saturating term, in logs:

```
log x[j,i,t] = log x[j,i,t-1] + g[j,i,t-1] - kappa[j] * (x[j,i,t-1] / xbar[j,i])^phi[j] + u[j,i,t]
g[j,i,t]     = rho_g * g[j,i,t-1] + (1 - rho_g) * gstar[j,i] + v[j,i,t]
```

The saturating term is what prevents the model from extrapolating a 2020s build rate to 2075 — the single most common failure of long-horizon capability projection. `xbar[j,i]` is a state-specific saturation scale with its own prior; `phi[j]` controls how sharply saturation bites.

**Committed:** identical functional form for both states. Asymmetry between the US and the PRC enters **only** through estimated parameter values, never through a different equation. A specification in which one state has a term the other lacks is a specification that has assumed its conclusion.

### 5.1 The stabilisation coefficient may be negative

`DATA-INTEGRITY.md` records the reflexivity problem: a state that observes a deteriorating indicator may act to correct it, so the indicator's own trajectory is not exogenous to policy response. This is modelled with a stabilisation coefficient on the growth equation, entering as a feedback from the state's own stress level:

```
gstar[j,i] = gstar0[j,i] + psi[j,i] * (stress[i,t] - stressbar[i])
```

`psi[j,i]` is **permitted to take either sign** and its prior is centred at zero. A negative `psi` means stress suppresses input growth; a positive `psi` means stress mobilises corrective investment. Both are historically observable, on both sides. Forcing the sign would embed a theory of state capacity that the model is supposed to test.

---

## 6. Block P — the two-level nested production function

This is the heart of the specification and the object the central empirical question is about.

### 6.1 The nest

```
Deployment aggregate:  Q_D = CES( D1, D2, D3 ; sigma_D )
Frontier aggregate:    Q_F = CES( F1, F2, F3 ; sigma_F )
Capability element:    Y[m] = CES( Q_D, Q_F ; sigma_top[t] ; weights w[m] )
```

with

```
CES(a, b ; sigma) = ( alpha * a^r + (1 - alpha) * b^r )^(1/r),   r = (sigma - 1)/sigma
```

The element-specific weights `w[m]` are what make `Y` a vector rather than a scalar: `Y_throughput` loads primarily on `Q_D`, `Y_frontier` primarily on `Q_F`, `Y_net` and `Y_fin` on both with different intensities. The weights are estimated, not assumed, subject to ordering constraints stated in `PRIORS.md`.

### 6.2 Nesting order is a data question, not an assumption

`README.md` commits that the nesting structure is determined by the data. Three candidate structures are estimated and compared:

| Structure | Reading |
|---|---|
`(D)(F)`  | Deployment and frontier aggregate separately, then combine — the committed default |
`(D F1)(F2 F3)` | Compute groups with deployment; capital and human capital separate |
`(D3 F1)(D1 D2)(F2 F3)` | Robotics groups with compute — the "embodied AI" structure |

Comparison is by leave-one-decade-out predictive density, not by in-sample fit. The third structure is included because it is the structure under which P2 is most naturally true, and excluding it would make P2 easier to support than it should be.

Precedent exists for nesting order being data-determined and for the intuitive ordering losing: van der Werf's twelve-country OECD panel finds `(KL)E` fits best ([Production Functions for Climate Policy Modeling](https://d-nb.info/1128231875/34)), while Shen and Whalley find `(E,L)K` statistically more appropriate for China than the widely used `(K,L)E` ([NBER Working Paper 19104](https://www.nber.org/system/files/working_papers/w19104/w19104.pdf)). That two careful studies reach different orderings on different samples is the reason this is estimated rather than asserted.

### 6.3 The top elasticity is a time-varying state

`sigma_top[t]` is not a constant. Over a fifty-year horizon a constant substitution elasticity is a strong and almost certainly false assumption, and it is precisely the assumption that would foreclose the central question.

```
logit_s[t] = logit_s[t-1] + delta * AI_intensity[t] + w[t],   w[t] ~ Normal(0, tau^2)
sigma_top[t] = sigma_min + (sigma_max - sigma_min) * inv_logit(logit_s[t])
```

`delta` is the **mechanism parameter**. It is the quantitative content of P2:

| `delta` | Interpretation | Bearing on P2 |
|---|---|---|
| `delta > 0` | AI-robotics intensity raises substitutability between bundles | P2 undermined — frontier capability can substitute for deployment scale |
| `delta ~ 0` | Intensity does not shift the relation | P2 not supported |
| `delta < 0` | Intensity drives the bundles toward complementarity — alternating bottlenecks | **P2 supported** |

Writing P2 as the sign of a single estimated parameter is the sharpest available commitment. It also means P2 is refutable on the estimation alone, independent of F1-F8. That redundancy is deliberate: a proposition testable by two independent routes is harder to rescue.

### 6.4 Alternating bottlenecks are a prediction, not a description

`sigma_top[t] < 1` with a shifting binding constraint produces alternating bottlenecks endogenously: whichever bundle is relatively scarcer dominates the marginal product. The model therefore predicts the **sequence** of binding constraints, and that sequence is checkable against history in the backtests. A specification that could only describe alternation after the fact would be worth much less.

---

## 7. AI-robotics intensity

`AI_intensity[t]` is a latent scalar per state, not an observable. It is measured through the indicator block from: frontier-capable compute stock under the boundary in `pipeline/definitions/frontier-compute.md`, robot stock from the decomposed IFR series, and manufacturing output per unit of installed automation.

It is deliberately **not** measured using any AI-exposure index of occupations. Those indices are the disputed object in F4, whose named source does not exist, and importing them here would make the mechanism parameter depend on the one falsifier that cannot resolve.

---

## 8. Political stress

`stress[i,t]` enters Block E through `psi` and enters `Y_net` as a deduction. Its construction, the decision to adopt a published specification verbatim, and the substantial published criticism of that specification are treated in `POLITICAL-STRESS.md`.

Both states carry a stress term computed the same way. Neither is modelled as institutionally healthy, per the second standing prohibition.

---

## 9. Output contract

The model emits, for every reported horizon in `{2030, 2040, 2050, 2075}`:

1. Posterior mass on each of `R1..R5`, with `2075` labelled low-confidence in every output that contains it.
2. Posterior for `Y[m]` ratios by element, never aggregated.
3. Posterior for `delta`, `sigma_top[t]`, `sigma_D`, `sigma_F`, and every `psi[j,i]`.
4. **Explicit statement of the parameter regions in which the core thesis is false**, with their posterior mass. An output that does not contain this is not publishable.
5. Prior-versus-posterior contraction diagnostics for every parameter, per `README.md`. Parameters whose posterior is indistinguishable from prior are reported as **not learned** rather than reported as estimates.
6. The `anchor_absent` list from section 4.2.

### 9.1 Contraction is a publication gate, not a diagnostic footnote

If the posterior for `delta` shows contraction below a pre-registered threshold, the correct report is that the mechanism claim was not learned from the data. It is not "weak evidence for P2". The threshold and the metric are fixed in `PRIORS.md`.

---

## 10. Implementation commitments

| Item | Commitment |
|---|---|
| Language | Python |
| Sampler | NumPyro NUTS; Stan retained as an independent cross-check on the reduced model |
| Chains | 4 minimum, 8 for published runs |
| Convergence | `r_hat < 1.01` all parameters, ESS > 400 per chain, zero divergences after adaptation |
| Divergences | A published run with divergent transitions is not published. Reparameterise or report failure |
| Seed | Recorded per run; results are reproducible bit-for-bit given seed and rule versions |
| Data interface | Reads only `data/derived/` and `data/adjudicated/`, never `data/raw/` |
| Failure disclosure | A specification that will not converge is reported as such, with the failing configuration committed |

The last row is the one that costs something. A non-converging model is ordinarily quietly replaced by a simpler one; here the failure and the abandoned configuration are committed, because the sequence of specifications tried is itself information about how strong the identification is.

---

## 11. What this specification cannot do

Stated here so that it need not be discovered by a reader.

- It cannot resolve the counterfactual of policy response. `psi` absorbs reflexivity as a reduced-form feedback; it does not model decisions.
- It cannot identify bias for any latent quantity lacking an anchored series, and says so per quantity.
- It cannot deliver a defensible 2075 point estimate. The 2075 outputs exist to show how fast the credible intervals widen, which is an argument for humility rather than a forecast.
- It cannot distinguish `R4` from `R5` in the region where both bundles saturate simultaneously. That degeneracy is characterised in `IDENTIFICATION.md` rather than resolved.
- It has no mechanism for military conflict. A specification claiming to price war outcomes in a production function would be a specification claiming more than it can support.

---

## Sources

- IFR, World Robotics 2024 press release — https://ifr.org/ifr-press-releases/news/global-robot-density-in-factories-doubled-in-seven-years
- IFR, World Robotics 2025 executive summary — https://ifr.org/img/worldrobotics/Executive_Summary_WR_2025_Industrial_Robots.pdf
- IFR, China tops world record of 2 million factory robots — https://ifr.org/downloads/press_docs/2025-09-25-IFR_press_release_China_in_English.pdf
- van der Werf, Production Functions for Climate Policy Modeling — https://d-nb.info/1128231875/34
- Shen and Whalley, Capital-Labor-Energy Substitution in Nested CES Production Functions for China, NBER WP 19104 — https://www.nber.org/system/files/working_papers/w19104/w19104.pdf


---

## Amendment 01 — 19 August 2026

Appended, not substituted. The sections above stand as originally committed; where this amendment and the original text differ, both readings are on the record and the divergence is stated here.

### 01.1 Registration of R009, regime classification

The output contract in section 3 names five regimes and does not specify the procedure mapping a simulated trajectory to one of them. That procedure is now registered as rule **R009**, version 0.1.0, specified in `pipeline/rules/R009-regime-classification.md` and implemented in `pipeline/src/usbip/model/prior_predictive.py`.

It is registered as a rule rather than left as model internals because its behaviour determined a gate outcome. PP2 failed at run 001 because the classifier sent every unclassifiable trajectory to R4, making the thesis regime a sink that could not be pushed below 0.2 prior mass by any adversarially chosen baseline. A component that can decide whether the central claim is refutable is not an implementation detail.

Three constants are registered with it: `DEADBAND` 0.10, `REVERSAL_DEPTH` 0.15, `CONSTRAINT_RATIO` 0.60. None is sourced and no sensitivity run over them exists. `CONSTRAINT_RATIO` governs the R5 branch, which currently fails PP1, so it is a parameter whose adjustment would make a failing gate pass; it is frozen and the failure is reported.

Two substantive divergences from the text above:

- **R3 is defined generically as challenger peaking**, not as PRC peaking. Under the state swap that PP4 tests, "PRC peaking" would have to become "US peaking", which is not in the regime set, so the PRC-specific label breaks equivariance while the concept does not. The PRC reading is recovered by observing which state is the challenger in the data.
- **A sixth label, `R0_no_material_change`, is added** and exempted from the PP1 coverage floor. The five regimes are described above as an exhaustive partition and they are not: a world in which neither state moves materially beyond the deadband is a possible world and is none of the five. It carries 0.385 prior mass at the 2030 horizon, which is itself worth stating — claims about relative position on a 2030 horizon are substantially claims about measurement noise.

### 01.2 Declaration of ENGINEERING_CEILING_MULTIPLE

Section 5 commits `xbar[j] ~ LogNormal(log(ceiling[j]), 0.6)` without declaring the ceilings. They are declared here, as multiples of each input's 2026 baseline:

| Input | Multiple |
|---|---:|
| D1 generation capacity | 4.0 |
| D2 transmission | 4.0 |
| D3 industrial robotics | 5.0 |
| F1 frontier compute | 8.0 |
| F2 R&D intensity | 6.0 |
| F3 advanced manufacturing | 3.0 |

Declared during Phase 3 because the implementation had drawn `uniform(3, 30) * baseline` for every input, contradicting the committed form. The values are ordered on the reasoning that compute has the most headroom and R&D intensity as a share of output the least, and they are judgement calls rather than sourced figures.

Lowering them is named in `model/PRIOR-PREDICTIVE-RUN-001.md` section 3.1 as a candidate remedy for the PP1 failure that has **not** been taken. Any future change requires a dated amendment with justification independent of gate outcomes, since a lower ceiling would bring both states into constraint by 2050 and so make PP1 pass.

### 01.3 Prior-predictive outcome, and the consequence for estimation

Section 10 commits that the gates are run before estimation and that failures are reported rather than resolved by adjusting priors until they pass. The gates have been run. **PP1 and PP3 fail at the committed priors and estimation is blocked.** Full disclosure, including two implementation defects, one prior-transcription defect, and a false diagnosis produced by the last of these, is in `model/PRIOR-PREDICTIVE-RUN-001.md`.

Both failures localise to `PRIORS.md` section 4 rather than to Blocks E, P or M. Candidate remedies are enumerated there and none has been chosen; the choice is deferred to a further dated amendment and will be made on grounds independent of which option makes a gate pass. The failing configuration is committed as-is so the amendment can be read against it.

### 01.4 R003 specified

`DATA-INTEGRITY.md` mandates the nameplate-to-dispatchable conversion for every series entering `Y_throughput`, and the rule was outstanding. It is now specified at version 0.1.0 in `pipeline/rules/R003-nameplate-to-dispatchable.md`, with US capacity factors from EIA Tables 6.7.A and 6.7.B, PRC factors implied from CEC and NEA utilisation hours, and published LBNL own-use adjustments applied to PRC gross capacity.

The rule carries a prohibition: because PRC factors derive from a differently scoped statistic, it refuses to produce a cross-state dispatchable ratio. Relative position enters through the measurement block, where a definitional gap is represented as uncertainty rather than absorbed into a ratio.

One expectation was refuted in the course of specifying it. The standard objection to comparing the two statistics is that PRC utilisation hours use a year-end capacity denominator. The published Chinese methodology is explicitly an average, calendar-time weighted, and EIA's annual figure is likewise a time-weighted average of monthly values, so on that dimension the official figures are comparable. The denominator error is real only in third-party recomputation. The refutation is recorded because the same reasoning would have justified an adjustment factor that is not warranted.

### Sources for this amendment

- `pipeline/rules/R009-regime-classification.md`
- `pipeline/rules/R003-nameplate-to-dispatchable.md`
- `model/PRIOR-PREDICTIVE-RUN-001.md`
- `model/prior-predictive-run-003.txt`
- EIA, Electric Power Monthly Table 6.7.A — https://www.eia.gov/electricity/monthly/xls/table_6_07_a.xlsx
- EIA, Electric Power Monthly Table 6.7.B — https://www.eia.gov/electricity/monthly/xls/table_6_07_b.xlsx
- NEA, 2024 national electric power industry statistics — https://www.nea.gov.cn/20250121/097bfd7c1cd3498897639857d86d5dac/c.html
- LBNL, Excess Capacity in China's Power System — https://eta-publications.lbl.gov/sites/default/files/lbnl1006638.pdf
- China Energy Portal, statistical reporting system for renewable energy — https://chinaenergyportal.org/statistical-reporting-system-for-renewable-energy/

---

## Amendment 02 -- 2026-08-20 -- output contract restricted: R5 reported at 2075 only

**Appended, not substituted.** Selected by author decision of 2026-08-20 in structured Q&A, from the three candidates recorded in `PRIOR-PREDICTIVE-RUN-001.md` section 3.1.

### The change

Section 9 item 1 is superseded prospectively: the model emits posterior mass on `R1..R4` (plus the `R0_no_material_change` bucket) at every reported horizon, and posterior mass on `R5` **at 2075 only**, carrying the low-confidence label section 9 already attaches to that horizon.

**Ground, statable without reference to any gate:** under the committed ceiling table and growth priors, dual systemic constraint does not typically arise until the 2060s. A regime the design cannot populate at 2050 is not identified there, and reporting a posterior for it at 2050 would present a number the prior structure cannot inform. The honest contract reports R5 where the design can speak to it. This is the option that changes what is *claimed* rather than any gate, prior, or constant -- the ground on which it was selected over the two alternatives, both of which move quantities that bear on gates or falsifier-adjacent ceilings.

**Gate effect, stated openly:** PP1's R5 coverage test becomes moot at 2050 because the claim it protected is no longer made there. The gate follows the claim: PP1 now checks each regime's coverage at the earliest horizon at which the contract claims it -- `R1..R4` at 2050, `R5` at 2075. See the same-day amendment to `IDENTIFICATION.md`. R5's prior mass at 2075 is 0.207 on run 003, so this is not a vacuous relocation; had R5 also been starved at 2075, PP1 would fail there and the design would have no horizon at which to claim the regime.

### What this does not change

The five-regime partition stands. R5 remains in the regime set, remains classifiable by R009, and remains reported at 2075. Papers describing the architecture state that the 2050 horizon speaks to four regimes and why.

### Sources for Amendment 02

- model/PRIOR-PREDICTIVE-RUN-001.md, section 3.1 (internal; candidate list, R5 masses by horizon)
- model/IDENTIFICATION.md, Amendment 1 (internal; the PP1 restatement this contract change induces)

---

## Amendment 03 -- 2026-08-20 -- AI-intensity evolution process committed

**Appended, not substituted.** Selected by author decision of 2026-08-20 in structured Q&A, closing registered gap 2 of `model/ESTIMATION-SYNTHETIC-RUN-001.md`. Section 7 names the indicators measuring `AI_intensity[t]` but commits no evolution process; the prior-predictive implementation used a deterministic exponential as a scope-limited stand-in, disclosed there.

### The commitment

Per state, `log(1 + AI_intensity[i,t])` follows the same local-linear-trend state-space form as the Block E inputs -- own long-run growth, own persistence inherited from `rho_g`, own innovation stream with its own scale -- measured through the section 7 indicator block (frontier-capable compute stock under the committed boundary, decomposed robot stock, manufacturing output per unit of installed automation), each indicator entering Block M with the usual loading, bias, and noise terms.

**Ground, statable without reference to any outcome.** Two, both structural. First, the identical-functional-form commitment in section 5 exists to prevent asymmetry smuggled in through equations; a latent that drives the mechanism parameter deserves the same discipline as the latents it interacts with. Second, and decisive: `AI_intensity` feeds `sigma_top[t]` through `delta`, the parameter that carries P2. A deterministic path has zero process noise over fifty years, which would understate `delta`'s posterior width -- in the direction of overstating the mechanism evidence. The stochastic form is the conservative choice for the programme's own hypothesis, which is the direction the standing prohibitions require errors to lean.

**Declined:** the deterministic exponential (parsimonious, but anti-conservative for P2 as above, and it forces indicator disagreement into the bias terms because the latent cannot move); a shared-global-trend-plus-state-offsets form (adds a cross-state coupling no committed text motivates).

The prior-predictive harness retains its deterministic exponential for the gates already run -- their record stands as computed -- and adopts this form at the next full re-run, reported either way.

### Sources for Amendment 03

- model/ESTIMATION-SYNTHETIC-RUN-001.md (internal; registered gap 2)
- Author Q&A of 2026-08-20 (structured; recommended option adopted)

### Follow-up note to Amendment 03 -- 2026-08-22 -- adoption details: cross-state pooling and the absence of an AI ceiling

Two readings had to be fixed at adoption, both flagged for author override; neither touches any published quantity.

1. **Cross-state pooling.** Amendment 03 commits one AI-intensity latent per state; section 6.3 commits one `sigma_top[t]` shared by both states. The adopted reading: the increments of the **cross-state mean of `log(1 + AI_intensity[i,t])`** drive the `sigma_top` transition through `delta`. Ground: `sigma_top` is a property of the shared technology, so the identical-functional-form commitment in section 5 forbids a per-state `sigma_top`; the mean is the only simple pooling that is exactly swap-invariant, which PP4 requires structurally (max fails differentiability at crossings; sum double-counts a global level).
2. **No saturation term.** The Block E inputs carry `kappa`, `phi`, `xbar` saturation; the AI-intensity latent carries none. No ceiling was ever committed for AI intensity, and inventing an `xbar_ai` would introduce a new judgement parameter with no committed source. The latent is a local linear trend without drag.

Both readings are adopted as readings of the 6.3-vs-7 ambiguity, not new commitments; the author may override either, and an override before first real estimation changes nothing already published.

### Gate re-run under Amendment 03 -- 2026-08-22 -- run 005: PASS

Amendment 03 committed that the prior-predictive harness adopts the stochastic AI form at the next full re-run, reported either way. Run 005 (n=400, seed 20260819, `model/prior-predictive-run-005.txt`): **all five gates pass.**

- **PP3 is verbatim identical to run 004** (max 2050 multiple 29.3x at US/D1; 0.2% breach rate). This was pre-committed as a strict regression check: AI intensity feeds `sigma_top`, never the x-paths, so any PP3 movement would have been a wiring bug. Strictness is achieved by drawing all AI-related variates from a spawned child generator so pre-existing draws keep their run-004 stream positions; the superseded scalar's stream slot is consumed and discarded (see `sample_prior`).
- PP4: exact mirror on all 400 paired draws, aggregate deviation 0.0000 -- the AI stream and `gstar_ai` are swapped in `Shocks.mirrored()` and `mirror_draw`, and the cross-state-mean coupling is swap-invariant by construction.
- PP1/PP2/PP5 masses moved within noise of run 004 (e.g. R4@2050 0.0775 vs 0.07; R1@2050 0.4175 vs 0.42), as expected from `sigma_top` dynamics gaining process noise; all margins clear.

### Corrective note to Amendment 01.2 -- 2026-08-22 -- F2/F3 labels; ceiling values frozen; shadow ceiling considered and declined

**Author decision of 2026-08-22, closing HANDOVER section 18 Decision A** (three-model council review -- Grok 4.6, Gemini 3.7, Kimi K3 -- with author-adopted recommendations; unanimous on the resolution).

The Amendment 01.2 ceiling table labels F2 "R&D intensity" and F3 "advanced manufacturing". These labels are **drift**, not a competing registration. Two registered artefacts establish this: section 5 fixes the roster in `README.md`, whose frontier bundle is "frontier-capable compute, capital depth, human capital"; and `model/PRIORS.md` section 1.1 -- a committed prior -- already reasons from the README roster, centring `sigma_F` at 0.7 "because the frontier bundle contains capital depth and human capital" and reaching for the capital-labour elasticity literature, not anything about R&D intensity. The 01.2 labels are contradicted by the fixing document and by a second registered artefact; they are corrected by this dated note and the original text stands unedited above.

**The ceiling VALUES (F2 6.0, F3 3.0) are frozen.** Consequence recorded as a known weakness rather than repaired: the 01.2 ordering rationale ("R&D intensity as a share of output the least [headroom]") reasons about measurands that are not the committed ones, so the F2/F3 ordering carries a rationale that does not apply to capital depth and human capital. The values stay because any re-derivation "for the right measurand" is the prohibited move in both directions: lowering ceilings is the PP1 remedy this file names as declined, and 01.2's own closing paragraph requires gate-independent grounds for any change. A rationale defect is not a gate-independent ground for a value change; it is a rationale defect, and it is now on the record as one. Sensitivity run S6 (0.7x and 1.5x on all ceilings) continues to bracket the judgement.

**Shadow ceiling: considered and declined, ground stated.** The council split on whether to compute the ceiling a correct-measurand rationale would produce and publish it unadopted under the shadow mechanism of `falsifiers/PRE-REGISTRATION.md` Amendment 1. Declined, two-to-one reasoning adopted: the shadow rule exists for *registered candidate rules* whose need was demonstrated by a dry run surfacing a verdict-determining gap (the F5-B precedent); no such demonstration exists here, no candidate rationale is registered, and manufacturing a shadow ceiling would create a number whose only function is to make the frozen value look wrong -- an invitation to exactly the gate-adjacent move this note refuses. The declining is recorded so that it is itself auditable.
