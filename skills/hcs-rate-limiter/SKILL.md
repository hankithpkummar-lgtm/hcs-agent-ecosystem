---
name: "HCS Rate Limiter"
description: "HCS Rate Limiter v1.0 — Autonomous Rate Limiting Engine. Implements rate limiting, throttling, and abuse prevention."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Rate Limiter

## Purpose

Implement rate limiting, throttling, and abuse prevention to protect APIs and services.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| **Rate Limiting** | Limit request rates |
| **Throttling** | Throttle requests |
| **IP Blocking** | Block abusive IPs |
| **API Keys** | Rate limit by API key |

## Rate Limiting Algorithms

| Algorithm | Best For |
|-----------|----------|
| **Fixed Window** | Simple limits |
| **Sliding Window** | Accurate limits |
| **Token Bucket** | Burst handling |
| **Leaky Bucket** | Smooth rate |

## Final Instructions

### Domain Rules
1. Choose appropriate algorithm
2. Implement per-user and per-endpoint limits
3. Use Redis for distributed rate limiting
4. Return proper rate limit headers
5. Monitor rate limit hits

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
