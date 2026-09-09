#!/usr/bin/env python
"""Static release checks for the current-results gallery."""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "reports/JMP_results_gallery_current.html"
NOR = ROOT / "reports/numbers_of_record_v5.json"

text = P.read_text(encoding="utf-8")
without_data = re.sub(r'data:image/png;base64,[A-Za-z0-9+/=]+', 'data:image/png;base64,…', text)
nor = json.loads(NOR.read_text(encoding="utf-8"))
checks = {}
checks["self_contained"] = "data:image/png;base64," in text and not re.search(r'<(?:img|script|link)[^>]+(?:src|href)=["\'](?!data:|#)', text)
checks["eight_sections"] = len(re.findall(r'<section id=', text)) == 8
checks["captions_complete"] = text.count("<figure") + text.count("<figcaption class=standalone>") == text.count("<span class=capkey>Population</span>")
checks["current_samples"] = f'{int(nor["entries"]["n_singles"]["value"]):,}' in text and f'{int(nor["entries"]["n_couples"]["value"]):,}' in text
forbidden = [r"[A-Fa-f0-9]{32,}", r"(?:[A-Za-z]:\\|\.\./|/runs/|/figures/)", r"\bR-\d+\b", r"\b(?:S11|S12|PRICE-D)\b", r"mission"]
checks["no_internal_paths_hashes_labels"] = not any(re.search(p, without_data) for p in forbidden)
checks["intervals_separate"] = "RQMC band" in text and "CR1 interval" in text and "never merged" in text
checks["no_mae_headline"] = "mean absolute error" not in text.lower() and ">MAE<" not in text
checks["registry_present"] = "gallery" in nor and bool(nor["gallery"].get("coefficients"))
failed = [k for k,v in checks.items() if not v]
for k,v in checks.items(): print(f'{"PASS" if v else "FAIL"}: {k}')
if failed: raise SystemExit("failed: " + ", ".join(failed))
