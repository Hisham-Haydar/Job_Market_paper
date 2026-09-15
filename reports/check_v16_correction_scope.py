"""V16 gate: the report differs from V15 by exactly the four V19-C2 corrections.

Applies the four recorded replacements (research_story_build/v16_sections.py) to the V15
generated Markdown and requires the result to equal the V16 generated Markdown, apart
from the release-version metadata. Also requires equal registry entries and identical
embedded images, and that the corrected strings render in the V16 HTML. A negative
control plants one extra edit in a temporary copy and must fail.
"""
from __future__ import annotations

import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "reports/research_story_build"))
import v16_sections as v16  # noqa: E402

MD15 = ROOT / "reports/research_story_build/story_v15.generated.md"
MD16 = ROOT / "reports/research_story_build/story_v16.generated.md"
HTML15 = ROOT / "reports/JMP_research_story_report_v15.html"
HTML16 = ROOT / "reports/JMP_research_story_report_v16.html"
REG15 = ROOT / "reports/numbers_of_record_v15.json"
REG16 = ROOT / "reports/numbers_of_record_v16.json"
OUT = ROOT / "reports/v16_correction_scope_results.json"


def expected_md(md15: str) -> str:
    out = md15
    for label, old, new in v16.CORRECTIONS:
        if out.count(old) != 1:
            raise SystemExit("correction anchor %r not found once in V15 Markdown" % label)
        out = out.replace(old, new)
    return out


def scope(md16: str) -> dict:
    md15 = MD15.read_text(encoding="utf-8")
    ok_md = expected_md(md15) == md16
    reg15 = json.loads(REG15.read_text(encoding="utf-8"))
    reg16 = json.loads(REG16.read_text(encoding="utf-8"))
    ok_reg = reg15["entries"] == reg16["entries"] and all(
        reg15[k] == reg16[k] for k in reg15 if k != "presentation_version")
    img = lambda p: re.findall(r"base64,([A-Za-z0-9+/=]+)", p.read_text(encoding="utf-8"))
    ok_img = img(HTML15) == img(HTML16)
    html16 = HTML16.read_text(encoding="utf-8")
    rendered = all(s in html16 for s in (
        r"g_i(j)=\left(g^{E}_i\cdot g^{H}_i(h)\cdot g^{\mathrm{Occ}}_i(k)\cdot",
        r"g_i(o)=1", "no consumption floor is applied",
        "is the executed preliminary decomposition", "realised-bundle",
        "ex-ante route that integrates attained welfare")) and "one-euro consumption floor" not in html16 \
        and "receives a one-euro floor inside this" not in html16
    return {"markdown_equals_v15_plus_corrections": ok_md, "registry_entries_unchanged": ok_reg,
            "embedded_images_identical": ok_img, "corrections_rendered": rendered,
            "status": "PASS" if ok_md and ok_reg and ok_img and rendered else "FAIL"}


def main() -> int:
    result = scope(MD16.read_text(encoding="utf-8"))
    planted = MD16.read_text(encoding="utf-8").replace("The third kind is support.",
                                                      "The third kind is the support.", 1)
    control = scope(planted)
    ok = result["status"] == "PASS" and control["status"] == "FAIL"
    payload = {"gate": "V16 correction scope", "status": "PASS" if ok else "FAIL",
               "result": result, "negative_control": {"planted": "one extra word in Section 2",
                                                      "observed": control["status"], "expected": "FAIL"}}
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n")
    print("V16 CORRECTION SCOPE %s: %s; negative control observed %s"
          % (payload["status"], {k: v for k, v in result.items() if k != "status"}, control["status"]))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
