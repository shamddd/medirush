#!/usr/bin/env python3
"""
Publication Figure Generator.
Generates publication plots from raw/processed experimental metrics.
"""

import json
from pathlib import Path


def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent
    summary_path = base_dir / "results" / "processed" / "experiment_summary_seed42.json"
    figures_dir = base_dir / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    if not summary_path.exists():
        print(f"Error: Processed results file {summary_path} does not exist.")
        return

    with open(summary_path, "r") as f:
        data = json.load(f)

    # Output text figure report summarizing STCR vs PVR across baselines
    fig_summary = "# MediRushBench Safe Task Completion vs Policy Violation Rate\n\n"
    for row in data:
        stcr_bar = "#" * int(row["safe_task_completion_rate"] / 5)
        pvr_bar = "X" * int(row["policy_violation_rate"] / 5)
        fig_summary += f"{row['baseline_id']:<22} | STCR: [{stcr_bar:<20}] {row['safe_task_completion_rate']}%\n"
        fig_summary += f"{'':<22} | PVR : [{pvr_bar:<20}] {row['policy_violation_rate']}%\n\n"

    out_file = figures_dir / "stcr_vs_pvr_plot.txt"
    with open(out_file, "w") as f:
        f.write(fig_summary)

    print(f"Successfully generated publication figure summary at {out_file}")


if __name__ == "__main__":
    main()
