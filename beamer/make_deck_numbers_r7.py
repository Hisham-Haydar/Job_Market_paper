"""Generate R7 deck macros from corrected POSFIT-v3b and unchanged records."""
from pathlib import Path
import importlib.util
import json


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("deck_numbers_r6_base",
                                              HERE / "make_deck_numbers_r6.py")
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
base.POSFIT = HERE.parents[1] / "MNL_posfit/outputs/positive_fit_diagnostics_v3b"
base.POSFIT_COMMIT = "cd7247cf"
base.DECK_SRC = HERE / "JMP_seminar_deck_r7.tex"
base.OUT_TEX = HERE / "deck_numbers_r7.tex"
base.OUT_JSON = HERE / "build/r7_number_provenance.json"
base.EXPECTED_ADEQUATE_GROUPS = {"couples_female", "singles_female"}
base.EXPECTED_LIMITED_GROUPS = {"couples_male", "singles_male"}

result = base.main()
corrected_path = (HERE.parents[1] / "MNL_posfit/experiments/JMP_SEMINAR_SPRINT/"
                  "runs/bandfix2_recompute/new_results_v1.json")
corrected = json.loads(corrected_path.read_text(encoding="utf-8"))
summaries = corrected["summaries"]
gaps = [100 * (row["observed"] - row["predicted"])
        for row in corrected["moments"]
        if row["model"] in ("SINGLES", "COUPLES")
        and row["moment"] == "hours::h_36_5_37_5"]
extra = [
    "% --- corrected Band-Fix-2 population fit ---",
    "\\newcommand{\\FitMAESinglesVSeven}{%.4f}" % summaries["SINGLES"]["mean_absolute_error"],
    "\\newcommand{\\FitMAECouplesVSeven}{%.4f}" % summaries["COUPLES"]["mean_absolute_error"],
    "\\newcommand{\\FitGapThirtySevenMinVSeven}{%.1f}" % min(gaps),
    "\\newcommand{\\FitGapThirtySevenMaxVSeven}{%.1f}" % max(gaps),
]
with base.OUT_TEX.open("a", encoding="utf-8") as handle:
    handle.write("\n".join(extra) + "\n")
text = base.OUT_TEX.read_text(encoding="utf-8")
text = text.replace("positive_fit_diagnostics_v3", "positive_fit_diagnostics_v3b")
text = text.replace("POSFIT v3", "POSFIT v3b")
text = text.replace("96693269", "cd7247cf")
base.OUT_TEX.write_text(text, encoding="utf-8")
raise SystemExit(result)
