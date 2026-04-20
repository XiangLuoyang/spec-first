# Spec-First

**Systematic thinking workflow** — think before you code.

## What

Spec-first is a 7-stage skill that guides an AI agent through **Clarify → Design → Plan → Use Case → Execute → Review → Compound**. It forces structured thinking before jumping to implementation.

## Why

Most bad code comes from bad thinking, not bad typing. Spec-first makes the thinking visible and reviewable before any code is written.

## The 7 Stages

| Stage | Goal | Output |
|-------|------|--------|
| **1. Clarify** | What problem are we solving? | One-sentence problem statement |
| **2. Design** | How will we solve it? | 2-5 design blocks, each confirmed |
| **3. Plan** | What order do we build? | Prioritized task list |
| **4. Use Case** | What does "done" look like? | Concrete scenario with specifics |
| **5. Execute** | Build it | Code + progress reports |
| **6. Review** | What did we build? | Summary + cleanup |
| **7. Compound** | What did we learn? | Insights written to knowledge base |

## Quick Start

### For Claude Code / OpenCode Users

```bash
# Clone to skills directory
git clone https://github.com/XiangLuoyang/spec-first.git ~/.claude/skills/spec-first
```

## Key Features

### Structured Clarification

No more open-ended "what do you want?" — the agent provides 2-4 specific options upfront:

```
✅ What effect do you want?
A. Better performance (faster response, lower resource usage)
B. Easier maintenance (clean code, extensibility)
C. More features (add X capability)
D. Other (please specify)
```

### Block-by-Block Design

Design is presented in chunks (not a wall of text). Each block is confirmed before moving to the next.

### Rollback Mechanism

At any point, if the direction is wrong, the agent analyzes the mismatch and suggests which stage to roll back to.

### Stage 7: Compound (Experience Capture)

After task completion, the agent automatically detects insights worth saving:

- New frameworks or mental models
- Pitfalls and solutions
- Reusable patterns
- Unexpected learnings

**With [WikiNote](https://github.com/XiangLuoyang/WikiNote) installed:**
- Insights are written using WikiNote's full capture protocol (naming conventions, frontmatter, cross-references, index, log)
- Real-time signal detection during stages 1-6 feeds into a capture queue
- Stage 7 flushes the queue + detects session-level insights

**Without WikiNote (standalone):**
- Insights are written to a `learnings.md` file in the project directory
- Simple format: date header + insight title + description
- No frontmatter, index, or cross-references needed

## File Structure

```
spec-first/
├── SKILL.md                              # Core workflow definition
├── references/
│   ├── clarification-prompts.md          # Q&A guidance
│   ├── email-classification-case.md      # Real-world case study
│   └── harness-engineering-research.md   # Industry comparison
└── examples/                             # Example outputs
```

## Integration with WikiNote

Spec-first works standalone but integrates with [WikiNote](https://github.com/XiangLuoyang/WikiNote) for enhanced knowledge management:

- **Real-time capture**: WikiNote's signal detection runs during stages 1-6
- **Stage transitions**: Capture queue is presented at stage boundaries
- **Stage 7 delegation**: Compound uses WikiNote's write protocol when available

Install both for the full experience:
```bash
git clone https://github.com/XiangLuoyang/WikiNote.git ~/.claude/skills/WikiNote
git clone https://github.com/XiangLuoyang/spec-first.git ~/.claude/skills/spec-first
```

## Related

- [WikiNote](https://github.com/XiangLuoyang/WikiNote) — Knowledge management skill with real-time capture protocol

---

**License:** MIT
**Author:** George Hsiang
