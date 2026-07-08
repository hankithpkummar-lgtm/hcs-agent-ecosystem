---
name: "HCS Cron Manager"
description: "HCS Cron Manager v1.0 — Autonomous Cron Job Engine. Implements scheduled tasks, cron jobs, and recurring operations."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Cron Manager

## Purpose

Implement scheduled tasks, cron jobs, and recurring operations for automated workflows.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| **Cron Jobs** | Schedule cron jobs |
| **Recurring Tasks** | Recurring operations |
| **Task Scheduling** | Schedule specific times |
| **Distributed Cron** | Multi-server cron |

## Cron Solutions

| Solution | Type |
|----------|------|
| **node-cron** | Node.js |
| **bullmq** | Distributed |
| **croner** | Lightweight |

## Cron Expressions

| Expression | Meaning |
|------------|---------|
| `* * * * *` | Every minute |
| `0 * * * *` | Every hour |
| `0 0 * * *` | Every day at midnight |
| `*/5 * * * *` | Every 5 minutes |

## Final Instructions

### Domain Rules
1. Use appropriate cron syntax
2. Implement error handling
3. Add logging for debugging
4. Support distributed execution
5. Monitor task health

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
