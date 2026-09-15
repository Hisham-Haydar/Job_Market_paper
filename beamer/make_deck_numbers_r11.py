"""Generate R11 deck macros: the R9 macros plus source-bound V11 keys."""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "reports/research_story_build"))
import v11_render_inputs as inputs  # noqa: E402

source = (HERE / "deck_numbers_r9.tex").read_text(encoding="utf-8")
source = source.replace("deck_numbers_r9.tex", "deck_numbers_r11.tex")

macros = {
    "AttOppMinRElevenMacro": ("att_opportunity_min_pct", ".1f"),
    "AttOppMaxRElevenMacro": ("att_opportunity_max_pct", ".1f"),
    "EAOppMinRElevenMacro": ("wea_opportunity_min_pct", ".1f"),
    "EAOppMaxRElevenMacro": ("wea_opportunity_max_pct", ".1f"),
    "MatchedAccessRatioREleven": ("mh_access_ratio", ".1f"),
    "MatchedEmpShareAREleven": ("mh_employment_share_a", ".2f"),
    "MatchedEmpShareBREleven": ("mh_employment_share_b", ".2f"),
    "MatchedWageGapREleven": ("mh_wage_gap", ".1f"),
}
source += "\n% V11 source-bound keys (certified comparison record; matched-household record).\n"
for name, (key, fmt) in macros.items():
    source += rf"\newcommand{{\{name}}}{{{format(float(inputs.REG[key]['value']), fmt)}}}" + "\n"

(HERE / "deck_numbers_r11.tex").write_text(source, encoding="utf-8", newline="\n")
target = HERE / "figures/r11"
target.mkdir(parents=True, exist_ok=True)
shutil.copyfile(inputs.MATCHED_FIG, target / "fig_matched_households_v11.png")
print("wrote deck_numbers_r11.tex and figures/r11/fig_matched_households_v11.png")
