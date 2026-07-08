---
name: "HCS Config Manager"
description: "HCS Config Manager v1.0 — Autonomous Configuration Engine. Implements configuration management, environment variables, and feature flags."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Config Manager

## Purpose

Implement configuration management, environment variables, and feature flags for applications.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| **Environment Variables** | Manage env vars |
| **Config Files** | Config file management |
| **Feature Flags** | Feature flag system |
| **Config Validation** | Validate config |

## Config Patterns

| Pattern | Description |
|---------|-------------|
| **12-Factor** | Environment-based config |
| **Config Files** | JSON/YAML/TOML files |
| **Feature Flags** | Toggle features |
| **Secrets Manager** | AWS Secrets, Vault |

## Final Instructions

### Domain Rules
1. Validate all configuration
2. Use environment variables for secrets
3. Implement feature flags
4. Support multiple environments
5. Rotate secrets regularly

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
