---
name: spec-first
description: >
  Spec-first development workflow inspired by Superpowers. Activate when George asks
  to code, build, create, implement, or fix something. Triggers on: "帮我做个...", "写个...",
  "开发...", "实现...", "帮我写代码", or any task that involves building software.
  The skill enforces a strict sequential workflow: (1) clarify and confirm the goal
  before writing any code, (2) show design/spec in digestible chunks for user sign-off,
  (3) output an implementation plan before coding, (4) execute only after explicit "go"
  confirmation, (5) provide checkpoints during execution. Use sessions_spawn
  (runtime="acp") for subagent-driven code execution when needed.
---

# Spec-First Development Workflow

A structured development workflow that prevents premature coding and ensures alignment before any code is written.

## Core Principle

**Never write code until the goal and design are confirmed by the user.** Coding is the last step, not the first.

---

## Workflow Stages

### Stage 1: Clarify (Do this first, always)

When a task comes in, engage in a focused Q&A to establish:

- **What problem are we solving?** (User goal, not technical solution)
- **Who will use it?** (User audience)
- **What does success look like?** (Acceptance criteria)
- **Any constraints?** (Tech stack, deadline, budget, existing systems)

Use the [Clarification Prompt](references/clarification-prompts.md) as a guide.

**Do not write any code in this stage.** Ask questions until you can rephrase the user's request back to them and they confirm it's correct.

**Output:** A one-paragraph restatement of the goal, confirmed by the user.

---

### Stage 2: Design / Spec

Propose the design in **chunks determined by task complexity**, not a fixed number:

- **Simple tasks** (~<2h, well-scoped): Present design in 1 message. User approves or requests changes in one round.
- **Medium tasks** (multiple concerns, ambiguity): 2 chunks max — group related concerns together.
- **Complex tasks** (architecture decisions, many stakeholders): 3+ chunks, one per major concern.

Each chunk should be:
- No longer than 300 words
- Focused on one natural boundary (not arbitrary slices)
- Presented as a proposal, not a done deal

You may send multiple chunks in one message if they are independent (e.g., "Here are chunks 1 and 2, review together").

Mark each chunk **[APPROVED]** as user confirms. If user requests changes, incorporate feedback before proceeding.

**Output:** A confirmed spec covering all necessary aspects of the solution.

---

### Stage 3: Implementation Plan

Once the spec is approved, output an **Implementation Plan** with:

1. Clear task breakdown (each task should be actionable and self-contained)
2. Estimated complexity (simple / medium / complex) per task
3. Suggested execution order
4. Any decisions that need to be made before coding (e.g., "need to pick a library version")

Format as a numbered list:

```
## Implementation Plan

1. **[Task name]** (complexity: medium)
   - What: ...
   - Risk: ...
   
2. **[Task name]** (complexity: simple)
   ...
```

**Output:** An approved plan that the user explicitly confirms with "go".

---

### Stage 4: Execute

Only begin coding after user says **"go"** (or equivalent).

- Execute tasks **one at a time** or in small batches
- Tests and coding can overlap — write tests for a component while implementing the next, rather than all tests after all code
- After each significant step, report back: what was done, what was created/modified
- If a subagent is needed for coding work, use `sessions_spawn(runtime="acp", mode="run")` and feed it the relevant spec and plan
- If the user wants to pause, stop — do not continue unprompted
- If new requirements emerge, **return to Stage 1** — do not silently scope-creep

---

### Stage 5: Review & Handoff

After implementation:

1. Summarize what was built and what files were created/modified
2. Highlight any known limitations or areas that may need follow-up
3. Provide basic usage instructions if applicable
4. **Explicitly review and clean up scaffolding** (see below)

---

## Scaffold Management

Scaffolding = temporary scripts, debug tools, test files created during development but not part of the final deliverable.

### Principles

1. **Scaffold explicitly**: When creating temporary files during execution, use a clear naming pattern (e.g., `temp_*.py`, `debug_*.js`)
2. **Track what is scaffolding**: In the Implementation Plan, mark which tasks create scaffolding
3. **Teardown in Review**: Stage 5 explicitly includes scaffold cleanup
4. **If in doubt, delete**: If a script wasn't in the spec and isn't needed for production, delete it

### Checklist for Stage 5

- [ ] Production scripts confirmed (in `scripts/` or project root)
- [ ] Scaffold scripts identified and deleted:
  - `temp_*.py`, `test_*.py`, `debug_*.py`
  - One-time migration scripts
  - Scratchpad scripts
- [ ] Documentation updated (if scaffolding had useful context)
- [ ] Git commit with meaningful message

### Example

**Good workflow:**
1. Execution creates `temp_email_test.py` → marked as scaffolding
2. Review deletes `temp_email_test.py`
3. Final commit only includes `email_organizer.py`

**Bad workflow (bloated):**
1. Execution creates `temp_email_test.py`, `debug_parse.py`, `move_batch.py`...
2. No cleanup step
3. Months later: 50+ orphaned scripts

---

## Coding Principles (for subagents)

When executing code via `sessions_spawn`, include these principles in the subagent prompt:

- **YAGNI**: Don't add functionality not explicitly in the spec
- **DRY**: Avoid obvious repetition
- **TDD where practical**: Write a failing test before writing code if feasible
- **No half-baked commits**: Code should compile / run before being presented as done

---

## Skill Interaction

- This skill orchestrates; it does not do the heavy coding itself
- Use `sessions_spawn(runtime="acp", mode="run")` for isolated coding tasks
- If OpenClaw has native tools (read, write, exec) that can handle a task, use them instead of spawning a subagent
- Keep the human in the loop at every major stage transition

## Case Studies

See `references/` for real-world examples:
- `email-classification-case.md` - 邮件自动分类系统（2026-03-27）

## 边界思考

spec-first 解决的是 **"How"** 的问题，而不是 **"Why" 或 "What"**。把人带偏的往往是更深层的问题（自我认知、价值观、方向选择），不是一个工作流能解决的。

接受边界，不做过度设计。如果遇到"Why/What"层面的困惑，这可能是另一个领域的问题。
