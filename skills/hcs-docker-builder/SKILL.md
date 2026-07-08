---
name: "HCS Docker Builder"
description: "HCS Docker Builder v1.0 — Autonomous Docker Engine. Creates and manages Docker containers, Dockerfiles, docker-compose, and Kubernetes deployments."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Docker Builder

## Purpose

Create and manage Docker containers, Dockerfiles, docker-compose configurations, and Kubernetes deployments.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| **Dockerfile Creation** | Generate optimized Dockerfiles |
| **Docker Compose** | Create multi-container setups |
| **Image Optimization** | Optimize image sizes |
| **Multi-stage Builds** | Implement multi-stage builds |
| **Kubernetes** | Create K8s deployments |

## Dockerfile Best Practices

| Practice | Description |
|----------|-------------|
| **Multi-stage Builds** | Separate build and production stages |
| **Alpine Linux** | Use alpine base images |
| **Layer Caching** | Order layers by change frequency |
| **Non-root User** | Run as non-root user |
| **Health Checks** | Implement health checks |

## Docker Compose Template

```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - db
      - redis
  db:
    image: postgres:16-alpine
  redis:
    image: redis:7-alpine
```

## Final Instructions

### Domain Rules
1. Use multi-stage builds
2. Minimize image size
3. Implement security best practices
4. Use health checks
5. Implement logging

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
