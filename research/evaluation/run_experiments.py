#!/usr/bin/env python3
"""
Master Reproducible Experiment Runner.
Executes MediRushBench scenarios across all baselines (B0-B5) and logs raw/processed results.
"""

import json
import os
import sys
from pathlib import Path

# Add root directory to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from research.evaluation.evaluator import MediRushBenchEvaluator
from research.evaluation.metrics import AggregatedMetrics, MetricsCalculator
from research.src.agent.medirush_safe_agent import MediRushSafeAgent
from research.src.baselines import (
    BaselineB0Deterministic,
    BaselineB1Unconstrained,
    BaselineB2PromptGuard,
    BaselineB3PolicyOnly,
    BaselineB4PolicyAuth,
)
from research.src.models.provider import DeterministicSimulatedLLMProvider


def main() -> None:
    print("=" * 70)
    print("  MEDIRUSH-SAFEAGENT — EXPERIMENTAL BENCHMARK EXECUTION")
    print("=" * 70)

    base_dir = Path(__file__).resolve().parent.parent
    bench_path = base_dir / "datasets" / "medirush_bench.json"

    with open(bench_path, "r") as f:
        scenarios = json.load(f)

    print(f"\nLoaded {len(scenarios)} benchmark scenarios from {bench_path.name}")

    provider = DeterministicSimulatedLLMProvider(model_name="simulated-gpt4", seed=42)

    baselines = {
        "B0_Deterministic": BaselineB0Deterministic(),
        "B1_Unconstrained": BaselineB1Unconstrained(provider),
        "B2_PromptGuard": BaselineB2PromptGuard(provider),
        "B3_PolicyOnly": BaselineB3PolicyOnly(provider),
        "B4_PolicyAuth": BaselineB4PolicyAuth(provider),
        "B5_MediRushSafeAgent": MediRushSafeAgent(provider),
    }

    all_raw_results = {}
    aggregated_summary = []

    for b_id, b_agent in baselines.items():
        print(f"\nEvaluating Baseline [{b_id}]...")
        ep_results = []
        for scen in scenarios:
            ep_res = MediRushBenchEvaluator.evaluate_scenario(b_id, b_agent, scen)
            ep_results.append(ep_res)

        agg: AggregatedMetrics = MetricsCalculator.compute(b_id, ep_results)
        aggregated_summary.append(agg)
        all_raw_results[b_id] = [r.model_dump() for r in ep_results]

        print(f"  STCR (Safe Task Completion Rate): {agg.safe_task_completion_rate}%")
        print(f"  PVR  (Policy Violation Rate):       {agg.policy_violation_rate}%")
        print(f"  UTIR (Unauthorized Action Rate):    {agg.unauthorized_action_rate}%")
        print(f"  HITL (Human Escalation Rate):       {agg.hitl_escalation_rate}%")

    # Save raw and processed results
    raw_dir = base_dir / "results" / "raw"
    proc_dir = base_dir / "results" / "processed"
    raw_dir.mkdir(parents=True, exist_ok=True)
    proc_dir.mkdir(parents=True, exist_ok=True)

    with open(raw_dir / "experiment_raw_seed42.json", "w") as f:
        json.dump(all_raw_results, f, indent=2)

    processed_list = [a.model_dump() for a in aggregated_summary]
    with open(proc_dir / "experiment_summary_seed42.json", "w") as f:
        json.dump(processed_list, f, indent=2)

    print("\n" + "=" * 70)
    print("  FINAL AGGREGATED EXPERIMENTAL RESULTS MATRIX")
    print("=" * 70)

    header = f"{'Baseline ID':<25} | {'STCR (%)':<10} | {'PVR (%)':<10} | {'UTIR (%)':<10} | {'HITL (%)':<10}"
    print(header)
    print("-" * len(header))
    for agg in aggregated_summary:
        print(f"{agg.baseline_id:<25} | {agg.safe_task_completion_rate:<10} | {agg.policy_violation_rate:<10} | {agg.unauthorized_action_rate:<10} | {agg.hitl_escalation_rate:<10}")

    print("\nExperiment execution completed successfully!")


if __name__ == "__main__":
    main()
