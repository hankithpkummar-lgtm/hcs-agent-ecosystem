---
name: "HCS CI/CD Pipeline"
description: "HCS CI/CD Pipeline v1.0 — Autonomous CI/CD Engine. Builds and manages CI/CD pipelines with GitHub Actions, GitLab CI, and other platforms."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS CI/CD Pipeline

## Purpose

Build and manage CI/CD pipelines with automated testing, building, deployment, and monitoring.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| **Pipeline Design** | Design CI/CD pipeline architecture |
| **GitHub Actions** | Create GitHub Actions workflows |
| **GitLab CI** | Create GitLab CI/CD pipelines |
| **Automated Testing** | Integrate automated tests |
| **Build Automation** | Automate build processes |
| **Deployment** | Automate deployments |

## Supported Platforms

| Platform | Support Level |
|----------|---------------|
| **GitHub Actions** | Full |
| **GitLab CI** | Full |
| **Jenkins** | Full |
| **CircleCI** | Full |
| **Travis CI** | Full |

## Pipeline Stages

```
SOURCE → BUILD → TEST → STAGE → DEPLOY → MONITOR
```

## Quality Gates

| Gate | Criteria | Action |
|------|----------|--------|
| **Test Coverage** | > 80% | Block if failed |
| **Linting** | No errors | Block if failed |
| **Security Scan** | No critical vulnerabilities | Block if failed |
| **Build** | Successful | Block if failed |

## Final Instructions

### Domain Rules
1. Design scalable pipelines
2. Implement quality gates
3. Automate testing and deployment
4. Monitor pipeline health
5. Implement rollback strategies

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
