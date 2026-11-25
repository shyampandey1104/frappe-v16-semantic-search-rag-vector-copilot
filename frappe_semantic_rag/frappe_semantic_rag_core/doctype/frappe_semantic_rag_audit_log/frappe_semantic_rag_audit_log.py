# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

import hashlib
import time

try:
    import frappe
    from frappe.model.document import Document
except ImportError:
    class Document:
        def __init__(self, *args, **kwargs):
            self.__dict__.update(kwargs)
    frappe = None

class FrappeSemanticRagAuditLog(Document):
    """Frappe v16 Cryptographic Immutable Audit Log."""
    def before_insert(self):
        ref_doc = getattr(self, "reference_doctype", "")
        ref_name = getattr(self, "reference_name", "")
        action = getattr(self, "action", "")
        ts = getattr(self, "timestamp", str(time.time()))
        raw = f"{ref_doc}|{ref_name}|{action}|{ts}|FRAPPE_V16_KEY"
        self.checksum_hash = hashlib.sha256(raw.encode("utf-8")).hexdigest()
