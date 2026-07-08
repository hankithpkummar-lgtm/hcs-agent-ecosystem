# OpenCode Skill Builder - Examples

## Table of Contents

1. [Basic Usage](#basic-usage)
2. [Create a New Skill](#create-a-new-skill)
3. [Update an Existing Skill](#update-an-existing-skill)
4. [Get Help](#get-help)
5. [Advanced Examples](#advanced-examples)

---

## Basic Usage

### Activate the Skill Builder

```
skill-builder
```

### Using Aliases

```
builder
create-skill
new-skill
edit-skill
update-skill
skill-manager
skill-factory
```

---

## Create a New Skill

### Example 1: Data Analysis Skill

**User:**
```
skill-builder: Create a skill for analyzing CSV data and generating reports
```

**AI Response:**
```
I'll help you create a new OpenCode skill. Let me start by collecting requirements.

## Basic Questions

1. What is the skill name?
   → data-analyzer

2. What is the purpose?
   → Analyze CSV data and generate insights

3. Who will use this skill?
   → Data analysts, researchers, business users

4. What input does it accept?
   → CSV files

5. What output does it produce?
   → Markdown reports with charts

[... interview continues ...]

## Requirement Expansion

Based on your requirements, I suggest these additional features:

1. Data validation — Ensure CSV structure is correct
2. Chart generation — Visualize data trends
3. Export options — Multiple output formats (PDF, HTML)
4. Caching — Store analysis results for reuse

Would you like any of these included?

[... requirements finalized ...]

## Architecture Design

### Folder Structure
```
data-analyzer/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── config.json
├── examples.md
└── prompts.md
```

### Execution Flow
1. Accept CSV file input
2. Validate CSV structure
3. Parse and analyze data
4. Generate insights
5. Create visualizations
6. Output Markdown report

[... skill generated, tested, deployed ...]

✓ data-analyzer installed successfully.
```

### Example 2: Code Review Skill

**User:**
```
create-skill: Build a skill for automated code review
```

**AI Response:**
```
I'll create a code review skill for you. Let me gather requirements.

[... interview process ...]

## Final Skill

### SKILL.md
```markdown
---
name: code-reviewer
description: Automated code review with security, performance, and style checks
license: MIT
compatibility: opencode
categories: [code-review, security, performance]
metadata:
  author: user
  version: "1.0.0"
  last_updated: "2026-07-07"
  scope: universal
---

# Code Reviewer v1.0.0

> **"Automated code review with security, performance, and style checks."**

[... full skill content ...]
```

✓ code-reviewer installed successfully.
```

### Example 3: Documentation Generator

**User:**
```
skill-builder new-skill: Create a documentation generator for APIs
```

**AI Response:**
```
I'll create an API documentation generator skill. Let me start with requirements.

[... interview process ...]

## Research Report

### Domain Analysis
- API documentation is critical for developer experience
- OpenAPI/Swagger is the industry standard
- Auto-generation saves significant time

### Best Practices
- Follow OpenAPI 3.0 specification
- Include authentication details
- Provide code examples
- Support multiple languages

[... skill built and deployed ...]

✓ api-doc-generator installed successfully.
```

---

## Update an Existing Skill

### Example 1: Add New Feature

**User:**
```
edit-skill: Add dark mode support to the ui-designer skill
```

**AI Response:**
```
I'll update the ui-designer skill to add dark mode support.

## Reading Existing Skill

[... reads current skill files ...]

## Current Architecture

- Design Token System ✓
- Animation Framework ✓
- Glass Morphism ✓
- Micro-Interactions ✓
- **Dark Mode** ✗ (missing)

## Update Plan

1. Add dark mode color tokens
2. Create theme toggle component
3. Update glass morphism for dark mode
4. Add CSS variables for theme switching
5. Update documentation

## Merging Changes

[... merges changes carefully ...]
[... preserves existing features ...]
[... updates documentation ...]

## Testing

| Test Case | Status |
|-----------|--------|
| Light mode | ✅ PASS |
| Dark mode | ✅ PASS |
| Theme switching | ✅ PASS |
| Existing features | ✅ PASS |

✓ ui-designer updated successfully.
```

### Example 2: Fix Bug

**User:**
```
update-skill: Fix the validation issue in data-analyzer
```

**AI Response:**
```
I'll fix the validation issue in data-analyzer.

## Reading Existing Skill

[... identifies bug ...]

## Root Cause

The CSV parser doesn't handle quoted fields correctly.

## Fix Applied

Updated the parsing logic to handle:
- Quoted fields with commas
- Escaped quotes
- Multi-line values

## Testing

| Test Case | Status |
|-----------|--------|
| Simple CSV | ✅ PASS |
| Quoted fields | ✅ PASS |
| Escaped quotes | ✅ PASS |
| Multi-line | ✅ PASS |

✓ data-analyzer fixed successfully.
```

---

## Get Help

### Example 1: General Help

**User:**
```
skill-builder: How do I create a skill?
```

**AI Response:**
```
To create a new OpenCode skill, follow these steps:

1. **Activate the Skill Builder**
   ```
   skill-builder
   ```

2. **Provide Requirements**
   - Skill name
   - Purpose
   - Input/output types
   - Target users

3. **Answer Follow-up Questions**
   - Business requirements
   - Technical constraints
   - Integration needs

4. **Review Architecture**
   - Folder structure
   - Execution flow
   - Dependencies

5. **Approve and Deploy**
   - Review generated skill
   - Approve for deployment
   - Verify installation

The skill builder will handle everything else automatically!
```

### Example 2: Best Practices

**User:**
```
skill-builder: What are best practices for OpenCode skills?
```

**AI Response:**
```
## Best Practices for OpenCode Skills

### Structure
1. Always include SKILL.md with proper frontmatter
2. Provide comprehensive README.md
3. Maintain CHANGELOG.md for version history
4. Include examples.md for usage examples

### Quality
1. Never build without complete requirements
2. Research best practices before implementation
3. Validate everything before deployment
4. Test across multiple scenarios

### Documentation
1. Write clear, concise documentation
2. Include working code examples
3. Document configuration options
4. Provide troubleshooting guides

### Maintenance
1. Use semantic versioning
2. Preserve user customizations
3. Document all changes
4. Monitor for improvements

### Performance
1. Optimize prompts for token efficiency
2. Minimize context window usage
3. Cache when appropriate
4. Test performance metrics
```

---

## Advanced Examples

### Example 1: Complex Skill with Multiple Components

**User:**
```
skill-builder: Create a full-stack application generator
```

**AI Response:**
```
I'll create a comprehensive full-stack application generator. This is a complex skill, so let me gather detailed requirements.

[... extensive interview ...]

## Architecture Design

### Folder Structure
```
fullstack-generator/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── config.json
├── examples.md
├── prompts/
│   ├── frontend.md
│   ├── backend.md
│   └── database.md
├── templates/
│   ├── react/
│   ├── nextjs/
│   ├── node/
│   └── python/
└── schemas/
    ├── api.json
    └── database.json
```

### Execution Flow
1. Collect project requirements
2. Select tech stack
3. Generate database schema
4. Create backend API
5. Build frontend components
6. Set up authentication
7. Configure deployment
8. Generate documentation

[... skill generated with all components ...]

✓ fullstack-generator installed successfully.
```

### Example 2: Integration Skill

**User:**
```
skill-factory: Create a skill that integrates with GitHub and Supabase
```

**AI Response:**
```
I'll create a GitHub-Supabase integration skill.

[... interview process ...]

## Integration Architecture

### GitHub Integration
- Repository management
- Issue tracking
- PR automation
- Webhook handling

### Supabase Integration
- Database operations
- Authentication
- Real-time subscriptions
- Storage management

### Combined Workflow
1. GitHub event triggers skill
2. Process data with AI
3. Store results in Supabase
4. Update GitHub issue/PR
5. Notify stakeholders

[... skill built with both integrations ...]

✓ github-supabase-integrator installed successfully.
```

### Example 3: Skill Chain

**User:**
```
skill-builder: Create a skill chain that combines data-analyzer, code-reviewer, and api-doc-generator
```

**AI Response:**
```
I'll create a skill chain that orchestrates multiple skills.

[... interview process ...]

## Skill Chain Architecture

### Components
1. data-analyzer — Analyze project data
2. code-reviewer — Review code quality
3. api-doc-generator — Generate API docs

### Orchestration Flow
1. Accept project repository
2. Run data-analyzer on project metrics
3. Run code-reviewer on source code
4. Run api-doc-generator on API endpoints
5. Combine results into comprehensive report
6. Output unified analysis

### Configuration
```json
{
  "chain": [
    "data-analyzer",
    "code-reviewer",
    "api-doc-generator"
  ],
  "parallel": false,
  "output": "combined"
}
```

[... skill chain built and tested ...]

✓ project-analyzer-chain installed successfully.
```

---

## Tips for Using Examples

1. **Be Specific** — The more details you provide, the better the skill
2. **Ask Questions** — The skill builder will interview you
3. **Review Architecture** — Always review the proposed structure
4. **Test Thoroughly** — Verify the skill works as expected
5. **Document Usage** — Add your own examples to the skill

---

## Need More Help?

If you need additional examples or have specific use cases, ask the skill builder:

```
skill-builder: Show me examples for [your use case]
```
