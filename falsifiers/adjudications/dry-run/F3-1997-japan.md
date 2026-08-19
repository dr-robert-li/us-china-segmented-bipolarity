# F3 dry run -- Korea 1997 expected-positive, Japan 1990s negative control

**Nothing in this file is a finding about the present.** Rubric exercise under `README.md` conventions, applying F3 Clause 2's unmanaged-cascade rubric to two closed episodes. Not a determination; binds no live verdict.

**Outcome, stated at the head: the Clause 2 rubric discriminates on the analogue pair.** Korea 1997 returns the analogue of `met`; Japan 1990s returns `not_met`. None of the three failure conditions occurred. The registered limitation stands undiminished: this tests the *unmanaged-cascade* rubric generically, not the PRC-specific LGFV counting rules, and Clause 1 (the augmented-debt arithmetic) is untested here. Score across the set: one failed (F5-B), two passed (F1, F3-C2 generic), two untestable (F6, F4), two remaining (F2, F8).

---

## Design and registration

**This is the first exercise in the set whose episode pair was registered before any evidence was gathered.** The pair, the selection criterion (known-answer clarity first, structural analogy second), and the limitation were fixed by author decision of 2026-08-20 in structured Q&A and committed to `README.md`'s registered-exercises table before reconnaissance began. The evidence below was fetched after registration; the sequence is verifiable from the commit history.

| Element | Committed |
|---|---|
| Falsifier | F3 -- IMF augmented debt above 180 percent of GDP **with** an unmanaged LGFV default cascade, by 2035 |
| Clause exercised | Clause 2 only: the unmanaged-cascade rubric and its six indicative criteria |
| Expected-positive | Republic of Korea, 1997: the chaebol-banking collapse |
| Negative control | Japan, 1990s: the managed absorption of a comparable debt overhang |
| Failure condition 1 | The rubric returns `not_met` on Korea |
| Failure condition 2 | The rubric returns `met` on Japan |
| Failure condition 3 | The same verdict on both -- the most serious |
| Registered limitation | Corporate-banking issuers stand in analogically for LGFVs; "province" reads as issuer-group/region; nothing here validates the LGFV-specific counting |

### The known answers

Korea 1997 is the archetypal unmanaged cascade in the modern record: sequential conglomerate insolvencies through 1997 ending at the sovereign's brink of default in December, resolved only by an externally enforced creditor standstill. Japan's 1990s banking problem is the canonical managed case: losses of far larger eventual size absorbed over a decade through deposit-insurance resolution, public capital injection, and orderly court process. Both characterisations are documented below from the sources fetched for this exercise; neither is contested in any account known to this project.

---

## The adverse case, written first

**Against the exercise's usefulness.** The strongest objection: a corporate-banking crisis is not a subnational quasi-fiscal debt crisis. Chaebol were private conglomerates with market creditors; LGFVs are implicit-liability vehicles of subnational governments whose "default" is intertwined with intergovernmental fiscal relations that have no Korean or Japanese analogue. A rubric that separates Korea from Japan may still fail on the thing it exists for -- distinguishing a managed LGFV workout from an unmanaged one inside a state with far greater administrative control over creditors than Seoul or Tokyo had. This is conceded in full; it is the registered limitation, and it is why this exercise is labelled a partial discrimination test.

**Against the expected-positive verdict.** The serious objection: Korea's sequence was eventually managed -- the IMF programme of December 1997 and the enforced rollover of January 1998 are management, and they worked. If "unmanaged" means *never brought under control*, Korea fails the definition. The response is in the clause's own wording, which the adapter places on the authorities' capacity: the clause requires evidence that authorities "attempted and failed to contain a default sequence". Korean authorities attempted containment through 1997 -- case-by-case support, then spending down reserves in October-November -- and the sequence ran to the sovereign's brink of default anyway; containment ultimately required external actors imposing a standstill on foreign creditors. A cascade that ends when outside parties compel a standstill is a cascade the domestic authorities failed to contain. The adverse reading is recorded, not erased: on a strict *never-managed-by-anyone* reading, no historical episode would ever qualify, which would make the clause unfalsifiable by construction.

**Against the negative-control verdict.** Japan's November 1997 was not tranquil: the failure of Sanyo Securities "caused a default in the interbank money market" which "sent shock waves and paralysed the interbank markets in the weeks that followed". A determined reader could call that an unmanaged cascade in miniature. It is addressed criterion by criterion below rather than dismissed.

---

## Evidence

Fetched 2026-08-20, content-addressed in `../../../research/snapshots/INDEX.md`:

- [Radelet and Sachs, "The East Asian Financial Crisis: Diagnosis, Remedies, Prospects", Brookings Papers on Economic Activity 1:1998](https://www.brookings.edu/wp-content/uploads/1998/01/1998a_bpea_radelet_sachs_cooper_bosworth.pdf) -- snapshot `sha256:6941dd9dbba06e62b2c98777a31bc8fba542fd065ef85bf26748dfc6a6a09f98`. Peer-discussed BPEA article; the crisis-chronology standard.
- [Radelet and Sachs, "The Onset of the East Asian Financial Crisis", NBER chapter](https://www.nber.org/system/files/chapters/c8691/c8691.pdf) -- snapshot `sha256:649ac7f1966c6b2a41aae85db2ca25c7e54a4460390e42d4770d7e66d17e5a56`. **Same authors as the BPEA piece; counted as a duplicate, not an independent source.**
- [Federal Reserve History, "Asian Financial Crisis"](https://www.federalreservehistory.org/essays/asian-financial-crisis) -- snapshot `sha256:714c4fa361a40de2f99f0d4ec40eb83bd79b251beb0109ac933609fa29e1902c`. Independent of Radelet-Sachs; records Korea "brought ... to the brink of default", the aim of helping "Korea avoid a disorderly default", and the creditor rollover into medium-term loans.
- [Nakaso, "The financial crisis in Japan during the 1990s: how the Bank of Japan responded and the lessons learnt", BIS Papers No. 6, 2001](https://www.bis.org/publ/bppdf/bispap06.pdf) -- snapshot `sha256:5332197c719508156e08740e2945a00958d3a0b0fc2579d8d4d761b64ceb8299`. **Sole source for the Japan side**, and a practitioner self-account by a Bank of Japan official published by the BIS -- evidence of the events and of the Bank's position on its own success, with the second element discounted accordingly.

IMF primary documents for the Korea programme were sought and are blocked to automated fetch (HTTP 403), consistent with the blocked-host weakness already registered in the citation audit. The programme's existence and December 1997 date are carried by both independent sources.

---

## Korea 1997 against the six criteria

| Criterion | Finding | Basis |
|---|---|---|
| **Scale** | **Engaged.** Multiple distinct issuers in a bounded window: Hanbo declared bankruptcy January 1997 "leaving $5.8 billion in debts"; "in the next few months, both Sammi Steel and Kia Motors faced similar difficulties", pressuring the merchant banks that had borrowed offshore to lend to the chaebol | Radelet-Sachs pp. 26-27 |
| **Instrument seniority** | **Engaged with a caveat recorded below.** The insolvencies were court-declared corporate bankruptcies and the terminal event was refusal of rollover on cross-border bank credits -- formal, senior, marketable obligations -- rather than missed coupons on public bonds specifically | Radelet-Sachs pp. 26-27, 55-56 |
| **Intervention** | **Engaged: attempted and failed.** Authorities intervened case-by-case, then "inexplicably spent down its reserves in a desperate attempt to defend the Korean won in October and November"; the sequence nonetheless ran to "Korea on the brink of default" by 24 December | Radelet-Sachs pp. 28, 55; Fed History |
| **Contagion** | **Engaged.** Chaebol insolvencies to merchant banks to systemic banking distress to currency collapse to sovereign near-default | Radelet-Sachs pp. 26-27, 55-56; Fed History |
| **Disorder** | **Engaged.** "The banks and the Korean government initially announced a standstill on debt servicing"; foreign commercial banks were pressed "to roll over their short-term credits to that country on an enforced basis" -- abrupt market closure and externally imposed resolution outside any pre-existing framework | Radelet-Sachs pp. 55-56; Fed History |
| **Persistence** | **Engaged.** January 1997 insolvencies through the December brink and the 16 January 1998 rollover agreement: not resolved within the same fiscal year by a workout | Radelet-Sachs pp. 26-27, 55-56 |

**Analogue verdict: `met`.** All six criteria engage; the holistic reading is not close. The adverse reading -- eventual management by external standstill -- is recorded above and does not alter the finding that domestic authorities attempted and failed to contain the sequence.

## Japan 1990s against the six criteria

| Criterion | Finding | Basis |
|---|---|---|
| **Scale** | **Partially engaged, once.** Sequential failures over a decade (jusen 1995-96; Sanyo, Hokkaido Takushoku, Yamaichi in November 1997; LTCB 1998), with one three-week cluster in November 1997 | Nakaso |
| **Instrument seniority** | **Weakly engaged.** One interbank default (Sanyo), "relatively small in amount"; no sequence of missed payments on public bonds or senior instruments across issuers | Nakaso, section on the failure of Sanyo Securities and the lessons-learnt discussion |
| **Intervention** | **Not engaged -- decisive.** After the Sanyo default paralysed interbank markets, the Bank "had to intervene on a large scale" and the disruption was contained; for Yamaichi "the Bank of Japan stepped in directly from the beginning" and "successfully avoided market disruption". Authorities acted and succeeded | Nakaso |
| **Contagion** | **Engaged briefly, then contained.** Three weeks of interbank paralysis; no spread into a sustained closure of any issuer class | Nakaso |
| **Disorder** | **Not engaged.** Losses ran through orderly frameworks: court reorganisation for Sanyo, the Deposit Insurance Corporation for depository institutions -- "up to March 2000, 110 deposit-taking institutions were dissolved under the deposit insurance system" -- and public funds (¥685 billion for the jusen resolution, ¥60,000 billion later for the banking system) under legislation | Nakaso |
| **Persistence** | **Not engaged in the clause's sense.** The problem persisted for a decade, but as a managed absorption, resolved episode-by-episode inside frameworks -- the opposite of a sequence outrunning its containment | Nakaso |

**Analogue verdict: `not_met`.** The November 1997 cluster is the closest approach, and it fails on the criterion the clause weights most: intervention succeeded, disorder ran through pre-existing frameworks, and the one senior-instrument default was small and contained. The rubric's own logic -- "a managed workout, even a very large one, is evidence of capacity to absorb stress" -- classifies Japan correctly *because* of the very facts a naive reading might count against it.

---

## Result against the pre-named failure conditions

| Failure condition | Outcome |
|---|---|
| 1 -- `not_met` on Korea | **Did not occur** |
| 2 -- `met` on Japan | **Did not occur** |
| 3 -- same verdict on both | **Did not occur** |

**The Clause 2 rubric discriminates on the analogue pair**, and the discrimination is criterion-resolved rather than impressionistic: Korea engages all six criteria, Japan decisively fails three including intervention, the one the clause's burden sits on.

---

## Findings

### Finding 1 -- generic-cascade discrimination: pass, within the registered limitation

The first qualitative rubric in the set to pass a paired exercise (F5's sub-clauses A and C discriminated within the F5 pair; F3-C2 now does across its own). What is validated: the six-criterion structure separates an archetypal unmanaged cascade from an archetypal managed absorption, including on a negative control that contains a genuine mini-cascade. What is not validated: everything LGFV-specific, and Clause 1.

### Finding 2 -- a watch item on the seniority criterion, recorded before it can matter

The criterion "missed payments on **public bonds**, not solely on non-standard or private-placement instruments" was the weakest discriminator on the expected-positive: Korea's cascade ran through court bankruptcies and cross-border **bank credit**, and a strict public-bond reading would have under-weighted the archetypal case. The direction of the risk is the F5-B pattern -- a counting rule strictest exactly where the event class expresses itself in other instruments first. In the PRC context, LGFV stress has historically surfaced in non-standard products before public chengtou bonds. **No change is proposed or permitted**; the criterion's anticipatory-reporting rationale stands, court-declared insolvency plausibly satisfies a seniority reading, and the clause is holistic rather than criterion-gated. Registered as a watch item against the adapter so that a future adjudication addresses the instrument-mix question explicitly rather than discovering it live.

### Finding 3 -- coverage

Clause 1's arithmetic (outturn-only rule, averaging prohibition, tolerance) was not exercised: no analogue augmented-debt series exists for these episodes and inventing one would test nothing. The compound-assembly and contemporaneity rules likewise remain covered only by the adapter's synthetic tests.

---

## Evidentiary deficiencies of this exercise

1. **Japan rests on a single source**, and a central-bank practitioner's self-account at that. Nakaso's factual chronology is corroborated nowhere in this file; his assessments of the Bank's success are evidence of a position. The F5 precedent (2012 resting on Miller alone) applies: recorded as an absence, not a consensus.
2. **Korea rests on two independent sources** (Radelet-Sachs; Federal Reserve History) plus a same-author duplicate. The three-independent-source rule for determinations is not met; this is a dry run, and the shortfall is recorded rather than excused.
3. **IMF primary documents are blocked to automated fetch** and were not obtained by other means; programme facts are carried by secondary sources.
4. **The analogue mapping is itself a judgement** -- issuer-group for province, conglomerate for financing vehicle -- made by the same author who scored the criteria. Blind scoring by episode-anonymised criteria was not attempted.

---

## Sources, full URLs

- https://www.brookings.edu/wp-content/uploads/1998/01/1998a_bpea_radelet_sachs_cooper_bosworth.pdf (snapshot sha256 6941dd9dbba06e62b2c98777a31bc8fba542fd065ef85bf26748dfc6a6a09f98)
- https://www.nber.org/system/files/chapters/c8691/c8691.pdf (snapshot sha256 649ac7f1966c6b2a41aae85db2ca25c7e54a4460390e42d4770d7e66d17e5a56)
- https://www.federalreservehistory.org/essays/asian-financial-crisis (snapshot sha256 714c4fa361a40de2f99f0d4ec40eb83bd79b251beb0109ac933609fa29e1902c)
- https://www.bis.org/publ/bppdf/bispap06.pdf (snapshot sha256 5332197c719508156e08740e2945a00958d3a0b0fc2579d8d4d761b64ceb8299)
- pipeline/adapters/F3.md (internal; the Clause 2 rubric and criteria)
- falsifiers/adjudications/dry-run/README.md (internal; the pre-registered pair and limitation)
