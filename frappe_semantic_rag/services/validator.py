# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

class EnterpriseValidationEngine:
    """Frappe v16 Cross-Table Compliance & Data Integrity Validator."""

    @staticmethod
    def validate_compliance_rules(doc) -> bool:
        items = getattr(doc, "items", []) or []
        for idx, row in enumerate(items, start=1):
            qty = float(getattr(row, "qty", 0.0) or 0.0)
            rate = float(getattr(row, "rate", 0.0) or 0.0)
            if qty < 0:
                raise ValueError(f"Row {idx}: Quantity cannot be negative in v16 ledger")
            if rate < 0:
                raise ValueError(f"Row {idx}: Rate cannot be negative in v16 ledger")
        return True
