# Architectural image-to-reimagination prompt kit
**Session / author:** S012 · Arena AI (Agent Mode). **Date:** 2026-09-29 (Asia/Singapore). **Mode:** @Autopilot, closing **@Review** leg (Brain-first). **Commissioned task:** research photo-based architectural re-imagine prompts for GIS/Google/location maps, Revit/AutoCAD, buildings/structures, other providers and relevant studies/field reports. **Companion:** [full evidence report](2026-09-29_architectural-image-reimagination-research.md) and source register `Brain/short_term/notes/2026-09-29_arch-image-source-register.md`. **Important:** These are **research-derived, untested templates**—not evidence of dimensional accuracy, a map licence, an edit-model benchmark, or a buildable design.

## Short answer
**[N]** (source: [P02](https://help.autodesk.com/cloudhelp/2026/ENU/Revit-DocumentPresent/files/GUID-A5E61A08-9635-44D0-93CA-75C15282119B.htm), [P04](https://www.usgs.gov/faqs/what-a-digital-orthophoto-quadrangle-doq-or-orthoimage), [P17](https://www.cambridge.org/core/journals/proceedings-of-the-design-society/article/generative-aipowered-parametric-modeling-and-bim-for-architectural-design-and-visualization/A76987B083B87FA9E8579B1DCA532A0B), [P21](https://www.mdpi.com/2079-8954/14/7/771)) {decay: 2027-09-29} For architectural work, treat an input photo/map/CAD screenshot as a **reference with declared roles and limits**, not as an automatically measured model. Specify **what stays, what may change, and what is unknown**; use the image model for a bounded visual experiment, then validate it against the **original survey/GIS/CAD/BIM**, not the generated image. A crisp render is not a measured site plan. For consistency over several views, return to the *same approved 3D/BIM model* to produce each view rather than rely on repeated prose. [R] (source: [P22](https://arxiv.org/abs/2503.03068), [P21](https://www.mdpi.com/2079-8954/14/7/771)) {decay: none}

### First gate: is the source image even eligible?

| Source | Before putting pixels into a third-party image tool |
|---|---|
| **Your own photo, sketch, Revit/AutoCAD model/view** | Verify photographer/firm/client authority, contract/NDAs, personally identifying information, cloud-processing policy, and permission to publish the output; *owning a copy is not necessarily owning every reuse right* [N] (source: [S12](https://www.ribaj.com/intelligence/copyright-in-the-age-of-ai/), [S18](https://www.nortonrosefulbright.com/en/knowledge/publications/4e9b05b9/infringement-risk-relating-to-creation-and-use-of-the-output-of-a-generative-ai-system)) {decay: 2027-09-29}. |
| **ArcGIS Online / Esri-hosted basemap or third-party layer** | Check **each item/layer's** terms plus static-map rules and attribution; listed static report uses are **not automatic AI-upload/derivative permission**. Do not build an unattended imagery scraper [N] (source: [P14](https://doc.arcgis.com/en/arcgis-online/reference/static-maps.htm), [P15](https://doc.arcgis.com/en/arcgis-online/reference/access-use-constraints.htm), [P16](https://doc.arcgis.com/en/arcgis-online/reference/display-copyrights.htm)) {decay: 2026-12-28}. Prefer owned/licensed geodata and a basemap cleared for the intended method. |
| **Google Maps, Earth, Street View, satellite view, or Map Tiles API** | **STOP until the exact product and use are checked.** Google's Geo Guidelines distinguish permissible annotation from significant alteration and prohibit Google Earth content for **commercial/promotional** use; a “simulation” caption does not waive that ban. Map Tiles API is a **separate** service whose policy disallows non-visualization image analysis/machine interpretation. Do not generalize the Tiles rule to *all* Maps uses, or assume a Maps screenshot may be sent to an AI editor [D] (source: [P12](https://about.google/intl/en-GB_ALL/brand-resource-center/products-and-services/geo-guidelines/), [P13](https://developers.google.com/maps/documentation/tile/policies)) {decay: 2026-12-28}. If rights are uncertain, create a new schematic from independently licensed map data; do not upload the Google imagery. |

**[N]** (source: P12–P16, [S15](https://www.washington.edu/news/2021/04/21/a-growing-problem-of-deepfake-geography-how-ai-falsifies-satellite-images/)) {decay: 2027-09-29} Keep the original geographic reference and any required provider attribution **separate and intact**; label a generated *proposal layer* as simulation rather than letting it masquerade as imagery. This is a communication safeguard, **not** a cure for a prohibited licence. No particular source image has been cleared in this session. Consult the relevant rightsholder and local professional/legal advisers for a real project.

## The input brief: six fields to fill before writing an art prompt

1. **SOURCE & rights:** `[own photo / licensed aerial / original GIS site diagram / Revit or CAD export]`, date, photographer/data provider, allowable edit/upload/publication, original file ID. If the answer is unknown, **do not upload**. [N] (P12–P16,S12) {decay: 2026-12-28}.
2. **VIEW & source-of-truth:** `plan/elevation/eye-level/aerial`, camera locked or not; north, scale, coordinate reference system, dimensions and model revision *only if supplied from actual documents*. A standalone PNG does not carry authoritative BIM objects or GIS feature coordinates [N] (source: [P01](https://doc.esri.com/en/arcgis-pro/latest/help/sharing/overview/export-a-map-or-layout.html), P02, [P03](https://help.autodesk.com/cloudhelp/2022/ENU/AutoCAD-Core/files/GUID-1A2C1CB7-2323-456E-AF23-1FBA900E5EFC.htm)) {decay: 2027-09-29}.
3. **LOCKED:** observed/signed-off features to preserve, e.g. footprint, public access route, bay count, window/door position, roof edge, structural grid, adjacent roads. Distinguish a *measured constraint* from a *visual cue*. [N] (P17,P21) {decay: 2027-09-29}.
4. **ALLOWED CHANGE:** one bounded material, façade zone, lighting, vegetation concept, or massing **option**. A proposed new wall or window is **not** the existing condition and must not silently appear as such. [N] (P21,[S07](https://www.archdaily.com/1034327/the-plan-and-the-prompt-how-ai-is-rewiring-design-and-practice)) {decay: 2027-09-29}.
5. **REFERENCE ROLES:** `Image 1 = geometry/base`; `Image 2 = style only`; `Image 3 = annotated edit zone / approved mask`, if the selected tool supports these. Do not copy a style reference's floor plan or building shape. [N] (source: [P07](https://docs.bfl.ai/guides/prompting_guide_flux2), [P10](https://helpx.adobe.com/photoshop/desktop/create-open-import-images/create-images/use-reference-images-for-consistent-results.html), [P19](https://blog.iaac.net/controlled-creativity/)) {decay: 2026-12-28}.
6. **AUDIENCE & evidence status:** `internal mood study / client concept / public / approval package`; required caption/credit; who reviews discrepancies. A render for an early conversation should not imply that code, drainage, structure, accessibility or cost is solved [N] (P21,[S11](https://www.ribaj.com/intelligence/ai-augmented-architectural-practice-from-the-inside/),[S16](https://archinect.com/forum/thread/150521508/i-feel-like-ai-use-is-unethical-for-architects)) {decay: 2027-09-29}.

## Copy-paste master prompt (for an eligible reference-image **edit**, not a design approval)

Replace all brackets with **known** inputs. Remove unknown claims instead of guessing. This template is a specification for a visual generator; **it cannot enforce the preservation lines by itself**. Select/mask or composite separately when pixels must be immutable. [N] (source: [P05](https://developers.openai.com/api/docs/guides/image-generation), [P06](https://ai.google.dev/gemini-api/docs/image-generation), [P21](https://www.mdpi.com/2079-8954/14/7/771), [S13](https://community.adobe.com/questions-712/changes-to-generative-fill-1174820)) {decay: 2027-09-29}

```text
Create ONE clearly conceptual architectural visual from the authorized input.
Image 1 is the BASE: [describe actual source and viewpoint]. It controls the
visible arrangement, camera, silhouette and documented relationships.
Image 2, if attached, is STYLE ONLY: [palette/material/lighting cue]; do not
use it as a source of geometry, location, factual context or a specific design.

Keep these documented features legible and in their original relationships:
[protected geometry/adjacency/circulation; list concrete observable features].
Only reinterpret [one precisely identified area, surface or design option].
The proposed visual direction is [material, light, planting/scene, stage].
Use the same viewpoint and broad framing as Image 1. Show one variation.

Treat unspecified site facts, dimensions, structure, code compliance and
hidden conditions as UNKNOWN. Do not add labels, measurements, logos, map
attributions or a claim that this is a photograph of completed work.
The image is a concept study, not a survey, construction document, or as-built.
```

**For a provider whose output is image-only:** place truthful credits, measured labels and the concept-status caption **outside the generative pass** in layout/GIS/presentation software; do not rely on generated text for legal attribution or a scale bar. [N] (P01,P04,P12–P16) {decay: 2027-09-29}

### Four architecture-specific versions

**A. Existing building photo → non-structural façade concept.** Applicable only to an image the team may edit/upload. Put the remodelled proposal next to the unchanged photo, with time/source and status labels supplied outside the image. [N] (P21,S07,S12) {decay: 2027-09-29}

```text
Use the authorized original photograph as the camera, streetscape and
existing-building reference. Explore only [the approved cladding bay/porch/
shading screen zone] in [chosen visual material palette]. Keep the visible
building outline, roof pitch, number and position of existing openings,
sidewalk and neighbouring-building silhouettes legible as in the source.
Show one daytime concept with realistic but explicitly unverified materials.
Do not imply a new column, load-bearing element, permit approval, heritage
consent, or construction that the source documents do not establish.
```

**B. Own/licensed GIS site diagram → *concept layer*, not regenerated survey.** Prefer to draw an **actual** footprint/boundary in GIS/CAD and use AI only on a separate visual/vignette; if the model is asked for a plan-like study, compare it back to the original data. A basemap whose licence is unclear **must not** be included in the model upload. [N] (P01,P04,P12–P16,P21,S15) {decay: 2027-09-29}

```text
From this rights-cleared, authored site diagram (NOT a third-party Google or
uncleared ArcGIS screenshot), create one illustrative landscape/massing
concept. Keep the provided north-up visual orientation, site-boundary
silhouette, existing roads and access connections recognisable. Restrict any
proposed building mass to [designated zone] as a conceptual option; express
[planting / pedestrian-space concept] only in [designated zone]. Leave survey
coordinates, setbacks, contours, road widths and map credits to the original
GIS/CAD document. This output is a proposal diagram, not new site imagery.
```

**C. Revit/AutoCAD view → material/lighting pass.** The unaltered signed-off model/drawing remains authoritative; a rasterized export is not editable geometry. For orthographic linework, keep the original CAD dimensions/annotations as a separate overlay rather than regenerating text. [N] (P02,P03,P17,[S01](https://www.mdpi.com/2673-8945/5/4/94)) {decay: 2027-09-29}

```text
Image 1 is a rights-cleared export from model/drawing revision [ID], view
[front elevation / named 3D camera]. The source model, not this render, defines
[verified floor count, roof edge, window-bay count, entrance side]. Render a
conceptual [material/lighting] variation confined to [defined façade region].
Hold the view, massing silhouette, structural grid cues, door and window
positions as visible in Image 1. Do not invent extra floors, cantilevers,
openings, dimensions, services or an unmodelled supporting structure.
Leave title block, labels, grid/dimensions and approval status to CAD/BIM.
```

**D. Structure photograph / conservation-sensitive exterior → surface-only study.** Do **not** imply a load-path alteration or verified restoration technique from pixels. If archival, check photographer and heritage rights before use. [N] (P18,P21,S12) {decay: 2027-09-29}

```text
Use the rights-cleared image solely to explore [reversible shade device / finish
palette / night-time lighting] on [named non-load-bearing zone]. Retain the
visibly documented columns, beam rhythm, spans, roofline and public entrance.
Treat hidden reinforcement, foundation, historic fabric, fire strategy and
structural adequacy as unknown. The result is a reversible visual hypothesis,
not a restoration drawing or engineer's instruction.
```

**Multi-view option:** Start from one approved model revision, export named cameras, and run the same bounded edit separately for each view. Re-use a **style** reference only to harmonize visual language; compare balcony counts, openings, ground levels and roof geometry across all images and the model. A common seed is not cross-view proof. [N] (source: [P22](https://arxiv.org/abs/2503.03068), [P19](https://blog.iaac.net/controlled-creativity/)) {decay: 2027-09-29}

## Provider translation notes — controls are *options*, never fidelity warranties

| Tool | How to adapt the prompt without promising something the product does not do |
|---|---|
| **OpenAI image editing / Gemini image editing** | Provide an authorized base image and a concise *edit* instruction; use a supported mask or iterative revision when available. Check the selected API/app version. Gemini image-input support says nothing about Google Map permissions. [N] ([P05](https://developers.openai.com/api/docs/guides/image-generation),[P06](https://ai.google.dev/gemini-api/docs/image-generation),P12) {decay: 2026-12-28}. |
| **FLUX.2** | Assign numbered base/style roles; describe the **desired visible state positively** (e.g., “the sidewalk remains empty and continuous”). The cited FLUX.2 guide says **no negative-prompt parameter**; do not copy Stability's `negative_prompt` field into it. [D] ([P07](https://docs.bfl.ai/guides/prompting_guide_flux2)) {decay: 2026-12-28}. |
| **Midjourney** | Ordinary **Image Prompts** are for inspiration, not exact preservation; phrase the desired *final image*, and consider its separate **Editor** if attempting a specific change. Verify drawings/model outside Midjourney either way. [N] ([P08](https://docs.midjourney.com/hc/en-us/articles/32040250122381-Image-Prompts),P21) {decay: 2026-12-28}. |
| **Stability AI** | Choose the endpoint deliberately: inpainting for a region; sketch/structure guidance for visible form; style routes for appearance. Some documented endpoints accept `negative_prompt`, but fields are endpoint-specific. [D] ([P09](https://platform.stability.ai/docs/api-reference)) {decay: 2026-12-28}. |
| **Adobe Photoshop** | Use a selection and optional role-appropriate reference for bounded edits; if the *unselected* pixels must be identical, composite approved results onto a copy of the original and compare the unchanged layer, rather than trusting the mask alone. [N] ([P10](https://helpx.adobe.com/photoshop/desktop/create-open-import-images/create-images/use-reference-images-for-consistent-results.html),[S13](https://community.adobe.com/questions-712/changes-to-generative-fill-1174820)) {decay: 2026-12-28}. |
| **Chaos Veras/Enscape** | Work from the named live viewport/model revision and try a **low Geometry Override** for detail retention, separate material override for finishes, and its selected-area edit where appropriate. Its vendor claims and older reviewer observations both demand comparison to the source model. [N] ([P11](https://documentation.chaos.com/space/EREVIT/128418464/Veras+for+Enscape),[S09](https://aecmag.com/visualisation/veras-ai-based-renderer-for-revit-models/)) {decay: 2026-12-28}. |

## Independent QA & publication gate (manual, project-specific)

**[N]** (P01–P04,P17,P21,P22,S07,S13–S17) {decay: 2027-09-29} For each proposed image, have a designer record `PASS / FAIL / UNVERIFIED` with actual evidence. **“Cannot tell from photo” = UNVERIFIED, never PASS.** A self-critique by the same image model is a useful discrepancy *lead*, not independent verification.

| Gate | Compare against, and reject/flag if... |
|---|---|
| Rights & attribution | Check actual image owner, platform/item terms, client permission and intended audience; stop if rights missing. Preserve original source credits and add concept disclosure. |
| Visual invariants | Overlay or place source and proposal side-by-side at identical crop; check roof, bay/opening/floor counts, façades, neighbouring structures and camera. Any unapproved change = `FAIL`. |
| Spatial/functional logic | Check entrances, road/footpath connections, parcel edges, turning, circulation, adjacency and levels **against survey/site plan**, not just pixels. Mismatch or missing data = `FAIL/UNVERIFIED`. |
| Drawing/model correspondence | Check footprint, spans, materials, grid, elevations and code-sensitive elements against original DWG/RVT/IFC and signed schedules. A pretty render cannot pass this by itself. |
| Cross-view | Use same model revision/camera list; line up opposite elevations/plan, opening and balcony counts, roofline and ground plane. Conflicting views = `FAIL`. |
| Outside-edit pixels | If immutable pixels are required, calculate or visually inspect the non-edited region and restore the original layer via compositing; mask fidelity is not guaranteed. |
| Release label | Put *Concept illustration — AI-assisted; not a survey/as-built or construction document* on the **presentation sheet**, with credited original separate from the proposal. This is clear communication, not a licence substitute. |

**Optional critique prompt, for a separate multimodal reviewer:**

```text
Compare Image A (unmodified authorized source) and Image B (AI-assisted
concept) only on VISIBLE differences. Make a table with: feature; unchanged /
changed / occluded; source A location; concept B location; why it matters;
which drawing, GIS layer or site record would independently verify it.
Do not estimate lengths, setbacks, structural capacity or code compliance from
pixels. Mark any such point UNVERIFIED. Flag every new door, floor, road,
water feature or building and any inconsistent cross-view element.
```

## Worked briefing example — fictional, **not a generated result**

*Assumed documents supplied by a hypothetical rights-holding design team:* a two-storey community library model; an approved east entrance, six east façade bays, an unchanged roof silhouette, and a named east-eye-level camera. A separate authored GIS diagram defines access and parcel limits; no commercial map screenshot is uploaded. **[N]** (P02,P12–P17,P21,P22) {decay: 2027-09-29} Here the user could put “east camera / model rev A” into Version C, set “allowed change = render one timber-look rainscreen palette only”, keep the six bays and entrance fixed, and compare results with rev A. The brief makes the visual task *auditable*; **no model was called**, so no fidelity or compliance outcome is claimed.

## @Review refresh report and triangulation trace

| Review requirement | S012 observation / verdict |
|---|---|
| Brain-first order | `[O]` Checked `Brain/long_term/` and `Brain/short_term/`/held collection digests at scout; no dedicated image-reimagination dossier. @Gather placed the 41 qualified source rows in `Brain/short_term/notes/2026-09-29_arch-image-source-register.md` and a separate findings report in `outputs/`. @Review reused those; S07, S09 and P12 were reopened solely for a claim-fit audit, with **zero newly qualified sources or gap fetches** in this leg. No claim was promoted into long_term or the Core. |
| Reverified / decay | `[O]` Source identities, claim-fit and apparent contradictions were checked in the preceding @Gather acquisition on 2026-09-29; @Review additionally reopened S07 (architecture commentary), S09 (older Veras review), and P12 (Google Geo Guidelines) to confirm their quoted limits. No cited product/policy fact has reached the proposed 2026-12-28 recheck date; study records are dated historical findings, not current guarantees. No `[DECAYED]` promotion or existing Brain record altered. Living provider docs can change after retrieval. |
| Independent claim check: image ≠ editable model | `[N]` P02 Autodesk's raster/model distinction + P17 Ko et al.'s independent hybrid workflow + S01 literature synthesis **agree on the limited proposition** that appearance alone is not an edited BIM source. **VERIFIED as a workflow distinction; no inference about a specific image.** |
| Independent claim check: site/cross-view fidelity is not ensured by prose alone | `[N]` P21 Jung's original site-study failures + P22 Du et al.'s specialized multi-view solution + P19's independent practitioner workflow **support treating those as separate validation problems**. **VERIFIED as a risk framing, not a universal error rate;** any particular design stays `[UNVERIFIED]`. |
| Independent claim check: rights vary by owner/product | `[D]` Google P12/P13 and Esri P14–P16 independently publish different policies. **VERIFIED that a universal screenshot-reuse rule is unsound;** Google/Esri permissions for a particular image remain `[UNVERIFIED]` until its actual product, item, ownership and intended use are identified. UK/other-jurisdiction S12/S18 do not confer local rights. |
| Non-triangulated inference | `[UNVERIFIED]` P20's prompt-richness association (text-only students) cannot prove this kit improves image-edit fidelity. No prompt or QA procedure here was run on user imagery; no architect, rights holder or site authority signed it off. |

**Autopilot log:** T1 explicit task = research architecture photo/reference prompting and other providers; AUTO → `research.md` for @Gather, then @Review for actionable synthesis. T2 cue: repo entry gate and mode/style rules; T3 standing orders not drawn because the explicit research objective was active; T4 earlier episodes informed the no-fabrication/no-bulk-fetch stance. Fork resolved: the GitHub link supplied **instructions**, not a request to reverse-engineer that repo; no @Decode branch. Bandwidth: HTML/docs and one small academic PDF; large RIBA PDF skipped. Safety: no tile/image scraping, client uploads, model tests, actual building/permit claims, or automatic canon write. Result: one evidence corpus and these **conditional** templates.

**If asked to continue:** (1) if the user provides an owned/cleared sample and exact change budget, run a documented input→output comparison against the model/GIS source; (2) refresh the exact selected provider/item licence immediately before publication; (3) build a version-pinned two-view benchmark only with licensed example data and human review. No work on those steps was represented as completed here.
