---
name: "HCS Payment Integration"
description: "HCS Payment Integration v1.0 — Autonomous Payment Engine. Integrates Stripe, PayPal, and payment processing."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Payment Integration

## Purpose
Integrate payment gateways securely and handle transactions reliably.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| **Stripe** | Card payments, subscriptions |
| **PayPal** | PayPal, cards, pay later |
| **Subscriptions** | Recurring billing |
| **Invoices** | Invoice generation |
| **Webhooks** | Payment event handling |

## Payment Providers

| Provider | Features |
|----------|----------|
| Stripe | Cards, wallets, subscriptions |
| PayPal | PayPal, cards, pay later |
| Lemon Squeezy | Digital products |

## Final Instructions

1. **ALWAYS use HTTPS** — Secure communication
2. **ALWAYS verify webhooks** — Validate signatures
3. **ALWAYS handle errors** — Graceful failure handling
4. **ALWAYS log transactions** — Audit trail
5. **ALWAYS test with test mode** — Sandbox first


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

