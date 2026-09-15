"""V13 report inputs: V12 evidence plus the four regenerated figures.

Every number printed on a V13 figure is registered under a ``fig13_`` key whose
value and printed text come from reports/v13_figure_values.json, and the value is
re-read here from its named source (CSV cell or certified JSON field) and must
match exactly. Captions carry no numbers.
"""
from __future__ import annotations

import csv
import json

from v12_render_inputs import (  # noqa: F401
    HERE, ROOT, PAPER, FIG, REG, TABLES, CAPTIONS, USED, DIAG_SHA256,
    resolve, val, MATCHED, MATCHED_FIG,
)

WORKSPACE = ROOT.parent
FIG13 = ROOT / "manuscript/figures/v13"
FIGURE_VALUES = ROOT / "reports/v13_figure_values.json"
ACCESS_DEF = "local unemployment exposure, region, urban or rural location and year"


def source_value(pointer: str) -> float:
    """Resolve a figure-value source pointer to the value stored at that source."""
    derived = pointer.startswith("derived ")
    path_part, field = pointer.removeprefix("derived ").split("::", 1)
    path = WORKSPACE / path_part
    if path.suffix == ".csv":
        spec = dict(item.split("=", 1) for item in field.split(",")[:-1])
        column = field.split(",")[-1]
        with path.open(encoding="utf-8", newline="") as handle:
            row = next(r for r in csv.DictReader(handle) if all(r[k] == v for k, v in spec.items()))
        return float(row[column])
    document = json.loads(path.read_text(encoding="utf-8"))
    if derived:
        numerator, rest = field.split(" / ")
        denominator = rest.removesuffix(" * 100")

        def get(dotted: str):
            node = document
            for part in dotted.split("."):
                node = node[part]
            return node
        base = ".".join(numerator.split(".")[:-2]) if ".W1F_phi." in numerator else ".".join(numerator.split(".")[:-2])
        return 100 * get(numerator) / get(base + "." + denominator)
    node = document
    for part in field.split("."):
        node = node[part]
    return float(node)


_figure_values = json.loads(FIGURE_VALUES.read_text(encoding="utf-8"))["values"]
for _key, _entry in _figure_values.items():
    _resolved = source_value(_entry["source"])
    if _resolved != _entry["value"] or format(_resolved, _entry["format"]) != _entry["text"]:
        raise SystemExit(f"figure value {_key} does not match its source")
    REG["fig13_" + _key] = {"value": _entry["value"], "source": _entry["source"],
                            "status": "figure value from certified source", "units": _entry["units"]}


def _caption(name: str, text: str) -> str:
    return "\n![" + text + "](" + (FIG13 / name).as_posix() + "){width=95%}\n"


CAPTIONS["v13architecture"] = _caption(
    "fig_v13_architecture.png",
    "How the decomposition is built. Three channels can be equalised: systematic preferences; "
    f"local labour-market access ({ACCESS_DEF}); and systematic earning opportunities. Household "
    "resources, needs and composition are held fixed in every coalition. Each counterfactual household "
    "is evaluated under both welfare perspectives, inequality is measured with the household-weighted "
    "Gini, and the Shapley rule averages each channel's marginal contribution over all orders.")
CAPTIONS["v13attdecomp"] = _caption(
    "fig_v13_att_decomposition.png",
    "Attained-bundle welfare: exact Shapley contribution of each channel to the change in the Gini, "
    "in Gini points, for raw and equivalised reporting, with each baseline Gini stated in the panel. "
    f"Access is local labour-market access ({ACCESS_DEF}). Preliminary. Household resources, needs and "
    "composition are held fixed. The preference contribution changes sign with equivalisation in both "
    "samples, so no directional claim is made about it. Values are the coalition and Shapley records of "
    "the attained-bundle decomposition.")
CAPTIONS["v13eadecomp"] = _caption(
    "fig_v13_ea_decomposition.png",
    "Ex-ante welfare: exact Shapley contribution of each channel to the change in the Gini, in Gini "
    "points, for raw and equivalised reporting, with each baseline Gini stated in the panel. Access is "
    f"local labour-market access ({ACCESS_DEF}). The calculation passed its numerical checks; household "
    "resources, needs and composition are held fixed. For couples the preference contribution changes "
    "sign with equivalisation.")
CAPTIONS["v13central"] = _caption(
    "fig_v13_central_result.png",
    "The central result. Access and earning-opportunity contributions, each as a percentage of its own "
    "perspective's baseline Gini, under attained-bundle welfare (ATT) and ex-ante welfare (EA). Access is "
    f"local labour-market access ({ACCESS_DEF}). For single-adult households earning opportunities are "
    "larger under ATT and access is larger under EA, on both scales; couples show no such reversal. "
    "Household resources, needs and composition are held fixed; neither perspective is designated primary.")
