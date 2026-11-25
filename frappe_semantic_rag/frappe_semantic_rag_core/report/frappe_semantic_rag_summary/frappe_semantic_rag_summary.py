# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

def execute(filters=None):
    columns = [
        {"fieldname": "name", "label": "Record ID", "fieldtype": "Link", "options": "Frappe v16 Vector Search & Semantic RAG Copilot Entry", "width": 180},
        {"fieldname": "posting_date", "label": "Date", "fieldtype": "Date", "width": 120},
        {"fieldname": "party", "label": "Party", "fieldtype": "Data", "width": 180},
        {"fieldname": "grand_total", "label": "Total Amount", "fieldtype": "Currency", "width": 150},
        {"fieldname": "status", "label": "Status", "fieldtype": "Data", "width": 120},
        {"fieldname": "audit_status", "label": "v16 Audit", "fieldtype": "Data", "width": 120}
    ]
    data = [
        {"name": "FRAPP-V16-0001", "posting_date": "2026-04-01", "party": "Global Enterprise Alpha", "grand_total": 54000.0, "status": "Submitted", "audit_status": "Compliant"},
        {"name": "FRAPP-V16-0002", "posting_date": "2026-04-02", "party": "National Industrial Beta", "grand_total": 82000.0, "status": "Submitted", "audit_status": "Compliant"}
    ]
    chart = {
        "data": {"labels": [r["name"] for r in data], "datasets": [{"name": "Valuation", "values": [r["grand_total"] for r in data]}]},
        "type": "bar",
        "colors": ["#2490EF"]
    }
    summary = [
        {"value": sum(r["grand_total"] for r in data), "label": "Total v16 Portfolio Value", "datatype": "Currency"},
        {"value": len(data), "label": "Active Records", "datatype": "Int"}
    ]
    return columns, data, None, chart, summary
