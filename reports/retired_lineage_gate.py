#!/usr/bin/env python
"""Shared PATH-based retired-lineage gate (LINEAGE-SWEEP-1).

Detects a *read* of a retired welfare-decomposition artifact by scanning the
actual source text of build scripts / generated registries / rendered
artifacts for the retired file's own PATH or basename -- never by grepping
rendered prose for a specific wording (e.g. "job-access opportunities") that
a rewrite can trivially dodge while the underlying data source is unchanged.
If a retired filename shows up in a build script's read call, or inside a
registry's own "source" provenance field, or leaks into rendered text as a
citation, the read happened -- independent of whatever the surrounding prose
says. A string gate over rendered wording passes vacuously once the text
changes; this gate does not, because it is anchored to the artifact's path.

Retired under DECOMP-PRESEMINAR-1 (superseded by DECOMP-2 / preseminar_pab_v1;
MNL_decomp worktree, branch welfare/preseminar-pab, commit b52761b4):

    headline_decomposition_v1.csv
    ss8_step1_states_v1.json
    cw_step3_states_v1.json
    gn_step2_nested_v1.json
    the s12_*_attributions family   (e.g. s12_six_index_attributions_v1.csv,
                                     s12_couples_nested_D_attributions_v1.*)
    the *headline_shares family     (e.g. s12_s11_cr1_headline_shares_v1.csv)
    s12_welfare_record_report_v1.md (S12 welfare-record narrative report)

Also forbidden by the ruling, but NOT path-detectable (see the four-factor
content check below, which is a supplementary heuristic, not the primary
mechanism): any four-factor P/A/B/D decomposition, and the withdrawn label
"job-access opportunities".

NOT retired -- do not add to RETIRED_PATH_PATTERNS without a fresh ruling:
s11_* estimation/fit artifacts; S12 *pricing*-panel files used only for plain
welfare levels/Lorenz curves (e.g. s12_principal_welfare_distributions_v1);
s12_w4_premise_audit_v1 (reference-domain sensitivity, not an attribution --
flagged UNVERIFIED-adjacent in the LINEAGE-SWEEP-1 report, not auto-failed
here, since one audit pass called it ACCEPTED and a sibling pass called it
RETIRED-by-broad-era; that disagreement is for a ruling, not this gate).

ACCEPTED_PATH_MARKERS are informational only (no verifier currently asserts
their presence) -- they let a human reading gate output see, at a glance,
whether a surface has migrated to the replacement lineage at all.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, Iterable, List

RETIRED_PATH_PATTERNS: Dict[str, re.Pattern] = {
    "headline_decomposition_v1": re.compile(r"headline_decomposition_v1"),
    "ss8_step1_states_v1": re.compile(r"ss8_step1_states_v1"),
    "cw_step3_states_v1": re.compile(r"cw_step3_states_v1"),
    "gn_step2_nested_v1": re.compile(r"gn_step2_nested_v1"),
    "s12_*_attributions family": re.compile(r"s12_\w*attribution\w*"),
    "*headline_shares family": re.compile(r"\w*headline_shares\w*"),
    "s12_welfare_record_report_v1": re.compile(r"s12_welfare_record_report_v1"),
}

ACCEPTED_PATH_MARKERS: Dict[str, re.Pattern] = {
    "coalition_values (DECOMP-2)": re.compile(r"coalition_values_"),
    "shapley_PAB (DECOMP-2)": re.compile(r"shapley_PAB_"),
    "log_variance_split_v1 (DECOMP-2)": re.compile(r"log_variance_split_v1"),
    "anchor_excluded_arm_v1 (DECOMP-2)": re.compile(r"anchor_excluded_arm_v1"),
    "preseminar_pab_v1 (DECOMP-2)": re.compile(r"preseminar_pab_v1"),
}

# Supplementary, explicitly non-primary: the four-factor P/A/B/D decomposition
# is forbidden "regardless of source file" and so cannot be caught by a path
# check at all -- it is a structural/mathematical signature, not a filename.
# These patterns are a best-effort net for it; a clean result here is NOT
# proof of compliance the way a clean RETIRED_PATH_PATTERNS scan is, because
# prose can be reworded around it. Report both, and label them differently.
FOUR_FACTOR_CONTENT_PATTERNS: Dict[str, re.Pattern] = {
    "X_i=(P_i,A_i,B_i,D_i) coalition notation": re.compile(
        r"X_i\s*=\s*\(\s*P_i\s*,\s*A_i\s*,\s*B_i\s*,\s*D_i\s*\)"),
    "four structural equalization operators": re.compile(
        r"four structural equalization operators", re.IGNORECASE),
    "four-player game / four operators": re.compile(
        r"four[- ](?:player game|operators|component)", re.IGNORECASE),
    "sixteen coalitions (2^4)": re.compile(r"sixteen coalitions", re.IGNORECASE),
}

# A rendered P/A/B/D attribution table need not use any of the phrases above
# at all (v3.html/v4.html: no literal retired filename, no "four operators"
# wording -- just four table rows). Co-occurrence of an "Access" row, an
# "Earning opportunities" row, and a resources/needs row ("Budget resources",
# "resources and needs", "resources/needs") is the structural fingerprint of
# that table, distinct from the r6 deck's legitimate two-row "job access" +
# "earning opportunities" split (which never adds a resources/needs row
# alongside them). Implemented as plain substring checks, NOT a regex with
# unanchored zero-width lookaheads -- that form is O(n^2) on an 8-10MB HTML
# file (re.search tries every start offset; each lookahead then rescans
# forward) and hangs for minutes. Three `in` checks are O(n) each.
_PABD_TABLE_PARTS = (
    ("access", re.compile(r"\baccess\b", re.IGNORECASE)),
    ("earning opportunities", re.compile(r"earning opportunities", re.IGNORECASE)),
    ("resources/needs row", re.compile(
        r"budget resources|resources[ /-]and[ /-]needs|resources[ /]needs|"
        r"endowments[ /-]and[ /-]needs|household endowments",
        re.IGNORECASE)),
)


def _has_pabd_table_signature(text: str) -> bool:
    return all(pat.search(text) for _, pat in _PABD_TABLE_PARTS)


def scan_four_factor(text: str) -> List[str]:
    """Supplementary, non-path content-signature scan for a forbidden
    four-factor P/A/B/D decomposition. Weaker evidence than scan_text() on
    RETIRED_PATH_PATTERNS: a clean result here does not clear a file the way
    a clean path scan does, because prose can be reworded around it; a hit
    here is still strong evidence, because the co-occurrence signature is
    the table structure itself, not a specific phrase."""
    hits = scan_text(text, FOUR_FACTOR_CONTENT_PATTERNS)
    if _has_pabd_table_signature(text):
        hits.append("co-occurring Access/Earning-opportunities/resources-needs "
                     "rows (P/A/B/D table)")
    return hits


def scan_text(text: str, patterns: Dict[str, re.Pattern] | None = None) -> List[str]:
    """Return the names of every pattern (default: retired paths) found in `text`."""
    patterns = RETIRED_PATH_PATTERNS if patterns is None else patterns
    return [name for name, pat in patterns.items() if pat.search(text)]


def _strip_full_line_py_comments(text: str) -> str:
    """Drop lines that are ONLY a '#' comment (leading whitespace then '#').
    A comment documenting that a retired file is deliberately NOT read (e.g.
    "# NOT sourced from headline_decomposition_v1.csv") is not itself a read
    and must not fail the gate -- but this must not get cute: it strips
    whole comment-only lines, nothing else. A retired filename appearing on
    a CODE line (`pd.read_csv("headline_decomposition_v1.csv")`, or in a
    trailing inline comment on a code line) still scans, still fails."""
    return "\n".join("" if line.lstrip().startswith("#") else line
                      for line in text.splitlines())


def scan_files(paths: Iterable[Path],
                patterns: Dict[str, re.Pattern] | None = None) -> Dict[Path, List[str]]:
    """Scan each file's own text. Skips files that don't exist or aren't text.
    For `.py` files, full-line comments are stripped first (see
    `_strip_full_line_py_comments`) so documentation of a retirement doesn't
    itself trip the gate meant to catch the retirement."""
    violations: Dict[Path, List[str]] = {}
    for p in paths:
        if not p.exists() or not p.is_file():
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if p.suffix == ".py":
            text = _strip_full_line_py_comments(text)
        hits = scan_text(text, patterns)
        if hits:
            violations[p] = hits
    return violations


def format_violations(violations: Dict[Path, List[str]], root: Path | None = None) -> str:
    lines = []
    for p, hits in violations.items():
        shown = p.relative_to(root) if root else p
        lines.append("  RETIRED-LINEAGE READ  %s: %s" % (shown, ", ".join(hits)))
    return "\n".join(lines)


if __name__ == "__main__":
    import sys
    root = Path(__file__).resolve().parents[1]
    targets = [Path(a) for a in sys.argv[1:]] or [root]
    files: List[Path] = []
    for t in targets:
        files.extend(t.rglob("*")) if t.is_dir() else files.append(t)
    v = scan_files([f for f in files if f.suffix in
                     {".py", ".json", ".md", ".tex", ".html", ".csv"}])
    if v:
        print(format_violations(v, root))
        sys.exit(1)
    print("no retired-lineage path references found under: %s"
          % ", ".join(str(t) for t in targets))
