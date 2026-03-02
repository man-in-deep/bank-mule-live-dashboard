# bank-mule-live-dashboard
---

# 🏦 Bank Mule Detection – Live Dashboard (PoC)

## 📌 Overview

This project is a **Proof of Concept (PoC)** for a **Banking Mule Account Detection System** built for **testing, demonstration, and hackathon evaluation purposes**.

⚠️ **Important Note**
This is **NOT a production system**.
It is a **testing / experimental implementation** designed to demonstrate:

* Mule detection logic
* Transaction graph analysis
* Scenario-based risk scoring
* Visual investigation workflows
* Compliance reporting concepts

A **real production system** would require:

* Bank-grade data pipelines
* Real-time streaming systems (Kafka)
* Advanced ML models
* Strong authentication & RBAC
* Regulatory approvals

---

## 🎯 What This PoC Demonstrates

### ✔ Core Capabilities

* Detects **potential mule accounts** using **rule-based scenarios**
* Handles **multi-account money flow**
* Supports **cycle / loop detection**
* Calculates **mule risk score**
* Flags suspicious accounts
* Stores alerts in SQLite
* Generates **SAR (Suspicious Activity Reports)**
* Provides **LLM-based explanations** (DeepSeek / OpenAI-compatible)
* Visualizes transactions as **interactive graphs**
* Drill-down investigation per account

---

## 🧠 Mule Scenarios Implemented (Rule-Based)

This PoC implements **10 core mule detection scenarios**, including:

1. High daily outgoing volume
2. Multiple unique beneficiary accounts
3. Rapid round-trip transfers
4. High transaction count
5. Repeated same-amount transfers
6. Cross-channel fund movement
7. Short time-window bursts
8. Funnel behavior (many → one)
9. Fan-out behavior (one → many)
10. Circular money flow (cycles)

> These are **heuristic rules**, not ML models.

---

## 📂 Project Structure

```
bank-mule-live-dashboard/
│
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── .env                      # API keys (local only, NOT committed)
├── style.css                 # Banking-style UI
│
├── data/
│   └── transactions.csv      # Transaction data (auto-appended)
│
├── db/
│   └── mule.db               # SQLite DB (auto-created)
│
├── core/
│   ├── ingestion.py          # CSV loader (microseconds-safe)
│   ├── csv_generator.py      # Adds new records every 5 minutes
│   ├── database.py           # SQLite helpers
│   ├── scenarios.py          # Mule scenarios
│   ├── scoring.py            # Mule score calculation
│   ├── cycles.py             # Cycle detection
│   ├── graphs.py             # Interactive Plotly graphs
│   ├── alert_history.py      # Alert storage
│   ├── sar_export.py         # SAR CSV / PDF export
│   └── llm.py                # LLM explanation logic
│
└── README.md
```

---

## 📊 Input Data Format (CSV)

The system **expects exactly this CSV structure**:

```
SourceAccount,TargetAccount,Channel,Amount,Timestamp
ACC_003,ACC_028,UPI,20247,2026-02-28 02:04:49.013980
```

### Rules

* `Amount` → **Always rounded (e.g., 2004.0)**
* `Timestamp` → Supports **with or without microseconds**
* Accounts → Format like `ACC_001`, `ACC_002`, etc.

---

## 🔄 Dynamic Data Behavior

* The system **automatically appends new synthetic records** every **5 minutes**
* After new records are added:

  * Mule scores are recalculated
  * Graphs update automatically
  * Alerts are logged in SQLite
* No user input is required for refresh

---

## 🖥️ How to Run Locally

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 2️⃣ Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Create `.env` File

Create a file named `.env` in the project root:

```env
LLM_API_KEY=your_api_key_here
LLM_API_URL=https://api.deepseek.com/v1/chat/completions
```

> `.env` is required **only for LLM explanations**
> The app will still run without it.

---

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

The dashboard will open automatically in your browser.

---

## ☁️ Deployment (Streamlit Cloud)

### Steps

1. Push code to GitHub
2. **Do NOT commit `.env`**
3. In **Streamlit Cloud → App Settings → Secrets**, add:

```toml
LLM_API_KEY="your_api_key_here"
LLM_API_URL="https://api.deepseek.com/v1/chat/completions"
```

4. Deploy

---

## 🧪 Testing vs Real System

### This PoC:

* Rule-based logic
* Synthetic / CSV-based data
* SQLite storage
* UI-focused demonstration

### Real Banking System Would Require:

* Real transaction feeds
* Distributed databases
* Machine learning models
* Model governance & explainability
* Role-based access (RBAC)
* Regulatory compliance (AML / FATF / RBI / FinCEN)

---

## 🏆 Hackathon Readiness

This project is designed to:

* Clearly explain **AML mule detection concepts**
* Impress judges with **visual investigation workflows**
* Demonstrate **end-to-end thinking**
* Show how AI (LLM) can assist compliance teams

---

## 📌 Disclaimer

This project is for **educational, research, and demonstration purposes only**.
It **must not** be used for real financial decision-making.

---

If you want:

* RBAC (Analyst / Compliance Officer)
* Kafka-style real-time simulation
* ML-based anomaly detection
* Production-grade architecture diagram

You can extend this PoC further.

---

✅ **End of README**
