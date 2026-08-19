# Snapshots -- content-addressed fetch records

**Why this exists.** The citation audit (`../../falsifiers/adjudications/CITATION-AUDIT-2026-08-19.md`) registered a method gap: no page was archived at fetch time, so content drift between fetch and reading is undetectable, and blocked hosts cannot be distinguished from dead pages by a later auditor. The gap was deliberately not retrofitted, because capturing a snapshot now would imply verification on the original fetch date.

**The rule, in force from 2026-08-20.** Every URL fetched for new work is snapshotted at fetch time via `snapshot.py`, which stores the exact response bytes under `store/<sha256>.<ext>` and appends the URL, hash, byte count and UTC timestamp to `INDEX.md`. A citation to a snapshotted source can name its hash; a reader can verify that the stored bytes carry that hash, and can compare the live page against the stored one.

**What this does not do.** It does not verify that the fetched page is authentic or accurate -- only that the text relied on is the text preserved. Citations from before 2026-08-20 remain unsnapshotted; the weakness stands as recorded and applies to them in full.

Run `python3 snapshot.py --selftest` to check the hashing.

## Sources

- ../../falsifiers/adjudications/CITATION-AUDIT-2026-08-19.md, section on the snapshot gap (internal)
