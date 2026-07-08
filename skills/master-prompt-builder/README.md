# Master Prompt Builder

**Version:** 1.0.0  
**Trigger:** `prompt-builder`  
**Category:** Prompt Engineering, Automation, Coding, AI

---

## Overview

Master Prompt Builder is a **lightweight, auto-executing prompt engine** that converts any natural language request into an optimized, structured prompt and sends it directly to the coding model.

**No approval gates. No delays. Just build.**

## How It Works

```
Your Request → Analysis → Prompt Generation → Auto-Execute → Building Starts
```

1. **Type any request** in natural language
2. **Skill analyzes** intent, domain, and complexity
3. **Generates optimized prompt** with all context
4. **Auto-selects** the best model for the task
5. **Sends prompt** to coder immediately
6. **Building begins** automatically

## Installation

This skill is installed at:
```
~/.config/opencode/skills/master-prompt-builder/
```

## Usage

### Basic Usage

```
prompt-builder: Build a calculator app with dark mode
```

### Shorthand

```
mpb: Add a loading spinner to the dashboard
```

### Any Alias Works

```
build-prompt: Create a user profile page
convert-prompt: Fix the login form validation
optimize-prompt: Add search functionality
auto-prompt: Build an admin panel
```

## Examples

### Simple Request

**You type:**
```
prompt-builder: Add a loading spinner to the dashboard
```

**What happens:**
1. Detects: Simple UI task
2. Generates: Focused prompt with requirements
3. Auto-executes: Sends to fast model
4. Building starts: Immediately

### Medium Request

**You type:**
```
mpb: Create a user profile page with edit functionality
```

**What happens:**
1. Detects: New component with multiple files
2. Generates: Detailed prompt with file structure, data models
3. Auto-executes: Sends to standard model
4. Building starts: Immediately

### Complex Request

**You type:**
```
prompt-builder: Build an admin dashboard with analytics and user management
```

**What happens:**
1. Detects: Multi-module feature
2. Generates: Full master prompt with architecture
3. Routes: To universal-master-dev-agent-v3 for full pipeline
4. Building starts: After brief confirmation

## Complexity Levels

| Level | Examples | Action |
|-------|----------|--------|
| **SIMPLE** | "Add a button", "Change color", "Fix typo" | Auto-execute immediately |
| **MEDIUM** | "Create a component", "Add a form", "New page" | Auto-execute with expanded prompt |
| **COMPLEX** | "Build dashboard", "Admin panel", "Full feature" | Auto-execute with detailed prompt |
| **ARCHITECTURAL** | "New project", "Complete rewrite", "Microservices" | Route to full pipeline |

## Model Selection

The skill automatically selects the best model:

| Task | Model |
|------|-------|
| Simple fixes | GPT-3.5 / Claude Haiku (fast) |
| UI components | Claude / GPT-4 |
| Backend/API | Claude / GPT-4 |
| Architecture | GPT-4 Opus / Claude Opus |

## Configuration

### config.json

```json
{
  "name": "master-prompt-builder",
  "version": "1.0.0",
  "settings": {
    "auto_execute": true,
    "complexity_threshold": "medium",
    "route_architectural": true,
    "default_model": "auto"
  }
}
```

### Settings

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `auto_execute` | boolean | `true` | Send prompts to coder without approval |
| `complexity_threshold` | string | `"medium"` | Max complexity for auto-execute |
| `route_architectural` | boolean | `true` | Route complex tasks to full pipeline |
| `default_model` | string | `"auto"` | Model selection strategy |

## How It Differs from universal-master-dev-agent-v3

| Feature | Master Prompt Builder | Universal Master Dev Agent |
|---------|----------------------|---------------------------|
| **Speed** | Instant | Full pipeline (minutes) |
| **Approval** | None for simple/medium | Always required |
| **Agents** | 1 (prompt builder) | 15 specialized agents |
| **Best for** | Quick tasks, fast iteration | Complex projects, full lifecycle |
| **Auto-execute** | Yes | No |

## When to Use Which

### Use Master Prompt Builder when:
- Quick UI tweaks
- Simple features
- Fast iteration
- Bug fixes
- Content updates
- Any task under 30 minutes

### Use Universal Master Dev Agent when:
- New projects from scratch
- Complex multi-module features
- Security-critical systems
- Production deployments
- Architecture decisions
- Full audit needed

## Quick Reference

| Command | Action |
|---------|--------|
| `prompt-builder [request]` | Convert + Build |
| `build-prompt [request]` | Same |
| `mpb [request]` | Shorthand |
| `auto-prompt [request]` | Same |

## Troubleshooting

**Issue:** Skill not triggering
**Solution:** Try `prompt-builder` or `mpb` as the trigger word.

**Issue:** Prompt seems incomplete
**Solution:** Provide more details in your request. The skill infers what it can.

**Issue:** Wrong model selected
**Solution:** Specify model in request: "Use GPT-4 to build..."

## Contributing

Contributions welcome. See the main OpenCode skills repository.

## License

MIT

---

**Remember:** Type your request, get building. No delays.
