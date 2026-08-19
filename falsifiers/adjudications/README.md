# Adjudication records

Written determinations for every clause that cannot be evaluated by arithmetic alone. Governed by `pipeline/adjudication.md` in full.

## What is in this directory

```
adjudications/
  <year>/                 One file per adjudicated clause, for that evaluation year
```

Each file corresponds to one `adjudication` record as specified in `pipeline/adjudication.md`. The YAML block at the head of each file is the record; the prose below it is the `adverse_case` and `reasoning` fields written out at length, because compressing them into YAML scalars would make them unreadable and unreviewable.

## Naming

`<falsifier_id>-<clause>.md`

Sub-clause identifiers follow the adapter specification. `F5-A.md` is F5 Sub-clause A. `F2-C2.md` is F2 Clause 2, the qualitative clause. No file is created for a quantitative clause, because the framework prohibits adjudicating anything computable.

## Reading order within a file

The order is deliberate and is the order in which the record was written:

1. The record header
2. **The adverse case** -- the strongest available argument that the clause **is** met
3. The reasoning
4. The determination
5. Sources, with standing and direction
6. Contestability
7. Amendments

The adverse case appears before the reasoning because Rule 2 requires it to be **written** before the determination. Presenting it afterwards would let a reader assume it was assembled to be knocked down. That assumption cannot be excluded by file ordering alone, and a reader is entitled to hold it, but the ordering at least matches the drafting sequence claimed.

## Freezing

Published adjudications are frozen. Corrections append as dated amendments carrying their own reasoning. Where a determination changes, both the original and the amendment remain visible in the same file.

## 2026

| Record | Clause | Determination | Contestable |
|---|---|---|---|
| `2026/F5-A.md` | Extra-constitutional leadership transfer | `not_met` | No |
| `2026/F5-B.md` | Purge exceeding 15 percent of the Politburo | `not_met` | Yes |
| `2026/F5-C.md` | Military intervention in succession | `not_met` | Yes |
| `2026/F2-C2.md` | Absence of a debt crisis | `met` | Yes |

Two of the four are recorded as contestable. That is not a hedge. F5-B is one member from its threshold and rests on a disputed member count; F5-C rests on a distinction between civilian-directed military purging and military intervention that the adjudication itself argues is doing heavy lifting. A reader who reaches the opposite determination on either has grounds available in the record.
