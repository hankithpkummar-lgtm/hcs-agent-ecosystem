---
name: "HCS Database Query Builder"
description: "HCS Database Query Builder v1.0 — Autonomous Query Builder Engine. Builds SQL queries, ORM queries, and database operations."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Database Query Builder

## Purpose

Build SQL queries, ORM queries, and database operations efficiently and safely.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| **Query Building** | Build SQL queries |
| **ORM Integration** | Prisma, Sequelize, TypeORM |
| **Query Optimization** | Optimize slow queries |
| **Raw SQL** | Generate raw SQL |

## Query Patterns

| Pattern | Description |
|---------|-------------|
| **SELECT** | Retrieve data |
| **INSERT** | Add new data |
| **UPDATE** | Modify existing data |
| **DELETE** | Remove data |
| **JOIN** | Combine tables |
| **Aggregation** | Group and count |
| **Pagination** | Limit and offset |

## Final Instructions

### Domain Rules
1. Use parameterized queries
2. Prevent SQL injection
3. Optimize query performance
4. Handle pagination
5. Support complex joins

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
