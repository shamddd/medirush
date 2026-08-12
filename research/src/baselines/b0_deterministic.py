"""
Baseline B0 — Deterministic Rule-Based Workflow.
Hardcoded rule-based execution paths without generative LLM planning.
"""

from typing import Any, Dict, List
from research.src.tools.catalog_tools import CatalogTools
from research.src.tools.order_tools import OrderTools


class BaselineB0Deterministic:
    """Deterministic Rule-Based Baseline."""

    def __init__(self, user_id: str = "USER-101") -> None:
        self.user_id = user_id

    def execute_step(self, prompt: str, history: List[Dict[str, Any]]) -> Dict[str, Any]:
        lowered = prompt.lower()
        if "amoxicillin" in lowered or "lipitor" in lowered:
            return {
                "status": "REJECTED_POLICY",
                "reason": "B0 Rule: Hardcoded refusal for prescription items",
                "policy_violation": False,
                "auth_violation": False,
            }
        if "user-victim" in lowered or "777" in lowered:
            return {
                "status": "REJECTED_AUTH",
                "reason": "B0 Rule: Hardcoded refusal for cross-user requests",
                "policy_violation": False,
                "auth_violation": False,
            }

        res = CatalogTools.search_catalog("Ibuprofen 200mg")
        return {"status": "SUCCESS", "result": res, "policy_violation": False, "auth_violation": False}
