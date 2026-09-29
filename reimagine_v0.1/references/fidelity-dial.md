# Fidelity Dial — the preserve/alter protocol

**Sources:** blind-spots leg §6 (executed experiment) · 3D-enhancers leg §7 (upgraded protocol) · student workflow steps 4–6 · prompt kit fields 3–5.

## The measured core `[I]`

Same model, same task, three runs; the only difference was the prompt:

| Run | Prompt | Edge-IoU | SSIM | Required-annotation retention |
|---|---|---|---|---|
| Naive | styling-led | 0.485 | 0.867 | 1.9% (red radius ring silently deleted) |
| **Preserve-list** | keep-list + restyle scope | **0.898** | **0.967** | **25.4%** |

The preserve-list roughly **doubled** geometric fidelity and kept the legally required ring. **The naive output looked fine.** That is the whole argument for forcing this protocol.

**Snippet warning `[I]`:** from a 460 px JPEG-quality-35 snippet, the preserve-list run still *looked* clean but measured SSIM 0.809 / IoU 0.653 vs the clean path's 0.967 / 0.898 — loss of fidelity is invisible without measurement. Prefer the best lawful base (clean viewport ≥1920px, own export); screenshots degrade invisibly.

## Decision bands (this harness's calibration on one plate — re-baseline on your own images)

| Edge-IoU (vs input) | SSIM | Verdict |
|---|---|---|
| ≥ 0.85 | ≥ 0.95 | **Faithful restyle** — submittable after QA gate |
| 0.6–0.8 | — | **Usable with redraw** — fix in an authoritative editor |
| < 0.6, or required annotations missing | — | **Not submittable as a document** — reject, redo |

## The protocol (operative — 3D leg §7, supersedes the earlier ladder where they conflict)

```text
STEP 0  FROZEN INTENT   write the request you will hold the tools to (atoms + invariants).
                        Enhancers never edit this text — they expand only look-fields.
STEP 1  INPUT           own model screenshot (clean viewport ≥1920px) ▸ own capture
                        (Polycam/KIRI class) ▸ lawfully licensed ▸ never unlicensed snippet.
STEP 2  ENHANCER ROUTE  provider "enhance" button → READ the enhanced prompt → edit it;
                        keep the preserve-list OUTSIDE its rewrite zone.
STEP 3  CHANNEL SETUP   restyle: img2img 0.35–0.55 + preserve-list; geometry-critical:
                        ControlNet depth 0.7–0.8 / Canny 0.9–1.0 / MLSD 0.4–0.6;
                        style: IP-Adapter 0.5–0.7; two-pass lock→style.
STEP 4  VIEW PROBLEMS   another angle? GO BACK TO THE MODEL or reconstruct via image→3D
                        → re-render. NEVER img2img "rotate it" for submittable work.
STEP 5  VERIFY          G1 adherence (atom checklist incl. "no unrequested content")
                        → G2 fidelity harness (IoU/SSIM vs input) → G3 plate audit if the
                        plate asserts dimensions → G4 provenance + disclosure.
STEP 6  SHIP            vector labels, title block, disclosure line, and the log
                        (input, tool, prompt, numbers).
```

## Writing the preserve-list (field 3 LOCKED, kit grammar)

- List **concrete observable features**: bay/window/door counts and positions, footprint edges, roof profile, entrance, circulation, camera viewpoint, framing — and **the projection/view itself** ("east elevation, eye-level, same camera" — the projection invariant was a measured win).
- Distinguish a **measured constraint** (from documents) from a **visual cue** (from pixels). Only the former is LOCKED.
- Alter list = **one bounded change**: a material, a facade zone, lighting, vegetation concept, or a massing **option** — never "make it better."
- A proposed new element is **not** the existing condition and must never silently appear as such.

## Reference roles (field 5, kit grammar)

`Image 1 = geometry/base` · `Image 2 = style only` (never a geometry source — don't copy a style reference's floor plan or building shape) · `Image 3 = annotated edit zone / approved mask` — only if the tool supports the roles; otherwise change tools.

## Practitioner reality check `[O]`

13 of 15 audited real prompts had no preserve-language; both that did were meta-advice, not generation text. Practitioners survive because their geometry channel is ControlNet/Veras/model export — **words carry look, tools carry truth**. If your tool has no geometry channel, the preserve-list is your only geometry defense: use it, and hold expectations accordingly.
