# -*- coding: utf-8 -*-
"""Replicate the in-browser self-check in Python, so the build can be gated.

Classification of every numeral found in the document body:

  BOUND        rendered from a key in one of the two embedded data blocks
  LITERAL      a declared non-result numeral (band edge, age bound, year, ...)
  STRUCTURAL   inside <code>, a heading, a table header or a figure caption:
               an identifier, a name or a label, never a result
  CROSSREF     "section 12", "block 5", a "13-18" range: navigation
  PROPER       a proper noun that contains a digit (NUTS-1, EU-LFS, PT1, ...)
  STRAY        anything else -> FAILURE
"""
from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

OUT = Path("C:/Users/hisham/Repo/Job_Market_paper/reports/"
           "JMP_research_story_report_v1.html")

html = OUT.read_text(encoding="utf-8")


def grab(idname: str):
    m = re.search(r'<script id="%s" type="application/json">(.*?)</script>' % idname,
                  html, re.S)
    return json.loads(m.group(1))


NOR = grab("NOR-DATA")
AUX = grab("AUX-DATA")

MISSING = object()


def lookup(src: str, key: str):
    if src == "nor":
        e = NOR["entries"].get(key)
        return MISSING if e is None else e.get("value")
    cur = AUX
    for part in key.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return MISSING
        cur = cur[part]
    return cur


SKIP_CLASSES = {"n", "lit", "eq", "exempt"}
SKIP_TAGS = {"script", "style", "code", "h1", "h2", "h3", "h4", "th", "figcaption"}

RANGE = re.compile(r"\d+(?:\.\d+)?\s*[\u2013\u2014-]\s*\d+(?:\.\d+)?")
# "section 12", "sections 15 and 19.2", "blocks 2 to 5", "section 19.6"
CROSSREF = re.compile(
    r"\b(?:sub)?(?:sections?|blocks?|figures?|parts?|steps?|points?|tables?)"
    r"\s*\u00a0?\s*\d+(?:\.\d+)?"
    r"(?:\s*(?:,|and|to|&amp;|&)\s*\d+(?:\.\d+)?)*", re.I)
PROPER = re.compile(
    r"\b(?:NUTS-\d|ISCO-\d+|EU-SILC|EU-LFS|SRCV|PT1|PT2|F35|FT|LH|R-\d+)\b")


class Doc(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack: list[tuple[str, set, str]] = []
        self.spans: list[tuple[str, str, str]] = []
        self.lits: list[tuple[str, str]] = []
        self.structural = 0
        self.crossrefs: list[str] = []
        self.stray: list[str] = []
        self.in_doc = False
        self._why = ""

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        cls = set((d.get("class") or "").split())
        eid = d.get("id", "")
        if eid == "doc":
            self.in_doc = True
        if not self.in_doc:
            return
        self.stack.append((tag, cls, eid))
        if "n" in cls and d.get("data-k"):
            self.spans.append((d.get("data-src", "nor"), d["data-k"],
                               d.get("data-f", "auto")))
        if "lit" in cls:
            self._why = d.get("data-why", "")

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if self.stack:
            self.stack.pop()

    def handle_endtag(self, tag):
        if not self.in_doc:
            return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        if not self.in_doc or not re.search(r"[0-9]", data):
            return
        classes = set()
        tags = set()
        in_selfcheck = False
        for tag, cls, eid in self.stack:
            tags.add(tag)
            classes |= cls
            if eid == "s23":
                in_selfcheck = True
        if in_selfcheck:
            return
        if "lit" in classes:
            self.lits.append((data.strip(), self._why))
            return
        if classes & SKIP_CLASSES:
            return
        if tags & SKIP_TAGS:
            self.structural += 1
            return

        txt = re.sub(r"\s+", " ", data).strip()
        if not txt:
            return
        rest = PROPER.sub(" ", txt)
        rest = RANGE.sub(" ", rest)
        rest = CROSSREF.sub(" ", rest)
        if re.search(r"[0-9]", rest):
            self.stray.append(rest.strip()[:200])
        else:
            self.crossrefs.append(txt[:110])


p = Doc()
p.feed(html)

missing = [(s, k) for (s, k, f) in p.spans if lookup(s, k) is MISSING]
keys = sorted({(s, k) for (s, k, f) in p.spans})
used_nor = {k for (s, k) in keys if s == "nor"}
unused = sorted(set(NOR["entries"]) - used_nor)

print("=" * 70)
print("SELF-CHECK  (Python replication of the in-page audit)")
print("=" * 70)
print("bound numerals           %d   over %d distinct keys (nor %d / aux %d)"
      % (len(p.spans), len(keys), len(used_nor), len(keys) - len(used_nor)))
print("declared literals        %d" % len(p.lits))
print("structural / identifier  %d" % p.structural)
print("cross-references         %d" % len(p.crossrefs))
print("numbers file             %d entries, %d cited, %d uncited"
      % (len(NOR["entries"]), len(used_nor), len(unused)))
print()
ok_a = not missing
ok_b = not p.stray
print("CHECK A  every bound numeral resolves to a key   : %s"
      % ("PASS" if ok_a else "FAIL (%d)" % len(missing)))
for s, k in missing:
    print("     MISSING  %s:%s" % (s, k))
print("CHECK B  no unclassified numeral in the prose    : %s"
      % ("PASS" if ok_b else "FAIL (%d)" % len(p.stray)))
for t in dict.fromkeys(p.stray):
    print("     STRAY    %s" % t)
print()
print("size  %.2f MB" % (len(html.encode("utf-8")) / 1024 / 1024))
sys.exit(0 if (ok_a and ok_b) else 1)
