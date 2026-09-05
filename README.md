


<div align="center">


# 🍯 HoneyToken

### **Enterprise Deception & Active Intrusion Tripwire System**

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/rushyaayt/HoneyToken/main.yml?branch=main&style=for-the-badge&logo=github&label=Build)](https://github.com/rushyaayt/HoneyToken)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Security Focus](https://img.shields.io/badge/Domain-Cybersecurity%20%26%20Deception-red?style=for-the-badge&logo=shield)](https://github.com/rushyaayt/HoneyToken)

*Catch unauthorized network access during early reconnaissance by deploying intelligent, zero-false-positive decoy credentials.*



[Key Features](#-key-features) • [Architecture](#-architecture) • [Getting Started](#-getting-started) • [Configuration](#-configuration) • [Integrations](#-integrations) • [License](#-license)

</div>



## 📌 Overview

**HoneyToken** is an open-source active defense framework designed to detect intruders during lateral movement and exfiltration attempts. By strategically scattering lure credentials—such as fake API keys, cloud tokens, database strings, and decoy configuration files—across your codebase, servers, and CI/CD pipelines, HoneyToken acts as an invisible security tripwire.

Because legitimate operators have no valid business reason to interact with decoy tokens, any access attempt generates an immediate, high-fidelity alert with zero false positives.



## ✨ Key Features

* ⚡ **Zero False Positives:** Every interaction with a honeytoken indicates unauthorized activity.
* 🛡️ **Multiple Decoy Types:** Support for AWS Keys, JWTs, Database Credentials, and HTTP Callback Webhooks.
* 📍 **Rich Telemetry Capture:** Logs source IP, reverse DNS, User-Agent header, geolocation data, and exact timestamp.
* 🔔 **Instant Alerting Dispatch:** Direct integrations with Discord, Slack, PagerDuty, Webhooks, and SIEM pipelines.
* 🪶 **Lightweight & Modular:** Asynchronous listener design with minimal resource footprint and simple API integration.



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



## 🚀 Getting Started

### Prerequisites

* **Python:** 3.9 or higher
* **Package Manager:** `pip`

### Installation

```bash
# Clone the repository
git clone [https://github.com/rushyaayt/HoneyToken.git](https://github.com/rushyaayt/HoneyToken.git)

# Navigate to project root
cd HoneyToken

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

```



## ⚙️ Quick Usage

### 1. Configure Environment

Copy the example configuration file and specify your listener and notification endpoints:

```bash
cp .env.example .env

```

### 2. Generate Decoy Tokens

Run the CLI tool to craft a new monitored credential:

```bash
python honeytoken.py generate --type aws_key --label "Production-DB-Lure"

```

### 3. Start the Listener

Spin up the ingestion engine to monitor incoming trigger attempts:

```bash
python honeytoken.py listen --port 8080

```



## 🔔 Integrations

Configure notifications in your `.env` file to stream real-time alerts to your security operating center (SOC) or messaging channels:

| Integration | Supported | Description |
| --- | --- | --- |
| **Discord Webhooks** | ✅ | Native rich embed alerts directly to your monitoring channel |
| **Slack Webhooks** | ✅ | Structured Block Kit notifications with actionable metadata |
| **Custom Webhooks** | ✅ | Forward raw JSON payloads to custom endpoints or SIEMs |
| **Email (SMTP)** | 🚧 | *In Development* |



## 🤝 Contributing

Contributions make the open-source community an incredible place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. **Fork** the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your Changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the Branch (`git push origin feature/AmazingFeature`)
5. Open a **Pull Request**



## 🛡️ License

Distributed under the **MIT License**. See [`LICENSE`](https://www.google.com/search?q=LICENSE) for details.


