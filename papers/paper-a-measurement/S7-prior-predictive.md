# Paper A, section 7 -- Prior-predictive checking, reported including its failures

**Status.** Draft, 2026-08-20. The outline for this section was written while two gates were failing and estimation was blocked. The gates now pass, and the section reports the full sequence -- failure, diagnosis, remedy selection, pass -- because the sequence is the evidence. A section reporting only the final pass would exhibit exactly the survivorship the gates exist to prevent.

---

## 7.1 The design

Five prior-predictive gates were specified before estimation and run before any observed data entered the model. They ask whether the committed structure behaves acceptably before it has seen anything: every regime reachable with non-trivial prior mass where the output contract claims it (PP1); the thesis regime refutable -- capable of receiving mass below 0.2 under some admissible data (PP2); no structurally runaway trajectories (PP3); exact symmetry under exchange of the two states (PP4); no divergence regime dominant a priori (PP5). Failure of any one blocks estimation, and the committed remedy discipline is that a failing configuration is amended only by a dated amendment whose grounds are statable without reference to which option makes the gate pass.

PP4 deserves one sentence of design detail: it is the mechanical implementation of the programme's first standing prohibition. Swapping the two states' data and state-indexed parameters must produce mirror-image regime classifications, draw by draw. Asymmetry there means asymmetry was built into the structure, and the committed remedy is to rebuild rather than adjust.

## 7.2 The failures

At the committed priors, **PP1 and PP3 failed**, and estimation was blocked. The dual-constraint regime was unreachable at the 2050 horizon (prior mass below the 0.05 floor), and a small but systematic fraction of prior draws produced input trajectories exceeding a 20x plausibility ceiling by 2050 -- paths no national generation fleet or robot stock has ever traced. The failing configuration was committed as-is rather than replaced, so that the eventual amendment could be read against it.

## 7.3 Three implementation defects, one of which manufactured a false diagnosis

Running the gates surfaced three defects in the checking code itself, disclosed in the run record:

1. **Surrogate priors in the harness.** The first implementation drew two saturation parameters from uniform surrogates rather than the committed distributions, truncating a tail and understating attainable saturation drag.
2. **Unpaired shocks in the symmetry test.** The first PP4 implementation consumed different random numbers in the base and mirrored runs, so the comparison measured Monte Carlo noise as well as asymmetry, and failed on noise. The fix -- pre-drawn shock streams applied identically to both runs -- makes the expected deviation exactly zero, so that any deviation at all is structural.
3. **A prior-transcription defect that produced a quantitatively specific, entirely false diagnosis.** The implementation shared one innovation scale across the level and growth shock streams where the committed priors distinguish them. The growth stream, compounding under persistence, produced the PP3 runaway -- and the first diagnosis attributed the failure to the committed growth priors themselves, which would have justified widening a pre-registered prior in exactly the direction that made the failing gate pass.

The third defect is the one this paper exists to report. It is the failure mode a pre-registration regime is least protected against: **the registered object was correct and the code implementing it was not**, and the code's error generated a plausible argument for amending the registered object. The remedy adopted was a moment audit -- the sampler's output checked distribution by distribution against the priors file -- which is now a standing test. The general lesson is that a pre-registered specification without a verified implementation is registered in name only.

## 7.4 The remedies, and the grounds on which they were chosen

Both failures localised to the prior file rather than to the model blocks, and both remedies were selected -- from candidate lists committed before selection -- on grounds statable without reference to gate outcomes:

- **PP1.** The output contract was restricted: the dual-constraint regime is reported at the 2075 horizon only, where the committed ceilings and growth priors can actually populate it, rather than at 2050, where they cannot. The gate follows the claim: coverage is now checked at the earliest horizon at which the contract claims each regime. The ground is that reporting a posterior for a regime at a horizon the prior structure cannot inform would present a number with no content -- true whatever any gate says. The alternative remedies -- lowering engineering ceilings or loosening the constraint threshold -- were declined because both move quantities that bear on gates or falsifier-adjacent ceilings.
- **PP3.** The growth-innovation stream received its own scale, as the committed priors always specified, with the scale itself derived by a procedure committed before its value was computed: the pooled AR(1) residual scale of observed log capacity growth for both states over 2002--2025, from a content-addressed snapshot of the source series. The derivation procedure's commit precedes the value's computation in the history, which is checkable.

## 7.5 The pass, with its margins stated

At the amended configuration all five gates pass. The passing run's honest margins are part of the record: the segmentation regime's coverage at 2050 sits at 0.070 against a 0.05 floor and dips below the floor under one classifier-constant sensitivity setting; the trajectory-sanity tail still reaches 29x inside its 2 percent breach-rate bar. A sensitivity sweep over the classifier constants was run before estimation, its gate-crossing values published openly, and the constants frozen: the values at which gates would flip are on the record precisely so that a later reader can check that none was quietly adjusted.

Two facts about the sequence bear on how much the pass is worth. The gates failed first, which is evidence they can fail -- a gate that has never failed is a gate of unknown power. And every remedy's ground is readable against the committed failing configuration, so a reader who thinks a remedy was outcome-directed has the materials to make that case. The gates do not certify the model; they certify that the model's structure was interrogated before data arrived, and they blocked estimation for exactly as long as the interrogation kept finding problems.
