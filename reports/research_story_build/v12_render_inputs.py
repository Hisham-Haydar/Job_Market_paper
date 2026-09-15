"""V12 report inputs: V11 evidence with caption and label corrections only.

No value changes. Edits:
- the attained-bundle Shapley table described the access pathway without local
  unemployment exposure; the executed substitution
  (preseminar_pab_record_v1.json, coalition_invariance.*.substituted_covariates)
  includes it, as the body text already states;
- fit-table and fit-figure captions no longer point to an appendix they have left.
"""
from __future__ import annotations

from v11_render_inputs import (  # noqa: F401
    HERE, ROOT, PAPER, FIG, REG, TABLES, CAPTIONS, USED, DIAG_SHA256,
    resolve, val, MATCHED, MATCHED_FIG,
)

OLD_A = "Region, urban or rural location, and year"
NEW_A = "Local unemployment exposure, region, urban or rural location, and year"
if TABLES["decomposition_reader"].count(OLD_A) != 4:
    raise SystemExit("expected four access rows in the attained-bundle Shapley table")
TABLES["decomposition_reader"] = TABLES["decomposition_reader"].replace(OLD_A, NEW_A)

for key in ("fitsingles", "fitcouples"):
    old = " Technical definitions and provenance are retained in this appendix."
    if old not in TABLES[key]:
        raise SystemExit("fit table caption changed: " + key)
    TABLES[key] = TABLES[key].replace(
        old, " Population predictions integrate the model over opportunities and taste shocks.")

_les = TABLES["observed_les"]
_caption_start = _les.index("Table:")
_caption_end = _les.index("\n\n|Group|")
TABLES["observed_les"] = (
    _les[:_caption_start]
    + "Table: Observed raw labour-force status, weighted shares with unweighted counts in "
      "parentheses, by sex and household type, on the final estimation samples. Spouses' raw "
      "status is recovered from the person-level survey file. The structural model maps both "
      "unemployment and inactivity to its single non-work alternative."
    + _les[_caption_end:]
)

_old_band = ("Technical predictive-fit figure retained for provenance. The main text "
             "reports the economic interpretation in words.")
if _old_band not in CAPTIONS["fitband"]:
    raise SystemExit("fit-band caption changed")
CAPTIONS["fitband"] = CAPTIONS["fitband"].replace(
    _old_band,
    "Weighted extensive-margin accuracy by group against the range the estimated "
    "model itself produces by chance; groups whose statistic is too imprecise are withheld.")
CAPTIONS["nodeconvergence"] = CAPTIONS["nodeconvergence"].replace(
    "Technical numerical-convergence figure retained for provenance.",
    "Numerical convergence of predicted participation as the number of integration points grows.")
