"""Check the V11 report, gallery, notebook, deck and rehearsal script are synchronised."""
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
report = (ROOT / "reports/JMP_research_story_report_v11.html").read_text(encoding="utf-8")
gallery = (ROOT / "reports/JMP_results_gallery_v11.html").read_text(encoding="utf-8")
deck = (ROOT / "beamer/JMP_seminar_deck_r11.tex").read_text(encoding="utf-8")
deck_numbers = (ROOT / "beamer/deck_numbers_r11.tex").read_text(encoding="utf-8")
script = (ROOT / "reports/rehearsal_pack_v11.md").read_text(encoding="utf-8")
notebook = json.loads((WORKSPACE / "MNL_wea/experiments/JMP_SEMINAR_SPRINT/JMP_canonical_AtoZ.ipynb")
                      .read_text(encoding="utf-8"))
notebook_text = "\n".join("".join(c.get("source", [])) for c in notebook["cells"]) + json.dumps(
    [c.get("outputs", []) for c in notebook["cells"]], ensure_ascii=False)


def flat(text: str) -> str:
    return " ".join(text.replace("’", "'").split())


surfaces = {"report": flat(report), "gallery": flat(gallery), "deck": flat(deck + " " + deck_numbers),
            "rehearsal": flat(script), "notebook": flat(notebook_text)}
title = "Unequal Job Opportunities and Well-Being Inequality: A Latent-Jobs Structural Decomposition"
checks = {
    "exact_title_report_gallery_deck_rehearsal": all(title in surfaces[n] for n in ("report", "gallery", "deck", "rehearsal")),
    "four_exante_shares": all(all(v in t for v in ("14.8", "20.3", "21.3", "7.9")) for t in surfaces.values()),
    "outcomes_versus_prospects": all(re.search(r"outcomes versus prospects|ATT", t) and re.search(r"\bEA\b|ex-ante", t)
                                     for t in surfaces.values()),
    "interpretation_sentence": all(re.search(r"depends on whether welfare evaluates the realised outcome or the opportunity prospect", t)
                                   for t in surfaces.values()),
    "couples_no_reversal": all(re.search(r"(?:[Cc]ouples show no such reversal|couples: no reversal|Couples show no such reversal)", t)
                               for n, t in surfaces.items() if n != "gallery") and "Couples show no such reversal" in surfaces["gallery"],
    "d_held_fixed": all(re.search(r"holding (?:household )?resources, needs and composition fixed", t) for t in surfaces.values()),
    "neither_primary": all(re.search(r"neither.{0,40}primary", t, flags=re.I) for t in surfaces.values()),
    "couples_scale_warning": all("21.3" in t and "7.9" in t and re.search(r"preference.{0,80}negative|negative.{0,80}preference", t, flags=re.I)
                                 for t in surfaces.values()),
    "matched_pair_report_gallery_deck_rehearsal": all(re.search(r"matched", t, flags=re.I) for n, t in surfaces.items() if n != "notebook"),
    "no_measure_one_defence": not any(re.search(r"Measure 1|Haydar--Maniquet|measure one and measure four", t) for t in surfaces.values()),
    "notebook_executed": next(c for c in notebook["cells"] if c.get("id") == "v9_wea_comparison").get("execution_count") is not None,
}
for name, ok in checks.items():
    print(("PASS" if ok else "FAIL") + ": " + name)
failed = [name for name, ok in checks.items() if not ok]
if failed:
    raise SystemExit("V11 surface sync failed: " + ", ".join(failed))
