"""Check the V9 gallery, notebook, deck and rehearsal script are synchronized."""
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
report = (ROOT / "reports/JMP_research_story_report_v9.html").read_text(encoding="utf-8")
gallery = (ROOT / "reports/JMP_results_gallery_v9.html").read_text(encoding="utf-8")
deck = (ROOT / "beamer/JMP_seminar_deck_r9.tex").read_text(encoding="utf-8")
script = (ROOT / "reports/rehearsal_pack_v9.md").read_text(encoding="utf-8")
notebook = json.loads((WORKSPACE / "MNL_wea/experiments/JMP_SEMINAR_SPRINT/JMP_canonical_AtoZ.ipynb").read_text(encoding="utf-8"))
notebook_text = json.dumps(notebook, ensure_ascii=False)
deck_numbers = (ROOT / "beamer/deck_numbers_r9.tex").read_text(encoding="utf-8")
exact_title = (
    "Unequal Job Opportunities and Well-Being Inequality: "
    "A Latent-Jobs Structural Decomposition"
)
surfaces = {"report": report, "gallery": gallery, "deck": deck + "\n" + deck_numbers,
            "rehearsal": script, "notebook": notebook_text}
checks = {
    "exact_title_report_gallery_deck_rehearsal": all(
        exact_title in surfaces[name] for name in ("report", "gallery", "deck", "rehearsal")),
    "four_exante_shares": all(
        all(value in text for value in ("14.8", "20.3", "21.3", "7.9"))
        for text in surfaces.values()),
    "channel_divergence": all(
        re.search(r"access.{0,80}(?:three|3).{0,30}(?:times|×).{0,40}earn", text,
                  flags=re.I | re.S)
        for text in surfaces.values()),
    "neither_primary": all(
        re.search(r"neither.{0,40}primary", text, flags=re.I | re.S)
        for text in surfaces.values()),
    "couples_scale_warning": all(
        "21.3" in text and "7.9" in text
        and re.search(r"preference.{0,80}negative|negative.{0,80}preference", text,
                      flags=re.I | re.S)
        for text in surfaces.values()),
    "deck_one_extra_frame": len(re.findall(r"\\begin\{frame\}", deck))
        == len(re.findall(r"\\begin\{frame\}",
                          (ROOT / "beamer/JMP_seminar_deck_r7.tex").read_text(encoding="utf-8"))) + 1,
    "notebook_executed": next(
        cell for cell in notebook["cells"] if cell.get("id") == "v9_wea_comparison"
    ).get("execution_count") is not None,
}
for name, ok in checks.items():
    print(("PASS" if ok else "FAIL") + ": " + name)
failed = [name for name, ok in checks.items() if not ok]
if failed:
    raise SystemExit("V9 surface sync failed: " + ", ".join(failed))
