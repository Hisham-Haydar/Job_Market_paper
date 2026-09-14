#!/usr/bin/env python
"""Layout check on the compiled v5 PDF.

A LaTeX "Overfull \\vbox ... while \\output is active" warning does not say which
page overflowed or by how much a reader would see it. This measures the rendered
result directly: for every page, the lowest and highest ink, against the page
box. Anything below the bottom margin is a visible defect.

Exit code 0 if no page has ink outside the print area.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pymupdf

PDF = (Path(__file__).resolve().parent.parent
       / 'manuscript/JMP_working_paper_for_seminar_v6.pdf')
# 25 mm margins, minus the space the page number legitimately occupies
MM = 72.0 / 25.4
TOP = 25.0 * MM - 6.0
BOTTOM_ALLOWANCE = 36.0          # the folio baseline sits this far into the margin
LEFT = 25.0 * MM - 6.0


def main() -> int:
    doc = pymupdf.open(PDF)
    bad = []
    for i, page in enumerate(doc, 1):
        r = page.rect
        bottom_limit = r.height - (25.0 * MM) + BOTTOM_ALLOWANCE
        lo, hi, left, right = None, None, None, None
        for b in page.get_text('blocks'):
            x0, y0, x1, y1 = b[:4]
            lo = y0 if lo is None else min(lo, y0)
            hi = y1 if hi is None else max(hi, y1)
            left = x0 if left is None else min(left, x0)
            right = x1 if right is None else max(right, x1)
        for d in page.get_drawings():
            rr = d['rect']
            if rr.is_empty or rr.height > r.height:
                continue
            hi = rr.y1 if hi is None else max(hi, rr.y1)
            lo = rr.y0 if lo is None else min(lo, rr.y0)
        if hi is not None and hi > bottom_limit:
            bad.append((i, 'ink %.1fpt below the print area'
                        % (hi - bottom_limit)))
        if lo is not None and lo < TOP - 8:
            bad.append((i, 'ink %.1fpt above the print area' % (TOP - lo)))
        if right is not None and right > r.width - LEFT + 10:
            bad.append((i, 'ink %.1fpt past the right margin'
                        % (right - (r.width - LEFT))))
    print('%s: %d pages' % (PDF.name, doc.page_count))
    if bad:
        for i, msg in bad:
            print('  page %-3d %s' % (i, msg))
        print('LAYOUT: FAIL (%d pages)' % len(bad))
        return 1
    print('LAYOUT: PASS, no ink outside the print area')
    return 0


if __name__ == '__main__':
    sys.exit(main())
