# Pipeline implementation

Executable implementation of `pipeline/schema.md`, `pipeline/rules/`, and `pipeline/adapters/F1.md`. Python 3.11 or later. Runtime dependencies: `numpy` for the model module only; the schema, rules, reconciliation and F1 adapter modules use the standard library alone.

**No network access.** Nothing in this directory fetches anything. Ingestion is a separate concern from derivation, and mixing them would make the derivation non-reproducible for anyone who cannot reach the upstream sources on the day they run it. Adapters accept `Observation` records and return verdicts; how those records were obtained is recorded in each observation's `source_id`, `vintage` and `retrieved_at` fields.

## Running

```
cd pipeline
PYTHONPATH=src python3 -m unittest discover -s tests -t .
```

37 tests. The prior-predictive gates:

```
cd pipeline/src
python3 -c "from usbip.model import prior_predictive as pp; [print(r) for r in pp.run_all(n_draws=400)]"
```

Two of the five gates fail at the committed priors, which is the recorded state of the project rather than a broken checkout. See `model/PRIOR-PREDICTIVE-RUN-001.md`. **Estimation is blocked** pending a dated amendment.

Regime masses at a chosen horizon:

```
python3 -c "from usbip.model import prior_predictive as pp; print(pp.regime_masses(400, 20260819, horizon=2050))"
```

## Layout

| Module | Implements |
|---|---|
| `usbip/schema.py` | The frozen observation record, closed flag set, unit conversions, Type B and D validation |
| `usbip/rules.py` | Registry `REGISTERED`, plus R001, R002 and R003 |
| `usbip/reconcile.py` | Cross-source comparison and vintage-conflict detection |
| `usbip/adapters/f1.py` | The F1 condition end to end |
| `usbip/model/prior_predictive.py` | Blocks E and P, the R009 classifier, gates PP1 to PP5 |

## Four design commitments visible in the code

**Determinism, and no wall-clock in any identifier.** `obs_id` is a SHA-256 over `series_id|geography|period_start|period_end|value|unit|vintage|source_id`. Derivation identifiers hash the rule id, version and sorted inputs. A `uuid4` or a timestamp in either would make two runs over identical inputs produce non-identical output, which breaks the idempotency and determinism tests and, more importantly, breaks the audit claim the repository makes.

**`DETERMINISTIC_EPOCH` rather than `datetime.now()`.** Anywhere a default timestamp is needed.

**No `resolve()` in `reconcile.py`, deliberately.** The module compares sources and raises flags. It does not pick a winner. A reconciliation function that silently selects between disagreeing sources is a favourable-source substitution mechanism with a neutral name, and the pre-registration prohibits exactly that. Disagreement blocks verdict emission and goes to adjudication.

**A closed flag set.** `FLAGS` is a frozen set and an unrecognised flag raises. An open flag vocabulary drifts, and a flag nobody recognises is not a flag.

## The synthetic baseline is not data

`SYNTHETIC_BASELINE` in `prior_predictive.py` is labelled NOT DATA in the source and is repeated here because it is the single most misreadable object in the codebase. It exists so that PP4, the state-swap symmetry gate, has something asymmetric to swap. Its values encode no estimate of either country's position. Any number produced from it is a statement about the prior, not about the world.

## Where the implementation diverges from a specification

Two places, both registered rather than silent:

- **R009 defines R3 as challenger peaking**, generically, while `SPECIFICATION.md` names it "PRC peaking". The PRC-specific label cannot survive a state swap and would break the equivariance PP4 tests. See `rules/R009-regime-classification.md` section 2.
- **`rules.py` carries a correction** to an earlier docstring that gave the denominator basis as the material reason PRC utilisation hours are not comparable to EIA capacity factors. Both countries' official annual figures use a time-averaged capacity denominator, so that reason is wrong for the published statistics. The correction is recorded in place rather than deleted, because the same reasoning would have justified an adjustment factor that is not warranted. See `rules/R003-nameplate-to-dispatchable.md` section 4.1.

## Not implemented

- Ingestion. No adapter fetches.
- Block M, the measurement block. The prior predictive concerns whether the structural core can produce all five regimes and behaves symmetrically; a measurement block would add bias terms without bearing on either question.
- Adapters for F2 through F8.
- Estimation. Blocked by the two failing gates.

## Sources

- `pipeline/schema.md` -- observation record and validation requirements
- `pipeline/rules/README.md` -- registry format and versioning policy
- `pipeline/adapters/F1.md` -- the F1 condition, its three hazards, and its seven required tests
- `model/PRIORS.md` -- committed prior forms, audited by `tests/test_registry_and_priors.py`
- `model/PRIOR-PREDICTIVE-RUN-001.md` -- runs 001 to 003 and the two failing gates
- `DATA-INTEGRITY.md` -- the dispatchable-conversion mandate and F1's bounded exemption
