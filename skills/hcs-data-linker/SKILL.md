# HCS Data Linker Skill

> **HCS SKILL** — Created by HCS Skill Builder System
> **Version:** 1.0.0
> **Last Updated:** 2026-07-08
> **Status:** ACTIVE
> **Category:** Development / Integration / Data Linking

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

This skill provides **data linking between backend, frontend, and calculation logic** by:
1. **Analyzing** all components (backend, frontend, calculations)
2. **Linking** data flow between components
3. **Fixing** broken connections automatically
4. **Enhancing** code for better integration
5. **Researching** best practices
6. **Saving** linking information for future reference

---

## SKILL TRIGGERS

| Trigger Phrase | Action |
|----------------|--------|
| "data link" | Start data linking |
| "link data" | Start data linking |
| "connect backend" | Connect backend to frontend |
| "connect frontend" | Connect frontend to backend |
| "connect api" | Connect API to frontend |
| "integrate" | Integrate systems |
| "sync" | Sync data between systems |
| "calculation" | Link calculation logic |
| "formula" | Link formulas |
| "inventory" | Link inventory system |
| "orders" | Link order system |
| "saas" | Link SaaS components |
| "ecommerce" | Link e-commerce components |
| "hotel" | Link hotel booking system |
| "booking" | Link booking system |
| "fix link" | Fix broken connections |
| "data mismatch" | Fix data mismatches |

---

## DATA LINKING COMPONENTS

### What is Data Linking?

| Component | Description | Examples |
|-----------|-------------|----------|
| **Backend** | Server-side logic | Google Apps Script, Node.js, Python, API |
| **Frontend** | Client-side interface | HTML, React, Vue, Angular |
| **Calculation Logic** | Business rules, formulas | JSON, Google Sheets formulas, Python functions |
| **Database** | Data storage | Google Sheets, MongoDB, PostgreSQL |
| **API Layer** | Communication layer | REST, GraphQL, WebSocket |

### Data Linking Flow

```
USER INTERACTION (Frontend)
    |
    v
API REQUEST (Frontend → Backend)
    |
    v
BACKEND PROCESSING
    |-- Receive request
    |-- Validate data
    |-- Process logic
    |-- Apply calculations
    |
    v
DATABASE OPERATION
    |-- Read/Write data
    |-- Update records
    |-- Query results
    |
    v
CALCULATION LOGIC
    |-- Apply formulas
    |-- Calculate totals
    |-- Generate results
    |
    v
API RESPONSE (Backend → Frontend)
    |
    v
FRONTEND DISPLAY
    |-- Show results
    |-- Update UI
    |-- Handle errors
```

---

## DATA LINKING WORKFLOW

### 12-Stage Data Linking Pipeline

```
DATA LINKING REQUEST RECEIVED
    |
    v
STAGE 1: ANALYZE REQUEST
    |-- Identify what needs to be linked
    |-- Map backend components
    |-- Map frontend components
    |-- Map calculation logic
    |
    v
STAGE 2: RESEARCH BEST PRACTICES
    |-- Research similar integrations
    |-- Find best patterns
    |-- Check latest APIs
    |-- Review security practices
    |
    v
STAGE 3: MAP DATA FLOW
    |-- Frontend → Backend flow
    |-- Backend → Database flow
    |-- Calculation logic flow
    |-- Response flow
    |
    v
STAGE 4: IDENTIFY CONNECTIONS
    |-- API endpoints needed
    |-- Data models needed
    |-- Calculation functions needed
    |-- Validation rules needed
    |
    v
STAGE 5: CHECK EXISTING CODE
    |-- Frontend code analysis
    |-- Backend code analysis
    |-- Calculation logic analysis
    |-- Database schema analysis
    |
    v
STAGE 6: IDENTIFY ISSUES
    |-- Missing connections
    |-- Data mismatches
    |-- Broken links
    |-- Logic errors
    |
    v
STAGE 7: FIX ISSUES
    |-- Fix frontend code
    |-- Fix backend code
    |-- Fix calculation logic
    |-- Fix database queries
    |
    v
STAGE 8: ENHANCE CODE
    |-- Add error handling
    |-- Add validation
    |-- Add logging
    |-- Add optimization
    |
    v
STAGE 9: TEST CONNECTIONS
    |-- Test frontend → backend
    |-- Test backend → database
    |-- Test calculations
    |-- Test error handling
    |
    v
STAGE 10: VERIFY DATA FLOW
    |-- Verify data flows correctly
    |-- Verify calculations are correct
    |-- Verify responses are correct
    |-- Verify errors are handled
    |
    v
STAGE 11: SAVE LINKING INFO
    |-- Save connection map
    |-- Save data flow diagram
    |-- Save configuration
    |-- Save documentation
    |
    v
STAGE 12: PROVIDE REPORT
    |-- Linking report
    |-- Issues found and fixed
    |-- Enhancements made
    |-- Recommendations
    |
    v
DATA LINKING COMPLETE
```

---

## DATA LINKING BY WEBSITE TYPE

### E-commerce Linking

| Component | Linking Requirements |
|-----------|---------------------|
| **Product Catalog** | Frontend display ↔ Backend API ↔ Database |
| **Shopping Cart** | Frontend cart ↔ Backend cart API ↔ Inventory |
| **Checkout** | Frontend form ↔ Backend payment ↔ Database |
| **Orders** | Frontend orders ↔ Backend orders API ↔ Database |
| **Inventory** | Backend inventory ↔ Calculation logic ↔ Database |

### SaaS Linking

| Component | Linking Requirements |
|-----------|---------------------|
| **User Auth** | Frontend login ↔ Backend auth ↔ Database |
| **Subscriptions** | Frontend plans ↔ Backend billing ↔ Database |
| **Usage Tracking** | Frontend usage ↔ Backend tracking ↔ Calculation |
| **Billing** | Backend billing ↔ Calculation logic ↔ Database |
| **Features** | Frontend features ↔ Backend permissions ↔ Database |

### Hotel/Booking Linking

| Component | Linking Requirements |
|-----------|---------------------|
| **Room Search** | Frontend search ↔ Backend search API ↔ Database |
| **Availability** | Backend availability ↔ Calculation logic ↔ Database |
| **Pricing** | Backend pricing ↔ Calculation logic ↔ Database |
| **Booking** | Frontend booking ↔ Backend booking API ↔ Database |
| **Cancellation** | Frontend cancel ↔ Backend cancel API ↔ Database |

### Inventory Management Linking

| Component | Linking Requirements |
|-----------|---------------------|
| **Stock Levels** | Backend stock ↔ Calculation logic ↔ Database |
| **Orders** | Frontend orders ↔ Backend orders ↔ Inventory |
| **Receiving** | Backend receiving ↔ Inventory ↔ Database |
| **Shipping** | Backend shipping ↔ Inventory ↔ Database |
| **Reports** | Backend reports ↔ Calculation logic ↔ Frontend |

---

## RESEARCH & ANALYSIS

### Research Areas

| Area | Research Focus |
|------|----------------|
| **API Best Practices** | REST, GraphQL, authentication, rate limiting |
| **Data Flow Patterns** | Event-driven, request-response, pub-sub |
| **Error Handling** | Retry logic, fallbacks, graceful degradation |
| **Security** | Input validation, CORS, authentication |
| **Performance** | Caching, pagination, optimization |
| **Testing** | Unit tests, integration tests, e2e tests |

### Research Commands

```bash
# Research similar integrations
SEARCH: "[backend] + [frontend] integration best practices 2026"
SEARCH: "[backend] + [frontend] data flow patterns"
SEARCH: "[backend] + [frontend] error handling"

# Research specific technologies
SEARCH: "Google Apps Script + HTML frontend integration"
SEARCH: "Node.js + React data linking"
SEARCH: "Python + Vue.js API integration"

# Research security
SEARCH: "[backend] + [frontend] security best practices"
SEARCH: "CORS configuration for [backend]"
SEARCH: "API authentication best practices"

# Research performance
SEARCH: "[backend] + [frontend] performance optimization"
SEARCH: "API caching strategies"
SEARCH: "Database query optimization"
```

---

## SAVING LINKING INFORMATION

### What to Save

| Information | Purpose |
|-------------|---------|
| **Connection Map** | Shows all connections between components |
| **Data Flow Diagram** | Shows how data flows through system |
| **Configuration** | API URLs, endpoints, settings |
| **Documentation** | How everything is connected |
| **Test Results** | What was tested and results |

### Save Format

```json
{
  "linkingInfo": {
    "date": "2026-07-08",
    "project": "E-commerce Website",
    "components": {
      "backend": {
        "type": "Google Apps Script",
        "url": "https://script.google.com/macros/s/[ID]/exec",
        "functions": ["getOrder", "saveOrder", "calculateTotal"]
      },
      "frontend": {
        "type": "HTML/JavaScript",
        "pages": ["orders.html", "checkout.html", "invoice.html"]
      },
      "calculation": {
        "type": "JSON",
        "formulas": ["orderTotal", "taxCalc", "discountCalc"]
      },
      "database": {
        "type": "Google Sheets",
        "sheets": ["Orders", "Products", "Customers"]
      }
    },
    "connections": [
      {
        "from": "frontend",
        "to": "backend",
        "type": "API",
        "endpoint": "/exec?fn=getOrder"
      },
      {
        "from": "backend",
        "to": "database",
        "type": "Read/Write",
        "sheet": "Orders"
      }
    ],
    "dataFlow": [
      "Frontend → Backend → Database",
      "Backend → Calculation → Backend"
    ]
  }
}
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

---

## QUALITY STANDARDS

### Data Linking Quality Checklist

- [ ] **All components connected** — Backend, frontend, calculations linked
- [ ] **Data flows correctly** — No broken connections
- [ ] **Calculations accurate** — All formulas work correctly
- [ ] **Error handling complete** — All errors handled gracefully
- [ ] **Security implemented** — Input validation, authentication
- [ ] **Performance optimized** — Caching, pagination
- [ ] **Documentation complete** — How everything is connected
- [ ] **Tests passing** — All connections tested

### Code Quality

- [ ] **Clean code** — Well-organized, readable
- [ ] **Modular design** — Separated concerns
- [ ] **Type safe** — Proper data types
- [ ] **Error resistant** — Try-catch blocks
- [ ] **Well documented** — Clear comments
- [ ] **Tested** — Unit and integration tests

---

## HCS PREFIX RULE

**PERMANENT AND MANDATORY**

This rule is PERMANENT and applies to ALL skills created by this agent:

1. **ALL Skills MUST Have HCS Prefix**
   - Every skill created must start with "HCS"
   - No exceptions allowed
   - This is permanent and cannot be changed

2. **Skill Names**
   - ✅ `hcs-data-linker`
   - ✅ `hcs-data-integration`
   - ❌ `data-linker`
   - ❌ `data-integration`

3. **Agent Names**
   - ✅ `hcs-data-linker-agent.md`
   - ❌ `data-linker-agent.md`
   - ❌ `linker.md`

4. **Enforcement**
   - Before creating any skill, check prefix
   - If no HCS prefix, add it
   - Never create skills without HCS prefix
   - This rule is permanent and cannot be changed

---

## SUCCESS METRICS

The HCS Data Linker Skill is successful when:

- [ ] All components are connected
- [ ] Data flows correctly
- [ ] Calculations are accurate
- [ ] Error handling works
- [ ] Security is implemented
- [ ] Performance is optimized
- [ ] Documentation is complete
- [ ] Tests are passing
- [ ] Linking info is saved
- [ ] Issues are fixed automatically

---

## MULTI-PLATFORM OUTPUT

### OpenCode
- Agent: `~/.config/opencode/agents/hcs-data-linker-agent.md`
- Skill: `~/.config/opencode/skills/hcs-data-linker/SKILL.md`

### Cursor
- Rules: `.cursor/rules/hcs-data-linker.mdc`
- Config: `.cursorrules`

### Claude Code
- Rules: `.claude/rules/hcs-data-linker.md`
- Config: `CLAUDE.md`

### Codex
- Rules: `.codex/rules/hcs-data-linker.md`
- Config: `AGENTS.md`

### Kimi Code
- Rules: `.kimi/rules/hcs-data-linker.md`
- Config: `.kimirc`

### VS Code
- Rules: `.vscode/rules/hcs-data-linker.md`
- Config: `.vscode/settings.json`

### Windsurf
- Rules: `.windsurf/rules/hcs-data-linker.md`
- Config: `.windsurfrules`

### Aider
- Rules: `.aider/rules/hcs-data-linker.md`
- Config: `.aider.conf`

---

*Generated by HCS Skill Builder System*
*Version: 1.0.0*
*Status: ACTIVE*

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

