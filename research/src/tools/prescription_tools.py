"""
Prescription Requirement Tools for Healthcare-Commerce.
"""

from research.src.models.base import ToolResult
from research.src.tools.catalog_tools import CatalogTools


class PrescriptionTools:
    """Mock prescription requirement tools."""

    @classmethod
    def check_prescription_requirement(cls, item_id: str) -> ToolResult:
        item = CatalogTools.MOCK_CATALOG.get(item_id)
        if item:
            requires_rx = item.get("requires_prescription", False)
            return ToolResult(
                tool_name="check_prescription_requirement",
                success=True,
                output={
                    "item_id": item_id,
                    "item_name": item["name"],
                    "requires_prescription": requires_rx,
                    "policy_rule": "Valid licensed physician prescription required prior to checkout" if requires_rx else "OTC - No prescription required",
                },
            )
        return ToolResult(
            tool_name="check_prescription_requirement",
            success=False,
            output=None,
            error_message=f"Item ID '{item_id}' not found.",
        )
