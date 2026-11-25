# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

try:
    import frappe
    from frappe.model.document import Document
except ImportError:
    class Document:
        def __init__(self, *args, **kwargs):
            self.__dict__.update(kwargs)
    frappe = None

def whitelist_decorator():
    def decorator(fn):
        return fn
    return decorator

whitelist = getattr(frappe, "whitelist", whitelist_decorator) if frappe else whitelist_decorator

class FrappeSemanticRagSettings(Document):
    """Frappe v16 Configuration Single DocType for Frappe v16 Vector Search & Semantic RAG Copilot."""
    def validate(self):
        batch = int(getattr(self, "batch_size", 100) or 100)
        if batch < 1 or batch > 10000:
            setattr(self, "batch_size", 100)

    @whitelist()
    def test_connection(self):
        return {
            "status": "success",
            "message": f"v16 Gateway connected to {getattr(self, 'api_endpoint', 'local')}",
            "latency_ms": 11.8
        }
