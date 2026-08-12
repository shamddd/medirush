# Novelty Analysis & Research Gap Matrix — MediRush-SafeAgent

**Author**: Sham Satish Thakare  
**Date**: August 12, 2026

---

## 1. Technical Comparison Matrix

| Existing Work | Tool Use | Policy Engine | Scope Auth | State Verification | Human Escalation | Failure Recovery | Adversarial Eval | Healthcare Scope |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **ReAct (Yao et al., 2023)** | Yes | No | No | No | No | Partial | No | No |
| **Toolformer (Schick et al., 2023)**| Yes | No | No | No | No | No | No | No |
| **AgentDojo (Debenedetti, 2024)** | Yes | No | No | No | No | No | Yes | No |
| **Progent (Chen et al., 2025)** | Yes | Yes (DSL) | Yes | No | No | No | Yes | No |
| **ChainCaps (Wang et al., 2025)** | Yes | Yes | Yes | No | No | No | Partial | No |
| **ToolGuardian (2026)** | Yes | Yes (ASP) | Partial | No | No | No | Yes | No |
| **AgentTrust (2026)** | Yes | Yes | No | No | Partial | No | Yes | No |
| **MediRush-SafeAgent (Ours)** | **Yes** | **Yes (Domain)** | **Yes** | **Yes** | **Yes (Risk-Adaptive)** | **Yes** | **Yes** | **Yes** |

---

## 2. What Exactly Is Novel?

We do NOT claim novelty based on using LLMs, LangGraph, or operating in healthcare. Instead, the novel technical contributions of **MediRush-SafeAgent** are:

1. **Integrated Multi-Stage Defense Architecture**: A formal 4-layer runtime interceptor coupling (a) Pre-execution policy enforcement, (b) Scope authorization verification, (c) Post-execution environment state verification, and (d) Dynamic risk-adaptive human escalation.
2. **Post-Execution State Verification Engine**: Unlike prior works that only check tool parameters before invocation, MediRush-SafeAgent executes a deterministic state diff verifier following tool execution. This detects hidden side-effects, corrupted outputs, or parameter tampering before returning results to the LLM context.
3. **Domain-Constrained Risk Scoring & HITL Routing**: A risk assessment classifier tailored to healthcare-commerce state transitions (e.g. OTC vs. Prescription, quantity limits, payment authorization) that calculates a dynamic risk vector $\vec{R}$ to decide whether to auto-commit or escalate to human approval.
4. **MediRushBench Standardized Benchmark**: The first benchmark specifically evaluating safety, authorization, and prompt injection resiliency in multi-step healthcare-commerce agent workflows.

---

## 3. Falsifiable Hypotheses

- **$H_1$ (Policy Enforcement)**: Explicit runtime policy-constrained tool execution achieves a statistically significant reduction in Policy Violation Rate ($\ge 80\%$ reduction) compared to unconstrained LLM tool-calling agents ($p < 0.01$).
- **$H_2$ (Risk-Adaptive Escalation)**: Dynamic risk-adaptive human escalation eliminates $100\%$ of high-risk autonomous safety breaches while maintaining $> 90\%$ autonomous task completion on low-risk OTC workflows.
- **$H_3$ (State Verification)**: Post-execution state verification improves multi-step workflow completion reliability under tool errors by $\ge 35\%$ compared to unverified tool execution.
- **$H_4$ (Joint Defense Synergy)**: Combining policy checks, scope authorization, state verification, and human escalation provides a statistically higher Safe Task Completion Rate than any individual defense component alone.
