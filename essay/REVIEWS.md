---
target: essay/DRAFT.md (second draft, seven movements)
reviewers: [codex, ollama]
reviewed_at: 2026-08-22T09:40:00+10:00
lanes_failed:
  gemini: not_attempted        # auth dead as of Paper A review; unchanged
  opencode: not_attempted      # hard-failed on large prompts at Paper A review; unchanged
  claude: self_skipped         # drafted inside Claude Code; independence rule
notes: |
  codex ran source-grounded (read-only sandbox, repo access) on gpt-5.4-mini --
  the account's only accepted model, as at the Paper A review. First attempt
  hung on stdin, second failed on the default model id; third ran clean.
  ollama ran gemma4:31b locally with no repo access and self-marked
  [reviewed-without-repo-access]; reduced consensus weight, per convention.
  Raw lane outputs committed as essay/review-raw-codex.txt and
  essay/review-raw-ollama.txt (terminal control noise stripped; the ollama
  file retains its visible thinking trace); substance reproduced below.
---

# Cross-AI Draft Review -- Essay

## Codex (gpt-5.4-mini, source-grounded) -- findings and dispositions

**Summary (reviewer's):** draft mostly executes the outline cleanly; core quantitative spine well grounded; one provenance slip, one policy-adjacent sentence, closing movement repeats more than it advances. Movements 3 and 6 strongest and mostly satisfy the fairest-passage requirement.

| # | Sev | Finding | Disposition |
|---|---|---|---|
| C1 | HIGH | Luxembourg 3rd-113th (and 60-of-163) not in the cited paper-A cluster; provenance statement broader than the record shown | **Fixed differently than proposed.** Both numbers are in the fetched record -- `research/phase4_measurement_sources.md` (Slottje pp. 18-19 and Saisana & Saltelli 2010, both reported inside Ravallion). Draft now attributes the chain explicitly and the status block names the research file. Nothing cut. |
| C2 | HIGH | "Force planning" / "alliance accounting" is policy framing, against the outline's constraint | **Fixed.** Sentence rewritten without downstream-use examples. |
| C3 | MEDIUM | Movement 7 weakest; closes by synthesis and recap rather than an irreducible final step | **Declined with ground, partially.** The outline commits M7 to exactly this close ("Close on the price, not the payoff"; "A last empirical caution to end on, so the essay does not close on its own preference") and mandates the two-analysts passage. The alternatives-problem paragraph added in this draft is M7's non-recap contribution. Author may overrule at author-read. |
| C4 | MEDIUM | M3 steel-man reads grudging: "the bet has been placed" pivots back to advocacy before the concession settles | **Fixed.** Closing paragraph reordered; the commitment is named as a liability and the movement now ends on the concession that the predictive record belongs to the other side. |
| C5 | LOW | M2 jargon-dense mid-section | **Declined.** The outline designates M2 "the technical heart, written for a reader who has never opened the composite-indicator literature"; density is the burden it carries. Flagged for author judgement. |
| C6 | LOW | Ending repeats exchange-rate/dashboard vocabulary | **Declined with C3's ground**; the caution close is outline-mandated. |

## Ollama (gemma4:31b, [reviewed-without-repo-access]) -- findings and dispositions

**Summary (reviewer's):** sophisticated methodological intervention; M3 a genuine steel-man, not grudging; M6 fair because it gives specific failure mechanisms; symmetric critique applied to own programme.

| # | Sev | Finding | Disposition |
|---|---|---|---|
| O1 | HIGH | M7's net-capacity composite admission is a "logical leak" -- the vector still contains a hidden exchange rate | **No change; working as designed.** The admission is the outline's own required concession ("`Y_net` is a composite in all but name... which is a difference of degree"), and the draft states the degree-not-kind verdict explicitly. A reviewer without repo access cannot see that the concession is pre-committed. |
| O2 | MEDIUM | M3-to-M7 bridge thin: a hostile reader may call trajectory monitoring descriptive bookkeeping if it cannot inform war prediction | **Accepted in part.** The alternatives-problem paragraph in M7 now carries the answer (some questions have no well-posed scalar answer; the vector serves the narrower one). The residual objection is real and unresolved; it is Lind's objection, which M4 explicitly records as unanswered. No further change without author direction. |
| O3 | LOW | Case-count symmetry passage risks academic skirmishing | **Declined.** The outline mandates the symmetry passage in the same breath as the critique; removing it would violate the no-asymmetric-standards constraint. |

## Consensus notes

Both lanes independently rate M3 and M6 as satisfying the fairest-passage requirement (codex with the C4 caveat, now fixed). Both identify M7 as the structurally weakest movement -- one as recap, one as residual tension -- which is consistent with the outline's own design decision to close on cost and caution; the author should read M7 knowing both reviewers paused there.

Word count after dispositions: 5,851 including front matter, ~5,600 body -- BELOW the outline's 6,000-word floor. Recorded rather than padded: the draft covers every outline commitment, and stretching it to the floor with filler would trade a stated shortfall for a hidden one. Whether to expand (candidates: M2's normalisation treatment, M5's objection table) is an author-read decision. Author read pending.
