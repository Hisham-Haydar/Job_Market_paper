"""V10 report sections: Stage A release-language correction only.

V10 makes exactly one class of edit relative to V9: inside the inherited
technical-record appendix, predecessor-version sentences that still assert
the ex-ante opportunity-prospect metric is undefined, blocked, or has no
numerical result are labelled as superseded-before-V9 historical
quotations and are immediately followed by the current, certified status.

No economic content, table, figure, section structure or numerical value
changes here. See JMP_v9_to_v10_release_consistency_v1.md for the full
audit (every stale location found, and why nothing else was touched).
"""
from __future__ import annotations

import v7_sections as v7
import v9_sections as v9


TITLE = v9.TITLE
ABSTRACT = v9.ABSTRACT
PRELIM_NOTE = v9.PRELIM_NOTE
reader_voice = v9.reader_voice


CURRENT_STATUS = (
    "The ex-ante calculation has been completed and passed the numerical "
    "checks documented here. Its results remain conditional on the "
    "estimated model, reference convention and specified counterfactual "
    "operators."
)

CERTIFICATION_SCOPE = (
    "This numerical certification establishes that the computation is "
    "correct given the model and operators; it does not establish causal "
    "identification, does not quantify statistical uncertainty in the "
    "estimated parameters, and does not establish that either welfare "
    "perspective is the normatively correct one."
)

POINTER = (
    "See “Ex-ante well-being and decomposition” in the main text "
    "and “Certified ex-ante calculation” below for the current, "
    "certified results."
)

SUPERSEDED_NOTE = (
    "*Superseded before V9.* The sentence(s) immediately below are "
    "reproduced unchanged from an earlier report version and describe "
    "that version's status only, not the current one. " + CURRENT_STATUS
    + " " + CERTIFICATION_SCOPE + " " + POINTER
)


def _label_superseded(text: str, old: str) -> str:
    if old not in text:
        raise RuntimeError(
            "expected superseded ex-ante status passage not found: "
            + old[:80]
        )
    return text.replace(old, SUPERSEDED_NOTE + "\n\n" + old)


_q26_answer = next(
    a for q, a in v7.QA
    if q == "Is the ex-ante opportunity-prospect metric a result?"
)

PROVENANCE = v9.PROVENANCE
# The three verbatim WEA_STATUS occurrences inherited from v7_sections.py
# (Technical record: Introduction; "The distinct ex-ante opportunity-
# prospect metric"; and the "What is not established" sensitivity block).
PROVENANCE = _label_superseded(PROVENANCE, v7.WEA_STATUS)
# The Q&A item 26 answer ("Is the ex-ante opportunity-prospect metric a
# result?"), reproduced verbatim inside the same collapsed appendix.
PROVENANCE = _label_superseded(PROVENANCE, _q26_answer)

# The certified-results record itself already states the certification is
# conditional on the model; make the causal/statistical/normative scoping
# explicit at the point where the certification gates are described
# (addendum A3).
_CERT_ANCHOR = "### Certification gates\n"
if _CERT_ANCHOR not in PROVENANCE:
    raise RuntimeError("certification gates heading not found for V10 scope note")
PROVENANCE = PROVENANCE.replace(
    _CERT_ANCHOR,
    _CERT_ANCHOR + "\n" + CERTIFICATION_SCOPE + "\n",
    1,
)
if CERTIFICATION_SCOPE not in PROVENANCE:
    raise RuntimeError("V10 certification scope caveat failed to attach")


SECTIONS = [dict(section) for section in v9.SECTIONS]
for _section in SECTIONS:
    if _section["key"] == "provenance":
        _section["body"] = PROVENANCE

QA = list(v9.QA)
