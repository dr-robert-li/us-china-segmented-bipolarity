---
target: Paper A drafted sections (S1, S2, S4-S9)
reviewers: [codex, ollama]
reviewed_at: 2026-08-20T16:55:00+10:00
sections_reviewed: [S1-claims.md, S2-introduction.md, S4-measurement-model.md, S5-pre-registration.md, S6-identification.md, S7-prior-predictive.md, S8-cannot-establish.md, S9-open-questions.md]
lanes_failed:
  gemini: auth_dead            # IneligibleTierError -- account requires Antigravity migration; agy CLI not installed
  opencode: review_timeout     # 3 attempts (25m full, 40m no-tools, 30m trimmed to S1/S5/S6/S7); probe fine at 8KB, hangs on large prompts
  claude: self_skipped         # running inside Claude Code; independence rule
  llama_cpp: host_unauthorized # :8080 answers Unauthorized
trimmed_reviewers:
  opencode:
    omitted: [S2, S4, S8, S9]
    note_injected: true
    hard_failed: true          # timed out even after trim; no review produced
notes: |
  codex ran source-grounded (read-only sandbox, repo access) on gpt-5.4-mini --
  the only model its ChatGPT-account auth accepts after the CLI update to 0.148.0.
  ollama ran gemma4:31b locally with no repo access and self-marked
  [reviewed-without-repo-access]; its verdict carries reduced consensus weight.
---

# Cross-AI Draft Review -- Paper A

## Codex Review (gpt-5.4-mini, source-grounded)

**Summary**
This is a strong draft in tone and in the discipline of saying what it cannot establish. The main problem is not the model logic but the calibration narrative: section 5.5 compresses a mixed dry-run corpus into language that implies a much more uniform paired-test regime than the repository record supports. Section 7 is mostly faithful to the committed prior-predictive runs, but there is one wording issue that can read as if a post hoc amendment had always been part of the original priors.

**Strengths**
- The draft consistently foregrounds strongest objections and non-claims rather than hiding them.
- Section 7 is unusually honest about failures, diagnosis, and amendment order, and it tracks the run record closely.
- The identification language is appropriately cautious about weak learning and nonidentification instead of pretending precision where the repository says there is none.
- The vector-vs-scalar case is framed as a measurement choice with explicit costs, which is methodologically cleaner than a standard polemic.

**Concerns**
- **HIGH**: Section 5.5 overstates how much of the dry-run set was actually exercised as paired discrimination tests. The draft says “seven of the eight registered conditions were exercised against historical windows with known answers” in [S5-pre-registration.md](https://github.com/placeholder) and presents the corpus as if the same design applied across the board, but the record is mixed: F2, F4, F6, and F8 are explicitly characterisation exercises or untestable, and F7 is excluded as a weakened falsifier. See [S5-pre-registration.md:115](https://github.com/placeholder), [falsifiers/adjudications/dry-run/README.md:90](https://github.com/placeholder), [falsifiers/adjudications/dry-run/F2-1962-2025.md:11](https://github.com/placeholder), [falsifiers/adjudications/dry-run/F6-2001-2010.md:11](https://github.com/placeholder). Mechanism: the paragraph collapses distinct evidentiary categories into one “calibration” story, which overstates the inferential weight of the dry-run record.
- **MEDIUM**: Section 7.4 says the growth-innovation stream received its own scale “as the committed priors always specified” in [S7-prior-predictive.md:32](https://github.com/placeholder), but the committed prior file shows that the separation was introduced by Amendment 1, replacing the original shared-scale statement in [model/PRIORS.md:249](https://github.com/placeholder). Mechanism: the wording can read as if the amended structure had been the original commitment, which weakens the paper’s auditability claim even if the amendment itself is properly logged.
- **LOW**: Section 6.2’s lower-bound case count is slightly looser than the committed identification file. The draft says “five to eight historical analogues” in [S6-identification.md:109](https://github.com/placeholder), while the committed identification file’s main count is “six to eight” in [model/IDENTIFICATION.md:24](https://github.com/placeholder). Mechanism: the discrepancy is small, but this paper is making a point about epistemic exactness, so the count should be harmonized or the inclusion rule that yields the lower bound should be stated explicitly.

**Suggestions**
- Rewrite section 5.5 as a status table that separates paired discrimination tests, characterisation exercises, untestable cases, live anchoring gaps, and excluded/weakened falsifiers.
- Tighten section 7.4 so it says “after Amendment 1” or “in the amended priors,” not “always specified.”
- Harmonize the analogue count in section 6.2 with the committed identification file, or explain exactly which inclusion rule changes the lower bound.
- If you want the calibration section to carry more evidentiary force, say explicitly which items were true paired tests and which were only structural characterisations.

**Risk Assessment**
**HIGH.** The paper is still likely to attract a referee-level objection on methodological grounds if section 5.5 remains as written, because that section is a load-bearing evidence claim and currently overstates the uniformity and breadth of the dry-run calibration corpus. The rest of the draft is much stronger, but that section is central enough that a skeptical reviewer could doubt the honesty of the evidentiary summary even if the underlying repository record is mostly sound.

---

## Ollama Review (gemma4:31b, [reviewed-without-repo-access])

[reviewed-without-repo-access]

## Summary
This is an extraordinarily rigorous draft that employs a "glass house" strategy—pre-emptively disclosing every possible methodological failure and providing the strongest available counter-arguments to its own claims. The author does not attempt to hide the "small-$n$" problem or the fragility of the core mechanism parameter ($\delta$), but instead centers them as part of the epistemic record. While the intellectual honesty is exemplary, the paper's survival depends on whether a referee accepts "auditability" and "structural transparency" as substitutes for "predictive validation." The prose is precise, and the internal architecture (from claims to identification to failures) is logically tight.

## Strengths
*   **Epistemic Integrity:** The habit of attaching the strongest published objection to every claim (Section 1) is a high-tier academic defense mechanism that significantly reduces the "hit surface" for referees.
*   **Identification Transparency:** Section 6 avoids the common error of assuming identification; it explicitely maps which parameters are identified, weakly identified, or not identified at all.
*   **Failure as Contribution:** Section 7's reporting of prior-predictive failures and implementation defects is a "gold standard" for reproducibility. It demonstrates that the gates actually work by showing they can fail.
*   **Clarity of Scope:** The paper explicitly denies claiming predictive superiority (Section 1.2, 8), effectively neutralizing the most common critique of vector-based measures over scalars.

## Concerns

### HIGH: Stability of $\delta$ and the "Information Gap"
Section 6.3 admits that $\delta$ (the mechanism parameter) is contingent on a decade of data for a fifty-year projection. While the paper honestly reports this, it may understate the *practical* implication: if $\delta$ is barely learned, the long-horizon trajectories in Paper B will be dominated by the priors rather than the data. 
*   **Referee Objection:** "The author claims the model is auditably registered, but since the core parameter $\delta$ is essentially unconstrained by the data, the results are a reflection of prior assumptions, not an empirical finding."

### MEDIUM: Small-n Calibration vs. Validation
Section 6.2 correctly distinguishes between calibration and validation given the dyad-count ($N=5\text{--}8$). However, "calibration" in a Bayesian context can still be seen as over-fitting if the model is sufficiently flexible.
*   **Referee Objection:** "With dozens of parameters and only 8 dyads, any 'sane behavior' observed during calibration is likely an artifact of parameter tuning rather than structural validity."

### MEDIUM: The Asymmetric Backtest (Section 6.4)
The decision to only test against "declinist waves" without a corresponding "ascendancy wave" test is defended as a lack of available data on falsified ascendancy claims.
*   **Referee Objection:** "By explicitly engineering the model to not repeat the mistakes of historical declinists, the author has effectively hard-coded an anti-declinist bias into the specification's selection process."

### LOW: Unverifiable Calibration Record (Technical)
Section 5.5 provides a very specific summary of the dry-run record (e.g., "F5 Sub-clause B returns the same verdict on the archetypal positive case and the negative control"). Because I lack access to `falsifiers/adjudications/dry-run/README.md`, I cannot verify if these summaries are faithful or if they gloss over other failures.

## Suggestions
1.  **Quantify the "Not Learned" state:** In Section 6.3, instead of just saying $\delta$ might be "not learned," explicitly define the posterior width that constitutes "not learned." If the posterior is nearly identical to the prior, this should be stated as a primary result of the measurement paper.
2.  **Address the "Prior-Driven" Risk:** Add a subsection in Section 8 or 9 discussing the risk of "prior-dominance." Acknowledge that if $\delta$ remains weakly identified, Paper B is essentially a sensitivity analysis of the priors rather than an empirical discovery.
3.  **Formalize the Naive Benchmark:** In Section 9, move from "posing the question" to proposing a specific candidate for the benchmark (e.g., a constrained random walk) based on the data's properties, even if it remains a proposal.

## Risk Assessment
**OVERALL RISK: MEDIUM**

The risk is not that the paper is "wrong," but that it is "too honest" about its limitations to be seen as providing a useful *measurement* tool by traditional standards. A hostile referee will ignore the auditability and focus entirely on the small-$n$ size and the weakly identified $\delta$. However, because these are already disclosed as failures/limitations in the text, the author has essentially "pre-answered" the objections. The paper is likely to pass if submitted to a venue that values methodological transparency over "clean" (but deceptive) results.

---

## Consensus Summary

Two reviewers returned substantive reviews: codex (source-grounded, full repo access) and ollama/gemma4 (text-only, reduced consensus weight per the [reviewed-without-repo-access] rule). Plan-level consensus below is based primarily on the grounded reviewer, with the text-only reviewer's concerns folded in where they converge.

**Orchestrator verification.** Codex's two sharpest claims were checked against the repository before this summary was written, and both are CONFIRMED:

1. `model/PRIORS.md` line 134 commits `u, v ~ Normal(0, sigma_u^2)` -- ONE shared scale -- and Amendment 1 (line 243) introduces `sigma_v` as a prospective supersession. S7.4's phrase "as the committed priors always specified" and S7.3's defect-3 framing ("the implementation shared one innovation scale where the committed priors distinguish them") are therefore factually wrong: the original commitment WAS shared-scale, the implementation was faithful to it, and the separation was a genuine prior change selected by Q&A. Run 001's actual defect C was four sampler transcription errors (kappa cap, phi uniform, rho_g uniform, xbar uniform) whose false diagnosis concerned kappa, not sigma_v. S7.3 conflates the defect story with the remedy story.
2. `model/IDENTIFICATION.md` carries "approximately five to eight" (line 11) and "Six to eight cases" (line 24); S6.2 quotes only the looser bound. Harmonise or state the inclusion rule.

### Agreed Strengths
- The objections-attached discipline (every claim carrying its strongest published objection) -- both reviewers independently call it the draft's defining strength.
- Section 7's failure reporting -- both call it gold-standard / unusually honest.
- Identification candour in section 6 -- explicit per-quantity identified/weak/not-identified mapping.

### Agreed Concerns
- **The calibration/evidentiary summary claims more uniformity than the record supports** (codex HIGH, verified; ollama flagged the same subsection as unverifiable from text alone -- convergent from both directions). S5.5's "seven of the eight ... exercised against historical windows with known answers: an expected-positive episode and a negative control" implies a uniform paired-test regime; the dry-run record is mixed -- F2/F6 characterisation or untestable, F4 untestable, F8 characterisation-with-discrimination, sequence disclosures varying by condition. Remedy both point to: a per-condition status table separating paired discrimination tests, characterisation exercises, untestable cases, and the excluded falsifier.
- **delta prior-dominance is understated in its practical consequence** (ollama HIGH; codex adjacent via identification-candour praise plus S7 wording concern). If delta is barely learned, Paper B's long-horizon output is prior sensitivity analysis, and S6.3/S8 should say that as a primary anticipated result, not a caveat.

### Divergent Views
- Overall risk: codex HIGH (driven entirely by S5.5's load-bearing overstatement), ollama MEDIUM ("too honest to be publishable as measurement" rather than wrong). Not a real disagreement about the text -- codex weights the one verified overclaim heavier because it could read as dishonest in a paper whose brand is honesty.

### Action items for the author
1. S5.5: replace the compressed narrative with the per-condition status table (HIGH, verified).
2. S7.3/7.4: rewrite the defect-3 and remedy wording to match PRIOR-PREDICTIVE-RUN-001.md defect C and PRIORS.md Amendment 1 -- "the amended priors", never "always specified" (MEDIUM, verified).
3. S6.2: harmonise the analogue count with IDENTIFICATION.md or state the inclusion rule (LOW, verified).
4. S6.3/S8: add the prior-dominance consequence for Paper B as an anticipated primary result (MEDIUM).
5. S9 question 3: consider proposing a concrete benchmark candidate rather than only posing the question (ollama suggestion, optional).

### Disposition -- 2026-08-20, author decision

A1-A3 applied (verified fixes). A4 applied (S6.3 consequence paragraph, S8 fifth item), author-reviewed. **A5 declined as prose, with recorded reason:** a benchmark named in the paper without registration is a soft commitment made outside the project's candidates-grounds-Q&A machinery -- the same shape as F1's unregistered-series defect -- and would anchor the later registration anyway. Benchmark selection is routed to prospective registration instead (queued in HANDOVER); S9 question 3 gains a sentence citing the registration once it exists.
