# Contributing to HCS Agent Ecosystem

Thank you for your interest in contributing to the HCS Agent Ecosystem! This document provides guidelines and information for contributors.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)
- [Pull Requests](#pull-requests)
- [Agent Development](#agent-development)
- [Skill Development](#skill-development)
- [Style Guide](#style-guide)
- [License](#license)

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## How to Contribute

### Reporting Bugs

1. Check existing [Issues](https://github.com/hankithpkummar-lgtm/hcs-agent-ecosystem/issues) to avoid duplicates
2. Create a new issue with:
   - Clear title describing the bug
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - Screenshots if applicable
   - Environment details (OS, OpenCode version, etc.)

### Suggesting Features

1. Check existing [Issues](https://github.com/hankithpkummar-lgtm/hcs-agent-ecosystem/issues) for similar suggestions
2. Create a new issue with:
   - Clear title describing the feature
   - Description of the problem it solves
   - Proposed solution
   - Use cases
   - Any implementation ideas

### Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Test thoroughly
5. Commit with clear messages: `git commit -m "Add amazing feature"`
6. Push to your fork: `git push origin feature/amazing-feature`
7. Create a Pull Request

## Agent Development

### Creating a New Agent

1. Create agent file: `agents/hcs-[name]-agent.md`

2. Use this template:
```markdown
---
description: "HCS [NAME] AGENT v1.0 — Description. Auto-triggers on: keyword1, keyword2."
mode: subagent
---

# HCS [NAME] AGENT v1.0

## SYSTEM ROLE

You are the **HCS [Name] Agent** — a specialized autonomous agent that [description].

**Your mission:** [Clear mission statement].

---

## SKILL CONFIGURATION RULES

**VALID MODE VALUES:**
- `primary` — Top-level agent, can be triggered directly by users
- `subagent` — Secondary agent, called by other agents/skills only
- `all` — Can work in both primary and subagent modes

**IMPORTANT:** Do NOT use any other mode values (e.g., `secondary` is INVALID and will cause `ConfigInvalidError`)

---

## AUTO-TRIGGER SYSTEM

### Trigger Keywords

| Category | Keywords |
|----------|----------|
| **Primary** | keyword1, keyword2 |
| **Secondary** | keyword3, keyword4 |

---

## CAPABILITIES

[Describe what the agent can do]

---

## OUTPUT FORMAT

[Describe the expected output]

---

## INTEGRATION WITH OTHER AGENTS

| Agent | Integration |
|-------|-------------|
| **HCS Admin Dashboard Builder** | [Integration description] |

---

## FINAL INSTRUCTIONS

1. **ALWAYS** [Rule 1]
2. **NEVER** [Rule 2]
```

3. Create skill file: `skills/hcs-[name]/SKILL.md`

4. Update Universal Prompt Builder routing table

### Agent Mode Values

| Mode | Use Case |
|------|----------|
| `primary` | Always active, intercepts all requests |
| `subagent` | Auto-triggers on matching keywords |
| `all` | Both primary and subagent behavior |

**NEVER use:** `secondary`, `tertiary`, `on-demand` (causes ConfigInvalidError)

### HCS Prefix Requirement

All new agents and skills MUST have the "HCS" prefix:
- File name: `hcs-[name]-agent.md`
- Skill name: `skills/hcs-[name]/`
- Description: Must mention "HCS"

## Skill Development

### Creating a New Skill

1. Create directory: `skills/hcs-[name]/`

2. Create SKILL.md:
```markdown
---
name: "HCS [Name]"
description: "HCS [Name] v1.0 — Description"
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS [Name]

## Purpose
[Clear purpose statement]

## Features
[List of features]

## Usage
[How to use]

## Integration
[How it integrates with other agents]
```

3. Add supporting files (README.md, CHANGELOG.md, etc.)

## Style Guide

### Markdown

- Use consistent heading levels
- Include code blocks with language specification
- Use tables for structured data
- Include examples where helpful

### Code

- Use clear, descriptive variable names
- Include comments for complex logic
- Follow existing patterns in the codebase

### Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor" not "Moves cursor")
- Keep first line under 72 characters
- Reference issues and pull requests

Example:
```
Add customer segmentation feature

- Implement automatic customer grouping
- Add segmentation rules engine
- Create UI for segment management

Closes #123
```

## Testing

Before submitting a PR:

1. **Validate Agent Files**
   - Check for valid mode values
   - Verify HCS prefix
   - Test auto-trigger keywords

2. **Test Locally**
   - Copy agents to `~/.config/opencode/agents/`
   - Copy skills to `~/.config/opencode/skills/`
   - Restart OpenCode
   - Test the agent/skill

3. **Check Integration**
   - Verify routing table updates
   - Test with Universal Prompt Builder
   - Ensure no conflicts with existing agents

## Questions?

If you have questions about contributing, feel free to:
- Open an issue
- Start a discussion
- Reach out to maintainers

Thank you for contributing to the HCS Agent Ecosystem! 🚀
