# MediRush Research System & MediRushBench

This directory contains the complete, reproducible research system for **MediRush-SafeAgent**: Policy-Constrained Tool-Using Agents for Safe Healthcare-Commerce Workflows.

**Author**: Sham Satish Thakare  
**Target PhD Applications**: Top CS / AI PhD Programs (Harvard, CMU, Stanford, MIT)

---

## Reproducibility Quick Start

### 1. Installation

```bash
# Clone repository
git clone https://github.com/shamddd/medirush.git
cd medirush

# Install research environment via uv
pip install uv
uv venv research-env --python 3.12
source research-env/bin/activate
uv pip install -r research/requirements.txt
```

### 2. Run Complete Experimental Suite

```bash
# Execute MediRushBench across all baselines (B0-B5) with deterministic seed=42
python research/evaluation/run_experiments.py --seed 42 --episodes 120

# Process raw JSON results into statistical tables & publication figures
python research/tables/generate_tables.py
python research/figures/generate_figures.py
```

---

## Directory Structure

- `src/`: Core Python research implementation (Policy Engine, Scope Auth, State Verifier, Dynamic Risk Classifier, MediRush-SafeAgent).
- `datasets/`: `MediRushBench` evaluation benchmark (12 categories, 120 scenario JSONs).
- `baselines/`: Implementations of $B_0$ through $B_4$ comparison baselines.
- `evaluation/`: Benchmark evaluator, metrics calculator, and experiment runner.
- `attacks/`: Adversarial direct/indirect prompt injection & tool misuse suite.
- `results/`: Raw and processed experimental results (`raw/`, `processed/`).
- `paper/main/`: Publication-ready double-blind LaTeX manuscript.
