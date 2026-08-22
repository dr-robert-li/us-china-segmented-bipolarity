# F2 capital depth: measurand and source commitment

Pre-registered, 0.1.0, 2026-08-22. Closes HANDOVER section 18 Decision B by author decision of 2026-08-22 (three-model council review -- Grok 4.6, Gemini 3.7, Kimi K3 -- with author-adopted recommendations; unanimous on the measurand reading). Committed **before any F2 series is fetched**, per the register-before-compute discipline: source selection fixed here cannot have been steered by seen data.

---

## The measurand

**F2 is produced-capital intensity: real capital stock per worker** (reading (i) of the section-18 Q&A). Physical and produced capital available per unit of labour, the classical "capital deepening" quantity, entering the frontier bundle as the capital input the `sigma_F` prior already reasons about (`model/PRIORS.md` section 1.1 centres `sigma_F` on the capital-labour elasticity literature "because the frontier bundle contains capital depth and human capital").

**Reading (ii) -- financial depth -- is declined as a specification error, not a preference.** `README.md` defines `Y_fin` as "capital-market depth, fiscal headroom, reserve-currency privilege". A financial-depth F2 (IMF Financial Development Index family, BIS credit series) would place the same latent construct on both sides of the production function -- once as a frontier input, once as a capability element -- and the double-count would be structural, not a matter of measurement precision.

## The committed source

**Penn World Table, capital series**: real capital stock at constant national prices and employment, giving capital stock per worker; both states; PPP-adjusted on PWT's published basis.

- **Vintage rule (provisional pending author ratification, in the Amendment-3 pattern):** the newest PWT release published at the date of first snapshot, pinned at fetch by release number and content hash; later vintages enter only by dated amendment. The vintage is a rule fixed before fetching, not a number chosen after.
- **Tail rule: truncate at the last year the pinned vintage covers.** No data-side extrapolation to 2025. Ground: Block M already treats every series as a noisy view of a latent that continues past the last observation, so the latent path covers the tail through the state-space process; an extrapolation rule would be a second, versioned, sensitivity-carrying data construction with no offsetting benefit. The truncation is registered as a **coverage flag** on every consuming output, in the F1/F8 pre-ingest pattern.
- **Coverage:** PWT reaches back past 1975 for both states; the estimation window's early years are covered. The known weakness is the PRC side of any PPP-based series and it is carried by the bias machinery, not hidden.

## Anchor status

**Anchor-absent, re-affirmed on a stated ground rather than inherited from the synthetic convention.** SPECIFICATION.md section 4 grants a tier-1 anchor on exactly one ground: physical measurability. A PPP-adjusted, depreciation-modelled, derived capital series is not physically measurable in that sense -- it is a model output of the national-accounts apparatus (DATA-INTEGRITY.md tier hierarchy). Consequence per section 4.2: the bias term is fixed at the prior mean, and F2 appears in the anchor-absent list exported with every fit. If a tier-1 or tier-2 anchor candidate is identified at ingest, its adoption is a dated amendment to this file.
