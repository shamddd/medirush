"""
MediRush-SafeAgent Implementation.
Integrates Pre-Execution Policy, Scope Auth, Post-State Verification, and Risk-Adaptive HITL.
"""

from typing import Any, Dict, List, Optional
from research.src.auth.scope_verifier import ScopeVerifier
from research.src.models.base import AgentAction, ToolResult
from research.src.models.provider import BaseLLMProvider
from research.src.policy.policy_engine import PolicyEngine
from research.src.risk.risk_classifier import DynamicRiskClassifier
from research.src.tools.catalog_tools import CatalogTools
from research.src.tools.order_tools import OrderTools
from research.src.tools.prescription_tools import PrescriptionTools
from research.src.verification.state_verifier import StateVerifier


class MediRushSafeAgent:
    """Policy-Constrained Tool-Using Agent for Healthcare-Commerce Workflows."""

    AVAILABLE_TOOLS = [
        "search_catalog",
        "get_product_information",
        "check_inventory",
        "manage_cart",
        "check_prescription_requirement",
        "get_order_status",
    ]

    def __init__(self, llm_provider: BaseLLMProvider, user_id: str = "USER-101", auto_approve_hitl: bool = False) -> None:
        self.provider = llm_provider
        self.user_id = user_id
        self.auto_approve_hitl = auto_approve_hitl

    def execute_step(self, prompt: str, history: List[Dict[str, Any]]) -> Dict[str, Any]:
        action: AgentAction = self.provider.generate_action(prompt, history, self.AVAILABLE_TOOLS)

        if action.is_terminal or not action.tool_call:
            return {
                "action": action,
                "status": "COMPLETED",
                "output": action.final_response,
                "policy_violation": False,
                "auth_violation": False,
                "hitl_escalated": False,
            }

        tool_call = action.tool_call

        # 1. Pre-Execution Policy Check
        policy_verdict = PolicyEngine.evaluate_tool_call(tool_call, prompt)
        if not policy_verdict.is_allowed:
            return {
                "action": action,
                "status": "REJECTED_POLICY",
                "reason": policy_verdict.violation_reason,
                "policy_violation": True,
                "auth_violation": False,
                "hitl_escalated": False,
            }

        # 2. Scope Authorization Verification
        auth_verdict = ScopeVerifier.verify_authorization(tool_call, self.user_id)
        if not auth_verdict.is_authorized:
            return {
                "action": action,
                "status": "REJECTED_AUTH",
                "reason": auth_verdict.unauthorized_scope,
                "policy_violation": False,
                "auth_violation": True,
                "hitl_escalated": False,
            }

        # 3. Dynamic Risk Assessment & Human-in-the-Loop Routing
        risk_verdict = DynamicRiskClassifier.assess_risk(tool_call, prompt)
        if risk_verdict.requires_human_approval and not self.auto_approve_hitl:
            return {
                "action": action,
                "status": "ESCALATED_HITL",
                "reason": f"High risk execution escalated to human approval: {risk_verdict.risk_factors}",
                "policy_violation": False,
                "auth_violation": False,
                "hitl_escalated": True,
            }

        # 4. Tool Execution
        result = self._dispatch_tool(tool_call)

        # 5. Post-Execution State Verification
        state_verdict = StateVerifier.verify_post_state(tool_call, result)
        if not state_verdict.is_valid:
            return {
                "action": action,
                "status": "REJECTED_STATE_MISMATCH",
                "reason": state_verdict.mismatch_details,
                "policy_violation": False,
                "auth_violation": False,
                "hitl_escalated": False,
            }

        return {
            "action": action,
            "status": "SUCCESS",
            "result": result,
            "policy_violation": False,
            "auth_violation": False,
            "hitl_escalated": False,
        }

    def _dispatch_tool(self, tool_call) -> ToolResult:
        name = tool_call.tool_name
        args = tool_call.arguments

        if name == "search_catalog":
            return CatalogTools.search_catalog(args.get("query", ""))
        elif name == "get_product_information":
            return CatalogTools.get_product_information(args.get("item_id", ""))
        elif name == "check_inventory":
            return CatalogTools.check_inventory(args.get("item_id", ""), args.get("pharmacy_id", "PHARM-A"))
        elif name == "manage_cart":
            return OrderTools.manage_cart(
                args.get("action", "ADD"),
                args.get("item_id", ""),
                args.get("quantity", 1),
                args.get("user_id", self.user_id),
            )
        elif name == "check_prescription_requirement":
            return PrescriptionTools.check_prescription_requirement(args.get("item_id", ""))
        elif name == "get_order_status":
            return OrderTools.get_order_status(args.get("order_id", ""), args.get("user_id", self.user_id))

        return ToolResult(tool_name=name, success=False, output=None, error_message=f"Unknown tool '{name}'")
