"""V15 report inputs: V14 evidence, with the theory figure restored to the
original stored image and its caption corrected.

The image itself is unchanged from the copy embedded in reports V4-V11
(manuscript/figures/v5/theory_w1.png, byte-identical to
manuscript/figures/v3/theory_w1.png). Only the caption text changes: the
premise behind the V14 regeneration -- that the construction requires
identical preferences across the two individuals -- was wrong. Each
individual is evaluated with their own preferences and their own ability
set; the figure's point is that the resulting money metrics are directly
comparable between them.
"""
from __future__ import annotations

from v14_render_inputs import (  # noqa: F401
    HERE, ROOT, PAPER, FIG, REG, TABLES, CAPTIONS, USED, DIAG_SHA256,
    resolve, val, MATCHED, MATCHED_FIG, FIG13,
)

THEORY_CAPTION = (
    r"Own-set equal-consumption equivalents: the theoretical construction from the companion "
    r"theory paper. Two individuals, with preferences $R_i$ and $R_h$ and ability sets "
    r"$A=\{j,k\}$ and $A^{\prime}=\{k,\ell\}$, attain bundles $z_i$ and $z_h$. For each "
    r"individual, a common consumption level is assigned to every job in their own set; the "
    r"level at which the preferred reference job becomes indifferent to the attained bundle is "
    r"that individual's money metric, $W^1_i$ and $W^1_h$. The two metrics are then directly "
    r"comparable. Adapted from Haydar and Maniquet (2026), work in progress. This is the "
    r"deterministic construction; the estimated ex-ante measure is its extension, defined in "
    r"Section 3."
)

# Plain-text variant for the gallery, which renders no MathJax: mirrors the
# notation convention already used there (beta_c, lambda_c, W_EA, Delta I).
THEORY_CAPTION_GALLERY = (
    "Own-set equal-consumption equivalents: the theoretical construction from the companion "
    "theory paper. Two individuals, with preferences R_i and R_h and ability sets A = {j,k} and "
    "A' = {k,l}, attain bundles z_i and z_h. For each individual, a common consumption level is "
    "assigned to every job in their own set; the level at which the preferred reference job "
    "becomes indifferent to the attained bundle is that individual's money metric, W1_i and "
    "W1_h. The two metrics are then directly comparable. Adapted from Haydar and Maniquet "
    "(2026), work in progress. This is the deterministic construction; the estimated ex-ante "
    "measure is its extension, defined in Section 3."
)

# Restore the original stored image; do not reuse the V14 regeneration.
THEORY_FIG = ROOT / "manuscript/figures/v5/theory_w1.png"
CAPTIONS["theory"] = "\n![" + THEORY_CAPTION + "](" + THEORY_FIG.as_posix() + "){width=95%}\n"

# Known, disclosed defect in the restored source image (not corrected here; a
# redraw is what lost the construction in V14): a few labels overlap --
# y(k) sits on its own marker, and the R_i/R_h labels collide with the
# y(l)/y'(l) labels. See JMP_v14_to_v15_theory_figure_restore_v1.md.
