# INTAKE FORM — the six-field brief, dual-mode

Fill every field; unknown → write **unknown** and treat per its gate (never guess). Machine contract: schemas/intake.schema.json.

## Field 1 — SOURCE & rights *(Gate 0)*

| Question | Answer |
|---|---|
| What is the base image? (own photo / own model or drawing export / licensed item / internet screenshot / other) | |
| Date created/captured | |
| Photographer / data provider | |
| Licence or permission status (confirmed where? host/licensor page) | |
| Original file ID / revision | |
| If internet-sourced: creator, item page, URL, date, licence, conditions | |

**Verdict:** own / licensed / cleared → eligible · unknown → **do not upload** (alternatives: own-words aesthetic · own reference · request permission · verifiable licensed substitute).

## Field 2 — VIEW & source-of-truth

| Question | Answer |
|---|---|
| View type (plan / elevation / section / eye-level / aerial / perspective) | |
| Camera locked? North, scale, coordinate system known? | |
| Dimensions or model revision **from actual documents**? (a PNG carries none) | |

## Field 3 — LOCKED (the preserve list raw material)

List features that must survive, each marked **M** (measured constraint, from documents) or **V** (visual cue, from pixels): bay/window/door counts and positions · footprint edges · roof profile · entrance · circulation · camera/viewpoint · the projection itself · legal annotations (radius ring, scale bar, hatching).

## Field 4 — ALLOWED CHANGE

One bounded change: a material · a facade zone · lighting · vegetation concept · a massing **option**. Not "make it better." A proposed new element is not the existing condition and must never silently appear as such.

## Field 5 — REFERENCE ROLES

`A = my structure/camera` (model export, sketch, section) · `B = cleared appearance only` (materials/light/palette — never a geometry source) · `C = edit area` (mask/layer). If the tool lacks a role slot → change tools or drop that reference.

## Field 6 — AUDIENCE & evidence status

internal mood study / client concept / public / approval package · required caption/credit · who reviews discrepancies. A render for an early conversation must not imply code, drainage, structure, accessibility or cost is solved.

## Context flags

School/competition context? (→ disclosure gate G4) · Deadline? · Provider access available? · Has the base been measured before? (IoU/SSIM baseline?)

---

## QUESTIONNAIRE MODE — for operators without vision

This operator **cannot see images**. When a photo is supplied, ask the user (merge into ≤ one round where possible):

1. What kind of image is it — photo, screenshot, render, sketch, satellite/site view? Is there visible browser/UI chrome or compression (JPEG artifacts, tiny text)?
2. Whose is it — did you make it, license it, or find it? If found: where, and do you know the creator/licence?
3. Does it carry watermarks, credits or attribution marks? (These are never removed — G2.)
4. Roughly what does it show — building/room/object, which view (front/elevation/plan/aerial/angle), what's the main subject?
5. What must survive the re-imagination — counts, edges, entrance, layout, camera angle? Be specific; these become the preserve list.
6. What exactly may change — and is it ONE bounded change?
7. Where will the result go — personal study, plate/coursework submission (→ disclosure), client, public?
8. Any deadline or provider preference/access?
9. Is there a better base available — the original model export or a cleaner capture? (Screenshots degrade invisibly; a clean export is worth more than any prompt.)
10. If another angle is needed later — do you have the model/source to re-export, or should the plan include a 3D reconstruction route?

**Rule:** answers to Q4/Q5 are the user's assertions — record them as such (`[O] user-described`), never as verified visual fact.
