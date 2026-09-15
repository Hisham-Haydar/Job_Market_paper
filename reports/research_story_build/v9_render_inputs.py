"""V9 report inputs: V8 evidence plus certified ex-ante results."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import json
import re

import v8_render_inputs as v8


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PAPER = ROOT / "manuscript"
FIG = v8.FIG
REG = deepcopy(v8.REG)
TABLES = deepcopy(v8.TABLES)
CAPTIONS = deepcopy(v8.CAPTIONS)
USED: set[str] = set()
DIAG_SHA256 = v8.DIAG_SHA256

WEA_RECORD = (
    ROOT.parent
    / "MNL_wea/docs/wea_sprint_1/stage4/stage4_certification_and_results_v1.json"
)
_record = json.loads(WEA_RECORD.read_text(encoding="utf-8"))


def register(key: str, value, pointer: str, units: str) -> None:
    REG[key] = {
        "value": value,
        "source": (
            "MNL_wea/docs/wea_sprint_1/stage4/"
            "stage4_certification_and_results_v1.json::" + pointer
        ),
        "status": "certified result",
        "units": units,
    }


_opportunity_shares = []
for _population in ("singles", "couples"):
    for _scale in ("unequivalised", "equivalised"):
        _row = _record["results"][_population][_scale]
        _prefix = f"wea_{_population}_{'uneq' if _scale == 'unequivalised' else 'eq'}"
        register(_prefix + "_n", _row["N"],
                 f"results.{_population}.{_scale}.N", "households")
        register(_prefix + "_mean", _row["mean"],
                 f"results.{_population}.{_scale}.mean", "EUR/month")
        register(_prefix + "_median", _row["median"],
                 f"results.{_population}.{_scale}.median", "EUR/month")
        register(_prefix + "_gini", _row["gini_EMPTY"],
                 f"results.{_population}.{_scale}.gini_EMPTY", "Gini")
        for _factor in ("P", "A", "B"):
            register(_prefix + "_phi_" + _factor.lower(), _row["phi"][_factor],
                     f"results.{_population}.{_scale}.phi.{_factor}", "Gini points")
        register(_prefix + "_opportunity_pct",
                 _row["A_plus_B_pct_of_baseline_gini"],
                 f"results.{_population}.{_scale}.A_plus_B_pct_of_baseline_gini",
                 "percent of baseline Gini")
        _opportunity_shares.append(_row["A_plus_B_pct_of_baseline_gini"])

register("wea_opportunity_min_pct", min(_opportunity_shares),
         "derived min(results.*.*.A_plus_B_pct_of_baseline_gini)",
         "percent of baseline Gini")
register("wea_opportunity_max_pct", max(_opportunity_shares),
         "derived max(results.*.*.A_plus_B_pct_of_baseline_gini)",
         "percent of baseline Gini")

_s_uneq = _record["results"]["singles"]["unequivalised"]
_s_eq = _record["results"]["singles"]["equivalised"]
register("wea_singles_access_earn_ratio_uneq",
         _s_uneq["phi"]["A"] / _s_uneq["phi"]["B"],
         "derived results.singles.unequivalised.phi.A / phi.B", "ratio")
register("wea_singles_access_earn_ratio_eq",
         _s_eq["phi"]["A"] / _s_eq["phi"]["B"],
         "derived results.singles.equivalised.phi.A / phi.B", "ratio")
register("wea_couples_opportunity_uneq_pct",
         _record["results"]["couples"]["unequivalised"]["A_plus_B_pct_of_baseline_gini"],
         "results.couples.unequivalised.A_plus_B_pct_of_baseline_gini",
         "percent of baseline Gini")
register("wea_couples_opportunity_eq_pct",
         _record["results"]["couples"]["equivalised"]["A_plus_B_pct_of_baseline_gini"],
         "results.couples.equivalised.A_plus_B_pct_of_baseline_gini",
         "percent of baseline Gini")
register("wea_couples_pref_uneq",
         _record["results"]["couples"]["unequivalised"]["phi"]["P"],
         "results.couples.unequivalised.phi.P", "Gini points")
register("wea_couples_pref_eq",
         _record["results"]["couples"]["equivalised"]["phi"]["P"],
         "results.couples.equivalised.phi.P", "Gini points")


def _wea_results_table() -> str:
    lines = [
        "",
        "Table: Ex-ante money-metric inequality and its exact Shapley allocation. "
        "Contributions are Gini points; access plus earnings is reported as a "
        "share of baseline inequality. Household-weighted.",
        "",
        "|Population|Scale|Households|Mean EUR/month|Median EUR/month|Baseline Gini|Preference|Access|Earning opportunities|Access + earnings / baseline|Ordering|",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for population, label in (("singles", "Single-adult"), ("couples", "Couple")):
        for scale, scale_label in (("unequivalised", "Raw household"),
                                   ("equivalised", "Equivalised")):
            row = _record["results"][population][scale]
            ordering = ("Earnings > access" if row["B_gt_A"]
                        else "Access > earnings")
            lines.append(
                f"|{label}|{scale_label}|{row['N']:,}|{row['mean']:,.1f}|"
                f"{row['median']:,.1f}|{row['gini_EMPTY']:.4f}|"
                f"{row['phi']['P']:.5f}|{row['phi']['A']:.5f}|"
                f"{row['phi']['B']:.5f}|"
                f"{row['A_plus_B_pct_of_baseline_gini']:.1f}%|{ordering}|"
            )
    return "\n".join(lines) + "\n"


def _comparison_table() -> str:
    lines = [
        "",
        "Table: The same access and earning-opportunity operators under two "
        "welfare perspectives. Shares are relative to each perspective's own "
        "baseline Gini. Neither perspective is designated primary.",
        "",
        "|Population|Scale|Attained-bundle A + B / baseline|Attained ordering|Ex-ante A + B / baseline|Ex-ante ordering|",
        "|---|---|---:|---|---:|---|",
    ]
    for population, label in (("singles", "Single-adult"), ("couples", "Couple")):
        for scale, scale_label in (("unequivalised", "Raw household"),
                                   ("equivalised", "Equivalised")):
            att = _record["comparison_W1F"][population][scale]
            ea = _record["results"][population][scale]
            att_order = "Earnings > access" if att["W1F_B_gt_A"] else "Access > earnings"
            ea_order = "Earnings > access" if ea["B_gt_A"] else "Access > earnings"
            lines.append(
                f"|{label}|{scale_label}|"
                f"{att['W1F_A_plus_B_pct_of_baseline']:.1f}%|{att_order}|"
                f"{ea['A_plus_B_pct_of_baseline_gini']:.1f}%|{ea_order}|"
            )
    return "\n".join(lines) + "\n"


TABLES["wea_results"] = _wea_results_table()
TABLES["perspective_comparison"] = _comparison_table()


def val(key: str, fmt: str | None = None) -> str:
    USED.add(key)
    value = REG[key]["value"]
    if key.endswith("_year"):
        return str(value)
    if fmt:
        return format(float(value), fmt)
    if isinstance(value, float):
        return format(value, ".6g")
    if isinstance(value, int):
        return format(value, ",d")
    return str(value)


def resolve(text: str, target: str) -> str:
    text = v8.strip_modes(text, target)
    text = re.sub(r"\{\{table:(.*?)\}\}", lambda match: TABLES[match[1]], text)

    def figure(match: re.Match) -> str:
        value = CAPTIONS[match[1]]
        if target == "paper":
            value = value.replace(v8.FIG.as_posix() + "/", "figures/v7/")
        return value

    text = re.sub(r"\{\{figure:(.*?)\}\}", figure, text)
    text = re.sub(
        r"\{\{n:([^|}]+?)(?:\|([^}]+))?\}\}",
        lambda match: val(match[1], match[2]),
        text,
    )
    if "{{" in text:
        raise SystemExit("Unresolved V9 token")
    return text
