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
