# Signal Channels — how a re-image prompt actually works

**Source:** 3D-enhancers leg §1–§5 (Skills repo `docs/`). The model behind every routing decision in this skill.

## The five-channel model

A re-image prompt is not one instruction. It is up to **five signal channels** entering a diffusion/transformer UNet at different layers, with a strict authority hierarchy:

```text
THE AUTHORITY LADDER (who wins when signals disagree):

explicit 3D condition  >  spatial ControlNet  >  image embedding  >  text
```

Text is the **weakest** channel. When the structural signal and the text disagree, the structural signal wins. Consequences:

- "Exact," "unchanged," "photoreal" in text lock **nothing** — pixels, geometry, dimensions, identity and unseen surfaces are not controlled by adjectives.
- If geometry must hold, put geometry in a **stronger channel** (ControlNet, model export, viewport, GIS layers) and let text carry only look.
- The judge-side catch `[R]`: enhancement changes what auditors measure — an enhanced prompt can shift the evaluation itself; keep the frozen intent outside any rewrite zone.

## "3D re-imagine" is three different transactions

Before routing any 3D request, decide which transaction it actually is:

1. **A picture** (one rendered view) — D01/D02 class; text-to-3D or single-photo speculative prop.
2. **An editable asset** (mesh you will modify) — D03/D04/D08 class; multi-view input, real topology, UV retention.
3. **A printable object** — D07 class; visible texture is not printable relief; scale/budget rules differ.

Wishing for one and requesting another is the classic failure; the router asks first.

## Spatial vocabulary as prompt equipment `[O]`

State **exactly what projection you want** — plan / elevation / section / eye-level / aerial / perspective — as an explicit invariant in the preserve-list (the projection invariant was a measured win: it prevents silent viewpoint drift). Practitioners' only fully-compliant captured prompt (the corpus comparator) was the one combining explicit projection terms with a preserve-list; every other captured prompt left the view to chance.

## Enhancer classes (evidence-ranked, 3D leg §2)

| Class | Evidence | Use |
|---|---|---|
| Research enhancers (peer-reviewed prompt-transform methods) | `[R]` | Candidate rewrites — never final without read-back |
| Provider-shipped "enhance" buttons | `[D]` | Read the enhanced prompt, edit it, keep the preserve-list outside its rewrite zone |
| Image→prompt ("reverse prompt") captioning nodes (Florence-2 / Qwen2.5-VL class) | `[D]/[O]` | Describing a base image; candidate text, never final |
| Local LLM rewrite | `[O]` | Candidate generator only |

All enhancers **expand look-fields**; none may touch the frozen intent.

## What "better re-imagination" actually is

A **parameter stack**, not a better model: base quality (≥1920px clean own capture) + preserve-list prompt + correct channel setup + measured verification (IoU/SSIM bands) + provenance. The measured experiment changed none of the model and doubled fidelity. Quality claims that skip the stack are styling advice, not re-imagination control.
