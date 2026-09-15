"""Reader-facing sections for the V16 research-story report (V19-C2 corrections).

V16 keeps every V15 section and changes exactly four passages; no number,
figure, table or other sentence changes.

1. The opportunity-density equation: access applies to market jobs only and
   non-employment is normalised, as in the executed criterion (the access index
   and all access shifters multiply the working indicator; the non-employment row
   has log g = 0).
2. Section 2: the likelihood does not floor non-positive simulated consumption;
   such alternatives lie outside the choice domain and are excluded.
3. Appendix, likelihood record: the same correction.
4. Appendix, attained-bundle simulation record: the "neither route" sentence
   now says that the simulation is the executed preliminary decomposition and
   names the two proposed final routes (wording from the V11 report) that are
   not executed. It does not claim that a final route has been completed.
"""
from __future__ import annotations

import v15_sections as v15

TITLE = v15.TITLE
D_STATUS = v15.D_STATUS
PERSPECTIVES_SENTENCE = v15.PERSPECTIVES_SENTENCE
INTERPRETATION_SENTENCE = v15.INTERPRETATION_SENTENCE
ABSTRACT = v15.ABSTRACT
PRELIM_NOTE = v15.PRELIM_NOTE
reader_voice = v15.reader_voice

CORRECTIONS = [
    ("opportunity-density equation",
     "g_i(j)=g^{E}_i\\cdot\\left(g^{H}_i(h)\\cdot g^{\\mathrm{Occ}}_i(k)\\cdot\n"
     "g^{W}_i(w\\mid k)\\right)^{E_i(j)} .",
     "g_i(j)=\\left(g^{E}_i\\cdot g^{H}_i(h)\\cdot g^{\\mathrm{Occ}}_i(k)\\cdot\n"
     "g^{W}_i(w\\mid k)\\right)^{E_i(j)},\\qquad g_i(o)=1 ."),
    ("Section 2 likelihood floor description",
     "non-positive *simulated* alternatives receive a one-euro consumption floor before "
     "utility is evaluated. Those are sampled alternatives entering the estimated choice "
     "likelihood.",
     "non-positive *simulated* alternatives lie outside the household's choice domain and "
     "are excluded from the estimated choice likelihood; no consumption floor is applied."),
    ("appendix likelihood floor description",
     "Non-positive simulated consumption receives a one-euro floor inside this\n"
     "likelihood only.",
     "Sampled alternatives with non-positive simulated consumption lie outside the\n"
     "household's choice domain and are excluded from this likelihood; no consumption\n"
     "floor is applied."),
    ("final-route sentence",
     "Neither\ncounterfactual-attainment route for a final decomposition is executed here.",
     "This simulation\n"
     "is the executed preliminary decomposition. Two routes proposed for a final\n"
     "counterfactual-attainment decomposition are not executed here: a realised-bundle\n"
     "route that conditions the behavioural latent state on the observed choice, and an\n"
     "ex-ante route that integrates attained welfare over the model-implied\n"
     "counterfactual choice distribution before inequality is measured."),
]

SECTIONS = []
_hits = {label: 0 for label, _, _ in CORRECTIONS}
for _section in v15.SECTIONS:
    _new = dict(_section)
    body = _section["body"]
    for label, old, new in CORRECTIONS:
        n = body.count(old)
        if n:
            _hits[label] += n
            body = body.replace(old, new)
    _new["body"] = body
    SECTIONS.append(_new)
_bad = {k: v for k, v in _hits.items() if v != 1}
if _bad:
    raise RuntimeError("V16 correction anchors not found exactly once: %s" % _bad)

QA = list(v15.QA)
