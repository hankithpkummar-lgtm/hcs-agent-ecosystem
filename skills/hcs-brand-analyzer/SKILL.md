---
name: "HCS Brand Analyzer"
description: "HCS Brand Analyzer v1.0 — Autonomous Brand Extraction & Style Analysis Engine. Extracts brand colors, fonts, logos, style from existing materials. Analyzes brand identity and generates design system."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Brand Analyzer

## Purpose
Extract, analyze, and structure brand identity from any source into website-ready design systems.

## Brand Analysis Pipeline

```
USER INPUT (Brand Source)
    |
    v
STEP 1: SOURCE DETECTION
    |-- Identify source type (logo, website, document, image)
    |-- Determine analysis method
    |
    v
STEP 2: COLOR EXTRACTION
    |-- Extract dominant colors
    |-- Identify primary/secondary colors
    |-- Extract accent colors
    |-- Generate color palette
    |-- Ensure accessibility contrast
    |
    v
STEP 3: TYPOGRAPHY EXTRACTION
    |-- Identify heading fonts
    |-- Identify body fonts
    |-- Determine font sizes
    |-- Extract line heights
    |-- Extract letter spacing
    |
    v
STEP 4: LOGO ANALYSIS
    |-- Extract logo variations
    |-- Determine logo usage rules
    |-- Extract clear space requirements
    |-- Identify logo colors
    |
    v
STEP 5: STYLE ANALYSIS
    |-- Analyze visual style
    |-- Determine design language
    |-- Extract spacing patterns
    |-- Identify border styles
    |-- Extract shadow styles
    |
    v
STEP 6: DESIGN SYSTEM GENERATION
    |-- Generate color tokens
    |-- Generate typography tokens
    |-- Generate spacing tokens
    |-- Generate Tailwind config
    |
    v
STEP 7: OUTPUT GENERATION
    |-- Generate JSON design system
    |-- Generate CSS variables
    |-- Generate Tailwind config
    |-- Save to linking_info.json
```

## Color Extraction

### Color Classification

| Color Type | Description | Example |
|------------|-------------|---------|
| **Primary** | Main brand color | #1a73e8 |
| **Secondary** | Supporting color | #34a853 |
| **Accent** | Highlight color | #ea4335 |
| **Neutral** | Background/text colors | #ffffff, #000000 |
| **Success** | Positive actions | #28a745 |
| **Warning** | Caution states | #ffc107 |
| **Error** | Error states | #dc3545 |
| **Info** | Information | #17a2b8 |

### Color Accessibility

| Standard | Requirement |
|----------|-------------|
| **Normal Text** | 4.5:1 contrast ratio |
| **Large Text** | 3:1 contrast ratio |
| **UI Components** | 3:1 contrast ratio |

## Typography Extraction

| Property | Description |
|----------|-------------|
| **Font Family** | Primary font name |
| **Font Weights** | Available weights (400, 500, 600, 700) |
| **Font Sizes** | Size scale (sm, base, lg, xl, etc.) |
| **Line Heights** | Leading values |
| **Letter Spacing** | Tracking values |

## Logo Analysis

### Logo Variations

| Variation | Use Case |
|-----------|----------|
| **Primary** | Main logo (full color) |
| **Dark** | For dark backgrounds |
| **Light** | For light backgrounds |
| **Icon** | Logo mark only |
| **Wordmark** | Text only |
| **Favicon** | Browser tab icon |

## Design System Output

### JSON Design System

```json
{
  "brand": {
    "name": "Company Name",
    "tagline": "Company Tagline"
  },
  "colors": {
    "primary": {
      "50": "#eff6ff",
      "100": "#dbeafe",
      "200": "#bfdbfe",
      "300": "#93c5fd",
      "400": "#60a5fa",
      "500": "#3b82f6",
      "600": "#2563eb",
      "700": "#1d4ed8",
      "800": "#1e40af",
      "900": "#1e3a8a"
    },
    "secondary": {
      "500": "#22c55e"
    },
    "accent": {
      "500": "#f97316"
    }
  },
  "typography": {
    "fontFamily": {
      "heading": "Inter, system-ui, sans-serif",
      "body": "Inter, system-ui, sans-serif"
    }
  },
  "spacing": {
    "1": "0.25rem",
    "2": "0.5rem",
    "4": "1rem",
    "8": "2rem"
  },
  "logo": {
    "primary": "/images/logo.png",
    "dark": "/images/logo-dark.png",
    "light": "/images/logo-light.png"
  }
}
```

### Tailwind Config

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: {
          500: '#3b82f6',
          600: '#2563eb',
        },
        secondary: {
          500: '#22c55e',
        },
      },
      fontFamily: {
        heading: ['Inter', 'system-ui', 'sans-serif'],
        body: ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
}
```

## Integration with Other Agents

| Agent | Integration |
|-------|-------------|
| **HCS Document Analyzer** | Receives brand materials for analysis |
| **HCS Website Generator** | Receives design system for styling |
| **HCS Content Planner** | Receives brand guidelines for content |
| **HCS Design Analyzer** | Receives design specifications |
| **HCS UI Designer** | Receives brand tokens for UI design |

## Final Instructions

1. **NEVER skip brand analysis** — Always extract brand identity first
2. **NEVER guess colors/fonts** — Only extract what's actually there
3. **ALWAYS ensure accessibility** — WCAG color contrast
4. **ALWAYS output structured data** — JSON + CSS + Tailwind config
5. **ALWAYS generate complete design system** — Colors, typography, spacing
6. **ALWAYS integrate** — Pass results to Website Generator


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

