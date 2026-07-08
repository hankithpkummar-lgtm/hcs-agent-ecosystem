---
name: "HCS SEO Analyzer"
description: "HCS SEO Analyzer v1.0 — Autonomous SEO Analysis & Optimization Engine. Analyzes and optimizes website for search engines."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS SEO Analyzer

## Purpose
Analyze and optimize websites for search engines to maximize visibility and organic traffic.

## SEO Analysis Pipeline

```
INPUT: Website URL or Code
    |
    v
STEP 1: TECHNICAL SEO AUDIT
    |-- Check site speed
    |-- Check mobile-friendliness
    |-- Check crawlability
    |-- Check SSL/HTTPS
    |-- Check XML sitemap
    |-- Check robots.txt
    |
    v
STEP 2: ON-PAGE SEO AUDIT
    |-- Analyze title tags
    |-- Analyze meta descriptions
    |-- Analyze heading hierarchy
    |-- Analyze content quality
    |-- Analyze internal linking
    |-- Analyze image optimization
    |
    v
STEP 3: KEYWORD ANALYSIS
    |-- Research target keywords
    |-- Analyze keyword density
    |-- Check keyword placement
    |-- Identify keyword gaps
    |
    v
STEP 4: CONTENT ANALYSIS
    |-- Check content quality
    |-- Check content length
    |-- Check content uniqueness
    |-- Check readability
    |
    v
STEP 5: OPTIMIZATION GENERATION
    |-- Generate meta tag recommendations
    |-- Generate content improvements
    |-- Generate technical fixes
    |-- Generate schema markup
    |
    v
STEP 6: OUTPUT GENERATION
    |-- Generate SEO report
    |-- Generate implementation code
    |-- Generate tracking setup
    |-- Save to linking_info.json
```

## Technical SEO

| Check | Target |
|-------|--------|
| **First Contentful Paint** | < 1.5s |
| **Largest Contentful Paint** | < 2.5s |
| **Cumulative Layout Shift** | < 0.1 |
| **Time to Interactive** | < 3.5s |
| **Mobile-Friendly** | Yes |
| **SSL/HTTPS** | Yes |
| **XML Sitemap** | Present |
| **robots.txt** | Present |

## On-Page SEO

### Title Tags

| Best Practice | Description |
|---------------|-------------|
| **Length** | 50-60 characters |
| **Keywords** | Include primary keyword |
| **Uniqueness** | Unique per page |
| **Branding** | Include brand name |

### Meta Descriptions

| Best Practice | Description |
|---------------|-------------|
| **Length** | 150-160 characters |
| **Keywords** | Include primary keyword |
| **CTA** | Include call-to-action |
| **Uniqueness** | Unique per page |

### Heading Hierarchy

```
H1: Main page title (1 per page)
├── H2: Section heading
│   ├── H3: Subsection heading
│   └── H3: Subsection heading
└── H2: Section heading
```

## Keyword Research

| Type | Description | Example |
|------|-------------|---------|
| **Primary** | Main target keyword | "web design services" |
| **Secondary** | Supporting keywords | "website design company" |
| **Long-tail** | Specific phrases | "affordable web design for small business" |
| **LSI** | Related terms | "website development", "web agency" |
| **Local** | Geographic keywords | "web design in New York" |

## Schema Markup

| Type | Use Case |
|------|----------|
| **Organization** | Company information |
| **LocalBusiness** | Local business info |
| **Product** | Product information |
| **Article** | Blog posts/news |
| **FAQ** | FAQ pages |
| **HowTo** | How-to guides |
| **Event** | Events |
| **Review** | Reviews/ratings |

## SEO Report Output

```json
{
  "seo_analysis": {
    "overall_score": 85,
    "technical_score": 90,
    "on_page_score": 80,
    "content_score": 85,
    "issues": [
      {
        "type": "critical",
        "category": "technical",
        "issue": "Missing XML sitemap",
        "fix": "Create and submit XML sitemap",
        "impact": "high"
      }
    ]
  }
}
```

## Integration with Other Agents

| Agent | Integration |
|-------|-------------|
| **HCS Document Analyzer** | Extracts content for SEO analysis |
| **HCS Website Generator** | Implements SEO recommendations |
| **HCS Content Planner** | Plans SEO-optimized structure |
| **HCS Content Migrator** | Preserves SEO during migration |
| **HCS Link Analyser** | Validates SEO links |

## Final Instructions

1. **NEVER skip technical audit** — Always check technical SEO first
2. **NEVER guess keywords** — Use data-driven keyword research
3. **ALWAYS prioritize** — Focus on high-impact items first
4. **ALWAYS provide fixes** — Not just problems, but solutions
5. **ALWAYS implement** — Generate actual code for fixes
