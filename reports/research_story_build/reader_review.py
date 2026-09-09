# -*- coding: utf-8 -*-
"""Reader self-review: read the built page as the target reader would - an
economist who knows mathematics but has never seen this computer - and list
(a) technical terms used but not defined, (b) process vocabulary in the body,
(c) sentences that need file access to follow."""
import pathlib
import re
import sys
from html.parser import HTMLParser

HTML = pathlib.Path(r"C:\Users\hisham\Repo\Job_Market_paper\reports"
                    r"\JMP_research_story_report_v2.html")


class Doc(HTMLParser):
    """Rendered text per section; provenance boxes and <code> kept apart."""

    SKIP = {"script", "style"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.on = False
        self.sec = "front"
        self.text, self.prov, self.code = {}, {}, {}
        self.d_skip = self.d_prov = self.d_code = 0
        self.stack = []

    def _t(self):
        if self.d_code:
            return self.code.setdefault(self.sec, [])
        if self.d_prov:
            return self.prov.setdefault(self.sec, [])
        return self.text.setdefault(self.sec, [])

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if d.get("id") == "doc":
            self.on = True
        if not self.on:
            return
        mark = None
        if tag in self.SKIP:
            self.d_skip += 1
            mark = "skip"
        if tag == "h2" and re.fullmatch(r"s\d+", d.get("id") or ""):
            self.sec = d["id"]
        if "prov" in set((d.get("class") or "").split()):
            self.d_prov += 1
            mark = "prov"
        if tag == "code":
            self.d_code += 1
            mark = "code"
        self.stack.append([tag, mark])

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if self.stack:
            self._pop(self.stack.pop()[1])

    def _pop(self, mark):
        if mark == "skip":
            self.d_skip -= 1
        elif mark == "prov":
            self.d_prov -= 1
        elif mark == "code":
            self.d_code -= 1

    def handle_endtag(self, tag):
        if not self.on:
            return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                for _, mark in self.stack[i:]:
                    self._pop(mark)
                del self.stack[i:]
                return

    def handle_data(self, data):
        if self.on and not self.d_skip:
            self._t().append(data)


p = Doc()
p.feed(HTML.read_text(encoding="utf-8"))

BODY = {k: re.sub(r"\s+", " ", " ".join(v)) for k, v in p.text.items()}
PROV = {k: re.sub(r"\s+", " ", " ".join(v)) for k, v in p.prov.items()}
CODE = {k: re.sub(r"\s+", " ", " ".join(v)) for k, v in p.code.items()}
ALLBODY = " ".join(BODY.values())

# ---- (a) technical terms that must be defined ---------------------------
TERMS = {
    "cluster-robust standard error": r"cluster(ed)?[- ]robust|clustered on the household",
    "randomised quasi-Monte Carlo": r"quasi-Monte Carlo|RQMC",
    "jackknife band": r"jackknife",
    "Shapley value": r"Shapley",
    "Owen value": r"Owen",
    "Box-Cox transformation": r"Box.Cox",
    "importance sampling": r"importance sampl",
    "proposal density": r"proposal density",
    "quadrature support": r"quadrature",
    "money metric": r"money metric",
    "equivalent income": r"equivalent income",
    "equivalence scale": r"equivalence scale",
    "EUROMOD": r"EUROMOD",
    "sampled-alternatives likelihood": r"sampled.alternatives likelihood|sampled-set likelihood",
    "active bound": r"active bound",
}
gloss = BODY.get("s24", "")
undefined = []
for term, rx in TERMS.items():
    used = bool(re.search(rx, ALLBODY, re.I))
    defined = bool(re.search(rx, gloss, re.I))
    if used and not defined:
        undefined.append(term)

# ---- (b) process vocabulary in the body ---------------------------------
PROCESS = [r"\bsession\b", r"\bcard\b", r"\bruling\b", r"\bmission\b",
           r"\bgate\b", r"\bgates\b", r"\bsprint\b", r"\bdeputy\b",
           r"\bcertified\b", r"\bfrozen artefact\b", r"\bartefact\b",
           r"\bregistry\b", r"\bcommit\b", r"\bpinned\b", r"\bof record\b"]
proc = []
for sec, txt in sorted(BODY.items()):
    for rx in PROCESS:
        for m in re.finditer(rx, txt, re.I):
            proc.append((sec, m.group(0),
                         txt[max(0, m.start() - 60):m.end() + 60]))

# ---- (c) file paths and identifiers in the body -------------------------
PATHS = [r"[A-Za-z_0-9]+\.(?:py|json|csv|parquet|ipynb|md|png|yaml)",
         r"\b[a-z_]+/[a-z_0-9/]+\b", r"\bSPRINT\b", r"\bMNL\b", r"\bJMP\b"]
paths = []
for sec, txt in sorted(BODY.items()):
    for rx in PATHS:
        for m in re.finditer(rx, txt):
            paths.append((sec, m.group(0),
                          txt[max(0, m.start() - 50):m.end() + 50]))

out = []
out.append("UNDEFINED TECHNICAL TERMS (used in the body, absent from the glossary)")
out.append("  " + (", ".join(undefined) if undefined else "none"))
out.append("")
out.append("PROCESS VOCABULARY IN THE BODY  (%d hits)" % len(proc))
seen = set()
for sec, w, ctx in proc:
    k = (sec, w.lower())
    if k in seen:
        continue
    seen.add(k)
    out.append("  %-6s %-14s ...%s..." % (sec, w, ctx.strip()[:110]))
out.append("")
out.append("FILE PATHS / REPOSITORY IDENTIFIERS IN THE BODY  (%d hits)" % len(paths))
seen = set()
for sec, w, ctx in paths:
    k = (sec, w)
    if k in seen:
        continue
    seen.add(k)
    out.append("  %-6s %-34s ...%s..." % (sec, w, ctx.strip()[:90]))
out.append("")
out.append("PROVENANCE BOXES (exempt): sections %s"
           % (", ".join(sorted(PROV)) or "none"))
out.append("CODE SPANS (exempt): %d sections carry <code> identifiers"
           % len(CODE))

txt = "\n".join(out)
sys.stdout.reconfigure(encoding="utf-8")
print(txt)
pathlib.Path(sys.argv[1]).write_text(txt, encoding="utf-8")
