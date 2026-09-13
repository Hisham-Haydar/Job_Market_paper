#!/usr/bin/env python
r"""Verify the three v4 builds against content_v2.

Retains the original path, macro, count, log, text-layer, word-count and
font gate families. The decisive verbatim-content brief replaces the
legacy fixed word cap and running order. See verify_content_v4.py for
PDF headline/caption/note equality and source checks.

Usage: python beamer/verify_deck_v1.py [--build build] [--job NAME]
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


# v4 preserves the seven gate families and enforces the decisive content brief.
from verify_content_v4 import main


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
