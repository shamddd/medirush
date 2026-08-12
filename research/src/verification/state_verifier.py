"""
Post-Execution State Verification Engine.
Validates side-effects and state deltas following tool execution.
"""

from typing import Any, Dict
from research.src.models.base import StateVerificationVerdict, ToolCall, ToolResult


class StateVerifier:
    """Verifies environment state integrity post-tool execution."""

    @classmethod
    def verify_post_state(cls, tool_call: ToolCall, result: ToolResult) -> StateVerificationVerdict:
        if not result.success:
            return StateVerificationVerdict(is_valid=True)  # Tool failed cleanly

        tool_name = tool_call.tool_name
        args = tool_call.arguments
        delta = result.state_delta

        # Verification Rule 1: Cart Add Verification
        if tool_name == "manage_cart" and args.get("action", "").upper() == "ADD":
            expected_item = args.get("item_id")
            actual_added = delta.get("added_item")
            if expected_item != actual_added:
                return StateVerificationVerdict(
                    is_valid=False,
                    mismatch_details=f"State Mismatch: Requested item '{expected_item}' does not match actual cart delta item '{actual_added}'.",
                )

        return StateVerificationVerdict(is_valid=True)
