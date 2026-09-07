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
