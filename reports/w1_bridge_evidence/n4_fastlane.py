"""N4 COINCIDENCE CHECK on the CERTIFIED F4/F5 fast-lane frame.

READ-ONLY. No EUROMOD, no pricing, no new draws, no estimation, no writes into
the repo. Reconstructs F4-C's own GroupState objects from the frozen staged
stem + pinned spec/theta and reads two things off the W1 reference map that the
published measure files do not carry:

  1. s_i  -- the share of the W1 reference integral carried by the non-work atom
            s_i = exp(lt_home + opp_home) / sum_j exp(lt_j + opp_j)
  2. Delta_i = lt_home - [logsumexp_j(lt_j+opp_j) - logS]
            = BC(W1_i/lam; th_c) - BC(W4_i/lam; th_c)

Both follow from the exact separability of the reference map: because W1 puts a
FLAT consumption level at every alternative, the consumption term leaves the
log-sum, so

    R_replace(m)     = BC(m/lam) + LSE_i        LSE_i = logsumexp_j(lt_j+opp_j)
    R_single_node(m) = BC(m/lam) + lt_home_i

with beta_c = 1. W1 and W4 are then CLOSED FORM off the same V_actual, and their
whole difference is Delta_i.

Self-validation: the closed-form W1 and W4 recomputed here must reproduce the
published F4-C vectors.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_REPO = Path("C:/Users/hisham/Repo/MNL")
for _p in ("scripts/bpool", "scripts/enhanced", "scripts/welfare",
           "scripts/pilot", "scripts/welfare/fastlane"):
    sys.path.insert(0, str(_REPO / _p))

import numpy as np                                          # noqa: E402
import pandas as pd                                         # noqa: E402
import jax                                                  # noqa: E402
jax.config.update("jax_enable_x64", True)

import estimation_spec_parser as sp                         # noqa: E402
import joint_recovery_test as jrt                           # noqa: E402
import run_f4a_singles_measure_core as f4a                  # noqa: E402
from _bpool_paths import bpool_dir                          # noqa: E402

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("n4_fastlane.json")
FL = _REPO / "outputs/welfare/fastlane"
BETA_C = 1.0


def box_cox(x, th):
    return f4a._box_cox(x, th)


def main() -> int:
    spec = sp.parse_specification(f4a._SPEC)
    theta = np.asarray(jrt.load_theta_star_from_csv(f4a._THETA, spec), np.float64)
    bp = bpool_dir()
    meta = json.loads((bp / (f4a.STAGED_STEM + "__mnlmeta.json")).read_text())
    c_scale = float(meta["normalization"]["singles"]["c_scale"])
    l_scale = float(meta["normalization"]["singles"]["l_scale"])

    viis = pd.read_parquet(FL / "singles_ViIS_dualstem_v1.parquet")
    viis_lookup = {int(r.uid): float(r.V_i_IS_staged) for r in viis.itertuples()}
    data_sm, data_sf, _ = jrt.build_data_objects(f4a.STAGED_STEM, [], 0)
    states = {g: f4a.GroupState(d, spec, theta, g, c_scale, l_scale, bp,
                                viis_lookup)
              for d, g in ((data_sm, "singles_male"), (data_sf, "singles_female"))}

    cert = pd.read_parquet(FL / "singles_measure_family_F5_households_v1.parquet")
    cert = cert.set_index("uid")

    rec = {"frame": "CERTIFIED F4-C / F5 fast-lane (staged stem "
                    + f4a.STAGED_STEM + ")",
           "c_scale_eur": c_scale, "l_scale_hours": l_scale,
           "beta_c": BETA_C, "gate": "none -- the F4 fast-lane does not route "
                                     "through m08_u6_rebind",
           "per_group": {}}
    frames = []

    for g, gs in states.items():
        logS = float(np.log(gs.n_alts))
        V_act = np.asarray(gs.V_target, np.float64) - logS
        lt = np.asarray(gs.leisure_term_grid, np.float64)
        opp = np.asarray(gs.opp_grid, np.float64)
        th_c = float(gs.theta_c)

        z = lt + opp
        zmax = z.max(axis=1, keepdims=True)
        ez = np.exp(z - zmax)
        LSE = zmax[:, 0] + np.log(ez.sum(axis=1))
        Lam = LSE - logS
        lt_home = np.asarray(gs.leisure_term_home, np.float64)

        home = np.zeros(z.shape, bool)
        home[np.arange(z.shape[0]), np.asarray(gs.home_idx, int)] = True
        # every non-work alternative, not only the tie-broken representative
        is_home_all = ~np.asarray(gs.working_grid, bool) \
            if hasattr(gs, "working_grid") else home
        s_rep = (ez * home).sum(axis=1) / ez.sum(axis=1)
        s_all = (ez * is_home_all).sum(axis=1) / ez.sum(axis=1)

        Delta = lt_home - Lam

        def inv(bc):
            base = 1.0 + th_c * bc
            ok = base > 0
            with np.errstate(invalid="ignore"):
                v = np.power(np.where(ok, base, np.nan), 1.0 / th_c) * c_scale
            return v, ok

        W1, _ = inv(V_act - Lam)
        W4, _ = inv(V_act - lt_home)

        c = cert.reindex(np.asarray(gs.uids, np.int64))
        W1c = c["W1_omega_eur"].to_numpy(np.float64)
        W4c = c["W4_omega_eur"].to_numpy(np.float64)
        W1wo = c["W1_workingonly_omega_eur"].to_numpy(np.float64)
        W6c = c["W6_omega_eur"].to_numpy(np.float64)
        dwt = c["dwt"].to_numpy(np.float64)

        lt_work = np.where(is_home_all, -np.inf, lt).max(axis=1)
        argmax_home = is_home_all[np.arange(lt.shape[0]), lt.argmax(axis=1)]
        # the same, on the FULL reference index lt+opp
        argmax_home_idx = is_home_all[np.arange(z.shape[0]), z.argmax(axis=1)]

        def qs(x, qq=(0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99)):
            return {str(q): float(np.nanquantile(x, q)) for q in qq}

        rec["per_group"][g] = {
            "n": int(lt.shape[0]), "n_alts": int(gs.n_alts),
            "theta_c": th_c, "theta_l": float(getattr(gs, "theta_l", np.nan)),
            "n_nonwork_alternatives_per_hh": {
                "min": int(is_home_all.sum(axis=1).min()),
                "max": int(is_home_all.sum(axis=1).max())},
            "reproduction_of_published_F4C": {
                "W1_max_abs_diff_eur": float(np.nanmax(np.abs(W1 - W1c))),
                "W4_max_abs_diff_eur": float(np.nanmax(np.abs(W4 - W4c))),
                "W1_max_rel_diff": float(np.nanmax(np.abs(W1 - W1c)
                                                   / np.abs(W1c))),
                "W4_max_rel_diff": float(np.nanmax(np.abs(W4 - W4c)
                                                   / np.abs(W4c)))},
            "share_of_reference_integral_at_nonwork": {
                "definition": "s_i = sum_{j nonwork} e^{lt+opp} / sum_j e^{lt+opp}",
                "mean": float(s_all.mean()), "min": float(s_all.min()),
                "max": float(s_all.max()), "q": qs(s_all),
                "n_above_0p99": int((s_all > .99).sum()),
                "n_above_0p90": int((s_all > .90).sum()),
                "n_above_0p50": int((s_all > .50).sum()),
                "n_below_0p10": int((s_all < .10).sum()),
                "n_below_0p01": int((s_all < .01).sum()),
                "tie_broken_single_atom_mean": float(s_rep.mean())},
            "argmax_of_leisure_index_is_nonwork_share": float(argmax_home.mean()),
            "argmax_of_full_reference_index_is_nonwork_share":
                float(argmax_home_idx.mean()),
            "lt_home_minus_lt_best_working_nats": {
                "mean": float(np.mean(lt_home - lt_work)),
                "n_negative": int((lt_home - lt_work < 0).sum()),
                "q": qs(lt_home - lt_work)},
            "Delta_nats": {"mean": float(Delta.mean()), "min": float(Delta.min()),
                           "max": float(Delta.max()),
                           "n_negative": int((Delta < 0).sum()), "q": qs(Delta)},
            "W1_eur": {"mean": float(np.nanmean(W1c)), "q": qs(W1c)},
            "W4_eur": {"mean": float(np.nanmean(W4c)), "q": qs(W4c)},
            "W1_workingonly_eur": {"mean": float(np.nanmean(W1wo)), "q": qs(W1wo)},
            "W4_over_W1": {"mean": float(np.nanmean(W4c / W1c)),
                           "min": float(np.nanmin(W4c / W1c)),
                           "max": float(np.nanmax(W4c / W1c)), "q": qs(W4c / W1c)},
            "W1wo_over_W1": {"mean": float(np.nanmean(W1wo / W1c)),
                             "min": float(np.nanmin(W1wo / W1c)),
                             "max": float(np.nanmax(W1wo / W1c)),
                             "q": qs(W1wo / W1c)},
        }
        frames.append(pd.DataFrame({
            "group": g, "uid": np.asarray(gs.uids, np.int64), "dwt": dwt,
            "V_actual": V_act, "Lambda": Lam, "lt_home": lt_home,
            "lt_best_working": lt_work, "Delta_nats": Delta,
            "share_nonwork_mass": s_all, "W1_eur": W1c, "W4_eur": W4c,
            "W1_workingonly_eur": W1wo, "W6_eur": W6c,
            "W1_closed_form_eur": W1, "W4_closed_form_eur": W4}))

    df = pd.concat(frames, ignore_index=True)
    df.to_csv(OUT.with_suffix(".csv"), index=False)
    w = df["dwt"].to_numpy(np.float64)
    w = np.where(np.isfinite(w), w, 0.0)

    def wq(x, q):
        x = np.asarray(x, np.float64)
        o = np.argsort(x)
        xs, ws = x[o], w[o]
        cc = (np.cumsum(ws) - 0.5 * ws) / ws.sum()
        return float(np.interp(q, cc, xs))

    QQ = (0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99)
    s = df["share_nonwork_mass"].to_numpy()
    d = df["Delta_nats"].to_numpy()
    rec["pooled_survey_weighted"] = {
        "n_households": int(len(df)),
        "share_of_reference_integral_at_nonwork": {
            "mean": float(np.average(s, weights=w)),
            "q": {str(q): wq(s, q) for q in QQ},
            "share_above_0p99": float(np.average(s > .99, weights=w)),
            "share_above_0p90": float(np.average(s > .90, weights=w)),
            "share_above_0p50": float(np.average(s > .50, weights=w)),
            "share_below_0p10": float(np.average(s < .10, weights=w)),
            "share_below_0p01": float(np.average(s < .01, weights=w))},
        "Delta_nats": {"mean": float(np.average(d, weights=w)),
                       "q": {str(q): wq(d, q) for q in QQ},
                       "share_negative": float(np.average(d < 0, weights=w))},
        "W1_eur": {"mean": float(np.average(df.W1_eur, weights=w)),
                   "q": {str(q): wq(df.W1_eur, q) for q in QQ}},
        "W4_eur": {"mean": float(np.average(df.W4_eur, weights=w)),
                   "q": {str(q): wq(df.W4_eur, q) for q in QQ}},
        "W1_workingonly_eur": {
            "mean": float(np.average(df.W1_workingonly_eur, weights=w)),
            "q": {str(q): wq(df.W1_workingonly_eur, q) for q in QQ}},
        "W4_over_W1": {"mean": float(np.average(df.W4_eur / df.W1_eur, weights=w)),
                       "q": {str(q): wq(df.W4_eur / df.W1_eur, q) for q in QQ}},
        "W1wo_over_W1": {
            "mean": float(np.average(df.W1_workingonly_eur / df.W1_eur, weights=w)),
            "q": {str(q): wq(df.W1_workingonly_eur / df.W1_eur, q) for q in QQ}},
    }
    OUT.write_text(json.dumps(rec, indent=2), encoding="utf-8")
    print(json.dumps(rec, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
