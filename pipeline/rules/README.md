# Transformation rules registry

`pipeline/schema.md` requires every derived observation to carry a `rule_id` and a semantic `rule_version`. This directory holds those rules. Its absence was a dangling reference in a committed specification.

A derived figure whose governing rule is not registered here is **not publishable**.

---

## Registry format

Each rule is a file `R<nnn>-<slug>.md` containing:

```yaml
rule:
  rule_id: string           # R001, R002, ...
  version: string           # semver
  name: string
  applies_to: [string]       # series_ids or falsifier_ids
  inputs: [string]
  output: string
  parameters: object         # with vintage where a parameter is itself sourced
  determinism: boolean       # must be true
  supersedes: string|null
```

The body states the transformation in prose, the reasoning for any judgement embedded in it, and the tests that establish it behaves as described.

---

## Versioning policy

- **Patch** -- documentation or test changes with no behavioural effect.
- **Minor** -- behavioural change that cannot alter any published verdict.
- **Major** -- behavioural change that could alter a published verdict.

A major bump requires the affected verdicts to be recomputed under both the old and new versions, with both published and the difference stated. Silently re-deriving published figures under a new rule version is prohibited.

Rule versions are frozen for a condition once that condition has crossed its threshold, mirroring the freeze rules in `falsifiers/dependence.md`.

---

## Initial rules

| ID | Name | Applies to | Status |
|---|---|---|---|
| **R001** | Net additions by differencing year-end totals | F1 | Specified in `adapters/F1.md` |
| **R002** | Ratio of three-year sums | F1 | Specified in `adapters/F1.md` |
| **R003** | Nameplate to dispatchable via published capacity factors | `Y_throughput` series | Specified in `rules/R003-nameplate-to-dispatchable.md`, v0.1.0 |
| **R004** | Precision normalisation to declared dense basis | F8 | Specified in `definitions/precision-basis.md` |
| **R005** | Frontier-capable filter, rolling factor of eight | F8 | Specified in `definitions/frontier-compute.md` |
| **R006** | Robot-density decomposition into stock and employment terms | F7 | Specified in `adapters/F7.md` |
| **R007** | PSI component construction and PRC operationalisation | `stress` series | Specified in `model/POLITICAL-STRESS.md` |
| **R008** | IFR robot-density break adjustment; stock term substituted across the NBS denominator revision | `D3`, F7 | Specified in `model/SPECIFICATION.md` |
| **R009** | Trajectory to regime label | model output | Specified in `rules/R009-regime-classification.md`, v0.1.0 |
| **R010** | Tracked-cluster stock construction (Construction B) | `compute_frontier_stock`, F8 | Specified in `definitions/frontier-compute.md` Amendment 1, v0.1.0 |
| **R011** | Intermediated-access bounded-enumeration band | `compute_intermediated_band`, F8 | Specified in `definitions/frontier-compute.md` Amendment 1, v0.1.0 |

Rules R001, R002, R004, R005, R006, R007 and R008 have their substance committed in the files named above. This registry records their identifiers, versions and dependency edges; it does not restate them, because a rule stated twice is a rule that can diverge from itself.

R010 and R011 were registered 2026-08-20 by `definitions/frontier-compute.md` Amendment 1, both at **0.1.0**: specified, but the coverage-error characterisation (R010) and the band enumeration (R011) have not yet been exercised at a first ingest, and a rule whose coverage component has never been computed is not at 1.0 merely because it is written down.

R008 was registered on discovering that the IFR China robot-density series is not comparable across the World Robotics 2024 and 2025 vintages, following a National Bureau of Statistics revision to the manufacturing-employment denominator. Reported density falls from 470 to 166 per 10,000 while absolute stock rises past two million units. The rule substitutes the stock term for the density ratio across the break.

R003 was the notable gap and is now specified, at version **0.1.0** rather than 1.0.0. It sits below 1.0 because two of its open items bear on the numbers it produces rather than only on its documentation: the PRC technology partition is coarser than the US partition and the reconciliation choice moves US `D1`, and the treatment of storage is undecided. A rule whose partition choice can move a headline input is not at 1.0 merely because it runs.

R009 was registered during Phase 3, by amendment to `model/SPECIFICATION.md`. It is the classifier that maps a simulated trajectory to a regime label, and it exists as a registered rule rather than as model internals because two prior-predictive gates turned on its behaviour: PP2 failed at run 001 because the classifier made the thesis regime a sink, and PP1 currently fails on a branch governed by one of its constants. A parameter that can determine whether a gate passes belongs in the registry.

Both are at 0.1.0 and both have sourced or judgement-bearing parameters, which is why each has a standalone file. R001, R002 and R004 to R008 have their substance committed in the files named in the table.

---

## Prohibitions

- No derived figure without a registered rule.
- No silent re-derivation of published figures under a new rule version.
- No non-deterministic rule.
- No rule whose parameters are sourced but unversioned.
