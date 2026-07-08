---
name: "HCS Webhook Manager"
description: "HCS Webhook Manager v1.0 — Autonomous Webhook Engine. Manages webhooks, event-driven systems, and real-time notifications."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Webhook Manager

## Purpose

Manage webhooks, event-driven systems, real-time notifications, and pub/sub architectures.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| **Webhook Creation** | Create and configure webhooks |
| **Event Handling** | Process incoming events |
| **Retry Logic** | Implement retry mechanisms |
| **Signature Verification** | Verify webhook signatures |
| **Event Routing** | Route events to handlers |

## Retry Strategy

| Attempt | Delay |
|---------|-------|
| 1 | Immediate |
| 2 | 1 minute |
| 3 | 5 minutes |
| 4 | 30 minutes |
| 5 | 2 hours |
| 6+ | Dead Letter Queue |

## Final Instructions

### Domain Rules
1. Always verify webhook signatures
2. Return 200 quickly, process async
3. Implement retry with exponential backoff
4. Use dead letter queue for failures
5. Log all webhook activity

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
