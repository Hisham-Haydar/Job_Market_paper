#!/usr/bin/env python
"""Build the V15 gallery from the V14 gallery: swap the theory figure only.

Replaces the V14 two-panel regeneration (image, alt text and figcaption) with
the original stored image (byte-identical to the V4-V11 copy) and the
corrected, plain-text caption. The bridging paragraph after the figure
(non-employment reference) is unchanged. Every other byte of the V14 gallery
is kept, apart from the version label and appendix markers.
"""
from __future__ import annotations

import base64
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "reports/research_story_build"))
import v15_render_inputs as inputs  # noqa: E402

SOURCE = ROOT / "reports/JMP_results_gallery_v14.html"
OUT = ROOT / "reports/JMP_results_gallery_v15.html"


def main() -> None:
    document = SOURCE.read_text(encoding="utf-8")

    old_fig_pattern = re.compile(
        r'<figure class=""><img alt="[^"]*" src="data:image/png;base64,[A-Za-z0-9+/=]+" '
        r'data-fig="fig_v14_theory_own_set"><figcaption>.*?</figcaption></figure>',
        flags=re.S,
    )
    matches = old_fig_pattern.findall(document)
    if len(matches) != 1:
        raise RuntimeError(f"expected exactly one V14 theory figure block, found {len(matches)}")
    new_data = base64.b64encode(inputs.THEORY_FIG.read_bytes()).decode()
    new_figure = (f'<figure class=""><img alt="Own-set equal-consumption equivalents" '
                  f'src="data:image/png;base64,{new_data}" data-fig="theory_w1">'
                  f"<figcaption>{inputs.THEORY_CAPTION_GALLERY}</figcaption></figure>")
    document = old_fig_pattern.sub(new_figure, document, count=1)

    document = document.replace("Reader-facing evidence · V14", "Reader-facing evidence · V15")
    for which in ("BEGIN", "END"):
        document = document.replace(f"<!-- V14_PROVENANCE_APPENDIX_{which} -->",
                                    f"<!-- V15_PROVENANCE_APPENDIX_{which} -->")
    if document.count("<figure") + document.count("<figcaption class=standalone>") != document.count("<figcaption"):
        raise RuntimeError("a gallery figure is missing its caption")
    OUT.write_text(document, encoding="utf-8", newline="\n")
    print(f"wrote {OUT} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
