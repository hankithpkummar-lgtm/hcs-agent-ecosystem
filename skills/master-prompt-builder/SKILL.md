---
name: HCS Master Prompt Builder
description: HCS Lightweight auto-executing prompt builder that converts any natural language request into optimized, structured prompts and sends them directly to the coding model. No approval gate for simple requests. Works alongside universal-master-dev-agent-v3 for complex projects.
license: MIT
compatibility: opencode
categories: [prompt-engineering, automation, coding, ai, opencode]
metadata:
  author: HCS
  version: "1.0.0"
  last_updated: "2026-07-07"
  scope: universal
  mode: auto-execute
---

# ═══════════════════════════════════════════════════════════════════════
# MASTER PROMPT BUILDER v1.0.0
# Lightweight Auto-Executing Prompt Engine
# ═══════════════════════════════════════════════════════════════════════

> **"Type any request. Get an optimized prompt. Start building. No approval gates. No delays."**

---

## TRIGGER

**Primary Trigger:** `prompt-builder`

**Aliases:**
- `build-prompt`
- `convert-prompt`
- `optimize-prompt`
- `master-prompt`
- `mpb`
- `auto-prompt`
- `prompt-engine`

---

## TABLE OF CONTENTS

1. [How It Works](#1-how-it-works)
2. [Complexity Detection](#2-complexity-detection)
3. [Prompt Generation Pipeline](#3-prompt-generation-pipeline)
4. [Prompt Templates](#4-prompt-templates)
5. [Model Selection](#5-model-selection)
6. [Auto-Execution Rules](#6-auto-execution-rules)
7. [Examples](#7-examples)

---

## 1. How It Works

### The 5-Step Pipeline

```
USER REQUEST (any natural language)
        ↓
┌───────────────────────────────────┐
│ STEP 1: INTENT ANALYSIS           │
│ - Detect what user wants          │
│ - Identify domain                 │
│ - Classify request type           │
└───────────────────────────────────┘
        ↓
┌───────────────────────────────────┐
│ STEP 2: COMPLEXITY CHECK          │
│ - Simple → Auto-execute           │
│ - Medium → Quick questions        │
│ - Complex → Route to master-dev   │
└───────────────────────────────────┘
        ↓
┌───────────────────────────────────┐
│ STEP 3: PROMPT GENERATION         │
│ - Expand requirements             │
│ - Add constraints                 │
│ - Structure output                │
└───────────────────────────────────┘
        ↓
┌───────────────────────────────────┐
│ STEP 4: MODEL SELECTION           │
│ - Choose best model for task      │
│ - Optimize for speed/cost         │
└───────────────────────────────────┘
        ↓
┌───────────────────────────────────┐
│ STEP 5: AUTO-EXECUTE              │
│ - Send prompt to coder            │
│ - Start building immediately      │
└───────────────────────────────────┘
        ↓
BUILDING BEGINS
```

---

## 2. Complexity Detection

### Automatic Classification

| Level | Indicators | Action |
|-------|-----------|--------|
| **SIMPLE** | Single file, UI tweak, small fix, content change | Auto-execute immediately |
| **MEDIUM** | New component, API endpoint, feature with 2-3 files | Auto-execute with expanded prompt |
| **COMPLEX** | Full feature, multiple modules, database, auth | Auto-execute with detailed prompt |
| **ARCHITECTURAL** | New system, major refactor, multi-service | Route to `universal-master-dev-agent-v3` |

### Complexity Keywords

**SIMPLE indicators:**
- "add a button", "change color", "fix typo", "update text"
- "make it blue", "center this", "add padding"
- "rename", "move", "delete", "toggle"

**MEDIUM indicators:**
- "create a component", "add a form", "build a page"
- "new API endpoint", "add authentication"
- "implement search", "add filtering"

**COMPLEX indicators:**
- "build a dashboard", "create admin panel"
- "full e-commerce", "multi-user system"
- "real-time", "webhook", "integration"

**ARCHITECTURAL indicators:**
- "new project from scratch", "complete rewrite"
- "microservices", "distributed system"
- "migration", "platform"

---

## 3. Prompt Generation Pipeline

### Step 1: Intent Analysis

```
INPUT: "Build a calculator app with dark mode"

ANALYSIS:
- Intent: Build new application
- Domain: General / Utility
- Type: New project
- Tech stack: Not specified → infer from context
- Complexity: MEDIUM
```

### Step 2: Requirement Expansion

```
EXPLICIT REQUIREMENTS:
1. Calculator app
2. Dark mode

INFERRED REQUIREMENTS:
3. Basic arithmetic operations (+, -, ×, ÷)
4. Responsive design (mobile + desktop)
5. Keyboard input support
6. Display history
7. Error handling (division by zero)
8. Accessible (WCAG)
9. Fast loading
10. Clean UI
```

### Step 3: Constraint Generation

```
CONSTRAINTS:
- Production quality (no placeholders)
- Error handling for all operations
- Responsive (works on mobile)
- Accessible (keyboard navigation)
- Performant (< 100ms response)
- Clean, maintainable code
```

### Step 4: Prompt Assembly

```
ASSEMBLED PROMPT:
[Role] + [Task] + [Requirements] + [Constraints] + [Examples] + [Success Criteria]
```

---

## 4. Prompt Templates

### Template A: Simple Request

```markdown
## TASK
[What needs to be built]

## REQUIREMENTS
1. [Requirement 1]
2. [Requirement 2]

## CONSTRAINTS
- [Constraint 1]
- [Constraint 2]

## OUTPUT
[Expected files/component structure]
```

### Template B: Medium Request

```markdown
## ROLE
You are a [specific role] expert.

## TASK
[What needs to be built]

## CONTEXT
- Project: [Project name/type]
- Tech Stack: [Technologies]
- Existing: [What already exists]

## REQUIREMENTS
1. [Requirement 1 with details]
2. [Requirement 2 with details]
3. [Requirement 3 with details]

## TECHNICAL SPECIFICATION
### Files to Create
- `path/file1.ts` - [purpose]
- `path/file2.ts` - [purpose]

### Data Models
[If applicable]

### API Endpoints
[If applicable]

## CONSTRAINTS
- Production quality
- Error handling
- Input validation
- Responsive design
- Accessibility

## SUCCESS CRITERIA
- [ ] [Criteria 1]
- [ ] [Criteria 2]
```

### Template C: Complex Request

```markdown
# MASTER PROMPT: [Feature Name]

## 1. CONTEXT
- **Project:** [Name and description]
- **Domain:** [Domain]
- **Request Type:** [new_feature | modification | bugfix]
- **Priority:** [High | Medium | Low]

## 2. OBJECTIVE
[One clear sentence describing what to build]

## 3. TECHNICAL SPECIFICATION

### 3.1 Architecture
[Component structure, data flow]

### 3.2 Files to Create
| File Path | Purpose |
|-----------|---------|
| `path/file1.ts` | [purpose] |
| `path/file2.ts` | [purpose] |

### 3.3 Files to Modify
| File Path | Change |
|-----------|--------|
| `path/existing.ts` | [what changes] |

### 3.4 Data Models
```typescript
interface DataType {
  field: type;
}
```

### 3.5 Business Logic
```
ALGORITHM: [Name]
INPUT: [inputs]
OUTPUT: [outputs]
STEPS:
  1. [Step 1]
  2. [Step 2]
EDGE CASES:
  - [Case]: [Handling]
```

## 4. REQUIREMENTS
1. [Detailed requirement 1]
2. [Detailed requirement 2]
3. [Detailed requirement 3]

## 5. CONSTRAINTS
- Production quality (no placeholders, no TODOs)
- Error handling with user-friendly messages
- Input validation on all endpoints
- Responsive design (mobile-first)
- WCAG 2.1 AA accessibility
- Performance: < 200ms response time
- Clean, maintainable code structure

## 6. ACCEPTANCE CRITERIA
- [ ] [Criteria 1]
- [ ] [Criteria 2]
- [ ] [Criteria 3]

## 7. OUT OF SCOPE
- [What NOT to build]
```

---

## 5. Model Selection

### Automatic Routing

| Task Type | Best Model | Why |
|-----------|-----------|-----|
| **UI/Frontend** | Claude, GPT-4 | Strong at component design |
| **Backend/API** | Claude, GPT-4 | Good at architecture |
| **Code Generation** | Codex, Claude | Specialized for code |
| **Simple Fix** | GPT-3.5, Claude Haiku | Fast, cost-effective |
| **Architecture** | GPT-4, Claude | Best reasoning |
| **Documentation** | Claude, GPT-4 | Strong writing |

### Selection Logic

```
IF task == "simple fix" OR "ui tweak":
    USE fast_model (GPT-3.5 / Claude Haiku)
ELIF task == "new feature" OR "component":
    USE standard_model (Claude / GPT-4)
ELIF task == "architecture" OR "complex system":
    USE reasoning_model (GPT-4 / Claude Opus)
ELSE:
    USE standard_model
```

---

## 6. Auto-Execution Rules

### Rule 1: No Approval for Simple/Medium

```
IF complexity == SIMPLE OR MEDIUM:
    GENERATE prompt
    SEND to model immediately
    START building
```

### Rule 2: Quick Confirm for Complex

```
IF complexity == COMPLEX:
    GENERATE prompt
    SHOW to user for quick review
    IF user says "go" OR "yes" OR "build":
        SEND to model
        START building
```

### Rule 3: Route for Architectural

```
IF complexity == ARCHITECTURAL:
    INFORM user
    ROUTE to universal-master-dev-agent-v3
    LET full pipeline handle it
```

### Rule 4: Never Block

```
NEVER say "I need more information" for simple requests
NEVER ask unnecessary questions
NEVER delay when you can infer
ALWAYS prefer action over discussion
```

### Rule 5: Smart Inference

```
IF tech_stack not specified:
    LOOK at existing project files
    INFER from package.json, framework, etc.
    USE inferred stack

IF design not specified:
    USE clean, modern defaults
    FOLLOW existing project patterns
```

---

## 7. Examples

### Example 1: Simple Request

**User:**
```
prompt-builder: Add a loading spinner to the dashboard
```

**Auto-Generated Prompt:**
```markdown
## TASK
Add a loading spinner component to the dashboard.

## REQUIREMENTS
1. Create a reusable LoadingSpinner component
2. Show spinner during data fetching
3. Smooth fade-in/fade-out animation
4. Centered on page/section
5. Accessible (aria-label, role="status")

## CONSTRAINTS
- Use existing project styling (Tailwind/CSS modules)
- Follow existing component patterns
- No external dependencies
- Responsive sizing

## OUTPUT
- `src/components/LoadingSpinner.tsx` - Spinner component
- Update `src/pages/Dashboard.tsx` - Add spinner during loading
```

**Action:** Sending to coder now...

---

### Example 2: Medium Request

**User:**
```
build-prompt: Create a user profile page with edit functionality
```

**Auto-Generated Prompt:**
```markdown
## ROLE
You are a React/Next.js developer specializing in user interfaces.

## TASK
Build a user profile page with view and edit modes.

## CONTEXT
- Project: Web application
- Tech Stack: Next.js, React, TypeScript, Tailwind CSS
- Existing: Auth system, user data model

## REQUIREMENTS
1. Profile page showing user info (name, email, avatar, bio)
2. Edit mode with form validation
3. Save/cancel buttons
4. Success/error notifications
5. Responsive design (mobile-first)
6. Loading states

## FILES TO CREATE
- `src/components/profile/ProfileCard.tsx` - Display user info
- `src/components/profile/ProfileForm.tsx` - Edit form
- `src/components/profile/ProfileAvatar.tsx` - Avatar with upload
- `src/app/profile/page.tsx` - Profile page

## DATA MODEL
```typescript
interface UserProfile {
  id: string;
  name: string;
  email: string;
  avatar?: string;
  bio?: string;
  updatedAt: Date;
}
```

## CONSTRAINTS
- Form validation (required fields, email format)
- Optimistic UI updates
- Error handling with user feedback
- Accessible (labels, focus management)
- Loading states for async operations

## SUCCESS CRITERIA
- [ ] Profile displays correctly
- [ ] Edit mode toggles smoothly
- [ ] Form validation works
- [ ] Save persists changes
- [ ] Responsive on all devices
```

**Action:** Sending to coder now...

---

### Example 3: Complex Request

**User:**
```
master-prompt: Build an admin dashboard with analytics, user management, and real-time notifications
```

**Auto-Generated Prompt:**
```markdown
# MASTER PROMPT: Admin Dashboard

## 1. CONTEXT
- **Project:** Admin Dashboard
- **Domain:** Web Application
- **Request Type:** New Feature
- **Priority:** High

## 2. OBJECTIVE
Build a comprehensive admin dashboard with analytics charts, user management table, and real-time notification system.

## 3. TECHNICAL SPECIFICATION

### 3.1 Architecture
```
AdminDashboard
├── AnalyticsPanel (charts, metrics)
├── UserManagement (table, CRUD)
├── NotificationSystem (real-time feed)
└── Layout (sidebar, header, content)
```

### 3.2 Files to Create
| File Path | Purpose |
|-----------|---------|
| `src/app/admin/page.tsx` | Dashboard layout |
| `src/components/admin/AnalyticsPanel.tsx` | Charts and metrics |
| `src/components/admin/UserTable.tsx` | User management table |
| `src/components/admin/NotificationFeed.tsx` | Real-time notifications |
| `src/hooks/useAnalytics.ts` | Analytics data hook |
| `src/hooks/useNotifications.ts` | WebSocket notifications |
| `src/lib/api/admin.ts` | Admin API functions |

### 3.3 API Endpoints
```
GET    /api/admin/analytics     - Dashboard metrics
GET    /api/admin/users         - User list with pagination
PUT    /api/admin/users/:id     - Update user role
DELETE /api/admin/users/:id     - Deactivate user
GET    /api/admin/notifications - Recent notifications
WS     /ws/notifications        - Real-time notification stream
```

## 4. REQUIREMENTS
1. **Analytics Panel**
   - User growth chart (line)
   - Revenue chart (bar)
   - Activity feed (list)
   - Key metrics cards

2. **User Management**
   - Searchable table
   - Sort by columns
   - Pagination
   - Role editing (admin/user)
   - Deactivate users

3. **Notifications**
   - Real-time WebSocket feed
   - Mark as read
   - Notification categories
   - Badge count

4. **Layout**
   - Collapsible sidebar
   - User menu
   - Breadcrumbs
   - Responsive (mobile sidebar → hamburger)

## 5. CONSTRAINTS
- Production quality (no placeholders)
- Error handling on all API calls
- Loading skeletons for all data
- Responsive design
- Keyboard navigation
- Role-based access control
- Audit logging for admin actions

## 6. ACCEPTANCE CRITERIA
- [ ] Dashboard loads in < 2s
- [ ] Charts render with real data
- [ ] User table pagination works
- [ ] Role changes persist
- [ ] Notifications appear in real-time
- [ ] Mobile responsive
- [ ] Accessible (WCAG AA)

## 7. OUT OF SCOPE
- User registration (exists)
- Password reset (exists)
- Email notifications (future)
```

**Action:** This is complex. Routing to universal-master-dev-agent-v3 for full pipeline handling.

---

## QUICK REFERENCE

### Activation Commands

| Command | Action |
|---------|--------|
| `prompt-builder [request]` | Convert request to prompt and build |
| `build-prompt [request]` | Same as above |
| `mpb [request]` | Shorthand |
| `auto-prompt [request]` | Same as above |

### What Happens

1. You type a request
2. Skill analyzes intent and complexity
3. Generates optimized, structured prompt
4. Sends prompt to appropriate coding model
5. Building starts immediately

### No More:
- ❌ Manual prompt writing
- ❌ Copy-pasting prompts
- ❌ Figuring out which model to use
- ❌ Waiting for approval on simple tasks
- ❌ Incomplete prompts missing context

---

## SELF-LEARNING SYSTEM

### Error Learning

- Track all errors encountered
- Analyze root causes
- Generate prevention rules
- Add test cases for errors
- Update knowledge base

### Usage Learning

- Monitor feature usage
- Identify popular features
- Detect unused features
- Optimize based on usage
- Add requested features

### Feedback Learning

- Collect user feedback
- Analyze feedback patterns
- Prioritize improvements
- Implement changes
- Verify improvements

### Knowledge Base

- Store best practices
- Store common solutions
- Store optimization techniques
- Store security patterns
- Store performance tips

### Cross-Project Updates

- Track improvements across projects
- Identify reusable patterns
- Propagate improvements globally
- Maintain consistency
- Share knowledge between skills

### Version Tracking

- Track all changes
- Document improvements
- Maintain changelog
- Enable rollback
- Support multiple versions

### Best Practice Updates

- Monitor industry trends
- Research new techniques
- Update skill accordingly
- Maintain compatibility
- Document changes

### Performance Monitoring

- Track execution time
- Monitor resource usage
- Identify bottlenecks
- Optimize performance
- Report improvements

---

**Remember:** This skill is designed for SPEED. Type your request, get building. For complex architectural projects, it will automatically route to the full 15-agent pipeline.
