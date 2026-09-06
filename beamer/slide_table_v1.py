#!/usr/bin/env python
r"""Print the per-slide table: headline, visual or equation, body words.

One row per frame in source order, so the deck's slide grammar can be read
off at a glance and checked against the frozen content document.

Usage:  python beamer/slide_table_v1.py [--csv PATH]
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from verify_deck_v1 import count_words                       # noqa: E402

TAG = re.compile(r"(?m)^\\(shortdeck|longdeck|mergedaway)\{%")
HEAD = re.compile(r"\\headlineframe\{((?:[^{}]|\{[^{}]*\})*)\}")
SLIDEFIG = re.compile(r"\\slidefig\{([^}]+)\}")
DISPLAY = re.compile(r"\\\[")
TIKZ = re.compile(r"\\begin\{tikzpicture\}")
TABULAR = re.compile(r"\\begin\{tabular\}")

DISPOSITION = {"shortdeck": "keep", "longdeck": "cut@25",
               "mergedaway": "merged@25"}


def visual_of(chunk: str) -> str:
    figs = SLIDEFIG.findall(chunk)
    if figs:
        uniq = list(dict.fromkeys(figs))
        return "figure: " + " / ".join(uniq)
    if DISPLAY.search(chunk):
        return "equation"
    if TIKZ.search(chunk):
        return "diagram"
    if TABULAR.search(chunk):
        return "table"
    return "(none)"


def rows(tex: str):
    body = tex.split(r"\begin{document}", 1)[1]
    running, backup = body.split(r"\appendix", 1)

    tags = TAG.findall(running)
    chunks = TAG.split(running)[1:]
    chunks = [chunks[i] for i in range(1, len(chunks), 2)]
    n = 0
    for tag, chunk in zip(tags, chunks):
        n += 1
        m = HEAD.search(chunk)
        head = re.sub(r"\s+", " ", m.group(1)).strip() if m else "(title page)"
        words, text = count_words(chunk)
        yield (str(n), head, visual_of(chunk), words, DISPOSITION[tag], text)

    for chunk in re.split(r"\\begin\{frame\}", backup)[1:]:
        chunk = chunk.split(r"\end{frame}")[0]
        m = HEAD.search(chunk)
        head = re.sub(r"\s+", " ", m.group(1)).strip() if m else "(untitled)"
        words, text = count_words(chunk)
        yield ("B", head, visual_of(chunk), words, "backup", text)


def main(csv: pathlib.Path | None, show_words: bool = False) -> int:
    tex = (HERE / "JMP_seminar_deck_v1.tex").read_text(encoding="utf-8")
    data = list(rows(tex))
    print("%-3s  %-58s  %-30s %5s  %s"
          % ("#", "headline", "visual / equation", "words", "25-min"))
    print("-" * 118)
    for n, head, vis, words, disp, text in data:
        print("%-3s  %-58s  %-30s %5d  %s"
              % (n, head[:58], vis[:30], words, disp))
        if show_words and words > 12:
            print("     -> %s" % text)
    print("-" * 118)
    running = [d for d in data if d[0] != "B"]
    print("%d running-order frames, %d backup; widest body %d words"
          % (len(running), len(data) - len(running),
             max(d[3] for d in data)))
    if csv:
        import csv as _csv
        with csv.open("w", newline="", encoding="utf-8") as fh:
            w = _csv.writer(fh)
            w.writerow(["slide", "headline", "visual_or_equation",
                        "body_words", "disposition_25min"])
            w.writerows([d[:5] for d in data])
        print("wrote", csv)
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", type=pathlib.Path, default=None)
    ap.add_argument("--words", action="store_true",
                    help="print the counted body text of any frame over budget")
    a = ap.parse_args()
    sys.exit(main(a.csv, a.words))
