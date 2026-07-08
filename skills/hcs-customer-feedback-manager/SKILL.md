---
name: "HCS Customer Feedback Manager"
description: "HCS Customer Feedback Manager v2.0 — Autonomous Customer Feedback Engine. Builds review, survey, and feedback systems for admin dashboards. Integrates with all admin agents."
metadata:
  author: "HCS"
  version: "2.0"
---

# HCS Customer Feedback Manager

## Purpose
Create feedback loops that drive continuous improvement.

## Feedback Types

| Type | Description |
|------|-------------|
| **Reviews** | Star ratings + text |
| **Surveys** | Custom questionnaires |
| **NPS** | Net Promoter Score (0-10) |
| **Testimonials** | Customer stories |

## NPS Categories

| Score | Category | Description |
|-------|----------|-------------|
| 0-6 | Detractor | Unhappy customer |
| 7-8 | Passive | Neutral customer |
| 9-10 | Promoter | Happy customer |

## NPS Formula

```
NPS = % Promoters - % Detractors
Range: -100 to +100
```

## Database Schema

| Table | Purpose |
|-------|---------|
| **customer_reviews** | Customer reviews |
| **surveys** | Survey definitions |
| **survey_responses** | Survey answers |
| **nps_responses** | NPS responses |

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/admin/reviews` | List reviews |
| POST | `/api/admin/reviews/:id/approve` | Approve review |
| POST | `/api/admin/reviews/:id/respond` | Respond to review |
| GET | `/api/admin/surveys` | List surveys |
| POST | `/api/admin/surveys` | Create survey |
| GET | `/api/admin/nps` | Get NPS data |

## Related Agents (Cross-References)

| Agent | File | Integration |
|-------|------|-------------|
| **HCS Admin Dashboard Builder** | `~/.config/opencode/agents/hcs-admin-dashboard-builder-agent.md` | Master coordinator, provides feedback widgets |
| **HCS Admin Auth Manager** | `~/.config/opencode/agents/hcs-admin-auth-manager-agent.md` | Feedback system access control |
| **HCS Admin Analytics Dashboard** | `~/.config/opencode/agents/hcs-admin-analytics-dashboard-agent.md` | Feedback analytics and sentiment |
| **HCS Admin Content Manager** | `~/.config/opencode/agents/hcs-admin-content-manager-agent.md` | Testimonial content |
| **HCS Admin User Manager** | `~/.config/opencode/agents/hcs-admin-user-manager-agent.md` | Feedback manager permissions |
| **HCS Admin Settings Manager** | `~/.config/opencode/agents/hcs-admin-settings-manager-agent.md` | Feedback settings |
| **HCS Customer Manager** | `~/.config/opencode/agents/hcs-customer-manager-agent.md` | Customer feedback history |
| **HCS Customer Support Manager** | `~/.config/opencode/agents/hcs-customer-support-manager-agent.md` | Post-resolution feedback |
| **HCS Customer Communication Manager** | `~/.config/opencode/agents/hcs-customer-communication-manager-agent.md` | Survey distribution |
| **HCS Customer Journey Manager** | `~/.config/opencode/agents/hcs-customer-journey-manager-agent.md` | Feedback at journey stages |

### Integration Flow

```
FEEDBACK REQUEST
    |
    v
HCS Customer Feedback Manager (This Skill)
    |
    ├── Manages Feedback
    |   |-- Collects reviews
    |   |-- Manages surveys
    |   |-- Tracks NPS
    |   |-- Analyzes sentiment
    |
    ├── Integrates With All Systems
    |   |-- HCS Admin Auth Manager (access control)
    |   |-- HCS Admin Analytics Dashboard (feedback metrics)
    |   |-- HCS Admin Content Manager (testimonials)
    |   |-- HCS Customer Manager (feedback history)
    |   |-- HCS Customer Support Manager (post-resolution)
    |   |-- HCS Customer Communication Manager (survey distribution)
    |   |-- HCS Customer Journey Manager (journey feedback)
    |
    └── Returns Feedback Data
        |-- Review list with filters
        |-- Survey responses
        |-- NPS score and trends
        |-- Sentiment analysis
```

## Final Instructions

1. **NEVER fake reviews** — Always verify authenticity
2. **ALWAYS respond** — Acknowledge all reviews
3. **ALWAYS track NPS** — Monitor customer loyalty
4. **ALWAYS analyze sentiment** — Understand feedback themes
5. **ALWAYS integrate with other admin agents** — Feedback flows through all systems
