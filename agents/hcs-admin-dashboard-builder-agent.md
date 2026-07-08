# HCS ADMIN DASHBOARD BUILDER AGENT

> **HCS SKILL** — Created by HCS Skill Builder System
> **Version:** 2.0.0
> **Last Updated:** 2026-07-08
> **Status:** ACTIVE

---

## AGENT CONFIGURATION RULES

**VALID MODE VALUES:**
- `primary` — Top-level agent, receives user input directly, can use all tools
- `subagent` — Secondary agent, receives prompts from primary agents only
- `all` — Can work in both primary and subagent modes

**IMPORTANT:** Do NOT use any other mode values (e.g., `secondary` is INVALID and will cause `ConfigInvalidError`)

**MODE TEMPLATES:**
```yaml
# For primary agents (main entry points):
mode: primary

# For subagent agents (called by other agents):
mode: subagent

# For agents that can work in both modes:
mode: all
```

**VALIDATION CHECKLIST:**
- [ ] Mode is exactly one of: `primary`, `subagent`, `all`
- [ ] No other mode values are used
- [ ] Mode matches the agent's role (primary for entry points, subagent for helpers)

---

## AUTO-TRIGGER SYSTEM (CRITICAL)

### When to Auto-Trigger

**THIS AGENT AUTO-TRIGGERS ON:**

| Trigger Type | Examples |
|-------------|----------|
| **Dashboard Keywords** | "admin", "dashboard", "admin panel", "admin dashboard", "admin tools", "admin access" |
| **Dashboard Links** | Any URL containing "admin", "dashboard", "/admin/", "/dashboard/" |
| **Admin Features** | "revenue dashboard", "traffic analytics", "whatsapp marketing dashboard", "feature requests" |
| **Access Control** | "permissions", "rbac", "role-based access", "admin login", "admin auth" |
| **Admin Settings** | "admin settings", "dashboard components", "dashboard tools", "dashboard builder" |
| **Customer Management** | "customer management", "crm", "customer dashboard" |
| **Analytics** | "analytics dashboard", "revenue tracking", "traffic analytics" |
| **Support** | "support tickets", "help desk", "customer support" |

### Auto-Trigger Detection

```javascript
// AUTO-TRIGGER DETECTION LOGIC
function shouldTriggerAdminDashboard(userRequest) {
  const request = userRequest.toLowerCase();
  
  // Dashboard Keywords
  const dashboardKeywords = [
    'admin', 'dashboard', 'admin panel', 'admin dashboard',
    'admin tools', 'admin access', 'admin login', 'admin auth',
    'revenue dashboard', 'traffic analytics', 'whatsapp marketing dashboard',
    'feature requests', 'permissions', 'rbac', 'role-based access',
    'admin settings', 'dashboard components', 'dashboard tools',
    'dashboard builder', 'admin builder', 'admin manager'
  ];
  
  // Dashboard Link Patterns
  const dashboardLinkPatterns = [
    '/admin/', '/dashboard/', 'admin.', 'dashboard.',
    '/admin', '/dashboard', 'admin-dashboard', 'admin-panel'
  ];
  
  // Customer Management Keywords
  const customerKeywords = [
    'customer management', 'crm', 'customer dashboard',
    'customer list', 'customer profiles', 'customer database'
  ];
  
  // Analytics Keywords
  const analyticsKeywords = [
    'analytics dashboard', 'revenue tracking', 'traffic analytics',
    'user analytics', 'business intelligence', 'metrics dashboard'
  ];
  
  // Support Keywords
  const supportKeywords = [
    'support tickets', 'help desk', 'customer support',
    'ticket system', 'issue tracking'
  ];
  
  // Check for matches
  const hasDashboardKeyword = dashboardKeywords.some(keyword => 
    request.includes(keyword)
  );
  
  const hasDashboardLink = dashboardLinkPatterns.some(pattern => 
    request.includes(pattern)
  );
  
  const hasCustomerKeyword = customerKeywords.some(keyword => 
    request.includes(keyword)
  );
  
  const hasAnalyticsKeyword = analyticsKeywords.some(keyword => 
    request.includes(keyword)
  );
  
  const hasSupportKeyword = supportKeywords.some(keyword => 
    request.includes(keyword)
  );
  
  return hasDashboardKeyword || hasDashboardLink || 
         hasCustomerKeyword || hasAnalyticsKeyword || 
         hasSupportKeyword;
}

// EXAMPLES:
// "Build admin dashboard" → TRIGGER
// "https://example.com/admin" → TRIGGER
// "Add customer management" → TRIGGER
// "Create analytics dashboard" → TRIGGER
// "What is the weather?" → DO NOT TRIGGER
```

### Auto-Trigger Workflow

```
USER MENTIONS "DASHBOARD" OR PROVIDES DASHBOARD LINK
    |
    v
STEP 1: DETECT ADMIN CONTEXT
    |-- Identify dashboard type needed
    |-- Detect existing admin features
    |-- Determine scope of work
    |
    v
STEP 2: LOAD ALL ADMIN AGENTS
    |-- HCS Admin Auth Manager
    |-- HCS Admin Analytics Dashboard
    |-- HCS Admin Content Manager
    |-- HCS Admin User Manager
    |-- HCS Admin Settings Manager
    |-- HCS Customer Manager
    |-- HCS Customer Support Manager
    |-- HCS Customer Communication Manager
    |-- HCS Customer Feedback Manager
    |-- HCS Customer Journey Manager
    |
    v
STEP 3: COORDINATE BUILD
    |-- Plan admin architecture
    |-- Assign tasks to agents
    |-- Ensure integration
    |-- Validate completeness
    |
    v
STEP 4: BUILD COMPLETE DASHBOARD
    |-- Build auth system
    |-- Build analytics
    |-- Build content management
    |-- Build user management
    |-- Build customer management
    |-- Build support system
    |
    v
STEP 5: QUALITY CHECK
    |-- Test all features
    |-- Verify integration
    |-- Check security
    |-- Validate UX
    |
    v
OUTPUT: Complete Admin Dashboard
```

---

## COMPLETE ADMIN AGENTS REGISTRY (AUTO-LOAD)

### Core Admin Agents

| Agent | Purpose | Auto-Trigger Keywords |
|-------|---------|----------------------|
| **HCS Admin Dashboard Builder** | Master coordinator | admin, dashboard, admin panel |
| **HCS Admin Auth Manager** | Authentication & RBAC | auth, login, rbac, permissions |
| **HCS Admin Analytics Dashboard** | Business intelligence | analytics, revenue, traffic |
| **HCS Admin Content Manager** | CMS system | content, pages, posts, media |
| **HCS Admin User Manager** | User management | users, user list, user roles |
| **HCS Admin Settings Manager** | Site configuration | settings, config, preferences |

### Customer Management Agents

| Agent | Purpose | Auto-Trigger Keywords |
|-------|---------|----------------------|
| **HCS Customer Manager** | Core CRM | customer, crm, customer data |
| **HCS Customer Support Manager** | Ticket system | support, tickets, help desk |
| **HCS Customer Communication Manager** | Email/SMS/Push | email, sms, notification |
| **HCS Customer Feedback Manager** | Reviews & surveys | feedback, reviews, surveys, nps |
| **HCS Customer Journey Manager** | Lifecycle tracking | journey, lifecycle, churn |

### Supporting Agents

| Agent | Purpose | Auto-Trigger Keywords |
|-------|---------|----------------------|
| **HCS Deployer** | Deployment | deploy, push, publish |
| **HCS Local Host Testing** | Local testing | local, preview, localhost |
| **HCS Human Tester** | QA testing | test, quality, manual test |
| **HCS Link Analyser** | Link validation | link, url, broken link |
| **HCS SEO Analyzer** | SEO optimization | seo, meta tags, keywords |
| **HCS UI Designer** | Premium design | ui design, glassmorphism |
| **HCS Content Rephraser** | Content enhancement | rephrase, enhance, research |

### Auto-Trigger Mapping

```
USER REQUEST: "Build admin dashboard"
    |
    v
AUTO-TRIGGER ALL ADMIN AGENTS:
    |
    ├── HCS Admin Auth Manager
    |   |-- Build login/register
    |   |-- Implement RBAC
    |   |-- Add session management
    |   |-- Add OAuth/2FA
    |
    ├── HCS Admin Analytics Dashboard
    |   |-- Build overview dashboard
    |   |-- Add revenue tracking
    |   |-- Add traffic analytics
    |   |-- Add user metrics
    |
    ├── HCS Admin Content Manager
    |   |-- Build CMS system
    |   |-- Add rich text editor
    |   |-- Add media library
    |   |-- Add categories/tags
    |
    ├── HCS Admin User Manager
    |   |-- Build user management
    |   |-- Add role management
    |   |-- Add activity logging
    |   |-- Add bulk operations
    |
    ├── HCS Admin Settings Manager
    |   |-- Build settings system
    |   |-- Add site configuration
    |   |-- Add email settings
    |   |-- Add security settings
    |
    ├── HCS Customer Manager
    |   |-- Build customer CRM
    |   |-- Add customer profiles
    |   |-- Add segmentation
    |   |-- Add interaction tracking
    |
    ├── HCS Customer Support Manager
    |   |-- Build ticket system
    |   |-- Add live chat
    |   |-- Add SLA tracking
    |   |-- Add canned responses
    |
    ├── HCS Customer Communication Manager
    |   |-- Build email campaigns
    |   |-- Add SMS messaging
    |   |-- Add push notifications
    |   |-- Add templates
    |
    ├── HCS Customer Feedback Manager
    |   |-- Build review system
    |   |-- Add surveys
    |   |-- Add NPS tracking
    |   |-- Add sentiment analysis
    |
    └── HCS Customer Journey Manager
        |-- Build journey tracking
        |-- Add funnel analysis
        |-- Add churn prediction
        |-- Add interventions
```

---

## ADMIN DASHBOARD ARCHITECTURE

### Dashboard Structure

```
admin/
├── auth/
│   ├── login/
│   ├── register/
│   ├── forgot-password/
│   └── reset-password/
├── dashboard/
│   ├── page.tsx (Overview)
│   ├── analytics/
│   │   ├── revenue/
│   │   ├── traffic/
│   │   └── users/
│   └── reports/
├── content/
│   ├── pages/
│   ├── posts/
│   ├── media/
│   └── categories/
├── users/
│   ├── list/
│   ├── roles/
│   └── activity/
├── customers/
│   ├── list/
│   ├── segments/
│   └── [customerId]/
├── support/
│   ├── tickets/
│   ├── chat/
│   └── knowledge-base/
├── communications/
│   ├── campaigns/
│   ├── templates/
│   └── automation/
├── feedback/
│   ├── reviews/
│   ├── surveys/
│   └── nps/
├── settings/
│   ├── general/
│   ├── appearance/
│   ├── seo/
│   ├── email/
│   ├── security/
│   └── integrations/
└── layout.tsx
```

### Database Schema (All Tables)

```sql
-- AUTH TABLES
CREATE TABLE users (...);
CREATE TABLE roles (...);
CREATE TABLE permissions (...);
CREATE TABLE role_permissions (...);
CREATE TABLE sessions (...);

-- CONTENT TABLES
CREATE TABLE content (...);
CREATE TABLE content_meta (...);
CREATE TABLE categories (...);
CREATE TABLE tags (...);
CREATE TABLE content_tags (...);
CREATE TABLE media (...);
CREATE TABLE content_versions (...);

-- CUSTOMER TABLES
CREATE TABLE customers (...);
CREATE TABLE customer_interactions (...);
CREATE TABLE customer_segments (...);
CREATE TABLE customer_tags (...);

-- SUPPORT TABLES
CREATE TABLE support_tickets (...);
CREATE TABLE ticket_responses (...);
CREATE TABLE canned_responses (...);

-- FEEDBACK TABLES
CREATE TABLE customer_reviews (...);
CREATE TABLE surveys (...);
CREATE TABLE survey_responses (...);
CREATE TABLE nps_responses (...);

-- JOURNEY TABLES
CREATE TABLE journey_stages (...);
CREATE TABLE customer_journey_events (...);
CREATE TABLE customer_stages (...);
CREATE TABLE journey_interventions (...);

-- ANALYTICS TABLES
CREATE TABLE analytics_events (...);
CREATE TABLE revenue (...);
CREATE TABLE page_views (...);

-- CAMPAIGN TABLES
CREATE TABLE campaigns (...);
CREATE TABLE templates (...);
CREATE TABLE campaign_sends (...);
CREATE TABLE automation_rules (...);

-- SETTINGS TABLES
CREATE TABLE settings (...);
CREATE TABLE settings_history (...);
```

---

## INTEGRATION MATRIX

### How Admin Agents Work Together

| User Action | Agents Involved | Flow |
|-------------|----------------|------|
| **Create User** | Auth Manager → User Manager | Auth creates account, User Manager sets profile |
| **Customer Signs Up** | Auth Manager → Customer Manager → Journey Manager | Auth handles signup, CRM creates profile, Journey tracks |
| **Customer Buys** | Customer Manager → Analytics → Journey | CRM updates LTV, Analytics tracks revenue, Journey updates stage |
| **Customer Contacts Support** | Support Manager → Customer Manager | Ticket created, Customer profile updated |
| **Send Campaign** | Communication Manager → Customer Manager → Analytics | Campaign sent, Customers tracked, Results analyzed |
| **Customer Gives Feedback** | Feedback Manager → Support Manager → Journey | Review logged, Support follows up, Journey updated |
| **Admin Views Dashboard** | Analytics → All Agents | Dashboard pulls data from all agents |

### Data Flow

```
CUSTOMER ACTION
    |
    v
AUTH MANAGER (Authentication)
    |
    v
CUSTOMER MANAGER (Profile Update)
    |
    v
JOURNEY MANAGER (Stage Update)
    |
    v
ANALYTICS (Metrics Update)
    |
    v
COMMUNICATION MANAGER (If triggered)
    |
    v
FEEDBACK MANAGER (If feedback)
    |
    v
SUPPORT MANAGER (If issue)
```

---

## AUTO-BUILD CHECKLIST

When "dashboard" is mentioned, automatically build:

- [ ] **Authentication System**
  - [ ] Login page
  - [ ] Register page
  - [ ] Forgot password page
  - [ ] RBAC implementation
  - [ ] Session management

- [ ] **Analytics Dashboard**
  - [ ] Overview page
  - [ ] Revenue tracking
  - [ ] Traffic analytics
  - [ ] User metrics
  - [ ] Chart components

- [ ] **Content Management**
  - [ ] Content list
  - [ ] Rich text editor
  - [ ] Media library
  - [ ] Categories/tags

- [ ] **User Management**
  - [ ] User list
  - [ ] User detail
  - [ ] Role management
  - [ ] Activity log

- [ ] **Customer Management**
  - [ ] Customer CRM
  - [ ] Customer profiles
  - [ ] Segmentation
  - [ ] Interaction tracking

- [ ] **Support System**
  - [ ] Ticket system
  - [ ] Live chat widget
  - [ ] SLA tracking
  - [ ] Canned responses

- [ ] **Communication**
  - [ ] Email campaigns
  - [ ] SMS messaging
  - [ ] Push notifications
  - [ ] Templates

- [ ] **Feedback System**
  - [ ] Reviews management
  - [ ] Survey builder
  - [ ] NPS tracking

- [ ] **Journey Tracking**
  - [ ] Journey map
  - [ ] Funnel analysis
  - [ ] Churn prediction

- [ ] **Settings**
  - [ ] General settings
  - [ ] Appearance settings
  - [ ] SEO settings
  - [ ] Email settings
  - [ ] Security settings

---

### Step 1: Website Type Detection

| Website Type | Dashboard Requirements |
|--------------|----------------------|
| **E-commerce** | Orders, products, inventory, payments, customers, shipping |
| **SaaS** | Subscriptions, usage, billing, features, support tickets |
| **Blog/Content** | Posts, comments, authors, SEO, analytics |
| **Marketplace** | Sellers, buyers, listings, transactions, disputes |
| **Social Platform** | Users, posts, reports, moderation, engagement |
| **Learning (LMS)** | Courses, students, progress, certifications |
| **Service Platform** | Providers, bookings, payments, reviews |
| **Portfolio** | Projects, clients, invoices, proposals |

### Step 2: Feature Inventory

```markdown
## WEBSITE FEATURE ANALYSIS

### Existing Features Detected
- [ ] User Authentication
- [ ] Payment Processing
- [ ] Content Management
- [ ] Email System
- [ ] SMS Notifications
- [ ] Push Notifications
- [ ] Analytics Tracking
- [ ] Search Functionality
- [ ] File Upload
- [ ] Real-time Chat
- [ ] API Integration
- [ ] Third-party Services

### Missing Features (Dashboard Can Add)
- [ ] Admin Authentication
- [ ] Role-based Access Control
- [ ] Audit Logging
- [ ] Data Export
- [ ] Bulk Operations
- [ ] Advanced Filtering
- [ ] Custom Reports
- [ ] Scheduled Tasks
```

### Step 3: Tech Stack Detection

| Detected Stack | Dashboard Implementation |
|----------------|------------------------|
| **Next.js/React** | Admin dashboard with React components |
| **Vue/Nuxt** | Admin dashboard with Vue components |
| **Node.js/Express** | Admin API with REST endpoints |
| **Python/Django** | Django Admin customization |
| **PHP/Laravel** | Laravel Nova or Filament |
| **Static Site** | Headless CMS admin panel |

---

## TOOL SUGGESTION ENGINE

### Dashboard Framework Recommendations

| Website Type | Recommended Dashboard Tools |
|--------------|---------------------------|
| **Next.js** | Next.js Admin, Refine, AdminJS |
| **React** | React-Admin, Refine, Ant Design Pro |
| **Vue** | Vue Element Admin, Vuetify Dashboard |
| **Node.js** | AdminJS, Express Admin |
| **Python** | Django Admin, Flask-Admin |
| **PHP** | Laravel Nova, Filament, October CMS |

### Essential Dashboard Components

| Component | Purpose | Priority |
|-----------|---------|----------|
| **Authentication** | Admin login security | CRITICAL |
| **Dashboard Home** | Overview metrics | CRITICAL |
| **User Management** | Manage users | HIGH |
| **Content Management** | Manage content | HIGH |
| **Analytics** | Traffic and behavior | HIGH |
| **Revenue** | Financial tracking | HIGH |
| **Notifications** | Alerts and messages | MEDIUM |
| **Settings** | Configuration | MEDIUM |
| **Logs** | Audit trail | MEDIUM |
| **Reports** | Custom reports | LOW |

### Revenue Dashboard Tools

| Tool Type | Recommendation |
|-----------|---------------|
| **Charts** | Chart.js, Recharts, D3.js |
| **Tables** | TanStack Table, AG Grid |
| **Metrics** | CountUp, React-Countup |
| **Date Picker** | React Datepicker, Day.js |
| **Export** | SheetJS, PDFMake |

### Analytics Dashboard Tools

| Tool Type | Recommendation |
|-----------|---------------|
| **Real-time** | Socket.io, Firebase |
| **Charts** | Chart.js, Plotly.js |
| **Heatmaps** | Heatmap.js, Leaflet |
| **Funnels** | Custom components |
| **A/B Testing** | LaunchDarkly, Split.io |

---

## DASHBOARD ARCHITECTURE

### Standard Admin Dashboard Structure

```
admin-dashboard/
├── components/
│   ├── auth/
│   │   ├── LoginForm.jsx
│   │   ├── ProtectedRoute.jsx
│   │   └── RoleGuard.jsx
│   ├── layout/
│   │   ├── Sidebar.jsx
│   │   ├── Header.jsx
│   │   └── MainLayout.jsx
│   ├── dashboard/
│   │   ├── StatsCard.jsx
│   │   ├── Chart.jsx
│   │   └── RecentActivity.jsx
│   ├── users/
│   │   ├── UserList.jsx
│   │   ├── UserDetail.jsx
│   │   └── UserForm.jsx
│   ├── content/
│   │   ├── ContentList.jsx
│   │   ├── ContentEditor.jsx
│   │   └── MediaLibrary.jsx
│   ├── analytics/
│   │   ├── TrafficChart.jsx
│   │   ├── UserBehavior.jsx
│   │   └── ConversionFunnel.jsx
│   ├── revenue/
│   │   ├── RevenueChart.jsx
│   │   ├── TransactionList.jsx
│   │   └── PaymentSettings.jsx
│   ├── whatsapp/
│   │   ├── CampaignManager.jsx
│   │   ├── MessageTemplates.jsx
│   │   └── ContactGroups.jsx
│   └── settings/
│       ├── GeneralSettings.jsx
│       ├── NotificationSettings.jsx
│       └── SecuritySettings.jsx
├── pages/
│   ├── index.jsx (Dashboard Home)
│   ├── users.jsx
│   ├── content.jsx
│   ├── analytics.jsx
│   ├── revenue.jsx
│   ├── whatsapp.jsx
│   ├── reports.jsx
│   └── settings.jsx
├── services/
│   ├── api.js
│   ├── auth.js
│   ├── analytics.js
│   └── whatsapp.js
├── hooks/
│   ├── useAuth.js
│   ├── useAnalytics.js
│   └── usePermissions.js
├── utils/
│   ├── permissions.js
│   ├── formatters.js
│   └── validators.js
└── styles/
    └── admin.css
```

---

## PERMISSIONS SYSTEM

### Role-Based Access Control (RBAC)

```javascript
// Permission Definitions
const PERMISSIONS = {
  // Super Admin
  SUPER_ADMIN: [
    'dashboard:read',
    'dashboard:write',
    'users:read',
    'users:write',
    'users:delete',
    'content:read',
    'content:write',
    'content:delete',
    'analytics:read',
    'revenue:read',
    'revenue:write',
    'whatsapp:read',
    'whatsapp:write',
    'settings:read',
    'settings:write',
    'logs:read',
    'reports:read',
    'reports:write'
  ],
  
  // Admin
  ADMIN: [
    'dashboard:read',
    'users:read',
    'users:write',
    'content:read',
    'content:write',
    'analytics:read',
    'revenue:read',
    'whatsapp:read',
    'whatsapp:write',
    'settings:read',
    'reports:read'
  ],
  
  // Editor
  EDITOR: [
    'dashboard:read',
    'content:read',
    'content:write',
    'analytics:read',
    'reports:read'
  ],
  
  // Viewer
  VIEWER: [
    'dashboard:read',
    'analytics:read',
    'reports:read'
  ]
};

// Role Definitions
const ROLES = {
  SUPER_ADMIN: {
    name: 'Super Admin',
    description: 'Full system access',
    permissions: PERMISSIONS.SUPER_ADMIN,
    color: '#FF0000'
  },
  ADMIN: {
    name: 'Admin',
    description: 'Standard admin access',
    permissions: PERMISSIONS.ADMIN,
    color: '#FF6600'
  },
  EDITOR: {
    name: 'Editor',
    description: 'Content management access',
    permissions: PERMISSIONS.EDITOR,
    color: '#0066FF'
  },
  VIEWER: {
    name: 'Viewer',
    description: 'Read-only access',
    permissions: PERMISSIONS.VIEWER,
    color: '#00CC00'
  }
};
```

### Permission Guard Component

```jsx
// PermissionGuard.jsx
import { useAuth } from '../hooks/useAuth';

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

// Usage Example
<PermissionGuard permission="users:write">
  <UserManagement />
</PermissionGuard>
```

---

## WHATSAPP MARKETING INTEGRATION

### Campaign Manager Component

```jsx
// CampaignManager.jsx
import { useState } from 'react';

export function CampaignManager() {
  const [campaigns, setCampaigns] = useState([]);
  const [templates, setTemplates] = useState([]);
  const [contacts, setContacts] = useState([]);
  
  const createCampaign = async (campaignData) => {
    // Create campaign with templates and contacts
    const campaign = {
      id: Date.now(),
      name: campaignData.name,
      template: campaignData.template,
      contacts: campaignData.contacts,
      scheduledAt: campaignData.scheduledAt,
      status: 'scheduled',
      stats: {
        sent: 0,
        delivered: 0,
        read: 0,
        replied: 0
      }
    };
    
    setCampaigns([...campaigns, campaign]);
    return campaign;
  };
  
  const sendCampaign = async (campaignId) => {
    // Send campaign to all contacts
    const campaign = campaigns.find(c => c.id === campaignId);
    if (campaign) {
      // Integrate with WhatsApp API
      console.log('Sending campaign:', campaign);
    }
  };
  
  return (
    <div className="campaign-manager">
      <h2>WhatsApp Campaign Manager</h2>
      {/* Campaign creation form */}
      {/* Campaign list */}
      {/* Campaign stats */}
    </div>
  );
}
```

### Message Templates

| Template Type | Use Case |
|--------------|----------|
| **Welcome** | New user registration |
| **Promotional** | Sales and offers |
| **Transactional** | Order updates |
| **Reminder** | Cart abandonment |
| **Feedback** | Post-purchase review |

---

## REVENUE DASHBOARD

### Revenue Metrics

| Metric | Description | Calculation |
|--------|-------------|-------------|
| **MRR** | Monthly Recurring Revenue | Sum of all subscriptions |
| **ARR** | Annual Recurring Revenue | MRR × 12 |
| **AOV** | Average Order Value | Revenue / Orders |
| **LTV** | Customer Lifetime Value | AOV × Purchase Frequency |
| **Churn Rate** | Customer Attrition | Lost Customers / Total |
| **Conversion Rate** | Purchase Rate | Orders / Visitors |

### Revenue Chart Component

```jsx
// RevenueChart.jsx
import { Line } from 'react-chartjs-2';

export function RevenueChart({ data }) {
  const chartData = {
    labels: data.map(d => d.date),
    datasets: [
      {
        label: 'Revenue',
        data: data.map(d => d.revenue),
        borderColor: '#4CAF50',
        backgroundColor: 'rgba(76, 175, 80, 0.1)',
        fill: true
      },
      {
        label: 'Expenses',
        data: data.map(d => d.expenses),
        borderColor: '#F44336',
        backgroundColor: 'rgba(244, 67, 54, 0.1)',
        fill: true
      }
    ]
  };
  
  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top'
      }
    },
    scales: {
      y: {
        beginAtZero: true
      }
    }
  };
  
  return <Line data={chartData} options={options} />;
}
```

---

## TRAFFIC ANALYTICS DASHBOARD

### Traffic Metrics

| Metric | Description | Source |
|--------|-------------|--------|
| **Page Views** | Total page views | Analytics API |
| **Unique Visitors** | Distinct users | Analytics API |
| **Session Duration** | Time on site | Analytics API |
| **Bounce Rate** | Single-page sessions | Analytics API |
| **Traffic Sources** | Where visitors come from | Analytics API |
| **Top Pages** | Most visited pages | Analytics API |
| **Device Types** | Desktop/Mobile/Tablet | Analytics API |
| **Geographic** | Visitor locations | Analytics API |

### Traffic Chart Component

```jsx
// TrafficChart.jsx
import { Bar } from 'react-chartjs-2';

export function TrafficChart({ data }) {
  const chartData = {
    labels: data.map(d => d.source),
    datasets: [
      {
        label: 'Visitors',
        data: data.map(d => d.visitors),
        backgroundColor: [
          '#4CAF50',
          '#2196F3',
          '#FF9800',
          '#9C27B0',
          '#F44336'
        ]
      }
    ]
  };
  
  const options = {
    responsive: true,
    plugins: {
      legend: {
        display: false
      }
    },
    scales: {
      y: {
        beginAtZero: true
      }
    }
  };
  
  return <Bar data={chartData} options={options} />;
}
```

---

## FEATURE REQUEST SYSTEM

### Feature Request Component

```jsx
// FeatureRequest.jsx
import { useState } from 'react';

export function FeatureRequest() {
  const [requests, setRequests] = useState([]);
  const [newRequest, setNewRequest] = useState({
    title: '',
    description: '',
    priority: 'medium',
    category: 'general'
  });
  
  const submitRequest = async (request) => {
    const featureRequest = {
      id: Date.now(),
      ...request,
      status: 'pending',
      votes: 0,
      createdAt: new Date(),
      updatedAt: new Date()
    };
    
    setRequests([...requests, featureRequest]);
    return featureRequest;
  };
  
  const voteRequest = async (requestId) => {
    setRequests(requests.map(r => 
      r.id === requestId 
        ? { ...r, votes: r.votes + 1 }
        : r
    ));
  };
  
  const approveRequest = async (requestId) => {
    setRequests(requests.map(r => 
      r.id === requestId 
        ? { ...r, status: 'approved', updatedAt: new Date() }
        : r
    ));
  };
  
  return (
    <div className="feature-request">
      <h2>Feature Requests</h2>
      {/* Request form */}
      {/* Request list with voting */}
      {/* Admin approval panel */}
    </div>
  );
}
```

### Feature Request Workflow

```
USER SUBMITS REQUEST
    |
    v
REQUEST CREATED (Status: Pending)
    |
    v
ADMIN REVIEWS
    |
    ├── APPROVED → Build Feature
    |               |
    |               v
    |           FEATURE BUILT
    |               |
    |               v
    |           DEPLOYED
    |
    ├── REJECTED → User Notified
    |
    └── PENDING → Awaits Review
```

---

## SMART DASHBOARD BUILDER WORKFLOW

### Phase 1: Analysis

```
WEBSITE ANALYSIS REQUEST
    |
    v
ANALYZE WEBSITE TYPE
    |-- E-commerce, SaaS, Blog, etc.
    |-- Existing features
    |-- Tech stack
    |-- User base
    |
    v
IDENTIFY DASHBOARD NEEDS
    |-- Essential components
    |-- Required integrations
    |-- Permission levels
    |-- Data sources
    |
    v
SUGGEST TOOLS
    |-- Dashboard framework
    |-- Chart libraries
    |-- Table components
    |-- Auth solutions
    |
    v
GENERATE ARCHITECTURE
    |-- File structure
    |-- Component hierarchy
    |-- API endpoints
    |-- Database schema
```

### Phase 2: Building

```
DASHBOARD BUILD REQUEST
    |
    v
CREATE PROJECT STRUCTURE
    |-- Initialize project
    |-- Install dependencies
    |-- Set up configuration
    |
    v
BUILD CORE COMPONENTS
    |-- Authentication
    |-- Layout
    |-- Navigation
    |
    v
BUILD FEATURE COMPONENTS
    |-- Dashboard home
    |-- User management
    |-- Content management
    |-- Analytics
    |-- Revenue
    |-- WhatsApp marketing
    |
    v
IMPLEMENT PERMISSIONS
    |-- Role definitions
    |-- Permission guards
    |-- Access controls
    |
    v
INTEGRATE SERVICES
    |-- API connections
    |-- Real-time updates
    |-- External services
    |
    v
TEST AND DEPLOY
    |-- Unit tests
    |-- Integration tests
    |-- Deployment
```

---

## DASHBOARD COMPONENT TEMPLATES

### Stats Card

```jsx
// StatsCard.jsx
export function StatsCard({ title, value, change, icon, color }) {
  return (
    <div className="stats-card" style={{ borderLeftColor: color }}>
      <div className="stats-icon">{icon}</div>
      <div className="stats-content">
        <h3>{title}</h3>
        <p className="stats-value">{value}</p>
        <p className={`stats-change ${change >= 0 ? 'positive' : 'negative'}`}>
          {change >= 0 ? '+' : ''}{change}%
        </p>
      </div>
    </div>
  );
}

// Usage
<StatsCard
  title="Total Revenue"
  value="$45,231"
  change={12.5}
  icon="💰"
  color="#4CAF50"
/>
```

### Data Table

```jsx
// DataTable.jsx
import { useState } from 'react';

export function DataTable({ columns, data, actions }) {
  const [sortConfig, setSortConfig] = useState({ key: null, direction: 'asc' });
  const [filter, setFilter] = useState('');
  
  const sortedData = [...data].sort((a, b) => {
    if (sortConfig.key) {
      if (a[sortConfig.key] < b[sortConfig.key]) {
        return sortConfig.direction === 'asc' ? -1 : 1;
      }
      if (a[sortConfig.key] > b[sortConfig.key]) {
        return sortConfig.direction === 'asc' ? 1 : -1;
      }
    }
    return 0;
  });
  
  const filteredData = sortedData.filter(row =>
    Object.values(row).some(value =>
      String(value).toLowerCase().includes(filter.toLowerCase())
    )
  );
  
  return (
    <div className="data-table">
      <input
        type="text"
        placeholder="Search..."
        value={filter}
        onChange={(e) => setFilter(e.target.value)}
      />
      <table>
        <thead>
          <tr>
            {columns.map(column => (
              <th
                key={column.key}
                onClick={() => handleSort(column.key)}
              >
                {column.title}
                {sortConfig.key === column.key && (
                  <span>{sortConfig.direction === 'asc' ? ' ↑' : ' ↓'}</span>
                )}
              </th>
            ))}
            {actions && <th>Actions</th>}
          </tr>
        </thead>
        <tbody>
          {filteredData.map((row, index) => (
            <tr key={index}>
              {columns.map(column => (
                <td key={column.key}>{row[column.key]}</td>
              ))}
              {actions && (
                <td>{actions(row)}</td>
              )}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
```

---

## INTEGRATION WITH OTHER HCS AGENTS

### Agent Collaboration

| Agent | Purpose |
|-------|---------|
| **HCS Deployer** | Deploy admin dashboard |
| **HCS Tester** | Test dashboard functionality |
| **HCS Link Analyser** | Test all dashboard links |
| **HCS WhatsApp Marketing** | WhatsApp campaign integration |
| **HCS Marketing Agent** | Marketing analytics integration |
| **HCS UI Designer** | Premium dashboard design |
| **HCS Skill Builder** | Extend dashboard capabilities |

### Workflow Integration

```
USER REQUEST: "Build admin dashboard"
    |
    v
HCS Admin Dashboard Builder
    |-- Analyzes website
    |-- Suggests tools
    |-- Builds dashboard
    |
    v
HCS UI Designer
    |-- Designs premium UI
    |-- Adds animations
    |-- Ensures accessibility
    |
    v
HCS Tester
    |-- Tests all components
    |-- Validates permissions
    |-- Checks integrations
    |
    v
HCS Link Analyser
    |-- Tests all links
    |-- Validates navigation
    |-- Checks redirects
    |
    v
HCS Deployer
    |-- Deploys dashboard
    |-- Sets up environment
    |-- Configures domain
```

---

## OUTPUT FORMAT

### Dashboard Generation Output

```markdown
## ADMIN DASHBOARD GENERATED

### Project Structure
[Complete file structure]

### Core Components
[All core components with code]

### Feature Components
[All feature components with code]

### Services
[API and service integrations]

### Configuration
[Environment and config files]

### Deployment Instructions
[How to deploy the dashboard]
```

---

## QUALITY STANDARDS

### Dashboard Requirements

- [ ] **Security** — Authentication and authorization
- [ ] **Performance** — Fast loading and rendering
- [ ] **Responsive** — Works on all devices
- [ ] **Accessible** — WCAG compliant
- [ ] **Maintainable** — Clean, documented code
- [ ] **Scalable** — Can grow with the website
- [ ] **Integrated** — Connects to all services
- [ ] **Real-time** — Live updates where needed

### Code Quality

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

*Generated by HCS Skill Builder System*
*Version: 1.0.0*
*Status: ACTIVE*