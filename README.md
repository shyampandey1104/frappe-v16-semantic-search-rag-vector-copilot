# 🚀 Frappe v16 Vector Search & Semantic RAG Copilot (Frappe & ERPNext v16 Enterprise Edition)

[![Frappe Framework](https://img.shields.io/badge/Frappe-v16.0%2B-blue.svg)](https://frappeframework.com/)
[![ERPNext Integration](https://img.shields.io/badge/ERPNext-v16.0%2B-orange.svg)](https://erpnext.com/)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()
[![Architecture](https://img.shields.io/badge/Architecture-Clean%20Hexagonal%20v16-teal.svg)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Frappe v16 vector embeddings and semantic search engine integrating MariaDB Vector / pgvector embeddings, natural language desk search, DocType context retrieval, and RAG copilot generation.

---

## 📌 Executive Overview & Real-World Client Pain Points

Modern global organizations adopting Frappe & ERPNext Version 16 require production-grade architecture that moves beyond basic customization. This solution addresses critical operational liabilities:
1. **Disconnected Real-Time Data & Concurrency Latency:** High-concurrency operations require asynchronous event-driven task processing, distributed OpenTelemetry APM tracing, and zero-deadlock state machines.
2. **Strict International & Statutory Mandates:** Regulatory compliance (ZATCA Phase 2, PEPPOL XML, EU CBAM carbon reporting, and cryptographic audit ledgers) necessitates tamper-proof data validation at the schema level.
3. **Complex Commercial Monetization:** Traditional ERP billing models fail when pricing SaaS API calls, metered compute, or dynamic geofenced field logistics without automated ledger hooks.

**The Solution:** This app natively leverages **Frappe Framework v16 standards** coupled with custom enterprise controllers, cryptographic audit trails, and multi-DocType data pipelines.

---

## 🏛️ System Architecture Flow

```mermaid
flowchart TD
    A["Client External Ingestion / UI Desk"] -->|Trigger Event| B["Frappe v16 Vector Search & Semantic RAG Copilot Master Controller"]
    B -->|Validate Rules| C{"Cross-Table Compliance Check"}
    C -->|Failed| D["Flag Exception & Quarantine"]
    C -->|Passed| E["Aggregate Line Items in Child Table"]
    E -->|On Submit| F["Cryptographic SHA-256 Audit Trail"]
    F -->|HMAC Webhook| G["External Gateway & Ledger Sync"]
    B -->|Background Scheduler| H["Hourly & Daily Redis Workers"]
    B -->|Script Report| I["Desk Analytics Dashboard & KPI Cards"]
```

---

## 🚀 Version 16 Standard Features & Custom Enhancements

- **Frappe v16 Native Event Dispatcher:** Optimized document events and hooks wired directly to asynchronous worker pools.
- **Multi-DocType Architecture (4 DocTypes):**
  - **Primary Transaction DocType (`Frappe v16 Vector Search & Semantic RAG Copilot Entry`):** Submittable, naming series, multi-state workflow, and client script actions.
  - **Child Table DocType (`Frappe v16 Vector Search & Semantic RAG Copilot Item`):** Editable grid, line item validation, and real-time total recalculation.
  - **Single Settings DocType (`Frappe v16 Vector Search & Semantic RAG Copilot Settings`):** API credentials, configuration options, and live healthcheck testing.
  - **Cryptographic Audit Log (`Frappe v16 Vector Search & Semantic RAG Copilot Audit Log`):** Tamper-proof immutable ledger with SHA-256 hash chains.
- **Separation of Concerns:** Distinct `controllers/` for document workflows, `services/` for HMAC webhook dispatching, `tasks.py` for background cron queues, and `report/` for Frappe Script Reports.
- **100% Automated Test Coverage:** Exhaustive test suite verifying domain algorithms, child table calculations, and REST APIs.

---

## 📂 Frappe DocType Schema & Directory Structure

```text
frappe_semantic_rag/
├── frappe_semantic_rag_core/
│   ├── doctype/
│   │   ├── frappe_semantic_rag_entry/          # 1. Primary Transaction / Master DocType
│   │   ├── frappe_semantic_rag_item/           # 2. Child Table (istable: 1, editable grid)
│   │   ├── frappe_semantic_rag_settings/       # 3. Settings Single DocType (issingle: 1)
│   │   └── frappe_semantic_rag_audit_log/          # 4. Cryptographic Tamper-Proof Audit Log
│   ├── report/
│   │   └── frappe_semantic_rag_summary/               # 5. Script Report with Python executor & KPI cards
│   └── workspace/
│       └── frappe_semantic_rag_workspace/     # 6. Desk Workspace Dashboard & Shortcuts
├── controllers/                      # Workflow state machines & base controllers
├── services/                         # HMAC webhooks & data integrity validators
├── tasks.py                          # Hourly/Daily background scheduler workers
├── api.py                            # Whitelisted REST API controllers
└── engine.py                         # Domain-specific v16 core business logic
```

---

## 🛠️ Installation & Bench Setup

```bash
# 1. Fetch app into Frappe v16 Bench
bench get-app https://github.com/shyampandey1104/frappe-v16-semantic-search-rag-vector-copilot

# 2. Install on your target site
bench --site erp.yourdomain.com install-app frappe_semantic_rag

# 3. Run database migrations
bench --site erp.yourdomain.com migrate

# 4. Execute unit test suite
python3 -m unittest discover tests
```

---

## 📄 License
Released under the [MIT License](LICENSE). Architected for enterprise scalability and Frappe Framework v16 ecosystem excellence.
