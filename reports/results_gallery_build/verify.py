#!/usr/bin/env python
"""Static release checks for the current-results gallery."""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import retired_lineage_gate as rlg  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "reports/JMP_results_gallery_current.html"
NOR = ROOT / "reports/numbers_of_record_v5.json"
BUILD = Path(__file__).resolve().parent / "build.py"

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
# The retired four-factor decomposition kept an RQMC integration band and a
# CR1 parameter interval visually separate and explicitly "never merged".
# The current preliminary three-factor decomposition (DECOMP-2) instead
# reports two different uncertainty summaries -- a Monte Carlo range across
# simulation replications, and an independent second-seed check -- and the
# analogous guarantee is that neither is ever presented as a confidence
# interval.
checks["intervals_separate"] = ("MC range (min" in text and "Second-seed" in text
                                 and "never confidence intervals" in text)
checks["no_mae_headline"] = "mean absolute error" not in text.lower() and ">MAE<" not in text
checks["registry_present"] = "gallery" in nor and bool(nor["gallery"].get("coefficients"))
# LINEAGE-SWEEP-1: path-based, not string-based -- scans the build script and
# the rendered HTML for a READ of a retired welfare-decomposition artifact by
# its own filename, independent of how the surrounding prose is worded.
_lineage_violations = rlg.scan_files([BUILD, P])
checks["no_retired_lineage_path_reads"] = not _lineage_violations
if _lineage_violations:
    print(rlg.format_violations(_lineage_violations, ROOT))
failed = [k for k,v in checks.items() if not v]
for k,v in checks.items(): print(f'{"PASS" if v else "FAIL"}: {k}')
if failed: raise SystemExit("failed: " + ", ".join(failed))
