"""Build the V11 matched-household opportunity illustration.

Evaluates the accepted single-adult specification's leisure index and opportunity
density for every estimation household with the certified ex-ante evaluators in
the MNL_wea working copy. No estimation, pricing, welfare or decomposition
routine is called. The selection rule is fixed in advance:

1. employed single adults of the same sex, the same observed occupation group,
   the same model hours band and the same observed-wage quintile;
2. keep pairs at or below the 10th percentile of leisure-profile distance
   (maximum absolute gap between leisure-index curves over 5-70 hours, divided
   by its population standard deviation);
3. choose the pair with the largest total-variation distance between their
   opportunity densities.

Outputs contain no household identifier, row index, exact observed value, age,
region, local unemployment value, urbanisation, year or weight; model
quantities are rounded.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from scipy.stats import norm  # noqa: E402

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
WEA = ROOT.parent / "MNL_wea"
FIG_DIR = ROOT / "manuscript/figures/v11"
FIG = FIG_DIR / "fig_matched_households_v11.png"
OUT = ROOT / "reports/v11_matched_households.json"

sys.path.insert(0, str(WEA / "scripts/welfare/wea_sprint1"))
import wea_core as WC  # noqa: E402

PAB = WC.PAB


def sha(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main() -> None:
    spec = PAB.public_spec("singles")
    eng, _theta, params = PAB.load_theta("singles", spec)
    meta = json.loads(PAB.EL.META_PATH.read_text(encoding="utf-8"))
    groups = PAB.build_groups("singles", eng, meta)
    reference = PAB.reference_environment(eng, groups)
    frame_path = PAB.F1.validate_accepted_frame("singles", PAB.MNL_ROOT)
    frame = pd.read_parquet(frame_path, columns=[
        "source_idhh", "is_chosen", "working", "hours", "wage", "loc4"])
    obs = frame[frame["is_chosen"] > 0].drop_duplicates("source_idhh").set_index("source_idhh")

    grid = np.arange(5.0, 70.0 + 1e-9, 0.25)
    i_h = sum((b - a) * np.exp(WC.band_log(np.array([0.5 * (a + b)]), params, "")[0])
              for a, b in zip(WC.EDGES[:-1], WC.EDGES[1:]))
    rows, curves = [], []
    for g in groups:
        terms = WC.household_terms("singles", eng, g, params, frozenset(), reference)["self"]
        leisure = terms.beta_l[:, None] * (WC.bc((80.0 - grid) / 10.0, terms.theta_l)
                                           - WC.bc(8.0, terms.theta_l))
        k_occ = float(np.exp(terms.beta_occ).sum())
        lam = np.exp(terms.m) * k_occ * i_h
        o = obs.loc[g.ids]
        for i in range(g.n_groups):
            rows.append(dict(
                male=int(g.is_male), m=float(terms.m[i]), access_mass=float(lam[i]),
                opp_employment_share=float(lam[i] / (1.0 + lam[i])),
                mu0=float(terms.mu0[i]), sigma=float(terms.sigma),
                beta_l=float(terms.beta_l[i]), theta_l=float(terms.theta_l),
                **{f"occ_{k + 1}": float(np.exp(terms.beta_occ[k]) / k_occ) for k in range(4)},
                **{f"delta_{k + 1}": float(terms.delta_occ[k]) for k in range(4)},
                working=float(o["working"].iloc[i]), hours=float(o["hours"].iloc[i]),
                wage=float(o["wage"].iloc[i]), loc4=int(o["loc4"].iloc[i])))
            curves.append(leisure[i])
    tab = pd.DataFrame(rows)
    leis = np.vstack(curves)
    hours_density = np.exp(WC.band_log(grid, params, "")) / i_h

    def band(h: float) -> str:
        for name, lo, hi in WC.BANDS:
            if lo <= h <= hi:
                return name
        return "residual"

    emp = (tab.working > 0.5).to_numpy()
    tab["band"] = np.where(emp, [band(h) for h in tab.hours], "none")
    tab["wq"] = 0
    tab.loc[emp, "wq"] = pd.qcut(tab.loc[emp, "wage"], 5, labels=False) + 1

    first, second = [], []
    for _, idx in tab[emp].groupby(["male", "loc4", "band", "wq"]).groups.items():
        v = np.asarray(list(idx))
        if v.size < 2:
            continue
        a, b = np.triu_indices(v.size, 1)
        first.append(v[a])
        second.append(v[b])
    first, second = np.concatenate(first), np.concatenate(second)
    d_pref = np.max(np.abs(leis[first] - leis[second]), 1) / float(np.std(leis[emp]))

    pi = tab.opp_employment_share.to_numpy()
    mu0 = tab.mu0.to_numpy()
    sigma = float(tab.sigma.iloc[0])

    def l1(a1, m1, a2, m2):
        d = m2 - m1
        same = np.abs(d) < 1e-15
        cross = 0.5 * (m1 + m2) + sigma ** 2 * np.log(a1 / a2) / np.where(same, 1.0, d)
        f1, f2 = norm.cdf((cross - m1) / sigma), norm.cdf((cross - m2) / sigma)
        return np.where(same, np.abs(a1 - a2),
                        np.abs(a1 * f1 - a2 * f2) + np.abs(a1 * (1 - f1) - a2 * (1 - f2)))

    d_opp = np.abs(pi[first] - pi[second])
    for k in range(1, 5):
        share = tab[f"occ_{k}"].to_numpy()
        delta = tab[f"delta_{k}"].to_numpy()
        d_opp = d_opp + l1(pi[first] * share[first], mu0[first] + delta[first],
                           pi[second] * share[second], mu0[second] + delta[second])
    d_opp = 0.5 * d_opp
    pairs = pd.DataFrame(dict(i=first, j=second, d_pref=d_pref, d_opp=d_opp))
    cut = float(pairs.d_pref.quantile(0.10))
    chosen = pairs[pairs.d_pref <= cut].sort_values("d_opp", ascending=False).iloc[0]
    a_row, b_row = tab.iloc[int(chosen.i)], tab.iloc[int(chosen.j)]
    a_leis, b_leis = leis[int(chosen.i)], leis[int(chosen.j)]
    if a_row.access_mass < b_row.access_mass:
        a_row, b_row, a_leis, b_leis = b_row, a_row, b_leis, a_leis

    def log_offer_survival(r, w):
        parts = [np.log(r[f"occ_{k}"]) + norm.logsf((np.log(w) - r.mu0 - r[f"delta_{k}"]) / sigma)
                 for k in range(1, 5)]
        return np.logaddexp.reduce(np.vstack(parts), axis=0)

    def offer_density(r, w):
        return sum(r[f"occ_{k}"] * norm.pdf((np.log(w) - r.mu0 - r[f"delta_{k}"]) / sigma)
                   / (sigma * w) for k in range(1, 5))

    w_fine = np.exp(np.linspace(np.log(2.0), np.log(590.0), 20000))
    ls_a, ls_b = log_offer_survival(a_row, w_fine), log_offer_survival(b_row, w_fine)
    b_dominates_normalised = bool(np.all(ls_b >= ls_a - 1e-12))
    a_dominates_normalised = bool(np.all(ls_a >= ls_b - 1e-12))
    gap = (np.log(a_row.access_mass) + ls_a) - (np.log(b_row.access_mass) + ls_b)
    a_more_offers_below = float(w_fine[np.argmax(gap < 0)]) if np.any(gap < 0) else None
    mass_above_crossing = (float(np.exp(ls_a[np.argmax(gap < 0)])) if np.any(gap < 0) else 0.0)

    result = {
        "illustration": "matched single-adult households, accepted specification",
        "selection_rule": {
            "admissible": "employed, same sex, same observed occupation group, same model "
                          "hours band, same observed-wage quintile",
            "preference_filter": "leisure-profile distance at or below its 10th percentile",
            "choice": "largest total-variation distance between opportunity densities",
            "admissible_pairs": int(len(pairs)),
        },
        "shared_by_construction": ["sex (both men)" if a_row.male else "sex (both women)",
                                   "occupation group", "hours band", "observed-wage quintile"],
        "leisure_profile_distance": round(float(chosen.d_pref), 3),
        "leisure_profile_distance_p10_cut": round(cut, 3),
        "leisure_weight_A": round(float(a_row.beta_l), 2),
        "leisure_weight_B": round(float(b_row.beta_l), 2),
        "opportunity_distance": round(float(chosen.d_opp), 2),
        "opportunity_distance_admissible_median": round(float(pairs.d_opp.median()), 2),
        "access_mass_ratio_A_over_B": round(float(a_row.access_mass / b_row.access_mass), 1),
        "log_access_gap": round(float(a_row.m - b_row.m), 2),
        "opportunity_employment_share_A": round(float(a_row.opp_employment_share), 2),
        "opportunity_employment_share_B": round(float(b_row.opp_employment_share), 2),
        "wage_location_gap_B_minus_A_logpoints": round(float(100 * (b_row.mu0 - a_row.mu0)), 1),
        "hours_density_distance": 0.0,
        "occupation_mass_distance": round(float(sum(abs(a_row[f"occ_{k}"] - b_row[f"occ_{k}"])
                                                    for k in range(1, 5))), 6),
        "wage_offer_FOSD_B_over_A": b_dominates_normalised,
        "wage_offer_FOSD_A_over_B": a_dominates_normalised,
        "A_more_offers_paying_at_least_w_up_to_eur_per_hour": (
            round(a_more_offers_below) if a_more_offers_below else None),
        "offer_share_above_that_wage": float(f"{mass_above_crossing:.1g}"),
        "sources": {
            "parameters": {"path": Path(PAB.THETA_NPY["singles"]).relative_to(ROOT.parent).as_posix()
                           if Path(PAB.THETA_NPY["singles"]).is_relative_to(ROOT.parent)
                           else Path(PAB.THETA_NPY["singles"]).name,
                           "sha256": sha(PAB.THETA_NPY["singles"])},
            "estimation_frame": {"path": Path(frame_path).relative_to(ROOT.parent).as_posix()
                                 if Path(frame_path).is_relative_to(ROOT.parent) else Path(frame_path).name,
                                 "sha256": sha(frame_path)},
            "evaluator": {"path": "MNL_wea/scripts/welfare/wea_sprint1/wea_core.py",
                          "sha256": sha(WEA / "scripts/welfare/wea_sprint1/wea_core.py")},
            "loader": {"path": "MNL_wea/scripts/welfare/preseminar_pab_v1.py",
                       "sha256": sha(WEA / "scripts/welfare/preseminar_pab_v1.py")},
        },
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")

    FIG_DIR.mkdir(parents=True, exist_ok=True)
    blue, orange, grey = "#1f4e79", "#b5651d", "#6b7280"
    fig, axes = plt.subplots(2, 3, figsize=(13.5, 7.6))
    ax = axes[0, 0]
    ax.plot(grid, a_leis, color=blue, lw=2.2, label="Household A")
    ax.plot(grid, b_leis, color=orange, lw=1.6, ls="--", label="Household B")
    ax.set_title("(a) Leisure value of hours worked")
    ax.set_xlabel("weekly hours")
    ax.set_ylabel("$L_i(h)-L_i(o)$, utility units")
    ax.legend(frameon=False)

    ax = axes[0, 1]
    shares = [a_row.opp_employment_share, b_row.opp_employment_share]
    ax.bar(["A", "B"], shares, color=[blue, orange])
    ax.set_ylim(0, 1)
    ax.set_title("(b) Access: employment share of\nopportunity mass")
    ax.set_ylabel("share")
    for x, s in enumerate(shares):
        ax.text(x, s + 0.03, f"{s:.2f}", ha="center")

    ax = axes[0, 2]
    ax.plot(grid, hours_density, color=grey, lw=2.0)
    ax.set_title("(c) Hours density (common to both)")
    ax.set_xlabel("weekly hours")
    ax.set_ylabel("density given employment")

    ax = axes[1, 0]
    occ = np.arange(1, 5)
    ax.bar(occ - 0.18, [a_row[f"occ_{k}"] for k in occ], width=0.36, color=blue, label="A")
    ax.bar(occ + 0.18, [b_row[f"occ_{k}"] for k in occ], width=0.36, color=orange, label="B")
    ax.set_xticks(occ)
    ax.set_title("(d) Occupation mass (identical)")
    ax.set_xlabel("occupation group")
    ax.set_ylabel("share given employment")
    ax.legend(frameon=False)

    w_plot = np.linspace(2.0, 60.0, 600)
    ax = axes[1, 1]
    ax.plot(w_plot, offer_density(a_row, w_plot), color=blue, lw=2.2, label="A")
    ax.plot(w_plot, offer_density(b_row, w_plot), color=orange, lw=1.6, ls="--", label="B")
    ax.set_title("(e) Wage-offer density given employment")
    ax.set_xlabel("EUR per hour")
    ax.legend(frameon=False)

    ax = axes[1, 2]
    ax.plot(w_plot, a_row.access_mass * np.exp(log_offer_survival(a_row, w_plot)),
            color=blue, lw=2.2, label="A")
    ax.plot(w_plot, b_row.access_mass * np.exp(log_offer_survival(b_row, w_plot)),
            color=orange, lw=1.6, ls="--", label="B")
    ax.set_yscale("log")
    ax.set_title("(f) Offers paying at least $w$\n(relative opportunity intensity)")
    ax.set_xlabel("EUR per hour")
    ax.legend(frameon=False)
    for axis in axes.flat:
        axis.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(FIG, dpi=160)
    print(f"wrote {FIG} and {OUT}")
    print(json.dumps({k: v for k, v in result.items() if k != "sources"}, indent=1))


if __name__ == "__main__":
    main()
