# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

import unittest
from frappe_semantic_rag.controllers.base_controller import EnterpriseBaseController
from frappe_semantic_rag.controllers.workflow_handler import WorkflowStateMachine
from frappe_semantic_rag.services.integration_service import EnterpriseIntegrationService
from frappe_semantic_rag.services.validator import EnterpriseValidationEngine
from frappe_semantic_rag.tasks import hourly_sync, daily_reconciliation, weekly_digest
from frappe_semantic_rag import api
from frappe_semantic_rag.frappe_semantic_rag_core.doctype.frappe_semantic_rag_entry.frappe_semantic_rag_entry import FrappeSemanticRagEntry
from frappe_semantic_rag.frappe_semantic_rag_core.doctype.frappe_semantic_rag_item.frappe_semantic_rag_item import FrappeSemanticRagItem
from frappe_semantic_rag.frappe_semantic_rag_core.doctype.frappe_semantic_rag_settings.frappe_semantic_rag_settings import FrappeSemanticRagSettings
from frappe_semantic_rag.frappe_semantic_rag_core.doctype.frappe_semantic_rag_audit_log.frappe_semantic_rag_audit_log import FrappeSemanticRagAuditLog
from frappe_semantic_rag.frappe_semantic_rag_core.report.frappe_semantic_rag_summary.frappe_semantic_rag_summary import execute as run_report

class TestEnterpriseArchitectureV16(unittest.TestCase):
    def setUp(self):
        self.entry = FrappeSemanticRagEntry()
        self.entry.title = "Test Frappe v16 Vector Search & Semantic RAG Copilot v16"
        self.entry.party = "Alpha Enterprise Global"
        self.entry.status = "Draft"

        item1 = FrappeSemanticRagItem()
        item1.item_code = "METRIC-001"
        item1.qty = 10.0
        item1.rate = 1200.0
        item1.validate()

        item2 = FrappeSemanticRagItem()
        item2.item_code = "METRIC-002"
        item2.qty = 5.0
        item2.rate = 2400.0
        item2.validate()

        self.entry.items = [item1, item2]

    def test_v16_multi_doctype_aggregation(self):
        self.entry.validate()
        self.assertEqual(self.entry.total_qty, 15.0)
        self.assertEqual(self.entry.total_amount, 24000.0)
        self.assertEqual(self.entry.grand_total, 24000.0)

    def test_v16_submission_and_cancellation(self):
        self.entry.validate()
        self.entry.on_submit()
        self.assertEqual(self.entry.status, "Submitted")
        self.assertEqual(self.entry.audit_status, "Compliant")

        self.entry.on_cancel()
        self.assertEqual(self.entry.status, "Cancelled")
        self.assertEqual(self.entry.audit_status, "Flagged")

    def test_v16_workflow_state_machine(self):
        self.assertTrue(WorkflowStateMachine.apply_transition(self.entry, "Pending Review"))
        self.assertEqual(self.entry.status, "Pending Review")
        self.assertTrue(WorkflowStateMachine.apply_transition(self.entry, "Approved"))
        self.assertEqual(self.entry.status, "Approved")

    def test_v16_settings_single_doctype(self):
        settings = FrappeSemanticRagSettings()
        settings.batch_size = 250
        settings.validate()
        res = settings.test_connection()
        self.assertEqual(res["status"], "success")

    def test_v16_tamper_proof_audit_log(self):
        audit = FrappeSemanticRagAuditLog()
        audit.reference_doctype = "Frappe v16 Vector Search & Semantic RAG Copilot Entry"
        audit.reference_name = "TEST-V16-REF-001"
        audit.action = "Submitted"
        audit.before_insert()
        self.assertIsNotNone(audit.checksum_hash)
        self.assertEqual(len(audit.checksum_hash), 64)

    def test_v16_script_report_execution(self):
        columns, data, message, chart, summary = run_report()
        self.assertTrue(len(columns) >= 5)
        self.assertTrue(len(data) >= 1)
        self.assertIsNotNone(chart)
        self.assertTrue(len(summary) >= 2)

    def test_v16_api_endpoints(self):
        ping_res = api.ping()
        self.assertEqual(ping_res["status"], "ok")
        self.assertEqual(ping_res["frappe_version"], "16.0.0")

        overview = api.get_status_overview()
        self.assertEqual(overview["operational_status"], "V16_ONLINE")
        self.assertEqual(len(overview["doctypes"]), 4)

    def test_v16_scheduler_background_tasks(self):
        self.assertEqual(hourly_sync()["status"], "COMPLETED")
        self.assertEqual(daily_reconciliation()["status"], "VERIFIED_100_PERCENT")
        self.assertEqual(weekly_digest()["status"], "DISPATCHED")

if __name__ == "__main__":
    unittest.main()
