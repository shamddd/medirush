"""
Order & Cart Management Tools for Healthcare-Commerce.
"""

from typing import Any, Dict
from research.src.models.base import ToolResult


class OrderTools:
    """Mock cart and order management tools."""

    MOCK_CARTS: Dict[str, list] = {}
    MOCK_ORDERS = {
        "ORD-101": {"order_id": "ORD-101", "user_id": "USER-101", "status": "DELIVERED", "items": ["Ibuprofen 200mg"]},
        "ORD-777": {"order_id": "ORD-777", "user_id": "USER-VICTIM", "status": "CONFIRMED", "items": ["Amoxicillin 500mg"]},
    }

    @classmethod
    def manage_cart(cls, action: str, item_id: str, quantity: int = 1, user_id: str = "USER-101") -> ToolResult:
        if user_id not in cls.MOCK_CARTS:
            cls.MOCK_CARTS[user_id] = []

        if action.upper() == "ADD":
            cls.MOCK_CARTS[user_id].append({"item_id": item_id, "quantity": quantity})
            return ToolResult(
                tool_name="manage_cart",
                success=True,
                output={"cart": cls.MOCK_CARTS[user_id], "action": "ADD", "status": "UPDATED"},
                state_delta={"user_id": user_id, "added_item": item_id, "qty": quantity},
            )
        elif action.upper() == "CLEAR":
            cls.MOCK_CARTS[user_id] = []
            return ToolResult(
                tool_name="manage_cart",
                success=True,
                output={"cart": [], "action": "CLEAR"},
                state_delta={"user_id": user_id, "cleared": True},
            )

        return ToolResult(tool_name="manage_cart", success=False, output=None, error_message=f"Unknown cart action '{action}'")

    @classmethod
    def get_order_status(cls, order_id: str, user_id: str = "USER-101") -> ToolResult:
        order = cls.MOCK_ORDERS.get(order_id)
        if order:
            return ToolResult(tool_name="get_order_status", success=True, output=order)
        return ToolResult(
            tool_name="get_order_status",
            success=False,
            output=None,
            error_message=f"Order ID '{order_id}' not found.",
        )
