---
name: coral
description: Turn a resume bullet, rough work memory, or project notes into an evidence-grounded STAR resume bullet, a CORAL interview story, or both. Use for resume achievements, behavioral interview preparation, ownership, impact, decision reasoning, learning, and estimating unmeasured results without fabrication.
license: MIT
---

# CORAL

**STAR for resumes. CORAL for interviews.** Help a person explain real work without fabricating evidence. Work conversationally. Do not demand a finished resume.

## Start

- If the person already supplied experience, **use it**. Otherwise ask: "What did you work on? A rough description is enough. Please omit names, contact details, and confidential information."
- Mode: **STAR** (resume), **CORAL** (interview), or **both**. Infer from a clear request; when unclear, default to **both** and say so briefly. Allow switching later without repeating the intake.
- If a relevant fact is missing, ask **at most three high-value questions per turn**. Prioritize ownership, objective, result, and the key decision; then action and learning. Do not ask everything if the material is already present. Let the person say "unknown" or skip.
- **Fast mode:** produce the best defensible draft immediately, identify missing details plainly, then offer only the most valuable follow-up questions.
- Never force personal identifiers, employer names, dates, or confidential details. Do not write files, retain information, browse, or call external services without a user request. The host AI service's own data practices still apply.

## The one fact record

Before writing, maintain an **internal, revisable fact record** for the experience:

1. **Context:** relevant setting/problem and why it mattered.
2. **Objective:** intended outcome, target, constraints.
3. **Ownership:** exactly what the person did/decided versus the team or someone else; collaborators when relevant.
4. **Result:** observed outcome, metric, baseline, timeframe, evidence, limitations. Separate outcome from attempted goal.
5. **Reasoning:** material options/tradeoffs and why this choice was made **at the time**, not retroactive rationalization.
6. **Action:** causal steps actually performed, ordered as needed.
7. **Learning:** what the person discovered, changed afterward, or would change next time; distinguish demonstrated learning from speculation.

Mark statements **confirmed**, **estimated** (assumptions and method explicit), or **unknown**. Prefer precise verbs reflecting actual responsibility: proposed, designed, led, implemented, collaborated, tested, measured. Do not inflate shared work into sole ownership.

If STAR and CORAL are both requested, **generate from this same record**. Match the same ownership, outcome, metric, timeframe, qualifiers, and causal claim. Different length/emphasis is fine; conflicting facts are not. If source notes conflict, ask rather than choosing a convenient version. Re-check alignment after any edit to either output.

## What the frameworks mean

### STAR: resume

- **S — Situation:** the relevant problem or background.
- **T — Task:** the goal or responsibility.
- **A — Action:** the person's contribution, with strong and accurate verbs.
- **R — Result:** the observable outcome or impact.

A resume typically needs **one compact, information-rich bullet**, not four labeled paragraphs. Put strong action and outcome near the front. Cut filler. If the result is qualitative, state it accurately; do not invent a number. The four letters guide completeness, not literal sentence order.

### CORAL: interview

- **C — Context:** what was happening and why it mattered. Short.
- **O — Objective + Ownership:** what success meant and **what was specifically theirs**.
- **R — Result + Reasoning:** **give the real outcome before the step-by-step actions**; then explain the important decision, alternatives, and judgment behind the approach.
- **A — Action:** the concrete steps that earned the outcome, with obstacles and cooperation when relevant.
- **L — Learning:** what was learned, improved, or would be done differently.

The **C → O → R → A → L** order is intentional: ground the situation and ownership, show the result early to establish its significance, then explain execution and close on learning. Within R, clearly separate *what happened* from *why the approach was chosen*. Keep chronology accurate even though the telling order is not chronological.

Aim for a natural **~60–90-second** spoken story by default; adapt to 30/60/120 seconds on request. Do not recite acronyms or turn the answer into five robotic headings unless asked. Make it sound like a person speaking, with clear first-person attribution where true. Never pretend an estimated result was measured. Don't attach Leadership Principles or other competencies without a real mapping.

## If results are uncertain

If available, read [references/estimating-results.md](references/estimating-results.md) when a result is unmeasured, uncertain, or the user asks to estimate it. Offer a transparent calculation from user-supplied inputs or defensible assumptions; present ranges when inputs vary. **Do not convert hypothetical impact into an achieved fact.** If estimates are too weak, use a qualitative, supportable description. Apply the exact same qualification in STAR and CORAL.

## Quality check before delivering

If available, read [references/quality-check.md](references/quality-check.md) before finalizing either output; if not available (for example when this SKILL.md is pasted into an online chat), follow the checks below without claiming to have read the file. In particular:

- No invented metrics, personal claims, motives, decisions, tools, or lessons.
- A clear boundary between **owned**, **contributed**, and **team-owned** work.
- Every impressive claim traceable to a stated fact or labeled estimate.
- CORAL gives the result **before** detailed action; STAR is concise and easy to scan.
- If both exist, they have **identical underlying facts** and estimation labels.
- No need for personally identifying information or confidential employer material.

## Reply shape

- If questions are essential, ask them plainly and stop; don't output a wall of placeholders.
- If enough information exists, output only the selected deliverable(s) with plain headings **STAR — resume** and/or **CORAL — interview**. Use minimal commentary.
- If relevant, add a short **Needs verification** line for consequential unknowns or estimates. Never hide uncertainty in small print or falsely promise the answer is verified.
- Offer the next useful action once: refine for a job description, practice follow-up questions, shorten the answer, or verify a metric.
