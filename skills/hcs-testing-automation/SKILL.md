---
name: "HCS Testing Automation"
description: "HCS Testing Automation v1.0 — Autonomous Testing Engine. Generates unit tests, integration tests, e2e tests, and test suites."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Testing Automation

## Purpose
Create comprehensive test suites that ensure application quality and reliability.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| **Unit Tests** | Test individual functions and components |
| **Integration Tests** | Test API endpoints and database operations |
| **E2E Tests** | Test complete user flows |
| **Test Utilities** | Factories, helpers, and mocks |
| **Code Coverage** | Coverage reports and thresholds |

## Supported Frameworks

| Framework | Language | Type |
|-----------|----------|------|
| Jest | JavaScript/TypeScript | Unit/Integration |
| Vitest | JavaScript/TypeScript | Unit/Integration |
| Cypress | JavaScript/TypeScript | E2E |
| Playwright | JavaScript/TypeScript | E2E |
| Pytest | Python | Unit/Integration |
| Go Test | Go | Unit/Integration |

## Test Pyramid

| Level | Count | Purpose |
|-------|-------|---------|
| Unit Tests | Many | Fast, isolated tests |
| Integration Tests | Some | API and DB testing |
| E2E Tests | Few | Full user flows |

## Related Agents (Cross-References)

| Agent | File | Integration |
|-------|------|-------------|
| **HCS Tester** | `~/.config/opencode/agents/hcs-tester-agent.md` | Enhanced testing |
| **HCS Human Tester** | `~/.config/opencode/agents/hcs-human-tester-agent.md` | Manual testing |
| **HCS Local Host Testing** | `~/.config/opencode/agents/hcs-local-host-testing-agent.md` | Test environment |
| **HCS API Builder** | `~/.config/opencode/agents/hcs-api-builder-agent.md` | API test generation |
| **HCS Database Manager** | `~/.config/opencode/agents/hcs-database-manager-agent.md` | Database tests |
| **HCS Security Auditor** | `~/.config/opencode/agents/hcs-security-auditor-agent.md` | Security tests |

## Final Instructions

1. **ALWAYS follow test pyramid** — Many unit, some integration, few E2E
2. **ALWAYS test edge cases** — Null, empty, boundary values
3. **ALWAYS mock externals** — Don't rely on external APIs
4. **ALWAYS use factories** — Generate test data consistently
5. **ALWAYS aim for 80%+ coverage** — Track coverage metrics


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

### Final Instructions

1. Be skeptical — Find issues, dont confirm everything
2. Be thorough — Check every claim
3. Be honest — Say clearly if wrong
4. Be specific — Provide exact findings
5. Be constructive — Suggest fixes

