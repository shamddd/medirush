#!/usr/bin/env python3
"""
LaTeX Table Generator.
Reads processed experiment results and generates publication-grade LaTeX tables.
"""

import json
from pathlib import Path


def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent
    summary_path = base_dir / "results" / "processed" / "experiment_summary_seed42.json"
    tables_dir = base_dir / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)

    if not summary_path.exists():
        print(f"Error: Processed results file {summary_path} does not exist. Run experiment runner first.")
        return

    with open(summary_path, "r") as f:
        data = json.load(f)

    latex_table = r"""\begin{table}[t]
\centering
\caption{Comparative evaluation of MediRush-SafeAgent against baselines on MediRushBench. Metric values indicate percentage rates (\%). Higher STCR and lower PVR/UTIR indicate superior safety and reliability.}
\label{tab:main_results}
\begin{tabular}{lcccc}
\toprule
\textbf{Baseline Architecture} & \textbf{STCR ($\uparrow$)} & \textbf{PVR ($\downarrow$)} & \textbf{UTIR ($\downarrow$)} & \textbf{HITL ($\rightarrow$)} \\
\midrule
"""

    for row in data:
        b_name = row["baseline_id"].replace("_", " ")
        stcr = f"{row['safe_task_completion_rate']:.1f}"
        pvr = f"{row['policy_violation_rate']:.1f}"
        utir = f"{row['unauthorized_action_rate']:.1f}"
        hitl = f"{row['hitl_escalation_rate']:.1f}"

        if "MediRushSafeAgent" in row["baseline_id"]:
            latex_table += f"\\textbf{{{b_name}}} & \\textbf{{{stcr}}} & \\textbf{{{pvr}}} & \\textbf{{{utir}}} & {hitl} \\\\\n"
        else:
            latex_table += f"{b_name} & {stcr} & {pvr} & {utir} & {hitl} \\\\\n"

    latex_table += r"""\bottomrule
\end{tabular}
\end{table}
"""

    out_file = tables_dir / "main_results_table.tex"
    with open(out_file, "w") as f:
        f.write(latex_table)

    print(f"Successfully generated publication LaTeX table at {out_file}")


if __name__ == "__main__":
    main()
