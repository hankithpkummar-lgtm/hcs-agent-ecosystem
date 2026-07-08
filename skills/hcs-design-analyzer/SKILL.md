---
name: "HCS Design Analyzer"
description: "HCS Design Analyzer v1.0 — Autonomous Design-to-Code Analysis Engine. Analyzes design files (Figma, Sketch, images) and converts to code specifications."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Design Analyzer

## Purpose
Analyze design files and convert them to precise, implementable code specifications.

## Design Analysis Pipeline

```
INPUT: Design File (Image, Figma, Sketch, etc.)
    |
    v
STEP 1: DESIGN DETECTION
    |-- Identify design tool
    |-- Determine analysis method
    |
    v
STEP 2: LAYOUT ANALYSIS
    |-- Analyze grid system
    |-- Identify columns/rows
    |-- Determine spacing
    |-- Measure dimensions
    |
    v
STEP 3: COMPONENT IDENTIFICATION
    |-- Identify components
    |-- Map component hierarchy
    |-- Determine component types
    |
    v
STEP 4: STYLE EXTRACTION
    |-- Extract colors
    |-- Extract typography
    |-- Extract spacing
    |-- Extract borders
    |-- Extract shadows
    |
    v
STEP 5: RESPONSIVE ANALYSIS
    |-- Plan mobile layout
    |-- Plan tablet layout
    |-- Plan desktop layout
    |
    v
STEP 6: CODE SPEC GENERATION
    |-- Generate component specs
    |-- Generate layout specs
    |-- Generate style specs
    |-- Generate responsive specs
    |
    v
STEP 7: OUTPUT GENERATION
    |-- Generate JSON specifications
    |-- Generate CSS/Tailwind code
    |-- Generate component code
    |-- Save to linking_info.json
```

## Component Identification

### Standard Components

| Component | Variants |
|-----------|----------|
| **Button** | Primary, secondary, ghost, icon, loading |
| **Card** | Basic, featured, interactive, horizontal |
| **Input** | Text, email, password, number, textarea |
| **Select** | Dropdown, multi-select, searchable |
| **Modal** | Small, medium, large, fullscreen |
| **Toast** | Success, error, warning, info |
| **Tabs** | Horizontal, vertical, pills |
| **Accordion** | Single, multi, nested |
| **Table** | Basic, sortable, paginated |

### Layout Components

| Component | Purpose |
|-----------|---------|
| **Header** | Navigation, logo, actions |
| **Footer** | Links, copyright, social |
| **Sidebar** | Secondary navigation |
| **Hero** | Main banner, CTA |
| **Section** | Content container |
| **Grid** | Multi-column layout |

## Style Specifications

### Color Specifications

```json
{
  "colors": {
    "primary": {
      "base": "#3b82f6",
      "hover": "#2563eb",
      "active": "#1d4ed8",
      "disabled": "#93c5fd"
    }
  }
}
```

### Typography Specifications

```json
{
  "typography": {
    "heading1": {
      "fontSize": "3rem",
      "fontWeight": "700",
      "lineHeight": "1.2"
    },
    "body": {
      "fontSize": "1rem",
      "fontWeight": "400",
      "lineHeight": "1.5"
    }
  }
}
```

## Responsive Specifications

### Breakpoint System

| Breakpoint | Width | Layout Changes |
|------------|-------|----------------|
| **Mobile** | < 640px | Single column, stacked |
| **Tablet** | 640-1024px | 2 columns, adjusted spacing |
| **Desktop** | > 1024px | Full layout, all columns |

## Code Generation

### Tailwind CSS Output

```html
<!-- Button Component -->
<button class="bg-primary-500 hover:bg-primary-600 text-white font-semibold py-3 px-6 rounded-lg transition-all duration-200 hover:-translate-y-0.5 hover:shadow-lg">
  Button Text
</button>

<!-- Card Component -->
<div class="bg-white border border-neutral-200 rounded-xl p-6 shadow-sm hover:shadow-xl hover:-translate-y-0.5 transition-all duration-200">
  <!-- Card Content -->
</div>
```

### React Component Output

```tsx
import React from 'react';

interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  children: React.ReactNode;
}

export const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'md',
  children
}) => {
  const baseStyles = 'font-semibold rounded-lg transition-all duration-200';
  const variantStyles = {
    primary: 'bg-primary-500 hover:bg-primary-600 text-white',
    secondary: 'bg-neutral-100 hover:bg-neutral-200 text-neutral-900',
    ghost: 'bg-transparent hover:bg-neutral-100 text-neutral-900'
  };

  return (
    <button className={`${baseStyles} ${variantStyles[variant]}`}>
      {children}
    </button>
  );
};
```

## Integration with Other Agents

| Agent | Integration |
|-------|-------------|
| **HCS Document Analyzer** | Receives design files for analysis |
| **HCS Brand Analyzer** | Receives brand guidelines for styling |
| **HCS Website Generator** | Receives design specifications for code |
| **HCS UI Designer** | Receives design enhancements |
| **HCS Content Planner** | Receives layout specifications |

## Final Instructions

1. **NEVER skip design analysis** — Always analyze design thoroughly
2. **NEVER guess measurements** — Only extract actual values
3. **ALWAYS identify components** — Find reusable components
4. **ALWAYS extract styles** — Colors, typography, spacing
5. **ALWAYS plan responsive** — Mobile, tablet, desktop
6. **ALWAYS generate code** — Tailwind CSS + React components
7. **ALWAYS integrate** — Pass results to Website Generator


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

