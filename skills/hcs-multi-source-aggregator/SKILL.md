---
name: "HCS Multi-Source Aggregator"
description: "HCS Multi-Source Aggregator v1.0 — Autonomous Content Aggregation & Merging Engine. Combines content from multiple sources into one cohesive website."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Multi-Source Aggregator

## Purpose
Combine content from multiple sources into one cohesive, unified website.

## Supported Sources

| Source Type | Input Method |
|-------------|-------------|
| **Documents** | PDF, Word, Text, Markdown |
| **Spreadsheets** | CSV, Excel, JSON |
| **Web Pages** | URLs, HTML files |
| **Images** | JPG, PNG (OCR extraction) |
| **Videos** | MP4 (speech-to-text) |
| **Audio** | MP3 (speech-to-text) |
| **Chat Logs** | WhatsApp, Telegram exports |
| **Emails** | .eml, .msg files |
| **APIs** | REST, GraphQL endpoints |
| **Databases** | SQL dumps, JSON exports |

## Aggregation Pipeline

```
INPUT: Multiple Sources
    |
    v
STEP 1: SOURCE INVENTORY
    |-- List all sources
    |-- Identify source types
    |-- Determine source quality
    |-- Rank source reliability
    |
    v
STEP 2: CONTENT EXTRACTION (Parallel)
    |-- Extract content from Source 1
    |-- Extract content from Source 2
    |-- Extract content from Source N
    |-- Use Document Analyzer for each
    |
    v
STEP 3: CONTENT CLASSIFICATION
    |-- Classify content by type
    |-- Identify overlapping content
    |-- Identify unique content
    |-- Identify conflicting content
    |
    v
STEP 4: CONFLICT RESOLUTION
    |-- Detect duplicate content
    |-- Detect conflicting information
    |-- Apply priority rules
    |-- Resolve conflicts
    |
    v
STEP 5: CONTENT MERGING
    |-- Merge similar sections
    |-- Combine related content
    |-- Organize by topic
    |-- Create unified hierarchy
    |
    v
STEP 6: STRUCTURED OUTPUT
    |-- Generate unified JSON
    |-- Generate merged markdown
    |-- Generate source attribution
    |-- Save to linking_info.json
```

## Conflict Resolution

| Conflict Type | Resolution |
|--------------|------------|
| **Duplicate** | Keep most detailed version |
| **Contradictory** | Use higher-ranked source |
| **Incomplete** | Use available content |
| **Formatting** | Standardize format |
| **Version** | Use most recent |

## Merge Strategies

| Strategy | Use Case |
|----------|----------|
| **Concatenate** | Sequential content (chapters) |
| **Interleave** | Alternating content (topics) |
| **Hierarchical** | Nested content (categories) |
| **Unified** | Similar content (same topic) |

## Integration with Other Agents

| Agent | Integration |
|-------|-------------|
| **HCS Document Analyzer** | Extracts content from each source |
| **HCS Website Generator** | Receives unified content for website |
| **HCS Brand Analyzer** | Merges brand materials from sources |
| **HCS Content Planner** | Plans structure for merged content |

## Final Instructions

1. **NEVER skip source inventory** — Always list all sources first
2. **NEVER guess content** — Only use extracted content
3. **ALWAYS detect conflicts** — Find duplicate/conflicting content
4. **ALWAYS resolve conflicts** — Apply priority rules
5. **ALWAYS merge intelligently** — Don't just concatenate
6. **ALWAYS track sources** — Attribution for every content piece
