"""Reader-facing V8 render inputs backed by the frozen V7 evidence.

V8 changes presentation only.  Corrected predictive quantities are read from
their accepted artifacts, while every unaffected numerical entry is inherited
from the V7 number registry.  No estimation, pricing, or decomposition routine
is run here.
"""
from copy import deepcopy
from pathlib import Path
import csv
import json
import re

import v6_render_inputs as frozen


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PAPER = ROOT / "manuscript"
FIG = PAPER / "figures/v7"
TABLE = PAPER / "tables/v7"

MNL_POSFIT = ROOT.parent / "MNL_posfit"
POSFIT = MNL_POSFIT / "outputs/positive_fit_diagnostics_v3b"
BAND_FIX_2 = (MNL_POSFIT / "experiments/JMP_SEMINAR_SPRINT/runs/"
              "bandfix2_recompute")
NEW_RESULTS = BAND_FIX_2 / "new_results_v1.json"

_v7_registry = json.loads(
    (ROOT / "reports/numbers_of_record_v7.json").read_text(encoding="utf-8")
)
REG = deepcopy(frozen.REG)
REG.update(deepcopy(_v7_registry["entries"]))
TABLES = deepcopy(frozen.TABLES)
CAPTIONS = deepcopy(frozen.CAPTIONS)
USED = set()
DIAG_SHA256 = frozen.DIAG_SHA256

TABLES["access"] = (
    TABLES["access"]
    .replace("width 26.5 hours per week", "width 29.5 hours per week")
    .replace("Part-time lower, [17.5, 21.5)", "Part-time lower, [18.5, 21.5)")
    .replace("Part-time upper, [28.5, 30.5)", "Part-time upper, [29.5, 30.5)")
    .replace("Full-time upper, [36.5, 40.5]", "Full-time upper, [37.5, 40.5]")
)
CAPTIONS["theory"] = CAPTIONS["theory"].replace(
    "the estimated measure is its ex-ante extension, defined in Section 4.",
    "the current empirical Mapping-F measure evaluates the attained bundle "
    "against the non-employment reference state, as defined in Section 4.",
)


def register(key, value, source, status="corrected result", units="dimensionless"):
    REG[key] = {
        "value": value,
        "source": source,
        "status": status,
        "units": units,
    }


_new = json.loads(NEW_RESULTS.read_text(encoding="utf-8"))
_moments = {
    (row["model"], row["sex"], row["moment"]): row
    for row in _new["moments"]
}
_moment_source = (
    "MNL_posfit/experiments/JMP_SEMINAR_SPRINT/runs/"
    "bandfix2_recompute/new_results_v1.json"
)
for _model, _key in (("SINGLES", "mae_singles"),
                     ("COUPLES", "mae_couples"),
                     ("RUM-A", "mae_ruma"),
                     ("RUM-B", "mae_rumb")):
    register(
        _key,
        _new["summaries"][_model]["mean_absolute_error"],
        f"{_moment_source}::summaries.{_model}.mean_absolute_error",
        units="mean absolute deviation",
    )

for _model, _sex, _key in (
    ("SINGLES", "male", "gap37_single_men"),
    ("SINGLES", "female", "gap37_single_women"),
    ("COUPLES", "male", "gap37_coupled_men"),
    ("COUPLES", "female", "gap37_coupled_women"),
):
    _row = _moments[(_model, _sex, "hours::h_36_5_37_5")]
    register(
        _key,
        100 * (float(_row["observed"]) - float(_row["predicted"])),
        f"{_moment_source}::moments[{_model},{_sex},hours::h_36_5_37_5]",
        status="corrected diagnostic",
        units="percentage points",
    )


def _csv_rows(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


_bands = {
    row["group"]: row
    for row in _csv_rows(POSFIT / "model_simulated_bands.csv")
    if row["weighting"] == "weighted"
    and row["scope"] == "all"
    and row["statistic"] == "extensive_accuracy"
    and row["support"] == "full"
}
_adequacy = {
    row["group"]: row
    for row in _csv_rows(POSFIT / "g2_adequacy.csv")
    if row["weighting"] == "weighted"
    and row["scope"] == "all"
    and row["statistic"] == "extensive_accuracy"
}
_fit_source = "MNL_posfit/outputs/positive_fit_diagnostics_v3b"
for _group, _prefix in (("singles_female", "single_women"),
                        ("couples_female", "coupled_women")):
    _row = _bands[_group]
    for _field, _suffix in (("observed", "accuracy"),
                            ("simulated_p025", "band_lo"),
                            ("simulated_p975", "band_hi")):
        register(
            f"{_prefix}_{_suffix}_pct",
            100 * float(_row[_field]),
            f"{_fit_source}/model_simulated_bands.csv::{_group}.{_field}",
            status="corrected diagnostic",
            units="percent",
        )

for _group, _prefix in (("singles_male", "single_men"),
                        ("couples_male", "coupled_men"),
                        ("singles_female", "single_women"),
                        ("couples_female", "coupled_women")):
    register(
        f"{_prefix}_integration_ratio",
        float(_adequacy[_group]["adequacy_ratio_mcse_to_sampling_sd"]),
        f"{_fit_source}/g2_adequacy.csv::{_group}.adequacy_ratio_mcse_to_sampling_sd",
        status="corrected diagnostic",
        units="ratio",
    )


def _table_from_csv(path, caption):
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.reader(handle))
    headers, body = rows[0], rows[1:]
    return (
        "\n" + caption + "\n\n|" + "|".join(headers) + "|\n|"
        + "|".join(["---"] * len(headers)) + "|\n"
        + "".join("|" + "|".join(cell.replace("|", "/") for cell in row)
                  + "|\n" for row in body)
        + "\n"
    )


# The technical appendix retains the corrected V7 tables without regenerating
# any numbers.  Its captions deliberately preserve detailed implementation
# terminology because that appendix is collapsed and explicitly provenance-only.
TABLES["fitsingles"] = _table_from_csv(
    TABLE / "v7_fit_singles.csv",
    "Table: Corrected observed and predicted population moments, single adults. "
    "Technical definitions and provenance are retained in this appendix.",
)
TABLES["fitcouples"] = _table_from_csv(
    TABLE / "v7_fit_couples.csv",
    "Table: Corrected observed and predicted population moments, couples. "
    "Technical definitions and provenance are retained in this appendix.",
)
TABLES["benchmark"] = _table_from_csv(
    TABLE / "v7_benchmark.csv",
    "Table: The preferred single-adult model and the two re-estimated "
    "common-opportunity benchmarks.",
)


def _reader_welfare_table(source):
    lines = source.strip().splitlines()
    body = lines[4:]
    return """
Table: Attained-bundle money-metric well-being and disposable consumption,
modified-OECD equivalised. Household euros per month, weighted using household
weights. The two populations are reported separately.

|Population|Households|Workers|Non-workers|Consumption mean|Consumption median|Consumption Gini|Money-metric mean|Money-metric median|Money-metric Gini|
|---|---|---|---|---|---|---|---|---|---|
""" + "\n".join(body) + "\n"


def _reader_decomposition_table(source):
    rows = []
    for line in source.splitlines():
        if not line.startswith("|") or line.startswith("|---") or "Population" in line:
            continue
        cells = line.strip("|").split("|")
        if len(cells) != 7:
            continue
        factor = cells[2]
        if factor == "P":
            cells[2] = "Systematic preferences"
            cells[3] = "Age profiles and the child-related shifter"
        elif factor == "A":
            cells[2] = "Coarse access"
            cells[3] = "Region, urban or rural location, and year"
        elif factor == "B":
            cells[2] = "Earning opportunities"
            cells[3] = "Systematic wage-offer location"
        elif "Delta I" in factor or "\\Delta I" in factor:
            cells[2] = "$\\Delta I$"
            cells[3] = "Total change after all three equalizations"
        rows.append("|" + "|".join(cells) + "|")
    return """
Table: Complete Shapley allocation of the change in the Gini after equalising
the three modelled dimensions. Contributions are Gini points; shares refer to
$\\Delta I$, not to baseline inequality. The last column reports an independent
simulation run. The preference share is left unstated because its contribution
changes sign with equivalisation.

|Population|Scale|Dimension|Economic content|Gini-point contribution|Share of $\\Delta I$|Independent-run Gini-point|
|---|---|---|---|---|---|---|
""" + "\n".join(rows) + "\n"


TABLES["welfare_reader"] = _reader_welfare_table(TABLES["baselinef1"])
TABLES["decomposition_reader"] = _reader_decomposition_table(TABLES["pabshapley"])


def _md_figure(path, caption):
    return "\n![" + caption + "](" + path.as_posix() + "){width=95%}\n"


CAPTIONS["fitband"] = _md_figure(
    FIG / "fitext_band_v3b.png",
    "Technical predictive-fit figure retained for provenance. The main text "
    "reports the economic interpretation in words.",
)
CAPTIONS["nodeconvergence"] = _md_figure(
    FIG / "node_convergence_v3b.png",
    "Technical numerical-convergence figure retained for provenance.",
)
CAPTIONS["fit"] = _md_figure(
    FIG / "fit_by_margin_v7.png",
    "Corrected population fit: observed against predicted shares.",
)


def strip_modes(text, target):
    for tag in ("report-only", "paper-only"):
        if tag == target + "-only":
            text = text.replace("{{" + tag + "}}", "").replace("{{/" + tag + "}}", "")
        else:
            text = re.sub(r"\{\{" + tag + r"\}\}.*?\{\{/" + tag + r"\}\}",
                          "", text, flags=re.S)
    return text


def val(key, fmt=None):
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


def resolve(text, target):
    text = strip_modes(text, target)
    text = re.sub(r"\{\{table:(.*?)\}\}", lambda match: TABLES[match[1]], text)

    def figure(match):
        value = CAPTIONS[match[1]]
        if target == "paper":
            value = value.replace(FIG.as_posix() + "/", "figures/v7/")
            value = value.replace(frozen.FIG.as_posix() + "/", "figures/v5/")
        return value

    text = re.sub(r"\{\{figure:(.*?)\}\}", figure, text)
    text = re.sub(
        r"\{\{n:([^|}]+?)(?:\|([^}]+))?\}\}",
        lambda match: val(match[1], match[2]),
        text,
    )
    if "{{" in text:
        raise SystemExit("Unresolved V8 token")
    return text
