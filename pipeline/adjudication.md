# Adjudication framework

Governs every clause that cannot be evaluated by arithmetic alone: the qualitative halves of Type B compound conditions, all of Type C, and the sustained-condition semantics that F7 and F6 depend on.

Committed before the adapters that consume it.

---

## What adjudication means here, stated plainly

This is a single-author research programme. "Adjudication" therefore does not mean a panel, a committee, or an independent referee. It means a **written, dated, source-cited determination that a third party can contest on the record**.

That is a weaker guarantee than institutional review and the framework should not pretend otherwise. Its strength comes from three properties rather than from independence:

1. The determination is written **before** its consequences are known to be favourable or unfavourable, because the trigger rules were fixed in advance.
2. The reasoning is public, so a reader who disagrees can identify precisely where.
3. The evidentiary standard is symmetric between triggering and non-triggering, which removes the most obvious channel for motivated reasoning.

Where an adjudication is genuinely contestable, that fact is recorded in the determination rather than resolved by assertion.

---

## The asymmetry hazard

An analyst with a thesis to defend has an obvious incentive to set a high evidentiary bar for `met` and a low one for `not_met`. Qualitative clauses are where that incentive can operate undetected, because there is no series to check the reasoning against.

Three rules close it.

### Rule 1 -- Symmetric bar

The evidentiary standard for `met` and for `not_met` is identical. Both require affirmative evidence. "Insufficient evidence that the condition occurred" yields `indeterminate`, **not** `not_met`.

This distinction does real work. Under the trigger rules, `not_met` protects the thesis while `indeterminate` does not — an indeterminate qualitative clause on a Type B condition blocks a clean verdict and must be carried forward as unresolved.

### Rule 2 -- Adverse-interest requirement

Before writing the determination, the adjudicator writes the **strongest available case that the clause is met**, with named sources, as though arguing for it. That case is published as part of the adjudication record whether or not the determination follows it.

This mirrors the standing prohibition on unengaged opponents, applied to the analyst's own verdicts rather than to the literature.

### Rule 3 -- Indeterminate must be earned

`indeterminate` is not a default. A determination of `indeterminate` must state what specific evidence would resolve it and whether that evidence could plausibly become available. An `indeterminate` that cannot name its own resolution condition is a failure to adjudicate, not an adjudication.

---

## Evidence standards

| Requirement | Rule |
|---|---|
| Minimum sources | Three independent, for any determination other than `indeterminate` |
| Contemporaneity | Sources dated within the evaluation window, or explicitly retrospective and flagged as such |
| Contrary sources | At least one source arguing against the determination must be cited where any exists |
| Source standing | Peer-reviewed, multilateral-institution, or primary official sources preferred over commentary; standing recorded per source |
| Official PRC or US statements | Admissible as evidence of a position, never as evidence of a fact |
| Anonymous or single-outlet reporting | Insufficient alone for `met` on any clause |

The last two matter for F5 and for F3's cascade clause specifically, where much of the available reporting is of exactly the kind these rules discount.

---

## Adjudication record

```yaml
adjudication:
  adjudication_id: string
  falsifier_id: string        # F3, F5, F7 ...
  clause: string              # which clause of a compound condition
  evaluation_year: integer
  determination: enum         # met | not_met | indeterminate
  adverse_case: string        # REQUIRED. The strongest case for `met`.
  reasoning: string
  sources: [object]           # citation, date, standing, supports_or_opposes
  resolution_condition: string|null  # REQUIRED where determination is indeterminate
  contestable: boolean
  contestable_note: string|null
  authored_by: string
  authored_at: timestamp
  dissent: [object]           # third-party challenges received, with responses
  amendments: [object]        # appended only; never overwrites
```

`adverse_case` may not be empty. A record submitted with an empty `adverse_case` fails validation, in the same way a series descriptor with an empty `definitional_boundary` does.

---

## Sustained-condition semantics

Three pre-registered conditions require a state to persist: F6 over five consecutive years, and F7 over five consecutive years on **both** of its clauses. The semantics below are fixed here so that no discretion enters at evaluation time.

### Recompute, never increment

The run length is **recomputed from scratch at every evaluation**, from the full history of per-year qualification. It is never stored as a counter and incremented.

This is the single most important rule in this section. A stateful counter cannot be corrected when an upstream revision changes a prior year's qualification; a recomputed run can, and does so automatically.

### Per-year qualification

Each year independently qualifies or does not. For conjunctive clauses of the form "X despite Y" -- F7's structure -- **both** sub-conditions must hold within the **same** year for that year to qualify. A year in which TFP growth is negative but robot-density growth has stalled does not qualify, because the condition tests failure of automation to offset, not failure in general.

### Gaps suspend, they do not break

A year with no admissible observation is `indeterminate` for that year. Its effect:

- The run does not advance.
- The run is **not** reset.
- The overall condition verdict becomes `indeterminate` if and only if the gap year is load-bearing, meaning the condition would trigger were the gap year to qualify.

Treating gaps as breaks would let a data outage protect the thesis. Treating gaps as qualifying years would let an outage refute it. Suspension is the only treatment that does neither.

### Revisions can break a run retroactively

If an upstream revision causes a prior year to stop qualifying, the run breaks at that year and the current verdict is recomputed. The prior published verdict is amended, not overwritten, per the annual-log rules.

Runs can therefore shorten as well as lengthen. An adapter that cannot produce a shorter run than it reported last year is implemented incorrectly.

### Consecutiveness spans the deadline

A run that would complete after the pre-registered deadline does not trigger. F7's five-year requirement with a 2040 deadline means the latest qualifying window is 2036 through 2040. A run beginning in 2037 cannot trigger F7 regardless of what follows, and this is a consequence of the pre-registration rather than a defect to be patched.

---

## Compound-condition assembly

For Type B conditions the two clauses are evaluated and recorded separately, then combined:

| Quantitative | Qualitative | Verdict |
|---|---|---|
| met | met | `triggered` |
| met | not_met | `not_triggered` |
| met | indeterminate | `indeterminate` |
| not_met | any | `not_triggered` |
| indeterminate | met | `indeterminate` |
| indeterminate | not_met | `not_triggered` |
| indeterminate | indeterminate | `indeterminate` |

A quantitative `not_met` short-circuits, because the condition is conjunctive and no qualitative finding can rescue it. Nothing else short-circuits.

---

## Timing and freezing

- Adjudications are dated at authoring and published in the annual log for their evaluation year.
- Once published, an adjudication is frozen. Changes are appended as amendments carrying their own date and reasoning.
- An adjudication may not be authored retrospectively for a year whose log has already been published, except as an amendment.
- Where a determination changes on amendment, both the original and the amended determination remain visible.

---

## Prohibitions

- No determination without a written `adverse_case`.
- No `not_met` on absence of evidence alone.
- No `indeterminate` without a stated resolution condition.
- No stateful run counters.
- No adjudication of a quantitative clause. If a clause can be computed, it is computed.
- No substitution of a more favourable source set after a determination has been drafted.

The last prohibition is the hardest to enforce technically and is recorded here so that a reader can at least ask whether it was observed.

---

## Amendment 1 -- 2026-08-20 -- the silent-procedure branch

**Appended, not substituted. Stated first, because it is the only thing that makes this amendment admissible: this change is inert for every live 2026 determination.** The constitutional documents in force in 2026 contain an express removal provision -- Article 42 of the Party Constitution as revised 22 October 2022, quoted below -- and the 2026 removals followed its published route, so no live clause routes through the branch this amendment adds. The change is made while it decides nothing.

### The defect

Clauses of the form "departure from the procedures set out in the documents in force at the time" -- F5 Sub-clause A is the instance in the set -- presuppose that a governing procedure exists. The dry run at `../falsifiers/adjudications/dry-run/2012.md` found the presupposition can fail: the 1973 Party Constitution contained **no** provision governing removal of a Politburo member -- no quorum, no majority requirement, no ratification route. "Departure from procedure" is not *false* in that situation. It is **undefined**, and the rubric as written did not distinguish the two.

Routing the silent case to `not_met` would let a constitution's silence protect the thesis, which is exactly the asymmetry Rule 1 exists to close: `not_met` requires affirmative evidence, and the absence of a procedure is not affirmative evidence that procedure was followed.

### The rule, committed

Where a clause tests departure from a procedure, adjudication first determines whether the documents in force at the time contain a procedure governing the event class at issue:

| Finding | Routing |
|---|---|
| Procedure exists and was followed | `not_met` |
| Procedure exists and was departed from | `met` (subject to the clause's other requirements) |
| **No procedure governs the event class** | **`indeterminate`**, per Rule 1 |

The `procedure_absent` routing is `indeterminate`, not `not_met`. Its resolution condition, required by Rule 3, is: identification of a document in force at the time that does govern the event class, or a determination on some other limb of the same condition that does not depend on procedural departure.

The finding of absence must itself meet the affirmative-evidence bar: silence is established by examination of the full document in force, cited, not by failure to locate a provision.

### Application to the current documents

For the event class "removal of a member or alternate member of the Central Committee" the document in force since 22 October 2022 is not silent. Article 42 of the Party Constitution provides that any such removal, disciplinary probation, or expulsion "must be approved by a two-thirds majority vote at a plenary meeting of the Party committee to which the member or alternate member belongs", with a provision for the Political Bureau to decide first "while awaiting confirmation at the plenary meeting" when the plenary is not in session ([Full text of Constitution of Communist Party of China, revised 22 October 2022, China Military Online](http://eng.chinamil.com.cn/CHINA_209163/TopStories_209189/10195159.html); snapshot `sha256:a4c640bf1de4d0958fb8193e7405dd294ee3bd1fdac0fbdae3af2e706d13e95c`, recorded in `../research/snapshots/INDEX.md`).

**A numbering correction is recorded here so it does not propagate.** The equivalent provision was Article 40 in the 2007 and 2012 texts, and internal working notes have referred to "Article 40 of the 2022 constitution". In the 2022 revision Article 40 is the general discipline article; the removal provision is **Article 42**. The provision's existence, which is what the inertness statement above rests on, is unaffected.

### Sources for Amendment 1

- http://eng.chinamil.com.cn/CHINA_209163/TopStories_209189/10195159.html (snapshot sha256 a4c640bf1de4d0958fb8193e7405dd294ee3bd1fdac0fbdae3af2e706d13e95c)
- https://www.marxists.org/subject/china/documents/cpc/CONSTITUTION_CPC.htm (1973 text, silence on removal; as cited in the 2012 dry run)
- http://www.china.org.cn/english/congress/229722.htm (2007 text, Article 40; as cited in the 2012 dry run)
- falsifiers/adjudications/dry-run/2012.md (internal; the open specification question this amendment resolves)

---

## Amendment 2 -- 2026-08-20 -- denominators from enumerated name lists

**Appended, not substituted. Inert for every live 2026 determination:** the 2026 F5 denominator of 24 was already established from an enumerated membership list corroborated by a third-party tabulation, and this amendment confirms that number rather than changing it. `ceil(0.15 * 24) = 4` before and after.

### The recurring failure

An official aggregate figure that admits an additive reading has now produced the same ambiguity three times:

1. **1973.** The State Council record's phrasing -- "9 Politburo Standing Committee members, 21 Politburo members, and 4 alternate members" -- admits a reading of 34. Only the enumerated 21-name list in the contemporaneous communiqué establishes that the 9 sit inside the 21. See `../falsifiers/adjudications/dry-run/1976.md`.
2. **2007.** Whether the 17th Politburo had alternates is not establishable from the aggregate record; the enumerated official name list settles the full-member count at 25. See `../falsifiers/adjudications/dry-run/2012.md`.
3. **2022.** The primary Party source states a count of 24 alongside a separate list of 7 Standing Committee members without stating whether the 7 are inside the 24. See Amendment 1 to `../falsifiers/adjudications/2026/F5-B.md`.

A threshold computed from a misread aggregate can be wrong by a factor that changes the threshold, in either direction, in either year.

### The rule, committed

Wherever a clause's arithmetic takes the membership of a named body as a denominator:

- The denominator is established from an **enumerated name list** in a primary source.
- Official aggregate figures **corroborate the total only**. An aggregate may never alone establish a denominator, and where an aggregate conflicts with an enumerated list, the list governs and the conflict is recorded.
- Where no enumerated list is obtainable, the denominator is not established and the clause's arithmetic returns `indeterminate` for want of it, per Rule 1.

### Sources for Amendment 2

- https://www.gov.cn/test/2007-08/28/content_729620.htm (the 1973 aggregate admitting an additive reading; as cited in the 1976 dry run)
- https://www.marxists.org/subject/china/china-reconstructs/1973/CR1973-11-Sup.pdf (the enumerated 21-name list resolving it)
- http://www.china.org.cn/english/congress/229262.htm (the 2007 enumerated name list)
- https://www.idcpc.org.cn/english2023/tjzl/cpcjj/leadershipof20thCentralCommittee/ (the 2022 primary source with the inside-or-outside ambiguity)
- falsifiers/adjudications/2026/F5-B.md, Amendment 1 (internal)
