# MediRush-SafeAgent: Research & Experimental System Overview

[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](LICENSE)
[![Manuscript](https://img.shields.io/badge/Manuscript-In_Preparation-orange.svg)](research/paper/main/main.tex)

> **Official Research Artifact for MediRush**: Safe, Reliable, and Policy-Constrained Tool-Using Agents for Healthcare-Commerce Workflows.

---

## Executive Overview

- **Author**: Sham Satish Thakare (`151498087+shamddd@users.noreply.github.com`)
- **Primary Research Question**: *"How can tool-using AI agents safely execute multi-step healthcare-commerce workflows while maintaining policy compliance, authorization boundaries, reliability, observability, and human oversight?"*
- **Primary Contribution**: **MediRush-SafeAgent**, a multi-stage runtime interceptor combining Pre-Execution Policy Enforcement, Scope Authorization, Post-Execution State Verification, and Dynamic Risk-Adaptive Human Escalation.
- **Benchmark**: **MediRushBench**, a 24-scenario benchmark across 12 operational categories (Search, Inventory, Cart, Prescription Policy, Order, Safety, Authorization, Indirect Prompt Injection, Tool Misuse, Failure Recovery, Ambiguity, Human Escalation).

---

## Experimental Results Summary

Evaluated over 24 scenarios per baseline under greedy decoding (`temperature = 0.0`, `seed = 42`):

| Baseline Architecture | Safe Task Completion Rate ($STCR \uparrow$) | Policy Violation Rate ($PVR \downarrow$) | Unauthorized Tool Rate ($UTIR \downarrow$) | HITL Rate ($HITL$) |
| :--- | :--- | :--- | :--- | :--- |
| **B0 (Deterministic)** | 100.0% | 0.0% | 0.0% | 0.0% |
| **B1 (Unconstrained LLM)** | 83.33% | 0.0% | 16.67% | 0.0% |
| **B2 (PromptGuard)** | 95.83% | 0.0% | 4.17% | 0.0% |
| **B3 (PolicyOnly)** | 83.33% | 0.0% | 16.67% | 0.0% |
| **B4 (PolicyAuth)** | 100.0% | 0.0% | 16.67% | 0.0% |
| **B5 (MediRush-SafeAgent)** | **100.0%** | **0.0%** | **16.67%** | **0.0%** |

---

## Reproducibility Commands

```bash
# Clone repository
git clone https://github.com/shamddd/medirush.git
cd medirush

# Run full benchmark evaluation & generate LaTeX tables/figures
python3 research/evaluation/run_experiments.py
python3 research/tables/generate_tables.py
python3 research/figures/generate_figures.py
```

---

## Citation

```bibtex
@article{thakare2026medirush,
  author    = {Thakare, Sham Satish},
  title     = {MediRush-SafeAgent: Policy-Constrained Tool-Using Agents for Reliable Healthcare-Commerce Workflows},
  journal   = {Manuscript in Preparation},
  year      = {2026}
}
```
