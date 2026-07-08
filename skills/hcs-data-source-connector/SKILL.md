---
name: "HCS Data Source Connector"
description: "HCS Data Source Connector v1.0 — Autonomous Data Integration Engine. Connects to CSV, JSON, SQL, APIs and generates website content."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Data Source Connector

## Purpose
Connect to various data sources and transform data into website content.

## Supported Data Sources

### File-Based Sources

| Source | Format | Connection Method |
|--------|--------|-------------------|
| **CSV** | `.csv` | File read + parse |
| **JSON** | `.json` | File read + parse |
| **XML** | `.xml` | File read + parse |
| **Excel** | `.xlsx`, `.xls` | File read + parse |

### Database Sources

| Source | Connection Method |
|--------|-------------------|
| **PostgreSQL** | Connection string + query |
| **MySQL** | Connection string + query |
| **SQLite** | File path + query |
| **MongoDB** | Connection string + query |

### API Sources

| Source | Connection Method |
|--------|-------------------|
| **REST API** | HTTP requests |
| **GraphQL** | GraphQL queries |
| **WebSocket** | Real-time connection |

### Cloud Sources

| Source | Connection Method |
|--------|-------------------|
| **Google Sheets** | API integration |
| **Airtable** | API integration |
| **Notion** | API integration |
| **Supabase** | SDK integration |

## Data Connection Pipeline

```
INPUT: Data Source
    |
    v
STEP 1: SOURCE DETECTION
    |-- Identify data source type
    |-- Determine connection method
    |-- Check accessibility
    |-- Validate source
    |
    v
STEP 2: SCHEMA ANALYSIS
    |-- Analyze data structure
    |-- Identify fields/columns
    |-- Determine data types
    |-- Detect relationships
    |
    v
STEP 3: DATA EXTRACTION
    |-- Extract data from source
    |-- Handle pagination (if needed)
    |-- Transform data format
    |-- Validate data integrity
    |
    v
STEP 4: DATA TRANSFORMATION
    |-- Clean data
    |-- Standardize formats
    |-- Handle missing values
    |-- Enrich data
    |
    v
STEP 5: CONTENT MAPPING
    |-- Map data to website sections
    |-- Determine display format
    |-- Plan interactive features
    |
    v
STEP 6: CODE GENERATION
    |-- Generate data fetching code
    |-- Generate data display components
    |-- Generate error handling
    |-- Generate loading states
    |
    v
STEP 7: OUTPUT GENERATION
    |-- Generate complete integration code
    |-- Generate data schema documentation
    |-- Generate setup instructions
    |-- Save to linking_info.json
```

## Content Mapping

| Data Type | Website Element |
|-----------|-----------------|
| **List of items** | Grid/list of cards |
| **Single item** | Detail page |
| **Key-value pairs** | Table or list |
| **Time series** | Chart or timeline |
| **Categories** | Categorized sections |
| **Products** | Product catalog |
| **Posts** | Blog/articles |

## Integration with Other Agents

| Agent | Integration |
|-------|-------------|
| **HCS Document Analyzer** | Extracts data from documents |
| **HCS Website Generator** | Receives data integration code |
| **HCS Multi-Source Aggregator** | Merges data from multiple sources |
| **HCS Data Linker** | Links data to frontend/backend |

## Final Instructions

1. **NEVER skip schema analysis** — Always detect data structure first
2. **NEVER guess data types** — Only use detected types
3. **ALWAYS clean data** — Handle missing/invalid values
4. **ALWAYS validate** — Ensure data integrity
5. **ALWAYS generate types** — Type-safe data handling
