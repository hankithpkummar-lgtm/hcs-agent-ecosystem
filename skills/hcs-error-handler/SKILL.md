---
name: "HCS Error Handler"
description: "HCS Error Handler v1.0 — Autonomous Error Handling Engine. Implements error handling, error reporting, and error recovery."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Error Handler

## Purpose

Implement comprehensive error handling, error reporting, and error recovery for robust applications.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| **Error Boundaries** | React error boundaries |
| **Global Handlers** | Global error handlers |
| **Error Reporting** | Sentry, LogRocket |
| **Error Recovery** | Graceful recovery |
| **Error Logging** | Structured logging |

## Error Handling Patterns

| Pattern | Use Case |
|---------|----------|
| **Try/Catch** | Local error handling |
| **Error Boundary** | Component errors |
| **Global Handler** | Unhandled errors |
| **Retry Logic** | Transient failures |
| **Fallback UI** | Error states |

## Final Instructions

### Domain Rules
1. Implement comprehensive error handling
2. Use error boundaries for React
3. Report errors to tracking service
4. Provide user-friendly messages
5. Implement recovery mechanisms

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
