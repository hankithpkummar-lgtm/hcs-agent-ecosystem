# HCS Local Host Testing Skill

> **HCS SKILL** — Created by HCS Skill Builder System
> **Version:** 4.0.0
> **Last Updated:** 2026-07-07
> **Status:** ACTIVE
> **Category:** Development / Testing / Local Server

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

This skill provides **local development server and preview link generation** by:
1. **Auto-starting** local development server
2. **Generating** preview links automatically
3. **Visualizing** all recent changes
4. **Auto-testing** on file changes
5. **Validating** before commit
6. **Blocking** deployment until explicitly requested

---

## COMPULSORY LOCALHOST-FIRST RULES

**THIS IS THE MOST IMPORTANT RULE IN THIS SKILL.**

### Core Principle

**EVERYTHING happens on localhost FIRST. Deployment is the FINAL step and requires EXPLICIT user permission.**

### Rules

| Rule | Description | Enforcement |
|------|-------------|-------------|
| **Rule 1** | All testing happens on localhost | COMPULSORY |
| **Rule 2** | All fixing happens on localhost | COMPULSORY |
| **Rule 3** | All improvements happen on localhost | COMPULSORY |
| **Rule 4** | All link testing happens on localhost | COMPULSORY |
| **Rule 5** | All feature testing happens on localhost | COMPULSORY |
| **Rule 6** | Deployment requires explicit user command | COMPULSORY |
| **Rule 7** | Deployer agent waits for deployment command | COMPULSORY |
| **Rule 8** | Localhost is preferred over deployment | COMPULSORY |

### Deployment Gate System

```
WORKFLOW START
    |
    v
LOCALHOST PHASE (DEFAULT)
    |-- All testing on localhost
    |-- All fixing on localhost
    |-- All improvements on localhost
    |-- All link checking on localhost
    |
    v
ASK FOR DEPLOYMENT
    |-- "Testing complete. Deploy to production?"
    |-- User must explicitly say YES
    |
    v
IF USER SAYS YES
    |
    v
DEPLOYMENT PHASE
    |-- Deploy to production
    |-- Verify deployment
    |-- Provide live URL
    |
    v
IF USER SAYS NO
    |
    v
CONTINUE LOCALHOST
    |-- Keep testing locally
    |-- Make more improvements
    |-- Ask again later
```

### Why Localhost First?

| Reason | Explanation |
|--------|-------------|
| **Faster** | No deployment wait time |
| **Cheaper** | No hosting costs during development |
| **Safer** | No broken production site |
| **Easier** | No rollback needed |
| **Better** | Test everything before going live |

### Deployment Requirements

Before deployment is allowed, ALL of these must be complete on localhost:

- [ ] All links tested and working
- [ ] All forms tested and working
- [ ] All features tested and working
- [ ] Responsive design verified
- [ ] Performance acceptable
- [ ] No critical errors
- [ ] Quality score > 80
- [ ] User explicitly requests deployment

### Deployment Command

**Deployment ONLY starts when user explicitly says:**

| User Says | Action |
|-----------|--------|
| "deploy" | Start deployment |
| "deploy to production" | Start deployment |
| "deploy to vercel" | Start deployment to Vercel |
| "deploy to netlify" | Start deployment to Netlify |
| "ship it" | Start deployment |
| "go live" | Start deployment |

**Deployment does NOT start for:**

| User Says | Action |
|-----------|--------|
| "test" | Localhost testing |
| "check" | Localhost testing |
| "fix" | Localhost fixing |
| "improve" | Localhost improvement |
| "preview" | Localhost preview |

### Deployment Ask Format

```markdown
## LOCALHOST TESTING COMPLETE ✅

### All Tests Passed
- ✅ All links working
- ✅ All forms working
- ✅ All features working
- ✅ Responsive design verified
- ✅ Performance acceptable
- ✅ No critical errors

### Quality Score: 90/100

### Ready to Deploy?

**Would you like to deploy to production?**

Type "yes" or "deploy" to deploy now.
Type "no" or "not yet" to continue testing locally.

**Note:** Deployment will take time to host. Localhost is faster for testing.
```

---

## LOCALHOST-FIRST PIPELINE

```
CODE CHANGES MADE
    |
    v
LOCALHOST PHASE (AUTOMATIC)
    |
    ├─── START LOCAL SERVER
    |    |-- Auto-start development server
    |    |-- Generate localhost URL
    |    |-- Enable hot reload
    |
    ├─── TEST ON LOCALHOST
    |    |-- Test all links on localhost
    |    |-- Test all forms on localhost
    |    |-- Test all features on localhost
    |    |-- Test responsiveness on localhost
    |
    ├─── FIX ON LOCALHOST
    |    |-- Fix all issues on localhost
    |    |-- Verify fixes on localhost
    |    |-- Re-test on localhost
    |
    ├─── IMPROVE ON LOCALHOST
    |    |-- Make improvements on localhost
    |    |-- Test improvements on localhost
    |    |-- Verify improvements on localhost
    |
    v
LOCALHOST TESTING COMPLETE
    |
    v
ASK FOR DEPLOYMENT (ALWAYS)
    |
    ├─── USER SAYS "YES" / "DEPLOY" / "SHIP IT"
    |    |
    |    v
    |    DEPLOYMENT PHASE
    |    |-- Deploy to production
    |    |-- Verify deployment
    |    |-- Provide live URL
    |
    └─── USER SAYS "NO" / "NOT YET" / "MORE TESTING"
         |
         v
         CONTINUE LOCALHOST
         |-- Keep testing locally
         |-- Make more improvements
         |-- Ask again later
```

---

## DEPLOYMENT GATE RULES

### Permanent Rule

**THIS RULE IS PERMANENT AND CANNOT BE CHANGED.**

| Rule | Description |
|------|-------------|
| **Localhost First** | All work happens on localhost |
| **Deployment Last** | Deployment is the final step |
| **Explicit Permission** | User must explicitly request deployment |
| **Deployer Waits** | Deployer agent waits for deployment command |
| **Ask Every Time** | Always ask if user wants to deploy |

### Deployment Block Rules

| Condition | Action |
|-----------|--------|
| **No explicit deploy command** | ❌ BLOCK deployment |
| **Tests failing on localhost** | ❌ BLOCK deployment |
| **Quality score < 80** | ❌ BLOCK deployment |
| **Critical issues found** | ❌ BLOCK deployment |
| **User says "no"** | ❌ BLOCK deployment |
| **All pass + user says "yes"** | ✅ ALLOW deployment |

---

## SKILL TRIGGERS

| Trigger Phrase | Action |
|----------------|--------|
| "local test" | Start local testing |
| "localhost" | Start local server |
| "preview link" | Generate preview link |
| "show changes" | Visualize recent changes |
| "test before commit" | Pre-commit validation |
| "before deploy" | Pre-deployment check |
| "start server" | Start local server |
| "local preview" | Generate local preview |

---

## AUTO-ENABLE SYSTEM

### What is Auto-Enable?

**Auto-Enable means this skill automatically activates when:**

| Trigger Event | Auto-Enable Action |
|---------------|-------------------|
| **Project Start** | Auto-start local server |
| **File Change** | Auto-reload preview |
| **Git Commit** | Auto-test before commit |
| **Pre-Deployment** | Auto-generate preview link |
| **User Request** | Auto-generate preview link |

### Auto-Enable Configuration

```json
{
  "autoEnable": {
    "enabled": true,
    "triggers": {
      "projectStart": true,
      "fileChange": true,
      "gitCommit": true,
      "preDeployment": true,
      "userRequest": true
    },
    "settings": {
      "autoStartServer": true,
      "autoOpenBrowser": true,
      "autoGenerateLink": true,
      "autoTestOnSave": true,
      "autoScreenshot": true
    }
  }
}
```

### Auto-Enable Triggers

| Trigger | Action | Compulsory |
|---------|--------|------------|
| **Project Start** | Start local server | YES |
| **File Change** | Reload preview | YES |
| **Git Pre-Commit** | Run tests | YES |
| **Pre-Deployment** | Generate preview | YES |
| **User Request** | Generate preview | YES |

---

## CAPABILITIES

### 1. Local Server Management

**What It Does:**
- Detects project type automatically
- Starts appropriate development server
- Manages server lifecycle
- Provides server status

**Output:**
```markdown
## SERVER STATUS

### Local Server
- **URL:** http://localhost:3000
- **Status:** ✅ Running
- **Framework:** Next.js
- **Auto-Reload:** Enabled

### Network Server
- **URL:** http://192.168.1.100:3000
- **Status:** ✅ Running
- **Access:** Same network
```

### 2. Preview Link Generation

**What It Does:**
- Generates local preview URL
- Creates shareable preview link
- Provides network access URL
- Generates QR code

**Output:**
```markdown
## PREVIEW LINKS

### Local Preview
- **URL:** http://localhost:3000
- **Access:** Local machine

### Shareable Preview
- **URL:** https://preview-abc123.localtest.me
- **Expires:** 24 hours
- **Password:** None

### Network Preview
- **URL:** http://192.168.1.100:3000
- **Access:** Same network

### QR Code
[QR Code Image]
```

### 3. Change Visualization

**What It Does:**
- Detects all changed files
- Generates before/after screenshots
- Creates visual diff
- Highlights changed areas

**Output:**
```markdown
## CHANGE VISUALIZATION

### Files Changed
| File | Changes | Impact |
|------|---------|--------|
| src/components/Header.jsx | +15 -5 | HIGH |
| src/styles/main.css | +20 -10 | MEDIUM |
| src/pages/Home.jsx | +5 -2 | LOW |

### Visual Diff
![Before](before.png)
![After](after.png)
![Diff](diff.png)
```

### 4. Auto-Testing

**What It Does:**
- Runs unit tests automatically
- Runs integration tests automatically
- Runs visual tests automatically
- Runs performance tests automatically

**Output:**
```markdown
## AUTO-TEST RESULTS

| Test Type | Status | Duration |
|-----------|--------|----------|
| Unit Tests | ✅ PASS | 2.3s |
| Integration Tests | ✅ PASS | 5.1s |
| Visual Tests | ✅ PASS | 3.2s |
| Performance Tests | ✅ PASS | 1.8s |
```

### 5. Pre-Commit Validation

**What It Does:**
- Validates code quality
- Runs all tests
- Checks documentation
- Verifies security

**Output:**
```markdown
## PRE-COMMIT CHECKLIST

### Code Quality
- [ ] No linting errors
- [ ] No formatting issues
- [ ] No console warnings

### Testing
- [ ] All unit tests pass
- [ ] All integration tests pass
- [ ] No visual regressions

### Commit Readiness
**✅ READY TO COMMIT**
```

### 6. Pre-Deployment Check

**What It Does:**
- Compulsory before deployment
- Blocks deployment if issues found
- Requires quality score > 80
- Provides deployment report

**Output:**
```markdown
## PRE-DEPLOYMENT CHECK

### Overall Status
**✅ DEPLOYMENT ALLOWED**

### Check Results
| Check | Status | Notes |
|-------|--------|-------|
| Tests | ✅ PASS | All passing |
| Quality | ✅ PASS | Score: 90/100 |
| Security | ✅ PASS | No issues |

### Deploy Command
```bash
npm run build && npm run deploy
```
```

---

## WORKFLOW

### Step 1: Receive Request

```
User: "Show me local preview"
    |
    v
HCS Local Host Testing Agent
    |-- Parse request
    |-- Identify action
    |-- Determine scope
```

### Step 2: Start Local Server

```
SERVER STARTUP PHASE
    |
    v
Detect Project Type
    |-- Next.js, React, Vue, etc.
    |
    v
Check Dependencies
    |-- node_modules exists?
    |-- Need to install?
    |
    v
Start Server
    |-- npm start / npm run dev
    |-- Wait for ready
    |-- Capture URL
    |
    v
Server Running
    |-- http://localhost:3000
    |-- Auto-reload enabled
```

### Step 3: Generate Preview

```
PREVIEW GENERATION PHASE
    |
    v
Generate Local URL
    |-- http://localhost:3000
    |
    v
Generate Shareable URL
    |-- https://preview-abc123.localtest.me
    |-- Expires in 24 hours
    |
    v
Generate Network URL
    |-- http://192.168.1.100:3000
    |-- Same network access
    |
    v
Generate QR Code
    |-- Scannable QR code
    |-- Links to preview
```

### Step 4: Visualize Changes

```
CHANGE VISUALIZATION PHASE
    |
    v
Detect Changes
    |-- git diff
    |-- Changed files
    |
    v
Generate Screenshots
    |-- Before screenshot
    |-- After screenshot
    |-- Visual diff
    |
    v
Highlight Changes
    |-- Changed areas
    |-- Impact analysis
    |
    v
Display Visualization
    |-- Before/After
    |-- Diff view
    |-- Change summary
```

### Step 5: Auto-Test

```
AUTO-TEST PHASE
    |
    v
Run Unit Tests
    |-- Test all components
    |-- Capture results
    |
    v
Run Integration Tests
    |-- Test all APIs
    |-- Capture results
    |
    v
Run Visual Tests
    |-- Compare screenshots
    |-- Capture results
    |
    v
Run Performance Tests
    |-- Measure load time
    |-- Capture results
    |
    v
Generate Test Report
    |-- All results
    |-- Pass/fail status
```

### Step 6: Validate

```
VALIDATION PHASE
    |
    v
Validate Code Quality
    |-- Linting
    |-- Formatting
    |-- Type checking
    |
    v
Validate Tests
    |-- All tests pass
    |-- No regressions
    |
    v
Validate Documentation
    |-- README updated
    |-- CHANGELOG updated
    |
    v
Validate Security
    |-- No secrets exposed
    |-- No vulnerabilities
```

### Step 7: Generate Report

```
REPORT GENERATION PHASE
    |
    v
Generate Test Report
    |-- Test results
    |-- Quality score
    |
    v
Generate Change Report
    |-- Files changed
    |-- Impact analysis
    |
    v
Generate Commit Report
    |-- Commit readiness
    |-- Commit command
    |
    v
Deliver to User
    |-- Complete report
    |-- Preview links
    |-- Recommendations
```

---

## COMPULSORY PRE-DEPLOYMENT TESTING

### Why is Local Testing Compulsory?

**Local testing is COMPULSORY before deployment because:**

1. **Prevents Broken Deployments** — Catch issues before they go live
2. **Ensures Quality** — Verify all features work
3. **Validates Changes** — Confirm all changes are correct
4. **Blocks Bad Code** — Prevent problematic code from deploying
5. **Provides Confidence** — Know everything works before deploy

### Pre-Deployment Workflow

```
DEPLOYMENT REQUESTED
    |
    v
⚠️ COMPULSORY: LOCAL TESTING REQUIRED
    |
    v
START LOCAL SERVER
    |-- Start development server
    |-- Wait for ready
    |-- Generate preview link
    |
    v
GENERATE PREVIEW
    |-- Create preview URL
    |-- Show all changes
    |-- Visualize differences
    |
    v
RUN ALL TESTS
    |-- Unit tests
    |-- Integration tests
    |-- Visual tests
    |-- Performance tests
    |
    v
VALIDATE ALL FEATURES
    |-- Test all links
    |-- Test all forms
    |-- Test all features
    |-- Test responsiveness
    |
    v
GENERATE DEPLOYMENT REPORT
    |-- All test results
    |-- Change summary
    |-- Quality score
    |
    v
✅ DEPLOYMENT ALLOWED
    |-- Only if all tests pass
    |-- Only if quality score > 80
    |-- Only if no critical issues
```

### Deployment Block Rules

| Condition | Action |
|-----------|--------|
| **Tests Failing** | ❌ BLOCK deployment |
| **Quality Score < 80** | ❌ BLOCK deployment |
| **Critical Issues** | ❌ BLOCK deployment |
| **Security Issues** | ❌ BLOCK deployment |
| **All Pass** | ✅ ALLOW deployment |

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

### Local Testing Quality Checklist

- [ ] **Auto-Enable** — Automatically activates on project start
- [ ] **Auto-Start Server** — Server starts automatically
- [ ] **Auto-Generate Link** — Preview link created automatically
- [ ] **Auto-Test on Save** — Tests run on every file save
- [ ] **Auto-Screenshot** — Screenshots captured automatically
- [ ] **Change Visualization** — All changes shown visually
- [ ] **Pre-Commit Validation** — Validates before commit
- [ ] **Pre-Deployment Check** — Compulsory before deployment

### Preview Link Quality

- [ ] **Fast Generation** — Link created in < 5 seconds
- [ ] **Shareable** — Can be shared with team
- [ ] **Time-Limited** — Expires after 24 hours
- [ ] **Device Responsive** — Works on all devices
- [ ] **Real-Time Updates** — Live reload enabled

---

## HCS PREFIX RULE

**PERMANENT AND MANDATORY**

This rule is PERMANENT and applies to ALL skills created by this agent:

1. **ALL Skills MUST Have HCS Prefix**
   - Every skill created must start with "HCS"
   - No exceptions allowed
   - This is permanent and cannot be changed

2. **Skill Names**
   - ✅ `hcs-local-host-testing`
   - ✅ `hcs-preview-server`
   - ❌ `local-host-testing`
   - ❌ `preview-server`

3. **Agent Names**
   - ✅ `hcs-local-host-testing-agent.md`
   - ❌ `local-host-testing-agent.md`
   - ❌ `local-server.md`

4. **Enforcement**
   - Before creating any skill, check prefix
   - If no HCS prefix, add it
   - Never create skills without HCS prefix
   - This rule is permanent and cannot be changed

---

## SUCCESS METRICS

The HCS Local Host Testing Skill is successful when:

- [ ] Local server starts automatically
- [ ] Preview link is generated
- [ ] All changes are visualized
- [ ] Auto-testing works on save
- [ ] Pre-commit validation works
- [ ] Pre-deployment check is compulsory
- [ ] Quality score is calculated
- [ ] Commit readiness is determined

---

## EXAMPLE USAGE

### Example 1: Local Preview

**User Request:**
"Show me local preview"

**HCS Local Host Testing Response:**

```markdown
## LOCAL PREVIEW GENERATED

### Server Status
- **URL:** http://localhost:3000
- **Status:** ✅ Running
- **Framework:** Next.js
- **Auto-Reload:** Enabled

### Preview Links
- **Local:** http://localhost:3000
- **Network:** http://192.168.1.100:3000
- **Shareable:** https://preview-abc123.localtest.me

### Changes Detected
| File | Changes | Impact |
|------|---------|--------|
| src/components/Header.jsx | +15 -5 | HIGH |
| src/styles/main.css | +20 -10 | MEDIUM |

### Test Results
| Test Type | Status | Duration |
|-----------|--------|----------|
| Unit Tests | ✅ PASS | 2.3s |
| Integration Tests | ✅ PASS | 5.1s |

### Commit Readiness
**✅ READY TO COMMIT**
```

### Example 2: Test Before Commit

**User Request:**
"Test before commit"

**HCS Local Host Testing Response:**

```markdown
## PRE-COMMIT TEST RESULTS

### Test Results
| Test Type | Status | Duration |
|-----------|--------|----------|
| Unit Tests | ✅ PASS | 2.3s |
| Integration Tests | ✅ PASS | 5.1s |
| Visual Tests | ✅ PASS | 3.2s |
| Performance Tests | ✅ PASS | 1.8s |

### Code Quality
- **Linting:** ✅ No errors
- **Formatting:** ✅ Correct
- **Type Checking:** ✅ No errors

### Documentation
- **README:** ✅ Updated
- **CHANGELOG:** ✅ Updated

### Commit Readiness
**✅ READY TO COMMIT**

### Commit Command
```bash
git add .
git commit -m "feat: update header component"
```
```

---

## MULTI-PLATFORM OUTPUT

### OpenCode
- Agent: `~/.config/opencode/agents/hcs-local-host-testing-agent.md`
- Skill: `~/.config/opencode/skills/hcs-local-host-testing/SKILL.md`

### Cursor
- Rules: `.cursor/rules/hcs-local-host-testing.mdc`
- Config: `.cursorrules`

### Claude Code
- Rules: `.claude/rules/hcs-local-host-testing.md`
- Config: `CLAUDE.md`

### Codex
- Rules: `.codex/rules/hcs-local-host-testing.md`
- Config: `AGENTS.md`

### Kimi Code
- Rules: `.kimi/rules/hcs-local-host-testing.md`
- Config: `.kimirc`

### VS Code
- Rules: `.vscode/rules/hcs-local-host-testing.md`
- Config: `.vscode/settings.json`

### Windsurf
- Rules: `.windsurf/rules/hcs-local-host-testing.md`
- Config: `.windsurfrules`

### Aider
- Rules: `.aider/rules/hcs-local-host-testing.md`
- Config: `.aider.conf`

---

*Generated by HCS Skill Builder System*
*Version: 3.0.0*
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

