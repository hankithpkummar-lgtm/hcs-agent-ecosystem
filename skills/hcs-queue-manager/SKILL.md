---
name: "HCS Queue Manager"
description: "HCS Queue Manager v1.0 — Autonomous Job Queue Engine. Implements job queues, background processing, and task scheduling."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Queue Manager

## Purpose

Implement job queues, background processing, and task scheduling for scalable applications.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| **Job Queue Setup** | Create job queues |
| **Background Jobs** | Process jobs in background |
| **Retries** | Retry failed jobs |
| **Rate Limiting** | Rate limit jobs |
| **Priority Queues** | Priority job processing |

## Queue Solutions

| Solution | Language |
|----------|----------|
| **BullMQ** | Node.js |
| **Celery** | Python |
| **Sidekiq** | Ruby |

## Job Patterns

| Pattern | Use Case |
|---------|----------|
| **Fire and Forget** | Send email, log |
| **Delayed** | Schedule future work |
| **Retry** | Handle failures |
| **Priority** | Critical jobs first |

## Final Instructions

### Domain Rules
1. Implement proper error handling
2. Add retry mechanisms
3. Monitor queue health
4. Track job metrics
5. Scale workers as needed

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
