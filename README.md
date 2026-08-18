# Segmented Bipolarity

**Does the AI-robotics transition change the production function of geopolitical capability?**

A research programme on the relative techno-industrial trajectories of the United States and the People's Republic of China, 2026-2075. This repository holds the papers, the consolidated long-form essay, the estimation code, and the pre-registered falsification record that governs all of them.

The repository is public by design. Third-party auditability is the pre-registration mechanism: the thresholds in `falsifiers/PRE-REGISTRATION.md` were committed before the estimation code existed, and the commit history is the proof of that ordering. Any later change to a threshold appears as a diff, not as a silent revision.

---

## The research question

The programme interrogates a conditional hypothesis, not a forecast:

> Conditional on a specified set of parameter ranges holding through roughly 2050, the relative strategic position of the United States and the PRC diverges in China's favour on selected physical-capacity dimensions -- electricity generation, grid transmission, and industrial robotics deployment -- while diverging in the United States' favour on other dimensions, including frontier compute, capital-market depth, net-resource efficiency, alliance density, and reserve-currency privilege.

The net direction of overall divergence is **indeterminate a priori** and must be established empirically. The sharper testable proposition is narrower: that the dimensions on which China is gaining ground are precisely the dimensions the AI-robotics transition disproportionately rewards. That is the hypothesis to interrogate, not a conclusion to defend.

The expected headline result is **segmented bipolarity** -- capability dividing by domain rather than resolving into a single hierarchy -- which is horizon-robust in a way that any directional claim is not.

## Central empirical object

Whether the frontier bundle and the deployment bundle are complements, substitutes, or alternating bottlenecks, in a two-level nested production structure:

- **Frontier bundle**: frontier-capable compute, capital depth, human capital
- **Deployment bundle**: dispatchable-adjusted electrical energy, grid transmission capacity, deployed industrial robotics

The nesting structure is to be determined by the data rather than assumed. Substitution elasticity is treated as a time-varying state, not a constant, over a fifty-year horizon.

## Dependent variable

Capability is measured as a **vector**, never as a single scalar. Aggregate national-power indices are rejected on evidentiary grounds, not stylistic ones.

| Element | Content |
|---|---|
| `Y_throughput` (primary) | Dispatchable energy, grid delivery, robot stock and installations, manufacturing output |
| `Y_frontier` | Frontier-capable compute, semiconductor capability, advanced research output |
| `Y_net` | Net-resource efficiency after deducting production, welfare and security costs |
| `Y_fin` | Capital-market depth, fiscal headroom, reserve-currency privilege |

Any composite is reported only alongside full weighting sensitivity. Changes in relative position are decomposed by element rather than aggregated, so that the divergence pattern cannot be concealed inside a summary score.

## Horizon discipline

| Horizon | Status |
|---|---|
| 2030 | Early-warning checkpoint |
| 2040 | Headline |
| 2050 | Headline |
| 2075 | Declared outer bound, low confidence |

No claim in this programme extends confidently beyond 2075. The scope is explicitly one to two generations, not the century-plus timeframe over which cliodynamic and demographic effects are sometimes discussed.

## Audience

Primary audience is scholarly and technically expert: international political economy, security studies, AI economics, energy systems, computational social science. Success is defined as a novel, falsifiable framework that survives adversarial scrutiny.

Policy and investment implications may appear as downstream interpretations. They do **not** determine model construction, scenario weighting, or horizon selection.

## Three standing prohibitions

These apply to every artifact in this repository.

1. **No asymmetric epistemic standards.** Every American structural pathology must be paired with its Chinese analogue assessed on the same scale, and vice versa. Scrutinising one side's data while accepting the other's uncritically is itself a methodological error.
2. **No teleology.** The words *inexorable*, *inevitable*, and *proves* do not appear in output. Both states are modelled as facing severe and broadly comparable structural stress; neither is modelled as institutionally healthy.
3. **No unengaged opponents.** The strongest counter-positions must appear wherever the corresponding supporting claim is made -- in particular the peaking-power thesis, net-resource critiques of gross-output measures, the critical literature on Chinese political meritocracy, conservative estimates of AI's macroeconomic effect, and the multilateral findings on AI and wage inequality.

A pillar that cannot survive contact with its own steel-man is downgraded rather than retained by assertion.

## Modelling commitments

- Identical functional form for both states. All asymmetry enters through country-specific **estimated parameters**, never through country-specific equation structure.
- Stabilisation-capacity coefficients may take negative values, representing maladaptive stabilisation. The sign for either country is estimated, not assumed.
- Energy enters as dispatchable-adjusted output using published capacity factors, never as nameplate capacity.
- Frontier compute is a wholly separate variable with its own trajectory, never folded into an undifferentiated scale term.
- Fiscal stress uses augmented debt measures for China and published projections with error bands for the United States.
- Inequality inputs are carried as ranges spanning competing measurement approaches, not point estimates.
- Labour-automation interaction terms incorporate the micro-level immiseration evidence explicitly rather than assuming frictionless substitution.
- Required output is a **probability distribution over divergence outcomes**, explicitly including the parameter regions in which the thesis is false, including US-favourable divergence.
- Prior-versus-posterior contraction diagnostics are mandatory, to demonstrate that posteriors learn from data rather than encode priors.

## Repository layout

```
papers/
  paper-a-measurement/    Capability vector, rejection of scalar indices,
                          Bayesian measurement model
  paper-b-application/    Estimation, complementarity test, peaking-power
                          thesis nested as a parameter region
essay/                    Consolidated long-form essay for expert circulation
model/                    State-space specification and diagnostics
pipeline/                 F1-F8 ingestion adapters, normalisation,
                          threshold evaluation, adjudication
data/
  raw/                    Append-only. Never edited in place.
  normalised/             Schema-conformed, provenance-tagged
  derived/                Dispatchable adjustment, rolling averages, ratios
  adjudicated/            Human-reviewed compound and qualitative conditions
falsifiers/               Pre-registration and the annual log
snapshots/                Immutable tagged states per published artifact
```

## Status

| Component | State |
|---|---|
| Pre-registration of F1-F8 | Committed |
| Data-integrity protocol | Committed |
| Audience and horizon mandate | Settled |
| Ingestion adapters (F1, F3, F7, F8) | Specification pending |
| Adjudication rules (F2, F4, F6) | Open |
| Measurement model | Not started |
| Estimation | Not started |
| Papers and essay | Not started |

## Governing principle

Defensibility comes from stating clearly what observation would prove the thesis wrong, and then being able to show, honestly, that it has not happened yet.
