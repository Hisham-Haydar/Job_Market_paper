# -*- coding: utf-8 -*-
"""Shared machinery for the research-story HTML build.

Every numeral that appears in the rendered document is emitted as a <span> that
carries a data key; the browser fills it from one of two embedded JSON blocks.
Nothing numeric is typed into the prose.
"""
from __future__ import annotations

import base64
import csv
import io
import json
from pathlib import Path

MNL = Path("C:/Users/hisham/Repo/MNL")
JMP = Path("C:/Users/hisham/Repo/Job_Market_paper")
SPRINT = MNL / "experiments/JMP_SEMINAR_SPRINT"
FIGDIR = SPRINT / "figures"
LOCAL_FIGDIR = Path(__file__).resolve().parent / "figures"
TABDIR = SPRINT / "tables"
NOR_PATH = JMP / "reports/numbers_of_record_v1.json"

MAX_FIG_WIDTH = 1200


# --------------------------------------------------------------------------- #
# numeral emitters
# --------------------------------------------------------------------------- #
def n(key: str, fmt: str = "auto", d: int | None = None, note: str = "") -> str:
    """A number of record, read from numbers_of_record_v1.json at render time."""
    dd = "" if d is None else ' data-d="%d"' % d
    nt = (' data-note="%s"' % esc(note)) if note else ""
    return '<span class="n" data-src="nor" data-k="%s" data-f="%s"%s%s></span>' % (
        esc(key), esc(fmt), dd, nt)


def a(key: str, fmt: str = "auto", d: int | None = None, note: str = "") -> str:
    """A number from the auxiliary block (frozen CSV artefacts of record)."""
    dd = "" if d is None else ' data-d="%d"' % d
    nt = (' data-note="%s"' % esc(note)) if note else ""
    return '<span class="n" data-src="aux" data-k="%s" data-f="%s"%s%s></span>' % (
        esc(key), esc(fmt), dd, nt)


def math(tex: str, label: str = "", note: str = "") -> str:
    """A rendered display equation.  Marked `eq` so the numeral self-check
    treats it as notation rather than as a result, exactly as the ASCII
    equation blocks are treated."""
    lb = ('<span class="lbl">%s</span>' % esc(label)) if label else ""
    nt = ('<p class="mathnote">%s</p>' % note) if note else ""
    return ('<div class="math eq">%s' % lb) + r"\[" + tex + r"\]" + "</div>" + nt


def imath(tex: str) -> str:
    """Inline maths."""
    return '<span class="eq">' + r"\(" + tex + r"\)" + "</span>"


def lit(text: str, why: str) -> str:
    """A declared non-result numeral: a definition, a bound, a calendar year."""
    return '<span class="lit" data-why="%s">%s</span>' % (esc(why), esc(text))


def esc(s) -> str:
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


# --------------------------------------------------------------------------- #
# loaders
# --------------------------------------------------------------------------- #
def load_nor() -> dict:
    return json.loads(NOR_PATH.read_text(encoding="utf-8"))


def read_csv_rows(path: Path) -> list[dict]:
    with open(path, encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def _num(v):
    if v is None:
        return None
    s = str(v).strip()
    if s == "" or s.upper() in {"NA", "NAN", "NONE"}:
        return None
    try:
        return float(s)
    except ValueError:
        return s


_AUX_CACHE: dict | None = None


def aux_data() -> dict:
    """The auxiliary block, built once and reused by the section modules."""
    global _AUX_CACHE
    if _AUX_CACHE is None:
        _AUX_CACHE = build_aux()
    return _AUX_CACHE


def build_aux() -> dict:
    """The auxiliary block: frozen per-row artefacts the numbers file does not carry.

    numbers_of_record_v1.json holds 203 scalar entries.  It deliberately does not
    carry the 41-row parameter table or the per-cell external-validation table,
    both of which this document must print in full.  Those are read here from
    their own frozen CSV artefacts of record and embedded alongside, so that the
    no-typed-numbers rule holds for them too.
    """
    aux: dict = {"_sources": {}}

    # -- the 41 estimated coordinates ---------------------------------------- #
    p = FIGDIR / "fig08_coefficients_by_block.csv"
    rows = read_csv_rows(p)
    params = {}
    order = []
    for r in rows:
        key = r["param"]
        order.append(key)
        params[key] = {
            "param": key,
            "block": r["block"],
            "sub_block": r["sub_block"],
            "estimate": _num(r["estimate"]),
            "se_robust": _num(r["se_robust"]),
            "lo95": _num(r["lo95"]),
            "hi95": _num(r["hi95"]),
            "z_robust": _num(r["z_robust"]),
            "at_active_bound": r["at_active_bound"].strip().lower() == "true",
            "status": r["status"],
        }
    aux["params41"] = params
    aux["params41_order"] = order
    aux["_sources"]["params41"] = str(p.relative_to(MNL)).replace("\\", "/")

    # -- the external hours validation cells ---------------------------------- #
    p = TABDIR / "external_hours_validation_v1.csv"
    rows = read_csv_rows(p)
    cells = {}
    for r in rows:
        k = "%s|%s" % (r.get("sex", ""), r.get("band", ""))
        cells[k] = {kk: _num(vv) if kk not in ("sex", "band") else vv
                    for kk, vv in r.items()}
    aux["hours_cells"] = cells
    aux["hours_cols"] = list(rows[0].keys()) if rows else []
    aux["_sources"]["hours_cells"] = str(p.relative_to(MNL)).replace("\\", "/")

    # -- the specification chronology ---------------------------------------- #
    # Transcribed from experiments/JMP_PS1/decision_note.md section 2 (the S1-S7
    # per-spec verdict table) and section 31 (the S9 selection criteria table).
    # These are the likelihood/criterion movements the chronology section reads.
    aux["chron"] = {
        "peak_negll_gain": 430.710,
        "peak_lr": 861.421,
        "peak_daic": -859.421,
        "peak_dbic_households": -854.072,
        "f35_share_without_peak": 0.0546,
        "f35_share_with_peak": 0.2520,
        "f35_share_observed": 0.2485,
        "hours_grid_mae_with_peak": 0.0083,
        "hours_grid_mae_without_peak": 0.0339,
        "male_child_z": 0.88,
        "male_child_se": 1.8671,
        "wage_edu_interaction_z": -1.50,
        "hp_expected_lr_at_half": 0.0081,
        "hp_expected_lr_at_one": 0.1351,
        "hp_observable_expected_lr": 0.597,
        "boundary_lr_threshold": 2.706,
        "ho_axis_lr_low": 1.0246,
        "ho_axis_lr_high": 13.5623,
        "ho_profile_lr_low": 0.0492,
        "ho_profile_lr_high": 0.6996,
        "bc_leisure_within_set_sd_men": 0.073,
        "bc_leisure_within_set_sd_women": 0.127,
        "negll_benchmark_no_peak": 18453.4750133318,
        "cond_number_preferred": 1.18e5,
        "cond_number_benchmark": 5.37e5,
        "logscore_preferred": -11.651709,
        "logscore_benchmark": -11.915976,
        "occ_share_mae_preferred": 0.00338,
        "occ_share_mae_benchmark": 0.00343,
        "employment_share_observed": 0.8708,
        "employment_share_predicted": 0.8668,
        "cr1_finite_sample_constant": 1.0257256,
        "wage_q1_over_prediction_pp": 5.3,
    }
    # -- sample construction and descriptives --------------------------------- #
    # The reader's-guide notebook exports every table it prints as a frozen CSV;
    # these are read rather than transcribed.
    RG = MNL / "outputs/p2a_singles2016/notebook_dev_v3"

    def _rg(name):
        return read_csv_rows(RG / name)

    sample = {}
    flow = _rg("results_discussion_table1_1_sample_flow.csv")
    sample["flow"] = [
        {"step": r["step"], "households": _num(r["households"]),
         "dropped": _num(r["dropped"]),
         "share_of_file": _num(r["share of file total"])}
        for r in flow]
    screen = _rg("results_discussion_table1_1a_composition_screen.csv")
    sample["composition_screen"] = [
        {"reason": r["what it means"] or r["class (name in the code)"],
         "households": _num(r["households"])} for r in screen]
    cw = _rg("results_discussion_table11_1_couples_waterfall.csv")
    sample["couples_flow"] = [
        {"step": r["step"], "all": _num(r["households (all)"]),
         "singles": _num(r["single-adult"]), "couples": _num(r["couples (m/f)"]),
         "couples_dropped": _num(r["couples dropped"]),
         "screen": r["what the screen is"]} for r in cw]
    comp = _rg("descriptives_categorical_v1.csv")
    sample["categorical"] = [
        {"dimension": r["dimension"], "category": r["category"],
         "n": _num(r["households_unweighted"]),
         "share_unweighted": _num(r["share_unweighted"]),
         "share_weighted": _num(r["share_weighted"])} for r in comp]
    cont = _rg("descriptives_continuous_v1.csv")
    sample["continuous"] = [
        {"dimension": r["dimension"], "unit": r["unit"],
         "n": _num(r["n_households_unweighted"]),
         "mean_weighted": _num(r["mean_weighted"]),
         "median_weighted": _num(r["median_weighted"]),
         "p10_weighted": _num(r["p10_weighted"]),
         "p90_weighted": _num(r["p90_weighted"]),
         "min": _num(r["min"]), "max": _num(r["max"])} for r in cont]
    ineq = {r["index"]: _num(r["observed disposable income"])
            for r in _rg("results_discussion_table3_1_observed_inequality.csv")}
    sample["observed"] = ineq
    sample["region_key"] = [
        {"code": _num(r["code"]), "name": r["region name (NUTS-1)"],
         "parts": r["constituent NUTS-2 regions"]}
        for r in _rg("results_discussion_table1_3_region_key.csv")]

    # children and urbanisation are not in the exported descriptive tables, so
    # they are computed here from the certified singles frame, household level.
    import pandas as _pd2
    _fr = (MNL / "outputs/p2a_singles2016/region_live_margqh_floor5_v1"
           / "fr_p2a_singles2016_regionlive_margqh_floor5_v1__singles.parquet")
    _cols = ["idorighh", "dwt", "n_children", "drgur", "drgmd"]
    _hh = _pd2.read_parquet(_fr, columns=_cols).drop_duplicates(subset=["idorighh"])
    _w = _hh["dwt"]
    sample["children"] = []
    for k in sorted(_hh["n_children"].unique()):
        m = _hh["n_children"] == k
        sample["children"].append(
            {"n_children": int(k), "households": int(m.sum()),
             "share_unweighted": float(m.mean()),
             "share_weighted": float(_w[m].sum() / _w.sum())})
    _urb = [("urban", _hh["drgur"] == 1),
            ("intermediate", _hh["drgmd"] == 1),
            ("rural", (_hh["drgur"] != 1) & (_hh["drgmd"] != 1))]
    sample["urbanisation"] = [
        {"zone": name, "households": int(m.sum()),
         "share_unweighted": float(m.mean()),
         "share_weighted": float(_w[m].sum() / _w.sum())}
        for name, m in _urb]

    aux["sample"] = sample
    # -- derived readings: e^beta ratios, for the plain-language column ------- #
    import math as _m
    ratios = {}
    for k, r in aux["params41"].items():
        e = r.get("estimate")
        if isinstance(e, (int, float)):
            ratios[k] = {"exp": _m.exp(e), "pct": (_m.exp(e) - 1.0) * 100.0}
    aux["ratio"] = ratios
    aux["_sources"]["ratio"] = ("exp(estimate) and 100*(exp(estimate)-1) of every "
                                "coordinate in the params41 block; arithmetic on "
                                "the reported coefficients, no new estimation")

    aux["_sources"]["sample"] = (
        "outputs/p2a_singles2016/notebook_dev_v3/ - the reader's-guide "
        "notebook's frozen exports: results_discussion_table1_1_sample_flow.csv, "
        "table1_1a_composition_screen.csv, table11_1_couples_waterfall.csv, "
        "table3_1_observed_inequality.csv, table1_3_region_key.csv, "
        "descriptives_categorical_v1.csv and "
        "descriptives_continuous_v1.csv. Children and urbanisation are "
        "computed household-level from the certified singles frame in "
        "outputs/p2a_singles2016/region_live_margqh_floor5_v1/.")

    # -- male exposure to a child-count term ---------------------------------- #
    # Computed on the certified singles frame: how many single men the male
    # child-count shifter would apply to at all.
    frame = (MNL / "outputs/p2a_singles2016/region_live_margqh_floor5_v1"
             / "fr_p2a_singles2016_regionlive_margqh_floor5_v1__singles.parquet")
    import pandas as _pd
    hh = _pd.read_parquet(frame, columns=["idorighh", "dgn", "dwt", "n_children"])
    hh = hh.drop_duplicates(subset=["idorighh"])
    men = hh[hh["dgn"] == 1]
    men_k = men["n_children"] > 0
    aux["child"] = {
        "male_units": int(len(men)),
        "male_with_children": int(men_k.sum()),
        "male_with_children_share_of_men": float(men_k.mean()),
        "male_with_children_share_of_sample": float(men_k.sum() / len(hh)),
        "male_with_children_share_of_men_weighted":
            float(men["dwt"][men_k].sum() / men["dwt"].sum()),
        "male_with_children_share_of_sample_weighted":
            float(men["dwt"][men_k].sum() / hh["dwt"].sum()),
    }
    aux["_sources"]["child"] = (
        "outputs/p2a_singles2016/region_live_margqh_floor5_v1/"
        "fr_p2a_singles2016_regionlive_margqh_floor5_v1__singles.parquet; "
        "household-level, dgn==1, n_children>0; dwt-weighted shares alongside")

    # -- the age-bound diagnostic --------------------------------------------- #
    # Read from the artefact, except the two lambda_ell = 40 re-expression values,
    # which are the exact-map figures transcribed from the decision note.
    ab = json.loads((SPRINT / "runs/agebound_addendum_s2/ab_verdict_v1.json")
                    .read_text(encoding="utf-8"))
    B = ab["B_materially_better_objective"]
    fm = B["_freed_coefficients"]["beta_l_age2_sm"]
    ff = B["_freed_coefficients"]["beta_l_age2_sf"]
    aux["agebound"] = {
        "delta_negll": B["_objective_gain"],
        "twice_the_gain": B["_twice_the_gain"],
        "delta_aic": B["_dAIC"],
        "released_m": fm["estimate"],
        "released_f": ff["estimate"],
        "ci_m": [fm["ci95_lo"], fm["ci95_hi"]],
        "ci_f": [ff["ci95_lo"], ff["ci95_hi"]],
        "bound_of_record": fm["S8_value"],
        "active_set_widened": len(ab["A_well_behaved"]["_active_set_AGEWIDE"]),
        "verdict": ab["verdict"],
        "failing_limb": ab["failing_limb"],
        "lambda40_m": 0.034845,
        "lambda40_f": 0.055555,
    }
    aux["_sources"]["agebound"] = (
        "experiments/JMP_SEMINAR_SPRINT/runs/agebound_addendum_s2/"
        "ab_verdict_v1.json; the two lambda_ell = 40 re-expression values from "
        "experiments/JMP_PS1/decision_note.md section 1 (exact map, no "
        "re-estimation)")

    aux["_sources"]["chron"] = ("experiments/JMP_PS1/decision_note.md "
                                "sections 2 and 31 (per-spec verdict table; "
                                "S9 selection criteria table)")

    # -- structural definitions ----------------------------------------------- #
    aux["defs"] = {
        "R_reference": 100,
        "f35_lo": 33.5, "f35_hi": 36.5,
        "pt1_lo": 17.5, "pt1_hi": 21.5,
        "pt2_lo": 28.5, "pt2_hi": 30.5,
        "ft_lo": 36.5, "ft_hi": 40.5,
        "lh_lo": 44.5, "lh_hi": 70.0,
        "hours_floor": 5.0,
        "age_lo": 20, "age_hi": 60,
        "n_occupation_groups": 4,
        "n_nuts1_regions": 8,
        "n_hours_bands_priced": 5,
        "jackknife_t": 2.364624251,
        "n_scrambles": 8,
    }
    aux["_sources"]["defs"] = ("structural constants of the estimated "
                              "specification; bundle spec YAML at "
                              "experiments/JMP_SEMINAR_SPRINT/export/"
                              "gpu_research_bundle_v1/spec/ and "
                              "tables/external_hours_validation_v1.md")
    return aux


# --------------------------------------------------------------------------- #
# figures
# --------------------------------------------------------------------------- #
def encode_figure(stem: str) -> tuple[str, int]:
    """Downscale and base64-encode one PNG from the sprint figure set."""
    from PIL import Image

    src = FIGDIR / (stem + ".png")
    if not src.is_file():
        # figures reused from the reader's-guide notebook are staged in the
        # report's own store so the build is reproducible from a clone
        src = LOCAL_FIGDIR / (stem + ".png")
    im = Image.open(src)
    if im.mode not in ("RGB", "RGBA"):
        im = im.convert("RGBA")
    if im.width > MAX_FIG_WIDTH:
        h = int(round(im.height * MAX_FIG_WIDTH / im.width))
        im = im.resize((MAX_FIG_WIDTH, h), Image.LANCZOS)
    if im.mode == "RGBA":
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    buf = io.BytesIO()
    im.save(buf, format="PNG", optimize=True)
    raw = buf.getvalue()
    return base64.b64encode(raw).decode("ascii"), len(raw)


class FigureBank:
    def __init__(self):
        self.used: dict[str, str] = {}
        self.bytes = 0

    def fig(self, stem: str, caption: str, credit: str = "") -> str:
        if stem not in self.used:
            b64, nb = encode_figure(stem)
            self.used[stem] = b64
            self.bytes += nb
        cr = ('<div class="credit">%s</div>' % esc(credit)) if credit else ""
        return (
            '<figure class="fig">'
            '<img alt="%s" src="data:image/png;base64,%s">'
            '<figcaption><span class="figname">%s</span> %s%s</figcaption>'
            "</figure>"
        ) % (esc(caption), self.used[stem], esc(stem), caption, cr)


# --------------------------------------------------------------------------- #
# small prose helpers
# --------------------------------------------------------------------------- #
def box(kind: str, title: str, body: str) -> str:
    return ('<div class="box %s"><div class="box-t">%s</div>%s</div>'
            % (kind, esc(title), body))


def qa(idx: int, question: str, short: str, technical: str, pointer: str) -> str:
    return (
        '<div class="qa" id="qa%d">'
        '<div class="qa-q"><span class="qa-i exempt">Q%d</span>%s</div>'
        '<div class="qa-s"><span class="lab exempt">15 seconds</span>%s</div>'
        '<div class="qa-t"><span class="lab">Technical</span>%s</div>'
        '<div class="qa-p"><span class="lab">Where to point</span>%s</div>'
        "</div>"
    ) % (idx, idx, question, short, technical, pointer)
