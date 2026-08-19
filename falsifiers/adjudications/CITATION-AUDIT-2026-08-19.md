# Citation and language audit -- Phase 5 records, 19 August 2026

An audit of the four adjudications published on 19 August 2026 (`2026/F5-A.md`, `2026/F5-B.md`, `2026/F5-C.md`, `2026/F2-C2.md`), the two log amendments of the same date, and the repository README, against the project's three standing prohibitions and its citation conventions.

This record exists because the audit found substantive defects. Publishing the audit alongside the corrections is the point: a project asserting that corrections are recorded rather than repaired has to record the corrections somewhere a reader can find them without reading commit diffs.

## Scope and method

| Check | Method | Coverage |
|---|---|---|
| Prohibited language | Case-insensitive search for `inexorab*`, `inevitab*`, `prove`/`proves`/`proved`/`proven`/`proof`, including inside quoted source material | All markdown in the repository |
| Inline-citation completeness | Every claim-bearing paragraph read against its cited URL | The four adjudications and two amendments |
| Plain-URL list completeness | Set difference between URLs cited inline and URLs listed in each file's `## Sources` section, computed both directions | The four adjudications and two amendments |
| Link integrity | HTTP status for every distinct URL, plus title inspection on a sample to detect soft 404s | 60 distinct URLs |

## Prohibited language -- clean on teleology, five judgement calls recorded

No occurrence of `inexorab*` or `inevitab*` appears anywhere in the repository other than inside the prohibition statement itself.

The prohibition as stated in `README.md` names *proves*. A full-repository sweep on `prove` / `proves` / `proved` / `proven` / `proof` returns **five substantive matches outside the prohibition statement itself**. An initial pass of this audit reported only the first of them; that undercount was found on re-running the sweep across all directories rather than only the Phase 5 records, and is corrected here. Each is examined and each is retained, with the reasoning exposed rather than the matches quietly cleared.

| Location | Text | Disposition |
|---|---|---|
| `README.md:7` | "the commit history is the **proof** of that ordering" | **Retained.** About the record's own chronology -- whether one file existed before another -- which a version-control log does settle. Not about the thesis, a falsifier, or any empirical claim. |
| `falsifiers/PRE-REGISTRATION.md:3` | "cannot specify what would **prove** it wrong" | **Retained.** Falsification language, used in the negative. The prohibition targets claims of positive demonstration; a statement about what would refute a thesis is the opposite move. |
| `papers/paper-a-measurement/S3-capability-vector.md:32` | "Munda and Nardo **prove** the incompatibility rather than asserting it" | **Retained.** A formal result in aggregation theory, where "prove" carries its mathematical sense, and the sentence's function is to distinguish proof from assertion. Nearest to the edge of the five, and recorded as such. |
| `model/IDENTIFICATION.md:95` | the estimate "later **proved** to have overstated" | **Retained.** Retrospective judgement about a historical intelligence estimate, not about this project's thesis. |
| `model/IDENTIFICATION.md:97` | declinism "repeatedly **proven** wrong" | **Retained.** Reported characterisation of Huntington's argument, used against a declinist thesis rather than for one. |

The governing-principle line in `README.md`, which had used "prove" about a substantive claim, was corrected during Phase 5 and the correction is noted in place.

**These dispositions are recorded rather than left silent**, because a reader running the same search will find the same five matches and is entitled to know they were seen and reasoned about rather than missed. A reader who thinks the distinction between proof about a record, proof in the mathematical sense, and proof about the world is too fine is disagreeing with a judgement that is now visible instead of buried. **The stricter reading -- that the prohibition should be enforced lexically with no exceptions -- is defensible and is not the one adopted**, on the ground that a lexical ban would forbid the sentence in `PRE-REGISTRATION.md` that states the project's entire method.

## Citation defects found and corrected

### 1. A load-bearing claim attributed to a source that does not state it -- `2026/F5-B.md`

The most serious finding. `F5-B.md` asserts a Politburo denominator of "24 full members **including** the 7-member Standing Committee" and attributes it to the International Department of the CPC Central Committee. Re-fetching that page shows it states a count of twenty-four and separately names the seven Standing Committee members, **without saying whether the seven are inside the twenty-four**, and without enumerating the twenty-four by name.

The two readings give different thresholds -- `ceil(0.15 * 24) = 4` against `ceil(0.15 * 31) = 5` -- so the clause was not merely imprecisely cited but imprecisely grounded on the quantity the whole determination turns on.

The inclusive reading is correct and is now supported by sources that state it in terms rather than by inference. Corrected by Amendment 1 to `2026/F5-B.md`, which also reverses the recorded standing of the two denominator sources: the enumeration establishes the count and the primary Party organ corroborates the total only.

**This is the defect class the audit was worth running for.** It would have survived any reader checking that the citations resolve. It fails only against a reader checking what the cited page says.

The same ambiguity was subsequently found in the 1976 sources, where an official page gives "9 Politburo Standing Committee members, 21 Politburo members, and 4 alternate members" -- also capable of an additive reading, also resolved only by an enumerated name list. Recorded in `dry-run/1976.md`.

### 2. An unnamed entity in a counted quantity -- `2026/F5-B.md`

The record adopted a Congressional Research Service formulation referring to "two members under investigation" without naming the second. Now named as Zhang Youxia and Ma Xingrui, with Liu Zhenli explicitly ruled out as a Central Military Commission member who is not a full Politburo member. Corrected by Amendment 1 to `2026/F5-B.md`.

### 3. Date imprecision -- `2026/F5-B.md`

"Elected 22--23 October 2022" corrected to 23 October 2022, the date of the first plenary session. Not load-bearing.

### 4. Source-list mismatch -- `2026/F5-B.md`, `2026/F5-C.md`

The inline citations to the Air University China Aerospace Studies Institute paper carried a `?ver=` query string that the plain-URL lists dropped, so the two forms did not match. Reconciled to the inline form, which is the one that resolves.

### 5. Uncited entries in a plain-URL list -- `2026/F2-C2.md`

Two URLs appeared in the source list without any inline citation. Both are now cited inline at the points they support -- a Bank of England Financial Stability Report in the source-standing table, and a Congressional Budget Office Director's testimony at the sentence recording that no located CBO product uses the phrase "fiscal crisis".

### 6. Missing plain-URL lists -- `../log/2026/F5.md`, `../log/2026/F2.md`

Both amendments carried inline links but no plain-URL section, against the convention that every file ends with one. A "Sources for Amendment 1" subsection has been added to each.

## Link integrity -- and the limit of the check

Of 60 distinct URLs, **39 return HTTP 200 and no dead link was found**.

Every non-200 response is a host that blocks automated requests rather than a missing page: Reuters returns 401 on eight URLs; the Congressional Budget Office, congress.gov, the International Monetary Fund, the New York Times, loc.gov and airuniversity.af.edu return 401 or 403. Soft-404 checks on a sample passed -- jamestown.org, lowyinstitute.org, english.news.cn, prcleader.org, journalofdemocracy.org, eng.mod.gov.cn and idcpc.org.cn all returned the expected page titles rather than generic error pages.

**The limitation has to be stated: a mechanical status check cannot distinguish a blocked page from a dead one.** The eight Reuters URLs are the largest single block, and their content is asserted in the records on the strength of having been fetched during research rather than on the strength of this check. A reader without an equivalent fetch path has to take those on trust, and that is a real weakness in a project whose entire claim is auditability. It is recorded rather than glossed.

## What the audit did not check

- **Whether each cited page still says what it said when fetched.** Content drift is undetected by status codes. No archival snapshots were captured at fetch time, which in retrospect is a gap in the project's own method rather than in this audit.
- **The accuracy of quoted material against the published version** where a paper was read via a mirror. `dry-run/1976.md` relies on a scholarly paper read through a partisan archive and records that the mirror was not checked against the journal of record.
- **Peer-reviewed status of every cited institution.** Several load-bearing sources are analytical commentary from research institutions rather than peer-reviewed scholarship, and are labelled as such in the individual records.

## Outcome

No determination changed. Six citation defects corrected by appended amendment. Five language matches examined and retained with reasons recorded, after an initial undercount in this audit's own first pass was found and corrected. One method gap identified for the project as a whole: **snapshot every cited page at fetch time**, which is registered as an open item in the repository README rather than retrofitted, since retrofitting snapshots now would capture today's content and imply it was verified on the original date.

## Sources, full URLs

- https://www.idcpc.org.cn/english2023/tjzl/cpcjj/leadershipof20thCentralCommittee/
- https://orcasia.org/pages/20cc/overview
- https://www.gssc.lt/wp-content/uploads/2022/11/National-Congress-of-the-CPC.pdf
- https://chinahorizons.eu/images/docs/policy_brief/DWARC_Policy_Brief_The_20th_Congress_of_the_CCP_FINAL.pdf
- https://www.reuters.com/world/china/chinese-politburo-member-ma-xingrui-under-investigation-by-anti-graft-watchdog-2026-04-03/
- https://www.reuters.com/world/china/china-investigating-senior-military-officials-zhang-youxia-liu-zhenli-says-2026-01-24/
- https://en.wikipedia.org/wiki/20th_Central_Committee_of_the_Chinese_Communist_Party
- https://www.airuniversity.af.edu/Portals/10/CASI/documents/Research/Other-Topics/2026-07-13%20PLA%20Corruption.pdf?ver=3FCdY-htIjQJMdbipAVSgg==
- https://www.bankofengland.co.uk/financial-stability-report/2025/july-2025
- https://www.cbo.gov/publication/62207
- https://www.gov.cn/test/2007-08/28/content_729620.htm
