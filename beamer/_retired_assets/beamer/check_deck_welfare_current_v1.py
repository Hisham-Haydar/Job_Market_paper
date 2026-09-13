#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fail while the deck still carries the retracted welfare record.

The deck's welfare slides were written against the historical record. s12
supersedes every share on them and reverses the ordering inside the environment.
This check fails while any of the retracted figures is still present without the
superseded banner, so the deck cannot be built and presented as if current.

It passes either when the block carries the banner (the honest holding state) or
when the retracted figures are gone (the rebased state).
"""
import sys
from pathlib import Path

DECK = (Path(__file__).resolve().parents[1]
        / "manuscript/JMP_seminar_deck_content_v2.md")

# figures that exist only in the historical record
RETRACTED = {
    "58%": "environment split with endowments and needs leading",
    "45.73": "nested non-labour resources share",
    "12.45": "nested composition share",
    "35.5%": "narrow job-opportunity total as about a third",
    "93.7": "environment share",
    "I00 = 0.134": "baseline Gini",
    "13.05": "geographic access share",
    "19.58": "men's job-access share",
}
BANNER = "SUPERSEDED — WELFARE BLOCK"


def main() -> int:
    if not DECK.exists():
        print("FAIL: deck content not found")
        return 1
    t = DECK.read_text(encoding="utf-8")
    present = {k: v for k, v in RETRACTED.items() if k in t}
    banner = BANNER in t
    print("retracted welfare figures still in the deck: %d" % len(present))
    for k, v in sorted(present.items()):
        print("   %-14s %s" % (k, v))
    print("superseded banner present: %s" % banner)
    if present and not banner:
        print()
        print("VERDICT: FAIL -- the deck states retracted welfare results with no "
              "banner. Either rebase the welfare block onto the s12 record or "
              "mark it superseded.")
        return 1
    if present:
        print()
        print("VERDICT: PASS (holding) -- retracted figures remain but the block "
              "is marked superseded and must not be presented.")
        return 0
    print()
    print("VERDICT: PASS -- no retracted welfare figure remains in the deck.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
