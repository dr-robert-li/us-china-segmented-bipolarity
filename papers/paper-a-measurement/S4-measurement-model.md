# Paper A, section 4 -- Measurement model

**Status.** Draft, 2026-08-20. The model class is not novel and this section says so at the start. The contribution is the application domain and the discipline around it, not the estimator.

---

## 4.1 The tradition being joined

Bayesian latent-variable measurement is an established practice in political science, and this paper joins it rather than founding anything. Four precedents are cited, each for a distinct reason, and together they define the standard the rest of the section is answerable to.

**Treier and Jackman** are cited for the demonstration that ignoring measurement error manufactures results. Treating Polity scores as observed data, a canonical downstream regression achieves r-squared of .63; on posterior means of the latent trait, .57; with posterior uncertainty propagated, .40, and the quadratic term of interest becomes indistinguishable from zero ([Treier and Jackman](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=61fb0ba9b2e3c6b8619a4aa493fa55f26ff6c10c)). The lesson imported here: every downstream consumer of the capability vector receives draws, never point estimates.

**Pemstein, Meserve and Melton** are cited for aggregation weights derived from the model rather than chosen by the analyst: their posterior mean is precision-weighted by construction -- `sum_j(t_ij / r_j^2) / (1/r_0^2 + sum_j 1/r_j^2)` -- which is the direct alternative to CINC's ad hoc equal weighting ([Pemstein, Meserve and Melton](https://www.cambridge.org/core/journals/political-analysis/article/democratic-compromise-a-latent-variable-analysis-of-ten-measures-of-regime-type/2A6B2BBA6F80367644F2C5007E1CFC29)). Where this paper's model weights sources, the weights are estimated precisions, not judgements.

**Fariss** is cited for dynamic latent traits with time-varying measurement -- the standard-changing problem is structurally identical to a statistical agency revising a methodology -- and for the practice of declaring non-identification in the running text ([Fariss](http://cfariss.com/documents/Fariss2014APSR.pdf)).

**Hanson and Sigman** are the closest existing analogue: 21 indicators of state capacity, three retained dimensions -- extractive, coercive, administrative -- deliberately not collapsed to one number ([Hanson and Sigman](https://public.websites.umich.edu/~jkhanson/resources/StateCapac_v1_doc.pdf)). The capability vector is the same architectural shape applied to a different substantive domain.

## 4.2 What is measured versus what is latent

No observed series is treated as the quantity itself. Every published statistic is a noisy, possibly biased view of a latent quantity:

```
z[k,i,t] = lambda[k] * f_k(x[i,t], Y[i,t]) + b[k,i] + eps[k,i,t]
```

where `k` indexes source-series pairs, `lambda[k]` is a loading, `b[k,i]` a source- and state-specific bias term, and `f_k` the committed mapping from latent inputs to what the series purports to measure.

The bias terms are symmetric by construction, implementing the programme's first standing prohibition -- no asymmetric epistemic standards -- as a property of the code rather than a statement in a preface. PRC GDP-linked series carry a bias term with an informative prior from a published falsification band; US fiscal projections carry a bias term with an informative prior from published CBO projection-error bands; US inequality measures carry a bias term with a wide prior because the competing-approach range is carried, not resolved. A series is granted `b = 0` on exactly one ground: physical measurability. That is the single asymmetry in the block, and it is an asymmetry between measurement types, not between countries.

The identification problem this creates is stated rather than hidden: a free bias per source-state pair is not identified from a single series. Identification comes from multiple sources on the same latent quantity with at least one physically-measurable or independently-audited anchor. Where no anchor exists, the bias is fixed at its prior mean rather than estimated, and the affected posterior carries an `anchor_absent` flag in every output that consumes it. The anchor-absent list is published with the estimates. Section 6 gives the per-quantity statements.

## 4.3 Rules as versioned objects

Every transformation from published statistic to model input is a registered rule with a semantic version and a source list; a derived figure whose governing rule is not registered is not publishable. Eleven rules are registered at the time of writing. Versioning is semantic in a specific sense: a patch changes documentation, a minor version cannot alter any published verdict, a major version can -- and a major bump requires the affected verdicts to be recomputed under both versions with both published. Silent re-derivation of published figures is prohibited outright.

The load-bearing rule for this paper is the conversion from nameplate generation capacity to dispatchable capacity, because it is where the definitional-divergence argument becomes concrete rather than rhetorical.

## 4.4 The refusal, stated as a property of the rule

United States capacity factors and PRC capacity factors are computed from differently scoped statistics. The dispatchable-capacity rule therefore **refuses to emit a cross-state ratio**. This is not a hedge appended to a number; the rule will not produce the number. Relative position on that element enters through the measurement block, where the definitional gap is represented as uncertainty.

The objection -- that this produces intervals too wide to inform anything -- is the strongest objection to claim C3 and is answered the only honest way available: by reporting the interval and letting the reader judge whether it is vacuous, rather than narrowing it with a comparability assumption that neither statistical system underwrites. If the interval turns out vacuous, that is a finding about the state of comparable measurement between the two countries, and it is reported as one.

## 4.5 One expectation refuted while specifying the rule, recorded rather than deleted

The standard objection to comparing PRC utilisation hours with US capacity factors is that the PRC denominator is year-end capacity, which understates utilisation in a fast-growing fleet. While specifying the rule, this expectation was checked against the primary methodology documents and found wrong: the published Chinese methodology is explicitly an average over calendar time ([China Energy Portal](https://chinaenergyportal.org/statistical-reporting-system-for-renewable-energy/)), and EIA's annual figure is likewise a time-weighted average of monthly values ([EIA Table 6.7.A](https://www.eia.gov/electricity/monthly/xls/table_6_07_a.xlsx)). The denominator error is real only in third-party recomputation from year-end stocks.

The refutation is reported for two reasons. The adjustment the expectation would have justified is in wide circulation and is not warranted against the official series. And a measurement paper that reports only the expectations it confirmed is exhibiting exactly the selection bias its measurement model exists to correct.
