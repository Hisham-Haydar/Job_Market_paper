# -*- coding: utf-8 -*-
"""Consistency gate — the executable form of reports/consistency_gate_spec_v1.md.

Usage:  python reports/run_consistency_gate.py [--out reports/consistency_gate_v2.md]

Reads the five artifacts named in the spec (J, P, H, D, N), applies the ten gate
items, and writes a markdown report.  Exit code 0 iff every (item, artifact) cell
is PASS or a justified N/A.

The spec is the authority; this file is only its implementation.  Where the spec
fixes a canonical string, that string appears here verbatim.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from html.parser import HTMLParser
from pathlib import Path

JMP = Path(__file__).resolve().parent.parent
MNL = JMP.parent / "MNL"

PATHS = {
    "J": JMP / "reports/numbers_of_record_v1.json",
    "P": JMP / "manuscript/JMP_working_paper_for_seminar_v2.md",
    "H": JMP / "reports/JMP_research_story_report_v1.html",
    "D": JMP / "manuscript/JMP_seminar_deck_content_v2.md",
    "N": MNL / "experiments/JMP_SEMINAR_SPRINT/JMP_research_lab.ipynb",
}

ARTS = ["P", "H", "D", "N"]
NAMES = {
    "P": "paper v2",
    "H": "story HTML",
    "D": "deck content v2.2",
    "N": "research-lab notebook (markdown)",
}

# --------------------------------------------------------------------------
# normalisation
# --------------------------------------------------------------------------

_LATEX_STRIP = [
    (re.compile(r"\\mathrm\{([^{}]*)\}"), r"\1"),
    (re.compile(r"\\mathbb\{([^{}]*)\}"), r"\1"),
    (re.compile(r"\\text\{([^{}]*)\}"), r"\1"),
    (re.compile(r"\\emph\{([^{}]*)\}"), r"\1"),
    (re.compile(r"\$W\^?\{?1\}?_?\{?i\}?\$"), "W1"),
    (re.compile(r"\$i\$"), "i"),
    (re.compile(r"[*`]"), ""),
    (re.compile(r"[$\\]"), ""),
]


def norm(s: str) -> str:
    """Markup-tolerant, case-folded, whitespace-collapsed form used for prose rules."""
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2013", "-").replace("\u2014", "-").replace("\u2212", "-")
    s = s.replace("&mdash;", "-").replace("&ndash;", "-").replace("&nbsp;", " ")
    s = s.replace("&amp;", "&").replace("&plusmn;", "\u00b1").replace("&minus;", "-")
    s = s.replace("\\(", "$").replace("\\)", "$")   # inline math, same as $ ... $
    for rx, rep in _LATEX_STRIP:
        s = rx.sub(rep, s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


# --------------------------------------------------------------------------
# artifact loading -> passages
# --------------------------------------------------------------------------

class Passage:
    __slots__ = ("art", "loc", "raw", "txt", "kind", "keys")

    def __init__(self, art, loc, raw, kind="prose", keys=None):
        self.art = art
        self.loc = loc
        self.raw = raw
        self.txt = norm(raw)
        self.kind = kind            # prose | code | provenance
        self.keys = keys or set()   # registry keys bound in this passage

    def __repr__(self):
        return "<%s %s>" % (self.art, self.loc)


def md_passages(art: str, path: Path, code_ok=False):
    """Split a markdown file into blank-line separated blocks, keeping line numbers."""
    lines = path.read_text(encoding="utf-8").splitlines()
    out, buf, start = [], [], 1
    for i, ln in enumerate(lines, 1):
        if ln.strip():
            if not buf:
                start = i
            buf.append(ln)
        else:
            if buf:
                out.append(Passage(art, "%d-%d" % (start, i - 1), "\n".join(buf)))
                buf = []
    if buf:
        out.append(Passage(art, "%d-%d" % (start, len(lines)), "\n".join(buf)))
    return out, lines


class DocParse(HTMLParser):
    """Rendered text layer of the story HTML, segmented by <h2 id="sNN">.

    Sections are h2-delimited, not <section>-wrapped.  Text inside a
    `<div class="box prov">` is collected separately: those are the permitted
    provenance sites of spec s10.
    """

    SKIP = {"script", "style"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_doc = False
        self.sec = "front"
        self.text = {}          # sec -> list of str  (prose)
        self.prov = {}          # sec -> list of str  (provenance boxes)
        self.code = {}          # sec -> list of str  (<code> spans)
        self.keys = {}          # sec -> set of data-k
        self.skip_depth = 0
        self.prov_depth = 0
        self.code_depth = 0
        self.stack = []
        self._pending_h2 = None

    def _t(self):
        if self.code_depth:
            return self.code.setdefault(self.sec, [])
        if self.prov_depth:
            return self.prov.setdefault(self.sec, [])
        return self.text.setdefault(self.sec, [])

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if d.get("id") == "doc":
            self.in_doc = True
        if not self.in_doc:
            return
        self.stack.append([tag, False])
        if tag in self.SKIP:
            self.skip_depth += 1
            self.stack[-1][1] = "skip"
        cls = set((d.get("class") or "").split())
        if tag == "h2" and re.fullmatch(r"s\d+", d.get("id") or ""):
            self.sec = d["id"]
        if tag == "code":
            self.code_depth += 1
            self.stack[-1][1] = "code"
        if "prov" in cls:
            self.prov_depth += 1
            self.stack[-1][1] = "prov"
        if d.get("data-k"):
            self.keys.setdefault(self.sec, set()).add(d["data-k"])
            self._t().append(" KEY:" + d["data-k"] + " ")

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if self.stack:
            _, mark = self.stack.pop()
            if mark == "skip":
                self.skip_depth -= 1
            elif mark == "prov":
                self.prov_depth -= 1
            elif mark == "code":
                self.code_depth -= 1

    def handle_endtag(self, tag):
        if not self.in_doc:
            return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                for _, mark in self.stack[i:]:
                    if mark == "skip":
                        self.skip_depth -= 1
                    elif mark == "prov":
                        self.prov_depth -= 1
                    elif mark == "code":
                        self.code_depth -= 1
                del self.stack[i:]
                return

    def handle_data(self, data):
        if self.in_doc and not self.skip_depth:
            self._t().append(data)


def html_passages():
    p = DocParse()
    p.feed(PATHS["H"].read_text(encoding="utf-8"))
    out = []
    for sec in sorted(set(p.text) | set(p.prov) | set(p.code)):
        out.append(Passage("H", sec, " ".join(p.text.get(sec, [])), "prose",
                           p.keys.get(sec, set())))
        if p.prov.get(sec):
            out.append(Passage("H", sec + " (provenance)",
                               " ".join(p.prov[sec]), "provenance"))
        if p.code.get(sec):
            out.append(Passage("H", sec + " (code)",
                               " ".join(p.code[sec]), "code"))
    return out, p


def nb_passages():
    nb = json.loads(PATHS["N"].read_text(encoding="utf-8"))
    md, code = [], []
    for i, c in enumerate(nb["cells"], 1):
        src = "".join(c["source"])
        if c["cell_type"] == "markdown":
            for j, blk in enumerate(re.split(r"\n\s*\n", src)):
                if blk.strip():
                    md.append(Passage("N", "cell %d/blk %d" % (i, j + 1), blk))
        else:
            outs = []
            for o in c.get("outputs", []):
                outs.extend(o.get("text", []))
                for k, v in (o.get("data") or {}).items():
                    if k in ("text/plain", "text/html"):
                        outs.extend(v if isinstance(v, list) else [v])
            code.append(Passage("N", "cell %d (code)" % i, src + "\n" + "".join(outs),
                                "code"))
    return md, code, nb


# --------------------------------------------------------------------------
# registry helpers
# --------------------------------------------------------------------------

J = json.loads(PATHS["J"].read_text(encoding="utf-8"))["entries"]


def val(k):
    return J[k]["value"]


POINT_PREFIXES = ("state_", "couples_state_", "C_", "couples_C_")


def point_keys():
    out = []
    for k in J:
        if not k.startswith(POINT_PREFIXES):
            continue
        if "__" in k or k.endswith("_share") or "_share_" in k:
            continue
        if k + "__rqmc_band" in J:
            out.append(k)
    return sorted(out)


def display_forms(v):
    """The report-precision renderings the gate treats as a print site."""
    forms = set()
    if isinstance(v, (int, float)):
        if abs(v) < 1e-12:
            return forms
        forms.add("%.6f" % abs(v))
    return forms


# --------------------------------------------------------------------------
# result plumbing
# --------------------------------------------------------------------------

class Item:
    def __init__(self, num, title):
        self.num = num
        self.title = title
        self.verdict = {}       # art -> PASS / FAIL / N/A
        self.evidence = {}      # art -> list of str

    def set(self, art, ok, note=None, na=False):
        self.verdict[art] = "N/A" if na else ("PASS" if ok else "FAIL")
        if note:
            self.evidence.setdefault(art, []).append(note)

    def fail(self, art, note):
        self.verdict[art] = "FAIL"
        self.evidence.setdefault(art, []).append(note)

    def note(self, art, note):
        self.evidence.setdefault(art, []).append(note)


ITEMS = []


def item(num, title):
    it = Item(num, title)
    ITEMS.append(it)
    return it


# --------------------------------------------------------------------------
# load
# --------------------------------------------------------------------------

P_PASS, P_LINES = md_passages("P", PATHS["P"])
D_PASS, D_LINES = md_passages("D", PATHS["D"])
H_PASS, H_DOC = html_passages()
N_MD, N_CODE, NB = nb_passages()

PROSE = {"P": P_PASS, "H": H_PASS, "D": D_PASS, "N": N_MD}
ALL = {"P": P_PASS, "H": H_PASS, "D": D_PASS, "N": N_MD + N_CODE}


def find(art, *needles, where=None):
    """Passages of `art` whose normalised text contains every needle."""
    src = (where or PROSE)[art]
    ns = [norm(x) for x in needles]
    return [p for p in src if all(n in p.txt for n in ns)]


def any_of(p, *needles):
    return any(norm(n) in p.txt for n in needles)



# --------------------------------------------------------------------------
# value presence: H renders numerals client-side, so it is checked on the key
# binding; P/D/N are checked on the printed numeral.
# --------------------------------------------------------------------------

VALUE_KEY = {
    "45.73": "C_nonlabour_female_raw_share",
    "12.45": "C_composition_female_raw_share",
    "33.25": "C_nonlabour_female_equivalized_share",
    "32.85": "C_composition_female_equivalized_share",
    "2.00": "one_factor_composition_raw",
    "6.3": "rum_share_pref_RURO_raw",
    "6.4": "rum_share_pref_RUMB_raw",
    "24.2": "rum_inequality_drop_raw",
    "0.428": "rum_leisure_gap_final",
    "1.991": "rum_leisure_gap_benchmark",
    "4.0": "rum_omitted_share_relabelled_as_preferences",
    "36.0": "rum_omitted_share_relabelled_as_needs",
    "68.0": "rum_omitted_share_leaves_measured_total",
    "87.6": "geo_share_of_C_acc_raw",
    "13.05": "geo_share_of_I00_raw",
    "1.019": "geo_share_of_C_acc_equivalized",
    "19.58": "subgroup_men_acc_share_raw",
    "9.79": "subgroup_women_acc_share_raw",
    "2.69": "subgroup_men_pref_share_female_ref",
    "2.78": "subgroup_men_pref_share_male_ref",
    "89.1": "s_env_female_raw__cr1_interval",
    "89.11": "s_env_female_raw__cr1_interval",
    "95.8": "s_env_female_raw__cr1_interval",
    "95.78": "s_env_female_raw__cr1_interval",
    "4.2": "s_pref_female_raw__cr1_interval",
    "4.22": "s_pref_female_raw__cr1_interval",
    "10.9": "s_pref_female_raw__cr1_interval",
    "10.89": "s_pref_female_raw__cr1_interval",
    "93.7": "C_env_female_raw_share",
}


def shows(passages, numstr):
    """True if the group of passages reports the quantity `numstr` names."""
    key = VALUE_KEY.get(numstr)
    for p in passages:
        if p.art == "H":
            if key and key in p.keys:
                return True
        elif numstr in p.raw.replace(",", ""):
            return True
    return False


# --------------------------------------------------------------------------
# section scope: items 5, 8 and 9 report a *block* that legitimately spans
# several paragraphs.  The scope for those items is the enclosing section:
# the <h2 id="sNN"> section in H (already one passage), the enclosing "##"/"###"
# heading block in P, the whole markdown cell in N, and the whole deck in D
# (slides are short and a block spans several of them).
# --------------------------------------------------------------------------

def _p_sections():
    heads = [i for i, ln in enumerate(P_LINES, 1)
             if ln.startswith("## ") or ln.startswith("### ")]
    heads.append(len(P_LINES) + 1)
    return [(heads[i], heads[i + 1] - 1) for i in range(len(heads) - 1)]


P_SECTIONS = _p_sections()


def scope(art, trig):
    """Expand a set of trigger passages to their enclosing sections."""
    if art == "H":
        return trig
    if art == "D":
        return PROSE["D"]
    if art == "N":
        cells = set()
        for p in trig:
            cells.add(p.loc.split("/")[0])
        return [p for p in PROSE["N"] if p.loc.split("/")[0] in cells]
    rngs = []
    for p in trig:
        lo = int(p.loc.split("-")[0])
        for a0, b0 in P_SECTIONS:
            if a0 <= lo <= b0:
                rngs.append((a0, b0))
                break
    out = []
    for p in PROSE["P"]:
        lo = int(p.loc.split("-")[0])
        if any(a0 <= lo <= b0 for a0, b0 in rngs):
            out.append(p)
    return out


# ==========================================================================
# ITEM 1 — notation
# ==========================================================================

FORBIDDEN_SYMBOLS = [
    "g^{acc}", "g^acc", "gacc", "log_gacc", "g^{market}", "g^market",
    "omega_ig", "\u03c9_ig", "working_ij", "age_i", "nkids_i",
]

it1 = item(1, "Notation — canonical symbols (spec \u00a71)")
for a in ARTS:
    bad = []
    for p in ALL[a]:
        # code cells may compute with any identifier; only *printed labels* count
        hay = p.txt
        for f in FORBIDDEN_SYMBOLS:
            if f in hay:
                if p.kind == "code" and f not in ("log_gacc", "g^{acc}", "g^market"):
                    continue
                bad.append("%s: `%s`" % (p.loc, f))
    # four-factor product statement
    prods = [p for p in PROSE[a]
             if re.search(r"g_?\{?ij\}?\s*(=|&=)", p.txt) or "g_{ij} =" in p.txt]
    for p in prods:
        have = sum(1 for s in ("g^{e}", "g^e") if s in p.txt), \
               sum(1 for s in ("g^{h}", "g^h") if s in p.txt)
        if not (any_of(p, "g^{E}", "g^E") and any_of(p, "g^{H}", "g^H")
                and any_of(p, "g^{Occ}", "g^{occ}", "g^occ")
                and any_of(p, "g^{W}", "g^W")):
            bad.append("%s: opportunity-density product is not the four canonical "
                       "factors" % p.loc)
    # F35 rule -- checked on the enclosing section, because a display equation is
    # its own block and its prose sits in the neighbouring one.
    for p in PROSE[a]:
        zero = ("f35" in p.txt
                and re.search(r"f35\}?\s*\}?\s*(\?equiv|≡|=)\s*0", p.txt))             or ("35-hour band" in p.txt and "reference" in p.txt
                and re.search(r"normali[sz]ed to zero", p.txt))
        if not zero:
            continue
        near = " ".join(q.txt for q in scope(a, [p]))
        if not any(x in near for x in ("opportunity peak", "35-hour peak",
                                       "adds one coefficient", "separately estimated",
                                       "beta_h_f35", "one coefficient on a 35-hour",
                                       "band step")):
            bad.append("%s: beta_F35 normalisation stated without naming the "
                       "separately estimated 35-hour peak" % p.loc)
    it1.set(a, not bad)
    for b in bad:
        it1.note(a, b)

# ==========================================================================
# ITEM 2 — the W1 statement
# ==========================================================================

W1_CORE = norm(
    "is the uniform pay that, offered at every job in household i's own "
    "opportunity distribution, reproduces the expected welfare the household "
    "actually attains")
PARAS = {
    "PARA-1": norm("the uniform pay across the jobs you can reach that would "
                   "leave you as well off"),
    "PARA-2": norm("the uniform pay across the jobs a household can reach that "
                   "would leave it exactly as well off as its actual "
                   "opportunity situation"),
    "PARA-3": norm("the uniform pay offered at every job in household i's own "
                   "opportunity distribution that reproduces the expected "
                   "welfare it actually attains"),
}
W1_FORBIDDEN = [
    "bc(w_i / needs_i", "bc(w_i/needs_i", "w_i / needs_i", "w_i/needs_i",
    "common reference household", "reference leisure",
    "lower bound within its own family", "lower bound on inequality",
]

it2 = item(2, "The W1 statement (spec \u00a72)")
for a in ARTS:
    bad = []
    hits = [p for p in PROSE[a] if W1_CORE in p.txt]
    para = [(pid, p) for pid, t in PARAS.items() for p in PROSE[a] if t in p.txt]
    if not hits and not para:
        bad.append("canonical W1 sentence absent, and no named paraphrase present")
    # three clauses
    clauses = {
        "C1 neutralises pay": any(
            re.search(r"neutrali[sz]\w*[^.]{0,160}\bpay\b|\bpay\b[^.]{0,160}"
                      r"neutrali[sz]", p.txt) for p in PROSE[a]),
        "C2 set differences remain": any(
            "differences in the set itself remain" in p.txt for p in PROSE[a]),
        "C3 same coalition both sides": any(
            "same coalition's set and preferences on both sides" in p.txt
            for p in PROSE[a]),
    }
    for name, ok in clauses.items():
        if not ok:
            bad.append("missing W1 clause: %s" % name)
    for p in PROSE[a]:
        for f in W1_FORBIDDEN:
            if f in p.txt:
                if f == "reference leisure" and a == "P" and "d.3" in p.txt:
                    continue
                bad.append("%s: forbidden W1 construction `%s`" % (p.loc, f))
    it2.set(a, not bad)
    if hits:
        it2.note(a, "canonical sentence at %s" % ", ".join(p.loc for p in hits[:3]))
    for pid, p in para[:3]:
        it2.note(a, "%s at %s" % (pid, p.loc))
    for b in bad:
        it2.note(a, b)

# ==========================================================================
# ITEM 3 — negLL labels
# ==========================================================================

NEGLL = {
    "negll_singles_final": ("singles final model negLL 18022.764617170084",
                            r"18022\.76", "18022.764617170084"),
    "negll_couples_final": ("couples clean baseline negLL 43493.342239066726",
                            r"43493\.34", "43493.342239066726"),
}
BAD_LABELS = ["objective value", "objective", "criterion"]

it3 = item(3, "negLL labels (spec \u00a73)")
for a in ARTS:
    bad, seen_any = [], False
    for key, (canon, rx, full) in NEGLL.items():
        sites = []
        for p in ALL[a]:
            if re.search(rx, p.txt) or ("key:" + key.lower()) in p.txt \
                    or key in p.txt:
                sites.append(p)
        if not sites:
            continue
        seen_any = True
        if norm(canon) not in " ".join(q.txt for q in ALL[a]):
            bad.append("L1: canonical label `%s` absent" % canon)
        for p in sites:
            if p.kind == "code":
                continue
            # L2/L3 are evaluated in a +/-400 character window around each print
            # site, not over the whole passage: a section may legitimately use the
            # word "objective" in an unrelated sentence.
            marks = [m.start() for m in re.finditer(rx, p.txt)]
            marks += [m.start() for m in re.finditer(re.escape(" key:" + key.lower()),
                                                     p.txt)]
            for i in marks or []:
                t = p.txt[max(0, i - 400):i + 400]
                named = ("negll" in t) or ("negative log-likelihood" in t)                     or ("negative log likelihood" in t)
                if not named:
                    bad.append("L2: %s prints %s without naming it negLL"
                               % (p.loc, key))
                for m in re.finditer(r"log[- ]likelihood", t):
                    pre = t[max(0, m.start() - 12):m.start()]
                    if "negative" not in pre:
                        bad.append("L2/L3: %s calls it an unqualified log-likelihood"
                                   % p.loc)
                        break
                for bl in BAD_LABELS:
                    if re.search(r"%s" % bl, t):
                        bad.append("L2: %s labels the quantity `%s`" % (p.loc, bl))
                        break
    # peak_negll_gain print sites
    for p in PROSE[a]:
        if re.search(r"430\.7", p.txt) and re.search(r"log[- ]likelihood", p.txt):
            m = re.search(r"log[- ]likelihood", p.txt)
            if "negative" not in p.txt[max(0, m.start() - 12):m.start()]:
                bad.append("L2: %s reports the 35-hour peak gain `in log-likelihood`"
                           % p.loc)
    if not seen_any and not bad:
        it3.set(a, True, "artifact reports neither negLL value", na=True)
    else:
        it3.set(a, not bad)
    for b in dict.fromkeys(bad):
        it3.note(a, b)

# ==========================================================================
# ITEM 4 — coverage: RQMC bands and CR1 intervals
# ==========================================================================

PK = point_keys()
# each endpoint at one or two decimals; either rendering satisfies COV-2
CR1_PCT = [("89.1", "89.11"), ("95.8", "95.78"),
           ("4.2", "4.22"), ("10.9", "10.89")]

it4 = item(4, "Coverage: RQMC bands and CR1 intervals (spec \u00a74)")
for a in ARTS:
    bad = []
    if a == "H":
        for p in H_PASS:
            for k in sorted(p.keys):
                if k in PK and (k + "__rqmc_band") not in p.keys:
                    bad.append("COV-1: section %s binds %s without its "
                               "__rqmc_band" % (p.loc, k))
        for p in H_PASS:
            if {"C_env_female_raw_share", "C_pref_female_raw_share"} & p.keys:
                if not ({"s_env_female_raw__cr1_interval",
                         "s_pref_female_raw__cr1_interval"} & p.keys):
                    bad.append("COV-2: section %s prints a headline share with no "
                               "CR1 interval" % p.loc)
    else:
        for p in PROSE[a]:
            hitk = []
            for k in PK:
                for f in display_forms(val(k)):
                    if f in p.raw.replace(",", ""):
                        hitk.append(k)
                        break
            bracket = re.search(r"\[\s*-?\d+\.\d+\s*,\s*-?\d+\.\d+\s*\]",
                                p.raw)
            if hitk and "±" not in p.raw and "+/-" not in p.raw                     and "band" not in p.txt and not bracket:
                bad.append("COV-1: %s prints %s with no band"
                           % (p.loc, ", ".join(sorted(set(hitk))[:4])))
    # COV-2 is artifact-level: an artifact that prints the headline shares must
    # also print both CR1 intervals and say the two uncertainties are distinct.
    if shows(PROSE[a], "93.7"):
        miss = [alts[0] for alts in CR1_PCT
                if not any(shows(PROSE[a], c) for c in alts)]
        if miss:
            bad.append("COV-2: headline shares printed; CR1 endpoints missing: %s"
                       % ", ".join(miss))
        if not any(any_of(p, "never merged", "not merged", "two different objects",
                          "two kinds of uncertainty") for p in PROSE[a]):
            bad.append("COV-3: no `the two uncertainties are never merged` "
                       "statement anywhere in the artifact")
    # COV-3 never merged / COV-4 CR1 arm restriction
    merged = [p for p in PROSE[a]
              if all(any(c in p.raw for c in alts) for alts in CR1_PCT)
              and not any_of(p, "never merged", "not merged",
                             "two different objects", "two kinds of uncertainty")]
    for p in merged:
        bad.append("COV-3: %s prints CR1 next to bands without the never-merged "
                   "statement" % p.loc)
    for p in PROSE[a]:
        if "cr1" in p.txt and re.search(r"male structural|equivalized", p.txt) \
                and re.search(r"cr1 interval[^.]{0,80}(male|equivalized)", p.txt) \
                and "only" not in p.txt and "no cr1" not in p.txt:
            bad.append("COV-4: %s appears to attach a CR1 interval to a "
                       "male-reference or equivalized quantity" % p.loc)
    it4.set(a, not bad)
    for b in dict.fromkeys(bad):
        it4.note(a, b)


# ==========================================================================
# ITEM 5 — nested endowments/needs, the six points
# ==========================================================================

it5 = item(5, "Nested endowments/needs semantics (spec \u00a75)")
NE_TRIGGER = ("non-labour resources", "c_nonlabour", "45.73",
              "household composition and needs")
for a in ARTS:
    trig = [p for p in PROSE[a] if any_of(p, *NE_TRIGGER)]
    if not trig:
        it5.set(a, True, "artifact does not report the nested split", na=True)
        continue
    trig = scope(a, trig)
    blob = " ".join(p.txt for p in trig)
    raw = " ".join(p.raw for p in trig)
    bad = []
    if not ("non-labour resources" in blob and
            ("household composition and needs" in blob
             or "composition and needs" in blob)):
        bad.append("NE-1: the two factors are not both named canonically")
    if not re.search(r"(common policy function|common to all|not a separate factor|"
                     r"no third factor|not a third factor|one common)", blob):
        bad.append("NE-2: no `tax-benefit schedule is common, not a third factor` "
                   "statement")
    if not (shows(trig, "12.45") and shows(trig, "2.00")):
        bad.append("NE-3: attributed 12.45 %% and one-factor 2.00 %% do not "
                   "appear together")
    if not re.search(r"(reference-dependent|is not claimed|not claimed|"
                     r"male arm reverses|reverses the equivalized)", blob):
        bad.append("NE-4: no `which leads is reference-dependent and is not "
                   "claimed` guard")
    for numstr in ("45.73", "12.45", "33.25", "32.85"):
        if not shows(trig, numstr):
            bad.append("NE-5: stored value %s not printed" % numstr)
    if not re.search(r"(not causal|non-causal|descriptive|structural, model-"
                     r"conditional|not a causal)", blob):
        bad.append("NE-6: no not-causal guard")
    if ("78.59" in raw or "21.41" in raw) and "of the needs channel" not in blob \
            and "share of the channel" not in blob:
        bad.append("NE-7: needs-channel shares printed without naming the "
                   "denominator")
    if "1.27" in raw and "band" in blob:
        bad.append("NE-8: the composed-from-parts share band (\u00b11.27) appears")
    it5.set(a, not bad)
    for b in dict.fromkeys(bad):
        it5.note(a, b)

# ==========================================================================
# ITEM 6 — reference labels
# ==========================================================================

it6 = item(6, "Reference labels (spec \u00a76)")
for a in ARTS:
    bad = []
    blob = " ".join(p.txt for p in PROSE[a])
    if "female-primary" not in blob:
        bad.append("REF-1: `female-primary` label absent")
    if "male structural-zero" not in blob and "male structural zero" not in blob:
        bad.append("REF-1: `male structural-zero` label absent")
    if "never averaged" not in blob:
        bad.append("REF-2: the `never averaged` statement is absent")
    for p in PROSE[a]:
        for m in re.finditer(r"nkids|children shifter|male child", p.txt):
            win = p.txt[max(0, m.start() - 300):m.end() + 300]
            if re.search(r"(?<!not )(?<!never )(estimated as zero|"
                         r"estimated at zero|not significant)", win):
                bad.append("REF-3: %s describes the male children shifter as "
                           "estimated as zero / not significant" % p.loc)
                break
    for p in PROSE[a]:
        if "couples" in p.txt and re.search(r"couples[^.]{0,120}"
                                            r"(female-primary|male structural)",
                                            p.txt):
            if "one shared" not in p.txt and "shared parameter vector" not in p.txt:
                bad.append("REF-4: %s applies the singles reference pair to "
                           "couples" % p.loc)
    it6.set(a, not bad)
    for b in dict.fromkeys(bad):
        it6.note(a, b)

# ==========================================================================
# ITEM 7 — couples beta_ll
# ==========================================================================

it7 = item(7, "Couples beta_ll (spec \u00a77)")
for a in ARTS:
    trig = [p for p in PROSE[a] if "beta_ll" in p.txt or "\u03b2_{\u2113\u2113}" in p.raw
            or "cross-leisure" in p.txt or "cross-spouse leisure" in p.txt]
    if not trig:
        it7.set(a, True, "artifact does not mention the cross-leisure term", na=True)
        continue
    blob = " ".join(p.txt for p in trig)
    bad = []
    if "absent" not in blob:
        bad.append("BLL-1: status ABSENT not stated")
    if not re.search(r"effective[^.]{0,80}=\s*0|effective(ly)? zero|"
                     r"zero in welfare|welfare_effective|exactly 0\.0", blob):
        bad.append("BLL-2: the welfare-effective 0.0 is not stated")
    if not re.search(r"not (an? )?(coordinate that was )?estimated|never estimated|"
                     r"not estimated|is not in the model at all|"
                     r"not an estimated-then-zeroed|imposed, not estimated", blob):
        bad.append("BLL-2: `not an estimated-then-zeroed coordinate` is not stated")
    if len(re.findall(r"boxcox|box-cox", blob)) < 2:
        bad.append("BLL-3: the cross-leisure functional form is not given")
    if not re.search(r"(limitation|cannot identify|not identified|weakness)", blob):
        bad.append("BLL-4: not stated as a named limitation")
    for p in ALL[a]:
        if re.search(r"beta_ll (was )?estimated|estimated beta_ll", p.txt):
            bad.append("%s: forbidden `beta_ll estimated`" % p.loc)
    it7.set(a, not bad)
    for b in dict.fromkeys(bad):
        it7.note(a, b)

# ==========================================================================
# ITEM 8 — the RUM block
# ==========================================================================

RUM_NUMS = ["6.3", "6.4", "24.2", "0.428", "1.991", "4.0", "36.0", "68.0"]

it8 = item(8, "The RUM block (spec \u00a78)")
for a in ARTS:
    trig = [p for p in PROSE[a]
            if any_of(p, "common-choice-set", "rum_b", "benchmark decomposition",
                      "omitting heterogeneous opportunities",
                      "omits heterogeneous opportunities")]
    if not trig:
        it8.set(a, True, "artifact does not report the RUM comparison", na=True)
        continue
    trig = scope(a, trig)
    raw = " ".join(p.raw for p in trig)
    blob = " ".join(p.txt for p in trig)
    bad = []
    missing = [x for x in RUM_NUMS if not shows(trig, x)]
    if missing:
        bad.append("RUM-1: missing from the block: %s" % ", ".join(missing))
    if not re.search(r"(not\s+(?:materially\s+)?raise[sd]?\s+the preference share|"
                     r"almost nothing to preferences|re-attributes almost nothing|"
                     r"preference share (?:barely|hardly) moves)", blob):
        bad.append("RUM-2: the `does not raise the preference share` reading is "
                   "absent")
    for p in trig:
        for m in re.finditer(r"(opportunity|opportunities)[^.?]{0,80}(becomes?|"
                             r"re-?attributed to|reappears? as) (a )?"
                             r"(taste|preference)", p.txt):
            # the sentence around the match: a question ("how much is
            # re-attributed to preferences?") poses the issue, it does not claim
            # it; a negated or quantified sentence answers it correctly.
            lo = max(p.txt.rfind(".", 0, m.start()), p.txt.rfind("?", 0, m.start()))
            hi = min([x for x in (p.txt.find(".", m.end()),
                                  p.txt.find("?", m.end())) if x != -1] or [len(p.txt)])
            sent = p.txt[lo + 1:hi + 1]
            if "?" in sent or "how much" in sent:
                continue
            if re.search(r"not|almost nothing|barely|hardly|slightly less|"
                         r"marginally less|-4\.0|does not", sent):
                continue
            bad.append("RUM-3: %s reads the misclassification as "
                       "opportunity-becomes-taste" % p.loc)
            break
    if "3.32" in raw and "6.45" not in raw and "different object" not in blob \
            and "not the" not in blob:
        bad.append("RUM-4: the 3.32 %% benchmark row is not distinguished from the "
                   "RUM_B decomposition")
    it8.set(a, not bad)
    for b in dict.fromkeys(bad):
        it8.note(a, b)

# ==========================================================================
# ITEM 9 — geography and sex
# ==========================================================================

it9 = item(9, "Geographic and sex results (spec \u00a79)")
for a in ARTS:
    bad = []
    geo = [p for p in PROSE[a] if any_of(p, "geograph", "c_geo")]
    geo = scope(a, geo) if geo else geo
    if geo:
        raw = " ".join(p.raw for p in geo)
        blob = " ".join(p.txt for p in geo)
        if not shows(geo, "87.6"):
            bad.append("GEO-1: 87.6 %% of the access channel absent")
        if not shows(geo, "13.05"):
            bad.append("GEO-1: 13.05 %% of baseline inequality absent")
        if not re.search(r"(not causal|descriptive|not a causal|non-causal)", blob):
            bad.append("GEO-4: no descriptive/not-causal guard")
        if shows(geo, "1.019") and "clip" not in blob and "above one" not in blob \
                and "exceeds one" not in blob and "signed" not in blob:
            bad.append("GEO-2: the equivalized ratio 1.019 is printed without "
                       "naming it a signed contribution ratio")
        if ("housing" in blob or "rent zone" in blob) and \
                not re.search(r"(distinct|distinguish|not the same|separate)", blob):
            bad.append("GEO-3: housing-allowance zone not distinguished from "
                       "structural access geography")
    sex = [p for p in PROSE[a] if any_of(p, "re-aggregated by sex", "by sex",
                                         "men and women", "subgroup")]
    sex = scope(a, sex) if sex else sex
    if sex:
        raw = " ".join(p.raw for p in sex)
        blob = " ".join(p.txt for p in sex)
        if shows(sex, "19.58") or shows(sex, "9.79"):
            for x in ("19.58", "9.79"):
                if not shows(sex, x):
                    bad.append("SEX-1: %s absent from the sex panel" % x)
        if shows(sex, "2.69") or shows(sex, "2.78"):
            for x in ("2.69", "2.78"):
                if not shows(sex, x):
                    bad.append("SEX-2: %s absent" % x)
            if not re.search(r"(sign|reverses|changes sign|negative under)", blob):
                bad.append("SEX-2: the sign change with the reference is not "
                           "stated")
    if not geo and not sex:
        it9.set(a, True, "artifact reports neither the geographic nor the sex "
                         "panel", na=True)
    else:
        it9.set(a, not bad)
    for b in dict.fromkeys(bad):
        it9.note(a, b)

# ==========================================================================
# ITEM 10 — forbidden terms and permitted sites
# ==========================================================================

FORBIDDEN = {
    "removes 93.7": {},
    "beta_ll estimated": {},
    "S8": {"P": ["__range__"], "H": ["provenance"], "N": ["__code__"]},
    "LOC4": {"P": ["__range__"], "H": ["provenance"], "N": ["__code__"]},
}


def p_ranges():
    """Permitted provenance line ranges in the paper: Appendix A.4 and the
    self-check (record-key) appendix."""
    out, start = [], None
    for i, ln in enumerate(P_LINES, 1):
        if ln.startswith("### A.4"):
            start = i
        elif start and ln.startswith(("## ", "# ")):
            out.append((start, i - 1))
            start = None
    for i, ln in enumerate(P_LINES, 1):
        if ln.startswith("## Self-check table"):
            out.append((i, len(P_LINES)))
    return out


P_PERMIT = p_ranges()


def in_permit(loc):
    try:
        lo, hi = (int(x) for x in loc.split("-"))
    except ValueError:
        return False
    return any(a <= lo and hi <= b for a, b in P_PERMIT)
CHANNEL_STEMS = ["C_P", "C_E", "C_A", "C_B", "C_D"]
STATUS_TOKENS = ["PROVISIONAL", "PENDING_ECONOMICS_REVIEW",
                 "NESTED_ENDOWMENTS_PROVISIONAL"]

it10 = item(10, "Forbidden terms and permitted sites (spec \u00a710)")
for a in ARTS:
    bad = []
    src_pass = ALL[a]
    for term, permits in FORBIDDEN.items():
        allow = permits.get(a, [])
        for p in src_pass:
            if term.lower() not in p.txt:
                continue
            if p.kind == "code" and "__code__" in allow:
                continue
            if "__range__" in allow and a == "P" and in_permit(p.loc):
                continue
            if any(x not in ("__code__", "__range__") and x in p.txt
                   for x in allow):
                continue
            if a == "H" and p.loc in H_DOC.prov:
                continue
            bad.append("%s: `%s` outside a permitted site" % (p.loc, term))
    for p in src_pass:
        if p.kind == "code":
            continue
        for stem in CHANNEL_STEMS:
            if re.search(r"(?<![A-Za-z_])%s(?![A-Za-z_])" % stem, p.raw):
                if a == "P" and in_permit(p.loc):
                    continue
                if a == "H" and p.loc in H_DOC.prov:
                    continue
                if "couples_c_" in p.txt:
                    continue
                bad.append("%s: audience-facing channel stem `%s`" % (p.loc, stem))
    for p in PROSE[a]:
        if re.search(r"\bremove[sd]?\b", p.txt) and re.search(
                r"(shapley|owen|attribut)", p.txt):
            if not re.search(r"(never|not|rather than|instead of|as opposed to|"
                             r"is not that|differ)", p.txt):
                bad.append("%s: a Shapley share described with `removes`" % p.loc)
    for p in PROSE[a]:
        if "bootstrap" in p.txt and "not a bootstrap" not in p.txt \
                and "no bootstrap" not in p.txt:
            bad.append("%s: `bootstrap` outside an explicit denial" % p.loc)
    for p in src_pass:
        for tok in STATUS_TOKENS:
            if tok in p.raw and p.kind != "code":
                bad.append("%s: status token `%s`" % (p.loc, tok))
    for p in PROSE[a]:
        for f in ("g^{acc}", "g^{market}"):
            if f in p.txt:
                bad.append("%s: forbidden symbol `%s`" % (p.loc, f))
    it10.set(a, not bad)
    for b in dict.fromkeys(bad):
        it10.note(a, b)


# ==========================================================================
# ITEM 11 - the boundary-active coordinates carry the age-bound diagnostic
# ==========================================================================

AB_TRIGGER = ("beta_l_age2_sm", "boundary-active", "bound-active",
              "bound-activity", "age-squared coefficients",
              "active box bound", "active bound at the optimum")
AB_FACTS = {
    "AB-1 widened by a factor of five": (
        r"factor of\s+(five|5)|\bfive\b[^.]{0,40}half-width|"
        r"\u00b15 to \u00b125|\+/-5 to \+/-25|5 to \u00b125"),
    "AB-2 the bounds disappear": (
        r"bounds? disappear|active set goes (from )?(two|2)? ?to (zero|empty|0)|"
        r"2 ?(to|\u2192|->) ?0|become interior|every coordinate is interior|"
        r"all 41 coordinates become interior"),
    "AB-3 negligible gain, not a chi-square": (
        r"0\.552|0\.55\b"),
    "AB-4 +1.0 inside both intervals": (
        r"\+1\.0[^.]{0,80}inside both|inside both[^.]{0,60}interval|"
        r"lies inside both"),
    "AB-5 the unit re-expression": (
        r"0\.034845|0\.035\b"),
    "AB-6 the retention verdict": (
        r"retain(ed|ing)? the preferred specification|retain_s8_close|"
        r"specification of record is retained|verdict is to retain"),
}

it11 = item(11, "Boundary-active coordinates: the age-bound line (spec \u00a711)")
for a in ARTS:
    trig = [p for p in PROSE[a] if any_of(p, *AB_TRIGGER)]
    if not trig:
        it11.set(a, True, "artifact does not introduce the boundary-active "
                          "coordinates", na=True)
        continue
    near = scope(a, trig)
    blob = " ".join(p.txt for p in near)
    raw = " ".join(p.raw for p in near)
    keys = set()
    for p in near:
        keys |= p.keys
    bad = []
    # In H the figures are rendered from the agebound AUX group at page load,
    # so the binding is the print site; elsewhere the numeral is.
    NUMERIC_AS_KEY = {
        "AB-3 negligible gain, not a chi-square": "agebound.delta_negll",
        "AB-5 the unit re-expression": "agebound.lambda40_m",
    }
    for name, rx in AB_FACTS.items():
        if a == "H" and NUMERIC_AS_KEY.get(name) in keys:
            continue
        if not re.search(rx, blob + " " + raw, re.I):
            bad.append("missing: %s" % name)
    if not (re.search(r"0\.055555|0\.056\b", blob + " " + raw)
            or (a == "H" and "agebound.lambda40_f" in keys)):
        bad.append("missing: AB-5 the second unit re-expression value")
    if not (re.search(r"3\.477|3\.475", raw)
            or (a == "H" and {"agebound.ci_m", "agebound.ci_f"} <= keys)):
        bad.append("missing: AB-4 the freed 95 %% intervals")
    if not re.search(r"chi-square|chi square|not a likelihood-ratio|"
                     r"no degree of freedom|k is identical|"
                     r"same free coordinates", blob):
        bad.append("AB-3: the gain is not disclaimed as a non-chi-square "
                   "statistic")
    it11.set(a, not bad)
    for b in dict.fromkeys(bad):
        it11.note(a, b)

# ==========================================================================
# ITEM 12 - the consumption curvature is MAINTAINED, not tested
# ==========================================================================

it12 = item(12, "Consumption curvature: maintained, not tested (spec \u00a712)")
for a in ARTS:
    # A bare theta_c inside a displayed utility equation is not a report of
    # the estimate; the trigger is the named curvature or its value.
    trig = [p for p in PROSE[a]
            if any_of(p, "consumption curvature", "theta_c_singles")
            or re.search(r"theta_c\s*=\s*0\.168|\u03b8_c\s*=\s*0\.168",
                         p.txt)]
    if not trig:
        it12.set(a, True, "artifact does not report the consumption curvature",
                 na=True)
        continue
    near = scope(a, trig)
    blob = " ".join(p.txt for p in near)
    bad = []
    if not re.search(r"maintain(ed)?|by construction of the certified", blob):
        bad.append("TC-1: the curvature is not stated as maintained common")
    if not re.search(r"never (been )?tested|not tested|never proposed|"
                     r"no test of it exists", blob):
        bad.append("TC-1: `not tested sex-specifically` is not stated")
    if not re.search(r"numeraire", blob):
        bad.append("TC-1: the scale-numeraire reason is missing")
    if not re.search(r"parsimony|never proposed", blob):
        bad.append("TC-1: the parsimony reason is missing")
    if re.search(r"(rejected|test(ed)?)[^.]{0,60}sex-specific consumption|"
                 r"sex-specific consumption curvature[^.]{0,40}(rejected|"
                 r"was tested)", blob):
        bad.append("TC-2: a sex-specific curvature is described as tested or "
                   "rejected")
    # TC-3: the limitations list
    lim = [p for p in PROSE[a]
           if any_of(p, "not identify", "limitation", "does not claim",
                     "candidate money-metric")]
    limblob = " ".join(p.txt for p in scope(a, lim)) if lim else ""
    if "consumption curvature" not in limblob and "theta_c" not in limblob:
        bad.append("TC-3: absent from the limitations list")
    elif "money-metric sensitivity" not in limblob and \
            "money metric" not in limblob:
        bad.append("TC-3: not named as a candidate money-metric sensitivity")
    it12.set(a, not bad)
    for b in dict.fromkeys(bad):
        it12.note(a, b)

# ==========================================================================
# ITEM 13 - the couples coefficient table
# ==========================================================================

COUPLES_PARAMS = sorted(
    k[len("couples_param_"):-len("__estimate")] for k in J
    if k.startswith("couples_param_") and k.endswith("__estimate"))

it13 = item(13, "The couples coefficient table (spec \u00a713)")
for a in ARTS:
    trig = [p for p in PROSE[a]
            if any_of(p, "46 free coordinates", "couples_param_",
                      "clean both-flexible baseline")]
    if not trig:
        it13.set(a, True, "artifact does not carry the couples coefficient "
                          "table", na=True)
        continue
    near = scope(a, trig)
    blob = " ".join(p.txt for p in near)
    raw = " ".join(p.raw for p in near)
    keys = set()
    for p in near:
        keys |= p.keys
    bad = []
    if len(COUPLES_PARAMS) != 46:
        bad.append("CT-1: the registry does not carry 46 couples coordinates")
    missing = [c for c in COUPLES_PARAMS
               if c not in raw and ("couples_param_%s__estimate" % c) not in keys]
    if missing:
        bad.append("CT-1: %d coordinates absent from the table (%s ...)"
                   % (len(missing), ", ".join(missing[:4])))
    for blk in ("male leisure", "female leisure", "hours opportunity",
                "occupation", "wage"):
        if blk not in blob:
            bad.append("CT-1: block `%s` is not named" % blk)
    if not re.search(r"robust|cr1", blob):
        bad.append("CT-2: the robust CR1 standard errors are not named")
    if "beta_w_pexp2" not in raw and \
            "couples_active_bound_coordinate" not in keys:
        bad.append("CT-2: the active-bound coordinate is not identified")
    for cnt in ("n_couples_free", "n_couples_interior", "n_couples_at_bound",
                "n_couples_pinned"):
        v = str(val(cnt))
        if v not in raw and cnt not in keys:
            bad.append("CT-3: count %s (%s) does not travel with the table"
                       % (cnt, v))
    if a == "H":
        unbound = [c for c in COUPLES_PARAMS
                   if ("couples_param_%s__estimate" % c) not in keys]
        if unbound:
            bad.append("CT-4: %d coefficients are not bound to a registry key"
                       % len(unbound))
    if not ("absent" in blob and re.search(r"beta_ll|cross-leisure", blob)):
        bad.append("CT-5: the table's note does not state the beta_ll ABSENT row")
    it13.set(a, not bad)
    for b in dict.fromkeys(bad):
        it13.note(a, b)

# ==========================================================================
# ITEM 14 - children: the male term and child age
# ==========================================================================

it14 = item(14, "Children: the male term and child age (spec \u00a714)")
for a in ARTS:
    trig = [p for p in PROSE[a]
            if any_of(p, "beta_l_nkids", "child-count shifter",
                      "children-in-leisure", "male child")]
    if not trig:
        it14.set(a, True, "artifact does not report the male child term",
                 na=True)
        continue
    near = scope(a, trig)
    blob = " ".join(p.txt for p in near)
    raw = " ".join(p.raw for p in near)
    keys = set()
    for p in near:
        keys |= p.keys
    bad = []
    # H renders every numeral from a binding at page load, so the binding is
    # the print site there.
    if not (re.search(r"1\.6468|1\.65\b", raw)
            or "beta_l_nkids_male_historical_test" in keys):
        bad.append("CH-1: the tested estimate is not printed")
    if not (re.search(r"1\.8671|1\.87\b", raw)
            or "chron.male_child_se" in keys):
        bad.append("CH-1: the robust standard error of the test is not printed")
    if not (re.search(r"0\.88\b", raw) or "chron.male_child_z" in keys):
        bad.append("CH-1: the z of the test is not printed")
    if not re.search(r"\btested\b", blob):
        bad.append("CH-1: the term is not stated to have been tested")
    if not re.search(r"not identified|do(es)? not support|"
                     r"indistinguishable from zero|not pinned down", blob):
        bad.append("CH-1: `not identified` is not stated")
    if not re.search(r"exposure|of single men|of the 1,555|apply to", blob):
        bad.append("CH-1: the exposure of the term is not stated")
    if not (re.search(r"12\.75|5\.85|\b91\b", raw)
            or "child.male_with_children" in keys):
        bad.append("CH-1: the exposure figure of record is not printed")
    if "absent" not in blob or "structural zero" not in blob:
        bad.append("CH-2: the ABSENT / structural-zero status is not stated")
    if re.search(r"(?<!not )(?<!never )estimated as zero|not significant", blob):
        bad.append("CH-2: the term is described as estimated as zero or "
                   "insignificant")
    if not re.search(r"not been re-?run|has not been re-?run|"
                     r"pre-correction|pre-floor5|earlier frame|"
                     r"historical test uses", blob):
        bad.append("CH-3: the scope caveat on the historical frame is missing")
    if not (re.search(r"date of birth", blob)
            and re.search(r"parent.child link", blob)
            and re.search(r"pre-school|under six|under 6", blob)
            and re.search(r"youngest", blob)):
        bad.append("CH-4: the child-age variables are not all named "
                   "(date of birth, parent-child link, youngest, pre-school)")
    if not re.search(r"post-seminar|future work|next step|not in the baseline",
                     blob):
        bad.append("CH-4: child age is not named as post-seminar work")
    it14.set(a, not bad)
    for b in dict.fromkeys(bad):
        it14.note(a, b)

# ==========================================================================
# ITEM 15 - execution profiles and backend parity
# ==========================================================================

OBSOLETE_BACKEND = [
    "cannot represent the specification",
    "cannot represent this specification",
    "gpu grammar cannot represent",
    "the gpu path is not available",
]

it15 = item(15, "Execution profiles and backend parity (spec \u00a715)")
for a in ARTS:
    trig = [p for p in ALL[a]
            if any_of(p, "server_jax_cpu", "laptop_torch_cuda",
                      "execution profile")]
    prose_trig = [p for p in PROSE[a]
                  if any_of(p, "server_jax_cpu", "laptop_torch_cuda",
                            "execution profile")]
    bad = []
    # BP-3 applies to every artifact, whether or not it names the profiles
    for p in PROSE[a]:
        for f in OBSOLETE_BACKEND:
            if f in p.txt:
                bad.append("BP-3: %s carries the obsolete `%s`" % (p.loc, f))
        if re.search(r"occupation-condition(al|ed) wage[^.]{0,120}\bcannot\b|"
                     r"\bcannot\b[^.]{0,120}occupation-condition(al|ed) wage",
                     p.txt):
            bad.append("BP-3: %s still pairs the occupation-conditioned wage "
                       "with `cannot`" % p.loc)
    if not prose_trig:
        if bad:
            it15.set(a, False)
            for b in dict.fromkeys(bad):
                it15.note(a, b)
        else:
            it15.set(a, True, "artifact does not carry the profile table, and "
                              "no obsolete backend claim remains", na=True)
        continue
    near = scope(a, prose_trig)
    if a == "H":
        secs = {p.loc.split(" (")[0] for p in near}
        near = [p for p in ALL["H"] if p.loc.split(" (")[0] in secs]
    blob = " ".join(p.txt for p in near)
    raw = " ".join(p.raw for p in near)
    for prof in ("server_jax_cpu", "laptop_jax_cpu", "laptop_torch_cuda"):
        spots = [m.start() for m in re.finditer(re.escape(prof), blob)]
        if not spots:
            bad.append("BP: profile %s is not listed" % prof)
            continue
        # In H the profile name is a <code> span and its status word is in the
        # neighbouring table cell, so the status is checked over the section.
        near_ok = any("supported" in blob[i:i + 400] for i in spots)
        if not (near_ok or (a == "H" and "supported" in blob)):
            bad.append("BP: %s is not stated SUPPORTED" % prof)
    if not re.search(r"pkg-?04b|1eed2756", blob):
        bad.append("BP: the parity clearance is not named (PKG-04B / 1eed2756)")
    if not re.search(r"18022\.764617170084", raw):
        bad.append("BP-1: the exact negLL is not printed with the parity claim")
    for name, rx in (("gradient", r"gradient"), ("hessian", r"hessian"),
                     ("scores", r"score"), ("covariance/CR1", r"covariance|cr1"),
                     ("standard errors", r"standard error|robust se"),
                     ("active-bound set", r"active[- ]bound"),
                     ("pinned", r"pinned")):
        if not re.search(rx, blob):
            bad.append("BP-1: the parity list omits %s" % name)
    if not re.search(r"cuda[^.]{0,120}(not available|unavailable|exported|"
                     r"outstanding)|not available[^.]{0,60}cuda|"
                     r"cuda_not_available", blob):
        bad.append("BP-2: the CUDA device caveat is missing")
    if not re.search(r"default[^.]{0,80}(unchanged|remains)|"
                     r"remains the default|profile unchanged", blob):
        bad.append("BP-4: the default-unchanged statement is missing")
    if not re.search(r"runtime is not re-?established|not re-?established|"
                     r"no speed claim|diagnostic", blob):
        bad.append("BP-4: runtime is not disclaimed")
    if a == "N":
        code_blob = " ".join(p.txt for p in N_CODE)
        if "bench_backends" not in code_blob:
            bad.append("BP-5: the notebook has no benchmark cell")
        elif "skipped" not in code_blob:
            bad.append("BP-5: the benchmark cell does not print SKIPPED")
    it15.set(a, not bad)
    for b in dict.fromkeys(bad):
        it15.note(a, b)



# ==========================================================================
# report
# ==========================================================================

def render(out_path: Path, stale: str) -> int:
    fails = sum(1 for it in ITEMS for a in ARTS if it.verdict.get(a) == "FAIL")
    overall = "PASS" if fails == 0 else "FAIL"
    L = []
    ver = out_path.stem.split("_")[-1]
    L.append("# Consistency gate %s" % ver)
    L.append("")
    L.append("**Overall: %s.** Instrument: `reports/run_consistency_gate.py`, "
             "implementing `reports/consistency_gate_spec_v1.md`. "
             "`reports/consistency_gate_v1.md` is retained unchanged." % overall)
    L.append("")
    L.append(stale)
    L.append("")
    L.append("## Verdict matrix")
    L.append("")
    L.append("| # | gate item | " + " | ".join(NAMES[a] for a in ARTS) + " |")
    L.append("|---|---|" + "---|" * len(ARTS))
    for it in ITEMS:
        L.append("| %d | %s | %s |" % (
            it.num, it.title,
            " | ".join("**%s**" % it.verdict.get(a, "?") for a in ARTS)))
    L.append("")
    L.append("%d of %d (item, artifact) cells FAIL." % (fails, len(ITEMS) * len(ARTS)))
    L.append("")
    L.append("## Evidence")
    for it in ITEMS:
        L.append("")
        L.append("### %d. %s" % (it.num, it.title))
        any_ev = False
        for a in ARTS:
            ev = it.evidence.get(a) or []
            if not ev and it.verdict.get(a) == "PASS":
                continue
            any_ev = True
            L.append("")
            L.append("**%s — %s**" % (NAMES[a], it.verdict.get(a)))
            L.append("")
            for e in ev[:40]:
                L.append("- %s" % e)
            if len(ev) > 40:
                L.append("- ... %d further locations" % (len(ev) - 40))
        if not any_ev:
            L.append("")
            L.append("All four artifacts PASS with no exceptions recorded.")
    L.append("")
    L.append("## Inputs")
    L.append("")
    L.append("| id | path |")
    L.append("|---|---|")
    for k in ("J", "P", "H", "D", "N"):
        L.append("| %s | `%s` |" % (k, PATHS[k]))
    out_path.write_text("\n".join(L) + "\n", encoding="utf-8")
    return 0 if overall == "PASS" else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(JMP / "reports/consistency_gate_v2.md"))
    ap.add_argument("--stale", default="")
    args = ap.parse_args()
    stale = args.stale or ("Run over the current build of H and the current saved "
                           "execution of N.")
    rc = render(Path(args.out), stale)
    for it in ITEMS:
        print("%-2d %-58s %s" % (it.num, it.title[:58],
                                 " ".join("%s=%s" % (a, it.verdict.get(a))
                                          for a in ARTS)))
    print("\nwrote %s  (exit %d)" % (args.out, rc))
    return rc


if __name__ == "__main__":
    sys.exit(main())
