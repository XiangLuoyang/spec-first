# Case 001 — spec-first loopen intake (2026-06-20)

> **Purpose**: First case captured by skill-loopen's `real-with-case-capture` mechanism.
> Saved automatically after skill-loopen intake completed on spec-first.
> This case becomes a practice/performance sample for spec-first's own training.

## Context

- **Date**: 2026-06-20 21:30 - 21:57 GMT+8
- **Channel**: feishu (direct chat)
- **Trigger**: 用户 said "Loopen一下我的spec-first的skill"
- **Pre-condition**: skill-loopen v0.1.0 just shipped (commit 117b376), GLM-5.2 newly set as primary model

## Intent (Stage 1: Problem)

用户 wants spec-first to be **loop-empowered** — to gain self-iteration capability through skill-loopen.
Real goal: make spec-first's "think clearly before doing" human-AI interaction continuously improve, avoiding formalism, and dimension-coverage gaps.

## Solution options (Stage 2: Design)

AI proposed 4 intake answers based on spec-first's nature (design-phase skill, frequent use, core tool):

| Question | AI proposed | 用户 revised |
|----------|-------------|----------------|
| Q2 objectives | accuracy + drift-resistance + robustness | + **ux-iteration** (human-AI interaction experience as iteratable dimension) |
| Q3 sample source | synthetic + real | synthetic + **real-with-case-capture** (each invoke auto-saves case snapshot) |
| Q4 policy | mixed | (no change) |
| Q5 cadence | 50 runs / 30 days | (no change) |

**Key AI choice + human override pattern**:
- AI was right about the *direction* (mixed policy, 50/30 cadence)
- AI missed *iteration dimensions* (ux-iteration) and *mechanism upgrades* (case-capture)
- 用户's revisions show: they value **meta-level iteration** (iteration about the iteration process itself)

## Plan (Stage 3)

1. Generate 4 LOOP files (LOOP.md / practice-log.md / evolution-report.md / drift-check.md)
2. Create `cases/` directory in spec-first (case-capture mechanism)
3. Save THIS case as case 001
4. **Recursive**: Save the same intake as a case in skill-loopen's own case library (meta-dogfood)

## Use Case preview (Stage 4)

After this intake:
- spec-first has explicit training objectives, sample sources, decision policy
- Each real-world spec-first invocation auto-saves a case to `cases/`
- Every 50 runs or 30 days, a report evaluates: ux-iteration health, drift, accuracy trends
- spec-first can improve autonomously (low-impact changes) or with human gate (high-impact)

## Execute (Stage 5)

- ✅ spec-first/LOOP.md (4733 bytes) generated
- ✅ spec-first/practice-log.md (644 bytes, empty header)
- ✅ spec-first/evolution-report.md (242 bytes, empty header)
- ✅ spec-first/drift-check.md (712 bytes, indicators defined)
- ✅ spec-first/cases/ created
- ✅ spec-first/cases/001-spec-first-loopen-intake.md (this file)
- ⏳ spec-first SKILL.md **NOT YET UPDATED** to reference LOOP.md / cases/ (Stage 6 of spec-first's own flow)

## Outcome

- **Status**: Intake complete, files generated. spec-first is now loop-empowered.
- **Files added to spec-first**: 5 (4 LOOP + 1 case)
- **Recursive case**: also saved in skill-loopen's case library
- **Next**: ux-iteration is a new dimension — needs real practice sessions to start generating signal

## Learnings (Stage 7: Compound)

### Insight 1: "ux-iteration" is a meta-dimension

accuracy / drift-resistance / robustness measure **output quality**.
ux-iteration measures **interaction quality** — the second-order question of "is the *process* of getting output good?"

This is the "form follows function" insight applied to skill design: a skill's *interaction design* is itself a dimension to iterate on, not just its output.

### Insight 2: case-capture is mechanism, not just data

"real + case-capture" is not a sample source — it's a **learning infrastructure**.
Without case-capture, real samples are ephemeral (in conversation history).
With case-capture, real samples accumulate into a **case library** that can be re-read, re-played, re-evaluated.

This is the difference between "we used the skill" and "the skill learned from being used."

### Insight 3: Recursive dogfood (this case)

This intake IS a case for skill-loopen itself.
- skill-loopen just got a real usage (first invoke)
- That usage is now a case in skill-loopen's own library
- Future skill-loopen sessions can dogfood against this case (how did the first intake go? was the proposal right? did the user's revisions improve the outcome?)

This is **self-bootstrapping** — the skill improves from its own first use, recursively.

## Sample for future practice

```yaml
case_id: 001
date: 2026-06-20
skill: spec-first
mode: intake (first-ever)
outcome: success with 2 human revisions
revisions:
  - ux-iteration added
  - case-capture mechanism added
key_observation: ux-iteration + case-capture are the *innovations* of this intake
```
