"""V16 gate: no section title appears in both the body and the appendix.

Titles are compared after normalisation (case, whitespace, punctuation, and the
bookkeeping prefixes "Technical record:", "Implementation record:" and
"Appendix X."), so a relabelled duplicate such as "Technical record: Estimation"
against "Estimation, in words" is still caught. A negative control copies a body
section title into the appendix of a temporary rendered copy and must fail.
"""
from __future__ import annotations

import html
import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / "reports/v16_section_title_results.json"
BEGIN = "<!-- V15_PROVENANCE_APPENDIX_BEGIN -->"
END = "<!-- V15_PROVENANCE_APPENDIX_END -->"
SURFACES = {
    "report": (ROOT / "reports/JMP_research_story_report_v16.html", r"h[1-3]"),
    "gallery": (ROOT / "reports/JMP_results_gallery_v15.html", r"h[23]"),
}
GENERIC = {"singles", "couples", "abstract", "contents", "bibliography"}


def normalise(title: str) -> str:
    t = html.unescape(re.sub(r"<[^>]+>", " ", title)).lower()
    t = re.sub(r"^\s*\d+(\.\d+)*\.?\s+", "", t)
    t = re.sub(r"^(technical record|implementation record)\s*:\s*", "", t)
    t = re.sub(r"^appendix\s+[a-z]\.\s*", "", t)
    t = re.sub(r",\s*in words$", "", t)
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return t.strip()


def titles(fragment: str, tags: str) -> set[str]:
    fragment = re.sub(r"<nav\b.*?</nav>", " ", fragment, flags=re.S)
    found = {normalise(m.group(2)) for m in re.finditer(rf"<({tags})\b[^>]*>(.*?)</\1>", fragment, flags=re.S)}
    return {t for t in found if t and t not in GENERIC}


def scan(document: str, tags: str) -> dict:
    if document.count(BEGIN) != 1 or document.count(END) != 1:
        raise SystemExit("appendix boundary missing")
    b, e = document.index(BEGIN), document.index(END)
    body = titles(document[:b] + document[e:], tags)
    appendix = titles(document[b:e], tags)
    shared = sorted(body & appendix)
    return {"body_titles": len(body), "appendix_titles": len(appendix), "shared": shared,
            "status": "PASS" if not shared else "FAIL"}


def main() -> int:
    results = {}
    for name, (path, tags) in SURFACES.items():
        results[name] = scan(path.read_text(encoding="utf-8"), tags)

    report_path, tags = SURFACES["report"]
    original = report_path.read_text(encoding="utf-8")
    injected = original.replace(END, "<h2>Behavioural estimates</h2><p>control</p>" + END, 1)
    with tempfile.TemporaryDirectory(prefix="jmp-v16-title-control-") as tmp:
        temp = Path(tmp) / report_path.name
        temp.write_text(injected, encoding="utf-8")
        control = scan(temp.read_text(encoding="utf-8"), tags)
    control_ok = control["status"] == "FAIL" and "behavioural estimates" in control["shared"]
    status = "PASS" if all(r["status"] == "PASS" for r in results.values()) and control_ok else "FAIL"
    payload = {"gate": "V16 body/appendix section-title uniqueness", "status": status,
               "surfaces": results,
               "negative_control": {"injected": "body title 'Behavioural estimates' inside the report appendix",
                                    "expected": "FAIL", "observed": control["status"],
                                    "shared": control["shared"], "status": "PASS" if control_ok else "FAIL"}}
    OUT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"V16 SECTION TITLES {status}: report shared {results['report']['shared']}, "
          f"gallery shared {results['gallery']['shared']}; negative control observed {control['status']}")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
