---
name: "HCS Chonkie"
description: "HCS Chonkie v1.0 — Autonomous Text Chunking Engine. Integrates Chonkie library for RAG pipeline text chunking."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Chonkie

## Purpose

Integrate Chonkie library for fast, efficient text chunking in RAG pipelines.

## GitHub

https://github.com/chonkie-inc/chonkie

## Chunkers

| Chunker | Description |
|---------|-------------|
| `TokenChunker` | Fixed-size token chunks |
| `FastChunker` | SIMD-accelerated (100+ GB/s) |
| `SentenceChunker` | Sentence-based |
| `RecursiveChunker` | Hierarchical rules |
| `SemanticChunker` | Semantic similarity |
| `CodeChunker` | Code-aware |
| `NeuralChunker` | Neural model |

## Installation

```bash
pip install chonkie
```

## Final Instructions

### Domain Rules
1. Choose appropriate chunker
2. Optimize chunk size
3. Handle overlap
4. Integrate with vector DBs
5. Monitor chunk quality

### Fabel5 Quality Rules
6. Be skeptical — Find issues
7. Be thorough — Check every claim
8. Be honest — Say if wrong
9. Be specific — Provide findings
10. Be constructive — Suggest fixes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## FABEL5 DISCIPLINE (MANDATORY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**This skill follows the Fabel5 six-phase senior-engineer loop.**

### Core Principle: THE MAKER IS NEVER THE GRADER

| Phase | Action |
|-------|--------|
| **1. THINK** | Map system, find source of truth |
| **2. DECOMPOSE** | Split into ONE bounded units |
| **3. PROVE IT** | Build, run tests, validate |
| **4. RESPECT INTENT** | Never reverse decisions silently |
| **5. VERIFY DELIVERY** | Confirm change landed |
| **6. LEAVE NAVIGABLE** | Update notes, write STATE.md |

### Evidence-Based Claims

| Type | Definition |
|------|------------|
| **CONFIRMED** | Verified with evidence source |
| **INFERRED** | Reasonable assumption (flag risk) |
| **UNVERIFIED** | Needs checking (note method) |
