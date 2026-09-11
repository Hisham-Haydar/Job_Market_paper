"""Reproduce every derived numeral in JMP_W1_reference_domain_fork_v1.md.

REC-1 / Deputy R3 item 2. One small deterministic script:

* reads ONLY the accepted S11 parameter tables (singles, couples), by path,
  plus the reference households the memo names (age, hours, children,
  consumption, recorded leisure weight) from the certified preference-figure
  record -- no other sample microdata;
* uses no welfare engine and no simulation; closed-form arithmetic and fixed
  grids only (standard library only);
* writes docs/normative/fork_derived_numerals_v1.csv with the columns
  numeral_id, memo_section, formula, inputs, value, memo_value, abs_diff, pass.

Tolerance: the memo's printed precision. A row passes iff
|value - memo_value| <= 0.5 * 10**(-d) (+1e-12), where d is the number of
decimals printed in the memo. Percentages are compared in percent units.
A mismatch is reported, never silently edited. Exit code 1 if any row fails.

Not covered (not authorised): counting sample couples in the man-only corner.

Conventions (spec conventions, not data): time endowment T = 80 h/week,
leisure normaliser 10 (l = (80 - h)/10), market hours support [5, 70].
Source of the support: MNL .../figE1_matched_households/e1_matched_households_v1.json
binding.spec_conventions (h_min 5.0, h_max 70.0).
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve()
JMP = HERE.parents[3]
MNL = HERE.parents[4] / "MNL"
RUNS = MNL / "experiments" / "JMP_SEMINAR_SPRINT" / "runs"

INPUTS = {
    "singles": (RUNS / "s11_welfare_specs_of_record" / "s11_singles_parameter_table_v1.csv",
                "cee4a136f9ce69753965beaa779753bed59e75972490ebb0f2b6114f790413ab"),
    "couples": (RUNS / "s11_welfare_specs_of_record" / "s11_couples_parameter_table_v1.csv",
                "fc1794b437c74ac4e6ab240aaa7c71b7c38ee21512395a175b38c785a5e061c9"),
    "refhh": (RUNS / "preference_figures_final" / "pff_step1_reference_v1.json",
              "594a941ebacad8e4b4462e464732199d836b8ca65c43a0679368e0c03375d41a"),
}
OUT = JMP / "docs" / "normative" / "fork_derived_numerals_v1.csv"

T_ENDOW, L_SCALE, H_MIN, H_MAX = 80.0, 10.0, 5.0, 70.0


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_table(path: Path) -> dict:
    with path.open(newline="", encoding="utf-8") as fh:
        return {r["param"]: float(r["estimate"]) for r in csv.DictReader(fh)}


def bc(z: float, th: float) -> float:
    """Box-Cox (z**th - 1)/th, th != 0 on every block used here."""
    return (z ** th - 1.0) / th


def lt(h: float) -> float:
    return (T_ENDOW - h) / L_SCALE


LT_HOME, LT_MIN, LT_MAX = lt(0.0), lt(H_MIN), lt(H_MAX)   # 8.0, 7.5, 1.0


def quad(b0, ba, ba2, a, bk=0.0, k=0.0):
    return b0 + ba * a + ba2 * a * a + bk * k


def main() -> int:
    for key, (path, want) in INPUTS.items():
        got = sha256(path)
        if got != want:
            print(f"INPUT HASH MISMATCH {key}: {path}\n  want {want}\n  got  {got}")
            return 2
        print(f"input {key}: {path.name} sha256 {got}")

    S, C = load_table(INPUTS["singles"][0]), load_table(INPUTS["couples"][0])
    ref = json.loads(INPUTS["refhh"][0].read_text(encoding="utf-8"))
    conv = ref["convention_evidence"]
    hh = {r["block"]: r for r in ref["reference_households"]}

    rows: list[list] = []

    def add(nid, sec, formula, inputs, value, memo):
        memo_s = str(memo).replace(",", "")
        d = len(memo_s.split(".")[1]) if "." in memo_s else 0
        diff = abs(value - float(memo_s))
        ok = diff <= 0.5 * 10 ** (-d) + 1e-12
        rows.append([nid, sec, formula, inputs, f"{value:.10g}", memo_s, f"{diff:.3g}", ok])

    # ---------------- singles --------------------------------------------
    bcS = S["beta_c"]
    blocks_s = {
        "sm": dict(b0=S["beta_l0_sm"], ba=S["beta_l_age_sm"], ba2=S["beta_l_age2_sm"], bk=0.0,
                   th=S["theta_l_sm"], hh=hh["singles_male"]),
        "sf": dict(b0=S["beta_l0_sf"], ba=S["beta_l_age_sf"], ba2=S["beta_l_age2_sf"],
                   bk=S["beta_l_nkids_sf"], th=S["theta_l_sf"], hh=hh["singles_female"]),
    }
    ctr_s, scl_s = conv["singles"]["age_centre"], conv["singles"]["age_scale"]

    def a_s(age):
        return (age - ctr_s) / scl_s

    add("REC.bc_singles", "§0 notation", "beta_c (singles)", "S11 singles", bcS, "2.0387")
    add("REC.bc_couples", "§0 notation", "beta_c (couples)", "S11 couples", C["beta_c"], "2.1017")

    memo_t1 = {  # block, case -> (beta, rho20, rho35, rho39, rho50, gap, nwlo, nwhi)
        # Values match the memo's Table 1 as corrected under revision r3
        # (REC-1 / Deputy R3 item 2): four cells were double-rounded in the
        # first pass and are now the script's own reproduced values.
        ("sm", "min"): ("7.814", "0.962", "0.891", "0.862", "0.736", "1.0089", "1.009", "9.75"),
        ("sm", "ref"): ("8.562", "0.958", "0.881", "0.850", "0.715", "1.0098", "1.010", "12.1"),
        ("sm", "age20"): ("9.171", "0.955", "0.874", "0.840", "0.698", "1.0105", "1.010", "14.5"),
        ("sm", "age60"): ("13.403", "0.935", "0.821", "0.775", "0.592", "1.0153", "1.015", "49.7"),
        ("sf", "min"): ("5.867", "0.896", "0.748", "0.698", "0.527", "1.0282", "1.028", "14.2"),
        ("sf", "ref"): ("6.053", "0.893", "0.741", "0.690", "0.516", "1.0291", "1.029", "15.4"),
        ("sf", "age20"): ("10.878", "0.815", "0.584", "0.513", "0.304", "1.0529", "1.053", "137"),
        ("sf", "age60"): ("8.970", "0.845", "0.642", "0.577", "0.375", "1.0435", "1.043", "57.7"),
    }
    memo_minage = {"sm": "33.2", "sf": "42.4"}
    memo_B = {"sm": ("0.594005", "0.591693", "-1.6263"), "sf": ("0.921565", "0.911895", "-0.9274")}
    beta_s: dict = {}

    for b, p in blocks_s.items():
        th = p["th"]
        B8, B75, B1 = bc(LT_HOME, th), bc(LT_MIN, th), bc(LT_MAX, th)
        add(f"T1.{b}.theta", "§1.2 Table 1 note", "theta_l", f"S11 singles theta_l_{b}", th, memo_B[b][2])
        add(f"T1.{b}.B8", "§1.2 Table 1 note", "B(8;theta)", f"theta_l_{b}", B8, memo_B[b][0])
        add(f"T1.{b}.B75", "§1.2 Table 1 note", "B(7.5;theta)", f"theta_l_{b}", B75, memo_B[b][1])
        astar = -p["ba"] / (2 * p["ba2"])
        bmin = quad(p["b0"], p["ba"], p["ba2"], astar)
        hr = p["hh"]
        kref = hr["n_children"] if p["bk"] else 0.0
        bref = quad(p["b0"], p["ba"], p["ba2"], a_s(hr["age_years"]), p["bk"], kref)
        add(f"GATE.{b}.beta_ref_vs_record", "input gate",
            "beta_l(ref HH) recomputed vs recorded omega_at_reference",
            f"S11 {b} leisure block; ref HH age {hr['age_years']}, k {kref}",
            bref, f"{hr['omega_at_reference']:.9f}")
        cases = {"min": bmin, "ref": bref,
                 "age20": quad(p["b0"], p["ba"], p["ba2"], a_s(20.0)),
                 "age60": quad(p["b0"], p["ba"], p["ba2"], a_s(60.0))}
        beta_s[b] = cases
        add(f"T1.{b}.min.age", "§1.2 Table 1", "age at min beta_l = centre + scale*(-ba/2ba2)",
            f"S11 {b}", ctr_s + scl_s * astar, memo_minage[b])
        for case, beta in cases.items():
            m = memo_t1[(b, case)]
            pre = f"T1.{b}.{case}"
            add(pre + ".beta", "§1.2 Table 1", "beta_l(x)", f"S11 {b}; case {case}", beta, m[0])
            for i, h in enumerate((20, 35, 39, 50)):
                val = math.exp(-beta * (B75 - bc(lt(h), th)) / bcS)
                add(pre + f".rho{h}", "§1.2 Table 1", "exp{-beta[B(7.5)-B((80-h)/10)]/beta_c}",
                    f"beta_l {case}; h={h}", val, m[1 + i])
            gap = math.exp(beta * (B8 - B75) / bcS)
            add(pre + ".gap", "§1.2 Table 1", "exp{beta[B(8)-B(7.5)]/beta_c}", f"beta_l {case}", gap, m[5])
            add(pre + ".nwlo", "§1.2 Table 1", "nonworker band lower = gap", f"beta_l {case}", gap, m[6])
            add(pre + ".nwhi", "§1.2 Table 1", "exp{beta[B(8)-B(1)]/beta_c}", f"beta_l {case}",
                math.exp(beta * (B8 - B1) / bcS), m[7])

    # singles reference households (worker at observed hours)
    def s_factors(b):
        p, beta = blocks_s[b], beta_s[b]["ref"]
        th, h = p["th"], p["hh"]["hours_per_week"]
        F = math.exp(-beta * (bc(LT_HOME, th) - bc(lt(h), th)) / bcS)
        Mlo = math.exp(-beta * (bc(LT_MIN, th) - bc(lt(h), th)) / bcS)
        return F, Mlo, p["hh"]["consumption_eur_per_month"]

    F_sm, Mlo_sm, C_sm = s_factors("sm")
    F_sf, Mlo_sf, C_sf = s_factors("sf")
    for tag, F, Mlo, Cc, mF, mM, eF, eM, eC in (
            ("sm", F_sm, Mlo_sm, C_sm, "0.8415", "0.8498", "1589", "1605", "1889"),
            ("sf", F_sf, Mlo_sf, C_sf, "0.7203", "0.7412", "1339", "1378", "1859")):
        add(f"REF.{tag}.F", "§1.2 ref households", "exp{[L(h_obs)-L(o)]/beta_c}", f"ref HH {tag}", F, mF)
        add(f"REF.{tag}.Mlo", "§1.2 ref households", "exp{[L(h_obs)-L(5)]/beta_c} (= dense-law M)",
            f"ref HH {tag}", Mlo, mM)
        add(f"REF.{tag}.Mhi", "§1.2 ref households", "worker upper bound = 1", f"ref HH {tag}", 1.0, "1.0000")
        add(f"REF.{tag}.EUR_F", "§1.2 ref households", "C_obs * F", f"C_obs {Cc:.2f}", Cc * F, eF)
        add(f"REF.{tag}.EUR_Mlo", "§1.2 ref households", "C_obs * Mlo", f"C_obs {Cc:.2f}", Cc * Mlo, eM)
        add(f"REF.{tag}.EUR_Mhi", "§1.2 ref households", "C_obs", f"C_obs {Cc:.2f}", Cc, eC)
    add("REF.sm.maxmove", "§1.2", "1 / Mlo (max kappa/law movement)", "ref single man", 1 / Mlo_sm, "1.18")
    add("REF.sm.MF_lo", "§1.2 comparison with F", "exp{[L(o)-L(5)]/beta_c}", "ref single man",
        Mlo_sm / F_sm, "1.010")
    add("REF.sm.MF_hi", "§1.2 comparison with F", "exp{[L(o)-L(h_obs)]/beta_c} = 1/F", "ref single man",
        1 / F_sm, "1.188")
    add("REF.sm.MF_hi_2dp", "§1.2 box", "1/F (printed 1.19)", "ref single man", 1 / F_sm, "1.19")
    sm_ref_nwhi = math.exp(beta_s["sm"]["ref"] * (bc(LT_HOME, blocks_s["sm"]["th"])
                                                  - bc(LT_MAX, blocks_s["sm"]["th"])) / bcS)
    add("E.sm.ceiling", "§0 5(e); §3.4(e)", "exp{[L(o)-L(70)]/beta_c}", "ref single man", sm_ref_nwhi, "12.1")
    add("TC.sm.12x", "§3.4 treatment (c)", "same ceiling, printed as 12x", "ref single man", sm_ref_nwhi, "12")

    # singles dense-law M/F gap ranges over ages 20-60 (k=0), incl. the minimum
    rng = {}
    for b, p in blocks_s.items():
        th = p["th"]
        dB = bc(LT_HOME, th) - bc(LT_MIN, th)
        ages = [20.0 + 0.01 * i for i in range(4001)]
        ages.append(ctr_s + scl_s * (-p["ba"] / (2 * p["ba2"])))
        gaps = [math.exp(quad(p["b0"], p["ba"], p["ba2"], a_s(x)) * dB / bcS) for x in ages]
        rng[b] = (min(gaps), max(gaps))
    add("G41.sm.lo", "§4.1", "min over ages 20-60 of gap", "S11 sm", rng["sm"][0], "1.009")
    add("G41.sm.hi", "§4.1", "max over ages 20-60 of gap", "S11 sm", rng["sm"][1], "1.015")
    add("G41.sf.lo", "§4.1", "min over ages 20-60 of gap (k=0)", "S11 sf", rng["sf"][0], "1.028")
    add("G41.sf.hi", "§4.1", "max over ages 20-60 of gap (k=0)", "S11 sf", rng["sf"][1], "1.053")

    # ---------------- couples --------------------------------------------
    bcC = C["beta_c"]
    thm, thf = C["theta_l_m"], C["theta_l_f"]
    b0m, bam, ba2m = C["beta_l0_m"], C["beta_l_age_m"], C["beta_l_age2_m"]
    b0f, baf, ba2f, bkf = C["beta_l0_f"], C["beta_l_age_f"], C["beta_l_age2_f"], C["beta_l_nkids_f"]
    ctr_c = conv["couples"]["age_centre_male"]
    assert ctr_c == conv["couples"]["age_centre_female"] and conv["couples"]["age_scale"] == 1.0

    def bm(age):
        return quad(b0m, bam, ba2m, age - ctr_c)

    def bf(age, k=0.0):
        return quad(b0f, baf, ba2f, age - ctr_c, bkf, k)

    B8m, B75m, B1m = bc(LT_HOME, thm), bc(LT_MIN, thm), bc(LT_MAX, thm)
    B8f, B75f, B1f = bc(LT_HOME, thf), bc(LT_MIN, thf), bc(LT_MAX, thf)
    dBm, dBf = B8m - B75m, B8f - B75f
    T = dBm / dBf

    add("C.theta_m", "§5.1", "theta_l_m", "S11 couples", thm, "-0.97611")
    add("C.theta_f", "§5.1", "theta_l_f", "S11 couples", thf, "-1.68631")
    add("C.theta_m_3dp", "§5.1 text", "theta_l_m", "S11 couples", thm, "-0.976")
    add("C.theta_f_3dp", "§5.1 text", "theta_l_f", "S11 couples", thf, "-1.686")
    add("C.B8m", "§5.1", "B(8;theta_m)", "theta_l_m", B8m, "0.889893")
    add("C.B75m", "§5.1", "B(7.5;theta_m)", "theta_l_m", B75m, "0.881143")
    add("C.B8f", "§5.1", "B(8;theta_f)", "theta_l_f", B8f, "0.575222")
    add("C.B75f", "§5.1", "B(7.5;theta_f)", "theta_l_f", B75f, "0.573176")
    add("C.dBm", "§5.1", "B(8)-B(7.5), men", "theta_l_m", dBm, "0.008751")
    add("C.dBf", "§5.1", "B(8)-B(7.5), women", "theta_l_f", dBf, "0.002045")
    add("C.slope_m", "§5.1", "7.75**(theta_m-1)", "theta_l_m", 7.75 ** (thm - 1), "0.01748")
    add("C.slope_f", "§5.1", "7.75**(theta_f-1)", "theta_l_f", 7.75 ** (thf - 1), "0.00408")
    add("C.threshold", "§5.1; §5 table", "dBm/dBf (man-only iff beta_f/beta_m exceeds it)",
        "theta_l_m, theta_l_f", T, "4.278")
    add("C.threshold_4dp", "§5.1", "dBm/dBf", "theta_l_m, theta_l_f", T, "4.2784")

    am_star = -bam / (2 * ba2m)
    af_star = -baf / (2 * ba2f)
    bm_min = quad(b0m, bam, ba2m, am_star)
    bf_min = quad(b0f, baf, ba2f, af_star)
    add("C.bm_min", "§5.1", "min over age of beta_l_m", "S11 couples male block", bm_min, "3.9789")
    add("C.bf_min", "§5.1", "min over age of beta_l_f (k=0)", "S11 couples female block", bf_min, "12.5868")
    add("C.loss_m_min", "§5.1", "bm_min*dBm", "", bm_min * dBm, "0.03482")
    add("C.loss_f_min", "§5.1", "bf_min*dBf", "", bf_min * dBf, "0.02575")
    add("C.bm_min_age", "§5.1", "centre - bam/(2 ba2m)", "S11 couples male block", ctr_c + am_star, "41.7")

    hm, hf = hh["couples_male"], hh["couples_female"]
    bm_ref = bm(hm["age_years"])
    bf_ref = bf(hf["age_years"], hf["n_children"])
    add("GATE.cm.beta_ref_vs_record", "input gate", "beta_l_m(ref) recomputed vs recorded",
        f"age {hm['age_years']}", bm_ref, f"{hm['omega_at_reference']:.9f}")
    add("GATE.cf.beta_ref_vs_record", "input gate", "beta_l_f(ref) recomputed vs recorded",
        f"age {hf['age_years']}, k {hf['n_children']}", bf_ref, f"{hf['omega_at_reference']:.9f}")
    add("C.bm_ref", "§5.1", "beta_l_m(ref HH)", "man 38", bm_ref, "4.0686")
    add("C.bf_ref", "§5.1", "beta_l_f(ref HH)", "woman 37, k=3", bf_ref, "12.8135")
    lm5, lf5 = bm_ref * dBm, bf_ref * dBf
    add("C.loss_m_ref", "§5.1", "bm_ref*dBm", "", lm5, "0.03560")
    add("C.loss_f_ref", "§5.1", "bf_ref*dBf", "", lf5, "0.02621")
    add("C.loss_m_ref_3dp", "§5 table", "bm_ref*dBm", "", lm5, "0.0356")
    add("C.loss_f_ref_3dp", "§5 table", "bf_ref*dBf", "", lf5, "0.0262")
    add("C.weight_ratio_ref", "§5.1", "bf_ref/bm_ref", "", bf_ref / bm_ref, "3.15")

    # same-age ratio peak (k=0) and limit
    best = (-1.0, 0.0)
    for i in range(120001):
        a = -60.0 + 0.001 * i
        r = quad(b0f, baf, ba2f, a) / quad(b0m, bam, ba2m, a)
        if r > best[0]:
            best = (r, a)
    add("C.peak_ratio", "§5.1", "max_a beta_f(a,k=0)/beta_m(a), same age (grid 0.001 y)", "", best[0], "3.33")
    add("C.peak_age", "§5.1", "argmax age", "", ctr_c + best[1], "37.7")
    add("C.ratio_limit", "§5.1", "ba2f/ba2m", "", ba2f / ba2m, "1.13")
    need = T * bm_min
    add("C.need_bf", "§5.1", "threshold * min beta_m", "", need, "17.02")

    def woman_ages(k):
        c = b0f + bkf * k - need
        disc = baf * baf - 4 * ba2f * c
        r1 = (-baf - math.sqrt(disc)) / (2 * ba2f)
        r2 = (-baf + math.sqrt(disc)) / (2 * ba2f)
        return ctr_c + min(r1, r2), ctr_c + max(r1, r2)

    for k, memo_lo in ((0, "24.9"), (1, "24.0"), (2, "23.2")):
        lo, hi = woman_ages(k)
        add(f"C.woman_max_age_k{k}", "§5.1", "woman age below which beta_f > 17.02", f"k={k}", lo, memo_lo)
        if k == 0:
            add("C.woman_min_age_old_k0", "§5.1", "woman age above which beta_f > 17.02", "k=0", hi, "74.1")

    def man_interval(af, k):
        thr = bf(af, k) / T
        c = b0m - thr
        disc = bam * bam - 4 * ba2m * c
        r1 = (-bam - math.sqrt(disc)) / (2 * ba2m)
        r2 = (-bam + math.sqrt(disc)) / (2 * ba2m)
        return ctr_c + min(r1, r2), ctr_c + max(r1, r2)

    for af, mlo, mhi in ((20.0, "33.4", "50.1"), (24.0, "38.3", "45.1")):
        lo, hi = man_interval(af, 0)
        add(f"C.man_lo_w{int(af)}", "§5.1", "man-age interval for man-only", f"woman {af:g}, k=0", lo, mlo)
        add(f"C.man_hi_w{int(af)}", "§5.1", "man-age interval for man-only", f"woman {af:g}, k=0", hi, mhi)

    # reference couple (dual earner 39/35) and man-only 39h, NN band
    def lm(h, beta=bm_ref):
        return beta * (B8m - bc(lt(h), thm))

    def lf(h, beta=bf_ref):
        return beta * (B8f - bc(lt(h), thf))

    ref_loss = min(lm5, lf5)
    LF = -(lm(39) + lf(35))
    WF = math.exp(LF / bcC)
    WM = math.exp((LF + ref_loss) / bcC)
    WFD = math.exp((LF + min(lm(39), lf(35))) / bcC)
    Ccpl = hm["consumption_eur_per_month"]
    add("REF.cpl.F", "§1.2 ref households", "exp{-(l_m(39)+l_f(35))/beta_c}", "ref couple", WF, "0.6587")
    add("REF.cpl.Mlo", "§1.2 ref households", "F*exp{min(l_m5,l_f5)/beta_c}", "ref couple", WM, "0.6670")
    add("REF.cpl.Mhi_FD", "§1.2 ref households", "F*exp{min(l_m(39),l_f(35))/beta_c}", "ref couple", WFD, "0.7868")
    add("REF.cpl.EUR_F", "§1.2 ref households", "C_obs*F", f"C_obs {Ccpl:.2f}", Ccpl * WF, "2769")
    add("REF.cpl.EUR_Mlo", "§1.2 ref households", "C_obs*Mlo", f"C_obs {Ccpl:.2f}", Ccpl * WM, "2804")
    add("REF.cpl.EUR_Mhi", "§1.2 ref households", "C_obs*Mhi_FD", f"C_obs {Ccpl:.2f}", Ccpl * WFD, "3308")
    add("C.manonly.F", "§5 table; §1.2 check", "exp{-l_m(39)/beta_c}", "ref weights", math.exp(-lm(39) / bcC), "0.7868")
    add("C.manonly.M", "§5 table; §1.2 check", "exp{(-l_m(39)+min loss5)/beta_c}", "ref weights",
        math.exp((-lm(39) + ref_loss) / bcC), "0.7967")
    add("C.NN.lo", "§5 table", "exp{min(l_m5,l_f5)/beta_c}", "ref weights", math.exp(ref_loss / bcC), "1.0125")
    nn_fd = math.exp(min(lm(70), lf(70)) / bcC)
    add("C.NN.hi_FD", "§5 table", "exp{min(l_m(70),l_f(70))/beta_c}", "ref weights", nn_fd, "5.60")
    add("E.NN.ceiling", "§3.4(e)", "same, printed 5.6x", "ref weights", nn_fd, "5.6")
    add("C.NN.hi_noFD", "§5 table", "exp{(l_m(70)+l_f(70))/beta_c}", "ref weights",
        math.exp((lm(70) + lf(70)) / bcC), "187")

    # couples dense-law gap
    g_min = math.exp(min(bm_min * dBm, bf_min * dBf) / bcC)
    g_ref = math.exp(ref_loss / bcC)
    add("G41.cpl.lo", "§4.1", "gap at block minima", "", min(g_min, g_ref), "1.012")
    add("G41.cpl.hi", "§4.1", "gap at reference household", "", max(g_min, g_ref), "1.013")
    gaps_c = []
    for i in range(81):
        for j in range(81):
            for k in range(4):
                am_, af_ = 20.0 + 0.5 * i, 20.0 + 0.5 * j
                gaps_c.append(math.exp(min(bm(am_) * dBm, bf(af_, k) * dBf) / bcC))
    add("C.gap2060.lo", "§5.1", "min gap over spouse ages 20-60 (0.5 y), k=0..3", "", min(gaps_c), "1.01")
    add("C.gap2060.hi", "§5.1", "max gap over spouse ages 20-60 (0.5 y), k=0..3", "", max(gaps_c), "1.02")

    # headline ranges quoted in prose (r0 log "1.01-1.05"; "1-5%")
    all_gaps = [rng["sm"][0], rng["sm"][1], rng["sf"][0], rng["sf"][1], min(g_min, g_ref), max(g_min, g_ref)]
    add("H.gap.lo", "revision log r0", "min dense-law gap (singles 20-60, couples)", "", min(all_gaps), "1.01")
    add("H.gap.hi", "revision log r0", "max dense-law gap (singles 20-60, couples)", "", max(all_gaps), "1.05")
    add("H.pct.lo", "§2.5; §4.3; §6", "min gap - 1, in percent", "", 100 * (min(all_gaps) - 1), "1")
    add("H.pct.hi", "§2.5; §4.3; §6", "max gap - 1, in percent", "", 100 * (max(all_gaps) - 1), "5")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["numeral_id", "memo_section", "formula", "inputs", "value", "memo_value", "abs_diff", "pass"])
        w.writerows(rows)

    fails = [r for r in rows if not r[7]]
    print(f"rows {len(rows)}  pass {len(rows) - len(fails)}  fail {len(fails)}")
    for r in fails:
        print("FAIL", r[0], "value", r[4], "memo", r[5], "diff", r[6])
    print(f"wrote {OUT}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
