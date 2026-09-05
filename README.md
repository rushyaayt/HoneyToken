
---


<div align="center">

# 🍯 HoneyToken

**Lightweight Active Intrusion Detection & Decoy Token System**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)
![Security](https://img.shields.io/badge/Focus-Cybersecurity%20%26%20Deception-red?style=for-the-badge)

*Detect unauthorized access instantly by placing fake, highly monitored credentials throughout your infrastructure.*

</div>

---

## 📌 Overview

**HoneyToken** is a deception-based security solution designed to catch attackers during the reconnaissance or lateral movement phase of a breach. By scattering fake API keys, database credentials, or sensitive files across environments, HoneyToken acts as a tripwire. 

The moment an unauthorized actor attempts to interact with or use a decoy token, the system triggers an immediate alert with source IP address, timestamp, and contextual metadata.

---

## 🚀 Key Features

* **Instant Alerting:** Real-time notification when a honeytoken is accessed or executed.
* **Low False-Positive Rate:** Genuine users have no operational reason to interact with decoy tokens.
* **Flexible Token Types:** Deploy AWS-style keys, database connection strings, or custom credentials.
* **Minimal Resource Overhead:** Lightweight design built for seamless deployment in dev, staging, or production.
* **Extensible Architecture:** Easy integration with Webhooks, Discord, Slack, or SIEM tools.

---

## 🏗️ Architecture & How It Works


```

[ Attacker / Intruder ]
│
▼ (Exfiltrates decoy credential)
┌───────────────────────────┐
│     Fake HoneyToken       │
└─────────────┬─────────────┘
│
▼ (Triggers callback endpoint)
┌───────────────────────────┐
│    HoneyToken Listener    │
└─────────────┬─────────────┘
│
▼ (Dispatches real-time alert)
[ Security Team / Webhook / SIEM ]



1. **Deploy:** Generate unique decoy tokens and embed them in source code, configuration files, or local environments.
2. **Monitor:** The HoneyToken listener actively waits for interactions with the generated tokens.
3. **Alert:** When triggered, the system captures actionable metadata (IP address, User-Agent, location details) and notifies the admin instantly.

---

## 🛠️ Quick Start

### Prerequisites
* Python 3.8 or higher
* `pip` package manager

### Installation

```bash
# Clone the repository
git clone [https://github.com/rushyaayt/HoneyToken.git](https://github.com/rushyaayt/HoneyToken.git)

# Navigate to the directory
cd HoneyToken

# Install dependencies
pip install -r requirements.txt

```

### Basic Usage

```bash
# Run the HoneyToken listener service
python main.py

```

---

## 🛡️ License

Distributed under the **MIT License**. See `LICENSE` for more information.

---
