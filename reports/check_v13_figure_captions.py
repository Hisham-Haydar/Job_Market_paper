"""V13 gate: every rendered figure caption uses the current access definition.

Scans every figcaption (and image alt text) in the rendered report and gallery,
appendix included. A caption that refers to the access channel must name local
unemployment exposure, and no caption may carry an outdated access definition.
Old decomposition image files must not be embedded. A negative control inserts a
figure with the outdated definition into a temporary copy and must fail.
"""
from __future__ import annotations

import html
import json
import re
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / "reports/v13_figure_caption_results.json"
SURFACES = {"report": ROOT / "reports/JMP_research_story_report_v13.html",
            "gallery": ROOT / "reports/JMP_results_gallery_v13.html"}
ACCESS_MENTION = re.compile(r"\baccess\b", re.I)
CURRENT = re.compile(r"local unemployment exposure", re.I)
OUTDATED = [
    re.compile(r"\(\s*region,\s*urban/rural,\s*year\s*\)", re.I),
    re.compile(r"geographic/temporal access shifters", re.I),
    re.compile(r"region,\s*urban or rural location,?\s*(?:and\s*)?year", re.I),
]


def captions(document: str) -> list[str]:
    document = re.sub(r'data:image/[a-z]+;base64,[A-Za-z0-9+/=]+', "", document)
    found = [m.group(1) for m in re.finditer(r"<figcaption\b[^>]*>(.*?)</figcaption>", document, flags=re.S)]
    found += [m.group(1) for m in re.finditer(r'<img\b[^>]*\balt="([^"]*)"', document, flags=re.S)]
    return [" ".join(html.unescape(re.sub(r"<[^>]+>", " ", c)).split()) for c in found]


def scan(document: str) -> dict:
    failures = []
    caps = captions(document)
    for text in caps:
        outdated = [p.pattern for p in OUTDATED
                    if (m := p.search(text)) and not CURRENT.search(text[max(0, m.start() - 60):m.end()])]
        if outdated or (ACCESS_MENTION.search(text) and re.search(r"access channel|access is|access \(", text, re.I)
                        and not CURRENT.search(text)):
            failures.append(text[:180])
    old_images = re.findall(r"fig_preseminar_pab_[a-z_]+", document)
    return {"captions_scanned": len(caps),
            "captions_naming_access": sum(1 for c in caps if ACCESS_MENTION.search(c)),
            "failures": failures, "old_images": sorted(set(old_images)),
            "status": "PASS" if not failures and not old_images else "FAIL"}


def main() -> int:
    results = {name: scan(path.read_text(encoding="utf-8")) for name, path in SURFACES.items()}
    report = SURFACES["report"].read_text(encoding="utf-8")
    injected = report.replace(
        "</main>",
        '<figure><img alt="control"><figcaption>Shapley contributions. Access is local '
        "geographic/temporal access shifters (region, urban/rural, year).</figcaption></figure></main>", 1)
    with tempfile.TemporaryDirectory(prefix="jmp-v13-caption-control-") as tmp:
        temp = Path(tmp) / "control.html"
        temp.write_text(injected, encoding="utf-8")
        control = scan(temp.read_text(encoding="utf-8"))
    control_ok = control["status"] == "FAIL" and len(control["failures"]) == 1
    status = "PASS" if all(r["status"] == "PASS" for r in results.values()) and control_ok else "FAIL"
    payload = {"gate": "V13 figure captions use the current access definition", "status": status,
               "surfaces": results,
               "negative_control": {"injected": "figure caption with the outdated access definition",
                                    "expected": "FAIL", "observed": control["status"],
                                    "failures": control["failures"], "status": "PASS" if control_ok else "FAIL"}}
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(f"V13 FIGURE CAPTIONS {status}: report {results['report']['captions_scanned']} captions "
          f"({results['report']['captions_naming_access']} naming access), gallery "
          f"{results['gallery']['captions_scanned']} ({results['gallery']['captions_naming_access']}); "
          f"negative control observed {control['status']}")
    for name, r in results.items():
        for f in r["failures"]:
            print(f"  FAIL {name}: {f}")
        if r["old_images"]:
            print(f"  FAIL {name}: old images {r['old_images']}")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
