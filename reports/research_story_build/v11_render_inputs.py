"""V11 report inputs: V10 evidence plus source-bound keys used by the new text.

The new keys register values that already exist in certified or generated
records; nothing is estimated, priced or recomputed:
- attained-bundle access-plus-earnings shares from the certified ex-ante record's
  ``comparison_W1F`` block;
- matched-household illustration quantities from
  ``reports/v11_matched_households.json``.
"""
from __future__ import annotations

import json

from v10_render_inputs import (  # noqa: F401
    HERE, ROOT, PAPER, FIG, REG, TABLES, CAPTIONS, USED, DIAG_SHA256,
    resolve, val,
)
import v9_render_inputs as v9

WEA_SOURCE = "MNL_wea/docs/wea_sprint_1/stage4/stage4_certification_and_results_v1.json"
MATCHED = ROOT / "reports/v11_matched_households.json"
MATCHED_FIG = ROOT / "manuscript/figures/v11/fig_matched_households_v11.png"

_att = []
for _population in ("singles", "couples"):
    for _scale in ("unequivalised", "equivalised"):
        _row = v9._record["comparison_W1F"][_population][_scale]
        _key = f"att_{_population}_{'uneq' if _scale == 'unequivalised' else 'eq'}_opportunity_pct"
        REG[_key] = {
            "value": _row["W1F_A_plus_B_pct_of_baseline"],
            "source": f"{WEA_SOURCE}::comparison_W1F.{_population}.{_scale}.W1F_A_plus_B_pct_of_baseline",
            "status": "certified comparison record",
            "units": "percent of baseline Gini",
        }
        _att.append(_row["W1F_A_plus_B_pct_of_baseline"])
for _name, _value in (("att_opportunity_min_pct", min(_att)),
                      ("att_opportunity_max_pct", max(_att))):
    REG[_name] = {
        "value": _value,
        "source": f"derived {_name[16:19]}({WEA_SOURCE}::comparison_W1F.*.*.W1F_A_plus_B_pct_of_baseline)",
        "status": "certified comparison record",
        "units": "percent of baseline Gini",
    }

_matched = json.loads(MATCHED.read_text(encoding="utf-8"))
for _key, _field, _units in (
    ("mh_admissible_pairs", "selection_rule.admissible_pairs", "pairs"),
    ("mh_leisure_weight_a", "leisure_weight_A", "utility weight"),
    ("mh_leisure_weight_b", "leisure_weight_B", "utility weight"),
    ("mh_leisure_distance", "leisure_profile_distance", "standardised distance"),
    ("mh_leisure_cut", "leisure_profile_distance_p10_cut", "standardised distance"),
    ("mh_access_ratio", "access_mass_ratio_A_over_B", "ratio"),
    ("mh_employment_share_a", "opportunity_employment_share_A", "share"),
    ("mh_employment_share_b", "opportunity_employment_share_B", "share"),
    ("mh_wage_gap", "wage_location_gap_B_minus_A_logpoints", "log points"),
    ("mh_crossing_wage", "A_more_offers_paying_at_least_w_up_to_eur_per_hour", "EUR/hour"),
    ("mh_opportunity_distance", "opportunity_distance", "total variation"),
    ("mh_opportunity_distance_median", "opportunity_distance_admissible_median", "total variation"),
):
    _value = _matched
    for _part in _field.split("."):
        _value = _value[_part]
    REG[_key] = {
        "value": _value,
        "source": "Job_Market_paper/reports/v11_matched_households.json::" + _field,
        "status": "model illustration (rounded)",
        "units": _units,
    }

if not (_matched["wage_offer_FOSD_B_over_A"] and not _matched["wage_offer_FOSD_A_over_B"]):
    raise SystemExit("matched-household dominance statement no longer holds; revise the text")
if _matched["hours_density_distance"] != 0.0 or _matched["occupation_mass_distance"] != 0.0:
    raise SystemExit("matched-household hours/occupation identity no longer holds; revise the text")

CAPTIONS["matched"] = (
    "\n![Two matched single-adult households under the accepted specification, "
    "labelled A and B. Both are employed men in the same occupation group, hours "
    "band and observed-wage quintile, with nearly identical estimated leisure "
    "profiles. Panels: (a) leisure value of hours worked relative to "
    "non-employment; (b) employment share of opportunity mass; (c) the hours "
    "density, common to all single adults; (d) occupation mass, common within "
    "sex; (e) wage-offer density given employment; (f) relative intensity of "
    "offers paying at least a given hourly wage, log scale. Model-implied "
    "quantities for a pair selected by a stated rule; not causal and not "
    "representative.](" + MATCHED_FIG.as_posix() + "){width=95%}\n"
)
