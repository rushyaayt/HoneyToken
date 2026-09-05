

<div align="center">

# 🍯 HoneyToken

### **Enterprise Deception & Active Intrusion Tripwire System**

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/rushyaayt/HoneyToken/main.yml?branch=main&style=for-the-badge&logo=github&label=Build)](https://github.com/rushyaayt/HoneyToken)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Security Focus](https://img.shields.io/badge/Domain-Cybersecurity%20%26%20Deception-red?style=for-the-badge&logo=shield)](https://github.com/rushyaayt/HoneyToken)

*Catch unauthorized network access during early reconnaissance by deploying intelligent, zero-false-positive decoy credentials.*
## Check (Installation.md) for running the project
---

</div>

---

## 📌 Overview
# Honeytoken-as-a-Service

Lightweight service to generate and seed realistic honeytokens (API keys, fake user accounts, DB rows) and emit high-fidelity alerts when a token is used.

Features
- Generate ephemeral or persistent honeytokens
- Simple webhook alerting and logging
- Dockerized FastAPI app

Quick start
1. Build: docker build -t honeytoken-service .
2. Run: docker run -p 8000:8000 honeytoken-service
3. POST /generate to get a token; any request using the token should hit /webhook on this service (or forward alerts).

Files
- src/honeytoken_service: app code
- examples/: seeding scripts
- .github/workflows: CI

License: MIT

Because legitimate operators have no valid business reason to interact with decoy tokens, any access attempt generates an immediate, high-fidelity alert with zero false positives.

---

## 🏗️ Architecture

The sequence below illustrates the lifecycle of an intruder interaction:


```

+-------------------+             +-----------------------+
|  Attacker / Threat|             |   Decoy Infrastructure|
|      Actor        |             |  (Codebase / Envs)    |
+---------+---------+             +-----------+-----------+
|                                   |
|  1. Exfiltrates & triggers        |
+---------------------------------->|
|
v
+-----------------------+
|    HoneyToken Lure    |
+-----------+-----------+
|
|  2. Sends payload request
v
+-----------------------+
|  HoneyToken Listener  |
|    (Ingestion Engine) |
+-----------+-----------+
|
|  3. Dispatches enriched alert
v
+-----------------------+
| Security Team / SIEM  |
| (Slack / Discord)     |
+-----------------------+

```

---

## 🚀 Getting Started
## 🔔 Integrations

Configure notifications in your `.env` file to stream real-time alerts to your security operating center (SOC) or messaging channels:

| Integration | Supported | Description |
| --- | --- | --- |
| **Discord Webhooks** | ✅ | Native rich embed alerts directly to your monitoring channel |
| **Slack Webhooks** | ✅ | Structured Block Kit notifications with actionable metadata |
| **Custom Webhooks** | ✅ | Forward raw JSON payloads to custom endpoints or SIEMs |
| **Email (SMTP)** | 🚧 | *In Development* |

---
