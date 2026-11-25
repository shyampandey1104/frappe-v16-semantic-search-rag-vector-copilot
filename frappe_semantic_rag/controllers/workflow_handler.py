# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

from frappe_semantic_rag.controllers.base_controller import EnterpriseBaseController

class WorkflowStateMachine:
    """Frappe v16 Event-Driven Workflow State Machine."""

    @classmethod
    def apply_transition(cls, doc, target_status: str, user: str = "Administrator") -> bool:
        current_status = getattr(doc, "status", "Draft")
        if not EnterpriseBaseController.validate_status_transition(current_status, target_status):
            raise ValueError(f"Invalid state transition from {current_status} to {target_status}")

        doc.status = target_status
        EnterpriseBaseController.audit_stamp(doc, f"V16_TRANSITION_{target_status.upper()}")
        return True
