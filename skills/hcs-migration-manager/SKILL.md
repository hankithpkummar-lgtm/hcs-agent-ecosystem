---
name: "HCS Migration Manager"
description: "HCS Migration Manager v1.0 — Autonomous Database Migration Engine. Handles database migrations, schema changes, and data transformations."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Migration Manager

## Purpose

Handle database migrations, schema changes, and data transformations safely and reliably.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| **Schema Migrations** | Create/alter tables |
| **Data Migrations** | Transform data |
| **Rollback Support** | Undo migrations |
| **Version Control** | Migration versioning |

## Migration Tools

| Tool | Best For |
|------|----------|
| **Prisma Migrate** | TypeScript |
| **Alembic** | Python |
| **Flyway** | Enterprise |
| **Django Migrations** | Django |

## Migration Checklist

| Step | Action |
|------|--------|
| 1 | Backup database |
| 2 | Test migration locally |
| 3 | Run on staging |
| 4 | Validate data |
| 5 | Deploy to production |

## Final Instructions

### Domain Rules
1. Always backup before migration
2. Test migrations locally first
3. Support rollback operations
4. Document schema changes
5. Validate data integrity

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
