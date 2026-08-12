"""
Dynamic Risk Assessment Classifier.
Evaluates workflow risk level and determines human-in-the-loop escalation routing.
"""

from typing import List
from research.src.models.base import RiskAssessmentVerdict, RiskLevel, ToolCall
from research.src.tools.catalog_tools import CatalogTools


class DynamicRiskClassifier:
    """Classifies execution risk vectors and routes high-risk tasks to human approval."""

    @classmethod
    def assess_risk(cls, tool_call: ToolCall, context_prompt: str) -> RiskAssessmentVerdict:
        risk_factors: List[str] = []

        tool_name = tool_call.tool_name
        args = tool_call.arguments

        # Factor 1: Prescription Item Involvement
        if tool_name == "manage_cart":
            item_id = args.get("item_id", "")
            item_info = CatalogTools.MOCK_CATALOG.get(item_id, {})
            if item_info.get("requires_prescription", False):
                risk_factors.append("Prescription drug order modification")

        # Factor 2: High Dollar Value / Quantity
        if tool_name == "manage_cart" and args.get("quantity", 1) >= 5:
            risk_factors.append("High volume item order")

        # Factor 3: User Order Retrieval / Sensitive Access
        if tool_name == "get_order_status":
            risk_factors.append("Order PII lookup")

        # Determine Risk Level
        if len(risk_factors) >= 2 or "Prescription drug order modification" in risk_factors:
            level = RiskLevel.HIGH
            requires_hitl = True
        elif len(risk_factors) == 1:
            level = RiskLevel.MEDIUM
            requires_hitl = False
        else:
            level = RiskLevel.LOW
            requires_hitl = False

        return RiskAssessmentVerdict(
            risk_level=level,
            requires_human_approval=requires_hitl,
            risk_factors=risk_factors,
        )
