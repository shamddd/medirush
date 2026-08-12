"""
Baseline B4 — Tool Agent + Policy Engine + Scope Authorization.
Enforces pre-execution policy and scope auth, but lacks post-state verification and dynamic HITL escalation.
"""

from typing import Any, Dict, List
from research.src.auth.scope_verifier import ScopeVerifier
from research.src.models.base import AgentAction
from research.src.models.provider import BaseLLMProvider
from research.src.policy.policy_engine import PolicyEngine
from research.src.tools.order_tools import OrderTools


class BaselineB4PolicyAuth:
    """Tool Agent + Policy Engine + Scope Authorization."""

    def __init__(self, llm_provider: BaseLLMProvider, user_id: str = "USER-101") -> None:
        self.provider = llm_provider
        self.user_id = user_id

    def execute_step(self, prompt: str, history: List[Dict[str, Any]]) -> Dict[str, Any]:
        action: AgentAction = self.provider.generate_action(prompt, history, ["all"])
        if action.is_terminal or not action.tool_call:
            return {"action": action, "status": "COMPLETED", "output": action.final_response, "policy_violation": False, "auth_violation": False}

        tool_call = action.tool_call
        pol_verdict = PolicyEngine.evaluate_tool_call(tool_call, prompt)
        if not pol_verdict.is_allowed:
            return {"action": action, "status": "REJECTED_POLICY", "reason": pol_verdict.violation_reason, "policy_violation": True, "auth_violation": False}

        auth_verdict = ScopeVerifier.verify_authorization(tool_call, self.user_id)
        if not auth_verdict.is_authorized:
            return {"action": action, "status": "REJECTED_AUTH", "reason": auth_verdict.unauthorized_scope, "policy_violation": False, "auth_violation": True}

        args = tool_call.arguments
        res = OrderTools.manage_cart(args.get("action", "ADD"), args.get("item_id", ""), args.get("quantity", 1), args.get("user_id", self.user_id))
        return {"action": action, "status": "SUCCESS", "result": res, "policy_violation": False, "auth_violation": False}
