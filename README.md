# MediRush (`medirush`)

[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![Next.js 15](https://img.shields.io/badge/Next.js-15-black.svg)](https://nextjs.org/)
[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](LICENSE)
[![Manuscript](https://img.shields.io/badge/Research-MediRush--SafeAgent-orange.svg)](RESEARCH.md)

> A production-grade healthcare-commerce platform and research system evaluating policy-constrained, safe, and reliable tool-using AI agents (**MediRush-SafeAgent**).

---

## 🏛 Architecture & Overview

```mermaid
flowchart TD
    UserReq["User Healthcare-Commerce Request"] --> IntentModule["Intent Understanding & Context Filter"]
    IntentModule --> SafetyPolicy["Runtime Policy & Security Guardrails Layer"]
    SafetyPolicy -->|Policy Approved| AgentPlanner["LLM Agent Planner & Tool Selector"]
    SafetyPolicy -.->|Policy Denied| SafetyRefusal["Safe System Refusal / User Escalation"]

    AgentPlanner --> ToolAuth["Tool Authorization & Scope Verifier"]
    ToolAuth -->|Authorized| ToolExec["Tool Execution Engine"]
    ToolAuth -.->|Unauthorized| AuthBlock["Authorization Block & Alert"]

    ToolExec --> StateVerif["Post-Execution State Verification Engine"]
    StateVerif --> RiskEval["Dynamic Risk Assessment Classifier"]

    RiskEval -->|Low / Medium Risk| FinalResponse["Structured Verified Response"]
    RiskEval -->|High / Critical Risk| HITL["Human-in-the-Loop Approval Escalation"]
```

---

## 🔬 Research & Benchmark (`MediRush-SafeAgent`)

See [`RESEARCH.md`](RESEARCH.md) for full research documentation, literature review, novelty analysis, experimental benchmark metrics, and manuscript sources.

- **Primary Research Paper**: [`research/paper/main/main.tex`](research/paper/main/main.tex)
- **MediRushBench Dataset**: [`research/datasets/medirush_bench.json`](research/datasets/medirush_bench.json)
- **Experimental Protocol**: [`research/EXPERIMENT_PROTOCOL.md`](research/EXPERIMENT_PROTOCOL.md)
- **Literature Review**: [`research/literature/literature-review.md`](research/literature/literature-review.md)

### Quick Experiment Run

```bash
python3 research/evaluation/run_experiments.py
```

---

## 💻 Web Application (`apps/web`)

```bash
pnpm install
pnpm dev
```

---

## Author

**Sham Satish Thakare**  
GitHub: [https://github.com/shamddd](https://github.com/shamddd)
