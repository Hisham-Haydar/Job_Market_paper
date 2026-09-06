#!/usr/bin/env python
r"""Verify the built deck against the source.

Checks, in order:
  1. every \deckfig / \includegraphics target resolves to a file on disk;
  2. every macro the .tex uses is defined in deck_numbers_v1.tex;
  3. the frame count, the overlay count and the PDF page count agree;
  4. the log carries no error and no overfull/underfull box.

Usage:  python beamer/verify_deck_v1.py [--build build] [--job JMP_seminar_deck_v1]
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent


def pdf_pages(path: pathlib.Path) -> int:
    data = path.read_bytes()
    counts = [int(m.group(1)) for m in re.finditer(rb"/Count\s+(\d+)", data)]
    if not counts:
        raise SystemExit("could not read a page count from " + str(path))
    return max(counts)


def main(build: str, job: str) -> int:
    tex = (HERE / "JMP_seminar_deck_v1.tex").read_text(encoding="utf-8")
    numbers = (HERE / "deck_numbers_v1.tex").read_text(encoding="utf-8")
    figdir = HERE / "figures"
    outdir = HERE / build
    ok = True

    def check(label, condition, detail=""):
        nonlocal ok
        status = "PASS" if condition else "FAIL"
        if not condition:
            ok = False
        print("  [%s] %-46s %s" % (status, label, detail))

    print("=== 1. figure paths ===")
    figs = set(re.findall(r"\\deckfig\{([^}]+)\}", tex))
    for left, right in re.findall(
            r"\\deckfigtwo\{([^}]+)\}\{[^}]*\}%?\s*\{([^}]+)\}", tex):
        figs.add(left)
        figs.add(right)
    figs |= set(re.findall(r"\\includegraphics\[[^\]]*\]\{([^}]+)\}", tex))
    missing = sorted(f for f in figs if not (figdir / (f + ".pdf")).exists())
    check("every figure resolves", not missing,
          "%d figures; missing: %s" % (len(figs), missing or "none"))
    onfile = {p.stem for p in figdir.glob("*.pdf")}
    unused = sorted(onfile - figs)
    check("no unused figure copy", not unused, "unused: %s" % (unused or "none"))

    print("=== 2. number macros ===")
    defined = set(re.findall(r"\\newcommand\{\\([A-Za-z]+)\}", numbers))
    # macros the deck uses that look like generated numbers
    used = set(re.findall(r"\\([A-Z][A-Za-z]*)\b", tex))
    preamble = set(re.findall(r"\\newcommand\{\\([A-Za-z]+)\}",
                              (HERE / "jmp_beamer_preamble.tex").read_text(
                                  encoding="utf-8")))
    latex_builtin = {
        "LaTeX", "TeX", "Large", "large", "Huge", "huge", "Big", "Bigg",
        "DeclareMathOperator", "PassOptionsToPackage", "AtBeginDocument",
    }
    undefined = sorted(u for u in used
                       if u not in defined and u not in preamble
                       and u not in latex_builtin
                       and re.match(r"^(Share|Band|Par|Sub|Bench|Ext|Reg|EOne|"
                                    r"Hours|Emp|Occ|Wage|Wish|Geo|Pref|"
                                    r"N[A-Z]|I[A-Z])", u))
    check("every number macro is generated", not undefined,
          "%d defined; undefined: %s" % (len(defined), undefined or "none"))

    # A near-miss of a generated name (\xtWish for \ExtWish, say) survives a
    # projection build because it only appears inside \note{} -- which is
    # typeset only in the rehearsal build.  Catch it here instead: flag any
    # control sequence that is within one leading character of a real macro.
    known = defined | preamble
    nearmiss = sorted(u for u in used
                      if u not in known
                      and any(k.endswith(u) and len(k) - len(u) <= 2
                              for k in known))
    check("no near-miss of a generated macro", not nearmiss,
          "suspects: %s" % (nearmiss or "none"))

    # Every generated macro should actually be used; an orphan means the
    # slide that quoted it was cut without regenerating.
    orphans = sorted(d for d in defined if ("\\" + d) not in tex)
    check("no orphaned generated macro", not orphans,
          "unused: %s" % (orphans or "none"))

    print("=== 3. frames and pages ===")
    body = tex.split(r"\begin{document}", 1)[1]
    running, backup = body.split(r"\appendix", 1)
    n_short = len(re.findall(r"\\shortdeck\{%", running))
    n_cut = len(re.findall(r"\\longdeck\{%", running))
    n_merged = len(re.findall(r"\\mergedaway\{%", running))
    n_backup = len(re.findall(r"\\begin\{frame\}", backup))
    check("running-order frames == 23", n_short + n_cut + n_merged == 23,
          "%d kept + %d cut + %d merged" % (n_short, n_cut, n_merged))
    check("25-minute variant == 16 frames", n_short == 16,
          "23 - %d cut - %d merged = %d" % (n_cut, n_merged, n_short))
    check("the frozen plan's 5 cuts", n_cut == 5, "%d cut to backup" % n_cut)
    check("the frozen plan's 2 merges", n_merged == 2, "%d merged" % n_merged)
    check("backup frames", n_backup >= 4, "%d backup frames" % n_backup)

    pdf = outdir / (job + ".pdf")
    if pdf.exists():
        pages = pdf_pages(pdf)
        # overlays: \only<n> and \onslide<n> and \item<n> beyond the first
        extra = 0
        for frame in re.split(r"\\begin\{frame\}", running)[1:]:
            steps = [int(x) for x in re.findall(
                r"\\(?:only|onslide|item)<(\d+)", frame)]
            if steps:
                extra += max(steps) - 1
        n_frames = n_short + n_cut + n_merged + n_backup
        expected = n_frames + extra
        check("PDF pages == frames + overlay steps", pages == expected,
              "%d pages; %d frames + %d overlay steps = %d"
              % (pages, n_frames, extra, expected))
    else:
        check("PDF present", False, str(pdf))

    print("=== 4. the log ===")
    log = outdir / (job + ".log")
    if log.exists():
        text = log.read_text(encoding="utf-8", errors="replace")
        errors = [l for l in text.splitlines() if l.startswith("!")]
        over = text.count("Overfull")
        under = text.count("Underfull")
        check("no LaTeX error", not errors, "%d errors" % len(errors))
        check("no overfull box", over == 0, "%d overfull" % over)
        check("no underfull box", under == 0, "%d underfull" % under)
    else:
        check("log present", False, str(log))

    print()
    print("VERDICT:", "ALL PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", default="build")
    ap.add_argument("--job", default="JMP_seminar_deck_v1")
    a = ap.parse_args()
    sys.exit(main(a.build, a.job))
