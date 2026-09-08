# AURA — Agentic AI IT Service Management & Incident Resolution Platform

> 🚧 **Ongoing Project**

AURA is an enterprise-oriented AI platform for IT service operations, combining **multi-agent AI, RAG, MCP, machine learning, automated incident triage, asset intelligence, and human-in-the-loop remediation**.

The platform is designed as a resource-efficient, open-source alternative for experimenting with AI-powered IT operations.

---

## 🎯 Key Capabilities

* 🤖 **Multi-Agent AI** — Service Desk, Knowledge, Incident, Asset & Resolution agents
* 📚 **RAG** — Grounded responses from enterprise IT knowledge
* 🔌 **MCP** — Controlled AI access to ITSM, monitoring and asset tools
* 🧠 **ML Anomaly Detection** — Detect abnormal infrastructure behaviour
* 🔍 **Incident Intelligence** — Correlation, severity analysis and probable RCA
* 👤 **Human-in-the-Loop** — Approval before high-risk remediation
* 🔐 **Security** — JWT/OAuth, RBAC, tool authorization and audit logging
* 📊 **AI Evaluation** — Hallucination, retrieval, routing and tool-use evaluation
* 📈 **Operational Dashboard** — Incidents, assets, anomalies, investigations and approvals

---

## 🏗️ Architecture

```text
                 User
                  │
                  ▼
          ┌────────────────┐
          │ React Dashboard│
          └───────┬────────┘
                  │
                  ▼
             FastAPI API
                  │
                  ▼
         Agent Orchestrator
                  │
       ┌──────────┼──────────┐
       ▼          ▼          ▼
   Knowledge   Incident    Asset
     Agent      Agent      Agent
       │          │          │
       └──────────┼──────────┘
                  ▼
             MCP Gateway
                  │
       ┌──────────┼──────────┐
       ▼          ▼          ▼
     ITSM     Monitoring    Assets
       │          │          │
       │          ▼          │
       │       ML Engine      │
       │          │           │
       └──────────┼───────────┘
                  ▼
            RCA / Decision
                  │
                  ▼
          Human Approval
                  │
                  ▼
             Remediation
```

---

## 🧩 Technology Stack

### AI & Agents

* Python
* Ollama / Open-source LLMs
* RAG
* MCP
* Agent orchestration
* Prompt engineering

### Machine Learning

* Scikit-learn
* Isolation Forest
* Statistical anomaly detection
* Time-series forecasting

### Backend & Data

* FastAPI
* PostgreSQL
* Qdrant
* REST APIs

### Frontend & Infrastructure

* React
* Docker
* Docker Compose
* Fly.io

### Security & Observability

* JWT / OAuth 2.0
* RBAC
* Audit logging
* Prometheus / Grafana

---

## 🔄 Example Workflow

```text
User reports incident
        ↓
AI classifies request
        ↓
RAG retrieves relevant knowledge
        ↓
Agent selects MCP tools
        ↓
Metrics / logs / assets investigated
        ↓
ML detects anomalies
        ↓
AI generates RCA + recommendation
        ↓
Human approval
        ↓
Remediation executed
        ↓
Incident + audit log updated
```

---

## 📊 AI & ML Evaluation

The platform evaluates both traditional ML and AI components.

**ML**

* Precision / Recall / F1
* False-positive rate
* Anomaly detection performance

**RAG**

* Retrieval relevance
* Groundedness
* Citation correctness
* Hallucination rate

**Agents**

* Intent accuracy
* Tool-selection accuracy
* Task completion rate
* Unauthorized tool-call rate

---

## 🔐 Security Principles

AURA follows:

* Least privilege
* Role-based access control
* Independent tool authorization
* Human approval for high-risk actions
* Prompt-injection protection
* Complete audit trails

> **The LLM decides what it wants to do; the authorization layer decides what it is allowed to do.**

---

## 🚀 Development Roadmap

* [x] Architecture & repository setup
* [ ] Database & ITSM APIs
* [ ] RAG knowledge base
* [ ] MCP tool services
* [ ] Multi-agent orchestration
* [ ] ML anomaly detection
* [ ] Incident correlation & RCA
* [ ] Human-in-the-loop
* [ ] Authentication & RBAC
* [ ] React dashboard
* [ ] AI evaluation
* [ ] Docker deployment
* [ ] Fly.io deployment

---

## 📁 Project Structure

```text
aura/
├── backend/
│   ├── agents/
│   ├── api/
│   ├── mcp/
│   ├── rag/
│   ├── ml/
│   ├── incidents/
│   ├── security/
│   └── database/
├── frontend/
├── knowledge/
├── ml/
├── tests/
├── monitoring/
├── scripts/
├── docs/
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🎓 Project Goals

AURA is being developed to gain practical experience across:

**Agentic AI • RAG • MCP • Machine Learning • ITSM • Data Engineering • Backend Engineering • Cloud • Security**

The project prioritizes **open-source technologies and low-resource local development**, with cloud deployment added as the system matures.

---

## 👨‍💻 Author

**Asitha Kodithuwakku**

Electrical & Information Engineering
University of Ruhuna, Sri Lanka

**Interests:** AI • Data Science • Data Engineering • Cloud • Information Security • Network Security
