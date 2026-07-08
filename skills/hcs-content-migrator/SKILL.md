---
name: "HCS Content Migrator"
description: "HCS Content Migrator v1.0 — Autonomous Content Migration Engine. Migrates content from old website to new."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Content Migrator

## Purpose
Seamlessly transfer all content from old websites to new ones while preserving structure and improving quality.

## Supported Platforms

| Platform | Extraction Method |
|----------|-------------------|
| **WordPress** | XML export / WP API |
| **Shopify** | CSV export / Admin API |
| **Wix** | Site export |
| **Squarespace** | XML export |
| **Webflow** | CMS API |
| **Contentful** | Management API |
| **Strapi** | REST API |
| **Custom HTML** | Web scraping |

## Migration Pipeline

```
INPUT: Old Website/Export File
    |
    v
STEP 1: SOURCE ANALYSIS
    |-- Analyze old website structure
    |-- Identify content types
    |-- Extract all content
    |-- Map content hierarchy
    |
    v
STEP 2: CONTENT EXTRACTION
    |-- Extract pages/posts
    |-- Extract media files
    |-- Extract metadata
    |-- Extract navigation
    |
    v
STEP 3: CONTENT TRANSFORMATION
    |-- Clean content
    |-- Standardize formatting
    |-- Update outdated info
    |-- Enhance content quality
    |
    v
STEP 4: STRUCTURE MAPPING
    |-- Map old structure to new
    |-- Plan new hierarchy
    |-- Design new navigation
    |-- Plan URL redirects
    |
    v
STEP 5: CONTENT ENRICHMENT
    |-- Add missing metadata
    |-- Optimize images
    |-- Improve SEO
    |-- Add accessibility
    |
    v
STEP 6: MIGRATION EXECUTION
    |-- Generate new content files
    |-- Create new structure
    |-- Set up redirects
    |-- Validate migration
    |
    v
STEP 7: QUALITY CHECK
    |-- Verify all content migrated
    |-- Check for broken links
    |-- Validate SEO
    |-- Test functionality
    |
    v
STEP 8: OUTPUT GENERATION
    |-- Generate migrated website
    |-- Generate migration report
    |-- Generate redirect map
    |-- Save to linking_info.json
```

## Content Types

| Type | Migration Handling |
|------|-------------------|
| **Pages** | Full content migration |
| **Posts/Articles** | Content + metadata + categories |
| **Products** | Product data + images + variants |
| **Media** | Images + videos + documents |
| **Categories/Tags** | Taxonomy migration |
| **Users** | User accounts (if needed) |
| **Comments** | Comment migration |

## Redirect Management

| Type | Use Case |
|------|----------|
| **301** | Permanent redirect |
| **302** | Temporary redirect |
| **307** | Temporary redirect (preserve method) |
| **308** | Permanent redirect (preserve method) |

## Integration with Other Agents

| Agent | Integration |
|-------|-------------|
| **HCS Document Analyzer** | Extracts content from old site |
| **HCS Website Generator** | Generates new website with migrated content |
| **HCS Multi-Source Aggregator** | Merges content from multiple old sites |
| **HCS SEO Analyzer** | Optimizes migrated content |
| **HCS Link Analyser** | Validates all links |

## Final Instructions

1. **NEVER skip source analysis** — Always analyze old site first
2. **NEVER lose content** — Ensure all content is extracted
3. **ALWAYS preserve structure** — Maintain content hierarchy
4. **ALWAYS create redirects** — Preserve SEO value
5. **ALWAYS enhance** — Improve while migrating
