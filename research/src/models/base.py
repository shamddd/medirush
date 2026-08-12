"""
Base Data Models for MediRush Research System.
"""

from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class RiskLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class ToolCall(BaseModel):
    tool_name: str
    arguments: Dict[str, Any] = Field(default_factory=dict)
    call_id: Optional[str] = None


class ToolResult(BaseModel):
    tool_name: str
    success: bool
    output: Any
    error_message: Optional[str] = None
    state_delta: Dict[str, Any] = Field(default_factory=dict)


class AgentAction(BaseModel):
    thought: str
    tool_call: Optional[ToolCall] = None
    final_response: Optional[str] = None
    is_terminal: bool = False


class PolicyVerdict(BaseModel):
    is_allowed: bool
    violation_reason: Optional[str] = None
    required_mitigation: Optional[str] = None


class AuthVerdict(BaseModel):
    is_authorized: bool
    unauthorized_scope: Optional[str] = None


class StateVerificationVerdict(BaseModel):
    is_valid: bool
    mismatch_details: Optional[str] = None


class RiskAssessmentVerdict(BaseModel):
    risk_level: RiskLevel
    requires_human_approval: bool
    risk_factors: List[str] = Field(default_factory=list)
