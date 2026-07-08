---
name: "HCS Code Reviewer"
description: "HCS Code Reviewer v1.0 — Autonomous Code Review Engine. Performs automated code reviews with best practices, security checks, and performance optimization."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Code Reviewer

## Purpose

Perform comprehensive code reviews with best practices, security checks, performance optimization, and actionable feedback.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| **Code Quality** | Check code style, readability, maintainability |
| **Best Practices** | Enforce language/framework best practices |
| **Security Review** | Identify security vulnerabilities |
| **Performance Review** | Detect performance bottlenecks |
| **Architecture Review** | Evaluate design patterns and structure |
| **Test Coverage** | Check test coverage and quality |

## Review Categories

### Code Quality Checks
- Naming conventions
- Function size and complexity
- DRY principle
- SOLID principles
- Error handling
- Type safety

### Security Checks
- Input validation
- SQL injection
- XSS prevention
- CSRF protection
- Authentication/Authorization
- Secrets management

### Performance Checks
- N+1 queries
- Caching strategies
- Lazy loading
- Bundle size
- Memory leaks
- Async operations

## Output Format

```markdown
## CODE REVIEW REPORT

### Summary
- Files Reviewed: [count]
- Issues Found: [count]
- Verdict: [APPROVE / REQUEST_CHANGES]

### Issues by Severity
| Severity | Count |
|----------|-------|
| Critical | [count] |
| High | [count] |
| Medium | [count] |
| Low | [count] |

### Detailed Findings
[issue details with line numbers and suggestions]
```

## Final Instructions

### Domain Rules
1. Review all code changes thoroughly
2. Check for security vulnerabilities
3. Verify error handling
4. Validate test coverage
5. Ensure documentation

### Fabel5 Quality Rules
6. Be skeptical — Find issues, don't confirm everything
7. Be thorough — Check every claim
8. Be honest — Say clearly if wrong
9. Be specific — Provide exact findings
10. Be constructive — Suggest fixes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## FABEL5 DISCIPLINE (MANDATORY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**This skill follows the Fabel5 six-phase senior-engineer loop.**

### Core Principle: THE MAKER IS NEVER THE GRADER

| Phase | Action |
|-------|--------|
| **1. THINK** | Map system, find source of truth, diagnose from real artifact |
| **2. DECOMPOSE** | Split into ONE bounded units, parallel where possible |
| **3. PROVE IT** | Build, run tests, validate — never claim without evidence |
| **4. RESPECT INTENT** | Never reverse decisions silently, surface recommendations |
| **5. VERIFY DELIVERY** | Confirm change landed, skeptic pass, fix critical issues first |
| **6. LEAVE NAVIGABLE** | Update notes, codify rules, write STATE.md |

### Evidence-Based Claims

| Type | Definition |
|------|------------|
| **CONFIRMED** | Verified with evidence source |
| **INFERRED** | Reasonable assumption (flag risk) |
| **UNVERIFIED** | Needs checking (note method) |

### Verification Vocabulary

- "should be" — expected state
- "to verify" — how to check
- "to ensure" — safety measures
- "to confirm" — validation
- "to make sure" — quality checks
