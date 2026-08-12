# Research Audit — MediRush (`medirush`)

**Author**: Sham Satish Thakare  
**Date**: August 12, 2026  
**Repository**: [https://github.com/shamddd/medirush](https://github.com/shamddd/medirush)

---

## Executive Audit Summary

This audit establishes the baseline status of the MediRush codebase prior to building the research-grade experimental harness (`MediRush-SafeAgent`).

---

## Codebase Component Classification

| Component | Status | Location | Notes / Technical Details |
| :--- | :--- | :--- | :--- |
| **Next.js Web Frontend** | `PARTIALLY IMPLEMENTED` | `apps/web/` | Next.js 15 App Router landing page UI. |
| **Healthcare Catalog Tools** | `PROPOSED` | `research/src/tools/` | Catalog search, inventory check, product info tools. |
| **Prescription Policy Engine** | `PROPOSED` | `research/src/policy/` | Pre-admission vetting and runtime policy checker. |
| **Scope Authorization Verifier**| `PROPOSED` | `research/src/auth/` | Cross-user data boundary & scope checker. |
| **Post-State Verifier** | `PROPOSED` | `research/src/verification/` | Execution trace & state consistency validator. |
| **Dynamic Risk Classifier** | `PROPOSED` | `research/src/risk/` | Risk scoring & HITL escalation router. |
| **MediRushBench Benchmark** | `PROPOSED` | `research/datasets/` | 12-category evaluation suite (120+ scenarios). |
| **Baseline Agent Models (B0-B4)**| `PROPOSED` | `research/src/baselines/` | Comparative baselines (Rule-based, ReAct, Prompt Guard). |
| **Adversarial Evaluation Suite**| `PROPOSED` | `research/attacks/` | Direct/indirect prompt injection & tool misuse attacks. |
| **Experimental Harness** | `PROPOSED` | `research/evaluation/` | Automated runner, result logger, latex table generator. |
| **Publication Manuscript** | `PROPOSED` | `research/paper/main/` | IEEE/ACM double-blind LaTeX submission paper. |

---

## Technical Novelty vs. Engineering Distinction

### Engineering Components (Non-Novel Infrastructure)
- Next.js monorepo setup, pnpm workspace, Tailwind styling.
- Standard REST / GraphQL API endpoints for pharmacy catalog lookup.
- Basic LLM prompt wrapping or standard tool-calling SDK integration.

### Scientific Research Contributions (Technically Novel)
1. **Multi-Stage Policy-Constrained Tool Authorization Framework**: Enforcing runtime policy assertions, scope validation, and state post-verification before committing high-risk actions.
2. **MediRushBench Benchmark**: Standardized, reproducible evaluation suite quantifying Safe Task Completion Rate and Policy Violation Rate in healthcare-commerce workflows.
3. **Risk-Adaptive Escalation Mechanism**: Dynamic risk scoring balancing human oversight overhead against safety violations under adversarial prompt injection.

---

## Verification Status Matrix

- **Implemented**: 5% (Initial Next.js Workspace)
- **Partially Implemented**: 5% (Landing UI)
- **Proposed**: 90% (Research Agent, Policy Engine, Benchmark, LaTeX Manuscript)
- **Experimentally Verified**: 0% (`TODO — EXPERIMENT REQUIRED`)
