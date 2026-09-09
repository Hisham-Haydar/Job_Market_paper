# -*- coding: utf-8 -*-
"""Sections 7-12: parameterization, chronology, fit, external validation,
couples, children."""
import json

from common import n, a, lit, box, math, imath, aux_data, NOR_PATH


# The audience-facing grouping of the 41 estimated coordinates.
PARAM_GROUPS = [
    ("Male preferences", "How single men value time, and how that changes with age.",
     ["beta_l0_sm", "beta_l_age_sm", "beta_l_age2_sm", "theta_l_sm"]),
    ("Female preferences",
     "How single women value time, with age and with children present.",
     ["beta_l0_sf", "beta_l_age_sf", "beta_l_age2_sf", "beta_l_nkids_sf", "theta_l_sf"]),
    ("Consumption curvature",
     "Diminishing marginal utility of consumption; governs the income&ndash;time "
     "trade-off. <b>Maintained common across the sexes</b> &mdash; not tested "
     "sex-specifically.",
     ["theta_c_singles"]),
    ("Employment and hours access",
     "The level of the employment margin, and how much offer density sits in each "
     "hours band.",
     ["beta_E", "beta_h_pt1", "beta_h_pt2", "beta_h_ft", "beta_h_lh"]),
    ("Geography and local market access",
     "How job access tilts with the local unemployment rate, region and urbanisation. "
     "Section&nbsp;17 is built entirely on this group.",
     ["beta_E_gsur", "beta_E_drgn2", "beta_E_drgn3", "beta_E_drgn4", "beta_E_drgn5",
      "beta_E_drgn6", "beta_E_drgn7", "beta_E_drgn8", "beta_E_drgur", "beta_E_drgmd"]),
    ("Occupation access",
     "How reachable each occupation group is, by sex. Group one is the reference.",
     ["beta_occ_2_m", "beta_occ_3_m", "beta_occ_4_m",
      "beta_occ_2_f", "beta_occ_3_f", "beta_occ_4_f"]),
    ("The statutory-week peak",
     "The extra offer density at the statutory working week. One coefficient; the "
     "largest single specification gain in the paper.",
     ["beta_h_f35"]),
    ("Wage opportunities",
     "Location and dispersion of the hourly offer density: schooling, experience and "
     "the common spread.",
     ["beta_w0", "beta_w_educL", "beta_w_educH", "beta_w_pexp", "beta_w_pexp2", "sigma"]),
    ("Occupation-conditioned wage shifts",
     "What each occupation group pays, on the same dispersion. Separate from whether "
     "it can be entered.",
     ["delta_occ_2", "delta_occ_3", "delta_occ_4"]),
]

PARAM_GLOSS = {
    "beta_l0_sm": "Baseline leisure weight, single men.",
    "beta_l_age_sm": "Linear age gradient in the male leisure weight.",
    "beta_l_age2_sm": "Quadratic age term, male leisure weight.",
    "theta_l_sm": "Box&ndash;Cox curvature on leisure, men. Strongly negative: sharply "
                  "diminishing marginal value of extra time.",
    "beta_l0_sf": "Baseline leisure weight, single women.",
    "beta_l_age_sf": "Linear age gradient in the female leisure weight.",
    "beta_l_age2_sf": "Quadratic age term, female leisure weight.",
    "beta_l_nkids_sf": "Shift in the female leisure weight per dependent child. "
                       "Section&nbsp;12.",
    "theta_l_sf": "Box&ndash;Cox curvature on leisure, women.",
    "theta_c_singles": "Box&ndash;Cox curvature on consumption. Well inside the unit interval, so marginal utility of income falls with income. "
                       "<b>Shared by the two sexes by construction of the specification</b>, for two reasons: the consumption coefficient is the scale numeraire, so the consumption block carries the units of the money metric and splitting its curvature would split the metric itself; and parsimony &mdash; a sex-specific consumption curvature was never proposed in the specification search, so it was <b>never tested</b>. The estimate is a level, not a test of pooling. Section&nbsp;20 carries it as a candidate money-metric sensitivity.",

    "beta_E": "Employment-margin intercept: the level of offer density on working at "
              "all, against the non-employment state.",
    "beta_h_pt1": "Offer density at short part time, relative to the residual bins.",
    "beta_h_pt2": "Offer density at long part time.",
    "beta_h_ft": "Offer density at standard full time.",
    "beta_h_lh": "Offer density at long hours.",
    "beta_E_gsur": "Local unemployment rate. Large and sharply negative: the single "
                   "strongest access regressor in the model.",
    "beta_E_drgn2": "NUTS-1 region indicator.", "beta_E_drgn3": "NUTS-1 region indicator.",
    "beta_E_drgn4": "NUTS-1 region indicator.", "beta_E_drgn5": "NUTS-1 region indicator.",
    "beta_E_drgn6": "NUTS-1 region indicator.", "beta_E_drgn7": "NUTS-1 region indicator.",
    "beta_E_drgn8": "NUTS-1 region indicator.",
    "beta_E_drgur": "Urban against rural.", "beta_E_drgmd": "Intermediate against rural.",
    "beta_occ_2_m": "Access to occupation group two, men.",
    "beta_occ_3_m": "Access to occupation group three, men.",
    "beta_occ_4_m": "Access to occupation group four, men.",
    "beta_occ_2_f": "Access to occupation group two, women.",
    "beta_occ_3_f": "Access to occupation group three, women.",
    "beta_occ_4_f": "Access to occupation group four, women.",
    "beta_h_f35": "The statutory-week peak: extra offer density in the statutory band.",
    "beta_w0": "Wage-offer location intercept.",
    "beta_w_educL": "Low education against the middle reference.",
    "beta_w_educH": "High education against the middle reference.",
    "beta_w_pexp": "Potential experience, linear.",
    "beta_w_pexp2": "Potential experience, squared.",
    "sigma": "Dispersion of the log wage-offer density. Common to all households.",
    "delta_occ_2": "Wage-offer location shift, occupation group two.",
    "delta_occ_3": "Wage-offer location shift, occupation group three.",
    "delta_occ_4": "Wage-offer location shift, occupation group four.",
}


def _param_table():
    rows = []
    rows.append('<div class="scroll"><table><thead><tr>'
                "<th>Coefficient</th><th>What it is</th>"
                '<th class="num">Estimate</th><th class="num">Robust SE</th>'
                '<th class="num">95% interval</th><th class="num">z</th>'
                "</tr></thead><tbody>")
    for title, blurb, keys in PARAM_GROUPS:
        rows.append('<tr class="grouphead"><td colspan="6">%s &mdash; <span '
                    'style="font-weight:400">%s</span></td></tr>' % (title, blurb))
        for k in keys:
            b = "params41.%s." % k
            gloss = PARAM_GLOSS.get(k, "")
            if k in ("beta_l_age2_sm", "beta_l_age2_sf"):
                est = a(b + "estimate", "f4")
                se = '<span class="bound">at bound</span>'
                ci = '<span class="bound">&mdash;</span>'
                z = '<span class="bound">&mdash;</span>'
                gloss += " <b class=\"bound\">Free but boundary-active.</b>"
            else:
                est = a(b + "estimate", "f4")
                se = a(b + "se_robust", "f4")
                ci = a(b + "lo95", "f3") + " to " + a(b + "hi95", "f3")
                z = a(b + "z_robust", "f2")
            rows.append("<tr><td><code>%s</code></td><td>%s</td>"
                        '<td class="num">%s</td><td class="num">%s</td>'
                        '<td class="num">%s</td><td class="num">%s</td></tr>'
                        % (k, gloss, est, se, ci, z))
    rows.append("</tbody></table></div>")
    return "".join(rows)


BAND_LABEL = {"PT1": "short part time", "PT2": "long part time",
              "F35": "the statutory week", "FT": "standard full time",
              "LH": "long hours"}


def _hours_table():
    out = ['<div class="scroll"><table><thead><tr><th>Band</th><th>Hours</th>'
           '<th class="num">Survey</th><th class="num">Sample</th>'
           '<th class="num">Model</th><th class="num">Offer weight '
           'vs statutory</th><th class="num">Wish more hours</th>'
           '<th class="num">Mean desired hours</th>'
           '<th class="num">Desired &minus; band upper</th>'
           "</tr></thead><tbody>"]
    for sex, label in (("male", "Single men"), ("female", "Single women")):
        out.append('<tr class="grouphead"><td colspan="9">%s</td></tr>' % label)
        for band in ("PT1", "PT2", "F35", "FT", "LH"):
            b = "hours_cells.%s|%s." % (sex, band)
            out.append("<tr><td><code>%s</code> %s</td><td>%s</td>"
                       '<td class="num">%s</td><td class="num">%s</td>'
                       '<td class="num">%s</td><td class="num">%s</td>'
                       '<td class="num">%s</td><td class="num">%s</td>'
                       '<td class="num">%s</td></tr>'
                       % (band, BAND_LABEL[band],
                          a(b + "band_definition", "raw"),
                          a(b + "lfs_share_of_focal_bands", "f3"),
                          a(b + "sample_obs_share_of_focal_bands", "f3"),
                          a(b + "model_pred_share_of_focal_bands", "f3"),
                          a(b + "model_rel_opportunity_weight_vs_f35", "f3"),
                          a(b + "lfs_wish_more_share_code2_YES", "f3"),
                          a(b + "lfs_desired_hours_mean", "f1"),
                          a(b + "lfs_excess_over_band_upper", "sf1")))
    out.append("</tbody></table></div>")
    return "".join(out)


def sections(F):
    _AUX = aux_data()
    _J = json.loads(NOR_PATH.read_text(encoding="utf-8"))["entries"]
    H = []
    W = H.append

    # ===================================================================== 7 ==
    W('<h2 id="s7" class="exempt">7. The estimated model, coefficient by '
      "coefficient</h2>")

    W('<p class="lede">Both applications of section&nbsp;6, side by side, block by '
      'block. Every coordinate carries a reading in economic units, because a '
      'coefficient in a log-density or inside a Box&ndash;Cox transformation is '
      'not interpretable at sight.</p>')

    W("<p>The single-adult model estimates "
      + n("n_params_active", "int") + " coordinates, of which "
      + n("n_params_interior", "int") + " are interior at the optimum and "
      + n("n_params_at_bound", "int") + " rest on an active bound; the couple "
      "model estimates " + n("n_couples_free", "int") + ", of which "
      + n("n_couples_interior", "int") + " are interior and "
      + n("n_couples_at_bound", "int") + " on a bound. At those optima the "
      "<b>" + lit("singles final model negLL 18022.764617170084",
                  "the canonical full-precision label of the singles negative "
                  "log-likelihood; the bound rendering follows")
      + "</b> and the <b>"
      + lit("couples clean baseline negLL 43493.342239066726",
            "the canonical full-precision label of the couples negative "
            "log-likelihood; the bound rendering follows")
      + "</b>. Both are <b>negative log-likelihoods</b> &mdash; positive numbers, "
      "because the sign is flipped &mdash; rendered here as "
      + n("negll_singles_final", "f4") + " and "
      + n("negll_couples_final", "f4") + ". A negLL is a badness-of-fit score: "
      "lower is better, and only differences between models on the same data "
      "mean anything.</p>")

    W(box("key", "How to read these tables",
          "<p><b>The standard errors.</b> Every standard error here is "
          "<b>clustered on the household</b>. A household contributes "
          + n("n_alternatives", "int") + " rows to the likelihood &mdash; its "
          "observed job and the drawn alternatives &mdash; and those rows are "
          "not independent of one another: they share the household's "
          "circumstances, its budget and its draws. Clustering allows the "
          "disturbances within a household to be correlated in an arbitrary way, "
          "and only assumes independence <em>across</em> households. The "
          "sandwich carries a finite-sample correction of "
          + imath(r"G/(G-K)") + ", where " + imath("G") + " is the number of "
          "households and " + imath("K") + " the number of coordinates that "
          "inference is taken over &mdash; "
          + n("n_households_singles", "int") + " and "
          + n("n_params_interior", "int") + " for the single-adult model, "
          + n("n_couples_clusters", "int") + " and "
          + n("n_couples_K_interior", "int") + " for the couple model.</p>"
          "<p><b>The reading column.</b> Where a coefficient sits inside a log "
          "density, " + imath(r"e^{\beta}") + " is a <b>ratio of availability</b> "
          "against the reference category, and that is how it is reported. Where "
          "it sits in the centre of the log wage-offer distribution, it is "
          "reported as a <b>percentage difference</b> in that centre. Where it is "
          "a curvature or a normalisation, the column says what it does and, if "
          "it has no standalone magnitude, says that instead.</p>"
          "<p><b>Two coordinates carry no standard error</b>, in the single-adult "
          "model, and one in the couple model. They rest on an <b>active bound</b> "
          "&mdash; the optimiser was free to move them and came to rest against "
          "the edge of the admissible region, where the usual sampling "
          "distribution does not apply. They are marked, and the boxes above "
          "explain what that costs.</p>"))

    def _sing(k, fmt="f4"):
        return a("params41." + k + ".estimate", fmt)

    def _singse(k):
        r = _AUX["params41"].get(k)
        if r is None:
            return '<span class="bound">&mdash;</span>'
        if r.get("at_active_bound"):
            return '<span class="bound">at bound</span>'
        return a("params41." + k + ".se_robust", "f4")

    def _cpl(k, fmt="f4"):
        return n("couples_param_" + k + "__estimate", fmt)

    def _cplse(k):
        e = _J.get("couples_param_" + k + "__se_robust")
        if e is None:
            return '<span class="bound">&mdash;</span>'
        if isinstance(e.get("value"), str):
            return '<span class="bound">at bound</span>'
        return n("couples_param_" + k + "__se_robust", "f4")

    DASH = '<td class="num">&mdash;</td><td class="num">&mdash;</td>'

    def row(label, sk, ck, reading):
        """One coordinate: singles cell pair, couples cell pair, reading."""
        cells = ""
        if sk:
            cells += ('<td class="num">' + _sing(sk) + "</td>"
                      '<td class="num">' + _singse(sk) + "</td>")
        else:
            cells += DASH
        if ck:
            cells += ('<td class="num">' + _cpl(ck) + "</td>"
                      '<td class="num">' + _cplse(ck) + "</td>")
        else:
            cells += DASH
        return ("<tr><td><code>" + label + "</code></td>" + cells
                + "<td>" + reading + "</td></tr>")

    def head(title):
        return ('<tr class="grouphead"><td colspan="6">%s</td></tr>' % title)

    W('<div class="scroll"><table><thead>'
      '<tr><th rowspan="2">Coordinate</th>'
      '<th class="num" colspan="2">Single adult</th>'
      '<th class="num" colspan="2">Couple</th>'
      '<th rowspan="2">What this number means</th></tr>'
      '<tr><th class="num">Estimate</th><th class="num">Std. error</th>'
      '<th class="num">Estimate</th><th class="num">Std. error</th></tr>'
      "</thead><tbody>"

      # ------------------------------------------------ preferences, male
      + head("Preferences &mdash; the value of time, men")
      + row("beta_l0", "beta_l0_sm", "beta_l0_m",
            "The <b>level of the leisure weight</b> for a man at the centre of "
            "the age range and with no children. It multiplies transformed "
            "leisure in utility. It is not a price or an MRS. A local consumption "
            "compensation slope also depends on both curvatures, both scales, "
            "consumption and leisure. On its own it is not comparable across the two "
            "models, because each is read against its own leisure curvature.")
      + row("beta_l_age", "beta_l_age_sm", "beta_l_age_m",
            "The <b>slope of the age profile</b> of the value of time, per decade "
            "of age from the centre. Read it with the row below rather than "
            "alone: together the two trace a curve, and the curve is what has "
            "economic content.")
      + row("beta_l_age2", "beta_l_age2_sm", "beta_l_age2_m",
            "The <b>curvature of that age profile</b>. In the single-adult model "
            "this coordinate rests on an <b>active bound</b> and carries no "
            "standard error; the implied profile is U-shaped in age with an "
            "interior minimum around forty, which section&nbsp;19 plots and "
            "tests. A positive value means the value of time is highest at the "
            "ends of the working life and lowest in the middle of it.")
      + row("theta_l", "theta_l_sm", "theta_l_m",
            "The <b>concavity of leisure</b>. Strongly negative in both models: "
            "the marginal value of an extra hour of time falls off sharply, so "
            "the tenth hour of leisure in a week is worth far less than the "
            "first. This is what stops the model from predicting that everyone "
            "either works nothing or works the maximum.")

      # ---------------------------------------------- preferences, female
      + head("Preferences &mdash; the value of time, women")
      + row("beta_l0", "beta_l0_sf", "beta_l0_f",
            "The level of the leisure weight for a woman, on the same reading as "
            "the male row above.")
      + row("beta_l_age", "beta_l_age_sf", "beta_l_age_f",
            "The slope of the female age profile, per decade.")
      + row("beta_l_age2", "beta_l_age2_sf", "beta_l_age2_f",
            "The curvature of the female age profile. In the single-adult model "
            "this too rests on an <b>active bound</b> and carries no standard "
            "error.")
      + row("beta_l_nkids", "beta_l_nkids_sf", "beta_l_nkids_f",
            "The <b>shift in the value of time per resident child</b>, for women "
            "only. One additional model-defined child changes the additive leisure-"
            "weight index by " + a("params41.beta_l_nkids_sf.estimate", "f4")
            + " model units in singles; exponentiating it is a formula error. At the "
            "single-female reference index, the profile-specific proportional change "
            "is about twenty-seven and a half per cent, not an elasticity. The couple "
            "estimate has the opposite sign and is imprecise. The singles estimate "
            "is marginal rather than comfortably precise "
            "inside it. There is <b>no male counterpart</b> in either model; "
            "section&nbsp;12 gives the test, the exposure and the reason.")
      + row("theta_l", "theta_l_sf", "theta_l_f",
            "The concavity of leisure for women, on the same reading as the male "
            "row.")

      # ------------------------------------------------ consumption curvature
      + head("Consumption curvature")
      + row("theta_c", "theta_c_singles", None,
            "The <b>concavity of consumption</b>: how fast the marginal value of "
            "an extra euro falls as income rises. Comfortably inside the unit "
            "interval, so marginal utility of income declines but does not "
            "collapse &mdash; well away from both the linear case and the "
            "logarithmic one. It governs the whole income&ndash;time trade-off, "
            "and therefore the money metric of section&nbsp;13. It is "
            "<b>maintained common across the sexes by construction</b> and was "
            "never tested sex-specifically: see the note below. In the couple "
            "model consumption enters logarithmically under the same restriction, so "
            "there is no coordinate to report.")

      # ----------------------------------------------------- employment access
      + head("Employment access &mdash; is work available at all?")
      + row("beta_E", "beta_E", None,
            "The <b>level of the employment margin</b>: how much offer density "
            "sits on working packages against the non-employment package, for a "
            "household in the reference region and zone. Strongly negative, so "
            "any one working package is much less available than not working "
            "&mdash; which is the offer-side counterpart of a fixed cost of "
            "work. It is <b>not</b> a probability of employment; that is a "
            "property of the whole density, and section&nbsp;9 compares it with "
            "the observed employment rate.")
      + row("beta_E_m", None, "beta_E_m",
            "The same level for the man in a couple. The couple model estimates "
            "it per spouse, because the participation margin differs sharply by "
            "sex.")
      + row("beta_E_f", None, "beta_E_f",
            "The same level for the woman in a couple.")
      # ------------------------------------------- geography and local market
      + head("Geography and the local labour market &mdash; how access is tilted")
      + row("beta_E_gsur", "beta_E_gsur", "beta_E_gsur",
            "The <b>group unemployment rate</b>: the rate for the household's own "
            "region, education and sex. This is the sharpest access coefficient "
            "in the model. The executed regressor is ten times the underlying rate. "
            "With the singles coefficient, a one-percentage-point increase multiplies "
            "the relative working-opportunity factor by about "
            + lit("0.8823", "derived from the extracted coefficient and executed scale")
            + ", an approximately eleven-point-eight-per-cent change in that factor, "
            "not an eleven-point-eight-percentage-point employment change. The full "
            "choice implication requires normalisation and utility. The same factor-ten "
            "transform is independently present in the clean-couples specification.")
      + row("beta_E_drgn2", "beta_E_drgn2", "beta_E_drgn2",
            "A <b>region indicator</b>, against the omitted region, once the "
            "continuous unemployment rate is already in. Multiplies working "
            "availability by " + a("ratio.beta_E_drgn2.exp", "f2") + ". None of "
            "the seven region indicators has an interval excluding zero: "
            "geography enters through the <em>rate</em> rather than through the "
            "zone, which is a finding rather than a failure.")
      + row("beta_E_drgn3", "beta_E_drgn3", "beta_E_drgn3",
            "Region indicator; availability ratio "
            + a("ratio.beta_E_drgn3.exp", "f2") + ".")
      + row("beta_E_drgn4", "beta_E_drgn4", "beta_E_drgn4",
            "Region indicator; availability ratio "
            + a("ratio.beta_E_drgn4.exp", "f2") + ".")
      + row("beta_E_drgn5", "beta_E_drgn5", "beta_E_drgn5",
            "Region indicator; availability ratio "
            + a("ratio.beta_E_drgn5.exp", "f2") + ".")
      + row("beta_E_drgn6", "beta_E_drgn6", "beta_E_drgn6",
            "Region indicator; availability ratio "
            + a("ratio.beta_E_drgn6.exp", "f2") + ".")
      + row("beta_E_drgn7", "beta_E_drgn7", "beta_E_drgn7",
            "Region indicator; availability ratio "
            + a("ratio.beta_E_drgn7.exp", "f2") + ".")
      + row("beta_E_drgn8", "beta_E_drgn8", "beta_E_drgn8",
            "Region indicator; availability ratio "
            + a("ratio.beta_E_drgn8.exp", "f2") + ".")
      + row("beta_E_drgur", "beta_E_drgur", "beta_E_drgur",
            "<b>Urban</b> against rural residence: availability ratio "
            + a("ratio.beta_E_drgur.exp", "f2") + ". Indistinguishable from one, "
            "again because the unemployment rate already carries the local "
            "market.")
      + row("beta_E_drgmd", "beta_E_drgmd", "beta_E_drgmd",
            "<b>Intermediate</b> zone against rural: availability ratio "
            + a("ratio.beta_E_drgmd.exp", "f2") + ".")

      # ------------------------------------------------------------- hours
      + head("Hours &mdash; at which lengths of week is work available?")
      + row("beta_h_pt1", "beta_h_pt1", "beta_h_pt1_m",
            "<b>Short part time</b> against the hours regions the bands do not "
            "cover: " + a("ratio.beta_h_pt1.exp", "f2") + " times as much offer "
            "density. Short part-time work is thin on the ground, which is the "
            "offer-side reading of a fact the descriptive hours distribution "
            "shows directly.")
      + row("beta_h_pt2", "beta_h_pt2", "beta_h_pt2_m",
            "<b>Long part time</b>: " + a("ratio.beta_h_pt2.exp", "f2")
            + " times the uncovered region.")
      + row("beta_h_ft", "beta_h_ft", "beta_h_ft_m",
            "<b>Above-statutory full time</b>: "
            + a("ratio.beta_h_ft.exp", "f1") + " times the uncovered region. "
            "This and the peak below are where the offer density concentrates.")
      + row("beta_h_lh", "beta_h_lh", "beta_h_lh_m",
            "<b>Long hours</b>: " + a("ratio.beta_h_lh.exp", "f2")
            + " times the uncovered region. Long-hours jobs are scarcer than "
            "full-time ones on the offer side, so the model does not explain "
            "long hours by a taste for work alone.")
      + row("beta_h_pt1_f", None, "beta_h_pt1_f",
            "The same short part-time coordinate for the woman in a couple. The "
            "couple model estimates the whole hours profile per spouse.")
      + row("beta_h_pt2_f", None, "beta_h_pt2_f",
            "Long part time, woman in a couple.")
      + row("beta_h_ft_f", None, "beta_h_ft_f",
            "Above-statutory full time, woman in a couple.")
      + row("beta_h_lh_f", None, "beta_h_lh_f",
            "Long hours, woman in a couple.")

      # -------------------------------------------------------- the 35h peak
      + head("The statutory-week peak")
      + row("beta_h_f35", "beta_h_f35", "beta_h_f35_m",
            "The <b>institutionally motivated opportunity peak</b>: a separate "
            "continuous density elevation over the narrow "
            + imath(r"[33.5,36.5)") + " hours band, not an atom at exactly thirty-five. In the "
            "single-adult model the fitted density height of "
            "<em>available</em> packages is <b>"
            + a("ratio.beta_h_f35.exp", "f1")
            + " times higher</b> in that band than in the uncovered hours region. "
            "Integrated mass also depends on band width. It is the single largest specification improvement in "
            "the paper. It is <b>not</b> an estimate of the causal effect of the "
            "statute: no counterfactual removing the statute is computed "
            "anywhere, and section&nbsp;14.4 states that placing this feature in "
            "the offer density rather than in preferences is a modelling choice "
            "the data do not adjudicate.")
      + row("beta_h_f35_f", None, "beta_h_f35_f",
            "The same peak for the woman in a couple. That the peak appears "
            "separately for each spouse, on data the single-adult model never "
            "saw, is corroboration of the institutional reading.")

      # ------------------------------------------------------- occupation
      + head("Occupation availability &mdash; which kinds of job are reachable?")
      + row("beta_occ_2_m", "beta_occ_2_m", "beta_occ_2_m",
            "Occupation group " + lit("2", "an occupation group label") + " against group " + lit("1", "an occupation group label")
            + ", <b>men</b>: "
            + a("ratio.beta_occ_2_m.exp", "f2") + " times as reachable. Large "
            "and precisely estimated &mdash; the occupation margin is where the "
            "sharpest sex differences in this model sit.")
      + row("beta_occ_3_m", "beta_occ_3_m", "beta_occ_3_m",
            "Group " + lit("3", "an occupation group label") + " against group " + lit("1", "an occupation group label") + ", men: " + a("ratio.beta_occ_3_m.exp", "f2")
            + " times as reachable.")
      + row("beta_occ_4_m", "beta_occ_4_m", "beta_occ_4_m",
            "Group " + lit("4", "an occupation group label") + " against group " + lit("1", "an occupation group label") + ", men: " + a("ratio.beta_occ_4_m.exp", "f2")
            + " times as reachable &mdash; that is, indistinguishable from "
            "equally reachable.")
      + row("beta_occ_2_f", "beta_occ_2_f", "beta_occ_2_f",
            "Group " + lit("2", "an occupation group label") + " against group " + lit("1", "an occupation group label")
            + ", <b>women</b>: "
            + a("ratio.beta_occ_2_f.exp", "f2") + ".")
      + row("beta_occ_3_f", "beta_occ_3_f", "beta_occ_3_f",
            "Group " + lit("3", "an occupation group label") + " against group " + lit("1", "an occupation group label") + ", women: "
            + a("ratio.beta_occ_3_f.exp", "f2") + ".")
      + row("beta_occ_4_f", "beta_occ_4_f", "beta_occ_4_f",
            "Group " + lit("4", "an occupation group label") + " against group " + lit("1", "an occupation group label") + ", women: "
            + a("ratio.beta_occ_4_f.exp", "f2") + " times as reachable. The "
            "contrast with the male coefficient on the same group is the "
            "occupation-access sex difference the model identifies.")

      # ----------------------------------------------------- wage offers
      + head("Earning opportunities &mdash; where the wage-offer distribution sits")
      + row("beta_w0", "beta_w0", "beta_w0",
            "The <b>intercept of the log wage-offer centre</b>, at middle "
            "education, occupation group " + lit("1", "an occupation group label") + " and the origin "
            "of the experience "
            "profile. On its own it locates the distribution; it has no "
            "standalone economic reading, and the rows below are read against "
            "it.")
      + row("beta_w_educL", "beta_w_educL", "beta_w_educL",
            "<b>Low education</b> against the middle group: the centre of the "
            "wage-offer distribution differs by "
            + a("ratio.beta_w_educL.pct", "sf1") + "&nbsp;per cent at the same "
            "experience and occupation. Small and imprecise.")
      + row("beta_w_educH", "beta_w_educH", "beta_w_educH",
            "<b>High education</b> against the middle group: "
            + a("ratio.beta_w_educH.pct", "sf1") + "&nbsp;per cent on the centre "
            "of the offer distribution, at the same experience and occupation. "
            "This is a statement about <em>observed earning capacity</em>, not "
            "about ability, and section&nbsp;14.4 keeps the two apart.")
      + row("beta_w_pexp", "beta_w_pexp", "beta_w_pexp",
            "The <b>linear experience term</b> in the offer centre. Read with "
            "the square below: together they trace a profile that rises and then "
            "flattens, which is the standard shape and a check that the offer "
            "density is behaving sensibly.")
      + row("beta_w_pexp2", "beta_w_pexp2", "beta_w_pexp2",
            "The <b>square of experience</b>, giving the profile its concavity. "
            "In the couple model this coordinate rests on an <b>active bound</b> "
            "and carries no standard error.")
      + row("sigma", "sigma", "sigma",
            "The <b>spread of the wage-offer distribution</b>, common to every "
            "household. A log-scale standard deviation of about "
            + _sing("sigma", "f2") + " means the offer distribution around its "
            "centre is wide: pay is genuinely uncertain conditional on "
            "education, experience and occupation, which is precisely why the "
            "model treats it as a density rather than a number.")

      # ------------------------------------------ occupation wage location
      + head("Occupation wage location &mdash; what each kind of job pays")
      + row("delta_occ_2", "delta_occ_2", "delta_occ_2",
            "Occupation group " + lit("2", "an occupation group label") + " against group " + lit("1", "an occupation group label") + ": "
            + a("ratio.delta_occ_2.pct", "sf1") + "&nbsp;per cent on the centre "
            "of the wage-offer distribution, at the same education and "
            "experience. <b>Not</b> a causal occupational premium: it is where "
            "that group's offer distribution sits.")
      + row("delta_occ_3", "delta_occ_3", "delta_occ_3",
            "Group " + lit("3", "an occupation group label") + " against group " + lit("1", "an occupation group label") + ": " + a("ratio.delta_occ_3.pct", "sf1")
            + "&nbsp;per cent on the offer centre.")
      + row("delta_occ_4", "delta_occ_4", "delta_occ_4",
            "Group " + lit("4", "an occupation group label") + " against group " + lit("1", "an occupation group label") + ": " + a("ratio.delta_occ_4.pct", "sf1")
            + "&nbsp;per cent on the offer centre. Together with the occupation "
            "<em>access</em> rows above, this is what lets the model say that a "
            "group is better paid and no easier to enter &mdash; the "
            "distinction a single occupation coefficient cannot make.")

      + "</tbody></table></div>")

    # -------------------------------------------- the two maintained points
    W("<h3>The restrictions the tables carry, stated rather than buried</h3>")

    W(box("warn", "The two boundary-active coordinates, and what the bound costs",
          "<p>The quadratic age terms in both single-adult leisure weights are "
          "<b>free parameters that came to rest on an active bound</b> at the "
          "optimum. They were not pinned and were not fixed by hand: the "
          "optimiser could move them and did not. A coordinate at a bound has no "
          "usual sampling distribution, which is why the standard-error cells "
          "are empty rather than large.</p>"
          "<p>Section&nbsp;19's diagnostic answers what that costs. The "
          "admissible region on the four quadratic-age coordinates is widened by "
          "a factor of <b>five</b> on half-widths ("
          + lit("linear from &plusmn;5 to &plusmn;25, quadratic from &plusmn;1 "
                "to &plusmn;5", "the declared admissible box of the diagnostic, "
                "a design constant")
          + "), nothing else changes, and the <b>bounds disappear</b>: the active "
          "set goes from " + n("n_params_at_bound", "int") + " to zero and all "
          + n("n_params_active", "int") + " coordinates become interior. The "
          "objective improves by only <b>&Delta;negLL "
          + a("agebound.delta_negll", "f3") + "</b>, so &Delta;AIC = &Delta;BIC = "
          + a("agebound.delta_aic", "sf3") + " &mdash; and because the two "
          "specifications have the same free coordinates and differ only by the "
          "admissible region, that is <em>not</em> a chi-square statistic and no "
          "<em>p</em>-value is quoted. The freed coordinates land at "
          + a("agebound.released_m", "f3") + " for men, interval "
          + a("agebound.ci_m", "range") + ", and "
          + a("agebound.released_f", "f3") + " for women, "
          + a("agebound.ci_f", "range") + " &mdash; and the bound value "
          + lit("+1.0", "the box ceiling of record, a design constant")
          + " lies <b>inside both</b>. This widened-bound re-estimation is the relevant "
          "sensitivity. A change of leisure units does not make boundary activity "
          "disappear: a true reparameterisation must transform the admissible set too. "
          "The earlier reported values " + a("agebound.lambda40_m", "f3") + " and "
          + a("agebound.lambda40_f", "f3") + " are therefore not evidence of "
          "interiority and carry no inferential verdict here.</p>"
          "<p><b>The verdict is to retain the specification reported here, and "
          "the margin is close.</b> The widened box fails the limb that asks for "
          "a materially better objective. The bound binds on a curvature the "
          "data do not pin down, and releasing it moves no coefficient this "
          "report interprets by as much as one standard error.</p>"))

    W(box("warn", "The consumption curvature is maintained common, not tested",
          "<p><b>" + imath(r"\theta_c") + " is shared by the two sexes by "
          "construction of the specification</b>, and no sex-specific "
          "alternative was ever estimated against it. Two reasons hold it "
          "common, and both are maintained reference choices rather than findings.</p>"
          "<ul>"
          "<li><b>The scale numeraire.</b> Utility in a discrete-choice model is "
          "identified only up to scale, and the consumption coefficient is what "
          "fixes that scale. The consumption block therefore carries the units of "
          "the money metric, and splitting its curvature by sex would split the "
          "metric itself &mdash; men and women would be measured on differently "
          "curved euro scales.</li>"
          "<li><b>Parsimony.</b> A sex-specific consumption curvature was never "
          "proposed in the specification search, so it was <b>never tested</b>. "
          "The estimate in the table is a level, not evidence for pooling.</li>"
          "</ul>"
          "<p>This is the untested assumption closest to the headline, because "
          "the money metric of section&nbsp;13 is obtained by <em>inverting the "
          "consumption block</em>: a curvature that differed by sex would move "
          "the welfare measure for men and for women by different amounts, and "
          "so would move the preference/environment split through the same "
          "channel as the reference choice. Section&nbsp;20 carries it as a "
          "named candidate sensitivity.</p>"))

    W(F.fig("figAB01_leisure_weight_by_age",
            "The estimated value of time as a profile over age, by sex &mdash; "
            "the age coefficients of the first two blocks read as a curve rather "
            "than as numbers. Strictly positive across the working ages and "
            "U-shaped, with an interior minimum around forty."))
    W(F.fig("figAB02_mrs_by_age_sex",
            "The same preferences read as a price: the consumption a household "
            "would need to be given to stay as well off after one more hour of "
            "work a week, by age and sex. This is the leisure block in euros, "
            "which is the form the money metric of section&nbsp;13 uses."))

    W("<p>Three consequences, all of which get asked:</p>")
    W("<ul>")
    W("<li><b>They carry no standard error.</b> The usual asymptotic argument needs an "
      "interior optimum. At a bound the sampling distribution is not asymptotically "
      "normal, so reporting an interval would be wrong rather than merely "
      "conservative. That is why the table shows a dash.</li>")
    W("<li><b>They are excluded from the inference dimension.</b> The finite-sample "
      "correction on the clustered sandwich uses the interior count, "
      + n("n_params_interior", "int") + ", not the free count, "
      + n("n_params_active", "int") + ". Using the free count instead inflates every "
      "robust standard error slightly and changes no significance verdict.</li>")
    W("<li><b>They are held fixed during resampling.</b> When parameter uncertainty is "
      "propagated into the welfare results (section&nbsp;19), the boundary-active pair "
      "is held at its point estimate and the interior "
      + n("n_params_interior", "int") + " are drawn.</li>")
    W("</ul>")
    W("<p>Economically, a leisure weight whose age curvature sits on its bound means "
      "the data want <em>at least</em> that much curvature in the age profile and the "
      "box will not let them have more. Section&nbsp;19 reports the diagnostic that "
      "widened the box to test exactly this.</p>")

    W(F.fig("fig08_coefficients_by_block",
            "The estimated coefficients grouped by economic block, with robust "
            "clustered intervals. The access and wage blocks are tightly estimated; the "
            "leisure block is the wide one, which is the honest shape of this "
            "identification problem and is discussed in section&nbsp;19."))

    W(box("prov", "Technical provenance: why some documents say fifty-one",
          "<p>The parameter vector has two representations and both appear in the "
          "project record.</p>"
          "<ul>"
          "<li><b>" + n("n_params_active", "int") + " &mdash; the active "
          "representation.</b> The coordinates the singles likelihood actually consumes. "
          "This is the representation used everywhere in this document, and the one "
          "whose count enters information criteria.</li>"
          "<li><b>" + n("n_params_provenance", "int") + " &mdash; the provenance "
          "vector.</b> " + n("n_params_active", "int") + " active coordinates plus ten "
          "that are dropped or pinned and never consumed by the singles branches: eight "
          "inactive couples coordinates carried in the shared parameter block, and two "
          "pinned year effects retained as fixed parameters because the frame is a "
          "single year and they are identically zero on it.</li>"
          "</ul>"
          "<p>The two forms give <b>bitwise identical</b> objective and gradient values. "
          "The active form is not an approximation of the long form; it is the long form "
          "with provably inert coordinates removed. A third figure, thirty-five, appears "
          "in one earlier planning document and is <b>not reproducible from anything on "
          "disk</b>; it was returned rather than adopted, and no result in this document "
          "rests on it. For inference the operative constant is the interior count, "
          + n("n_params_interior", "int") + ".</p>"))

    # ===================================================================== 8 ==
    W('<h2 id="s8" class="exempt">8. How this specification was reached</h2>')
    W("<p>The specification was not chosen in one step, and the rejected variants are "
      "more informative than the accepted one. What follows is the scientific "
      "chronology with the economic reason in each case.</p>")

    W("<h3>Stage 1 &mdash; the base random-utility, random-opportunity model</h3>")
    W("<p>The starting point is a labour-supply model with a preference block over "
      "consumption and leisure and an opportunity block over employment, hours and "
      "occupation, with the budget solved exactly by the tax-benefit simulator. This "
      "delivers a working model and a defensible fit on employment and occupation, and "
      "one conspicuous failure: it cannot reproduce the shape of the hours "
      "distribution.</p>")

    W("<h3>Stage 2 &mdash; enriching the opportunity side</h3>")
    W("<p>Circumstances were added to the access block: the local unemployment rate, "
      "region and urbanisation. The economic argument is that these shift what is "
      "available and have no business in a utility function. Empirically the local "
      "unemployment rate is the strongest single access regressor in the finished "
      "model, and the exclusion is what makes the geographic decomposition of "
      "section&nbsp;17 meaningful rather than circular.</p>")

    W("<h3>Stage 3 &mdash; the exact proposal correction</h3>")
    W("<p>The hours-mixture correction of section&nbsp;5. This is a correctness fix, "
      "not a specification choice: the earlier implementation optimised a likelihood in the "
      "labelled space rather than the job space. Everything downstream is on the "
      "corrected rule, and pre-correction results are retained as history rather "
      "than compared against.</p>")

    W("<h3>Stage 4 &mdash; occupation-conditioned wage shifts</h3>")
    W("<p>Initially the wage-offer location did not depend on occupation, which forces "
      "an economically false restriction: every occupation pays the same conditional on "
      "schooling and experience. Adding occupation-specific location shifts on a common "
      "dispersion separates <em>what a group pays</em> from <em>whether it can be "
      "entered</em>. Both are needed &mdash; a group can be well paid and hard to reach, "
      "and that combination is precisely what an opportunity model should be able to "
      "say. The occupation access and wage-location blocks remain jointly "
      "well-conditioned once both are present, so the two are separately identified "
      "rather than trading off.</p>")

    W("<h3>Stage 5 &mdash; the statutory-week peak, and why it was retained</h3>")
    W("<p>This is the decisive step. Adding a single coefficient for the statutory "
      "hours band buys <b>" + a("chron.peak_negll_gain", "f1")
      + "</b> in negLL &mdash; the negative log-likelihood falls by that much "
      "&mdash; for <b>one</b> degree of freedom, and repairs the "
      "model&rsquo;s largest failure directly:</p>")
    W('<div class="scroll"><table><thead><tr><th>Statutory-band share</th>'
      '<th class="num">Without the peak</th><th class="num">With the peak</th>'
      '<th class="num">Observed</th></tr></thead><tbody>'
      "<tr><td>Predicted share of employed at the statutory week</td>"
      '<td class="num">' + a("chron.f35_share_without_peak", "f3") + "</td>"
      '<td class="num">' + a("chron.f35_share_with_peak", "f3") + "</td>"
      '<td class="num">' + a("chron.f35_share_observed", "f3") + "</td></tr>"
      "<tr><td>Hours-grid mean absolute error</td>"
      '<td class="num">' + a("chron.hours_grid_mae_without_peak", "f4") + "</td>"
      '<td class="num">' + a("chron.hours_grid_mae_with_peak", "f4") + "</td>"
      '<td class="num">&mdash;</td></tr>'
      "</tbody></table></div>")
    W("<p><b>The economic interpretation is maintained, not non-parametrically "
      "proved.</b> The elevated density covers the continuous narrow interval "
      + imath(r"[33.5,36.5)") + ", not a point mass. Its concentration supports the "
      "relevance of an institutional hours feature, but the choice data do not prove "
      "that the whole feature belongs to offers rather than tastes. The model assigns "
      "it to opportunities and discloses that channel choice.</p>")
    W("<p>It is also the <em>most parsimonious</em> admitted extension, not the "
      "richest: it costs exactly one free coefficient over the nested benchmark, and it "
      "is the only variant in the whole search whose robust intervals all stay clear of "
      "their bounds.</p>")

    W("<h3>Stage 6 &mdash; the five-hour support correction</h3>")
    W("<p>The corrected employed support begins at "
      + lit("5", "hours floor of the corrected support") + " hours per week. The "
      "historical repair did not newly remove benefit-dominated near-zero jobs: it "
      "preserved the actual six-to-nine-hour observations of seven chosen workers that "
      "an older construction had floored at ten. The repair required re-pricing and "
      "re-estimation and defines the frame for every current result.</p>")

    W("<h3>The variants that were tried and rejected</h3>")
    W("<p>Each of these was estimated. Each was rejected on economic and empirical "
      "grounds, not dropped.</p>")
    W('<div class="scroll"><table><thead><tr><th>Variant</th>'
      "<th>Economic idea</th><th>Why it was rejected</th></tr></thead><tbody>"

      "<tr><td><b>Re-centring the age profile</b></td>"
      "<td>Recentre the leisure-weight age polynomial so its intercept sits at the "
      "youngest age in the sample rather than at zero.</td>"
      "<td><b>Exactly equivalent, so uninformative.</b> Once the admissible box is "
      "carried through the same transformation the model is the identical model, "
      "reproducing the objective to machine precision. Retained as an invariance check "
      "&mdash; useful evidence the estimator is not sensitive to arbitrary "
      "normalisation &mdash; not as a candidate.</td></tr>"

      "<tr><td><b>Relocating the age bound</b></td>"
      "<td>Move the admissible region for the age terms so the quadratic is not "
      "boundary-active.</td>"
      "<td><b>It relocates the problem rather than solving it.</b> The quadratic leaves "
      "its bound but both linear age terms then arrive at the translated floor, and the "
      "total likelihood gain is under two units for no change in dimension. The data "
      "want a particular amount of age curvature and the box is not the reason.</td></tr>"

      "<tr><td><b>A child-count term for single men</b></td>"
      "<td>Let dependent children shift the male leisure weight as they do the "
      "female one.</td>"
      "<td><b>No signal, and both information criteria penalise it.</b> The coefficient "
      "is statistically indistinguishable from zero at <em>z</em> = "
      + a("chron.male_child_z", "f2") + ", its interval touches its bound, and the "
      "Akaike criterion worsens. Substantively this is unsurprising: single fathers are "
      "a small and selected group in this sample. Section&nbsp;12.</td></tr>"

      "<tr><td><b>Education-interacted wage opportunities</b></td>"
      "<td>Let the schooling return differ by group rather than being a common "
      "shift.</td>"
      "<td><b>The new degree of freedom is not supported.</b> The interaction enters at "
      "<em>z</em> = " + a("chron.wage_edu_interaction_z", "f2")
      + ", and the Bayesian criterion moves the wrong way under both reference definitions. The "
      "richer wage location does not buy anything the common shift does not already "
      "deliver.</td></tr>"

      "<tr><td><b>Sex-specific hours-opportunity coefficients</b></td>"
      "<td>Let men and women face different hours-band offer densities.</td>"
      "<td><b>The two criteria disagree and nothing else moves.</b> Akaike rejects, "
      "Bayes marginally favours, and no other coefficient in the model responds. A "
      "specification change that no substantive quantity notices is not a specification "
      "improvement.</td></tr>"

      "<tr><td><b>Per-sex occupation preference shifters</b></td>"
      "<td>Let occupation enter tastes, not only access.</td>"
      "<td><b>Opposite-signed, insignificant, and boundary-touching.</b> The male and "
      "female shifters come out with opposite signs, neither is estimated precisely, "
      "significance, and both intervals touch their bounds. The Bayesian penalty is "
      "large. Retained as a diagnostic only.</td></tr>"

      "<tr><td><b>An additive hours term in the wage location</b></td>"
      "<td>Let the wage offer depend on hours as well as occupation.</td>"
      "<td><b>Supported by the likelihood, rejected on fit.</b> It is likelihood- and "
      "Akaike-favoured but Bayes-penalised, and it <em>degrades</em> five of seven fit "
      "metrics. Its two largest interaction coefficients rest on a handful of "
      "households. It also fails to repair the misfit it was proposed for &mdash; the "
      "bottom wage quintile, which stays over-predicted by roughly "
      + a("chron.wage_q1_over_prediction_pp", "f1") + " percentage points under every "
      "specification tried. That residual misfit is an acknowledged open item.</td></tr>"

      "<tr><td><b>Splitting couples&rsquo; access coefficients by sex</b></td>"
      "<td>Let the employment and hours access blocks differ between husbands and "
      "wives.</td>"
      "<td><b>Likelihood-favoured but not recoverable.</b> A likelihood-ratio test "
      "rejects pooling, but on synthetic data generated from the split model itself the "
      "split coefficients do not come back: one of them recovers with the wrong sign "
      "and a tight standard error. A likelihood-ratio rejection of pooling is "
      "<em>not</em> evidence that the split is identified, and this is the clearest "
      "example of that in the project.</td></tr>"
      "</tbody></table></div>")

    W("<h3>The three attempts at persistent unobserved heterogeneity</h3>")
    W("<p>The most substantial rejected extensions try to add unobserved heterogeneity "
      "that persists across a household&rsquo;s alternatives &mdash; the natural next "
      "step for any model of this kind. All three failed to be identified, and "
      "critically <b>they failed in three different ways</b>. One repeated mechanism "
      "would suggest a fixable defect; three distinct ones say the design is the "
      "constraint.</p>")
    W('<div class="scroll"><table><thead><tr><th>Extension</th><th>The idea</th>'
      "<th>How it failed</th></tr></thead><tbody>"

      "<tr><td><b>A random leisure intercept</b></td>"
      "<td>People differ in how much they value time, in ways not captured by age, sex "
      "and children.</td>"
      "<td><b>No leverage at all.</b> The dispersion parameter piles onto its zero "
      "bound in most replications, and the expected likelihood-ratio statistic against "
      "a true non-zero dispersion is "
      + a("chron.hp_expected_lr_at_half", "f4") + " to "
      + a("chron.hp_expected_lr_at_one", "f4") + ", against the "
      + a("chron.boundary_lr_threshold", "f3") + " a boundary test needs. The cause is "
      "the <em>loading</em>: the transformed leisure term varies by only "
      + a("chron.bc_leisure_within_set_sd_men", "f3") + " (men) and "
      + a("chron.bc_leisure_within_set_sd_women", "f3") + " (women) <em>within</em> a "
      "household&rsquo;s own choice set, against a logit error of scale one. There is "
      "almost nothing for the heterogeneity to attach to.</td></tr>"

      "<tr><td><b>An opportunity-intensity frailty</b></td>"
      "<td>Some people simply face more offers than their circumstances predict.</td>"
      "<td><b>Leverage, but no second contrast.</b> Unlike the leisure version this one "
      "does move the likelihood along its own axis ("
      + a("chron.ho_axis_lr_low", "f3") + " to " + a("chron.ho_axis_lr_high", "f3")
      + "). But refitting the rest of the model with the frailty switched off absorbs "
      "about ninety-five per cent of it, collapsing the profiled statistic to "
      + a("chron.ho_profile_lr_low", "f4") + " to " + a("chron.ho_profile_lr_high", "f4")
      + ". The reason is structural: a frailty that shifts every working alternative "
      "equally is exactly a binary mixed logit on the employment margin with one "
      "observation per household. A single binary outcome cannot separate a mean from a "
      "variance.</td></tr>"

      "<tr><td><b>Wage-residual / preference dependence</b></td>"
      "<td>People who draw better wage offers than their characteristics predict may "
      "also differ in taste &mdash; the classic selection concern.</td>"
      "<td><b>A flat ridge, not a boundary pile-up.</b> The correlation parameter runs "
      "to its box endpoint at <em>every</em> truth including zero. The interesting "
      "detail is that the economically meaningful composite is nearly unbiased but has "
      "<em>no obtainable interval</em>: the likelihood is flat along the direction that "
      "trades the two components at constant product, and the delta method needs a "
      "block that the box endpoint destroys.</td></tr>"
      "</tbody></table></div>")
    W("<p><b>What they share, and the design rule that came out of it.</b> Two of the "
      "three fail because of the same thing: what the heterogeneity loads on barely "
      "varies inside a household&rsquo;s own choice set. Making the heterogeneity "
      "observable rather than latent bought about two orders of magnitude of information "
      "&mdash; and was <em>still</em> short by a factor of two. The rule adopted is that "
      "any future heterogeneity design must be judged on the within-choice-set spread of "
      "whatever it loads on, <b>before</b> it is built.</p>")
    W("<p>A joint preference-<em>and</em>-opportunity heterogeneity model was never "
      "attempted, and deliberately so: estimating unrestricted joint preference and "
      "opportunity classes from the same choice outcomes, with no independent "
      "identification source, is not a well-posed problem. The frailty result makes that "
      "case harder, not easier.</p>")

    W(box("say", "The chronology in one sentence",
          "<p>&ldquo;The model got richer on the opportunity side, where circumstances "
          "and institutions gave it something to attach to, and every attempt to make it "
          "richer on the unobserved-heterogeneity side failed &mdash; three times, for "
          "three different reasons.&rdquo;</p>"))

    # ===================================================================== 9 ==
    W('<h2 id="s9" class="exempt">9. Does the model fit?</h2>')
    W(box("key", "Internal fit and external validation are different things",
          "<p><b>This section is internal fit</b>: the model against the sample it was "
          "estimated on. Its job is to show the specification reproduces the features it "
          "claims to explain. It cannot, by itself, be evidence the model is right &mdash; "
          "a model fits its own estimation sample partly by construction.</p>"
          "<p><b>Section&nbsp;10 is external validation</b>: the model against an "
          "independent data source that entered no likelihood, no estimation step and "
          "no merge. "
          "Keep the two apart in the talk, because conflating them invites exactly the "
          "objection you do not want.</p>"))

    W("<h3>Employment</h3>")
    W("<p>The observed employment rate in the singles sample is "
      + a("chron.employment_share_observed", "f4") + " against a predicted "
      + a("chron.employment_share_predicted", "f4") + " &mdash; well within any "
      "reasonable tolerance, and matched separately by sex.</p>")
    W(F.fig("fig03_employment_obs_vs_pred",
            "Observed and predicted employment rates, all single-adult households and "
            "by sex."))

    W("<h3>Hours, and the statutory-week mass</h3>")
    W("<p>The hours distribution is where the specification was designed to bite. The "
      "raw data show the concentration the model has to explain:</p>")
    W(F.fig("fig01_observed_hours_35h_peak",
            "Observed weekly hours among employed single-adult households, with the "
            "statutory band the peak coefficient prices. The concentration is the "
            "feature; no smooth preference specification generates it."))
    W(F.fig("fig02_hours_bands_obs_vs_pred",
            "Observed and model-implied hours-band shares. The statutory-band share is "
            "matched to within a fraction of a percentage point; without the peak "
            "coefficient the model puts roughly a fifth of the observed mass there."))

    W("<h3>Occupation</h3>")
    W("<p>Occupation shares are matched to a mean absolute error of "
      + a("chron.occ_share_mae_preferred", "f5") + " across the "
      + lit("four", "number of task-based occupation groups") + " groups.</p>")
    W(box("warn", "One honest exception, stated before anyone finds it",
          "<p>Occupation <em>hard</em> accuracy &mdash; the share of households whose "
          "single most likely occupation is the observed one &mdash; is slightly "
          "<em>worse</em> under the preferred model than under the benchmark without the "
          "peak. Every other occupation metric moves the right way: the share fit, the "
          "Brier score and probabilistic accuracy all improve.</p>"
          "<p>This is an argmax-relocation effect. Redistributing probability mass "
          "across hours bands can flip which occupation is modally most likely for a "
          "household without making the probability distribution worse &mdash; and by "
          "the calibrated measures it is better. It is reported rather than "
          "suppressed.</p>"))
    W(F.fig("fig04_occupation_obs_vs_pred",
            "Observed and model-implied occupation shares."))

    W("<h3>Wages</h3>")
    W(F.fig("fig05_wage_offer_by_occupation",
            "Fitted log-normal wage-offer densities by occupation: a common dispersion "
            "with occupation-specific locations. The separation between the groups is "
            "what the occupation wage-location shifts deliver."))
    W("<p><b>The wage block is the model&rsquo;s residual misfit and it is not "
      "repaired.</b> The bottom wage quintile is over-predicted by roughly "
      + a("chron.wage_q1_over_prediction_pp", "f1") + " percentage points, under every "
      "specification tried including the richer wage-location variants of "
      "section&nbsp;8. This is stated as an open item, not explained away.</p>")

    W("<h3>Sex differences</h3>")
    W("<p>Men and women differ in the model on both surfaces at once, and separating "
      "them is the point of the exercise. Women face a distinctly different occupation "
      "access profile &mdash; the occupation-access coefficients are estimated "
      "separately by sex and differ sharply &mdash; while the leisure weights differ in "
      "level and age profile. Section&nbsp;18 shows what happens to that decomposition "
      "when the opportunity side is removed: the estimated male&ndash;female difference "
      "in leisure valuation does not merely shrink, it <b>reverses sign</b>, from "
      + n("rum_leisure_gap_final", "sf3") + " to "
      + n("rum_leisure_gap_benchmark", "sf3") + ".</p>")

    W("<h3>Calibration and overall predictive fit</h3>")
    W("<p>The log score is " + a("chron.logscore_preferred", "f4")
      + " against " + a("chron.logscore_benchmark", "f4")
      + " for the nested benchmark without the peak.</p>")
    W(F.fig("fig07_calibration",
            "Predicted against observed shares across every diagnostic cell. Shares, "
            "not ranks: on an importance-sampled choice set of this size, chosen-row "
            "rank and top-k statistics are near-degenerate in level and not comparable "
            "across resolutions, so they are not used as fit measures."))

    W("<h3>Draw-count stability</h3>")
    W("<p>Fit and coefficients are stable in the numerical resolution. Over the ladder "
      + n("drawcount_ladder", "list") + ", the largest movement of any coefficient at or "
      "above the reference resolution is "
      + n("drawcount_max_deviation_geq_reference", "f2") + " standard errors; across the "
      "full range including the coarsest setting it is "
      + n("drawcount_max_deviation_full_range", "f2") + ". Section&nbsp;19.</p>")
    W(F.fig("figS6_06_participation_vs_draws",
            "Observed and predicted participation against the draw count, with the fit "
            "error on the participation margin."))

    # ==================================================================== 10 ==
    W('<h2 id="s10" class="exempt">10. External validation</h2>')

    W("<p>One genuinely independent source is used: the French labour force survey for "
      "the same year, "
      + n("external_validation_n_rows", "int") + " reported cells across hours bands "
      "and sex. The assembled public DADS wage benchmark is a distinct available "
      "artifact; restricted DADS/BTS microdata are not available. The two facts must "
      "not be collapsed into a claim that no wage benchmark exists.</p>")

    W(box("warn", "Validation is not identification",
          "<p><b>No moment from the labour force survey enters the likelihood.</b> It is "
          "not an instrument, it enters no estimation step, no merge and no covariate, "
      "and it does "
          "not identify preferences against opportunities. It can only show that "
          "features the estimated model prices are <em>visible in an independent "
          "source</em>. If someone asks &ldquo;what identifies the opportunity "
          "block?&rdquo; the answer is the exclusion restrictions and the functional "
          "structure of section&nbsp;6, <b>not</b> this section.</p>"))

    W("<h3>What each source validates</h3>")
    W('<div class="scroll"><table><thead><tr><th>Source</th><th>Validates</th>'
      "<th>Enters the likelihood?</th></tr></thead><tbody>"
      "<tr><td><b>Labour force survey, usual hours</b></td>"
      "<td>Hours-band composition and the concentration at the statutory week.</td>"
      '<td><span class="tag no">no</span></td></tr>'
      "<tr><td><b>Labour force survey, wish-to-work-more</b></td>"
      "<td>Whether short-hours workers report hours constraints &mdash; a direct, if "
      "imperfect, read on the model&rsquo;s central claim.</td>"
      '<td><span class="tag no">no</span></td></tr>'
      "<tr><td><b>EU-SILC estimation sample</b></td>"
      "<td>The observed side of every comparison in section&nbsp;9.</td>"
      '<td><span class="tag yes">yes &mdash; it is the sample</span></td></tr>'
      "<tr><td><b>EUROMOD</b></td>"
      "<td>The budget at every alternative.</td>"
      '<td><span class="tag yes">yes &mdash; as frozen prices</span></td></tr>'
      "</tbody></table></div>")

    W("<h3>The statutory-week concentration, three ways</h3>")
    W("<p>The independent survey puts " + n("external_validation_statutory_band_lfs", "pct", 1)
      + " of workers in the statutory band. The estimation sample has "
      + n("external_validation_statutory_band_obs", "pct", 1)
      + ", and the model predicts " + n("external_validation_statutory_band_pred", "pct", 1)
      + ". The model tracks its own sample closely, and the sample sits somewhat below "
      "the national survey figure &mdash; a sample-composition difference, since the "
      "estimation sample is single-adult households only while the survey covers "
      "everyone.</p>")
    W("<p><b>The point is the qualitative one.</b> A pronounced concentration at the "
      "statutory week is present in a survey the model never saw. That is what licenses "
      "reading the peak coefficient as an institutional feature of what is offered "
      "rather than as an accident of the fit.</p>")

    W(_hours_table())
    W(F.fig("figX1_external_hours_lfs_validation",
            "Hours-band shares: the independent labour force survey, the estimation "
            "sample, and the model. Shares are of the five priced bands, the only base "
            "on which the three sources are commensurable."))

    W("<h3>The wish-to-work-more gradient, and its caveat</h3>")
    W("<p>The survey asks employed people whether they would like to work more hours. "
      "The reported rate falls monotonically as hours rise &mdash; short-hours workers "
      "are far more likely to say yes in the coded table. This remains descriptive "
      "context because the model has no desired-hours outcome. A group mean desired "
      "hours above a band's upper edge does <em>not</em> imply that every worker in "
      "that band wants more hours, and even the mean gap requires the same conditional "
      "population on both sides.</p>")
    W(box("warn", "Coding direction is not robust to binary reversal",
          "<p>A genuine reversal maps a reported share p to one minus p and reverses an "
          "increasing/decreasing gradient. The earlier claim of direction robustness is "
          "unsupported and withdrawn. Reliable official underemployment figures are "
          "retained only as context; they do not validate offer weights or identify a "
          "preference/constraint wedge.</p>"))

    W("<h3>Why occupation cannot be validated the same way</h3>")
    W("<p>The obvious external check &mdash; compare modelled occupation shares to "
      "published French occupation aggregates &mdash; <b>cannot be done cleanly</b>, "
      "and the reason is structural rather than a matter of effort.</p>")
    W("<ul>")
    W("<li>Published French aggregates are on the national socio-professional "
      "classification. The model&rsquo;s groups are a <em>task-based</em> aggregation of "
      "the international standard classification.</li>")
    W("<li>Official probabilistic correspondences can exist, but the published coarse "
      "cells do not yield a unique aggregate mapping into this paper's four research "
      "groups. An official correspondence and a unique aggregate crosswalk are "
      "different objects.</li>")
    W("<li>A many-to-many crosswalk applied to aggregate shares produces a comparison "
      "whose disagreement is uninterpretable: any gap could be the model or could be "
      "the mapping.</li>")
    W("</ul>")
    W("<p>The honest position, and the one taken, is that occupation is validated "
      "internally (section&nbsp;9) and not externally, and that this is a real "
      "limitation.</p>")

    # ==================================================================== 11 ==
    W('<h2 id="s11" class="exempt">11. Couples</h2>')

    W("<p>The couples model is estimated on " + n("n_households_couples", "int")
      + " two-adult households. The <b>"
      + lit("couples clean baseline negLL 43493.342239066726",
            "the canonical full-precision label of the couples negative "
            "log-likelihood; the bound rendering follows")
      + "</b> is the negative log-likelihood at that optimum, "
      "rendered here as <b>" + n("negll_couples_final", "f4") + "</b>.</p>")

    W("<h3>The joint decision problem</h3>")
    W("<p>A couple is modelled as choosing a <b>joint alternative</b>: an "
      "employment&ndash;hours&ndash;occupation&ndash;wage bundle for <em>each</em> "
      "spouse simultaneously, priced as one household through the tax-benefit system. "
      "This matters for reasons that are not presentational: French income tax and "
      "means-tested benefits are assessed on the household, so one spouse&rsquo;s "
      "earnings change the other&rsquo;s effective return to work. A model that priced "
      "the two separately would get the budget wrong at every alternative.</p>")
    W("<p>The observed joint pair is inserted deterministically, exactly as in the "
      "singles model, and the joint proposal is the product of the two spouses&rsquo; "
      "marginal proposals with the same exact-marginal rule.</p>")
    W("<p>Preferences are the natural extension: each spouse has a leisure weight with "
      "its own intercept and age profile, and the household has a single consumption "
      "term over the joint budget. It is a <b>unitary</b> model &mdash; one household "
      "objective, not a bargaining problem.</p>")

    W(F.fig("r240_couples_participation_obs_vs_pred",
            "Observed and predicted shares of the four joint participation regimes: "
            "neither works, man only, woman only, and both work. Every share uses the "
            "same denominator of all 2,275 clean-couples households; these are joint "
            "regime probabilities, not separate spouse marginals."))
    W(F.fig("r240_couples_hours_obs_vs_pred_by_spouse",
            "Observed and predicted hours by spouse."))
    W(F.fig("r240_couples_coefficients_by_block",
            "Couples coefficients by economic block."))

    W("<h3>The 46 free coordinates</h3>")
    W("<p>The clean both-flexible baseline, by economic block and spouse, with "
      "cluster-robust " + lit("CR1", "the sandwich family, a name") + " standard "
      "errors at "
      + n("n_couples_K_interior", "int") + " interior coordinates over "
      + n("n_couples_clusters", "int") + " household clusters. "
      + n("n_couples_free", "int") + " free coordinates: "
      + n("n_couples_interior", "int") + " interior and "
      + n("n_couples_at_bound", "int") + " on an active bound (<code>"
      + n("couples_active_bound_coordinate", "raw") + "</code>, which carries no "
      "standard error by the " + lit("CR1", "the sandwich family, a name")
      + " restriction). A further "
      + n("n_couples_pinned", "int") + " coordinates are pinned inert and are not "
      "displayed.</p>")
    W('<div class="scroll"><table><thead><tr><th>Coefficient</th><th>What it is</th>'
      '<th class="num">Estimate</th><th class="num">Robust SE</th>'
      '<th class="num">z</th></tr></thead><tbody>' 
      '<tr class="grouphead"><td colspan="5">Male leisure</td></tr>'
      "<tr><td><code>beta_l0_m</code></td><td>Baseline leisure weight.</td>"
      '<td class="num">' + n("couples_param_beta_l0_m__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_l0_m__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_l0_m__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_l_age_m</code></td><td>Linear age gradient.</td>"
      '<td class="num">' + n("couples_param_beta_l_age_m__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_l_age_m__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_l_age_m__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_l_age2_m</code></td><td>Quadratic age term.</td>"
      '<td class="num">' + n("couples_param_beta_l_age2_m__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_l_age2_m__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_l_age2_m__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>theta_l_m</code></td><td>Box&ndash;Cox curvature on leisure.</td>"
      '<td class="num">' + n("couples_param_theta_l_m__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_theta_l_m__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_theta_l_m__z_robust", "f2") + "</td></tr>"
      '<tr class="grouphead"><td colspan="5">Female leisure</td></tr>'
      "<tr><td><code>beta_l0_f</code></td><td>Baseline leisure weight.</td>"
      '<td class="num">' + n("couples_param_beta_l0_f__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_l0_f__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_l0_f__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_l_age_f</code></td><td>Linear age gradient.</td>"
      '<td class="num">' + n("couples_param_beta_l_age_f__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_l_age_f__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_l_age_f__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_l_age2_f</code></td><td>Quadratic age term.</td>"
      '<td class="num">' + n("couples_param_beta_l_age2_f__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_l_age2_f__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_l_age2_f__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_l_nkids_f</code></td><td>Shift per dependent child; on the female leisure only.</td>"
      '<td class="num">' + n("couples_param_beta_l_nkids_f__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_l_nkids_f__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_l_nkids_f__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>theta_l_f</code></td><td>Box&ndash;Cox curvature on leisure.</td>"
      '<td class="num">' + n("couples_param_theta_l_f__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_theta_l_f__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_theta_l_f__z_robust", "f2") + "</td></tr>"
      '<tr class="grouphead"><td colspan="5">Male hours opportunity</td></tr>'
      "<tr><td><code>beta_E_m</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_E_m__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_m__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_m__z_robust", "f2") + "</td></tr>"
      '<tr class="grouphead"><td colspan="5">Female hours opportunity</td></tr>'
      "<tr><td><code>beta_E_f</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_E_f__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_f__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_f__z_robust", "f2") + "</td></tr>"
      '<tr class="grouphead"><td colspan="5">Male hours opportunity</td></tr>'
      "<tr><td><code>beta_h_pt1_m</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_h_pt1_m__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_h_pt1_m__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_h_pt1_m__z_robust", "f2") + "</td></tr>"
      '<tr class="grouphead"><td colspan="5">Female hours opportunity</td></tr>'
      "<tr><td><code>beta_h_pt1_f</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_h_pt1_f__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_h_pt1_f__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_h_pt1_f__z_robust", "f2") + "</td></tr>"
      '<tr class="grouphead"><td colspan="5">Male hours opportunity</td></tr>'
      "<tr><td><code>beta_h_pt2_m</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_h_pt2_m__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_h_pt2_m__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_h_pt2_m__z_robust", "f2") + "</td></tr>"
      '<tr class="grouphead"><td colspan="5">Female hours opportunity</td></tr>'
      "<tr><td><code>beta_h_pt2_f</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_h_pt2_f__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_h_pt2_f__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_h_pt2_f__z_robust", "f2") + "</td></tr>"
      '<tr class="grouphead"><td colspan="5">Male hours opportunity</td></tr>'
      "<tr><td><code>beta_h_f35_m</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_h_f35_m__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_h_f35_m__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_h_f35_m__z_robust", "f2") + "</td></tr>"
      '<tr class="grouphead"><td colspan="5">Female hours opportunity</td></tr>'
      "<tr><td><code>beta_h_f35_f</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_h_f35_f__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_h_f35_f__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_h_f35_f__z_robust", "f2") + "</td></tr>"
      '<tr class="grouphead"><td colspan="5">Male hours opportunity</td></tr>'
      "<tr><td><code>beta_h_ft_m</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_h_ft_m__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_h_ft_m__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_h_ft_m__z_robust", "f2") + "</td></tr>"
      '<tr class="grouphead"><td colspan="5">Female hours opportunity</td></tr>'
      "<tr><td><code>beta_h_ft_f</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_h_ft_f__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_h_ft_f__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_h_ft_f__z_robust", "f2") + "</td></tr>"
      '<tr class="grouphead"><td colspan="5">Male hours opportunity</td></tr>'
      "<tr><td><code>beta_h_lh_m</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_h_lh_m__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_h_lh_m__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_h_lh_m__z_robust", "f2") + "</td></tr>"
      '<tr class="grouphead"><td colspan="5">Female hours opportunity</td></tr>'
      "<tr><td><code>beta_h_lh_f</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_h_lh_f__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_h_lh_f__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_h_lh_f__z_robust", "f2") + "</td></tr>"
      '<tr class="grouphead"><td colspan="5">Employment and local market access</td></tr>'
      "<tr><td><code>beta_E_gsur</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_E_gsur__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_gsur__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_gsur__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_E_drgn2</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_E_drgn2__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_drgn2__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_drgn2__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_E_drgn3</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_E_drgn3__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_drgn3__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_drgn3__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_E_drgn4</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_E_drgn4__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_drgn4__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_drgn4__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_E_drgn5</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_E_drgn5__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_drgn5__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_drgn5__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_E_drgn6</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_E_drgn6__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_drgn6__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_drgn6__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_E_drgn7</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_E_drgn7__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_drgn7__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_drgn7__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_E_drgn8</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_E_drgn8__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_drgn8__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_drgn8__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_E_drgur</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_E_drgur__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_drgur__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_drgur__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_E_drgmd</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_E_drgmd__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_drgmd__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_E_drgmd__z_robust", "f2") + "</td></tr>"
      '<tr class="grouphead"><td colspan="5">Male occupation availability</td></tr>'
      "<tr><td><code>beta_occ_2_m</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_occ_2_m__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_occ_2_m__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_occ_2_m__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_occ_3_m</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_occ_3_m__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_occ_3_m__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_occ_3_m__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_occ_4_m</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_occ_4_m__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_occ_4_m__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_occ_4_m__z_robust", "f2") + "</td></tr>"
      '<tr class="grouphead"><td colspan="5">Female occupation availability</td></tr>'
      "<tr><td><code>beta_occ_2_f</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_occ_2_f__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_occ_2_f__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_occ_2_f__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_occ_3_f</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_occ_3_f__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_occ_3_f__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_occ_3_f__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_occ_4_f</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_occ_4_f__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_occ_4_f__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_occ_4_f__z_robust", "f2") + "</td></tr>"
      '<tr class="grouphead"><td colspan="5">Wage-offer density</td></tr>'
      "<tr><td><code>beta_w0</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_w0__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_w0__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_w0__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_w_educL</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_w_educL__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_w_educL__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_w_educL__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_w_educH</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_w_educH__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_w_educH__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_w_educH__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_w_pexp</code></td><td></td>"
      '<td class="num">' + n("couples_param_beta_w_pexp__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_w_pexp__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_beta_w_pexp__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>beta_w_pexp2</code></td><td> <b class=\"bound\">Free but boundary-active.</b></td>"
      '<td class="num">' + n("couples_param_beta_w_pexp2__estimate", "f4") + "</td>"
      '<td class="num"><span class="bound">at bound</span></td>'
      '<td class="num"><span class="bound">&mdash;</span></td></tr>'
      "<tr><td><code>sigma</code></td><td></td>"
      '<td class="num">' + n("couples_param_sigma__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_sigma__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_sigma__z_robust", "f2") + "</td></tr>"
      '<tr class="grouphead"><td colspan="5">Occupation wage location</td></tr>'
      "<tr><td><code>delta_occ_2</code></td><td></td>"
      '<td class="num">' + n("couples_param_delta_occ_2__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_delta_occ_2__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_delta_occ_2__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>delta_occ_3</code></td><td></td>"
      '<td class="num">' + n("couples_param_delta_occ_3__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_delta_occ_3__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_delta_occ_3__z_robust", "f2") + "</td></tr>"
      "<tr><td><code>delta_occ_4</code></td><td></td>"
      '<td class="num">' + n("couples_param_delta_occ_4__estimate", "f4") + "</td>"
      '<td class="num">' + n("couples_param_delta_occ_4__se_robust", "f4") + "</td>"
      '<td class="num">' + n("couples_param_delta_occ_4__z_robust", "f2") + "</td></tr>"
      "</tbody></table></div>")
    W("<p class=\"sub\"><b>The cross-leisure interaction is not a row of this "
      "table, and that is the point of the note.</b> <code>beta_ll</code> is not a "
      "coordinate of this model: its status is <code>"
      + n("beta_ll_status", "raw") + "</code>, the welfare pipeline uses an "
      "effective value of " + n("beta_ll_welfare_effective_value", "f1")
      + ", and the form it would take is <code>"
      + n("beta_ll_cross_leisure_form", "raw") + "</code>. It was not estimated "
      "and found small, and it was not estimated and then set to zero.</p>")


    W(box("warn", "The cross-leisure term is absent, and this is the first thing to "
                  "volunteer about couples",
          "<p>The natural interaction in a joint labour-supply model is a term in "
          "<em>both</em> spouses&rsquo; leisure:</p>"
          '<div class="eq">'
          "u_household  =  ... +  beta_ll · BC( leisure_male )  ·  BC( leisure_female )"
          "\n\n"
          "the same form written out:\n"
          "  beta_ll * BoxCox(leisure_male) * BoxCox(leisure_female)"
          "</div>"
          "<p><b>Its status in the estimated model is <code>"
          + n("beta_ll_status", "raw") + "</code>, and the welfare pipeline uses the "
          "value " + n("beta_ll_welfare_effective_value", "f1") + " for it &mdash; "
          "exactly zero.</b> It is not estimated, and it must not be described as "
          "estimated.</p>"
          "<p><b>What it would mean.</b> The sign of that coefficient is the sign of the "
          "<em>complementarity of spouses&rsquo; time</em>. Positive means leisure is "
          "jointly enjoyed &mdash; time off is worth more when taken together, so "
          "spouses coordinate their schedules and their labour supply responses "
          "reinforce each other. Negative means the spouses&rsquo; time substitutes, as "
          "it would if household production has to be covered by someone: one partner "
          "working more raises the value of the other&rsquo;s time at home. Setting it "
          "to zero removes the direct leisure interaction. Spouses still interact "
          "through joint consumption, income effects, non-linear household taxes and "
          "transfers, and the joint choice problem; their decisions are not independent. For a "
          "model of joint labour supply that is a real restriction, and it is the "
          "restriction most likely to be challenged.</p>"
          "<p><b>Why it is zero.</b> Including it made the joint estimation problem "
          "ill-conditioned: the curvature at the optimum lost positive definiteness. "
          "Fixing it at zero restored a well-behaved optimum, but the weak direction "
          "then <em>moved</em> to the male leisure block rather than disappearing &mdash; "
          "which is why the male-leisure sensitivity below is material. This historical "
          "curvature failure motivated the restriction, but does not prove that the "
          "interaction is unidentifiable in every corrected couples specification. "
          "Estimating it is post-seminar work; it was not found to be zero.</p>"))

    W("<h3>Couples welfare, and why singles remain the headline</h3>")
    W("<p>The same welfare machinery runs on couples. It is exhaustive in the same "
      "sense: equalizing everything drives measured inequality to "
      + n("couples_state_I1111_equivalized", "sci", 1)
      + " Gini points (RQMC band "
      + n("couples_state_I1111_equivalized__rqmc_band", "range")
      + ") from a baseline of "
      + n("couples_state_I0000_equivalized", "f3") + " (band "
      + n("couples_state_I0000_equivalized__rqmc_band", "range") + ").</p>")
    W("<p class=\"exempt\">These are RQMC numerical-integration bands only. Couples welfare does not "
      "carry the same conditional CR1 parameter-uncertainty propagation as the singles "
      "headline; male-leisure specification sensitivity is reported separately. The "
      "uncertainty sources are not merged.</p>")
    W('<div class="scroll"><table><thead><tr><th>Channel</th>'
      '<th class="num">Gini points, with the eight-scramble RQMC band</th>'
      '<th>Reading</th></tr></thead><tbody>'
      "<tr><td><b>Preferences</b></td>"
      '<td class="num">' + n("couples_C_P_equivalized", "f4")
      + '<br><small class="bandnote">'
      + n("couples_C_P_equivalized__rqmc_band", "range")
      + "</small></td>"
      "<td>Small, as in singles &mdash; but the least stable quantity in the couples "
      "model.</td></tr>"
      "<tr><td><b>Job access</b></td>"
      '<td class="num">' + n("couples_C_A_equivalized", "f4")
      + '<br><small class="bandnote">'
      + n("couples_C_A_equivalized__rqmc_band", "range")
      + "</small></td>"
      "<td>The employment and hours opportunity margin.</td></tr>"
      "<tr><td><b>Earning opportunities</b></td>"
      '<td class="num">' + n("couples_C_B_equivalized", "f4")
      + '<br><small class="bandnote">'
      + n("couples_C_B_equivalized__rqmc_band", "range")
      + "</small></td>"
      "<td>The wage-offer technology, both spouses.</td></tr>"
      "<tr><td><b>Endowments and needs</b></td>"
      '<td class="num">' + n("couples_C_D_equivalized", "f4")
      + '<br><small class="bandnote">'
      + n("couples_C_D_equivalized__rqmc_band", "range")
      + "</small></td>"
      "<td>Non-labour resources and household composition.</td></tr>"
      "<tr><td><b>The environment, total</b></td>"
      '<td class="num">' + n("couples_C_E_equivalized", "f4")
      + '<br><small class="bandnote">'
      + n("couples_C_E_equivalized__rqmc_band", "range")
      + "</small></td>"
      "<td>Everything that is not preference.</td></tr>"
      "</tbody></table></div>")

    W(F.fig("figC02_couples_decomposition",
            "The couples decomposition with uncertainty bands."))
    W(F.fig("figC03_singles_vs_couples",
            "Singles against couples, side by side. The broad shape is the same: a "
            "small preference contribution against a dominant environment."))

    W(box("warn", "Why the couples numbers are a companion result, not the headline",
          "<p>Three reasons, in order of force.</p>"
          "<ol>"
          "<li><b>The preference channel is not stable.</b> Across the male-leisure "
          "sensitivity battery, the couples preference contribution moves by up to "
          + n("couples_male_leisure_sensitivity_max", "pct", 1)
          + " in relative terms. That is a material movement in exactly the quantity the "
          "paper is about, and it traces back to the weak direction left behind when the "
          "cross-leisure term was set to zero.</li>"
          "<li><b>The unitary model assigns no welfare to individuals.</b> A couple has "
          "one household welfare level. The model takes no position on how it is shared, "
          "so nothing in the couples results can speak to inequality <em>within</em> "
          "households &mdash; which for a paper about opportunity is a serious "
          "restriction, and is stated as such in section&nbsp;20.</li>"
          "<li><b>Singles and couples cannot be pooled into one decomposition.</b> "
          "Attempting it gives a decomposition that does not close: the two household "
          "types need different reference households, and forcing a common one leaves a "
          "large unattributed remainder. The two are reported side by side, never "
          "summed.</li>"
          "</ol>"))
    W(F.fig("figC05_male_leisure_sensitivity",
            "The male-leisure sensitivity, all arms. The spread in the preference "
            "channel is the reason couples are a companion result."))

    # ==================================================================== 12 ==
    W('<h2 id="s12" class="exempt">12. Children</h2>')

    W("<p>Children enter the model in two quite different places, and keeping them "
      "apart matters for reading the results.</p>")
    W("<ol>")
    W("<li><b>Through the budget.</b> Family benefits, means-tested transfers and the "
      "tax schedule all respond to the number of children, and the simulator applies "
      "all of it at every alternative. This channel is fully present and is not a "
      "modelling choice.</li>")
    W("<li><b>Through preferences</b>, as a shifter in the leisure weight &mdash; the "
      "value of time at home. This channel is present for single women only.</li>")
    W("</ol>")

    W('<div class="scroll"><table><thead><tr><th>Term</th><th class="num">Estimate</th>'
      '<th class="num">Robust SE</th><th class="num">z</th><th>Status</th>'
      "</tr></thead><tbody>"
      "<tr><td><b>Child count, single women</b></td>"
      '<td class="num">' + n("beta_l_nkids_female", "f4") + "</td>"
      '<td class="num">' + n("beta_l_nkids_female_se", "f4") + "</td>"
      '<td class="num">' + n("beta_l_nkids_female_z", "f3") + "</td>"
      '<td><span class="tag yes">in the model</span> interior, estimated</td></tr>'
      "<tr><td><b>Child count, single men</b></td>"
      '<td class="num">' + n("beta_l_nkids_male_historical_test", "f4") + "</td>"
      '<td class="num">' + a("chron.male_child_se", "f4") + "</td>"
      '<td class="num">' + a("chron.male_child_z", "f2") + "</td>"
      '<td><span class="tag no">absent</span> tested and rejected</td></tr>'
      "</tbody></table></div>")

    W("<p>For single women, one additional model-defined child adds "
      + n("beta_l_nkids_female", "f4") + " model units to the leisure-weight index. "
      "It is not exponentiated and is not itself a labour-supply elasticity. The "
      "estimated couples-female term is negative and imprecise, so the two applications "
      "do not support a universal positive childcare-preference statement. The singles "
      "term is only marginally precise.</p>")
    W("<p><b>Tested, not identified, and applying to few households &mdash; the "
      "three things to say about the male term, in that order.</b> It was "
      "<b>tested</b>: the historical S-battery arm added one male child-count "
      "shifter to the nested benchmark and returned "
      + n("beta_l_nkids_male_historical_test", "f4") + " with a robust standard "
      "error of " + a("chron.male_child_se", "f4") + " and <em>z</em> of "
      + a("chron.male_child_z", "f2") + ", flagged on the boundary-diagnostic "
      "criterion, with " + lit("&Delta;AIC +1.506", "the information-criterion "
      "movement of the historical S-battery arm") + " and "
      + lit("&Delta;BIC +6.855 / +11.470", "the same, on households and on rows")
      + ". It is <b>not identified</b> on that evidence: the point estimate is "
      "larger than the female one but its standard error is larger still, and both "
      "criteria penalise the extra parameter. And its <b>exposure is small</b> "
      "&mdash; " + a("child.male_with_children", "int") + " of "
      + a("child.male_units", "int") + " single men in the estimation sample have "
      "a child in the frame, "
      + a("child.male_with_children_share_of_men", "pct", 2) + " of single men and "
      + a("child.male_with_children_share_of_sample", "pct", 2) + " of the "
      + n("n_households_singles", "int") + "-household sample (weighted, "
      + a("child.male_with_children_share_of_men_weighted", "pct", 2) + " and "
      + a("child.male_with_children_share_of_sample_weighted", "pct", 2)
      + "). So the model imposes a structural zero rather than carrying a noisy "
      "coefficient: its status is <code>"
      + n("beta_l_nkids_male_status", "raw") + "</code> &mdash; <b>absent by the "
      "sex-specific shifter specification</b>, not estimated as zero and not "
      "&ldquo;insignificant&rdquo;.</p>")
    W("<p><b>The scope caveat travels with it.</b> That test was run on the "
      "pre-correction benchmark frame, not on the final corrected model, and it "
      "has <b>not</b> been re-run there. What is on the record is a rejection on "
      "the earlier frame plus a structural absence in the current one.</p>")

    W(box("key", "What child age would add, and why it is not in the seminar baseline",
          "<p><b>The construction is available, and the variables can be named.</b> "
          "The raw frame of "
          + n("n_households_raw_frame", "int") + " households carries the "
          "<b>parent&ndash;child link</b> and each child&rsquo;s <b>date of "
          "birth</b>. Three variables follow with no new data: each resident "
          "child&rsquo;s <b>age</b>, the <b>age of the youngest child</b>, and a "
          "<b>pre-school indicator</b> for a youngest child under six. They are "
          "named here as post-seminar work, not as a result.</p>"
          "<p><b>Why it would matter.</b> A count treats a two-year-old and a "
          "fifteen-year-old as the same object. They are not: the constraint from a "
          "pre-school child is far sharper, is concentrated in the years when childcare "
          "is scarce or expensive, and falls away as children reach school age. A count "
          "term averages a large early effect and a small late one into a middling "
          "coefficient with a wide interval &mdash; which is exactly the shape of the "
          "estimate above. A young-child indicator would very plausibly be better "
          "determined than the count it would replace.</p>"
          "<p><b>Why it is not in the baseline.</b> It is a targeted refinement that was "
          "not part of the specification search, and adding it now would mean re-pricing "
          "and re-estimating outside the frozen frame. It is named here as future work, "
          "and it is a good answer to give if asked &mdash; it is a concrete, "
          "already-feasible next step rather than a deflection.</p>"))

    return H
