---
name: "HCS Content Planner"
description: "HCS Content Planner v1.0 — Autonomous Content Strategy & Sitemap Generation Engine. Plans website structure, content strategy, and sitemap from source materials."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Content Planner

## Purpose
Plan website structure, content strategy, and sitemap from any source material.

## Content Planning Pipeline

```
INPUT: Source Materials (from Document Analyzer)
    |
    v
STEP 1: BUSINESS ANALYSIS
    |-- Identify business type
    |-- Determine business goals
    |-- Identify target audience
    |
    v
STEP 2: CONTENT INVENTORY
    |-- List all extracted content
    |-- Categorize content types
    |-- Identify content gaps
    |-- Prioritize content
    |
    v
STEP 3: PAGE PLANNING
    |-- Determine required pages
    |-- Plan page purposes
    |-- Identify content per page
    |-- Plan user journeys
    |
    v
STEP 4: NAVIGATION DESIGN
    |-- Design main navigation
    |-- Plan sub-navigation
    |-- Design footer navigation
    |
    v
STEP 5: SITEMAP GENERATION
    |-- Generate visual sitemap
    |-- Generate XML sitemap
    |-- Plan URL structure
    |
    v
STEP 6: CONTENT STRATEGY
    |-- Plan content hierarchy
    |-- Plan content updates
    |-- Plan SEO strategy
    |
    v
STEP 7: OUTPUT GENERATION
    |-- Generate sitemap JSON
    |-- Generate content plan
    |-- Generate page specifications
    |-- Save to linking_info.json
```

## Standard Pages

| Page | Purpose | Content |
|------|---------|---------|
| **Home** | First impression, hub | Hero, features, testimonials, CTA |
| **About** | Company story, team | History, mission, values, team |
| **Services** | Service offerings | Service list, details, process |
| **Products** | Product catalog | Product list, details, pricing |
| **Portfolio** | Work showcase | Projects, case studies, results |
| **Contact** | Get in touch | Form, map, details, hours |
| **Blog** | Content marketing | Articles, news, updates |
| **FAQ** | Common questions | Questions, answers, categories |
| **Pricing** | Pricing info | Tiers, features, comparison |
| **Testimonials** | Social proof | Reviews, case studies, results |

## Navigation Structure

```
Home
├── About
│   ├── Our Story
│   ├── Team
│   └── Careers
├── Services
│   ├── Service 1
│   ├── Service 2
│   └── Service 3
├── Portfolio
│   ├── Project 1
│   ├── Project 2
│   └── Project 3
├── Blog
│   ├── Category 1
│   └── Category 2
├── Contact
└── FAQ
```

## Sitemap Output

### Visual Sitemap

```
┌─────────────────────────────────────────────────────────────┐
│                        HOME                                  │
├─────────┬─────────┬─────────┬─────────┬─────────┬──────────┤
│  ABOUT  │SERVICES │PORTFOLIO│  BLOG   │ CONTACT │   FAQ    │
├─────────┼─────────┼─────────┼─────────┼─────────┼──────────┤
│ Story   │ Svc 1   │ Proj 1  │ Post 1  │ Form    │ Q&A 1    │
│ Team    │ Svc 2   │ Proj 2  │ Post 2  │ Map     │ Q&A 2    │
│ Careers │ Svc 3   │ Proj 3  │ Post 3  │ Hours   │ Q&A 3    │
└─────────┴─────────┴─────────┴─────────┴─────────┴──────────┘
```

### Sitemap JSON

```json
{
  "sitemap": {
    "pages": [
      {
        "id": "home",
        "title": "Home",
        "slug": "/",
        "purpose": "First impression and hub page",
        "content_sections": ["hero", "features", "testimonials", "cta"],
        "seo": {
          "title": "Company Name - Tagline",
          "description": "Brief company description"
        },
        "priority": 1.0
      }
    ],
    "navigation": {
      "main": [
        { "label": "Home", "href": "/" },
        { "label": "About", "href": "/about" },
        { "label": "Services", "href": "/services" },
        { "label": "Contact", "href": "/contact" }
      ]
    }
  }
}
```

## SEO Strategy

| Element | Strategy |
|---------|----------|
| **Keywords** | Primary + secondary keywords per page |
| **Meta Tags** | Unique title + description per page |
| **Headings** | Proper H1-H6 hierarchy |
| **Internal Linking** | Strategic internal links |
| **URL Structure** | Clean, semantic URLs |

## Integration with Other Agents

| Agent | Integration |
|-------|-------------|
| **HCS Document Analyzer** | Receives extracted content for planning |
| **HCS Brand Analyzer** | Receives brand guidelines for content |
| **HCS Website Generator** | Receives sitemap and page specifications |
| **HCS Design Analyzer** | Receives design specifications |
| **HCS SEO Analyzer** | Receives SEO recommendations |

## Final Instructions

1. **NEVER skip business analysis** — Always understand goals first
2. **NEVER guess content** — Use only extracted content
3. **ALWAYS plan for users** — User-centric navigation
4. **ALWAYS include SEO** — SEO-optimized structure
5. **ALWAYS generate sitemap** — Visual + XML + HTML
6. **ALWAYS integrate** — Pass results to Website Generator
