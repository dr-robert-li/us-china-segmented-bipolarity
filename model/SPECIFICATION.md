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
