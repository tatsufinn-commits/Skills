# QA GATE — decidable checks and the reject-drift rule

**Source:** prompt kit "Independent QA & publication gate" · student workflow step 6. A designer records `PASS / FAIL / UNVERIFIED` per gate with actual evidence. **"Cannot tell from photo" = UNVERIFIED, never PASS.** A self-critique by the same image model is a discrepancy *lead*, not independent verification.

## The gate table

| Gate | Compare against — reject/flag if… |
|---|---|
| **Rights & attribution** | Actual image owner, platform/item terms, client permission, intended audience. Rights missing → STOP. Original source credits preserved + concept disclosure added. |
| **Visual invariants** | Source and proposal side-by-side at identical crop: roof, bay/opening/floor counts, facades, neighbouring structures, camera. Any unapproved change = FAIL. |
| **Spatial/functional logic** | Entrances, road/footpath connections, parcel edges, turning, circulation, adjacency, levels — checked **against survey/site plan**, not just pixels. Mismatch or missing data = FAIL/UNVERIFIED. |
| **Drawing/model correspondence** | Footprint, spans, materials, grid, elevations, code-sensitive elements — against original DWG/RVT/IFC and signed schedules. A pretty render cannot pass this by itself. |
| **Cross-view** | Same model revision/camera list; opposite elevations/plan aligned; opening and balcony counts, roofline, ground plane. Conflicting views = FAIL. |
| **Outside-edit pixels** | If immutable pixels are required: calculate/inspect the non-edited region and restore the original layer via compositing; mask fidelity is not guaranteed. |
| **Release label** | *"Concept illustration — AI-assisted; not a survey/as-built or construction document"* on the presentation sheet, credited original separate from the proposal. Clear communication, not a licence substitute. |

## Reject-beautiful-failure checks (workflow step 6, side-by-side with the original)

a. the intended change **is present**;
b. floor/window/bay count, doors, roof, circulation and camera relations remain correct where required;
c. unselected areas have not drifted;
d. people, context, symbols and shadows are plausible;
e. another view agrees with the **same original model** if claimed.

A wrong preserved opening is a **FAIL**, not an aesthetic trade-off. Validate dimensions/site conditions in the original CAD/BIM/GIS or project records — **never the AI image**.

## The reject-drift rule (binding)

If a LOCKED invariant drifted: **reject the output; redo the operation in an authoritative CAD/photo/mesh editor, or attach better measured/multi-view inputs.** Do not re-prompt "keep it exactly the same" at a drifted output — adjectives do not lock pixels; the authority ladder says the structural channel wins.

## Optional critique pass (separate multimodal reviewer, T01-class)

> Compare Image A (unmodified authorized source) and Image B (AI-assisted concept) only on VISIBLE differences. Table: feature; unchanged/changed/occluded; source A location; concept B location; why it matters; which drawing, GIS layer or site record would independently verify it. Do not estimate lengths, setbacks, structural capacity or code compliance from pixels — mark any such point UNVERIFIED. Flag every new door, floor, road, water feature or building and any inconsistent cross-view element.

## Programmatic pre-check

`python3 evals/grader.py <worksheet>` — checks the **configuration** (C1–C6 core: completeness, explicitness, law, QA decidability, traceability, disclosure + F11 tool settings, conditional on PHOTO: yes — seven result rows with a photo, six for text-only). Grader PASS ≠ image quality; it means the package is complete, explicit, lawful, decidable, traceable and disclosed. Image quality stays `[N]` until the fidelity harness measures a run.
