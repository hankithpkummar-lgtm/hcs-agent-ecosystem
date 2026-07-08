---
name: "HCS Admin Analytics Dashboard"
description: "HCS Admin Analytics Dashboard v2.0 — Autonomous Admin Analytics Engine. Builds revenue, traffic, user analytics dashboards. Integrates with all admin agents."
metadata:
  author: "HCS"
  version: "2.0"
---

# HCS Admin Analytics Dashboard

## Purpose
Create data-driven dashboards that provide actionable business insights.

## Dashboard Types

| Dashboard | Metrics |
|-----------|---------|
| **Overview** | Revenue, users, orders, conversion rate |
| **Revenue** | Sales, payment methods, top products |
| **Traffic** | Visitors, pageviews, sources, bounce rate |
| **Users** | Active users, demographics, behavior |
| **Content** | Top pages, engagement, conversions |

## Chart Components

| Component | Use Case |
|-----------|----------|
| **LineChart** | Trends over time |
| **BarChart** | Comparisons |
| **PieChart** | Distributions |
| **KPICard** | Key metrics with trends |
| **AreaChart** | Cumulative data |
| **Heatmap** | Patterns |

## Database Schema

| Table | Purpose |
|-------|---------|
| **analytics_events** | Custom events |
| **revenue** | Revenue tracking |
| **page_views** | Page view tracking |

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/analytics/overview` | Dashboard overview |
| GET | `/api/analytics/revenue` | Revenue metrics |
| GET | `/api/analytics/traffic` | Traffic metrics |
| GET | `/api/analytics/users` | User metrics |
| GET | `/api/analytics/realtime` | Real-time metrics |
| GET | `/api/analytics/export` | Export as CSV |

## Related Agents (Cross-References)

| Agent | File | Integration |
|-------|------|-------------|
| **HCS Admin Dashboard Builder** | `~/.config/opencode/agents/hcs-admin-dashboard-builder-agent.md` | Master coordinator, provides analytics widgets |
| **HCS Admin Auth Manager** | `~/.config/opencode/agents/hcs-admin-auth-manager-agent.md` | User activity tracking |
| **HCS Admin Content Manager** | `~/.config/opencode/agents/hcs-admin-content-manager-agent.md` | Content performance metrics |
| **HCS Admin User Manager** | `~/.config/opencode/agents/hcs-admin-user-manager-agent.md` | User analytics and behavior |
| **HCS Admin Settings Manager** | `~/.config/opencode/agents/hcs-admin-settings-manager-agent.md` | Analytics configuration |
| **HCS Customer Manager** | `~/.config/opencode/agents/hcs-customer-manager-agent.md` | Customer analytics and segmentation |
| **HCS Customer Support Manager** | `~/.config/opencode/agents/hcs-customer-support-manager-agent.md` | Support metrics and SLA tracking |
| **HCS Customer Communication Manager** | `~/.config/opencode/agents/hcs-customer-communication-manager-agent.md` | Campaign performance analytics |
| **HCS Customer Feedback Manager** | `~/.config/opencode/agents/hcs-customer-feedback-manager-agent.md` | Feedback analytics and NPS |
| **HCS Customer Journey Manager** | `~/.config/opencode/agents/hcs-customer-journey-manager-agent.md` | Journey funnel and conversion analytics |

### Integration Flow

```
ANALYTICS REQUEST
    |
    v
HCS Admin Analytics Dashboard (This Skill)
    |
    ├── Collects Data From All Systems
    |   |-- HCS Admin Auth Manager (user activity)
    |   |-- HCS Admin Content Manager (content metrics)
    |   |-- HCS Admin User Manager (user behavior)
    |   |-- HCS Customer Manager (customer data)
    |   |-- HCS Customer Support Manager (support metrics)
    |   |-- HCS Customer Communication Manager (campaign data)
    |   |-- HCS Customer Feedback Manager (feedback data)
    |   |-- HCS Customer Journey Manager (journey data)
    |
    ├── Processes & Visualizes
    |   |-- Calculates metrics
    |   |-- Generates charts
    |   |-- Creates reports
    |   |-- Exports data
    |
    └── Returns Dashboard
        |-- Overview dashboard
        |-- Revenue analytics
        |-- Traffic analytics
        |-- User analytics
        |-- Content analytics
```

## Final Instructions

1. **NEVER skip data validation** — Always validate analytics data
2. **NEVER expose sensitive data** — Anonymize when needed
3. **ALWAYS cache** — Cache expensive queries
4. **ALWAYS optimize** — Use database indexes
5. **ALWAYS export** — Allow CSV/PDF export
6. **ALWAYS integrate with other admin agents** — Pull data from all systems for comprehensive analytics


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

