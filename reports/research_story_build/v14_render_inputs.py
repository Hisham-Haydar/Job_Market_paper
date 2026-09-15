"""V14 report inputs: V13 evidence plus the regenerated theory figure (no numbers)."""
from __future__ import annotations

from v13_render_inputs import (  # noqa: F401
    HERE, ROOT, PAPER, FIG, REG, TABLES, CAPTIONS, USED, DIAG_SHA256,
    resolve, val, MATCHED, MATCHED_FIG, FIG13,
)

THEORY_FIG = ROOT / "manuscript/figures/v14/fig_v14_theory_own_set.png"
THEORY_CAPTION = (
    "Own-set equal-consumption equivalents: the theoretical construction from the companion "
    "theory paper. Two individuals with the same preferences but different ability sets attain "
    "different bundles. For each individual a common consumption level is assigned to every job "
    "in their own set; the level at which the preferred reference job becomes indifferent to the "
    "attained bundle is the money metric. Adapted from Haydar and Maniquet (2026), work in "
    "progress. This is the deterministic construction; the estimated ex-ante measure is its "
    "extension, defined in Section 3."
)
CAPTIONS["v14theory"] = "\n![" + THEORY_CAPTION + "](" + THEORY_FIG.as_posix() + "){width=95%}\n"
