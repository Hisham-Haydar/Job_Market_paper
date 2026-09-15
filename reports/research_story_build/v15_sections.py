"""Reader-facing sections for the V15 research-story report (theory figure restore).

V15 keeps the V14 text and structure, replaces the two-panel regeneration with
the original stored theory figure (byte-identical to the V4-V11 copy), and
corrects the surrounding text: the construction does not require identical
preferences between the two individuals -- each is evaluated with their own
preferences and their own ability set, and the figure's point is that the
resulting money metrics are directly comparable. No number changes.
"""
from __future__ import annotations

import v11_sections as v11
import v14_sections as v14

TITLE = v14.TITLE
D_STATUS = v14.D_STATUS
PERSPECTIVES_SENTENCE = v14.PERSPECTIVES_SENTENCE
INTERPRETATION_SENTENCE = v14.INTERPRETATION_SENTENCE
ABSTRACT = v14.ABSTRACT
PRELIM_NOTE = v14.PRELIM_NOTE
reader_voice = v14.reader_voice
_replace_once = v11._replace_once

THEORY_INTRO = (
    "**The deterministic construction.** Both money metrics descend from a construction in the "
    "companion theory paper, drawn below before any algebra. Two individuals, each with their "
    "own preferences and their own set of jobs they are able to take, attain different bundles. "
    "For each individual, give every job in their own set the same consumption; that individual "
    "then prefers one of those jobs, and the consumption level at which that preferred job is "
    "exactly as good as the attained bundle is their money metric. The construction's point is "
    "that the two individuals' money metrics, built this way, are directly comparable even "
    "though their preferences and job sets differ. The figure is a theoretical illustration: it "
    "contains no estimated value, no household data and no result."
)

WELFARE = _replace_once(v14.WELFARE, v14.THEORY_INTRO, THEORY_INTRO)
WELFARE = _replace_once(WELFARE, "{{figure:v14theory}}", "{{figure:theory}}")

SECTIONS = []
for _section in v14.SECTIONS:
    _new = dict(_section)
    if _section["key"] == "money":
        _new["body"] = WELFARE
    SECTIONS.append(_new)

QA: list = []
