# HCS Agent Ecosystem v2.0

[![HCS Agent Ecosystem](https://img.shields.io/badge/HCS-Agent%20Ecosystem-v2.0-blue.svg)](https://github.com/hankithpkummar-lgtm/hcs-agent-ecosystem)
[![OpenCode Compatible](https://img.shields.io/badge/OpenCode-Compatible-green.svg)](https://opencode.ai)
[![36 Agents](https://img.shields.io/badge/36-Agents-orange.svg)](#agent-ecosystem)
[![Multi-Platform](https://img.shields.io/badge/Multi--Platform-Supported-purple.svg)](#multi-platform-support)

> **A complete autonomous agent and skill system for OpenCode with smart auto-triggering, self-learning, multi-platform support, and localhost-first pipeline.**

---

## 🚀 What is HCS Agent Ecosystem?

The HCS Agent Ecosystem is a comprehensive collection of **36 autonomous agents** and **30+ skills** designed to automate the entire software development lifecycle. From document analysis to deployment, every task is handled by specialized agents that work together seamlessly.

### Key Features

| Feature | Description |
|---------|-------------|
| **36 Autonomous Agents** | Specialized agents for every development task |
| **Smart Auto-Trigger** | Agents automatically activate based on keywords |
| **Multi-Platform Support** | Works with OpenCode, Cursor, Claude Code, Codex, Kimi Code, VS Code, Windsurf, Aider |
| **Localhost-First Pipeline** | Everything happens locally first, deployment requires explicit permission |
| **Self-Learning System** | Agents improve after every task |
| **Admin Dashboard Builder** | Complete admin panel with 16 integrated agents |
| **Customer Management Suite** | CRM, Support, Communication, Feedback, Journey tracking |
| **Content Rephraser Pipeline** | Analyze → Research → Implement → Rephrase model |

---

## 📦 Agent Categories

### Core Agents (15)

| Agent | Purpose | Auto-Trigger |
|-------|---------|--------------|
| **Universal Prompt Builder** | Routes all requests to appropriate agents | Always active |
| **Master Dev Agent** | Full development lifecycle | build, create, develop |
| **Deployer** | GitHub, Vercel, Netlify, VPS deployment | deploy, push, publish |
| **Google Apps Script Builder** | Google Sheets automation | google sheets, apps script |
| **Link Analyser** | Link validation and fixing | analyze link, check link |
| **Tester** | Logic testing and debugging | test, check, debug |
| **Skill Builder** | Creates new OpenCode skills | create skill, build skill |
| **Skill Factory** | Autonomous skill creation | new skill, skill builder |
| **Master Prompt Builder** | Optimizes prompts | prompt, optimize request |
| **UI Designer** | Premium UI/UX design | ui design, glassmorphism |
| **Marketing Agent** | Marketing research and content | marketing, campaign |
| **WhatsApp Marketing Dashboard** | WhatsApp campaigns | whatsapp marketing |
| **Human Tester** | QA testing like a real human | human test, manual test |
| **Local Host Testing** | Local development testing | local, preview, localhost |
| **Data Linker** | Backend/frontend integration | data link, connect api |

### Admin Dashboard Agents (6)

| Agent | Purpose | Auto-Trigger |
|-------|---------|--------------|
| **Admin Dashboard Builder** | Master coordinator for all admin features | admin, dashboard |
| **Admin Auth Manager** | Authentication, RBAC, sessions, OAuth, 2FA | auth, login, rbac |
| **Admin Analytics Dashboard** | Revenue, traffic, user metrics | analytics, revenue |
| **Admin Content Manager** | CMS, rich text editor, media library | cms, content, pages |
| **Admin User Manager** | User CRUD, roles, activity logs | users, user list |
| **Admin Settings Manager** | Site configuration, appearance | settings, config |

### Customer Management Agents (5)

| Agent | Purpose | Auto-Trigger |
|-------|---------|--------------|
| **Customer Manager** | Core CRM, profiles, segmentation | customer, crm |
| **Customer Support Manager** | Ticket system, live chat, SLA | support, tickets |
| **Customer Communication Manager** | Email, SMS, push notifications | email, sms, campaign |
| **Customer Feedback Manager** | Reviews, surveys, NPS | feedback, reviews, nps |
| **Customer Journey Manager** | Lifecycle tracking, churn prediction | journey, lifecycle |

### Document & Content Agents (7)

| Agent | Purpose | Auto-Trigger |
|-------|---------|--------------|
| **Document Analyzer** | PDF, Word, images, video extraction | document, pdf, extract |
| **Website Generator** | Next.js, React, Vue code generation | generate website, build site |
| **Brand Analyzer** | Colors, fonts, logos, design system | brand, logo, colors |
| **Content Planner** | Sitemap, navigation, SEO strategy | content plan, sitemap |
| **Design Analyzer** | Figma/Sketch to code | analyze design, figma to code |
| **Multi-Source Aggregator** | Combine multiple sources | combine sources, merge content |
| **Website Clone** | Recreate existing websites | clone website, copy site |

### Data & Migration Agents (3)

| Agent | Purpose | Auto-Trigger |
|-------|---------|--------------|
| **Data Source Connector** | CSV, JSON, SQL, API integration | connect data, csv, json |
| **Content Migrator** | Transfer content between sites | migrate content, move website |
| **SEO Analyzer** | Technical SEO, keywords, schema | seo, search engine, keywords |

### Content Enhancement Agents (1)

| Agent | Purpose | Auto-Trigger |
|-------|---------|--------------|
| **Content Rephraser** | Analyze → Research → Implement → Rephrase pipeline | rephrase, enhance content |

---

## 🔄 Auto-Trigger System

The Universal Prompt Builder intercepts ALL requests and routes them to the appropriate agent based on keywords:

```
USER REQUEST
    ↓
UNIVERSAL PROMPT BUILDER (Always Active)
    ↓
KEYWORD DETECTION
    ↓
┌─────────────────────────────────────────────────────────────┐
│ "admin" / "dashboard"     → HCS Admin Dashboard Builder    │
│ "deploy" / "push"         → HCS Deployer                   │
│ "test" / "check"          → HCS Tester                     │
│ "link" / "url"            → HCS Link Analyser              │
│ "customer" / "crm"        → HCS Customer Manager           │
│ "rephrase" / "enhance"    → HCS Content Rephraser          │
│ "google sheets"           → HCS Google Apps Script Builder │
│ "whatsapp"                → HCS WhatsApp Marketing         │
│ "ui design"               → HCS UI Designer                │
│ "marketing"               → HCS Marketing Agent            │
│ No match                  → Universal Prompt Builder       │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 Content Rephraser Pipeline

The Content Rephraser follows a 4-phase pipeline:

```
PHASE 1: ANALYZE
├── Parse existing content structure
├── Identify content type
├── Extract all topics and subtopics
├── Map content hierarchy
└── Identify content gaps

PHASE 2: RESEARCH
├── Web search for each topic
├── Find authoritative sources
├── Gather latest statistics
├── Locate expert opinions
└── Find case studies

PHASE 3: IMPLEMENT
├── Topic gap analysis
├── Create implementation plan
├── Design content architecture
├── Resource planning
└── Implementation document

PHASE 4: REPHRASE
├── Adapt to website type
├── Enhance content
├── Integrate research
├── Add new topics
└── Quality validation
```

---

## 🏗️ Admin Dashboard Architecture

When "dashboard" is mentioned, the system automatically triggers:

```
HCS ADMIN DASHBOARD BUILDER
    ├── HCS Admin Auth Manager
    │   └── Login, Register, RBAC, Sessions, OAuth, 2FA
    ├── HCS Admin Analytics Dashboard
    │   └── Revenue, Traffic, User Metrics, Charts
    ├── HCS Admin Content Manager
    │   └── CMS, Rich Text Editor, Media Library
    ├── HCS Admin User Manager
    │   └── User CRUD, Roles, Activity Logs
    ├── HCS Admin Settings Manager
    │   └── Site Config, Appearance, Security
    ├── HCS Customer Manager
    │   └── CRM, Profiles, Segmentation
    ├── HCS Customer Support Manager
    │   └── Tickets, Live Chat, SLA
    ├── HCS Customer Communication Manager
    │   └── Email, SMS, Push Notifications
    ├── HCS Customer Feedback Manager
    │   └── Reviews, Surveys, NPS
    └── HCS Customer Journey Manager
        └── Lifecycle, Churn, Funnel
```

---

## 🌐 Multi-Platform Support

All agents and skills are compatible with:

| Platform | Configuration |
|----------|--------------|
| **OpenCode** | `~/.config/opencode/agents/` and `skills/` |
| **Cursor** | `.cursor/rules/` and `.cursorrules` |
| **Claude Code** | `.claude/rules/` and `CLAUDE.md` |
| **Codex** | `.codex/rules/` and `AGENTS.md` |
| **Kimi Code** | `.kimi/rules/` and `.kimirc` |
| **VS Code** | `.vscode/rules/` and `.vscode/settings.json` |
| **Windsurf** | `.windsurf/rules/` and `.windsurfrules` |
| **Aider** | `.aider/rules/` and `.aider.conf` |

---

## 📁 File Structure

```
~/.config/opencode/
├── agents/
│   ├── universal-prompt-builder.md          # PRIMARY - Always active
│   ├── hcs-admin-dashboard-builder-agent.md # Admin Dashboard
│   ├── hcs-admin-auth-manager-agent.md      # Auth & RBAC
│   ├── hcs-admin-analytics-dashboard-agent.md # Analytics
│   ├── hcs-admin-content-manager-agent.md   # CMS
│   ├── hcs-admin-user-manager-agent.md      # Users
│   ├── hcs-admin-settings-manager-agent.md  # Settings
│   ├── hcs-customer-manager-agent.md        # CRM
│   ├── hcs-customer-support-manager-agent.md # Support
│   ├── hcs-customer-communication-manager-agent.md # Comms
│   ├── hcs-customer-feedback-manager-agent.md # Feedback
│   ├── hcs-customer-journey-manager-agent.md # Journey
│   ├── hcs-content-rephraser-agent.md       # Content Rephraser
│   ├── hcs-deployer-agent.md                # Deployment
│   ├── hcs-document-analyzer-agent.md       # Documents
│   ├── hcs-website-generator-agent.md       # Website Generation
│   ├── hcs-brand-analyzer-agent.md          # Brand Analysis
│   ├── hcs-content-planner-agent.md         # Content Planning
│   ├── hcs-design-analyzer-agent.md         # Design Analysis
│   ├── hcs-multi-source-aggregator-agent.md # Multi-Source
│   ├── hcs-website-clone-agent.md           # Website Clone
│   ├── hcs-data-source-connector-agent.md   # Data Sources
│   ├── hcs-content-migrator-agent.md        # Content Migration
│   ├── hcs-seo-analyzer-agent.md            # SEO
│   ├── hcs-data-linker-agent.md             # Data Linking
│   ├── hcs-human-tester-agent.md            # Human Testing
│   ├── hcs-local-host-testing-agent.md      # Local Testing
│   ├── hcs-google-apps-script-builder-agent.md # Google Sheets
│   ├── hcs-link-analyser-agent.md           # Link Analysis
│   ├── hcs-tester-agent.md                  # Testing
│   ├── hcs-skill-builder-agent.md           # Skill Building
│   ├── hcs-skill-factory-agent.md           # Skill Factory
│   ├── hcs-master-prompt-builder-agent.md   # Prompt Building
│   ├── hcs-ui-designer-agent.md             # UI Design
│   ├── hcs-marketing-agent.md               # Marketing
│   └── hcs-whatsapp-marketing-dashboard-agent.md # WhatsApp
├── skills/
│   ├── hcs-admin-dashboard-builder/SKILL.md
│   ├── hcs-admin-auth-manager/SKILL.md
│   ├── hcs-admin-analytics-dashboard/SKILL.md
│   ├── hcs-admin-content-manager/SKILL.md
│   ├── hcs-admin-user-manager/SKILL.md
│   ├── hcs-admin-settings-manager/SKILL.md
│   ├── hcs-customer-manager/SKILL.md
│   ├── hcs-customer-support-manager/SKILL.md
│   ├── hcs-customer-communication-manager/SKILL.md
│   ├── hcs-customer-feedback-manager/SKILL.md
│   ├── hcs-customer-journey-manager/SKILL.md
│   ├── hcs-content-rephraser/SKILL.md
│   ├── hcs-document-analyzer/SKILL.md
│   ├── hcs-website-generator/SKILL.md
│   ├── hcs-brand-analyzer/SKILL.md
│   ├── hcs-content-planner/SKILL.md
│   ├── hcs-design-analyzer/SKILL.md
│   ├── hcs-multi-source-aggregator/SKILL.md
│   ├── hcs-website-clone/SKILL.md
│   ├── hcs-data-source-connector/SKILL.md
│   ├── hcs-content-migrator/SKILL.md
│   ├── hcs-seo-analyzer/SKILL.md
│   ├── hcs-data-linker/SKILL.md
│   ├── hcs-local-host-testing/SKILL.md
│   ├── master-dev-agent/SKILL.md
│   ├── google-apps-script-builder/SKILL.md
│   ├── link-analyser/SKILL.md
│   ├── tester/SKILL.md
│   ├── skill-builder/SKILL.md
│   ├── master-prompt-builder/SKILL.md
│   ├── ui-designer/SKILL.md
│   ├── marketing-agent/SKILL.md
│   └── whatsapp-marketing-dashboard/SKILL.md
├── plugins/
│   └── claude-mem.js
└── opencode.jsonc
```

---

## 🛠️ Installation

### OpenCode (Primary)

1. Clone this repository:
```bash
git clone https://github.com/hankithpkummar-lgtm/hcs-agent-ecosystem.git
```

2. Copy agents and skills to OpenCode config:
```bash
cp -r agents/* ~/.config/opencode/agents/
cp -r skills/* ~/.config/opencode/skills/
cp plugins/* ~/.config/opencode/plugins/
```

3. Restart OpenCode

### Other Platforms

See [MULTI-PLATFORM.md](MULTI-PLATFORM.md) for detailed installation instructions for each platform.

---

## 📋 Agent Configuration Rules

### Valid Mode Values

| Mode | Value | Use Case |
|------|-------|----------|
| **Primary** | `mode: primary` | Always active, runs on every message |
| **Subagent** | `mode: subagent` | Auto-triggers on matching keywords |
| **All** | `mode: all` | Both primary + subagent behavior |

### INVALID Mode Values (NEVER USE)

| Invalid Value | Why It Fails |
|---------------|--------------|
| `mode: secondary` | NOT a valid OpenCode mode — causes ConfigInvalidError |
| `mode: tertiary` | NOT a valid OpenCode mode |
| `mode: on-demand` | NOT a valid OpenCode mode |

---

## 🎯 Localhost-First Pipeline

**THIS IS THE MOST IMPORTANT RULE.**

```
CODE CHANGES MADE
    ↓
LOCALHOST PHASE (AUTOMATIC)
    ├── HCS LOCAL HOST TESTING AGENT
    │   ├── Start local server
    │   ├── Generate preview link
    │   ├── Test all links
    │   ├── Test all forms
    │   ├── Test all features
    │   ├── Fix all issues
    │   └── Improve everything
    ├── HCS HUMAN TESTER AGENT
    │   ├── Test like a real human
    │   ├── Click every link
    │   ├── Fill every form
    │   └── Check responsiveness
    └── HCS LINK ANALYSER AGENT
        ├── Analyze all links
        ├── Fix broken links
        └── Verify all URLs
    ↓
LOCALHOST TESTING COMPLETE
    ↓
ASK FOR DEPLOYMENT (ALWAYS)
    ├── USER SAYS "YES" / "DEPLOY" / "SHIP IT"
    │   └── HCS DEPLOYER AGENT → Deploy to production
    └── USER SAYS "NO" / "NOT YET"
        └── CONTINUE LOCALHOST → Keep testing locally
```

---

## 🤝 Integration Matrix

### How Admin Agents Work Together

| User Action | Agents Involved | Flow |
|-------------|----------------|------|
| **Create User** | Auth Manager → User Manager | Auth creates account, User Manager sets profile |
| **Customer Signs Up** | Auth Manager → Customer Manager → Journey Manager | Auth handles signup, CRM creates profile, Journey tracks |
| **Customer Buys** | Customer Manager → Analytics → Journey | CRM updates LTV, Analytics tracks revenue, Journey updates stage |
| **Customer Contacts Support** | Support Manager → Customer Manager | Ticket created, Customer profile updated |
| **Send Campaign** | Communication Manager → Customer Manager → Analytics | Campaign sent, Customers tracked, Results analyzed |
| **Customer Gives Feedback** | Feedback Manager → Support Manager → Journey | Review logged, Support follows up, Journey updated |

---

## 📊 Quality Standards

### Writing Quality

| Standard | Requirement |
|----------|-------------|
| **Clarity** | Easy to understand |
| **Conciseness** | No unnecessary words |
| **Coherence** | Logical flow |
| **Correctness** | Grammar, spelling, punctuation |
| **Consistency** | Uniform style |
| **Completeness** | All points covered |

### Research Quality

| Standard | Requirement |
|----------|-------------|
| **Relevance** | Directly related to topic |
| **Recency** | Current (within 2 years) |
| **Reliability** | Credible sources |
| **Diversity** | Multiple perspectives |
| **Accuracy** | Fact-checked |

---

## 🔧 Customization

### Adding New Agents

1. Create agent file: `~/.config/opencode/agents/hcs-[name]-agent.md`
2. Add frontmatter:
```markdown
---
description: "HCS [NAME] AGENT v1.0 — Description. Auto-triggers on: keyword1, keyword2."
mode: subagent
---
```
3. Add skill file: `~/.config/opencode/skills/hcs-[name]/SKILL.md`
4. Update Universal Prompt Builder routing table

### Adding New Keywords

Edit `universal-prompt-builder.md` and add keywords to the routing table:

```markdown
| **HCS Your Agent** | keyword1, keyword2, keyword3 |
```

---

## 📈 Statistics

| Metric | Count |
|--------|-------|
| **Total Agents** | 36 |
| **Total Skills** | 30+ |
| **Admin Agents** | 16 |
| **Customer Agents** | 5 |
| **Content Agents** | 7 |
| **Core Agents** | 15 |
| **Platforms Supported** | 8 |

---

## 🐛 Known Issues

- None currently reported

## 📝 Changelog

### v2.0.0 (2026-07-08)
- Complete admin dashboard builder with 16 integrated agents
- Customer management suite (CRM, Support, Communication, Feedback, Journey)
- Content Rephraser v2.0 with Analyze-Research-Implement-Rephrase pipeline
- Universal Prompt Builder with comprehensive routing table
- Multi-platform support for 8 platforms
- Localhost-first pipeline enforced
- Self-learning system for continuous improvement

### v1.0.0 (2026-07-07)
- Initial release with 15 core agents
- Auto-trigger system
- Basic skill system

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- OpenCode for the amazing platform
- All contributors who helped build this ecosystem
- The AI community for inspiration and best practices

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/hankithpkummar-lgtm/hcs-agent-ecosystem/issues)
- **Discussions**: [GitHub Discussions](https://github.com/hankithpkummar-lgtm/hcs-agent-ecosystem/discussions)

---

## ⭐ Star History

If you find this project useful, please give it a star on GitHub!

---

**Built with ❤️ by HCS**
