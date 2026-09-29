# Evidence Appendix — Why `@educate` / Horizon Expansion

**Purpose:** Design-of-record backing for the claim: *LLMs often have coverage but not the depth needed for everyday serious use.*  
**Date:** 2026-09-27 · **Skill:** `@educate` v0.1

---

## 1. Problem statement (operational)

Default chat completions optimize for **helpful fluent coverage**. Everyday Commander work needs **depth**: prerequisites, adjacency, multi-hop integration, and source-traceable claims. Without a mandate, the superior AI stops early — the same failure users patch with “educate yourself on X.”

---

## 2. Key findings (literature & industry)

### 2.1 LLM summaries → shallower human knowledge

Melumad & Yun (*PNAS Nexus*): across large experiments, people who learned via **LLM syntheses** developed **shallower knowledge** than those who used **traditional web links**, even when underlying facts were matched. Downstream advice was sparser, less original, and less adopted by others. Mechanism: less active discovery and synthesis effort.

**Implication for `@educate`:** Prefer source-first acquisition and a structured pack over a single polished monologue.

### 2.2 Unused knowledge (not only missing knowledge)

Analyses of model bottlenecks distinguish **missing** vs **unused** knowledge: many errors are failures to **deploy** knowledge that is already latent (“lay-in” broader than working knowledge). Related work shows correct answers often rank high in the distribution while the model still emits a wrong surface answer.

**Implication:** Horizon folds must **activate and express** claims explicitly (with grades), not assume “the model knows.”

### 2.3 Great memory, shallow reasoning

Retrieval-augmented / kNN-style systems can excel at memory-like tasks yet fail when **multiple pieces must be integrated** — even under strong retrieval. Reasoning surveys describe surface pattern matching and brittle multi-step behavior.

**Implication:** Fold **Integrate** is mandatory when core and necessary are both populated.

### 2.4 Breadth vs depth as separate axes

Information-science and alignment work separate **knowledge breadth** (many domains) from **knowledge depth** (complex, narrow competence). DepthCharge-style evaluation shows models that look fine on shallow probes **degrade under adaptive deep follow-ups**.

**Implication:** Horizon Pack tracks depth-oriented content (necessary/procedure/strategy), not only topic count.

### 2.5 Under-exploration / “think too fast”

Empirical work on exploration finds many LLMs under-explore relative to humans; short reasoning traces correlate with weaker open-ended performance versus more deliberate models.

**Implication:** Stop criteria must be **checklist-based**, not fluency-based.

### 2.6 Industry “Deep Research” products

OpenAI Deep Research, Anthropic multi-agent research systems, and open deep-research repos converge on: **plan → multi-step/parallel gather → gap detection → cited synthesis**. That product category exists because default chat is insufficient for depth.

**Implication:** `@educate` adopts the **shape** (mandate + iteration + pack) without adopting multi-agent governance as RADIATION law (one superior AI remains).

---

## 3. Mapping findings → design controls

| Finding | Control in `@educate` |
|---------|------------------------|
| Shallow summary learning | Horizon Pack + source index; not essay-only |
| Unused latent knowledge | Explicit core/necessary claims |
| Weak multi-hop | Integrate fold |
| Breadth≠depth | Necessary + depth_tags; use-case anchor |
| Early exit | stop_reason enum; quota |
| Deep Research pattern | Ordered folds + gap-fill action |
| Tourism risk | CTP on folds; adjacency cap |

---

## 4. Non-claims

- This appendix does **not** claim `@educate` matches commercial Deep Research quality out of the box.  
- It does **not** claim parametric knowledge is empty — only that **expression and integration** are unreliable without process.  
- It does **not** authorize uncited invention to “complete” a horizon.

---

## 5. Selected references (indicative)

- Melumad, S., & Yun, J. H. — Experimental evidence on LLMs vs web search and depth of learning (*PNAS Nexus*).  
- Missing vs unused knowledge framing in patent/understanding bottleneck work (arXiv family).  
- Geng, Zhao, Rush — *Great Memory, Shallow Reasoning: Limits of kNN-LMs* (NAACL).  
- Peng et al. — Knowledge breadth and depth measurement of LLMs (ASIS&T).  
- DepthCharge — depth-dependent knowledge measurement framework (arXiv).  
- OpenAI — Introducing deep research (product note).  
- Anthropic — How we built our multi-agent research system (engineering note).  

Full URLs and versions should be re-verified at Patch time under house citation rules.

---

**End of evidence appendix.**
