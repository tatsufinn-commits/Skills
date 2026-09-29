# @reimagine — Configuration Worksheet V2-W · 2026-09-29

## Brief
TASK: Re-imagine the dated east-elevation render with a timber-cladding mood while keeping the six bays, entrance, roofline and camera
CARD: A02
PROVIDER: Reference-faithful editor (Kontext class) — img2img 0.45, model version confirmed in live UI
PHOTO: yes
PHOTO_SOURCE: own
SCHOOL: yes
STYLE_AUTHORITY: Movement/palette rung — warm timber rainscreen language; no named architect
AUDIENCE: coursework plate
DEADLINE: 2026-10-03

## Paste text
```text
Create ONE clearly conceptual architectural visual from the authorized input. Image 1 is
the BASE: my dated east-elevation render, model revision A. It controls the visible
arrangement, camera, silhouette and documented relationships. Keep these documented
features legible and in their original relationships: the east elevation at eye level
with the same camera and framing; six facade bays in count and position; the entrance
location; the roofline silhouette; the ground line. Only reinterpret the selected
facade zone: a warm timber rainscreen palette as a finish study. Use the same viewpoint
and broad framing as Image 1. Show one variation. Treat unspecified site facts,
dimensions, structure, code compliance and hidden conditions as UNKNOWN. Do not add
labels, measurements, logos or a claim that this is a photograph of completed work. The
image is a concept study, not a survey, construction document, or as-built.
```

## Preserve list
- East elevation view at eye level — same camera and framing as the dated render (projection invariant)
- Six facade bays — count and positions
- Entrance location and door
- Roofline silhouette and ground line

## Alter list
- Cladding mood across the selected facade zone: warm timber rainscreen palette (finish study only — not a specification)

## Tool settings
- Image 1 = A (geometry/base): east-elevation render rev A — attached as the edit base
- No style reference attached (palette described in words — rung 2 authority)
- img2img denoise 0.45 (restyle band 0.35–0.55); selection limited to the facade zone; seed recorded if exposed; original kept untouched

## QA gate
- [ ] Overlay source and output at identical crop: verify six east facade bays unchanged in count and position
- [ ] Compare roofline silhouette and entrance location against the dated render
- [ ] Confirm no new floors, balconies, openings or structural members appear
- [ ] Inspect sky, ground and adjoining surfaces for drift outside the selected zone
- [ ] Count window mullions against the original; any change = FAIL and redo in editor
- [ ] Validate dimensions in the model file (rev A), never from the generated image
- [ ] Confirm caption and attribution placed outside the generative pass
REJECT-DRIFT RULE: on drift of any LOCKED invariant — reject, redo in an authoritative CAD/photo editor or attach better measured inputs; never re-prompt adjectives at a drifted output.

## Disclosure
Caption on the presentation sheet: "AI-assisted concept visualization based on my 2026-09-28 model render (rev A); material/light reimagined; building dimensions and site context must be checked against the original drawings."
Reproducible attribution: base = own model render rev A (2026-09-28); prompt description = preserve-list timber re-clad concept study via @reimagine card A02; skill source: https://github.com/tatsufinn-commits/Skills accessed 2026-09-29.

## Rationale
RATIONALE: Card A02 (facade-region refinish) because the request is a finish-mood study over one selected zone with all geometry locked. Reference-faithful editor routed per the provider matrix, img2img 0.45 inside the restyle band; no ControlNet channel in this workflow, so the preserve-list text is the only geometry defense — risk flag: text is the weakest signal channel, QA overlay checks are mandatory, and the card's exact wording is [N] (corpus-untested). Provider facts decay-checked (2026-12-28). Configuration graded; image quality not measured — runtime tranche pending.

## Log
- 2026-09-29 · input: east-elevation-render_revA.png · reference-faithful editor (version per live UI) · card A02 · not measured (runtime tranche pending) · worksheet emitted
