---
name: "HCS Monitoring"
description: "HCS Monitoring v1.0 — Autonomous Monitoring & Observability Engine. Implements logging, metrics, alerting, and observability."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Monitoring

## Purpose
Implement comprehensive monitoring and observability for applications.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| **Logging** | Structured logging with pino/winston |
| **Metrics** | Prometheus metrics collection |
| **Tracing** | Distributed tracing with OpenTelemetry |
| **Alerting** | Alert rules and notifications |
| **Dashboards** | Grafana/Datadog dashboards |

## Three Pillars

| Pillar | Description |
|--------|-------------|
| **Logging** | Application logs and events |
| **Metrics** | Quantitative measurements |
| **Tracing** | Request flow through system |

## Final Instructions

1. **ALWAYS implement logging** — Use structured logging
2. **ALWAYS track metrics** — Business and technical
3. **ALWAYS set alerts** — Proactive issue detection
4. **ALWAYS use correlation IDs** — Trace requests end-to-end
5. **ALWAYS monitor health** — Health check endpoints
