# HCS Admin Dashboard Builder Skill

> **HCS SKILL** — Created by HCS Skill Builder System
> **Version:** 2.0.0
> **Last Updated:** 2026-07-08
> **Status:** ACTIVE
> **Category:** Development / Dashboard

---

## SKILL CONFIGURATION RULES

**VALID MODE VALUES:**
- `primary` — Top-level skill, can be triggered directly by users
- `subagent` — Secondary skill, called by other agents/skills only
- `all` — Can work in both primary and subagent modes

**IMPORTANT:** Do NOT use any other mode values (e.g., `secondary` is INVALID and will cause `ConfigInvalidError`)

**MODE TEMPLATES:**
```yaml
# For primary skills (main entry points):
mode: primary

# For subagent skills (called by other agents):
mode: subagent

# For skills that can work in both modes:
mode: all
```

**VALIDATION CHECKLIST:**
- [ ] Mode is exactly one of: `primary`, `subagent`, `all`
- [ ] No other mode values are used
- [ ] Mode matches the skill's role (primary for entry points, subagent for helpers)

---

## SKILL PURPOSE

This skill builds **comprehensive admin dashboards** for websites by:
1. **Analyzing** website features and capabilities
2. **Suggesting** the best tools and components
3. **Building** complete admin panels with all required services
4. **Integrating** WhatsApp marketing, revenue tracking, traffic analytics
5. **Implementing** special permissions and data access controls
6. **Creating** feature request systems and building requested features

---

## SKILL TRIGGERS

| Trigger Phrase | Action |
|----------------|--------|
| "build admin dashboard" | Start dashboard creation |
| "create admin panel" | Build admin panel |
| "admin tools" | Suggest admin tools |
| "dashboard for website" | Analyze and build dashboard |
| "revenue dashboard" | Build revenue tracking |
| "traffic analytics" | Build analytics dashboard |
| "whatsapp marketing" | Integrate WhatsApp campaigns |
| "admin permissions" | Implement RBAC system |
| "feature requests" | Build feature request system |
| "customer management" | Build customer CRM |
| "support tickets" | Build ticket system |
| "analytics dashboard" | Build business intelligence |

---

## RELATED AGENTS (AUTO-TRIGGER INTEGRATION)

### Core Admin Agents

| Agent | File | Purpose |
|-------|------|---------|
| **HCS Admin Auth Manager** | `~/.config/opencode/agents/hcs-admin-auth-manager-agent.md` | Authentication, RBAC, sessions, OAuth, 2FA |
| **HCS Admin Analytics Dashboard** | `~/.config/opencode/agents/hcs-admin-analytics-dashboard-agent.md` | Revenue, traffic, user metrics, charts |
| **HCS Admin Content Manager** | `~/.config/opencode/agents/hcs-admin-content-manager-agent.md` | CMS, rich text, media, categories |
| **HCS Admin User Manager** | `~/.config/opencode/agents/hcs-admin-user-manager-agent.md` | User CRUD, roles, activity, bulk ops |
| **HCS Admin Settings Manager** | `~/.config/opencode/agents/hcs-admin-settings-manager-agent.md` | Site config, appearance, security |

### Customer Management Agents

| Agent | File | Purpose |
|-------|------|---------|
| **HCS Customer Manager** | `~/.config/opencode/agents/hcs-customer-manager-agent.md` | CRM, profiles, segmentation |
| **HCS Customer Support Manager** | `~/.config/opencode/agents/hcs-customer-support-manager-agent.md` | Tickets, SLA, live chat |
| **HCS Customer Communication Manager** | `~/.config/opencode/agents/hcs-customer-communication-manager-agent.md` | Email, SMS, push notifications |
| **HCS Customer Feedback Manager** | `~/.config/opencode/agents/hcs-customer-feedback-manager-agent.md` | Reviews, surveys, NPS |
| **HCS Customer Journey Manager** | `~/.config/opencode/agents/hcs-customer-journey-manager-agent.md` | Lifecycle, churn, funnel |

### Supporting Agents

| Agent | File | Purpose |
|-------|------|---------|
| **HCS Deployer** | `~/.config/opencode/agents/hcs-deployer-agent.md` | Deployment |
| **HCS Local Host Testing** | `~/.config/opencode/agents/hcs-local-host-testing-agent.md` | Local testing |
| **HCS Human Tester** | `~/.config/opencode/agents/hcs-human-tester-agent.md` | QA testing |
| **HCS SEO Analyzer** | `~/.config/opencode/agents/hcs-seo-analyzer-agent.md` | SEO optimization |
| **HCS UI Designer** | `~/.config/opencode/agents/hcs-ui-designer-agent.md` | Premium design |
| **HCS Content Rephraser** | `~/.config/opencode/agents/hcs-content-rephraser-agent.md` | Content enhancement |

### Auto-Trigger Integration

```
USER: "Build admin dashboard"
    |
    v
HCS ADMIN DASHBOARD BUILDER (This Skill)
    |
    ├── Auto-Trigger: HCS Admin Auth Manager
    |   └── Builds login, register, RBAC, sessions
    |
    ├── Auto-Trigger: HCS Admin Analytics Dashboard
    |   └── Builds overview, revenue, traffic, users
    |
    ├── Auto-Trigger: HCS Admin Content Manager
    |   └── Builds CMS, editor, media, categories
    |
    ├── Auto-Trigger: HCS Admin User Manager
    |   └── Builds user list, roles, activity
    |
    ├── Auto-Trigger: HCS Admin Settings Manager
    |   └── Builds settings, config, appearance
    |
    ├── Auto-Trigger: HCS Customer Manager
    |   └── Builds CRM, profiles, segmentation
    |
    ├── Auto-Trigger: HCS Customer Support Manager
    |   └── Builds tickets, chat, SLA
    |
    ├── Auto-Trigger: HCS Customer Communication Manager
    |   └── Builds campaigns, templates, automation
    |
    ├── Auto-Trigger: HCS Customer Feedback Manager
    |   └── Builds reviews, surveys, NPS
    |
    └── Auto-Trigger: HCS Customer Journey Manager
        └── Builds journey, funnel, churn
```

---

## CAPABILITIES

### 1. Website Analysis

**What It Does:**
- Detects website type (E-commerce, SaaS, Blog, etc.)
- Identifies existing features
- Maps tech stack
- Analyzes user base

**Output:**
```markdown
## WEBSITE ANALYSIS REPORT

### Type: E-commerce
### Tech Stack: Next.js + Stripe + PostgreSQL
### Existing Features: [list]
### Missing Features: [list]
### Recommended Dashboard Tools: [list]
```

### 2. Tool Suggestion Engine

**What It Does:**
- Recommends dashboard frameworks
- Suggests chart libraries
- Proposes table components
- Recommends auth solutions

**Output:**
| Category | Recommendation | Reason |
|----------|---------------|--------|
| Dashboard | Refine | Best for Next.js |
| Charts | Recharts | React-native |
| Tables | TanStack Table | Feature-rich |
| Auth | NextAuth.js | Easy integration |

### 3. Dashboard Builder

**What It Does:**
- Creates project structure
- Builds core components
- Implements feature components
- Sets up services

**Output:**
```
admin-dashboard/
├── components/
│   ├── auth/
│   ├── layout/
│   ├── dashboard/
│   ├── users/
│   ├── content/
│   ├── analytics/
│   ├── revenue/
│   ├── whatsapp/
│   └── settings/
├── pages/
├── services/
├── hooks/
├── utils/
└── styles/
```

### 4. Permissions System

**What It Does:**
- Defines roles (Super Admin, Admin, Editor, Viewer)
- Creates permission guards
- Implements access controls
- Manages user permissions

**Output:**
```javascript
// Role-Based Access Control
const PERMISSIONS = {
  SUPER_ADMIN: ['*'],
  ADMIN: ['dashboard:read', 'users:read', ...],
  EDITOR: ['content:read', 'content:write', ...],
  VIEWER: ['dashboard:read', 'analytics:read', ...]
};
```

### 5. WhatsApp Marketing Integration

**What It Does:**
- Creates campaign manager
- Builds message templates
- Manages contact groups
- Tracks campaign stats

**Output:**
```jsx
// Campaign Manager Component
<CampaignManager
  templates={templates}
  contacts={contacts}
  onSend={handleSend}
/>
```

### 6. Revenue Dashboard

**What It Does:**
- Tracks MRR, ARR, AOV, LTV
- Displays revenue charts
- Manages transactions
- Generates financial reports

**Output:**
```jsx
// Revenue Dashboard
<RevenueChart data={revenueData} />
<TransactionList transactions={transactions} />
<FinancialReport report={report} />
```

### 7. Traffic Analytics

**What It Does:**
- Tracks page views, visitors, sessions
- Analyzes traffic sources
- Shows device and geographic data
- Displays conversion funnels

**Output:**
```jsx
// Analytics Dashboard
<TrafficChart data={trafficData} />
<TopPages pages={topPages} />
<ConversionFunnel funnel={funnelData} />
```

### 8. Feature Request System

**What It Does:**
- Allows users to submit requests
- Enables voting on features
- Manages approval workflow
- Tracks feature implementation

**Output:**
```jsx
// Feature Request Component
<FeatureRequestList requests={requests} />
<FeatureRequestForm onSubmit={handleSubmit} />
<ApprovalPanel onApprove={handleApprove} />
```

---

## WORKFLOW

### Step 1: Receive Request

```
User: "Build admin dashboard for my e-commerce site"
    |
    v
HCS Admin Dashboard Builder
    |-- Parse request
    |-- Identify website type
    |-- Determine scope
```

### Step 2: Analyze Website

```
ANALYSIS PHASE
    |
    v
Detect Website Type
    |-- E-commerce, SaaS, Blog, etc.
    |
    v
Identify Features
    |-- Existing features
    |-- Missing features
    |
    v
Map Tech Stack
    |-- Frontend framework
    |-- Backend framework
    |-- Database
    |-- External services
    |
    v
Generate Analysis Report
```

### Step 3: Suggest Tools

```
TOOL SUGGESTION PHASE
    |
    v
Dashboard Framework
    |-- Next.js Admin
    |-- Refine
    |-- AdminJS
    |
    v
Chart Libraries
    |-- Recharts
    |-- Chart.js
    |-- D3.js
    |
    v
Table Components
    |-- TanStack Table
    |-- AG Grid
    |
    v
Auth Solutions
    |-- NextAuth.js
    |-- Auth0
    |-- Firebase Auth
    |
    v
Generate Tool Report
```

### Step 4: Build Dashboard

```
BUILD PHASE
    |
    v
Create Project Structure
    |-- Initialize project
    |-- Install dependencies
    |-- Set up configuration
    |
    v
Build Core Components
    |-- Authentication
    |-- Layout
    |-- Navigation
    |
    v
Build Feature Components
    |-- Dashboard home
    |-- User management
    |-- Content management
    |-- Analytics
    |-- Revenue
    |-- WhatsApp marketing
    |
    v
Implement Permissions
    |-- Role definitions
    |-- Permission guards
    |-- Access controls
    |
    v
Integrate Services
    |-- API connections
    |-- Real-time updates
    |-- External services
    |
    v
Test Components
    |-- Unit tests
    |-- Integration tests
```

### Step 5: Deploy Dashboard

```
DEPLOYMENT PHASE
    |
    v
Prepare for Deployment
    |-- Environment variables
    |-- Build configuration
    |-- Domain setup
    |
    v
Deploy to Platform
    |-- Vercel
    |-- Netlify
    |-- Custom server
    |
    v
Verify Deployment
    |-- Test all features
    |-- Check permissions
    |-- Validate integrations
    |
    v
Provide Access
    |-- Admin login credentials
    |-- Dashboard URL
    |-- Documentation
```

---

## DASHBOARD COMPONENTS

### Core Components

| Component | Purpose | Priority |
|-----------|---------|----------|
| **LoginForm** | Admin authentication | CRITICAL |
| **ProtectedRoute** | Route protection | CRITICAL |
| **RoleGuard** | Permission checking | CRITICAL |
| **Sidebar** | Navigation | HIGH |
| **Header** | Top bar | HIGH |
| **MainLayout** | Page layout | HIGH |

### Feature Components

| Component | Purpose | Priority |
|-----------|---------|----------|
| **StatsCard** | Display metrics | HIGH |
| **Chart** | Data visualization | HIGH |
| **DataTable** | Data display | HIGH |
| **UserList** | User management | HIGH |
| **ContentEditor** | Content management | HIGH |
| **RevenueChart** | Financial tracking | HIGH |
| **TrafficChart** | Analytics | HIGH |
| **CampaignManager** | WhatsApp marketing | HIGH |
| **FeatureRequest** | Feature requests | MEDIUM |
| **SettingsForm** | Configuration | MEDIUM |

---

## INTEGRATION POINTS

### WhatsApp Marketing

```javascript
// WhatsApp Integration
const whatsappIntegration = {
  // Campaign Management
  createCampaign: (data) => { /* ... */ },
  sendCampaign: (id) => { /* ... */ },
  getCampaignStats: (id) => { /* ... */ },
  
  // Template Management
  createTemplate: (data) => { /* ... */ },
  updateTemplate: (id, data) => { /* ... */ },
  deleteTemplate: (id) => { /* ... */ },
  
  // Contact Management
  addContact: (data) => { /* ... */ },
  removeContact: (id) => { /* ... */ },
  importContacts: (file) => { /* ... */ },
  
  // Analytics
  getDeliveryStats: () => { /* ... */ },
  getReadStats: () => { /* ... */ },
  getReplyStats: () => { /* ... */ }
};
```

### Revenue Tracking

```javascript
// Revenue Integration
const revenueIntegration = {
  // Transactions
  getTransactions: (filters) => { /* ... */ },
  getTransaction: (id) => { /* ... */ },
  
  // Subscriptions
  getSubscriptions: () => { /* ... */ },
  getMRR: () => { /* ... */ },
  getARR: () => { /* ... */ },
  
  // Reports
  generateReport: (period) => { /* ... */ },
  exportReport: (format) => { /* ... */ },
  
  // Payments
  getPaymentMethods: () => { /* ... */ },
  processRefund: (id) => { /* ... */ }
};
```

### Traffic Analytics

```javascript
// Analytics Integration
const analyticsIntegration = {
  // Real-time
  getRealTimeVisitors: () => { /* ... */ },
  getPageViews: (period) => { /* ... */ },
  
  // Sources
  getTrafficSources: () => { /* ... */ },
  getTopPages: () => { /* ... */ },
  
  // Users
  getUniqueVisitors: (period) => { /* ... */ },
  getSessionDuration: () => { /* ... */ },
  getBounceRate: () => { /* ... */ },
  
  // Devices
  getDeviceTypes: () => { /* ... */ },
  getBrowserStats: () => { /* ... */ },
  
  // Geographic
  getVisitorLocations: () => { /* ... */ },
  getTopCountries: () => { /* ... */ }
};
```

---

## PERMISSIONS SYSTEM

### Role Definitions

| Role | Description | Permissions |
|------|-------------|-------------|
| **Super Admin** | Full system access | All permissions |
| **Admin** | Standard admin access | Most permissions |
| **Editor** | Content management | Content permissions |
| **Viewer** | Read-only access | View permissions |

### Permission Types

| Permission | Description |
|------------|-------------|
| `dashboard:read` | View dashboard |
| `dashboard:write` | Modify dashboard |
| `users:read` | View users |
| `users:write` | Modify users |
| `users:delete` | Delete users |
| `content:read` | View content |
| `content:write` | Modify content |
| `content:delete` | Delete content |
| `analytics:read` | View analytics |
| `revenue:read` | View revenue |
| `revenue:write` | Modify revenue |
| `whatsapp:read` | View WhatsApp campaigns |
| `whatsapp:write` | Modify WhatsApp campaigns |
| `settings:read` | View settings |
| `settings:write` | Modify settings |
| `logs:read` | View logs |
| `reports:read` | View reports |
| `reports:write` | Modify reports |

### Permission Guard

```jsx
// Permission Guard Component
export function PermissionGuard({ permission, children, fallback }) {
  const { user, hasPermission } = useAuth();
  
  if (!user) {
    return fallback || <div>Please log in</div>;
  }
  
  if (!hasPermission(permission)) {
    return fallback || <div>Access Denied</div>;
  }
  
  return children;
}

// Usage
<PermissionGuard permission="users:write">
  <UserManagement />
</PermissionGuard>
```

---

## SELF-LEARNING SYSTEM

### Error Learning

```json
{
  "error_logs": [],
  "resolution_patterns": [],
  "prevention_rules": []
}
```

**How It Works:**
1. When an error occurs, log it
2. Analyze the error pattern
3. Find the resolution
4. Create a prevention rule
5. Update the knowledge base

### Usage Learning

```json
{
  "usage_logs": [],
  "optimization_patterns": [],
  "best_practices": []
}
```

**How It Works:**
1. Track how skills are used
2. Identify common patterns
3. Find optimization opportunities
4. Create best practices
5. Update the knowledge base

### Feedback Learning

```json
{
  "feedback_logs": [],
  "improvement_patterns": [],
  "enhancement_rules": []
}
```

**How It Works:**
1. Collect user feedback
2. Analyze feedback patterns
3. Identify improvements
4. Create enhancement rules
5. Update the knowledge base

### Knowledge Base

```json
{
  "error_solutions": {},
  "usage_optimizations": {},
  "feedback_improvements": {},
  "best_practices": {},
  "lessons_learned": {}
}
```

**How It Works:**
1. Store all learned patterns
2. Query knowledge base for solutions
3. Apply learned patterns
4. Continuously improve
5. Share knowledge across projects

---

## QUALITY STANDARDS

### Dashboard Quality Checklist

- [ ] **Authentication** — Secure admin login
- [ ] **Authorization** — Role-based access control
- [ ] **Responsive** — Works on all devices
- [ ] **Accessible** — WCAG compliant
- [ ] **Performant** — Fast loading
- [ ] **Secure** — Input validation, XSS protection
- [ ] **Maintainable** — Clean, documented code
- [ ] **Scalable** — Can grow with the website
- [ ] **Integrated** — Connects to all services
- [ ] **Real-time** — Live updates where needed

### Code Quality Checklist

- [ ] **Component-based** — Reusable components
- [ ] **Type-safe** — TypeScript or PropTypes
- [ ] **Tested** — Unit and integration tests
- [ ] **Documented** — Clear documentation
- [ ] **Consistent** — Following design system
- [ ] **Optimized** — Performance optimized
- [ ] **Secure** — Input validation and sanitization

---

## HCS PREFIX RULE

**PERMANENT AND MANDATORY**

This rule is PERMANENT and applies to ALL skills created by this agent:

1. **ALL Skills MUST Have HCS Prefix**
   - Every skill created must start with "HCS"
   - No exceptions allowed
   - This is permanent and cannot be changed

2. **Skill Names**
   - ✅ `hcs-admin-dashboard-builder`
   - ✅ `hcs-ecommerce-admin`
   - ❌ `admin-dashboard-builder`
   - ❌ `admin-panel`

3. **Agent Names**
   - ✅ `hcs-admin-dashboard-builder-agent.md`
   - ❌ `admin-dashboard-builder-agent.md`
   - ❌ `admin-builder.md`

4. **Enforcement**
   - Before creating any skill, check prefix
   - If no HCS prefix, add it
   - Never create skills without HCS prefix
   - This rule is permanent and cannot be changed

---

## SUCCESS METRICS

The HCS Admin Dashboard Builder is successful when:

- [ ] Website is properly analyzed
- [ ] Dashboard tools are suggested
- [ ] Complete dashboard is built
- [ ] All features are implemented
- [ ] Permissions are working
- [ ] WhatsApp marketing is integrated
- [ ] Revenue tracking is functional
- [ ] Analytics are displaying
- [ ] Feature requests can be made
- [ ] Dashboard is deployed and accessible

---

## EXAMPLE USAGE

### Example 1: E-commerce Dashboard

**User Request:**
"Build admin dashboard for my Next.js e-commerce site with Stripe"

**HCS Admin Dashboard Builder Response:**

```markdown
## E-COMMERCE ADMIN DASHBOARD

### Analysis
- **Type:** E-commerce
- **Tech Stack:** Next.js + Stripe + PostgreSQL
- **Features Detected:** Product catalog, cart, checkout

### Recommended Tools
- **Dashboard:** Refine (best for Next.js)
- **Charts:** Recharts
- **Tables:** TanStack Table
- **Auth:** NextAuth.js

### Dashboard Components
1. **Dashboard Home** — Stats, charts, recent activity
2. **Products** — CRUD operations
3. **Orders** — Order management
4. **Customers** — User management
5. **Revenue** — Financial tracking
6. **Analytics** — Traffic and behavior
7. **Settings** — Configuration

### Permissions
- **Super Admin:** Full access
- **Admin:** Most access
- **Editor:** Content only
- **Viewer:** Read-only

### Deployment
- Platform: Vercel
- Domain: admin.yourstore.com
- SSL: Automatic
```

### Example 2: SaaS Dashboard

**User Request:**
"Create admin panel for my SaaS platform"

**HCS Admin Dashboard Builder Response:**

```markdown
## SAAS ADMIN DASHBOARD

### Analysis
- **Type:** SaaS
- **Tech Stack:** React + Node.js + MongoDB
- **Features Detected:** User auth, subscriptions, billing

### Recommended Tools
- **Dashboard:** AdminJS
- **Charts:** Chart.js
- **Tables:** AG Grid
- **Auth:** Auth0

### Dashboard Components
1. **Dashboard** — MRR, ARR, churn, growth
2. **Subscriptions** — Plan management
3. **Users** — User management
4. **Billing** — Payment tracking
5. **Features** — Feature flags
6. **Support** — Ticket system
7. **Settings** — Configuration

### Permissions
- **Super Admin:** Full access
- **Admin:** User management
- **Support:** Ticket management
- **Viewer:** Read-only

### Deployment
- Platform: Custom server
- Domain: admin.yoursaas.com
- SSL: Let's Encrypt
```

---

## USER REQUEST RESEARCH

### Phase 0: Research Before Building

When user provides a dashboard request, research:

1. **Dashboard Best Practices**
   - Search for latest dashboard design patterns
   - Research admin panel best practices
   - Find security recommendations

2. **Tool Research**
   - Search for latest dashboard tools
   - Research component libraries
   - Find deployment platforms

3. **Integration Research**
   - Search for WhatsApp API best practices
   - Research payment gateway integration
   - Find analytics service options

4. **Security Research**
   - Search for admin security best practices
   - Research RBAC implementations
   - Find authentication solutions

### Research Integration

**Research findings are automatically injected into:**
- Tool suggestions
- Architecture decisions
- Component implementations
- Security configurations

### Research Sources

| Source | Purpose |
|--------|---------|
| **Official Docs** | Framework documentation |
| **GitHub** | Open-source solutions |
| **npm** | Package quality/safety |
| **Security Advisories** | Vulnerability checks |
| **Community Forums** | Best practices |
| **Stack Overflow** | Common issues |

---

*Generated by HCS Skill Builder System*
*Version: 1.0.0*
*Status: ACTIVE*