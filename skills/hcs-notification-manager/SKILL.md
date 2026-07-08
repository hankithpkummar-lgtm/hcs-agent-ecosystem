---
name: "HCS Notification Manager"
description: "HCS Notification Manager v1.0 — Autonomous Notification Engine. Implements push notifications, email notifications, SMS, and in-app notifications."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Notification Manager

## Purpose

Implement push notifications, email notifications, SMS, and in-app notifications for multi-channel communication.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| **Push Notifications** | Browser & mobile push |
| **Email Notifications** | Transactional email |
| **SMS Notifications** | Text messages |
| **In-App Notifications** | Real-time alerts |

## Notification Channels

| Channel | Tool |
|---------|------|
| **Web Push** | Web Push API |
| **iOS Push** | APNs |
| **Android Push** | FCM |
| **Email** | SendGrid, AWS SES |
| **SMS** | Twilio, AWS SNS |

## Final Instructions

### Domain Rules
1. Implement multi-channel support
2. Handle notification preferences
3. Add quiet hours support
4. Track delivery status
5. Handle failures gracefully

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
