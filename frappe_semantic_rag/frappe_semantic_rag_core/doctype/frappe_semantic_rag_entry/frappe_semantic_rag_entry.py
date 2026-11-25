# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

try:
    import frappe
    from frappe.model.document import Document
except ImportError:
    class Document:
        def __init__(self, *args, **kwargs):
            self.__dict__.update(kwargs)
            if not hasattr(self, "name"):
                self.name = "FRAPP-V16-0001"
            if not hasattr(self, "items"):
                self.items = []
        def get(self, key, default=None):
            return getattr(self, key, default)
        def set(self, key, value):
            setattr(self, key, value)
    frappe = None

from frappe_semantic_rag.controllers.base_controller import EnterpriseBaseController
from frappe_semantic_rag.services.validator import EnterpriseValidationEngine
from frappe_semantic_rag.services.integration_service import EnterpriseIntegrationService

class FrappeSemanticRagEntry(Document):
    """Frappe v16 Primary Document Controller for Frappe v16 Vector Search & Semantic RAG Copilot."""

    def validate(self):
        if not getattr(self, "title", None):
            self.title = "Frappe v16 Vector Search & Semantic RAG Copilot - " + str(getattr(self, "name", "Draft"))
        if not getattr(self, "party", None):
            self.party = "ENTERPRISE-PARTY-V16"

        self.calculate_totals()
        EnterpriseValidationEngine.validate_compliance_rules(self)

    def calculate_totals(self):
        total_qty = 0.0
        total_amount = 0.0
        for row in (getattr(self, "items", []) or []):
            qty = float(getattr(row, "qty", 0.0) or 0.0)
            rate = float(getattr(row, "rate", 0.0) or 0.0)
            amount = round(qty * rate, 2)
            if hasattr(row, "amount"):
                row.amount = amount
            elif isinstance(row, dict):
                row["amount"] = amount
            total_qty += qty
            total_amount += amount

        self.total_qty = total_qty
        self.total_amount = total_amount
        self.grand_total = total_amount

    def on_submit(self):
        self.status = "Submitted"
        self.audit_status = "Compliant"
        EnterpriseBaseController.audit_stamp(self, "V16_SUBMIT")
        EnterpriseIntegrationService.dispatch_webhook("V16_ON_SUBMIT", {
            "doctype": "Frappe v16 Vector Search & Semantic RAG Copilot Entry",
            "name": getattr(self, "name", ""),
            "grand_total": getattr(self, "grand_total", 0.0)
        })

    def on_cancel(self):
        self.status = "Cancelled"
        self.audit_status = "Flagged"
        EnterpriseBaseController.audit_stamp(self, "V16_CANCEL")
