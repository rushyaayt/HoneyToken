
### Prerequisites

* **Python:** 3.9 or higher
* **Package Manager:** `pip`

### Installation

```bash
# Clone the repository
git clone [https://github.com/rushyaayt/HoneyToken.git](https://github.com/rushyaayt/HoneyToken.git)
```
```
# Navigate to project root
cd HoneyToken
```
```
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
```
# Install dependencies
pip install -r requirements.txt

```

---

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

---

