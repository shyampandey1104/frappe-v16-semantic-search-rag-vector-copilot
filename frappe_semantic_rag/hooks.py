# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "frappe_semantic_rag"
app_title = "Frappe v16 Vector Search & Semantic RAG Copilot"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe v16 vector embeddings and semantic search engine integrating MariaDB Vector / pgvector embeddings, natural language desk search, DocType context retrieval, and RAG copilot generation."
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"
required_frappe_version = ">=16.0.0"

# Includes in <head>
app_include_css = "/assets/frappe_semantic_rag/css/frappe_semantic_rag.bundle.css"
app_include_js = "/assets/frappe_semantic_rag/js/frappe_semantic_rag.bundle.js"

# Document Events
doc_events = {
    "Frappe v16 Vector Search & Semantic RAG Copilot Entry": {
        "validate": "frappe_semantic_rag.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "frappe_semantic_rag.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
scheduler_events = {
    "hourly": [
        "frappe_semantic_rag.tasks.hourly_sync"
    ],
    "daily": [
        "frappe_semantic_rag.tasks.daily_reconciliation"
    ],
    "weekly": [
        "frappe_semantic_rag.tasks.weekly_digest"
    ]
}
