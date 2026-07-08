---
name: "HCS vLLM"
description: "HCS vLLM v1.0 — Autonomous LLM Inference Engine. Integrates vLLM for high-throughput LLM serving."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS vLLM

## Purpose

Integrate vLLM for high-throughput, memory-efficient LLM inference and serving.

## GitHub

https://github.com/vllm-project/vllm

## Features

| Feature | Description |
|---------|-------------|
| **High Throughput** | Batch requests |
| **Memory Efficient** | PagedAttention |
| **Continuous Batching** | Dynamic batching |
| **Tensor Parallelism** | Multi-GPU |
| **OpenAI API** | Compatible API |

## Installation

```bash
pip install vllm
```

## Final Instructions

### Domain Rules
1. Optimize GPU memory usage
2. Configure batching properly
3. Monitor throughput
4. Handle model loading
5. Scale horizontally

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
