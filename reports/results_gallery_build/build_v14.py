#!/usr/bin/env python
"""Build the V14 gallery from the V13 gallery: add the theory figure only.

The figure goes into the welfare panel immediately after the two-perspective
framing sentence and before the attained-bundle notice. Every other byte of the
V13 gallery is kept, apart from the version label and appendix markers.
"""
from __future__ import annotations

import base64
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "reports/research_story_build"))
import v14_render_inputs as inputs  # noqa: E402
import v14_sections as sections  # noqa: E402

SOURCE = ROOT / "reports/JMP_results_gallery_v13.html"
OUT = ROOT / "reports/JMP_results_gallery_v14.html"


def main() -> None:
    document = SOURCE.read_text(encoding="utf-8")
    anchor = "<p class=lead>" + sections.PERSPECTIVES_SENTENCE + "</p>"
    if document.count(anchor) != 1:
        raise RuntimeError("welfare-panel framing sentence not found exactly once")
    data = base64.b64encode(inputs.THEORY_FIG.read_bytes()).decode()
    figure = ('<figure class=""><img alt="Own-set equal-consumption equivalents: the theoretical construction" '
              f'src="data:image/png;base64,{data}" data-fig="fig_v14_theory_own_set">'
              f"<figcaption>{inputs.THEORY_CAPTION}</figcaption></figure>"
              f"<p>{sections.THEORY_BRIDGE}</p>")
    document = document.replace(anchor, anchor + figure, 1)
    document = document.replace("Reader-facing evidence · V13", "Reader-facing evidence · V14")
    for which in ("BEGIN", "END"):
        document = document.replace(f"<!-- V13_PROVENANCE_APPENDIX_{which} -->",
                                    f"<!-- V14_PROVENANCE_APPENDIX_{which} -->")
    if document.count("<figure") + document.count("<figcaption class=standalone>") != document.count("<figcaption"):
        raise RuntimeError("a gallery figure is missing its caption")
    OUT.write_text(document, encoding="utf-8", newline="\n")
    print(f"wrote {OUT} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
