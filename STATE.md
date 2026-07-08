# HCS STATE.md
# Memory System for HCS Agent Ecosystem
# Last Updated: [TIMESTAMP]

## Purpose

This file tracks verified facts, general rules, open failures, lessons learned, and session checkpoints across all HCS agent operations.

**Read at session start. Write before walking away.**

---

## Verified Facts (Stage 3)

_Facts that have been verified with evidence. Don't re-derive these._

| Fact | Evidence | Verified By | Timestamp |
|------|----------|-------------|-----------|
| [fact] | [source] | [agent] | [time] |

---

## General Rules (Stage 4)

_Rules derived from specific cases. Apply to future tasks._

| Rule | Derived From | Applies To |
|------|--------------|------------|
| [rule] | [specific case] | [future scenario] |

---

## Open Failures (Stages 1-2)

_Failures that need investigation or are still in progress._

| Failure | Symptom | Investigation Status | Next Step |
|---------|---------|---------------------|-----------|
| [failure] | [symptom] | [status] | [next] |

---

## Lessons Learned (Stage 4)

_Distilled lessons from past sessions._

| Lesson | How Learned | When to Apply |
|--------|-------------|---------------|
| [lesson] | [experience] | [scenario] |

---

## Last Session (Stage 5)

_Session checkpoint for resumption._

- **Timestamp:** [last session time]
- **Checkpoint:** [where we left off]
- **Next Action:** [what to do next]
- **Blocking Issues:** [any blockers]

---

## Usage Protocol

### Before Every Session:
1. Read this file
2. Load relevant lessons
3. Resume from last checkpoint

### After Every Session:
1. Write verified facts
2. Distill general rules
3. Record open failures
4. Update last session pointer

### Memory Progression:
1. **Fail** → Document failure with detail
2. **Investigate** → Diagnose root cause
3. **Verify** → Turn guess into checked fact
4. **Distill** → Create general rule
5. **Consult** → Read rule next task
