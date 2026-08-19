# Handover

> **State update appended 2026-08-20 -- see the final section.** Priorities 2, 3 and 4 are closed, the snapshot rule is in force with tooling, the n_eff caveat is written into `dependence.md`, and the first Priority 1 dry run (F1) is on file and passed. Section 5's list below is retained as written; the final section records what changed.

**State as at commit `93af2b7`, 20 August 2026.** Written so the project can be continued by someone else, or by the same author in a different working environment, without reconstructing context from conversation history.

Read `README.md` first for what the project is. This file covers what state it is in, what is blocked and why, what must not be changed, and what to do next.

---

## 1. What exists

Six phases are committed. Each was one commit.

| Commit | Phase | What landed |
|---|---|---|
| `93af2b7` | 6 | Dry-run adjudications (1976, 2012); citation and language audit; F5-B false-negative mode registered |
| `417cddf` | 5 | The two self-compliance breaches closed: F5 sub-clause adjudications and the F2 Clause 2 adverse case |
| `5043ab6` | 4 | Paper A and B outlines, essay outline, Paper A section 3 drafted |
| `2d87dff` | 3 | Pipeline implementation, rules R003 and R009, prior-predictive gates run |
| `a7eb4a4` | 2 | Model specification, political stress, priors, identification |
| `79846b0` | 1 | Rules registry, precision basis, 2026 baseline falsifier log |
| `3e7047e`, `0e172e3`, `6c3550b` | -- | Adjudication framework, compute boundary, initial structure |

Tests: 37 passing. Run them with

```
cd pipeline && PYTHONPATH=src python3 -m unittest discover -s tests -t .
```

There is no `pytest` in the environment used to date. Dependencies observed: Python 3.14, numpy 2.5.2, scipy 1.18.0.

---

## 2. The invariants -- read before changing anything

These are the rules that make the project's claim work. A continuation that breaks one of them has produced a different project with the same file names.

1. **Thresholds and counting rules do not move as they are approached.** Not in either direction. A change that makes the project's own thesis easier to support is not more acceptable than one that makes it harder -- if anything less, because the incentive to make it is stronger and the supporting reasoning will feel more compelling to the person making it. This is the rule F5-B is currently being held to at a cost. See section 4.

2. **Amendments append. They never overwrite.** Every correction so far is an appended `## Amendment N` block with a date and a statement of what changed and what did not. The superseded text stays visible. `falsifiers/adjudications/2026/F5-A.md` is the pattern to copy: the original limitation paragraph is left standing, with the narrowing appended below and a pointer inserted.

3. **Corrections are recorded, not repaired.** Where the project failed to comply with its own rules, the failure is written down as a failure. `falsifiers/adjudications/CITATION-AUDIT-2026-08-19.md` records that the audit itself under-reported on its first pass.

4. **No favourable source substitution, no deadline extension, no reclassification to dodge a verdict.**

5. **Three standing prohibitions on all output.** No asymmetric epistemic standards -- the bar for evidence supporting the thesis is the bar for evidence against it. No teleology -- the words *inexorable*, *inevitable* and *proves* do not appear as claims about the thesis; the five retained `prove`-family matches and the reasoning for each are in the citation audit. No unengaged opponents -- a steel-manned counter-position appears wherever the supporting claim is made, and it is written *before* the reasoning that answers it, not after.

6. **Adjudication Rule 1, the symmetric bar.** "Insufficient evidence that the condition occurred" is `indeterminate`, never `not_met`. `not_met` requires affirmative evidence. This matters because `not_met` protects the thesis and `indeterminate` does not.

7. **Adjudication Rule 2, adverse interest.** The strongest case for the opposite of the determination is written first and published regardless of where the reasoning lands.

8. **Official PRC and US statements are evidence of a position, never of a fact.**

9. **The Gate 2 posterior threshold of 0.25 and the `n_eff` threshold of 1.8 in `falsifiers/dependence.md` are frozen and may not be changed at all.**

10. **The repository is public by design.** Third-party auditability is the pre-registration mechanism. Do not make it private, and do not rewrite history.

---

## 3. Current position

No threshold crossings. `n_eff` is zero. No gate has fired.

| ID | Verdict | Distance | Note |
|---|---|---|---|
| F1 | `not_triggered` | ~30pp | Moved away |
| F2 | `not_triggered` | ~0.1pp | Current-year estimate, not elapsed outturn |
| F3 | `not_triggered` | ~39pp | Revised vintage |
| F4 | `indeterminate` | -- | The source series does not exist |
| F5 | `not_triggered` | 1-2 Politburo members | Flagged `known_false_negative_mode` |
| F6 | `not_triggered` | ~12pp | Moved away |
| F7 | `indeterminate` | -- | PRC manufacturing TFP series not continuously available |
| F8 | `indeterminate` | ~1.1pp below | Estimated compute |

**The set is not well calibrated and the papers must say so.** The two conditions nearest their thresholds -- F2 and F8 -- are also the two whose measurement is least direct. F5 is one to two members away on a condition with no series at all. More of the architecture's weight rests on definitional choices than the threshold table suggests.

---

## 4. Three live blockers

### 4.1 Estimation is blocked by two failing prior-predictive gates

Canonical run 003, n=400, seed 20260819: **PP1 FAIL, PP2 PASS, PP3 FAIL, PP4 PASS, PP5 PASS.** Full diagnosis in `model/PRIOR-PREDICTIVE-RUN-001.md`.

- **PP1** fails on R5 only, at 0.000 mass against a 0.05 floor. Dual systemic constraint does not typically arise until the 2060s under the committed ceiling table, and the gate evaluates at 2050. Three candidate readings are recorded; **none has been chosen.**
- **PP3** fails on trajectory sanity. The tail reaches 1,598x against a pre-registered 20x ceiling. Widening the ceiling was rejected in advance.

**No prior has been adjusted to make a gate pass, and none may be.** The specification commits to reporting failures rather than tuning. Remedies must be selected on grounds statable without reference to the gate outcome, and the selection must be a dated amendment.

Read the note in that file about run 002: a plausible, quantitative, well-formed diagnosis of a structural model limitation turned out to be a sampler typo. The prior predictive did not catch it; an audit of the sampler against `PRIORS.md` did. Treat any elegant diagnosis with suspicion until the code is read.

**Paper B drafting is held behind this.** Do not start it.

### 4.2 F5 Sub-clause B has a demonstrated false-negative mode

The dry runs in `falsifiers/adjudications/dry-run/` paired an expected-positive episode with a negative control and named the failure conditions before computing.

| Sub-clause | 1976 | 2012 | Discriminates? |
|---|---|---|---|
| A | `met` | `not_met` | Yes |
| B | **`not_met`** | `not_met` | **No** |
| C | `met` | `not_met` | Yes |

The anchoring rule counts from the first official announcement of expulsion. That date is **anti-correlated** with the irregularity the clause measures: orderly removals are announced promptly and count, irregular ones are announced late and do not. The clause is least sensitive to exactly the events it exists to detect.

The better rule -- effective loss of office -- is registered as `F5-B-ANCHOR-2` in `pipeline/adapters/F5.md`, Amendment 3, **not in force, earliest effect evaluation year 2027**. It is not adopted because it would take the live 2026 numerator from 2 to 3 against a threshold of 4. Invariant 1 governs.

**Do not adopt it early. Do not retire the clause.** Deleting a clause known to be insensitive also deletes the record of the failure, which is the most valuable output of Phase 6.

### 4.3 R003 sits at v0.1.0 and its partition choice can move a headline input

`pipeline/rules/R003-nameplate-to-dispatchable.md`. Two open items bear on the numbers rather than the documentation: the PRC technology partition is coarser than the US partition and the reconciliation choice moves US `D1`, and the treatment of storage is undecided. F1 is exempt, so this blocks the model rather than the dashboard.

---

## 5. What to do next, and why in this order

The naive order -- work on the conditions nearest their thresholds -- is **inverted** by invariant 1. The closer a clause is to firing, the less you are permitted to change it. So the fix window closes as urgency rises.

### Priority 1 -- dry-run the distant conditions while their fix window is still open

F3 (~39pp), F6 (~12pp), F1 (~30pp), F4 and F7. One clause of eight has been discrimination-tested and it failed; the other seven are untested, not passed. Each needs the paired design in `falsifiers/adjudications/dry-run/README.md`: an expected-positive episode, a negative control, failure conditions named before computing.

**Do F2 and F8 as well, but expect that any defect found cannot be fixed.** At 0.1pp and 1.1pp their fix windows are arguably already shut. A defect found there gets carried as a flag plus a published shadow value, and that asymmetry belongs in the papers rather than in a referee report.

### Priority 2 -- the fixes that are provably inert for 2026

These do not touch a live number, so invariant 1 does not bite. All three were identified by the dry runs.

1. **The silent-constitution branch.** The 1973 Party Constitution contained no removal provision. "Departure from procedure" is not false when no procedure exists -- it is undefined, and Rule 1 makes that `indeterminate`. Add a `procedure_absent` branch to Sub-clause A routing in `pipeline/adjudication.md`. Inert because Article 40 of the 2022 constitution exists and was followed. Recorded as an open specification question in `dry-run/2012.md`.
2. **The denominator source rule.** An official aggregate capable of an additive reading, resolvable only by an enumerated name list, has now caused the same failure three times -- 1976, 2007, 2022. Generalise: denominators come from enumerated name lists; aggregates corroborate the total only. Inert, because it confirms the 21 and 24 already in use.
3. **The death-vacancy rate.** Five of 21 seats fell vacant by death in the 1976 window -- 24 percent, above the threshold alone. Excluding deaths is correct but its magnitude is invisible. Report the rate alongside every Sub-clause B verdict. Adds a published quantity without touching the numerator.

### Priority 3 -- the shadow-publication rule

The prohibition in invariant 1 binds the **determination**, not publication. Nothing prevents computing `F5-B-ANCHOR-2` each year and publishing both values side by side with the binding one labelled. Make it a standing rule: any clause carrying a registered candidate rule publishes the shadow value.

This preserves pre-registration exactly while removing the false negative's power to mislead. Concealing the second number is what would make the flag cosmetic.

### Priority 4 -- add discrimination testing to the pre-registration, prospectively

No clause reported as a determination without paired dry runs on file. F5-B failed because it was pre-registered without ever being exercised against a case with a known answer. Applies to 2027 onward and to any new falsifier; it cannot be applied retrospectively to the 2026 determinations without invalidating them, which is not the intent.

### Priority 5 -- select the PP1 and PP3 remedies

See 4.1. Requires a dated amendment with reasons statable independently of gate outcomes.

### Priority 6 -- writing

Paper A sections 1, 2 and 4 through 9 are undrafted; section 3 is committed. Essay movements 1 through 7 are undrafted. Paper B is held behind 4.1.

---

## 6. Conventions -- match these exactly

- **Plain-text arithmetic in fenced blocks or backticks. No LaTeX anywhere.**
- Markdown tables for anything comparative.
- Inline citations as `[Source name](full URL)`. Never a bare URL, never "source" or "link" as anchor text.
- Every file ends with a `## Sources` section, or `## Sources, full URLs`, listing full URLs as plain text. Amendments add their own `### Added by Amendment N` or `### Sources for Amendment N` subsection rather than editing the main list.
- Em-dashes are written as `--` in files authored from Phase 1 onward.
- Verdict vocabulary is fixed: `not_triggered`, `triggered`, `indeterminate` at the falsifier level; `not_met`, `met` at the clause level.
- Adjudications carry a YAML front block. Required keys: `adjudication_id`, `falsifier_id`, `clause`, `evaluation_year`, `determination`, `adverse_case`, `reasoning`, `sources`, `resolution_condition`, `contestable`, `contestable_note`, `authored_by`, `authored_at`, `dissent`, `amendments`.
- An `indeterminate` must name its resolution condition.
- Three independent sources minimum for anything other than `indeterminate`, and at least one contrary source wherever one exists.

---

## 7. Where the evidence is

`research/` holds the raw evidence bases -- roughly 2,750 lines across five files, several hundred fetched URLs, with gap sections recording what was sought and not found. **They are unvetted working notes, not findings**, and `research/README.md` says so in terms. Where a note conflicts with a published determination, the determination governs.

They are in the repository so that continuation does not require re-fetching everything, and so a reader can see what was gathered before it was filtered.

---

## 8. Known weaknesses -- where a referee will go first

Listed because a handover that omits them is not a handover.

1. **No page was snapshotted at fetch time.** Content drift is undetectable. Registered as a method gap and deliberately not retrofitted, since capturing snapshots now would imply verification on the original date. **Start doing this immediately for all new work** -- content-addressed, with the text hash recorded at fetch. That also solves the next item.
2. **A mechanical link check cannot distinguish a blocked host from a dead page.** Eight Reuters URLs return 401 to any automated checker, as do CBO, congress.gov, IMF, NYT, loc.gov and airuniversity. Their content is asserted on the strength of having been fetched during research. A reader without an equivalent fetch path has to take those on trust, which is a real weakness in a project whose whole claim is auditability.
3. **Single-source dependencies.** Sub-clause A's scholarly characterisation of the 2012 transition rests on Alice Miller alone, in an analytical publication rather than a peer-reviewed one. "No dissent found" is not "no dissent exists."
4. **One quotation set is read through a partisan archive mirror** and was not checked against the journal of record. Flagged in `dry-run/1976.md`.
5. **F5's disjunction has a seam.** The reduction of the Central Military Commission from seven members to two -- the most consequential civil-military event in the window -- passes through F5 without satisfying any limb. Sub-clause B by routing, where it does not reach the threshold; Sub-clause C finds it out of scope. Not repaired, because widening a clause after observing it is hard to satisfy is the move invariant 1 exists to prevent. See `falsifiers/adjudications/2026/F5-C.md`.
6. **`n_eff` assumes each falsifier is a live test.** A clause with a demonstrated false-negative mode contributes less than one, so the set's effective independence is overstated and the rejection gates are harder to fire than the arithmetic implies. The Gate 2 thresholds are frozen, so this is recorded as a caveat on the gates rather than a recomputation. **Not yet written into `falsifiers/dependence.md`.**
7. **F2's 5.9% is a current-year estimate inside a projection publication, not elapsed outturn.** Under the outturn-only rule it returns `not_met` even at 6.1%. The rule's first live application worked against the falsifier, which is the honest test of whether it was written for the right reason -- but it means F2's ~0.1pp distance is softer than it looks.

---

## 9. What is not decided

Do not assume any of these has an answer somewhere in the repository.

- The PP1 and PP3 remedies. Candidates are listed; none is chosen.
- The R003 PRC and US technology partition, and the treatment of storage.
- Whether an R009 sensitivity run is required before estimation.
- F8's method items.
- Whether F7 can proceed at all, given that the PRC manufacturing TFP series does not exist continuously.
- Whether `F5-B-ANCHOR-2` will in fact be adopted in 2027. It is registered with a condition attached: both dry runs must be re-run under it and published first, and if the negative control fires under the new anchoring the candidate is rejected and the registration closes unadopted.

---

## 10. Audience

Academic contribution and intellectual artifact. Written for peer intellectual consumption, **not** for investment decisions and not for policy planning. Tone follows from that: the methodological failures are the contribution, not an embarrassment to be minimised. Phase 6 is the clearest instance -- the finding that a pre-registered clause cannot distinguish the archetypal positive case from a negative control is more valuable than a clean set of verdicts would have been.

---

## 11. State update -- 2026-08-20

Everything above stands as written at `93af2b7`. This section records what a continuation session closed the same day, so the next continuation does not re-derive it.

### Closed

- **Priority 2 in full.** All three inert fixes landed as dated amendments with the inertness arithmetic stated first: the silent-procedure branch (`pipeline/adjudication.md` Amendment 1 -- `procedure_absent` routes to `indeterminate` under Rule 1), the enumerated-name-list denominator rule (`pipeline/adjudication.md` Amendment 2), and the death-vacancy rate (`pipeline/adapters/F5.md` Amendment 4; 1976 = 23.8%, 2012 = 0%, 2026 = 0%).
- **Priority 3.** Shadow publication is a standing rule (`falsifiers/PRE-REGISTRATION.md` Amendment 1) and the first shadow value is published (`falsifiers/log/2026/F5.md` Amendment 3): binding 2 of 4, shadow under `F5-B-ANCHOR-2` 3 of 4, both `not_met`, distance one member on the shadow.
- **Priority 4.** Paired dry runs are required prospectively from evaluation year 2027 and for any new falsifier (`falsifiers/PRE-REGISTRATION.md` Amendment 2). Not retroactive to 2026, as intended.
- **Known-weakness 6.** The n_eff caveat is now written into `falsifiers/dependence.md` as Amendment 1. Frozen thresholds untouched.
- **Known-weakness 1, prospectively.** Content-addressed snapshots are in force: `research/snapshots/snapshot.py` stores exact response bytes under `store/<sha256>` and appends to `INDEX.md`. Every URL fetched on 2026-08-20 is snapshotted, including the full Ember yearly CSV (~47 MB, deliberate -- it is F1's committed primary and the exercise is reproducible against the exact bytes).
- **Priority 1, first instalment.** F1 is dry-run tested and **passed**: `falsifiers/adjudications/dry-run/F1-2003-2024.md`, expected-positive 2003 (`triggered`, R = 2.35), negative control 2024 (`not_triggered`, R = 0.094), robust across constructions and numerator source. Score so far: one clause failed its dry run (F5-B), one passed (F1), six untested.

### Found along the way

- **F1's 5 percent source-tolerance rule has no committed comparison basis** and is breached in both dry-run windows *and in 2022--2024* by the installed-versus-net-summer definitional gap (2025 sits inside tolerance at 4.2 percent). A 2026 evaluation's three-year window contains the breaching years, so as written the rule blocks automatic verdict emission for the live window. Registered as `tolerance_basis_unspecified` (`pipeline/adapters/F1.md` Amendment 1); a basis-matched cross-check pair must be committed before first ingest. One-directional: can block a verdict, cannot flip one.
- **Negative net additions are real** (US 2015, both sources) and the adapter's semantics for a negative three-year sum are unstated. Registered as an open question, resolution required before first ingest.
- **Ember publishes no total-capacity row**; `cap_total_installed` must be derived by summing fuel-level rows. Summation rule to be committed at first ingest.
- **A numbering correction:** the removal provision cited in this file's section 5 as "Article 40 of the 2022 constitution" is **Article 42** in the 2022 revision (Article 40 is now the general discipline article). The provision exists and was followed, so the inertness argument is unaffected. Recorded in `pipeline/adjudication.md` Amendment 1, with the 2022 text snapshotted.

### What to do next

**Superseded by section 12 below, same day: item 2 is closed (remedies selected, gates pass), item 1's F3 episode problem is closed (pair registered), and the committed dry-run order is in section 12.** Retained as written for the record.

Unchanged in structure from section 5, minus what closed:

1. **Continue Priority 1**: dry runs for F3, F6, F4, F7, then F2 and F8 (expecting that defects found at F2/F8 can only be flagged, not fixed). F6 is the natural next candidate -- long public series, sustained-condition semantics worth exercising against `pipeline/adjudication.md`'s recompute-never-increment rules. F3's expected-positive episode choice is itself an open problem; do not start there.
2. **Priority 5** (PP1/PP3 remedy selection) still requires an authored decision; candidates listed in `model/PRIOR-PREDICTIVE-RUN-001.md`, none chosen. Paper B stays blocked behind it.
3. **Priority 6** writing, unchanged.
4. Before F1 first ingest: commit the basis-matched cross-check pair, the negative-sum semantics, and the fuel-row summation rule (all registered in `pipeline/adapters/F1.md` Amendment 1).

---

## 12. State update -- 2026-08-20, second session block: all open decisions resolved by Q&A; estimation unblocked

Author Q&A of 2026-08-20 resolved every open decision in section 9. Each selection is a dated amendment carrying its gate-independent ground.

### Decisions and where they landed

| Decision | Selection | Amendment |
|---|---|---|
| PP1 remedy | Candidate 3: R5 reported at 2075 only; gate follows claim | `SPECIFICATION.md` A02, `IDENTIFICATION.md` A1 |
| PP3 remedy | Candidate 1: `sigma_v ~ HalfNormal(s_v)`, procedure committed before computation; `s_v = 0.0191` | `PRIORS.md` A1 |
| R003 gas partition | Coarse common partition, generation-weighted; fine US factors as sensitivity | R003 A1, v0.2.0 |
| R003 storage | Excluded from D1; `cap_storage_installed` series; pumped storage stripped from PRC hydro | R003 A1 |
| R009 sensitivity | Run before estimation -- done | `model/R009-SENSITIVITY-RUN-001.md`, R009 A1 |
| F7 stance | Weakened falsifier accepted and stated; proxy declined; prospective re-arm condition | F7 A1 |
| F3 dry-run pair | Korea 1997 / Japan 1990s, partial-test limitation registered | dry-run README |
| Dry-run order | F6, F4, F3, then flag-only F2 and F8 | dry-run README |

### Run 004: all five gates pass. **Estimation is unblocked.**

PP1 PASS (R5 at 2075 = 0.175; R1--R4 at 2050 all above floor), PP2 PASS (0.065), PP3 PASS (0.2% breach against the 2% bar, max 29.3x), PP4 exact, PP5 PASS. The commit history shows the `s_v` procedure committed before its value was computed. Honest margins: R4's 2050 coverage is 0.070 against a 0.05 floor and dips below it at `deadband = 0.20` per the sensitivity run; PP3's tail still reaches 29.3x inside the rate bar.

### R009 sensitivity findings

Directions as predicted. Gate-crossing values published openly: `deadband = 0.20` starves R4 at 2050; `constraint_ratio = 0.40` starves R5 at 2075; R5's 2075 mass spans 0.037--0.588 across the constraint-ratio sweep, making it the dominant sensitivity. Constants remain frozen.

### Next

1. **Paper B is no longer blocked by the gates.** It remains gated on the model actually being estimated (NumPyro implementation does not exist yet) -- the block moved from "gates fail" to "estimator unbuilt".
2. Dry runs in the committed order: ~~F6 next~~ **F6 run 2026-08-20** -- outcome `discrimination_untestable`, flag `threshold_outside_observed_range` (threshold 7.8pp below the series' 36-year minimum; F6 close to unfalsifiable in practice; see `falsifiers/adjudications/dry-run/F6-2001-2010.md` and F6 adapter Amendment 1). Next: **F4**, then F3 (registered pair), then flag-only F2 and F8.
3. The papers' calibration statement gains four standing caveats: F5-B false-negative mode, F7 weakened-falsifier status, F6 threshold-outside-observed-range, R4's thin 2050 coverage.

---

## 13. State update -- 2026-08-20, third session block: Priority 1 complete, all eight conditions examined

The committed order F4, F3, F2, F8 was run to completion the same day. Full outcomes in `falsifiers/adjudications/dry-run/README.md`; per-adapter flags in each adapter's Amendment 1.

### Final dry-run scoreboard

| Condition | Outcome | Load-bearing flag |
|---|---|---|
| F1 | **Passed** | `tolerance_basis_unspecified` (blocks automatic verdicts; fix before first ingest) |
| F2 | Characterised | **Anchoring gap is verdict-determining**: shadow verdict `triggered` vs binding `not_triggered` -- the only outright disagreement in the set. Candidate `F2-ANCHOR-2` registered, earliest 2027. Threshold at the bottom of a 64-year outturn range (inverted F6) |
| F3 (Clause 2) | **Passed** (generic; the one blind-registered pair -- others disclosed reconnaissance-first) | `seniority_criterion_instrument_mix` watch item |
| F4 | Untestable | `verdict_input_shape_unpublished` -- the majority rule counts a cell no publication provides; sample rule completed while inert; Jaccoud (2025) located, runs toward trigger, **not substituted** |
| F5-B | Failed (Phase 6) | `known_false_negative_mode`; shadow numerator published |
| F6 | Untestable | `threshold_outside_observed_range` -- 7.8pp below the 36-year minimum |
| F7 | Excluded | Weakened falsifier accepted by amendment; no series exists |
| F8 | **Passed** -- the only measurand visiting both sides of its threshold in-record | `construction_spread_exceeds_margin` (~1.7pp spread vs ~1.0pp margin; near-threshold verdicts construction-determined) |

### What the papers must now carry, consolidated

The eight-condition set decomposes as: three clauses with demonstrated discrimination (F1, F3-C2 generically, F8), one demonstrated false-negative (F5-B), two thresholds outside their measurands' observed ranges in opposite directions (F6 never reached, F2 never left), one condition whose live verdict currently depends on an unspecified anchoring with a published disagreeing shadow (F2), and two conditions that cannot currently resolve at all (F4, F7). The set's effective size and independence are both materially below eight, in directions now individually quantified. This paragraph, or its equivalent, belongs in Paper A's calibration section and the essay.

### Next

1. **Writing** (Priority 6): Paper A sections 1, 2, 4-9; essay movements 1-7. The calibration material above is drafted evidence for section 4-adjacent content.
2. **Estimator build** for Paper B (gates pass; NumPyro implementation does not exist).
3. **Before F1 first ingest**: basis-matched cross-check pair, negative-sum semantics, fuel-row summation rule (F1 Amendment 1).
4. **2027 annual review queue**: F5-B-ANCHOR-2 and F2-ANCHOR-2 both become eligible, each with published re-run conditions; F2 shadow needs committed-series (CBO) confirmation at next access.
