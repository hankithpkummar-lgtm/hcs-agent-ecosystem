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
