#!/usr/bin/env python
"""Build the V10 gallery: Stage A release-language correction of V9 only.

Everything is copied verbatim from JMP_results_gallery_v9.html except: the
"Distinct ex-ante metric" provenance warn-box, which still asserted the
old blocked/no-result status, and the version label. No number, table or
figure changes.
"""
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "reports/JMP_results_gallery_v9.html"
OUT = ROOT / "reports/JMP_results_gallery_v10.html"
BEGIN_V9 = "<!-- V9_PROVENANCE_APPENDIX_BEGIN -->"
END_V9 = "<!-- V9_PROVENANCE_APPENDIX_END -->"
BEGIN_V10 = "<!-- V10_PROVENANCE_APPENDIX_BEGIN -->"
END_V10 = "<!-- V10_PROVENANCE_APPENDIX_END -->"

OLD_ARTICLE = (
    "<h3>Distinct ex-ante metric</h3><p>W_EA_flat is definition-only and "
    "numerically blocked. Under the primary full-environment domain, "
    "non-positive-consumption states contribute zero to the actual "
    "functional through the limiting rule and remain in the flat "
    "reference with common consumption. No numerical result is "
    "reported.</p></article>"
)

CURRENT_STATUS = (
    "The ex-ante calculation has been completed and passed the numerical "
    "checks documented here. Its results remain conditional on the "
    "estimated model, reference convention and specified counterfactual "
    "operators. This numerical certification establishes that the "
    "computation is correct given the model and operators; it does not "
    "establish causal identification, does not quantify statistical "
    "uncertainty in the estimated parameters, and does not establish "
    "that either welfare perspective is the normatively correct one. "
    "See the results section above and the research-story report&#8217;s "
    "certified ex-ante calculation record for the current results."
)

NEW_ARTICLE = (
    "<h3>Distinct ex-ante metric</h3>"
    "<p><em>Superseded before V9.</em> The sentence immediately below is "
    "reproduced unchanged from an earlier report version and describes "
    "that version&#8217;s status only, not the current one. "
    + CURRENT_STATUS + "</p>"
    "<p>W_EA_flat is definition-only and numerically blocked. Under the "
    "primary full-environment domain, non-positive-consumption states "
    "contribute zero to the actual functional through the limiting rule "
    "and remain in the flat reference with common consumption. No "
    "numerical result is reported.</p></article>"
)


def main() -> None:
    document = SOURCE.read_text(encoding="utf-8")

    count = document.count(OLD_ARTICLE)
    if count != 1:
        raise RuntimeError(
            f"expected exactly one stale 'Distinct ex-ante metric' article, "
            f"found {count}"
        )
    document = document.replace(OLD_ARTICLE, NEW_ARTICLE, 1)

    document = document.replace("Reader-facing evidence · V9",
                                "Reader-facing evidence · V10")
    document = document.replace(BEGIN_V9, BEGIN_V10).replace(END_V9, END_V10)
    if document.count(BEGIN_V10) != 1 or document.count(END_V10) != 1:
        raise RuntimeError("V10 gallery must contain exactly one appendix marker pair")

    OUT.write_text(document, encoding="utf-8", newline="\n")
    print(f"wrote {OUT} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
