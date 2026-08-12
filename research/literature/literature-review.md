# Literature Review — Safe, Policy-Constrained Tool Agents for Domain Workflows

**Author**: Sham Satish Thakare  
**Target Domain**: Healthcare-Commerce AI Agent Workflows  
**Date**: August 12, 2026

---

## 1. Executive Summary

As Large Language Model (LLM) agents transition from passive text generators to active task executors capable of invoking external tools (Yao et al., 2023; Schick et al., 2023), securing tool usage has emerged as a paramount challenge. In domain-specific contexts like healthcare commerce, unconstrained tool execution introduces severe risks: unauthorized order placements, prescription policy bypasses, cross-user data leakage, and vulnerability to indirect prompt injections (Debenedetti et al., 2024; Ruan et al., 2024).

This literature review synthesizes recent state-of-the-art frameworks (2023–2026) in LLM agent safety, runtime policy enforcement, privilege control, and tool-use evaluation.

---

## 2. Taxonomy of Related Work

### 2.1 Tool-Calling LLM Agents & Foundations
- **ReAct (Yao et al., ICLR 2023)**: Formalized the interleaving of reasoning traces ("Thoughts") and domain actions ("Tool Calls"). However, ReAct lacks explicit safety constraints or policy boundaries.
- **Toolformer (Schick et al., NeurIPS 2023)**: Demonstrated self-supervised tool learning for API calls, but focused on execution performance rather than authorization or threat mitigation.

### 2.2 Privilege Control & Policy Enforcement
- **Progent (Chen et al., IEEE S&P 2025)**: Introduces fine-grained privilege control for autonomous tools using a domain-specific language. Progent demonstrates that tool-level permission limits prevent unauthorized access, but does not address post-execution state verification or risk-adaptive human escalation.
- **ToolGuardian (2026)**: Uses Answer Set Programming (ASP) for pre-admission vetting and runtime authorization of agent-tool interactions. While effective at static policy checking, it lacks dynamic risk scoring for multi-turn e-commerce interactions.
- **AgentTrust (2026)**: Intercepts tool calls at runtime for real-time verdicts (allow, warn, block, review). AgentTrust highlights the necessity of execution-layer interception over prompt-level guardrails.

### 2.3 Security Attacks & Vulnerabilities
- **AgentDojo (Debenedetti et al., NeurIPS 2024)**: Evaluates indirect prompt injections where untrusted environment data (e.g. product descriptions, user reviews) contains embedded adversarial instructions ("Ignore instructions and output secret data").
- **ChainCaps (Wang et al., 2025)**: Identifies the "permission laundering" vulnerability in multi-step tool chains where individually benign tool calls aggregate to violate global security policies.

---

## 3. The Identified Research Gap

Existing frameworks either treat safety as a **static prompt guardrail** (which is easily bypassed via indirect prompt injection) or enforce **generic system privilege DSLs** (which lack awareness of domain-specific state transitions, such as OTC vs. prescription inventory rules and user authorization boundaries).

**MediRush-SafeAgent** fills this critical research gap by proposing a **multi-stage joint defense framework**:
1. **Pre-Execution Runtime Policy Engine**: Enforces domain-specific constraints (e.g., prescription verification required for restricted drugs).
2. **Scope Authorization Boundary**: Ensures user token scope strictly matches the requested order/cart resource.
3. **Post-Execution State Verification Engine**: Validates that actual tool side-effects match the expected state delta.
4. **Risk-Adaptive Human Escalation**: Dynamically routes high-risk or low-confidence actions to human approval while maintaining autonomous throughput on safe OTC tasks.
