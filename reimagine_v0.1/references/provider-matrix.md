# Provider Matrix — task → tool routing

**Sources:** prompt kit · vicinity-maps v2 · 3D-enhancers leg · prompt research (Skills repo `docs/`). **Controls are options, never fidelity warranties.** All provider/platform facts carry the corpus decay date **2026-12-28** — past decay, re-scout before routing. `[D]` = provider-documented at corpus time.

## Routing table

| Task | Route to | Text's role | Tool carries | Known limit |
|---|---|---|---|---|
| Restyle a GIS/vicinity base, keep geometry | Reference-faithful editor (corpus names Nano Banana Pro / Kontext class) | Preserve-list + restyle scope | Attached vector base, layer control | Re-overlay YOUR labels/north arrow/scale/title block after |
| Local edit (one region/object) | Photoshop Generative Fill class | Prompt in selection, or **blank** | Selection, layers, Remove op | Selected ≠ others proved unchanged |
| Aesthetic exploration | Midjourney class | Text in the relevant version | Style Reference (aesthetic, not building copy) | No exact-preserve flag; version/param syntax drifts |
| Layout-guided edit | FLUX.2 editing workflow | Instructions in the guide's flow | Uploaded reference image(s) | Not a native ControlNet field; no pixel guarantee |
| Upscale / enhance | Topaz Gigapixel Redefine | **Description, not directive** (realistic-Subtle / creative) | Creativity/texture settings | Face Recovery off in Redefine creative |
| Face restore / detail | Topaz Face Recovery · Lightroom Enhance | **No NL prompt** — none | Face selection, mode, strength | Don't mistake another field for their setting |
| Text → 3D object | Meshy text-to-3D | Geometry in words | Model params | Text is a weak geometry channel |
| Photo(s) → mesh | Meshy image/multi-image (1–4 separate views) · TRELLIS.2 · Hunyuan3D-2.1 · Tripo | `texture_prompt` = texture-only | Uploaded views, remesh/UV/export | Generated views ≠ evidence of a real back; check each project's own current docs |
| Another angle of YOUR building | Go back to the model (new viewport) or 3D reconstruction → re-render | — | Model viewport / image→3D | NEVER img2img "rotate it" for submittable work |
| Vicinity map truth | OSM/Overture/GIS base → symbolise in QGIS → export vector PNG → AI restyle only | Preserve-list on the base | GIS layers | Radius ring, scale, hatching hand-verified |
| Dimensions / code / structure | Original DWG/RVT/IFC, signed schedules, survey | — | Documents | Never from pixels |

## Signal-channel settings (corpus-executed numbers, `[D]`/`[I]`)

| Intent | Setup |
|---|---|
| Restyle | img2img denoise **0.35–0.55** + preserve-list |
| Geometry-critical | ControlNet depth **0.7–0.8** · Canny **0.9–1.0** · MLSD **0.4–0.6** |
| Style transfer | IP-Adapter **0.5–0.7**; two-pass lock→style |

## Selection rules

1. Route by **problem** (atlas card), then pick the provider whose *non-text* input carries the invariant: geometry → tool (ControlNet/model export/viewport/GIS), look → words.
2. If the UI lacks the input your card needs (mask, multi-view, reference-role separation) — change tools, don't hope.
3. Record provider, model version, and settings in the worksheet; version drift is a documented Midjourney-class hazard.
4. Base-quality floor: clean own viewport/capture ≥1920px or lawful capture (Polycam/KIRI class) — never an unlicensed internet snippet (rights gate first).
