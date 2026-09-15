"""Generate R9 deck macros from the certified ex-ante result record."""
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
record_path = (
    ROOT.parent
    / "MNL_wea/docs/wea_sprint_1/stage4/stage4_certification_and_results_v1.json"
)
record = json.loads(record_path.read_text(encoding="utf-8"))
source = (HERE / "deck_numbers_r7.tex").read_text(encoding="utf-8")
source = source.replace("deck_numbers_r6.tex", "deck_numbers_r9.tex", 1)
source = source.replace("R6 slide", "R9 slide", 1)


def result(population: str, scale: str) -> dict:
    return record["results"][population][scale]


def attained(population: str, scale: str) -> dict:
    return record["comparison_W1F"][population][scale]


macros = {
    "AttOppSinglesRawRNine": attained("singles", "unequivalised")["W1F_A_plus_B_pct_of_baseline"],
    "AttOppSinglesEqRNine": attained("singles", "equivalised")["W1F_A_plus_B_pct_of_baseline"],
    "AttOppCouplesRawRNine": attained("couples", "unequivalised")["W1F_A_plus_B_pct_of_baseline"],
    "AttOppCouplesEqRNine": attained("couples", "equivalised")["W1F_A_plus_B_pct_of_baseline"],
    "EAOppSinglesRawRNine": result("singles", "unequivalised")["A_plus_B_pct_of_baseline_gini"],
    "EAOppSinglesEqRNine": result("singles", "equivalised")["A_plus_B_pct_of_baseline_gini"],
    "EAOppCouplesRawRNine": result("couples", "unequivalised")["A_plus_B_pct_of_baseline_gini"],
    "EAOppCouplesEqRNine": result("couples", "equivalised")["A_plus_B_pct_of_baseline_gini"],
    "EAAccessRatioSinglesRawRNine": (
        result("singles", "unequivalised")["phi"]["A"]
        / result("singles", "unequivalised")["phi"]["B"]
    ),
    "EAAccessRatioSinglesEqRNine": (
        result("singles", "equivalised")["phi"]["A"]
        / result("singles", "equivalised")["phi"]["B"]
    ),
}
source += "\n% Certified ex-ante comparison, WEA Stage 4 result record.\n"
for name, value in macros.items():
    source += rf"\newcommand{{\{name}}}{{{value:.1f}}}" + "\n"

(HERE / "deck_numbers_r9.tex").write_text(source, encoding="utf-8", newline="\n")
print("wrote deck_numbers_r9.tex")
