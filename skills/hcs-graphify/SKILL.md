---
name: "HCS Graphify"
description: "HCS Knowledge Graph Engine — Converts any folder of files into navigable knowledge graphs with community detection, audit trails, and multiple output formats (HTML, JSON, Obsidian, Neo4j). Triggers on: graphify, knowledge graph, code graph, graph visualization, community detection, graphrag."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS GRAPHIFY

## PURPOSE

Convert any folder of files (code, docs, papers, images) into a structured knowledge graph that shows you what you didn't know was connected.

## WHAT GRAPHIFY DOES

- 📂 **File Processing** — Accepts folders, files, or piped context
- 🔗 **Graph Building** — Entities and edges with evidence tags
- 🏷️ **Honest Tags** — EXTRACTED, INFERRED, AMBIGUOUS
- 🔍 **Graph Queries** — BFS/DFS traversal
- 🏘️ **Community Detection** — Automatic clustering
- 🌐 **Path Finding** — Discover connections
- 📊 **Audit Trail** — God nodes, surprises, suggestions
- 🔄 **Incremental Updates** — Change only what changed
- 📁 **Multiple Formats** — HTML, JSON, Obsidian, Neo4j

## USAGE

```bash
# Full pipeline on current directory
/graphify

# Full pipeline on specific path
/graphify <path>

# Deep mode - richer extraction
/graphify <path> --mode deep

# Incremental update
/graphify <path> --update

# Query the graph
/graphify query "How does auth module connect to database?"

# Find shortest path
/graphify path "AuthModule" "Database"

# Explain a concept
/graphify explain "SwinTransformer"
```

## OUTPUTS

| Output | Description |
|--------|-------------|
| `graph.html` | Interactive graph visualization |
| `GRAPH_REPORT.md` | Audit report with god nodes, surprises |
| `graph.json` | GraphRAG-ready JSON |
| `obsidian/` | Obsidian vault (opt-in) |
| `cypher.txt` | Neo4j import (opt-in) |

## HOW IT WORKS

### Step 1: Detect Files
- Scans folder for code, docs, papers, images, video
- Counts words and files

### Step 2: Extract Entities
- **Part A**: AST extraction for code (deterministic, free)
- **Part B**: Semantic extraction for docs/papers (LLM-based)
- **Part C**: Merge AST + semantic results

### Step 3: Build Graph
- Build NetworkX graph from extraction
- Community detection (Louvain)
- God node identification
- Surprising connection discovery

### Step 4: Generate Outputs
- Interactive HTML visualization
- Audit report with suggestions
- GraphRAG-ready JSON

## EDGE CONFIDENCE

| Tag | Description | Score |
|-----|-------------|-------|
| **EXTRACTED** | Explicit in source | 1.0 |
| **INFERRED** | Reasonable inference | 0.6-0.9 |
| **AMBIGUOUS** | Uncertain, flagged for review | 0.1-0.3 |

## QUERY MODES

| Mode | Flag | Best For |
|------|------|----------|
| **BFS** | (default) | "What is X connected to?" — broad context |
| **DFS** | `--dfs` | "How does X reach Y?" — trace specific path |

## PIPELINE

1. **Scan folder** — Detect files, count words
2. **Extract entities** — AST + semantic (parallel)
3. **Build graph** — Nodes, edges, confidence
4. **Community detection** — Louvain algorithm
5. **Query traversal** — BFS/DFS
6. **Generate outputs** — HTML, JSON, report
7. **Audit trail** — God nodes, surprises
8. **Suggestions** — Missing connections, topics
9. **Export formats** — Obsidian, Neo4j

## RELATED AGENTS

| Agent | Integration |
|-------|-------------|
| **HCS Document Analyzer** | Document processing |
| **HCS Chonkie** | Text chunking |
| **HCS Code Generator** | Code analysis |
| **HCS Data Visualizer** | Graph visualization |
| **HCS RAG Builder** | RAG pipelines |

## FINAL INSTRUCTIONS

1. Follow the 9-step pipeline
2. Use parallel extraction (AST + semantic)
3. Tag edges with confidence levels
4. Generate honest audit trails
5. Support incremental updates

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

### Adversarial Checklist

- [ ] Did I test on exact input that failed?
- [ ] Did I verify visual/PDF/3D output?
- [ ] Did I run skeptic pass on my own work?
- [ ] Did I check for silent reversals?
- [ ] Did I mark claims as CONFIRMED/INFERRED?
- [ ] Did I provide evidence sources?
