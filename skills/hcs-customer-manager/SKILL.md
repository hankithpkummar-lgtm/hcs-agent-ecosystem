---
name: "HCS Customer Manager"
description: "HCS Customer Manager v2.0 — Autonomous Customer Management Engine. Builds complete customer management systems for admin dashboards. Integrates with all admin agents."
metadata:
  author: "HCS"
  version: "2.0"
---

# HCS Customer Manager

## Purpose
Create intuitive customer management interfaces that build stronger customer relationships.

## Customer Fields

| Field | Type | Required |
|-------|------|----------|
| **email** | Email | Yes |
| **name** | Text | Yes |
| **phone** | Text | No |
| **company** | Text | No |
| **status** | Enum | Yes |
| **source** | Enum | Yes |
| **segment** | Reference | No |
| **tags** | Array | No |
| **lifetime_value** | Number | Auto |

## Customer Statuses

| Status | Description |
|--------|-------------|
| **lead** | Potential customer |
| **active** | Current customer |
| **inactive** | No recent activity |
| **churned** | Lost customer |

## Database Schema

| Table | Purpose |
|-------|---------|
| **customers** | Customer profiles |
| **customer_interactions** | Interaction history |
| **customer_segments** | Customer groups |
| **customer_tags** | Custom tags |

## Segmentation Rules

| Segment | Rules |
|---------|-------|
| **New Customers** | created_at > 30 days ago |
| **Active Customers** | last_contact > 30 days |
| **Inactive Customers** | last_contact > 90 days |
| **High Value** | lifetime_value > $1000 |
| **At Risk** | last_contact > 60 days AND lifetime_value > $500 |

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/admin/customers` | List customers |
| POST | `/api/admin/customers` | Create customer |
| PUT | `/api/admin/customers/:id` | Update customer |
| DELETE | `/api/admin/customers/:id` | Delete customer |
| GET | `/api/admin/customers/:id/interactions` | Get interactions |
| POST | `/api/admin/customers/segments` | Create segment |
| GET | `/api/admin/customers/export` | Export CSV |

## Related Agents (Cross-References)

| Agent | File | Integration |
|-------|------|-------------|
| **HCS Admin Dashboard Builder** | `~/.config/opencode/agents/hcs-admin-dashboard-builder-agent.md` | Master coordinator, provides customer widgets |
| **HCS Admin Auth Manager** | `~/.config/opencode/agents/hcs-admin-auth-manager-agent.md` | Customer authentication |
| **HCS Admin Analytics Dashboard** | `~/.config/opencode/agents/hcs-admin-analytics-dashboard-agent.md` | Customer analytics and metrics |
| **HCS Admin Content Manager** | `~/.config/opencode/agents/hcs-admin-content-manager-agent.md` | Customer-facing content |
| **HCS Admin User Manager** | `~/.config/opencode/agents/hcs-admin-user-manager-agent.md` | Customer user profiles |
| **HCS Admin Settings Manager** | `~/.config/opencode/agents/hcs-admin-settings-manager-agent.md` | Customer settings |
| **HCS Customer Support Manager** | `~/.config/opencode/agents/hcs-customer-support-manager-agent.md` | Support tickets and service |
| **HCS Customer Communication Manager** | `~/.config/opencode/agents/hcs-customer-communication-manager-agent.md` | Email/SMS/push campaigns |
| **HCS Customer Feedback Manager** | `~/.config/opencode/agents/hcs-customer-feedback-manager-agent.md` | Reviews, surveys, NPS |
| **HCS Customer Journey Manager** | `~/.config/opencode/agents/hcs-customer-journey-manager-agent.md` | Lifecycle and churn tracking |

### Integration Flow

```
CUSTOMER REQUEST
    |
    v
HCS Customer Manager (This Skill)
    |
    ├── Manages Customers
    |   |-- Creates/updates profiles
    |   |-- Segments customers
    |   |-- Tracks interactions
    |   |-- Calculates LTV
    |
    ├── Integrates With All Systems
    |   |-- HCS Admin Auth Manager (customer authentication)
    |   |-- HCS Admin Analytics Dashboard (customer metrics)
    |   |-- HCS Admin Content Manager (customer content)
    |   |-- HCS Customer Support Manager (support tickets)
    |   |-- HCS Customer Communication Manager (campaigns)
    |   |-- HCS Customer Feedback Manager (feedback)
    |   |-- HCS Customer Journey Manager (lifecycle)
    |
    └── Returns Customer Data
        |-- Customer list with filters
        |-- Customer profiles
        |-- Segmentation results
        |-- Export data
```

## Final Instructions

1. **NEVER skip privacy** — Always protect customer data
2. **ALWAYS audit** — Log all customer operations
3. **ALWAYS integrate with other admin agents** — Customer data flows through all systems
4. **ALWAYS segment** — Group customers for targeted marketing
5. **ALWAYS track lifecycle** — Monitor customer journey stages
3. **ALWAYS support segmentation** — Smart customer grouping
4. **ALWAYS be searchable** — Advanced search/filter
5. **ALWAYS integrate** — Pass results to Admin Dashboard Builder


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

