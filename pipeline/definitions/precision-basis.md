# Declared precision basis

Resolves the first open item in `pipeline/definitions/frontier-compute.md`. Governs rule **R004**.

---

## Why this is not a detail

Accelerator throughput is advertised at whichever numeric format flatters the part. Successive architectures have added progressively lower-precision formats, and each addition roughly doubles the headline number without any change in the underlying silicon's capability at higher precision.

The spread on a single current part illustrates the scale of the problem. One flagship accelerator is specified at approximately **2,250 TFLOPS** dense FP16, **4,500 TFLOPS** dense FP8, and **9,000 TFLOPS** dense FP4, with sparsity-assumed figures doubling each of those again. A ratio built from headline numbers would therefore measure disclosure convention rather than capability, and would drift as vendors adopt new formats at different times.

---

## Committed basis

**Dense BF16/FP16 tensor throughput.**

This follows established analytical practice, in which peak accelerator throughput is taken at dense BF16/FP16 unless a specific training run is documented as having used a lower precision. Adopting the existing convention rather than inventing one is deliberate: it makes the figures comparable to published work and removes a degree of freedom.

Two further specifications:

- **Tensor throughput**, not non-tensor. Published hardware datasets record these as distinct fields, and tensor units are what frontier training uses. Conflating them understates post-2017 hardware substantially.
- **Dense**, never sparsity-assumed. Structured sparsity conventionally doubles the quoted figure, but real workloads do not exhibit consistently sparse activations, so the sparse number is a ceiling rather than a capability.

---

## Conversion table

Applied where a source publishes only at another format. Ratios are the conventional architectural relationships, not measurements.

| Source format | Multiplier to dense BF16/FP16 | Confidence |
|---|---|---|
| Dense BF16/FP16 tensor | 1.0 | Exact, no conversion |
| Dense FP8 | 0.5 | High -- consistent 2:1 across parts |
| Dense FP4 | 0.25 | Moderate -- fewer parts, shorter history |
| Dense INT8 | 0.5 | Moderate -- treated as FP8-equivalent |
| Any sparsity-assumed figure | 0.5 applied first, then the format multiplier | High |
| Non-tensor FP16 | **No conversion permitted** | Excluded |
| FP32, TF32, FP64 | **No conversion permitted** | Excluded |

Where no conversion is permitted, the device is **excluded** and the exclusion is logged. An excluded device is not estimated at, and does not silently drop out of, the aggregate.

The FP4 multiplier carries lower confidence because the format is recent and the relationship rests on fewer observations. Its use is flagged.

---

## Interaction with the factor-of-eight window

`frontier-compute.md` defines frontier-capable as within a factor of eight of the highest-throughput device in volume production, on this basis.

Worked at present values: a leading part at approximately 2,250 TFLOPS dense BF16 implies a floor of about **281 TFLOPS**. A prior-generation flagship at roughly 312 TFLOPS BF16 therefore falls **inside** the window.

### A calibration discrepancy, recorded

`frontier-compute.md` justified the factor of eight as spanning "roughly two hardware generations." On the worked values it spans closer to **three**, admitting hardware released around four years before the current flagship.

The factor is **not** changed. It was pre-registered, and adjusting it on discovering that it is more permissive than described would be exactly the behaviour the pre-registration exists to prevent. What changes is the description: the window is wider than the original justification claimed, and the sensitivity settings at factors of four and sixteen become more important as a result, since the committed setting is nearer the permissive end of its own range than intended.

A reader who thinks a factor of four is the better boundary will find that verdict reported alongside the committed one.

---

## Source hierarchy for device specifications

1. Curated hardware datasets recording precision-disaggregated fields, preferred because the disaggregation is explicit
2. Vendor technical documentation, where the format and sparsity assumption are stated unambiguously
3. Secondary comparison compilations, cross-check only

Secondary compilations are ingested but do not feed the aggregate, because they frequently mix formats within a single table.

### An observed source defect

At least one secondary compilation consulted during specification states a flagship FP4 figure of "99,000 TFLOPS (18,000 TFLOPS sparse)" while stating elsewhere in the same document that the part delivers 9 PFLOPS dense and 18 PFLOPS sparse FP4. The first figure is internally inconsistent with the second and with the sparse-doubling convention.

Recorded because it is a concrete instance of why tier-3 sources are excluded from the aggregate, and because an implementer who encounters the erroneous figure should recognise it rather than ingest it.

---

## Tests

1. Dense FP8 input converts at 0.5 and records the conversion in the derivation record.
2. A sparsity-assumed FP4 figure applies both multipliers, yielding 0.125.
3. A non-tensor FP16 figure is excluded, with a log entry.
4. An FP32-only device is excluded, with a log entry.
5. An FP4-converted device carries a low-confidence flag.
6. The factor-of-eight floor recomputes when the leading part changes.
7. Excluded devices are enumerable from the run artifact.

Test 7 matters because exclusions bias the aggregate downward, and a reader must be able to see how much was excluded rather than trusting that it was immaterial.

---

## Remaining open items in `frontier-compute.md`

Unaffected by this file:

- Shipment and utilisation estimation method, and its error characterisation
- Whether a bilateral construction is available from published sources
- The intermediated-access band, still with no committed estimation method

F8 cannot emit a published verdict until the first of these is resolved.
