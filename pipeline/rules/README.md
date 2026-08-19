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
| **R003** | Nameplate to dispatchable via published capacity factors | `Y_throughput` series | Not yet specified |
| **R004** | Precision normalisation to declared dense basis | F8 | Specified in `definitions/precision-basis.md` |
| **R005** | Frontier-capable filter, rolling factor of eight | F8 | Specified in `definitions/frontier-compute.md` |
| **R006** | Robot-density decomposition into stock and employment terms | F7 | Specified in `adapters/F7.md` |

Rules R001, R002, R004, R005 and R006 have their substance committed in the files named above. This registry records their identifiers, versions and dependency edges; it does not restate them, because a rule stated twice is a rule that can diverge from itself.

R003 is the notable gap. The dispatchable conversion is mandated by `DATA-INTEGRITY.md` for every series feeding the capability vector, and it has no committed rule. It is not required by any falsifier adapter -- F1 is explicitly exempt -- so it blocks the model rather than the dashboard.

---

## Prohibitions

- No derived figure without a registered rule.
- No silent re-derivation of published figures under a new rule version.
- No non-deterministic rule.
- No rule whose parameters are sourced but unversioned.
