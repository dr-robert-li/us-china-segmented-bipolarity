# F3 human capital: measurand and source commitment

Pre-registered, 0.1.0, 2026-08-22. Closes HANDOVER section 18 Decision C by author decision of 2026-08-22 (three-model council review -- Grok 4.6, Gemini 3.7, Kimi K3; author-adopted recommendations; the council SPLIT on this one and the split is recorded below rather than smoothed). Committed **before any F3 series is fetched**.

---

## The measurand and the committed primary source

**F3 is the PWT human-capital index (hc)**: the Penn World Table's continuous per-worker human-capital measure, derived from Barro-Lee attainment via returns-to-schooling, both states, same vintage-pinning rule as F2 (`pipeline/definitions/capital-depth.md` -- one pinned PWT release serves both inputs, one snapshot, one hash discipline, same truncation-with-coverage-flag tail rule).

**Barro-Lee attainment DIRECTLY is declined on a technical ground, not a preference:** the attainment tables step in 5-year intervals, and any interpolation to annual frequency injects a deterministic sawtooth into a latent that the model commits to a local-linear-trend process -- a periodic artefact the growth-innovation stream would absorb, biasing `sigma_v`-adjacent estimation downward. PWT's hc is the same underlying information already smoothed by a published, versioned procedure that is not this programme's own invention.

## The recorded objection, and what it buys

The council's construct-validity objection (Gemini lane) is real and is recorded rather than argued away: "human capital as a frontier input" is not general schooling. An economy-wide attainment index moves slowly and smoothly across the whole 1975-2025 window regardless of what happens at the frontier, so hc is a weak instrument for exactly the frontier-labour question the bundle poses. The alternative it argued for -- an R&D-personnel headcount, tertiary/researcher-weighted (OECD MSTI / UNESCO) -- tracks the construct better and fails on coverage: the CN researcher series has material gaps before the 1990s, and a frontier input unobservable for the first third of the window forces either an anchored splice or a very wide anchor-absent prior across half the panel.

**Resolution: hc committed as primary; the researcher-weighted variant registered as mandatory sensitivity run S11** (`model/PRIORS.md` Amendment 4 -- the section 7 list is extended, never shortened). The construct-validity objection is thereby honoured with a registered obligation rather than left as an unrecorded road not taken: if a headline result flips under the researcher-weighted variant over its observable window, it is reported as prior-dependent in the abstract, per the S-list's own rule.

## Anchor status

**Anchor-absent**, same ground as F2: a returns-to-schooling-weighted index is a derived model output, not a physically measurable quantity; bias fixed at prior mean per SPECIFICATION.md section 4.2; F3 stays on the exported anchor-absent list. Tier-1/tier-2 anchor adoption, if ever, by dated amendment here.
