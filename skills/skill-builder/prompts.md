# OpenCode Skill Builder - Prompt Templates

## Table of Contents

1. [Skill Creation Prompts](#skill-creation-prompts)
2. [Skill Update Prompts](#skill-update-prompts)
3. [Research Prompts](#research-prompts)
4. [Architecture Prompts](#architecture-prompts)
5. [Validation Prompts](#validation-prompts)
6. [Testing Prompts](#testing-prompts)
7. [Documentation Prompts](#documentation-prompts)

---

## Skill Creation Prompts

### Requirement Collection Prompt

```
I'll help you create a new OpenCode skill. Let me start by collecting requirements.

## Basic Questions

1. What is the skill name?
2. What is the purpose?
3. Who will use this skill?
4. What input does it accept?
5. What output does it produce?
6. Which AI models should it support?

## Business Questions

1. What problem are you solving?
2. Why are you building this?
3. What is your current workflow?
4. What is your desired workflow?
5. What is the expected outcome?
6. How often will this be used?
7. What defines success?

Please answer these questions so I can build the perfect skill for you.
```

### Requirement Expansion Prompt

```
Based on your requirements, I suggest these additional features:

1. **Error Handling** — Graceful failure recovery
   - Benefit: Improved reliability and user experience

2. **Logging** — Track execution and errors
   - Benefit: Easier debugging and monitoring

3. **Caching** — Store results for reuse
   - Benefit: Improved performance

4. **Configuration** — User-adjustable settings
   - Benefit: Flexibility for different use cases

5. **Documentation** — Comprehensive guides
   - Benefit: Easier adoption and maintenance

Would you like any of these included? You can also specify any other features not listed.
```

### Research Prompt

```
Let me research best practices for this skill domain.

## Research Areas

1. **Industry Standards** — What are the common patterns?
2. **Existing Solutions** — Similar skills or tools?
3. **Best Practices** — Recommended approaches?
4. **Security** — Vulnerability prevention?
5. **Performance** — Optimization techniques?
6. **Limitations** — Known issues or trade-offs?

I'll analyze these areas and provide recommendations before building the skill.
```

---

## Skill Update Prompts

### Read Existing Skill Prompt

```
I'll update the existing skill. Let me first read and understand the current implementation.

[... reads skill files ...]

## Current Architecture

- **Structure:** [Current folder structure]
- **Features:** [List of current features]
- **Dependencies:** [Current dependencies]
- **Configuration:** [Current settings]

## Identified Changes

1. [Change 1] — [Reason]
2. [Change 2] — [Reason]
3. [Change 3] — [Reason]

## Update Plan

1. [Step 1]
2. [Step 2]
3. [Step 3]

I'll merge these changes while preserving existing functionality and user customizations.
```

### Merge Changes Prompt

```
## Merging Changes

### Preserved Features
- [Feature 1] — Unchanged
- [Feature 2] — Unchanged
- [Feature 3] — Unchanged

### Modified Features
- [Feature 4] — Updated with [changes]
- [Feature 5] — Enhanced with [improvements]

### New Features
- [New Feature 1] — [Description]
- [New Feature 2] — [Description]

### Backward Compatibility
- All existing functionality preserved
- No breaking changes
- Configuration remains compatible

I'll now update the documentation and version number.
```

---

## Research Prompts

### Domain Analysis Prompt

```
## Domain Analysis: [Skill Domain]

### Current State
- [Analysis of current situation]
- [Common challenges]
- [Existing solutions]

### Best Practices
- [Practice 1]
- [Practice 2]
- [Practice 3]

### Recommendations
- [Recommendation 1]
- [Recommendation 2]
- [Recommendation 3]

### Risks
- [Risk 1] — Mitigation: [Strategy]
- [Risk 2] — Mitigation: [Strategy]
```

### Technology Research Prompt

```
## Technology Research: [Technology]

### Overview
- [What it is]
- [Why it's relevant]

### Features
- [Feature 1]
- [Feature 2]
- [Feature 3]

### Pros
- [Advantage 1]
- [Advantage 2]

### Cons
- [Disadvantage 1]
- [Disadvantage 2]

### Alternatives
- [Alternative 1]
- [Alternative 2]

### Recommendation
- [Your recommendation with reasoning]
```

---

## Architecture Prompts

### Architecture Design Prompt

```
## Architecture Design: [Skill Name]

### Folder Structure
```
skill-name/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── config.json
├── examples.md
└── prompts.md
```

### Execution Flow
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Module Breakdown
- **Module 1:** [Description]
- **Module 2:** [Description]
- **Module 3:** [Description]

### Dependencies
- [Dependency 1] — [Purpose]
- [Dependency 2] — [Purpose]

### Configuration
- [Option 1] — [Description]
- [Option 2] — [Description]

### Error Handling
- [Error Type 1] — [Recovery Strategy]
- [Error Type 2] — [Recovery Strategy]
```

### Prompt Flow Design Prompt

```
## Prompt Flow Design

### System Prompt
```
[Role definition]
[Context]
[Instructions]
```

### User Prompt Template
```
[Task description]
[Input format]
[Output requirements]
```

### Example Prompts
1. **Basic:** [Simple example]
2. **Advanced:** [Complex example]
3. **Edge Case:** [Special scenario]

### Validation Rules
- [Rule 1]
- [Rule 2]
- [Rule 3]
```

---

## Validation Prompts

### Validation Checklist Prompt

```
## Validation Report: [Skill Name]

### Status: ✅ PASSED / ❌ FAILED

### Checks

| Check | Status | Notes |
|-------|--------|-------|
| Markdown | ✅/❌ | [Notes] |
| Frontmatter | ✅/❌ | [Notes] |
| Structure | ✅/❌ | [Notes] |
| Syntax | ✅/❌ | [Notes] |
| Variables | ✅/❌ | [Notes] |
| Examples | ✅/❌ | [Notes] |
| Links | ✅/❌ | [Notes] |
| Completeness | ✅/❌ | [Notes] |

### Issues Found
- [Issue 1] — [Severity] — [Suggestion]
- [Issue 2] — [Severity] — [Suggestion]

### Recommendations
- [Recommendation 1]
- [Recommendation 2]
```

### Quality Check Prompt

```
## Quality Check: [Skill Name]

### Production Readiness
- [ ] No placeholders or TODOs
- [ ] Complete implementation
- [ ] Error handling
- [ ] Edge case coverage

### Documentation Quality
- [ ] Clear README
- [ ] Working examples
- [ ] Configuration guide
- [ ] Troubleshooting section

### Performance
- [ ] Optimized prompts
- [ ] Efficient token usage
- [ ] Fast execution
- [ ] Minimal context

### Security
- [ ] Input validation
- [ ] Safe execution
- [ ] No vulnerabilities
- [ ] Audit trail

### Overall Score: [X/100]
```

---

## Testing Prompts

### Test Case Generation Prompt

```
## Test Cases: [Skill Name]

### Normal Input Tests

1. **Test 1:** [Description]
   - Input: [Input]
   - Expected: [Output]
   - Status: ✅/❌

2. **Test 2:** [Description]
   - Input: [Input]
   - Expected: [Output]
   - Status: ✅/❌

### Edge Case Tests

1. **Test 1:** [Description]
   - Input: [Input]
   - Expected: [Output]
   - Status: ✅/❌

2. **Test 2:** [Description]
   - Input: [Input]
   - Expected: [Output]
   - Status: ✅/❌

### Invalid Input Tests

1. **Test 1:** [Description]
   - Input: [Input]
   - Expected: [Error handling]
   - Status: ✅/❌

2. **Test 2:** [Description]
   - Input: [Input]
   - Expected: [Error handling]
   - Status: ✅/❌

### Performance Tests

1. **Test 1:** [Description]
   - Input: [Large input]
   - Expected: [Performance metric]
   - Status: ✅/❌

### Test Summary
- Total: [X]
- Passed: [X]
- Failed: [X]
- Success Rate: [X%]
```

### Stress Test Prompt

```
## Stress Test: [Skill Name]

### Test Parameters
- Concurrent requests: [X]
- Input size: [X]
- Duration: [X seconds]

### Results

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Response Time | < [X]ms | [X]ms | ✅/❌ |
| Memory Usage | < [X]MB | [X]MB | ✅/❌ |
| Token Usage | < [X] | [X] | ✅/❌ |
| Error Rate | < [X]% | [X]% | ✅/❌ |

### Observations
- [Observation 1]
- [Observation 2]

### Recommendations
- [Recommendation 1]
- [Recommendation 2]
```

---

## Documentation Prompts

### README Generation Prompt

```
# [Skill Name]

[One-line description]

## Overview

[Detailed description of what the skill does and why it exists.]

## Installation

### Automatic Installation

[Instructions for automatic installation]

### Manual Installation

1. Create directory: `~/.config/opencode/skills/[skill-name]/`
2. Copy files to the directory
3. Restart OpenCode

## Usage

### Basic Usage

[Step-by-step instructions]

### Advanced Usage

[Advanced features]

## Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| [option] | [type] | [default] | [description] |

## Examples

[Working examples]

## Troubleshooting

### Common Issues

**Issue:** [Problem]
**Solution:** [Fix]

## Contributing

[How to contribute]

## License

MIT
```

### CHANGELOG Generation Prompt

```markdown
# Changelog

All notable changes to [SKILL_NAME] will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- [New features]

### Changed
- [Changes to existing features]

### Fixed
- [Bug fixes]

### Removed
- [Removed features]

## [1.0.0] - YYYY-MM-DD

### Added
- Initial release
- [Feature 1]
- [Feature 2]
- [Feature 3]
```

### Examples Generation Prompt

```
# Examples: [Skill Name]

## Basic Usage

### Example 1: [Scenario]

**Input:**
```
[Input example]
```

**Output:**
```
[Output example]
```

**Explanation:**
[What happened and why]

## Advanced Usage

### Example 2: [Complex Scenario]

**Input:**
```
[Complex input]
```

**Output:**
```
[Complex output]
```

**Configuration:**
```json
{
  "setting": "value"
}
```

## Edge Cases

### Example 3: [Special Case]

**Input:**
```
[Edge case input]
```

**Output:**
```
[Edge case output]
```

**Notes:**
[Special handling]
```

---

## Usage Tips

1. **Customize Prompts** — Adapt these templates to your specific needs
2. **Add Context** — Include relevant project details
3. **Be Specific** — Clear instructions produce better results
4. **Iterate** — Refine prompts based on results
5. **Document** — Keep track of what works

---

## Need Custom Prompts?

If you need prompts for specific use cases, ask the skill builder:

```
skill-builder: Create prompts for [your use case]
```
