#!/usr/bin/env python
"""Build the self-contained current-results gallery.

Run with --refresh-registry after a reviewed source update.  That mode copies
the non-S12 cells used by the gallery into numbers_of_record_v5.json.  A normal
build reads displayed non-S12 numbers only from that registry; S12 tables are
read from their CSV records, as allowed by the gallery's source contract.
"""
from __future__ import annotations

import argparse
import base64
import csv
import html
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "reports"
MNL = ROOT.parent / "MNL"
SPRINT = MNL / "experiments/JMP_SEMINAR_SPRINT"
RUNS = SPRINT / "runs"
FIG = SPRINT / "figures"
V5 = RUNS / "v5_evidence"
S11 = RUNS / "s11_welfare_specs_of_record"
S12 = RUNS / "s12_welfare_record"
PREF = FIG / "preferences_final"
# Preliminary three-factor P/A/B decomposition (supersedes the retired
# four-factor P/A/B/D decomposition previously read from the S12 tables
# above). Source: MNL_decomp, branch welfare/preseminar-pab. Deliberately
# NOT sourced from headline_decomposition_v1.csv or any ss8*/cw_step3*/
# gn_step2* state file -- those remain excluded pending a separate lineage
# verdict.
DECOMP2 = ROOT.parent / "MNL_decomp" / "outputs/welfare/preseminar_pab_v1"
NOR_PATH = REPORTS / "numbers_of_record_v5.json"
OUT = REPORTS / "JMP_results_gallery_current.html"


def rows(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def num(x):
    if x in (None, "", "nan", "NA"):
        return None
    return float(x)


def refresh_registry(nor):
    """Register the exact non-S12 cells displayed by this document."""
    full_funnel = rows(RUNS / "final_descriptives/fd_funnel_v1.csv")
    funnel = []
    for r in full_funnel:
        if r["screen"].startswith("FINAL:"):
            continue
        funnel.append({
            "screen": r["screen"],
            "households_singles": r["households_singles"],
            "households_couples": r["households_couples"],
            "dropped_singles": r["dropped_singles"],
            "dropped_couples": r["dropped_couples"],
            "reason_detail": r["operational_criterion"],
        })
    for r in rows(V5 / "v5_funnel_tail_v1.csv"):
        rr = dict(r)
        rr["reason_detail"] = r["operational_criterion"]
        funnel.append(rr)
    cont = rows(V5 / "v5_descriptives_continuous_v1.csv")
    cat = rows(V5 / "v5_descriptives_categorical_v1.csv")
    occ = rows(V5 / "v5_occupation_v1.csv")
    coef = {}
    for sample in ("singles", "couples"):
        rs = rows(S11 / f"s11_{sample}_parameter_table_v1.csv")
        # A reporting table is an inference object, not the optimizer's storage
        # vector.  Pinned/structurally absent coordinates have no sampling SE
        # and are disclosed once in the maintained-restrictions note instead.
        coef[sample] = [{
            "parameter": r["param"], "estimate": num(r["estimate"]),
            "cr1_se": num(r["se_robust_CR1"]), "lower": num(r["lower_bound"]),
            "upper": num(r["upper_bound"]),
            "pinned": r["pinned"].lower() == "true",
            "active_bound": r["active_bound"].lower() == "true",
        } for r in rs if r["pinned"].lower() != "true"]

    fit = [{
        "sample": r["sample"], "sex": r["sex"], "margin": r["moment"],
        "observed": num(r["observed"]), "model": num(r["predicted"]),
        "deviation": num(r["predicted"]) - num(r["observed"]),
        "denominator": r["denominator"],
    } for r in rows(S11 / "s11_criterion_b_population_moments_v1.csv")
          if r["sample"] in ("singles", "couples")]

    def wage_quantile_fit():
        """Re-use the certified population-integration code, adding quantiles.

        The maintained fit export stops at mean log wage.  This evaluates the
        same direct criterion-B probabilities at the stored S11 optimum and
        summarizes their worker-conditional wage distribution.  No estimation,
        pricing, or new simulation is performed.
        """
        import numpy as np
        import pandas as pd
        p10 = RUNS / "s10_criterion_a_iid_r100"
        pscale = RUNS / "s10_scale_identification"
        sys.path[:0] = [str(p10), str(pscale), str(MNL / "scripts/welfare")]
        import run_s10_population_fit_v1 as PF
        import run_s10_scale_identification_v1 as SCALE
        import s10_estimation_lib_v1 as L
        from dclaborsupply.data.loader import load_couples, load_singles
        from dclaborsupply.likelihood.engine_jax import build_jax_couples_ll, build_jax_singles_ll

        def wq(x, w, q):
            x, w = np.asarray(x, float), np.asarray(w, float)
            keep = np.isfinite(x) & np.isfinite(w) & (w > 0)
            x, w = x[keep], w[keep]
            o = np.argsort(x); x, w = x[o], w[o]
            return float(x[np.searchsorted(np.cumsum(w), q*w.sum(), side="left")])

        metadata = json.loads(L.META_PATH.read_text(encoding="utf-8"))
        out = []
        sf = pd.read_parquet(L.SINGLES_FRAME).sort_values(["source_idhh","draw"]).reset_index(drop=True)
        sa = PF.singles_atom_frame(sf)
        _, sspec, *_ = SCALE.build_target("singles", metadata)
        st = np.load(S11 / "s11_singles_theta_hat_v1.npy")
        sspec, st = SCALE.expand_shared_singles_beta(sspec, st)
        sspec.market_opportunity_center_within_choice_set = False
        for male, sex in ((True,"male"),(False,"female")):
            f=sf[sf.dgn.eq(1 if male else 0)].reset_index(drop=True)
            a=sa[sa.dgn.eq(1 if male else 0)].reset_index(drop=True)
            dat=load_singles(f,sspec,is_male=male,metadata=metadata)
            ada=load_singles(a,sspec,is_male=male,metadata=metadata)
            ix,_=build_jax_singles_ll(dat,sspec,is_male=male,return_index=True)
            ai,_=build_jax_singles_ll(ada,sspec,is_male=male,return_index=True)
            pr,_=PF._direct_probabilities(f,np.asarray(ix(st)),a,np.asarray(ai(st)),"draw",f.working.eq(0).to_numpy())
            ng=len(a); hw=f.groupby("source_idhh",sort=False).dwt.first().to_numpy(float)
            wa=np.column_stack([np.zeros(ng),f.wage.to_numpy().reshape(ng,PF.R+1)[:,1:]])
            wk=np.column_stack([np.zeros(ng),f.working.to_numpy().reshape(ng,PF.R+1)[:,1:]])
            ch=f[f.is_chosen.eq(1)].sort_values("source_idhh")
            ow=ch.working.to_numpy(float)
            for q in (.1,.25,.5,.75,.9):
                out.append({"sample":"singles","sex":sex,"quantile":q,
                            "observed":wq(ch.wage,hw*ow,q),
                            "model":wq(wa.ravel(),(pr*wk*hw[:,None]).ravel(),q)})

        cf = pd.read_parquet(L.COUPLES_FRAME).sort_values(["source_idhh","draw_joint"]).reset_index(drop=True)
        ca,_ = PF.couples_atom_frame(cf,metadata)
        _,cspec,*_ = SCALE.build_target("couples",metadata)
        cspec.bounds=dict(cspec.bounds); cspec.bounds["beta_w_pexp"]=(-3.0,3.0); cspec.bounds["beta_w_pexp2"]=(-.3,.3)
        ct=np.load(S11 / "s11_couples_theta_hat_v1.npy")
        cspec.market_opportunity_center_within_choice_set=False
        dat=load_couples(cf,cspec,metadata=metadata); ada=load_couples(ca,cspec,metadata=metadata)
        gs=list(getattr(cspec,"gender_split",[]) or [])
        ix,_=build_jax_couples_ll(dat,cspec,gender_split=gs,return_index=True)
        ai,_=build_jax_couples_ll(ada,cspec,gender_split=gs,return_index=True)
        disc=(cf.working_male.eq(0)&cf.working_female.eq(0)).to_numpy()
        pr,_=PF._direct_probabilities(cf,np.asarray(ix(ct)),ca,np.asarray(ai(ct)),"draw_joint",disc)
        ng=len(ca); hw=cf.groupby("source_idhh",sort=False).dwt.first().to_numpy(float)
        ch=cf[cf.is_chosen.eq(1)].sort_values("source_idhh")
        for sex in ("male","female"):
            wa=np.column_stack([np.zeros(ng),cf[f"wage_{sex}"].to_numpy().reshape(ng,PF.R+1)[:,1:]])
            wk=np.column_stack([np.zeros(ng),cf[f"working_{sex}"].to_numpy().reshape(ng,PF.R+1)[:,1:]])
            ow=ch[f"working_{sex}"].to_numpy(float)
            for q in (.1,.25,.5,.75,.9):
                out.append({"sample":"couples","sex":sex,"quantile":q,
                            "observed":wq(ch[f"wage_{sex}"],hw*ow,q),
                            "model":wq(wa.ravel(),(pr*wk*hw[:,None]).ravel(),q)})
        for r in out: r["deviation"] = r["model"] - r["observed"]
        return out

    wage_quantiles = wage_quantile_fit()

    # Selected weighted summaries: the complete distributions remain visible in
    # figV08/09, while this table keeps the side-by-side reading economical.
    wanted_cont = {
        ("single-adult", "the decider", "age"),
        ("couple", "the man", "age"), ("couple", "the woman", "age"),
        ("single-adult", "the employed decider", "weekly hours (continuous)"),
        ("couple", "the employed man", "weekly hours (continuous)"),
        ("couple", "the employed woman", "weekly hours (continuous)"),
        ("single-adult", "the employed decider", "hourly wage measure (EUR/hour)"),
        ("couple", "the employed man", "hourly wage measure (EUR/hour)"),
        ("couple", "the employed woman", "hourly wage measure (EUR/hour)"),
        ("single-adult", "the household", "disposable income (EUR/month)"),
        ("couple", "the household", "disposable income (EUR/month)"),
        ("single-adult", "the household", "equivalized disposable income (EUR/month)"),
        ("couple", "the household", "equivalized disposable income (EUR/month)"),
    }
    descriptives = [{
        "population": r["household_type"], "unit": r["unit"],
        "measure": r["variable"], "n": int(r["n_unweighted"]),
        "weighted_mean": num(r["mean_weighted"]),
        "weighted_median": num(r["median_weighted"]),
        "weighted_p10": num(r["p10_weighted"]),
        "weighted_p90": num(r["p90_weighted"]),
    } for r in cont if (r["household_type"], r["unit"], r["variable"]) in wanted_cont]

    observed = [{
        "population": r["household_type"], "unit": r["unit"],
        "dimension": r["dimension"], "category": r["category"],
        "count": int(r["households_unweighted"]),
        "weighted_share": num(r["share_weighted"]),
    } for r in cat if r["dimension"] in (
        "employment", "joint participation regime",
        "structural hours band (opportunity support)")]
    occupation = [{
        "population": r.get("household_type", ""), "unit": r.get("unit", ""),
        "system": r.get("classification", ""),
        "category": r.get("label", ""),
        "count": int(float(r.get("workers_unweighted", 0))),
        "weighted_share": num(r.get("share_weighted")),
    } for r in occ]

    worked = json.loads((V5 / "v5_step4_worked_examples_v1.json").read_text(encoding="utf-8"))["examples"]
    examples = {}
    for sample, e in worked.items():
        examples[sample] = {
            "selection": e["selection"], "profile": e["profile"],
            "observed_consumption": e["observed_disposable_income_eur_per_month"],
            "weighted_rank": e["weighted_rank_in_the_distribution"],
            "states": e["states"],
        }

    # Anonymous component-density examples.  They use S11 parameters and the
    # weighted-median profiles.  Access is shown as the employment/joint-regime
    # margin; hours and occupation are normalized structural intensities; wage
    # curves are the corresponding occupation-conditional lognormal densities.
    def pm(sample):
        return {r["parameter"]: r["estimate"] for r in coef[sample]}

    bands = [("short part-time", "pt1", 4.0), ("long part-time", "pt2", 2.0),
             ("around thirty-five", "f35", 3.0), ("full-time", "ft", 4.0),
             ("long hours", "lh", 25.5), ("residual support", None, 26.5)]

    def hour_shares(p, suffix=""):
        z = []
        for label, key, width in bands:
            b = 0.0 if key is None else p[f"beta_h_{key}{suffix}"]
            z.append((label, width * math.exp(b)))
        den = sum(v for _, v in z)
        return [{"label": k, "share": v / den} for k, v in z]

    def occ_shares(p, sex):
        v = [1.0] + [math.exp(p[f"beta_occ_{k}_{sex}"]) for k in (2, 3, 4)]
        return [x / sum(v) for x in v]

    def density_curve(mu, sigma):
        out = []
        for wage in range(2, 81, 2):
            z = (math.log(wage) - mu) / sigma
            d = math.exp(-0.5*z*z) / (wage * sigma * math.sqrt(2*math.pi))
            out.append({"wage": wage, "density": d})
        return out

    ps, pc = pm("singles"), pm("couples")
    sp = worked["singles"]["profile"]
    ssex = "m" if sp["sex of the decider"] == "man" else "f"
    # The access panel is a profile illustration.  The exact current fitted
    # population employment margin is used; it is the registered model-implied
    # probability for this sex and avoids pretending node weights are published.
    sf = next(r for r in fit if r["sample"] == "singles" and r["sex"] == ("male" if ssex == "m" else "female") and r["margin"] == "employment")
    educ = sp["education"]
    age_mid = sum(map(int, sp["age band"].split("-"))) / 2
    pexp = max(age_mid - (16 if educ == "low" else 19 if educ == "medium" else 22), 0) / 20
    mu_s = ps["beta_w0"] + ps["beta_w_educL"]*(educ == "low") + ps["beta_w_educH"]*(educ == "high") + ps["beta_w_pexp"]*pexp + ps["beta_w_pexp2"]*pexp*pexp
    os = occ_shares(ps, ssex)
    opportunity = {"singles": {
        "access": [{"label": "not employed", "share": 1-sf["model"]}, {"label": "employed", "share": sf["model"]}],
        "hours": hour_shares(ps),
        "occupation": [{"label": f"group {k}", "share": os[k-1]} for k in range(1,5)],
        "wages": [{"occupation": f"group {k}", "curve": density_curve(mu_s + (0 if k == 1 else ps[f"delta_occ_{k}"]), ps["sigma"])} for k in range(1,5)],
    }}
    regimes = [r for r in fit if r["sample"] == "couples" and r["sex"] == "household"]
    cp = worked["couples"]["profile"]
    wage_curves = []
    for sex, tag in (("man", "m"), ("woman", "f")):
        educ = cp[f"education, {sex}"]
        amid = sum(map(int, cp[f"age band, {sex}"].split("-"))) / 2
        px = max(amid - (16 if educ == "low" else 19 if educ == "medium" else 22), 0) / 20
        mu = pc["beta_w0"] + pc["beta_w_educL"]*(educ == "low") + pc["beta_w_educH"]*(educ == "high") + pc["beta_w_pexp"]*px + pc["beta_w_pexp2"]*px*px
        wage_curves.append({"occupation": sex, "curve": density_curve(mu, pc["sigma"])})
    opportunity["couples"] = {
        "access": [{"label": r["margin"].split("::")[1], "share": r["model"]} for r in regimes],
        "hours": [{"label": f"{x['label']} · {sex}", "share": x["share"]}
                  for sex, suff in (("man", "_m"), ("woman", "_f")) for x in hour_shares(pc, suff)],
        "occupation": [{"label": f"group {k} · {sex}", "share": sh}
                       for sex, tag in (("man", "m"), ("woman", "f"))
                       for k, sh in enumerate(occ_shares(pc, tag), 1)],
        "wages": wage_curves,
    }

    w4 = json.loads((S12 / "s12_w4_premise_audit_v1.json").read_text(encoding="utf-8"))
    w4_corrected = {sample: {
        "ratio": w4[sample]["unit_mass_corrected_bridge"]["W4_over_W1"],
        "gap_nats": w4[sample]["unit_mass_corrected_bridge"]["Delta_nats"],
        "w4_eur": w4[sample]["unit_mass_corrected_bridge"]["W4_EA_eur"],
    } for sample in ("singles", "couples")}
    nor["gallery"] = {
        "registered_for": "current results gallery",
        "sample_funnel": funnel, "descriptives": descriptives,
        "observed_margins": observed, "occupation": occupation,
        "coefficients": coef, "fit": fit, "examples": examples,
        "wage_quantile_fit": wage_quantiles,
        "w4_corrected": w4_corrected,
        "opportunity_examples": opportunity,
    }
    # Preserve the registry's Windows line-ending convention.
    with NOR_PATH.open("w", encoding="utf-8", newline=None) as f:
        f.write(json.dumps(nor, indent=2, ensure_ascii=False) + "\n")


def fmt(v, kind="num"):
    if v is None:
        return "—"
    if kind == "pct":
        return f"{100*float(v):.1f}%"
    if kind == "eur":
        return f"€{float(v):,.0f}"
    if kind == "int":
        return f"{int(float(v)):,}"
    x = float(v)
    return f"{x:.4f}" if abs(x) < 10 else f"{x:,.2f}"


def img_data(path: Path):
    return "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode("ascii")


def figure(path: Path, title: str, caption: str, cls=""):
    return (f'<figure class="{cls}"><img src="{img_data(path)}" alt="{html.escape(title)}">'
            f'<figcaption><strong>{html.escape(title)}.</strong> {caption}</figcaption></figure>')


def cap(pop, units, measure, reference, status):
    return (f"<span class=capkey>Population</span> {pop}. "
            f"<span class=capkey>Units</span> {units}. "
            f"<span class=capkey>Measure</span> {measure}. "
            f"<span class=capkey>Reference</span> {reference}. "
            f"<span class=capkey>Status</span> {status}.")


def table(headers, body, classes=""):
    h = "".join(f"<th>{x}</th>" for x in headers)
    rs = "".join("<tr>" + "".join(f"<td>{x}</td>" for x in r) + "</tr>" for r in body)
    return f'<div class="tablewrap"><table class="{classes}"><thead><tr>{h}</tr></thead><tbody>{rs}</tbody></table></div>'


def bar_svg(data, title, percent=True, max_items=12):
    data = data[:max_items]
    w, left, top, rowh = 620, 178, 34, 28
    h = top + rowh*len(data) + 22
    maxv = max((float(d["share"]) for d in data), default=1) or 1
    out = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{html.escape(title)}">',
           f'<text x="0" y="17" class="svgt">{html.escape(title)}</text>']
    for i, d in enumerate(data):
        y = top + i*rowh
        bw = 375*float(d["share"])/maxv
        val = fmt(d["share"], "pct") if percent else fmt(d["share"])
        out += [f'<text x="0" y="{y+14}" class="svgl">{html.escape(str(d["label"]))}</text>',
                f'<rect x="{left}" y="{y}" width="{bw:.2f}" height="17" rx="3" class="bar"/>',
                f'<text x="{left+bw+7:.2f}" y="{y+14}" class="svgv">{val}</text>']
    return "".join(out) + "</svg>"


def wage_svg(series, title):
    w, h, l, t, pw, ph = 620, 235, 48, 30, 540, 165
    ymax = max(d["density"] for s in series for d in s["curve"])
    colors = ["#1d6f78", "#d2793f", "#775da6", "#718247"]
    out = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{html.escape(title)}">',
           f'<text x="0" y="17" class="svgt">{html.escape(title)}</text>',
           f'<line x1="{l}" y1="{t+ph}" x2="{l+pw}" y2="{t+ph}" class="axis"/>']
    for k, s in enumerate(series):
        pts = []
        for d in s["curve"]:
            x = l + pw*(d["wage"]-2)/78
            y = t + ph*(1-d["density"]/ymax)
            pts.append(f"{x:.1f},{y:.1f}")
        out.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{colors[k%4]}" stroke-width="2.3"/>')
        out.append(f'<text x="{l+110*k}" y="{h-8}" fill="{colors[k%4]}" class="svgv">{html.escape(s["occupation"])}</text>')
    out += [f'<text x="{l}" y="{t+ph+17}" class="svgv">€2</text>',
            f'<text x="{l+pw-25}" y="{t+ph+17}" class="svgv">€80</text>']
    return "".join(out) + "</svg>"


def block_of(name):
    if name == "beta_c" or name.startswith("theta_c"):
        return "consumption"
    if name.startswith(("beta_l", "theta_l")):
        return "preferences"
    if name.startswith("beta_E"):
        return "access"
    if name.startswith("beta_h"):
        return "hours"
    if name.startswith("beta_occ"):
        return "occupation"
    return "wages"


def build(nor):
    if "gallery" not in nor:
        raise SystemExit("gallery registry missing; run build.py --refresh-registry")
    g, n = nor["gallery"], {k: v["value"] for k, v in nor["entries"].items()}
    s12_sum = rows(S12 / "s12_principal_welfare_summary_v1.csv")

    # --- Preliminary three-factor P/A/B decomposition (DECOMP-2) ---------
    d2_coal = {smp: rows(DECOMP2 / f"coalition_values_{smp}.csv") for smp in ("singles", "couples")}
    d2_shap = {smp: rows(DECOMP2 / f"shapley_PAB_{smp}.csv") for smp in ("singles", "couples")}
    d2_var = rows(DECOMP2 / "log_variance_split_v1.csv")
    d2_anchor = json.loads((DECOMP2 / "anchor_excluded_arm_v1.json").read_text(encoding="utf-8"))

    D2_COALITION_LABEL = {"EMPTY": "∅ (actual)", "P": "P", "A": "A", "B": "B",
                           "PA": "P + A", "PB": "P + B", "AB": "A + B", "PAB": "P + A + B"}
    D2_FACTOR_FULL = {
        "P": "systematic utility heterogeneity",
        "A": "local labour-market access (region, urban/rural, year)",
        "B": "earning opportunities",
        "Delta_I": "ΔI = I(actual) − I(PAB), the PAB-reducible inequality",
        "RESIDUAL I(PAB)": "residual inequality with P, A and B equalised: household resources/needs/"
                            "composition, sex-block parameter differences, and behavioural randomness",
    }
    D2_FACTOR_CODE = {"P": "P", "A": "A", "B": "B", "Delta_I": "ΔI", "RESIDUAL I(PAB)": "I(PAB)"}

    def signed(x, nd=4):
        x = float(x)
        return f"{'+' if x >= 0 else chr(8722)}{abs(x):.{nd}f}"

    def d2_coalition_table(sample):
        rr = [[r["scale"], D2_COALITION_LABEL.get(r["coalition"], r["coalition"]),
               fmt(num(r["I_S_gini"])), fmt(num(r["change_from_actual"])),
               f"{fmt(num(r['mc_min']))}–{fmt(num(r['mc_max']))}",
               fmt(num(r["mc_sd_across_replications"]))] for r in d2_coal[sample]]
        return table(["Scale", "Coalition", "I(S) Gini", "Change from actual",
                       "MC range (min–max)", "MC sd"], rr, "compact")

    def d2_shapley_table(sample):
        rr = []
        for r in d2_shap[sample]:
            f = r["factor"]
            if f not in ("P", "A", "B", "Delta_I", "RESIDUAL I(PAB)"):
                continue
            lo, hi = num(r["mc_min_share_of_delta_I"]), num(r["mc_max_share_of_delta_I"])
            mc_share = f"{fmt(lo,'pct')}–{fmt(hi,'pct')}" if lo is not None else "—"
            rr.append([r["scale"], D2_FACTOR_CODE.get(f, f), D2_FACTOR_FULL.get(f, r["label"]),
                       fmt(num(r["gini_point_contribution"])),
                       fmt(num(r["share_of_delta_I"]), "pct"), mc_share,
                       fmt(num(r["second_seed_gini_point"]))])
        return table(["Scale", "Factor", "Label", "Gini-point contribution", "Share of ΔI",
                       "MC share range (min–max)", "Second-seed Gini-point"], rr, "compact")

    def d2_variance_table():
        rr = [[r["sample"], D2_COALITION_LABEL.get(r["coalition"], r["coalition"]),
               fmt(num(r["var_log_W1F"])),
               f"{fmt(num(r['var_log_C']))} ({fmt(num(r['share_var_log_C']),'pct')})",
               f"{fmt(num(r['var_log_rho']))} ({fmt(num(r['share_var_log_rho']),'pct')})",
               f"{fmt(num(r['two_cov']))} ({fmt(num(r['share_two_cov']),'pct')})"] for r in d2_var]
        return table(["Population", "Coalition", "Var(log W1_F)", "Var(log C) [share]",
                       "Var(log ρ) [share]", "2·Cov(log C, log ρ) [share]"], rr, "compact")

    def d2_phi_p_note():
        parts = []
        for smp in ("singles", "couples"):
            byscale = {r["scale"]: r for r in d2_shap[smp] if r["factor"] == "P"}
            u = signed(byscale["unequivalised"]["gini_point_contribution"])
            e = signed(byscale["equivalised"]["gini_point_contribution"])
            parts.append(f"{smp}: {u} unequivalised vs {e} equivalised")
        return ("No directional claim is made about P: its sign changes between unequivalised and "
                 "equivalised reporting in both samples (" + "; ".join(parts) + ").")

    def d2_anchor_line():
        moves = [(smp, scale, d2_anchor[smp][scale]["delta_I_relative_move"])
                 for smp in ("singles", "couples") for scale in ("unequivalised", "equivalised")]
        worst = max(moves, key=lambda t: abs(t[2]))
        return (f"Robustness: excluding the anchor arm moves ΔI by at most "
                 f"{signed(worst[2]*100, 1)}% ({worst[0]}, {worst[1]}), with no sign flip in any specification.")

    def d2fig(name, title, caption):
        return figure(DECOMP2 / f"{name}.png", title, caption)

    d2_phi_note = d2_phi_p_note()
    d2_robust_line = d2_anchor_line()

    funnel = table(["Screen", "Singles left", "Couples left", "Removed: singles", "Removed: couples", "Reason detail"], [[
        html.escape(r["screen"]), fmt(r["households_singles"], "int") if r["households_singles"] else "—",
        fmt(r["households_couples"], "int") if r["households_couples"] else "—",
        fmt(r["dropped_singles"], "int") if r["dropped_singles"] else "—",
        fmt(r["dropped_couples"], "int") if r["dropped_couples"] else "—",
        html.escape(r["reason_detail"]),
    ] for r in g["sample_funnel"]])
    desc = table(["Population / unit", "Measure", "N", "Weighted mean", "Weighted median", "P10–P90"], [[
        f"{r['population']} · {r['unit'].replace('the ', '')}", html.escape(r["measure"]), fmt(r["n"], "int"),
        fmt(r["weighted_mean"]), fmt(r["weighted_median"]), f"{fmt(r['weighted_p10'])}–{fmt(r['weighted_p90'])}"
    ] for r in g["descriptives"]])

    obs_rows = [r for r in g["observed_margins"] if r["dimension"] in ("employment", "joint participation regime")]
    obs_table = table(["Population / unit", "Observed category", "Count", "Weighted share"], [[
        f"{r['population']} · {r['unit'].replace('the ', '')}", html.escape(r["category"]), fmt(r["count"], "int"), fmt(r["weighted_share"], "pct")
    ] for r in obs_rows])
    occ_table = table(["Population / unit", "Model occupation group", "Workers", "Weighted share"], [[
        f"{r['population']} · {r['unit'].replace('the ', '')}", html.escape(r["category"]),
        fmt(r["count"], "int"), fmt(r["weighted_share"], "pct")
    ] for r in g["occupation"] if r["system"] == "model four-group aggregation"])

    coef_html = []
    for sample in ("singles", "couples"):
        cr = g["coefficients"][sample]
        rr = []
        for block in ("preferences", "consumption", "access", "hours", "occupation", "wages"):
            for r in [x for x in cr if block_of(x["parameter"]) == block]:
                mark = "● active" if r["active_bound"] else ""
                rr.append([block, f"<code>{html.escape(r['parameter'])}</code>", fmt(r["estimate"]), fmt(r["cr1_se"]), mark])
        coef_html.append(f'<div class="pop"><h3>{sample.title()}</h3>' + table(["Block", "Coefficient", "Estimate", "CR1 SE", "Bound"], rr, "compact") + "</div>")
    restriction_note = ("<p><b>Maintained restrictions.</b> Singles: "
                        "<code>theta_c_singles = 0</code>; the couples preference block "
                        "(<code>beta_l0_m, beta_l_age_m, beta_l_age2_m, beta_l0_f, "
                        "beta_l_age_f, beta_l_age2_f, beta_l_nkids_f, theta_l_f</code>) "
                        "does not enter the singles likelihood; and <code>beta_E_y2015</code> "
                        "and <code>beta_E_y2017</code> are absent because the 2015 and 2017 data "
                        "are not used. Couples: <code>theta_c = 0</code>, the male children leisure "
                        "effect is structurally zero, and the direct cross-leisure term is fixed at zero. "
                        "These are restrictions, not estimates.</p>")

    def fit_group(sample):
        rr = []
        for r in g["fit"]:
            if r["sample"] != sample:
                continue
            label = r["margin"].replace("hours::", "hours · ").replace("occupation::", "occupation · ").replace("quadrant::", "regime · ").replace("mean_log_wage", "mean log wage")
            rr.append([r["sex"], label, fmt(r["observed"]), fmt(r["model"]), fmt(r["deviation"])])
        return table(["Unit", "Margin", "Observed", "Model-implied", "Deviation (model − observed)"], rr, "compact")

    wageq = table(["Population", "Unit", "Quantile", "Observed €/hour", "Model-implied €/hour", "Deviation"], [[
        r["sample"], r["sex"], fmt(r["quantile"], "pct"), fmt(r["observed"]), fmt(r["model"]), fmt(r["deviation"])
    ] for r in g["wage_quantile_fit"]])

    opportunity = []
    for sample in ("singles", "couples"):
        o = g["opportunity_examples"][sample]
        opportunity.append(f'<div class="pop"><h3>{sample.title()}</h3><div class="minigrid">'
            + bar_svg(o["access"], "Access / participation")
            + bar_svg(o["hours"], "Hours density by structural band")
            + bar_svg(o["occupation"], "Occupation density")
            + wage_svg(o["wages"], "Conditional wage-offer density") + "</div></div>")

    # Four principal state levels, directly from S12.
    welfare_rows = []
    for r in s12_sum:
        primary = (r["sample"] == "couples" or r["reference"] == "singles_female")
        if primary and r["state"] in ("I00", "I10", "I01", "I11") and r["basis"] in ("raw", "equivalized"):
            welfare_rows.append([r["sample"], r["basis"], r["state"], fmt(r["mean"], "eur"), fmt(r["median"], "eur"), f"{fmt(r['p10'],'eur')}–{fmt(r['p90'],'eur')}"])
    welfare_table = table(["Population", "Basis", "State", "Mean", "Median", "P10–P90"], welfare_rows)

    w4_rows = []
    for sample in ("singles", "couples"):
        r = g["w4_corrected"][sample]
        w4_rows.append([sample, fmt(r["ratio"]["median"]),
                        f"{fmt(r['ratio']['min'])}–{fmt(r['ratio']['max'])}",
                        fmt(r["gap_nats"]["median"]), fmt(r["w4_eur"]["median"], "eur"),
                        f"{fmt(r['w4_eur']['p10'],'eur')}–{fmt(r['w4_eur']['p90'],'eur')}"])
    w4_table = table(["Population", "Median W4/W1", "Ratio range", "Median gap (nats)", "Median W4", "W4 P10–P90"], w4_rows)

    fig = lambda name, title, caption, pref=False: figure((PREF if pref else FIG) / f"{name}_paper.png", title, caption)
    sections = []
    sections.append(("samples", "Samples and screens", f'''<p class=lead>Two estimation populations, followed through the final support and positive-consumption screens.</p>{funnel}<h3>Weighted descriptives</h3>{desc}
    {fig("figV08_data_panel", "The estimation samples: people and work", cap("single-adult and couple estimation samples", "years, weekly hours, category shares and euros per hour", "weighted observed age, education, hours and delivered wages", "each population is separate; hours bands are structural overlays", "observed"))}
    {fig("figV09_resources_panel", "The estimation samples: household resources", cap("single-adult and couple estimation samples", "euros per month, counts and weighted shares", "disposable income, children, non-labour resources and urbanisation", "raw household values unless equivalized is stated", "observed"))}'''))
    sections.append(("observed", "Observed behaviour", f'''{obs_table}<h3>Occupation of the observed job</h3>{occ_table}
    {fig("figV08_data_panel", "Continuous hours, structural bands, occupation and wages", cap("employed deciders and spouses in both populations", "weekly hours, weighted shares and euros per hour", "continuous observed work outcomes with the model's support bands overlaid", "population-specific, conditional on employment where stated", "observed"))}
    {fig("figV09_resources_panel", "Raw and equivalized disposable consumption", cap("households in both populations", "euros per month", "tax-benefit disposable consumption at the observed choice", "raw household and modified-OECD-equivalized conventions shown separately", "observed"))}
    {fig("figV01_welfare_lorenz", "Observed disposable-consumption Lorenz curves", cap("households in both populations", "cumulative weighted shares", "Lorenz curves for observed disposable consumption, shown beside welfare for orientation", "within-population ordering; raw and equivalized conventions remain distinct", "observed and estimated, explicitly distinguished in the panel"))}'''))
    sections.append(("model", "The estimated model", f'''<p class=lead>Estimates are grouped by their economic role. Standard errors are household-cluster robust; the dot marks a coordinate at an active bound. The consumption coefficient has its own block.</p><div class=twocol>{''.join(coef_html)}</div>{restriction_note}
    <div class=figuregrid>{fig("figP01_indifference_curves_singles", "Single-adult indifference curves", cap("representative single-adult profiles", "monthly euros and weekly leisure", "estimated level sets", "own characteristics at the stated representative profiles", "illustrative from estimated preferences"), True)}
    {fig("figP02_indifference_curves_couples", "Couple indifference curves", cap("representative couple profile", "monthly euros and weekly leisure", "estimated level sets by spouse", "the other spouse's hours held at the panel convention", "illustrative from estimated preferences"), True)}
    {fig("figP03_marginal_utilities", "Marginal utilities", cap("representative profiles from both populations", "utility-index change per leisure or consumption unit", "estimated marginal utility of leisure and consumption", "evaluation points shown in the panel", "illustrative from estimated preferences"), True)}
    {fig("figP04_mrs_by_age_sex", "Marginal rates of substitution", cap("representative and employed profiles in both populations", "euros per month per weekly hour", "local consumption-for-leisure compensation slope", "own characteristics with the figure's evaluation convention", "illustrative from estimated preferences"), True)}
    {fig("figP06_normalization_sensitivity", "Normalization sensitivity", cap("representative profiles in both populations", "relative deviations and re-expressed coefficients", "invariance of preferences to leisure-coordinate normalization", "record normalization compared with alternative coordinates", "illustrative sensitivity"), True)}
    {fig("figP05_euro_value_of_one_nat", "The value of one natural unit", cap("representative consumption levels in both populations", "proportional and euro changes in consumption", "consumption compensation for one natural unit of the utility index", "estimated consumption coefficient, holding the evaluation point fixed", "illustrative from estimated preferences"), True)}
    {fig("figP07_w1_power_mean_weighting", "The power-mean kernel", cap("both estimated population models", "relative consumption and relative kernel weight", "power-mean weighting implied by the estimated consumption coefficient", "median consumption normalized within population", "illustrative algebraic kernel, not a welfare recomputation"), True)}</div>'''))
    sections.append(("fit", "Fit, margin by margin", f'''<p class=lead>Each row keeps its own deviation. The sub-ten-hour zero prediction is a genuine fit error caused by tail coverage of the integration panel. Both the structural density and proposal put positive mass on (5,10): about 4.15% of normalized structural hours mass and 0.00019% conditional proposal mass. The expected draw count is 0.249; the realized panel contains no draw there. The long-hours bin includes 70, and observed singles partitions close separately by sex.</p><div class=twocol><div class=pop><h3>Singles</h3>{fit_group("singles")}</div><div class=pop><h3>Couples</h3>{fit_group("couples")}</div></div><h3>Worker-conditional wage quantiles</h3>{wageq}
    {fig("figV06_fit_by_margin", "Observed against model-implied margins", cap("both estimation populations", "shares and mean log euros per hour", "employment, participation regimes, hours bands, occupation and wage-location margins", "model population integration against weighted observations", "observed and model-implied"))}'''))
    sections.append(("opportunities", "The opportunity distributions", f'''<p class=lead>One anonymous weighted-median profile per population. These panels show the estimated components of the opportunity kernel—not choice probabilities and not personal identifiers.</p><div class=twocol>{''.join(opportunity)}</div>
    <figcaption class=standalone>{cap("one anonymous weighted-median profile from each population", "probability mass, density mass and density per euro", "employment or joint-regime access, structural hours, occupation and conditional wage-offer components", "each component normalized on its own displayed support", "illustrative from the estimated model")}</figcaption>'''))
    sections.append(("welfare", "Welfare", f'''<p>With consumption curvature zero and estimated consumption weights {n['beta_c_singles']:.4f} (singles) and {n['beta_c_couples']:.4f} (couples), W = [sum_r r_ir C_ir^beta_c]^(1/beta_c). This is a power mean, arithmetic only at beta_c = 1. The coefficient is both the mean order and the own-consumption elasticity of the implied weight C^beta_c, holding reference probabilities fixed; doubling consumption multiplies the contribution by {2**n['beta_c_singles']:.2f} or {2**n['beta_c_couples']:.2f}. See The power-mean kernel figure.</p>
    <p>The proposal carries no economic content but enters finite-node welfare through the singles importance correction -log q^W and the couples common-proposal terms in both J and H. Non-positive consumption at simulated nodes receives a one-euro floor before utility evaluation (22,597 singles and 59,821 couples node-evaluations); these alternatives enter J and H alike. See the discussion notebook, Section 7, Construction and the power-mean identity.</p>{welfare_table}
    <div class=figuregrid>{fig("figV02_welfare_distributions", "W1-EA distributions", cap("households in both populations", "equivalent euros per month and density", "estimated own-set equal-consumption welfare distributions", "raw and modified-OECD-equivalized; populations not pooled", "model-implied"))}
    {fig("figV01_welfare_lorenz", "W1-EA Lorenz curves", cap("households in both populations", "cumulative weighted shares", "Lorenz curves and Gini comparisons of W1-EA and observed disposable consumption", "within-population, raw and equivalized conventions shown separately", "observed and model-implied"))}</div>
    <h3>The corrected W4 comparison</h3>{w4_table}<p>The comparison uses the opportunity kernel normalized on exactly the reference domain. The earlier scale-dependent levels are not shown.</p>'''))
    sections.append(("decomposition", "The decomposition", f'''<div class=notice><strong>Preliminary structural decomposition of well-being inequality (P/A/B).</strong> This is a bounded three-factor decomposition of a model-simulated distribution of money-metric well-being, presented ahead of the final decomposition architecture. Monte Carlo ranges quoted anywhere in this section are numerical simulation variation, never confidence intervals.</div>
    <p class=lead>Using the accepted model and the already-priced estimation panel &mdash; no re-estimation, no new pricing &mdash; each household's attained bundle is simulated under eight counterfactual environments, and the dwt-weighted Gini of money-metric well-being W1_F is measured in each. An exact three-factor Shapley allocation splits &Delta;I&nbsp;=&nbsp;I(actual)&nbsp;&minus;&nbsp;I(PAB) across <strong>P&nbsp;=&nbsp;systematic utility heterogeneity</strong>, <strong>A&nbsp;=&nbsp;local labour-market access (region, urban/rural, year)</strong> and <strong>B&nbsp;=&nbsp;earning opportunities</strong>.</p>
    <p>Earning opportunities dominate (58.6%&ndash;124.0% of &Delta;I across samples and scales). Local labour-market access is second and small (4.6%&ndash;29.6%). {d2_phi_note}</p>
    <p><strong>&Delta;I is small (1.8%&ndash;9.9% of measured inequality) by design of the decomposition, not because opportunities are unimportant.</strong> Household resources, needs and composition are held fixed in every coalition, and that fixed component carries the consumption-level variation that dominates the variance of log&nbsp;W1_F &mdash; the variance of log consumption alone is 100%&ndash;127% of it. Sex-specific parameter differences also remain in the residual I(PAB) and are not attributed to P, A or B.</p>
    <p class=small>{d2_robust_line} The estimation panel used for this simulation also carries the household's own observed choice as an anchor node in every coalition, so counterfactual attainment is mechanically anchored toward the observed outcome to a small, roughly common, degree across coalitions (about 2.9% of singles and 3.9% of couples attain it under any coalition); the anchor-exclusion check above tests this directly.</p>
    {d2fig("fig_preseminar_pab_architecture_v1", "The eight P/A/B counterfactual coalitions", cap("both estimation populations", "coalition structure, no units", "how each of the eight P/A/B counterfactual environments is built from the accepted model by equalising household-constant covariates within a block", "node-level alternative characteristics are preserved in every coalition; only household-constant covariates are equalised", "preliminary, model-based"))}
    <p class=small>Reading the MC share range: it is the across-replication spread of a single replication's Shapley share, which divides by that replication's own &Delta;I. When a replication's &Delta;I is near zero the ratio can be extreme in either direction; the column is reported for completeness but is not informative on its own. The Gini-point contribution (the mean over 1,000 replications) and the second-seed check are the informative comparison.</p>
    <h3>Singles &mdash; coalition Gini levels and the exact Shapley allocation</h3>{d2_coalition_table("singles")}{d2_shapley_table("singles")}
    {d2fig("fig_preseminar_pab_decomposition_singles_v1", "Singles: P/A/B decomposition of well-being inequality", cap("single-adult estimation sample", "Gini points of money-metric well-being and shares of ΔI", "coalition Gini levels and the exact Shapley allocation of ΔI across P, A and B, with the sign-instability of P annotated", "modified-OECD-equivalised W1_F; Monte Carlo ranges over 1,000 replications, not confidence intervals", "preliminary, model-based"))}
    <h3>Couples &mdash; coalition Gini levels and the exact Shapley allocation</h3>{d2_coalition_table("couples")}{d2_shapley_table("couples")}
    {d2fig("fig_preseminar_pab_decomposition_couples_v1", "Couples: P/A/B decomposition of well-being inequality", cap("couple estimation sample", "Gini points of money-metric well-being and shares of ΔI", "coalition Gini levels and the exact Shapley allocation of ΔI across P, A and B, with the sign-instability of P annotated", "modified-OECD-equivalised W1_F; Monte Carlo ranges over 1,000 replications, not confidence intervals", "preliminary, model-based"))}
    <h3>Why &Delta;I is small: the variance arithmetic</h3><p class=small>log&nbsp;W1_F splits exactly into a consumption-level term log&nbsp;C, a leisure-valuation term log&nbsp;&rho;, and their covariance. Equalising P, A and B barely moves the dominant consumption term, because none of the three operators can touch a household's tax-benefit position, non-labour income or composition.</p>{d2_variance_table()}'''))
    sections.append(("robustness", "What is robust and what is not", f'''<div class=verdicts><article><h3>Holds in every sample and scale</h3><p>Earning opportunities are the largest of the three factors everywhere (58.6%&ndash;124.0% of &Delta;I); local labour-market access is second and small (4.6%&ndash;29.6%). {d2_robust_line}</p></article>
    <article><h3>Holds across an independent second simulation run</h3><p>Every coalition Gini level and every Shapley share reproduces closely under an independent second simulation seed, and every sign &mdash; including the sign reversal of P between scales &mdash; agrees across both runs.</p></article>
    <article class=warn><h3>Does not hold</h3><p>{d2_phi_note}</p></article>
    <article class=warn><h3>Scope of the preliminary decomposition</h3><p>&Delta;I is small by design, not because opportunities are unimportant: household resources, needs and composition are held fixed in every coalition and are not attributed to P, A or B, and nor are sex-specific parameter differences. The estimation panel used to simulate attainment carries the household's observed choice as an anchor node in every coalition; this is a structural feature of reusing an estimation frame as a welfare panel, tested and found small in its consequences here, but not yet replaced by a purpose-built non-anchored support.</p></article></div>
    '''))

    nav = "".join(f'<a href="#{i}"><span>{k:02d}</span>{html.escape(t)}</a>' for k, (i,t,_) in enumerate(sections,1))
    body = "".join(f'<section id="{i}"><div class=kicker>{k:02d} / results</div><h2>{html.escape(t)}</h2>{c}</section>' for k,(i,t,c) in enumerate(sections,1))
    css = r'''
:root{--ink:#14242a;--muted:#607078;--paper:#f7f5ef;--card:#fff;--line:#d9ddd9;--teal:#1d6f78;--orange:#d2793f;--wash:#e8f0ee;--warn:#fff3df}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font:15px/1.55 Inter,Segoe UI,Arial,sans-serif}.sidebar{position:fixed;inset:0 auto 0 0;width:250px;background:#102c33;color:#fff;padding:28px 18px;overflow:auto}.brand{font:700 20px/1.15 Georgia,serif;margin:0 8px 28px}.brand small{display:block;color:#a9c7c7;font:11px/1.4 Inter,sans-serif;text-transform:uppercase;letter-spacing:.14em;margin-top:8px}.sidebar a{display:flex;gap:12px;color:#d9e6e5;text-decoration:none;padding:9px 8px;border-radius:7px}.sidebar a:hover{background:#1d454c;color:#fff}.sidebar a span{color:#87abae;font-variant-numeric:tabular-nums}main{margin-left:250px}.hero{padding:72px max(6vw,40px) 64px;background:linear-gradient(135deg,#e3eeeb,#f7f5ef)}.hero h1{font:700 clamp(42px,6vw,78px)/.95 Georgia,serif;max-width:900px;margin:12px 0 24px}.eyebrow,.kicker{text-transform:uppercase;letter-spacing:.16em;font-size:11px;font-weight:700;color:var(--teal)}.hero p{font-size:19px;max-width:760px;color:#3d5259}section{padding:64px max(5vw,34px);border-top:1px solid var(--line);max-width:1500px}h2{font:700 42px/1.05 Georgia,serif;margin:10px 0 34px}h3{font:700 21px/1.2 Georgia,serif;margin:30px 0 12px}.lead{font:20px/1.5 Georgia,serif;max-width:900px}.twocol,.figuregrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;align-items:start}.pop{min-width:0}figure{margin:28px 0;background:var(--card);border:1px solid var(--line);border-radius:10px;overflow:hidden}figure img{width:100%;display:block;background:#fff}figcaption{padding:14px 18px;color:#506169;font-size:13px;border-top:1px solid var(--line)}.standalone{display:block;background:#fff;border:1px solid var(--line);border-radius:8px;margin-top:18px}.capkey{font-weight:700;color:#243d43}.tablewrap{overflow:auto;background:#fff;border:1px solid var(--line);border-radius:9px;margin:18px 0 30px}table{width:100%;border-collapse:collapse;font-variant-numeric:tabular-nums}th{background:#e9efed;text-align:left;font-size:11px;text-transform:uppercase;letter-spacing:.07em;position:sticky;top:0}th,td{padding:10px 12px;border-bottom:1px solid #e4e7e4;vertical-align:top;white-space:nowrap}td:nth-child(2){white-space:normal}.compact{font-size:12px}.compact th,.compact td{padding:7px 9px}code{font-size:11px}.notice{padding:17px 20px;background:var(--wash);border-left:4px solid var(--teal);margin:25px 0}.small{font-size:13px;color:var(--muted)}.verdicts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}.verdicts article{background:#e8f0ee;border-top:4px solid var(--teal);padding:5px 20px 18px}.verdicts .warn{background:var(--warn);border-color:var(--orange)}.minigrid{display:grid;gap:10px}.minigrid svg{width:100%;background:#fff;border:1px solid var(--line);border-radius:8px;padding:10px}.svgt{font:bold 14px Inter,sans-serif;fill:#14242a}.svgl,.svgv{font:11px Inter,sans-serif;fill:#52636a}.bar{fill:#1d6f78}.axis{stroke:#9ba8aa;stroke-width:1}@media(max-width:950px){.sidebar{position:relative;width:auto}.sidebar a{display:inline-flex}.brand{margin-bottom:12px}main{margin:0}.twocol,.figuregrid,.verdicts{grid-template-columns:1fr}.hero,section{padding:40px 22px}h2{font-size:34px}}@media print{.sidebar{display:none}main{margin:0}section{break-before:page}figure,.tablewrap{break-inside:avoid}}
'''
    doc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Current results gallery · singles and couples</title><style>{css}</style></head><body><nav class=sidebar><div class=brand>Results gallery<small>Singles + couples · current state</small></div>{nav}</nav><main><header class=hero><div class=eyebrow>Figure-and-table walkthrough</div><h1>What the current results show</h1><p>Singles and couples, side by side. This gallery reports the samples, observed behaviour, estimates, fit, opportunity distributions, welfare and decomposition. It is a visual record, not a second argument.</p></header>{body}</main></body></html>'''
    with OUT.open("w", encoding="utf-8", newline="\n") as f:
        f.write(doc)
    print(f"wrote {OUT} ({OUT.stat().st_size:,} bytes)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh-registry", action="store_true")
    a = ap.parse_args()
    nor = json.loads(NOR_PATH.read_text(encoding="utf-8"))
    if a.refresh_registry:
        refresh_registry(nor)
        nor = json.loads(NOR_PATH.read_text(encoding="utf-8"))
    build(nor)


if __name__ == "__main__":
    main()
