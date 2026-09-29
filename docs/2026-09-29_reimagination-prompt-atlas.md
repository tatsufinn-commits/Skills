# Re-imagination prompt atlas — 3D · photo/enhancement · architecture
**S014 · 2026-09-29 · @Autopilot → @Review · AUTO.** **34 problem-indexed, copyable candidate briefs/prompts:** 12 architectural (A01–A12), 10 photo (P01–P10), 10 3D (D01–D10), 2 evaluation/refinement (T01–T02). **Every prompt below is `[N]` — untested.** No source tested any exact wording in this atlas. The companion [@Gather research report](2026-09-29_reimagination-prompt-research.md) defines the `[D]` provider controls, `[R]` bounded research and `[O]` individual experiences and gives direct links for all D/R/O IDs; the [source register](../Brain/short_term/notes/2026-09-29_prompt-atlas-source-register.md) audits each. A cited complaint explains **why** a candidate card exists; it is **not** evidence that this card solves it.

## How to use the atlas
1. Choose a **problem**, not a provider. Replace `[bracketed fields]` with real observations/desired changes. An “image A” or “mesh” in text refers to a *separately attached permitted file*; writing its name does not upload it. Distinguish **geometry/source**, **style reference**, **texture reference**, **mask**, and **output specification**. If a UI lacks one of those inputs, omit that claim or change tools.
2. Use the text only in a **text-capable** generation/editing field or as a human task brief. Operations/controls in the setup line are **not** words to paste. Keep an unchanged original and record version, settings, source/view and what was actually accepted. Prompt adjectives such as “exact,” “unchanged,” and “photoreal” do **not** lock pixels, geometry, dimensions, identity or unseen surfaces.
3. Protect inputs: verify permission to upload borrowed photos/screenshots, model and client material, and the tool's usage/privacy rules first; school use alone is not a universal licence (HELD S012/S013 evidence in the report). Label a speculative output as **AI concept visualization**, not survey, as-built elevation, historical restoration, manufacturing drawing or approved material schedule. Do not erase a watermark/credit to launder a source.
4. **Make a stop decision from the QA line.** If an invariant is non-negotiable (bay count, face identity, text, mesh scale or printability), reject drift, do the operation in an authoritative CAD/photo/mesh editor or attach better measured/multi-view inputs. Where a reference is incomplete, choose an explicitly speculative image instead of claiming recovery.

### Fast selector
| Future problem | Start with | Required distinction |
|---|---|---|
| Sketch/model → exterior mood without moving openings | A01,A03 | Source view ≠ geometric guarantee. |
| Facade finish, interior furnishing, insert one object | A02,A04,A05 | Region/selection versus whole-view rewrite. |
| Context/site, elevation, floorplan, camera angles | A07,A08,A10,A12 | Speculative image versus geospatial/CAD truth. |
| Remove an object, extend a photo, fix a seam | P01–P03 | Blank fill/Remove/selection and edge QA. |
| Denoise, restore face, rescue tiny text or fabric | P05–P09 | Conservative settings versus new invented detail. |
| Invent a mesh from words/front photo/multiple views | D01–D03 | Text input, one input image, actual multi-image input. |
| Change mesh look, game asset, print object | D04–D07,D10 | UV/topology/scale and geometry versus color map. |
| Debug why any prompt failed | T01,T02 | Diagnose operation and observed delta before adding adjectives. |

### Paste-field router — recheck the live UI before using
| Workflow | Where text goes, if at all | Non-text input/setting and major limit |
|---|---|---|
| SketchUp AI Render | Current prompt field, if enabled (D01–D03) | Model view, style preset, Paint/Erase mask where available (O04). Historical geometry-respect sliders requested back by O05 must **not** be assumed present. |
| Photoshop Generative Fill | Selection → prompt or **blank** → model/variations (D14) | Selection, layers and possibly another Remove operation; selected does **not** mean non-selected pixels are proved unchanged (O10–O12; HELD S012 S13). |
| Midjourney | Generate/Editor text **in the relevant version** (D17, HELD S013 E06) | Style Reference D16 changes aesthetic, not copies building; Edit Model is separate; confirm permissions/version/parameter syntax. No universal exact-preserve flag. |
| FLUX.2 layout guidance | Instructions in guide's editing workflow (D19) | Uploaded reference image(s), **not** an automatically available native ControlNet field; no pixel-perfect guarantee. |
| Topaz Gigapixel Redefine | *Image description* on documented **realistic Subtle** or **creative** configurations (D12); phrase as **description**, not directive | Creativity/texture settings; Face Recovery disabled in Redefine creative per D12. Recover v2 uses Detail, not this description. |
| Topaz Gigapixel Face Recovery / Lightroom Enhance | **No natural-language prompt in these documented controls** (D13,D15) | Select desired face(s), model/mode/strength; or Lightroom detail operation. A text prompt elsewhere is **not** their setting. |
| Meshy text / image / multi-image / retexture | Text describes geometry in text-to-3D (D05) or retexturing in D08. D06/D07's optional `texture_prompt` is **texture-only**, not a geometry-instruction slot; upload source image(s) separately. | D07 accepts 1–4 **separately supplied geometry views** (photos, or eligible generated views that are not evidence of a real back), distinct from D06's returned thumbnails. D06/D07 also expose optional `texture_prompt` for **texturing**, not geometry; remesh, UV retention and export are separate. Do not use deprecated `negative_prompt` as a current recipe. |
| TRELLIS.2 / Hunyuan3D-2.1 / Tripo | Check their own current upstream UI/README/tips (D09–D11) | A GitHub request or one failure report (O19,O20) does not create Meshy's input route on these projects. |

## Architecture: preserve a design while changing its portrayal
All A cards are for a text-capable **image-to-image editor** with the named permitted images attached; A10 also assumes actual separate views. For a purely text-to-image tool, replace “source view” with an explicitly imagined design and remove all fidelity claims. The **Setup** is an operation outside the paste text; **Check** is performed on the generated result, not assumed. Codes in *Basis* link to the research report's references.

### A01 — Rough massing / model screenshot → exterior concept
**Setup:** attach your model/screenshot as geometry-and-camera source; select style preset/reference separately only if offered. Choose an exploration image, not technical documentation.
```text
Create a conceptual exterior visualization from the attached model view. Retain the visible building's overall massing, roof profile, main entrance, count and positions of visible window bays, and the camera viewpoint. Change only the portrayal: warm late-afternoon light, pale stone at [specified wall], dark metal at [specified frames], realistic planting outside the building footprint. Keep unspecified finishes neutral. Do not invent extra floors, balconies, openings or structural members. This is a schematic design visualization, not a measured elevation.
```
**Check/fallback:** compare bay count, roofline, footprint edge and camera to the original; if any must be exact, render from the source model or manually composite rather than endlessly restating “preserve.” **Basis:** D01–D03 [D], O01–O03 [O], S013 E09 [R]; text `[N]`.

### A02 — Refinish only a facade region
**Setup:** supply source view; select only `[facade panel]` in a local editor or use model material assignment; a look reference is **style only**, not replacement geometry.
```text
In the selected facade panel only, show matte terracotta cladding in [specified brick/tile module], keeping the existing panel boundaries and all visible windows, mullions, signs and door locations. Preserve the other walls, ground, sky and camera framing. Match the original light direction. Do not reinterpret the cladding as a new facade grid or alter the building volume.
```
**Check/fallback:** align before/after windows, seams, edges and intended panel color; for a real finish specification edit the CAD/BIM materials and export anew. **Basis:** D14 [D], O06 [O], D16 [D]; `[N]`.

### A03 — Same geometry, new daylight / weather mood
**Setup:** attach rendered source/model view; use relight or local sky edit if available; lock camera/model in the renderer if exact geometry matters.
```text
Reimagine the attached exterior on a bright overcast morning. Keep the same camera, building silhouette, number and location of visible openings, pathway geometry, planted areas and surface materials. Change only the sky ambience, shadow softness and plausible exposure; avoid new architectural elements. Keep the concept deliberately schematic wherever the original is schematic.
```
**Check/fallback:** compare facade grid and cast-shadow direction; when sky/lighting accuracy is required, re-render in a controlled lighting setup. **Basis:** D18,D19 [D], O07 [O], O09 [O]; `[N]`.

### A04 — Interior palette/furnishing refresh without redesign
**Setup:** attach source interior view; if possible select only paint/upholstery/furniture regions, keeping fixed walls/glazing/circulation defined by the source.
```text
In this existing interior view, make a quiet adaptive-reuse reading room: [specified wall] is warm off-white, existing brick remains exposed, loose furniture uses walnut and muted green upholstery. Keep all visible columns, doors, window locations, ceiling height as depicted, built-in counters and passage openings in place. Change loose furnishings and lighting mood only; do not add or remove partitions, change the camera, or portray the scene as code-compliant.
```
**Check/fallback:** overlay doors, columns and fixed cabinet outlines; edit the model/material schedule if circulation or accessibility must be verified. **Basis:** D18 [D], O01,O08 [O]; `[N]`.

### A05 — Insert one object without replacing the room
**Setup:** mask the intended zone with an editor that supports local insertion; supply an owned/licensed object reference if shape matters.
```text
Add one freestanding [object, e.g. low walnut display plinth] inside the selected area of the supplied interior photo. Set it on the existing floor with contact shadow matching the room lighting. Leave walls, windows, signage, people and all unselected furniture unchanged in content and viewpoint. Do not create duplicates or obstruct the visible doorway.
```
**Check/fallback:** inspect mask perimeter, scale, contact shadow and any shifted existing object; if critical, use a composited 3D object from a measured room view. **Basis:** D14 [D], O04 [D/O], HELD S013 E06 [D]; `[N]`.

### A06 — Remove temporary clutter from a building photograph
**Setup:** work on a licensed photo; select a car, person or temporary fence; choose an actual Remove/heal tool or blank Generative Fill where supported. Do **not** remove authorship marks.
```text
Reconstruct only the ground and facade surfaces visibly occluded by the selected temporary [object]. Continue the adjacent perspective, paving joints, illumination and material colors. Keep the building's existing windows, doors, signs and all other objects at their original positions. Do not invent unseen facade details; use visually neutral continuation where evidence is missing.
```
**Check/fallback:** look for repeated tiles, doubled mullions and halo edges; manual clone/composite is safer for a measured facade. **Basis:** D14 [D], O10–O12 [O], HELD S012 S13 [O]; `[N]`.

### A07 — Context/site atmosphere, not a survey
**Setup:** attach a permitted site photo or site plan **and** a distinct building view; label them `[SITE]` and `[DESIGN]` when the interface supports multiple inputs. Use confirmed site constraints supplied by the user, not a guessed map.
```text
Create a clearly labelled concept visualization placing the design in the supplied site context. Treat [DESIGN] as the building's visible massing and entrance source; treat [SITE] as the background, adjacent street and tree-location reference. Preserve the supplied street orientation and any explicitly marked site boundary. Show [desired landscape/season] only as an illustrative option. Do not invent surveyed distances, road alignments, neighbors or regulatory setbacks; leave uncertain background areas schematic.
```
**Check/fallback:** cross-check actual parcel/road data against GIS/CAD and record which portions were invented; do not use the image as site evidence. **Basis:** D19 [D], HELD S012 source-truth/rights research, O08 [O]; `[N]`.

### A08 — Elevation / diagram *style* without invented dimensions
**Setup:** start from a real elevation/export if one exists, or say “illustrative diagram” if starting from a perspective. Avoid auto-created scale bars, labels or dimension strings.
```text
Turn the supplied [front elevation drawing] into a clean presentation elevation with a white background, restrained grey fill and thin black outlines. Keep the visible building outline, opening count and alignment, datum positions and scale relationship from the input. Do not add dimension numbers, floor heights, structural notes or construction specifications that are not legible in the source. Label the result illustrative if the source is only a photograph.
```
**Check/fallback:** overlay against the CAD elevation; if measurements/annotations matter, compose them from CAD, not generated pixels. **Basis:** D19 [D], O02 [O], HELD S012 CAD/raster distinction; `[N]`.

### A09 — Early-stage physical-model / sketch look
**Setup:** supply massing/model view as composition; use an aesthetic style reference only if authorised, or describe the finish in words.
```text
Make an early-stage white-card physical-model visualization of the attached massing. Keep the model's overall block volumes, entrance position and camera framing. Use neutral white material, subtle paper edges, diffuse studio shadows and minimal contextual trees. Suppress invented construction details, specific finish choices, storefront names and photoreal people. Mark this as a massing study, not a final render.
```
**Check/fallback:** ensure the output has not added buildable-looking components or implied final materials; return to simple model export when drift occurs. **Basis:** D02,D16 [D], O08,O09 [O]; `[N]`.

### A10 — Two existing views of the same building, coordinated look
**Setup:** upload **actual front and side views of the same unchanged model** if the chosen editor supports them. Process each view separately with the same palette/lighting brief. A single photo cannot supply a measured unseen elevation.
```text
Apply the same restrained visualization treatment to the attached front and side model views: [specified material palette], [time/weather], and [landscape treatment]. Use each individual view for its own geometry and camera. Keep the visible opening count, roof outline and entrance of each view from its own source. Do not transfer a window or balcony from one elevation to another or infer a missing rear elevation. Output coordinated concept images, not verified multiview reconstruction.
```
**Check/fallback:** compare each result to its own source, and cross-check overlapping corners/material boundaries; if consistency is required, render both from one actual 3D model. **Basis:** D19 [D], O01–O03 [O], HELD S013 E06 [D]; `[N]`.

### A11 — Change the building's *design*, with a stated change boundary
**Setup:** only for design exploration (not preservation). Supply source concept and specify what may change versus what is fixed; keep approval decisions separate.
```text
Explore one alternative for the supplied [two-storey community library]: introduce a shaded colonnade on the [east] elevation and use a [specified material] roof screen. Keep the site boundary, entrance location, two-storey massing, existing stair position if visible and [named non-negotiables]. Treat facade openings inside the new colonnade as proposed, not as existing conditions. Produce a concept visualization with clearly distinguishable new and unchanged zones.
```
**Check/fallback:** mark additions on a redline and have the designer decide whether the change is actually permissible; a pretty image is not an authorized design revision. **Basis:** D03,D18 [D], O08 [O], HELD S013 E08 [R]; `[N]`.

### A12 — Floorplan → perspective *impression* (not automatic BIM)
**Setup:** attach a legitimately sourced legible plan **plus** labelled room/door information; an image editor may create an impression but not measured 3D. Use model creation instead when geometry is mandatory.
```text
Create an illustrative interior perspective inspired by the supplied [room plan]. Respect the labeled room function, entrance wall and window wall only where they are unambiguously marked. Show [viewpoint, e.g. from entry toward windows], [furniture palette] and [light condition]. Do not claim exact room dimensions, egress widths, ceiling height or hidden construction. If a relationship is unclear from the plan, keep it schematic rather than presenting a fabricated measured detail.
```
**Check/fallback:** verify against an actual measured model/drawing and annotate all interpreted dimensions; reject as construction documentation. **Basis:** D19 [D], O02 [O], HELD S012 CAD/raster boundary; `[N]`.

## Photo / enhancement: correction is not factual recovery
P cards are for **text-capable image editors unless explicitly routed otherwise**. No prompt can prove that missing scene detail, unreadable text or an unfamiliar face matches the real original. For a settings-only workflow, use its controls and the **Check** as a separate human decision.

### P01 — Remove one distraction rather than redesign the photograph
**Setup:** select the unwanted item in Photoshop or a comparable editor; try Remove/heal or blank Fill if those operations fit; text below only for a compatible promptable fill.
```text
Remove only the selected [cable or parked bin] and continue the immediately surrounding wall/floor texture, perspective and light. Preserve every unselected object, architectural edge, logo and person in the original photograph. Do not add new objects or change the camera/view.
```
**Check/fallback:** inspect edge contours at full size, area outside mask and layer before/after; if removal no-ops, inspect tool/version/connectivity rather than simply adding more adjectives. **Basis:** D14 [D], O12 [O], HELD S012 S13 [O]; `[N]`.

### P02 — Refill a small damaged area or paint blemish
**Setup:** mask only scratch/stain; use nearby pixels/reference under an editor that accepts them; not a face-identity recovery operation.
```text
Repair the small selected surface blemish by continuing the adjacent [plaster/wood/sky] pattern and local grain. Match existing luminance, perspective and noise. Keep the original linework, labels, junctions and surrounding materials unchanged. If evidence is insufficient, prefer an unobtrusive neutral patch over a newly invented motif.
```
**Check/fallback:** inspect repeating patterns and seams; use manual retouching for linework or printed text. **Basis:** D14 [D], O10,O11 [O]; `[N]`.

### P03 — Expand a photograph for a poster crop
**Setup:** use an outpainting/expand region outside the original; preserve source rectangle as a separately saved layer.
```text
Extend the supplied image to the [left/right/top] for a [portrait/landscape] crop. Continue the existing sky, wall or landscape perspective and lighting without moving or rescaling the building/subject in the original image. Keep new regions visually subdued and avoid new signage, people, windows or identifying details. The original central rectangle is the reference, not material to reimagine.
```
**Check/fallback:** audit the seam at 100% and compare unexpanded source pixels; composite the untouched original back over the generated center if exact retention matters. **Basis:** D14 [D], O10,O11 [O]; `[N]`.

### P04 — Match the color of a retouched patch to the source
**Setup:** only for a text-capable localized editor; use actual color/exposure tools after generation when possible.
```text
Within the selected repaired patch, match the surrounding [warm/cool] color temperature, midtone brightness and film grain. Keep the scene's visible objects and their edges as in the source. Adjust the patch's tone and texture only; avoid new surfaces, stronger sharpening or a different time of day.
```
**Check/fallback:** toggle before/after, inspect at full and thumbnail size plus edge histograms/eyedropper; apply a manual adjustment layer if tone still differs. **Basis:** D14 [D], O11 [O]; `[N]`.

### P05 — Low-light denoise that keeps fine texture
**Setup:** if the chosen program lacks a text input, **do not paste**; choose conservative denoise/sharpen settings instead. A promptable image editor can use the brief below.
```text
Reduce visible high-ISO noise in the supplied photo while keeping actual fabric weave, hair strands, brick mortar, printed lettering, hard edges and the original face proportions. Do not add sharper imaginary texture, new lettering or plastic skin. Keep color and exposure close to the source; leave genuinely unreadable details soft.
```
**Check/fallback:** inspect cloth, sky gradients, hair, eyelashes and halos at 100%; lower strength or turn off creative restoration if detail becomes invented. **Basis:** D15 [D], O15,O16 [O], HELD S013 E10–E11 [R/D]; `[N]`.

### P06 — Old portrait restoration with an identity ceiling
**Setup:** text is for a text-capable restoration/editor only. **Topaz Face Recovery has no text field**; there select actual faces, lower strength and compare Realistic/Creative modes as controls (D13). Obtain consent where needed.
```text
Clean scratches, exposure loss and dust in this supplied portrait. Use only the original as the person's identity reference. Keep the apparent face shape, expression, visible hairline, age cues and any visible facial hair unchanged; do not add eyelashes, teeth, spectacles or facial hair not present in the source. Where features are unreadable, retain uncertainty/softness rather than inventing a plausible face.
```
**Check/fallback:** crop both originals and outputs side-by-side, especially eyes/mouth/hair; stop if identity-critical traits change. This cannot establish who the person historically was. **Basis:** D13 [D], O13,O17,O18 [O]; `[N]`.

### P07 — Tiny screenshot, logo or text: enhance legibility, do not hallucinate facts
**Setup:** use a legitimate high-resolution original if available; use conservative upscaling. Below is a text-capable *brief* only, not an OCR certification.
```text
Improve overall legibility of the supplied low-resolution screenshot while keeping the existing layout, logo silhouette and text positions. Do not guess unreadable letters, numbers, addresses, dates or measurements. Keep uncertain areas visibly uncertain; avoid adding facade openings or hard architectural details that the original does not establish.
```
**Check/fallback:** compare every character against the original and fetch a better source if needed; never quote generated lettering as primary evidence. **Basis:** D12,D15 [D], HELD S013 E10–E11 [R/D]; `[N]`.

### P08 — A genuinely promptable Gigapixel image description
**Setup:** only in **Topaz Gigapixel Redefine creative** or documented **Redefine realistic + Subtle** when *Image description* is visible. Example for a **permitted** old streetscape; not for Recover v2 or Face Recovery. Use a description, not “change the image.”
```text
A softly detailed archival street photograph of a low-rise brick building, its visible window rhythm, a pale overcast sky, quiet pavement, natural film grain and muted colors.
```
**Check/fallback:** compare invented windows, lettering, people and tone; choose lower creativity or Recover/conservative model when reconstruction is unsafe. Topaz says Redefine creative disables Face Recovery; don't expect both simultaneously. **Basis:** D12,D13 [D], O14,O17 [O]; the example wording `[N]`.

### P09 — Fabric/skin smoothing or sharp halo triage
**Setup:** a **settings-led diagnostic**, not a text command for Topaz denoise: inspect model/strength/face selection; if a separate text-capable editor is used, this brief is pasteable there.
```text
Produce a restrained enhancement of the supplied photo. Keep the source's fabric weave, natural pores, printed pattern and fine edges rather than manufacturing extra micro-detail. Do not produce bright halos around high-contrast borders or banding in smooth cloth/sky. Leave weak source details naturally soft.
```
**Check/fallback:** compare identical 100% crops across original, conservative setting and creative setting; lower sharpening/texture or disable face recovery when it creates features. **Basis:** D12,D13 [D], O15–O18 [O]; `[N]`.

### P10 — Intentional creative reinterpretation with honest labeling
**Setup:** a text-capable image editor plus an owned/cleared source photo; use a separate style reference if the provider offers one. This **allows** scene changes and must not be passed off as a record.
```text
Make an openly fictional cinematic twilight reinterpretation of the attached street photograph. Use the photo for the recognizable overall building silhouette and street viewpoint, and use [licensed style reference or description] for palette and atmosphere only. Show blue-hour rain reflections and a restrained warm interior glow. Preserve the real photo separately; mark this result as an AI concept, not documentary evidence of weather, lights, occupancy or the actual facade finish.
```
**Check/fallback:** confirm the label persists when shared, and that source/licence and people/privacy rules allow transformation. **Basis:** D16 [D], O08 [O], HELD S012/S013 rights work; `[N]`.

## 3D: decide whether you need a picture, an editable asset, or a printable object
The D prompts are *object descriptions/production briefs*. A text field can guide **visible appearance**; actual source views, model file, topology, UV, remesh and export are **separate controls**. For image-only APIs, the quoted brief is an acceptance specification for a human/operator, **not** a purported API parameter. Meshy D07 supplies real source images as input; D06's returned viewpoint thumbnails do not.

### D01 — Words → simple 3D product-study object
**Setup:** use a text-to-3D field such as the documented D05 route; choose one isolated object rather than an entire building/interior.
```text
A single freestanding reading lamp for a product concept: circular weighted base, one slender vertical stem, one simple bell-shaped shade, continuous visible joints, approximately [target overall height] in the intended design. Matte dark green metal and warm white inner shade. Show a coherent back and underside, not duplicate shades, extra stems, logos or background furniture. Intended use: visual concept first; dimensions require later measurement.
```
**Check/fallback:** orbit all sides, verify one lamp/one shade, base contact and silhouette; do not infer actual dimensions from appearance. **Basis:** D05 [D], O21,O22 [O], R01 [R]; `[N]`.

### D02 — Single product photo → speculative 3D prop
**Setup:** attach a clean, rights-cleared photo to an **image-to-3D** endpoint (D06/Tripo D09). The following is a copyable **production/QA brief**, **not** a Meshy geometry API parameter: D06's optional `texture_prompt` only steers texturing, and cannot make its one input image disclose a real unseen rear.
```text
Use [front product photo] as the reference for the visible silhouette, major parts, colors and proportion of a single chair. Treat the unseen back and underside as uncertain rather than verified. Do not add arms, legs, cushions or labels absent from the visible evidence. Output a separate 3D concept asset for inspection from all angles, not a measured replica.
```
**Check/fallback:** inspect hidden back/seat underside and leg count, reject invented attachments; find real side/rear photos or model the missing geometry manually. **Basis:** D06,D09 [D], O19,O21 [O]; `[N]`.

### D03 — Real multi-view photos → one object mesh
**Setup:** if using Meshy's **dedicated multi-image endpoint D07**, submit **1–4 separately supplied source images of the same object from different angles** for geometry (API: eligible image URLs/data URIs or a compatible prior task); photographed views give real-world evidence, whereas generated views (also accepted from eligible tasks) are only guesses about hidden sides. For Meshy 7.1, place the intended front view first. Texture-only reference views/optional `texture_prompt` have their own independent input roles; the latter guides texture, **not** geometry. Keep scale/pose consistent. Do not treat generated four-view *output thumbnails* from D06 as independent photographs. The text below is an **operator brief**, not a geometry-text parameter on this endpoint.
```text
Geometry sources: [front], [left], [rear], [right] photographs of the same [object]. Match the single object's silhouette and part count across them. Color/finish reference: [separately provided, if supported]. Do not use an unrelated style image to infer shape. Deliver a concept mesh whose rear, underside, seams and visible parts can be inspected; unknown scale and hidden geometry must remain flagged for manual verification.
```
**Optional D07 `texture_prompt` (texture phase only, not geometry; do not combine with incompatible texture-image inputs):**
```text
Matte oiled oak on the wooden frame, woven olive fabric on the seat, subdued natural wear, no logos.
```
**Check/fallback:** orbit and compare each geometry source view, inspect normals/UV/material maps and fit to known dimensions. If views contradict, resolve capture/source first; if the tool lacks multi-image input, do not fake it with words. **Basis:** D06–D08 [D], O19,O20 [O]; both brief and texture wording `[N]`.

### D04 — Retexture a supplied mesh without asking for a new object
**Setup:** provide a legitimately sourced **existing mesh** to a retexture workflow (D08), and set keep-UV/remesh options separately. Use the description only where a text styling field exists.
```text
Retexture the supplied existing [chair] as matte walnut wood for the frame and muted woven green fabric for the seat. Preserve the source mesh's part boundaries, physical silhouette and material assignment areas; do not add legs, change geometry or repaint outside the named surfaces. Avoid readable branding. Desired result: a different appearance for the same model, not a new chair.
```
**Check/fallback:** compare vertex/topology/UV and exported material maps against the original; the phrase “same model” is not a mesh integrity test. **Basis:** D08 [D], R03 [R], O20 [O]; `[N]`.

### D05 — Low-poly game prop with a target budget
**Setup:** text-to-3D for a draft; configure documented topology/remesh/export controls outside the prompt. Character rigging and LOD optimization are **not** assumed.
```text
A single stylized low-poly supply crate for a game prototype: rectangular closed box, four reinforced corners, readable lid separation and simple large shapes. Flat painted wood and worn metal, no tiny text, no handles floating off the mesh, no ground plane. Target [poly/triangle budget if supported by the tool], coherent silhouette from all directions; topology and collisions to be checked in the game engine.
```
**Check/fallback:** verify poly count, non-manifold edges, pivots, UVs, normals, dimensions, LOD and collision manually; if constraints fail, retopologize in a 3D editor. **Basis:** D05,D07 [D], R01,R02 [R]; `[N]`.

### D06 — Object missing or wrong from rear view
**Setup:** if an authentic rear/side image exists, move to D03. Without one, the text-to-3D route can only make an **explicitly speculative** reverse.
```text
Design a concept [cabinet] consistent with the attached front appearance: two front doors, flat top and four visible short legs. The rear is an unverified design proposal: simple continuous backing panel, no extra doors, no open shelves or disconnected pieces. Keep one object and a consistent proportion when viewed from front, side and back. Do not describe this as reconstruction of the original unseen rear.
```
**Check/fallback:** orbit and annotate rear as invented; for exact catalog/heritage reconstruction, obtain actual rear image/model. **Basis:** D06,D07 [D], O19,O21 [O], R03 [R]; `[N]`.

### D07 — 3D print concept: visible texture is not printable relief
**Setup:** text-to-3D description for a proposed physical figurine; print suitability requires separate thickness, watertightness, overhang and slicer checks. A texture/color map is **not** physical geometry.
```text
A single small desk figurine shaped like a simplified lighthouse: one continuous main tower, broad stable base, rounded edges, a large clearly modeled entry recess, and no fragile freestanding cables or paper-thin railings. Any features intended to print in relief should be part of the actual surface geometry, not just painted texture. Approximate target height [mm]; exact printable dimensions and wall thickness to be measured in a mesh editor and slicer.
```
**Check/fallback:** inspect actual mm scale, min wall thickness, manifold/closed mesh, supports and whether “relief” exists in geometry. Never call it print-ready from a rendered thumbnail. **Basis:** D05,D07 [D], R02 [R]; physical-print safety is **not** established by those sources, so this is a QA proposal `[N]`, not a vendor promise.

### D08 — Change one feature on an *existing* 3D asset
**Setup:** use a genuine mesh editor or a 3D editing method that accepts this task; do **not** assume any image-to-3D API can modify an existing mesh from this text. If working from a 2D concept edit, the phrase below is a human change brief; EditP23 R03 is research, not an available generic button.
```text
On the existing [lamp mesh], widen only the lower shade rim to [specified target] while retaining base, stem, joint positions and material assignments. Propagate the altered rim consistently to every viewpoint; keep the other parts unchanged. Export a separate version and identify any changed topology or UV seams for inspection.
```
**Check/fallback:** diff original/new geometry and orbit; rework manually if unrelated vertices change. **Basis:** D08 [D], R03 [R]; `[N]`.

### D09 — Furniture kit, not a one-shot “build my whole room” mesh
**Setup:** text-to-3D or image-to-3D **separately per object**, then assemble in a real modeling/scene tool; use A04/A12 for a room *image*.
```text
Create one standalone [dining chair] asset for a modular room kit, with consistent proportions, a distinct seat/back/leg structure and the [specified palette]. Do not include a table, room walls, people or surrounding decor in this asset. The companion [table] and [pendant] will be separate objects assembled using a measured room layout later.
```
**Check/fallback:** match scale/pivots and clearances of each independent asset in the actual room; don't treat a styled room photograph as an editable room model. **Basis:** D05–D08 [D], O19 [O]; `[N]`.

### D10 — Decorative surface versus actual modeled carving
**Setup:** decide whether the use is *rendering* (texture okay) or *physical print/CNC* (geometry necessary). D08 retexture is suitable only for appearance; direct mesh editing is required for measured relief.
```text
For a visual concept of the supplied [panel mesh], show an engraved-looking geometric motif in the central face while keeping the outer dimensions and border. If the output is intended for fabrication, this description is only a design brief: create real modeled recesses with [specified depth] in the source mesh, not a flat color or normal-map illusion. Do not infer machinability from the render.
```
**Check/fallback:** inspect wireframe/height in the actual model, export and measure recesses, and obtain fabrication review; do not count a pleasing shaded surface as cut geometry. **Basis:** D08 [D], R02 [R]; print/CNC constraints are outside the cited product performance `[N]`.

## Two reusable prompts for auditing and revising — not automatic measurement

### T01 — Source/output difference log for an image or mesh
**Setup:** attach source and proposed output to a vision-capable assistant **with permission**; it may miscount or miss tiny details. Ask a person to verify the critical items and use authoritative files for dimensions.
```text
Compare SOURCE and GENERATED for this specific task. List (1) requested changes that are visibly present, (2) unintended changes in protected areas, (3) visible geometry/object-count/material/text/face differences, and (4) things you cannot verify from these images. Quote no unreadable dimensions or signs as facts. Separate observations from guesses; provide a short accept/reject checklist for a human reviewer, not a claim of pixel or engineering certainty.
```
**Check/fallback:** human cross-check every listed observation at full resolution; for a mesh examine it in 3D, not just a two-image assistant. **Basis:** HELD S013 E08 [R], R01,R02 [R], O01,O17 [O]; `[N]`.

### T02 — After a failed generation, revise *one variable*
**Setup:** provide failed output and source if permitted, the selected tool/version and actual controls; do not paste imagined UI parameters.
```text
My target was [one requested change]; the source to protect is [image/mesh]; the failed output changed [specific unwanted element]. Before rewriting, identify whether the likely issue is the wrong operation, missing input view, wrong reference role, too-wide mask, setting/version mismatch, or contradictory text. Draft one shorter next-attempt prompt changing only [one permitted variable]. State which non-text control must be set separately and what visible or mesh-level check would falsify success. Do not claim the prompt has been tested.
```
**Check/fallback:** log source, settings, one edit and result; if the failure persists, change the input/control/workflow rather than stacking synonyms. **Basis:** D04,D07,D12,D14,D17,D19 [D], O03,O12,O19 [O]; `[N]`.

## Failure-to-control lookup
| If the result does this… | Change the task/control, not just adjectives | Verify before reuse |
|---|---|---|
| More/moved windows despite “keep facade” | Re-render source geometry; select only target material; use real layout input where supported (A01–A03). | Count/opening alignments against original drawing (O02,O05,D19). |
| “Fixed” object remains or is beautified | Check selection and **Remove vs Fill/blank Fill**, connectivity, model/version (P01). | Confirm selected object actually disappeared (O12,D14). |
| Expansion seam/dark patch | Preserve original center, correct edge/tone locally (P03,P04). | Compare seam at 100% and print size (O10,O11). |
| Face becomes a different person | Revert to lower strength/selection or stop; don't describe an invented face as restoration (P06). | Side-by-side identifiable features (D13,O17,O18). |
| Back of mesh fabricated or mirrored | Obtain real alternate-angle input and use D07-supported multi-image route; else label speculative (D02,D03,D06). | Orbit, compare real source views, inspect mesh (O19,O20). |
| Good image, bad game/print asset | Evaluate topology, UV, normals, scale/watertightness in downstream tool; retopologize/model if needed (D05,D07,D10). | File-level utility, not visual preference alone (R01,R02). |

## Brain refresh / retention decision (@Review)
- **Used, not re-acquired:** S012's CAD/GIS-versus-raster truth, licence/attribution and inspirational image-reference limits; S013's structural/style/region separation, student source preparation and non-target preservation checks. See the companion report's HELD list. None contributes to the S014 new-source count.
- **New working knowledge:** the [S014 register](../Brain/short_term/notes/2026-09-29_prompt-atlas-source-register.md) distinguishes actual multi-image **3D input** from output thumbnails; conditional Gigapixel Redefine *Image description* from settings-only Face Recovery; architectural mask-mode context and removed legacy sliders; and human reports from measured success. These remain task-scoped short_term/temporal findings, not a universal prompt-performance rule.
- **Unpromoted/decay:** no successful prompt or longitudinal comparison was measured, so no evergreen success rate or provider ranking moves to long_term. Recheck living docs/tool versions and permissions when a concrete provider is selected, provisionally by **2026-12-28**; blocked Reddit posts remain leads rather than source claims.

**Coverage honesty:** Reddit was explicitly sought for people's experiences but direct access returned 403. The [register](../Brain/short_term/notes/2026-09-29_prompt-atlas-source-register.md#held-excluded-and-search-index-leads) lists Reddit *search-index leads only*; they were **not read, counted or used as evidence**. The first-hand `[O]` cases here instead come from 22 directly readable public discussions across SketchUp, Adobe, Topaz, GitHub and Hacker News. None is a user study of these 34 prompt wordings.
