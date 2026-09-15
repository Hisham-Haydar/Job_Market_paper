"""Reader-facing sections for the V13 research-story report (figures release).

V13 keeps the V12 text and structure and adds four figures regenerated from the
certified records: the decomposition architecture (Section 4), the attained-bundle
and ex-ante Shapley contributions (Section 5), and the central two-perspective
comparison (Section 5, "The central result"). No number changes.
"""
from __future__ import annotations

import v11_sections as v11
import v12_sections as v12

TITLE = v12.TITLE
D_STATUS = v12.D_STATUS
PERSPECTIVES_SENTENCE = v12.PERSPECTIVES_SENTENCE
INTERPRETATION_SENTENCE = v12.INTERPRETATION_SENTENCE
ABSTRACT = v12.ABSTRACT
PRELIM_NOTE = v12.PRELIM_NOTE
reader_voice = v12.reader_voice
_replace_once = v11._replace_once

DECOMPOSITION = [s for s in v12.SECTIONS if s["key"] == "decomposition"][0]["body"]
DECOMPOSITION = _replace_once(
    DECOMPOSITION,
    "the sources of welfare inequality.\n",
    "the sources of welfare inequality.\n\n"
    "The figure maps the exercise before the formal objects. Any combination of the "
    "three channels is equalised to a common reference while household resources, "
    "needs and composition stay fixed; the resulting counterfactual household is "
    "evaluated under both welfare perspectives, inequality is measured, and the "
    "Shapley rule allocates the change.\n\n{{figure:v13architecture}}\n",
)

RESULTS = v12.RESULTS
RESULTS = _replace_once(
    RESULTS, "{{table:decomposition_reader}}",
    "{{table:decomposition_reader}}\n\n{{figure:v13attdecomp}}",
)
RESULTS = _replace_once(
    RESULTS, "{{table:wea_results}}",
    "{{table:wea_results}}\n\n{{figure:v13eadecomp}}",
)
RESULTS = _replace_once(
    RESULTS, "{{table:perspective_comparison}}",
    "{{figure:v13central}}\n\n{{table:perspective_comparison}}",
)

SECTIONS = []
for _section in v12.SECTIONS:
    _new = dict(_section)
    _new["body"] = {"decomposition": DECOMPOSITION, "results": RESULTS}.get(_section["key"], _section["body"])
    SECTIONS.append(_new)

QA = []
