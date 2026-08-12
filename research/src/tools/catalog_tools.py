"""
Catalog and Inventory Inspection Tools for Healthcare-Commerce.
"""

from typing import Any, Dict
from research.src.models.base import ToolResult


class CatalogTools:
    """Mock healthcare catalog tool executions."""

    MOCK_CATALOG = {
        "MED-OTC-001": {
            "name": "Ibuprofen 200mg",
            "category": "OTC",
            "price": 8.99,
            "requires_prescription": False,
            "description": "Pain reliever and fever reducer.",
        },
        "MED-OTC-002": {
            "name": "Acetaminophen 500mg",
            "category": "OTC",
            "price": 6.49,
            "requires_prescription": False,
            "description": "Pain reliever and fever reducer.",
        },
        "MED-RX-001": {
            "name": "Amoxicillin 500mg",
            "category": "Prescription Antibiotic",
            "price": 14.99,
            "requires_prescription": True,
            "description": "Prescription antibiotic medication.",
        },
        "MED-RX-002": {
            "name": "Lipitor 20mg",
            "category": "Prescription Statin",
            "price": 24.99,
            "requires_prescription": True,
            "description": "Cholesterol-lowering prescription medication.",
        },
    }

    @classmethod
    def search_catalog(cls, query: str) -> ToolResult:
        query_lower = query.lower()
        results = [
            item for item in cls.MOCK_CATALOG.values()
            if query_lower in item["name"].lower() or query_lower in item["category"].lower()
        ]
        return ToolResult(
            tool_name="search_catalog",
            success=True,
            output={"results": results, "count": len(results)},
        )

    @classmethod
    def get_product_information(cls, item_id: str) -> ToolResult:
        info = cls.MOCK_CATALOG.get(item_id)
        if info:
            return ToolResult(tool_name="get_product_information", success=True, output=info)
        return ToolResult(
            tool_name="get_product_information",
            success=False,
            output=None,
            error_message=f"Item ID '{item_id}' not found in catalog.",
        )

    @classmethod
    def check_inventory(cls, item_id: str, pharmacy_id: str = "PHARM-A") -> ToolResult:
        if item_id in cls.MOCK_CATALOG:
            stock = 45 if "OTC" in item_id else 12
            return ToolResult(
                tool_name="check_inventory",
                success=True,
                output={"item_id": item_id, "pharmacy_id": pharmacy_id, "in_stock": True, "stock_count": stock},
            )
        return ToolResult(
            tool_name="check_inventory",
            success=False,
            output=None,
            error_message=f"Item ID '{item_id}' not found.",
        )
