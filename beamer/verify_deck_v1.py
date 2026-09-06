#!/usr/bin/env python
r"""Verify the built deck against the source.

Checks, in order:
  1. every \slidefig / \includegraphics target resolves, and no figure copy
     is unused;
  2. every macro the .tex uses is defined in deck_numbers_v1.tex, with no
     near-miss and no orphan;
  3. the frame count, the overlay count and the PDF page count agree;
  4. the log carries no error and no overfull/underfull box;
  5. the PDF TEXT LAYER of every built PDF carries no internal label
     (pdftotext + the forbidden-label regex), outside the backup slides'
     own citations;
  6. no frame carries more than MAX_WORDS words of body text, counting
     neither the headline nor an equation;
  7. the slide figures were rendered at a minimum font size >= 18 pt, as
     recorded by make_slide_figures_v1.py.

Usage:  python beamer/verify_deck_v1.py [--build build] [--job NAME]
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import shutil
import subprocess
import sys

HERE = pathlib.Path(__file__).parent

# Internal labels that must never reach a rendered slide.  R-260.
FORBIDDEN = re.compile(
    r"S8|LOC4|C_P|C_E|C_A|C_B|C_D|R-2|PENDING|PROVISIONAL|EXPLORATORY"
    r"|deputy|ruling")

# Body text outside the headline and any equation.
MAX_WORDS = 12

# The slide figure kit's minimum rendered font size, in points.
MIN_FONT_PT = 18

# Set by --debug-overlays: print the per-frame page count the arithmetic
# derives, so a mismatch with the PDF can be located rather than guessed at.
DEBUG_OVERLAYS = False


def pdf_pages(path: pathlib.Path) -> int:
    data = path.read_bytes()
    counts = [int(m.group(1)) for m in re.finditer(rb"/Count\s+(\d+)", data)]
    if not counts:
        raise SystemExit("could not read a page count from " + str(path))
    return max(counts)


def strip_tex(chunk: str) -> str:
    r"""Reduce a frame body to the words an audience would read off it.

    Drops \note{...}, comments, equations, tikz pictures, the headline, all
    macro names and all braces, leaving the prose that is actually set.
    """
    # comments
    chunk = re.sub(r"(?<!\\)%.*", "", chunk)
    # the speaker notes -- brace-matched, since they contain braces
    out, i = [], 0
    while i < len(chunk):
        m = re.compile(r"\\note\{").search(chunk, i)
        if not m:
            out.append(chunk[i:])
            break
        out.append(chunk[i:m.start()])
        depth, j = 1, m.end()
        while j < len(chunk) and depth:
            if chunk[j] == "{" and chunk[j - 1] != "\\":
                depth += 1
            elif chunk[j] == "}" and chunk[j - 1] != "\\":
                depth -= 1
            j += 1
        i = j
    chunk = "".join(out)
    # The headline is the message, not body text.
    chunk = re.sub(r"\\headlineframe\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}", "", chunk)
    # An equation is the VISUAL on an equation slide, and the word gloss that
    # names each of its symbols is part of that visual, not prose: it labels
    # the equation the way an axis label labels a chart.
    chunk = re.sub(r"\\\[.*?\\\]", "", chunk, flags=re.S)
    chunk = re.sub(r"\$[^$]*\$", "", chunk)
    # A diagram carries its own labels; those are the visual too.
    chunk = re.sub(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", "",
                   chunk, flags=re.S)
    # A table IS the visual on the frames that carry one.
    chunk = re.sub(r"\\begin\{tabular\}.*?\\end\{tabular\}", "", chunk,
                   flags=re.S)
    # A \caveat{...} is the ONE permitted caption line.  Two things here are
    # ALTERNATIVES, not additions, and only the longest of each may count:
    #   * several \caveat{} on one frame, one per \only build;
    #   * several \only<n>{...} INSIDE one \caveat, one per build.
    # A viewer sees exactly one of each at a time, so summing them would
    # charge a frame for text that never appears together.
    def longest_alternative(body: str) -> str:
        alts = re.findall(r"\\only<[^>]*>\{((?:[^{}]|\{[^{}]*\})*)\}", body)
        if not alts:
            return body
        rest = re.sub(r"\\only<[^>]*>\{(?:[^{}]|\{[^{}]*\})*\}", " ", body)
        return rest + " " + max(alts, key=len)

    caveats = re.findall(r"\\caveat\{((?:[^{}]|\{[^{}]*\})*)\}", chunk)
    chunk = re.sub(r"\\caveat\{(?:[^{}]|\{[^{}]*\})*\}", " ", chunk)
    if caveats:
        chunk += " " + max((longest_alternative(c) for c in caveats), key=len)
    # A \slidefig{name} is the visual; its file name is not a word on the
    # slide.  Drop the argument with the macro.
    chunk = re.sub(r"\\slidefig\{[^}]*\}", " ", chunk)
    chunk = re.sub(r"\\includegraphics(\[[^\]]*\])?\{[^}]*\}", " ", chunk)
    # \begin{env} / \end{env} -- the environment NAME is markup, not prose.
    chunk = re.sub(r"\\(?:begin|end)\{[^}]*\}(\[[^\]]*\])?", " ", chunk)
    # remaining macros, braces, lengths
    chunk = re.sub(r"\\[A-Za-z@]+\s*(\[[^\]]*\])?", " ", chunk)
    chunk = re.sub(r"[{}\[\]&\\~^_]", " ", chunk)
    chunk = re.sub(r"\d+(\.\d+)?(em|pt|cm|ex)\b", " ", chunk)
    return chunk


def count_words(chunk: str) -> tuple[int, str]:
    text = strip_tex(chunk)
    tokens = [t for t in re.split(r"\s+", text) if re.search(r"[A-Za-z]", t)]
    return len(tokens), " ".join(tokens)


def main(build: str, jobs: list[str]) -> int:
    tex = (HERE / "JMP_seminar_deck_v1.tex").read_text(encoding="utf-8")
    numbers = (HERE / "deck_numbers_v1.tex").read_text(encoding="utf-8")
    preamble_src = (HERE / "jmp_beamer_preamble.tex").read_text(encoding="utf-8")
    slidedir = HERE / "figures" / "slides"
    outdir = HERE / build
    ok = True

    def check(label, condition, detail=""):
        nonlocal ok
        status = "PASS" if condition else "FAIL"
        if not condition:
            ok = False
        print("  [%s] %-48s %s" % (status, label, detail))

    # ------------------------------------------------------- 1. figures
    print("=== 1. figure paths ===")
    figs = set(re.findall(r"\\slidefig\{([^}]+)\}", tex))
    plain = set(re.findall(r"\\deckfig\{([^}]+)\}", tex))
    missing = sorted(f for f in figs
                     if not (slidedir / (f + "_slide.pdf")).exists())
    check("every slide figure resolves", not missing,
          "%d used; missing: %s" % (len(figs), missing or "none"))
    onfile = {p.stem[:-6] for p in slidedir.glob("*_slide.pdf")}
    unused = sorted(onfile - figs)
    check("no unused slide figure", not unused, "unused: %s" % (unused or "none"))
    check("no paper-style figure left on a slide", not plain,
          "paper figures still used: %s" % (sorted(plain) or "none"))

    # ------------------------------------------------------- 2. macros
    print("=== 2. number macros ===")
    defined = set(re.findall(r"\\newcommand\{\\([A-Za-z]+)\}", numbers))
    used = set(re.findall(r"\\([A-Z][A-Za-z]*)\b", tex))
    preamble = set(re.findall(r"\\newcommand\{\\([A-Za-z]+)\}", preamble_src))
    # the shared theory figure defines drawing macros, not numbers
    figure_src = (HERE / "theory_model_figure.tex").read_text(encoding="utf-8")
    preamble |= set(re.findall(r"\\newcommand\{\\([A-Za-z]+)\}", figure_src))
    preamble |= set(re.findall(r"\\newif\\if([A-Za-z]+)", figure_src))
    latex_builtin = {
        "LaTeX", "TeX", "Large", "LARGE", "large", "Huge", "huge", "Big",
        "Bigg", "DeclareMathOperator", "PassOptionsToPackage",
        "AtBeginDocument",
    }
    undefined = sorted(u for u in used
                       if u not in defined and u not in preamble
                       and u not in latex_builtin
                       and re.match(r"^(Share|Band|Par|Sub|Bench|Ext|Reg|EOne|"
                                    r"Hours|Emp|Occ|Wage|Wish|Geo|Pref|Rnd|"
                                    r"N[A-Z]|I[A-Z])", u))
    check("every number macro is generated", not undefined,
          "%d defined; undefined: %s" % (len(defined), undefined or "none"))
    known = defined | preamble
    nearmiss = sorted(u for u in used
                      if u not in known
                      and any(k.endswith(u) and len(k) - len(u) <= 2
                              for k in known))
    check("no near-miss of a generated macro", not nearmiss,
          "suspects: %s" % (nearmiss or "none"))
    orphans = sorted(d for d in defined if ("\\" + d) not in tex)
    check("no orphaned generated macro", not orphans,
          "unused: %s" % (orphans or "none"))

    # ------------------------------------------------- 3. frames and pages
    print("=== 3. frames and pages ===")
    body = tex.split(r"\begin{document}", 1)[1]
    running, backup = body.split(r"\appendix", 1)
    n_short = len(re.findall(r"\\shortdeck\{%", running))
    n_cut = len(re.findall(r"\\longdeck\{%", running))
    n_merged = len(re.findall(r"\\mergedaway\{%", running))
    n_backup = len(re.findall(r"\\begin\{frame\}", backup))
    # The frozen content document fixes 23 MESSAGES, not 23 frames.  R-261
    # splits the opening message across the theory-grammar builds and adds
    # the two-answers slide, so the running order is longer than 23 while
    # every frozen message is still carried.  What must hold is the SHAPE:
    # the plan's five cuts and two merges, and a 25-minute order that is
    # meaningfully shorter than the 45-minute one.
    n_run = n_short + n_cut + n_merged
    check("running order covers the frozen 23 messages", n_run >= 23,
          "%d frames: %d kept + %d cut + %d merged"
          % (n_run, n_short, n_cut, n_merged))
    check("25-minute variant is shorter", n_short == n_run - n_cut - n_merged
          and n_short < n_run,
          "%d frames, from %d" % (n_short, n_run))
    check("the frozen plan's 5 cuts", n_cut == 5, "%d cut to backup" % n_cut)
    check("the frozen plan's 2 merges", n_merged == 2, "%d merged" % n_merged)
    check("backup frames", n_backup >= 4, "%d backup frames" % n_backup)

    pdf = outdir / (jobs[0] + ".pdf")
    if pdf.exists():
        pages = pdf_pages(pdf)
        # A frame's page count is its highest overlay step.  Specs come as
        # <2>, <2->, <1-3> and <2,4->, so take every integer that appears in
        # any spec on the frame and use the largest.
        # Overlay steps come from BOTH the running order and the backups, so
        # scan the whole body.  Concatenating the two halves would drop the
        # frame that straddles the \appendix seam.
        extra = 0
        for frame in re.split(r"\\begin\{frame\}", body)[1:]:
            frame = frame.split(r"\end{frame}")[0]
            steps = []
            for spec in re.findall(r"\\(?:only|onslide|item)<([^>]*)>", frame):
                steps += [int(x) for x in re.findall(r"\d+", spec)]
            # The shared theory figure takes its overlay specs through the
            # macros \LabelOv and \PayLabOv, so a step set only there -- e.g.
            # \renewcommand{\LabelOv}{4-} -- is invisible to the scan above
            # but still makes beamer generate that many slides.
            for spec in re.findall(
                    r"\\renewcommand\{\\(?:LabelOv|PayLabOv)\}\{([^}]*)\}",
                    frame):
                steps += [int(x) for x in re.findall(r"\d+", spec)]
            # A spec of 0 (e.g. \renewcommand{\LabelOv}{0}, used to switch a
            # layer off) is a suppression, not a page: a frame always has at
            # least one.  Floor the count at 1 so it cannot go negative.
            if steps:
                extra += max(max(steps), 1) - 1
                if DEBUG_OVERLAYS:
                    h = re.search(
                        r"\\headlineframe\{((?:[^{}]|\{[^{}]*\})*)\}", frame)
                    print("        %d pages  %s" % (
                        max(steps),
                        re.sub(r"\s+", " ", h.group(1))[:46] if h else "(title)"))
        if DEBUG_OVERLAYS:
            print("        running extra = %d" % extra)
        n_frames = n_short + n_cut + n_merged + n_backup
        expected = n_frames + extra
        check("PDF pages == frames + overlay steps", pages == expected,
              "%d pages; %d frames + %d overlay steps = %d"
              % (pages, n_frames, extra, expected))
    else:
        check("PDF present", False, str(pdf))

    # ------------------------------------------------------- 4. the logs
    print("=== 4. the logs ===")
    for job in jobs:
        log = outdir / (job + ".log")
        if not log.exists():
            check("log present: " + job, False, str(log))
            continue
        text = log.read_text(encoding="utf-8", errors="replace")
        errors = [l for l in text.splitlines() if l.startswith("!")]
        over = text.count("Overfull")
        under = text.count("Underfull")
        check("clean log: " + job, not errors and over == 0 and under == 0,
              "%d errors, %d overfull, %d underfull"
              % (len(errors), over, under))

    # --------------------------------------------- 5. the PDF text layer
    print("=== 5. the PDF text layer ===")
    pdftotext = shutil.which("pdftotext")
    if not pdftotext:
        check("pdftotext available", False,
              "install poppler / MiKTeX's pdftotext to run this check")
    else:
        # The backup slides may cite the companion paper and name a ruling in
        # their own text; the running order may not.  Locate the first backup
        # page so hits can be attributed.
        for job in jobs:
            p = outdir / (job + ".pdf")
            if not p.exists():
                check("PDF present: " + job, False, str(p))
                continue
            pages = pdf_pages(p)
            bad = []
            for n in range(1, pages + 1):
                r = subprocess.run(
                    [pdftotext, "-f", str(n), "-l", str(n), str(p), "-"],
                    capture_output=True, text=True, errors="replace")
                hits = sorted(set(FORBIDDEN.findall(r.stdout)))
                if hits:
                    bad.append("p%d:%s" % (n, ",".join(hits)))
            # backup pages are the last n_backup (+ their overlays); a hit
            # there is only allowed inside a citation, which this deck has
            # none of, so any hit anywhere is a failure.
            check("no internal label in the text layer: " + job, not bad,
                  "; ".join(bad) if bad else "0 hits on %d pages" % pages)

        # the slide figures themselves
        bad = []
        for f in sorted(slidedir.glob("*_slide.pdf")):
            r = subprocess.run([pdftotext, str(f), "-"], capture_output=True,
                               text=True, errors="replace")
            hits = sorted(set(FORBIDDEN.findall(r.stdout)))
            if hits:
                bad.append("%s:%s" % (f.name, ",".join(hits)))
        check("no internal label in a slide figure", not bad,
              "; ".join(bad) if bad else
              "0 hits in %d figures" % len(list(slidedir.glob("*_slide.pdf"))))

    # ------------------------------------------------ 6. words per frame
    print("=== 6. words per frame ===")
    worst = []
    for chunk in re.split(r"\\begin\{frame\}", body)[1:]:
        chunk = chunk.split(r"\end{frame}")[0]
        title = re.search(r"\\headlineframe\{((?:[^{}]|\{[^{}]*\})*)\}", chunk)
        n, text = count_words(chunk)
        worst.append((n, (title.group(1)[:44] if title else "(title frame)"),
                      text[:70]))
    worst.sort(reverse=True)
    over = [w for w in worst if w[0] > MAX_WORDS]
    check("body text <= %d words per frame" % MAX_WORDS, not over,
          "worst: %d words -- %s" % (worst[0][0], worst[0][1]) if worst else "")
    if over:
        for n, t, txt in over[:6]:
            print("        %3d words  %-46s %s" % (n, t, txt))

    # ------------------------------------------- 7. the slide figure fonts
    print("=== 7. the slide figure fonts ===")
    style = slidedir / "slide_style_v1.json"
    if not style.exists():
        check("slide style recorded", False, str(style))
    else:
        rc = json.loads(style.read_text(encoding="utf-8"))
        pts = {k: v for k, v in rc.items()
               if k.endswith("size") and isinstance(v, (int, float))}
        if pts:
            where, smallest = min(pts.items(), key=lambda kv: kv[1])
        else:
            where, smallest = "none", 0
        check("every recorded font >= %d pt" % MIN_FONT_PT,
              smallest >= MIN_FONT_PT,
              "smallest recorded: %g pt (%s)" % (smallest, where))
        fs = rc.get("figure.figsize")
        ratio = (fs[0] / fs[1]) if isinstance(fs, (list, tuple)) and fs[1] else 0
        check("16:9 canvas", abs(ratio - 16 / 9) < 0.02,
              "%.3f (16:9 = %.3f)" % (ratio, 16 / 9))

    print()
    print("VERDICT:", "ALL PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", default="build")
    ap.add_argument("--job", action="append", default=None)
    ap.add_argument("--debug-overlays", action="store_true")
    a = ap.parse_args()
    DEBUG_OVERLAYS = a.debug_overlays
    globals()["DEBUG_OVERLAYS"] = a.debug_overlays
    jobs = a.job or ["JMP_seminar_deck_v1", "JMP_seminar_deck_v1_25min",
                     "JMP_seminar_deck_v1_rehearsal"]
    sys.exit(main(a.build, jobs))
