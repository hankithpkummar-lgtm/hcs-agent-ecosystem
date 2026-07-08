---
name: "HCS Load Tester"
description: "HCS Load Tester v1.0 — Autonomous Load Testing Engine. Performs load testing, stress testing, and performance testing with k6, JMeter, and other tools."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Load Tester

## Purpose

Perform load testing, stress testing, and performance testing to ensure applications can handle expected traffic.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| **Load Testing** | Test normal traffic conditions |
| **Stress Testing** | Test beyond normal capacity |
| **Spike Testing** | Test sudden traffic spikes |
| **Endurance Testing** | Test sustained load |
| **Performance Metrics** | Collect performance data |

## Load Testing Tools

| Tool | Best For |
|------|----------|
| **k6** | Developer-friendly |
| **JMeter** | Complex scenarios |
| **Gatling** | Scala users |
| **Locust** | Python users |
| **Artillery** | Quick tests |

## Performance Targets

| Metric | Target |
|--------|--------|
| **Response Time** | < 200ms |
| **Error Rate** | < 1% |
| **P95 Latency** | < 500ms |
| **CPU Usage** | < 80% |
| **Memory Usage** | < 80% |

## Final Instructions

### Domain Rules
1. Test realistic scenarios
2. Set clear performance targets
3. Monitor server metrics
4. Analyze bottlenecks
5. Generate comprehensive reports

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
