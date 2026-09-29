# Evidence Appendix — Problem-Formation / Always-on Clarify–Reframe

**Purpose:** Back the design: underspecified asks need a **compliance gate**, not optional skill hope.  
**Date:** 2026-09-27 · **Package:** clarify_subskill v0.1

---

## 1. Problem statement

User tasks are often incomplete or multi-interpretable. Default LLM behavior is to **answer under a hidden interpretation**. That produces wrong plans, wrong tools, and confident waste. RADIATION already has `NEEDS_CLARIFY` hooks; it lacks a full **when / what / stop** process that forces recognition into behavior.

---

## 2. Key findings

### 2.1 Knowing but not showing

Su & Cardie (2026): models often **detect** ambiguity in judgment settings but in standard QA **default to direct answers**. Retrieved context increases answerability and **further suppresses** clarifying questions.

**Design implication:** Optional `@clarify` will be skipped under the same bias. **Always-on gate** is required so detection becomes path selection (ASK/REFRAME/ASSUME), not silent completion.

### 2.2 When to clarify (not always)

- **Clarify when necessary** frameworks: decide *when*, *what*, then answer with new info; uncertainty over **intents** (e.g. Intent-Sim) beats raw confidence alone.  
- Practice guidance: ask when the answer **materially changes work** or **raises risk**; else proceed and **state assumptions**.  
- Over-clarification harms autonomy; under-clarification harms correctness.  

**Design implication:** Paths **PROCEED / ASSUME / ASK / REFRAME / CONFIRM** — always *checked*, not always *asked*.

### 2.3 Agents and incomplete instructions

Tool-calling agents fail when instructions omit parameters; structured uncertainty / EVPI-style selection improves coverage while **reducing** question count. “Ask when Needed” prompting improves tool accuracy on unclear instruction benchmarks. ClarifyMT-Bench: models **under-clarify** as dialogue deepens.

**Design implication:** Gate before PLAN/tool effects; cap questions; stop rules.

### 2.4 Reframe alongside ask

Rephrase-and-Respond, ambiguity-guided query rewrite, and input reformulation for agents show that **sharpening the problem statement** (not only interrogating the user) improves outcomes. Rewrite-everything is harmful; rewrite **when ambiguity detected**.

**Design implication:** **REFRAME** is first-class next to **ASK**.

### 2.5 Provider / constitution direction

Anthropic agent and constitution-adjacent public materials emphasize: pause for clarification under genuine ambiguity; balance against constant interruption; train recognition of when only the user can settle intent vs when the agent can resolve.

**Design implication:** Aligns with Commander-rank + honest assumptions; CONFIRM for high-impact acts.

---

## 3. Mapping → RADIATION controls

| Finding | Control |
|---------|---------|
| Knowing but not showing | Always-on intake gate (not skill-only) |
| Material vs minor gaps | PROCEED / ASSUME / ASK / REFRAME / CONFIRM |
| Question cost | ≤3 ranked; value-of-information line |
| Reframe helps | REFRAME path + assumptions + original preserved |
| Tool wrong-path risk | Gate before neuron PLAN / control-plane effects |
| Neuron NEEDS_CLARIFY | Implement with Problem-Formation receipt |

---

## 4. Non-claims

- Does not claim host models will match trained clarification specialists without process.  
- Does not authorize inventing Commander intent.  
- Does not require multi-agent swarm for clarification.

---

## 5. Indicative references

- Su & Cardie — *Knowing but Not Showing: LLMs Recognize Ambiguity but Rarely Ask Clarifying Questions*  
- Zhang, Knox, Choi — Modeling future turns to teach clarifying questions  
- Clarify when necessary / Intent-Sim line of work  
- Structured uncertainty guided clarification for LLM agents (EVPI-style)  
- Ask-when-Needed / NoisyToolBench-style agent instruction work  
- ClarifyMT-Bench — multi-turn clarification under-clarification bias  
- Rephrase and Respond (RaR); Ambiguity-guided query rewrite  
- Anthropic — trustworthy agents / clarification vs autonomy balance  

Re-verify URLs and versions at Patch time under house citation rules.

---

**End of evidence appendix.**
