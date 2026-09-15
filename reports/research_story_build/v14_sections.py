"""Reader-facing sections for the V14 research-story report (theory figure).

V14 keeps the V13 text, structure and figures, and restores the deterministic
own-set equal-consumption figure at the start of Section 3, immediately after
the two-perspective framing and before Perspective 1. No number changes.
"""
from __future__ import annotations

import v11_sections as v11
import v13_sections as v13

TITLE = v13.TITLE
D_STATUS = v13.D_STATUS
PERSPECTIVES_SENTENCE = v13.PERSPECTIVES_SENTENCE
INTERPRETATION_SENTENCE = v13.INTERPRETATION_SENTENCE
ABSTRACT = v13.ABSTRACT
PRELIM_NOTE = v13.PRELIM_NOTE
reader_voice = v13.reader_voice
_replace_once = v11._replace_once

THEORY_INTRO = (
    "**The deterministic construction.** Both money metrics descend from a construction in the "
    "companion theory paper, drawn below before any algebra. Two individuals share the same "
    "preferences over consumption and jobs but can take different sets of jobs, and each "
    "attains a different bundle. Give every job in an individual's own set the same "
    "consumption; the individual then prefers one of those jobs, and the consumption level at "
    "which that preferred job is exactly as good as the attained bundle is the money metric. "
    "The figure is a theoretical illustration: it contains no estimated value, no household "
    "data and no result."
)

THEORY_BRIDGE = (
    "The estimated attained-bundle measure should not be read as using a rich set of reference "
    "jobs like the one drawn here. Its reference is non-employment: on the current empirical "
    "domain non-employment is the job every household prefers when all jobs pay the same, so "
    "the reference collapses to that single state. The ex-ante measure keeps the "
    "equal-consumption idea but applies it to the household's estimated opportunity prospect "
    "instead of a known set of jobs, as Perspective 2 shows."
)

WELFARE = [s for s in v13.SECTIONS if s["key"] == "money"][0]["body"]
WELFARE = _replace_once(
    WELFARE,
    PERSPECTIVES_SENTENCE + "\n\n",
    PERSPECTIVES_SENTENCE + "\n\n" + THEORY_INTRO + "\n\n{{figure:v14theory}}\n\n" + THEORY_BRIDGE + "\n\n",
)

SECTIONS = []
for _section in v13.SECTIONS:
    _new = dict(_section)
    if _section["key"] == "money":
        _new["body"] = WELFARE
    SECTIONS.append(_new)

QA = []
