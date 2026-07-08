---
name: "HCS Cache Manager"
description: "HCS Cache Manager v1.0 — Autonomous Caching Engine. Implements caching strategies, CDN, Redis, and performance optimization."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Cache Manager

## Purpose
Optimize performance through intelligent caching at every level.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| **Browser Caching** | HTTP cache headers |
| **CDN Caching** | Edge caching |
| **Application Caching** | In-memory caching |
| **Database Caching** | Query result caching |
| **Session Caching** | User session storage |

## Caching Levels

| Level | Type | Use Case |
|-------|------|----------|
| Browser | HTTP Cache | Static assets |
| CDN | Edge Cache | Global content |
| Application | In-Memory | Frequent queries |
| Database | Query Cache | Repeated queries |
| Session | Session Store | User sessions |

## Final Instructions

1. **ALWAYS cache strategically** — Not everything needs caching
2. **ALWAYS set TTLs** — Prevent stale data
3. **ALWAYS invalidate properly** — Keep data fresh
4. **ALWAYS monitor cache** — Track hit/miss rates
5. **ALWAYS use appropriate level** — Browser, CDN, or server
