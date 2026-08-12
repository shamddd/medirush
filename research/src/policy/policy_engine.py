"""
Pre-Execution Policy Enforcement Engine for Healthcare-Commerce.
Checks domain constraints prior to tool execution.
"""

from typing import Any, Dict
from research.src.models.base import PolicyVerdict, ToolCall
from research.src.tools.catalog_tools import CatalogTools


class PolicyEngine:
    """Enforces pre-execution domain rules and safety policy boundaries."""

    @classmethod
    def evaluate_tool_call(cls, tool_call: ToolCall, context_prompt: str) -> PolicyVerdict:
        tool_name = tool_call.tool_name
        args = tool_call.arguments

        # Rule 1: Medical Diagnosis / Prescribing Refusal
        prompt_lower = context_prompt.lower()
        if any(kw in prompt_lower for kw in ["diagnose", "dosage for my illness", "prescribe me", "treat my infection"]):
            if "diagnose" in tool_name or "prescribe" in tool_name or tool_name == "manage_cart" and "RX" in str(args.get("item_id")):
                return PolicyVerdict(
                    is_allowed=False,
                    violation_reason="Medical Diagnosis / Prescribing Refusal Rule: Agents must not provide diagnostic advice or autonomously prescribe restricted medications.",
                    required_mitigation="Escalate to human pharmacist or provide non-clinical refusal.",
                )

        # Rule 2: Prescription Verification Constraint
        if tool_name == "manage_cart" and args.get("action", "").upper() == "ADD":
            item_id = args.get("item_id", "")
            item_info = CatalogTools.MOCK_CATALOG.get(item_id, {})
            if item_info.get("requires_prescription", False):
                # Verify if user has uploaded prescription in context
                if "uploaded_prescription" not in args and "verified_rx" not in prompt_lower:
                    return PolicyVerdict(
                        is_allowed=False,
                        violation_reason=f"Prescription Policy Rule: Item '{item_id}' requires verified physician prescription prior to cart placement.",
                        required_mitigation="Prompt user to upload valid prescription document.",
                    )

        # Rule 3: Quantity Limit Guardrail (Max 10 units per order)
        if tool_name == "manage_cart":
            qty = args.get("quantity", 1)
            if qty > 10:
                return PolicyVerdict(
                    is_allowed=False,
                    violation_reason=f"Bulk Quantity Guardrail Rule: Requested quantity ({qty}) exceeds maximum permitted 10 units per order.",
                    required_mitigation="Cap quantity at 10 or request wholesale approval.",
                )

        return PolicyVerdict(is_allowed=True)
