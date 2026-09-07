# -*- coding: utf-8 -*-
"""Sections 7-12: parameterization, chronology, fit, external validation,
couples, children."""
from common import n, a, lit, box


# The audience-facing grouping of the 41 estimated coordinates.
PARAM_GROUPS = [
    ("Male preferences", "How single men value time, and how that changes with age.",
     ["beta_l0_sm", "beta_l_age_sm", "beta_l_age2_sm", "theta_l_sm"]),
    ("Female preferences",
     "How single women value time, with age and with children present.",
     ["beta_l0_sf", "beta_l_age_sf", "beta_l_age2_sf", "beta_l_nkids_sf", "theta_l_sf"]),
    ("Consumption curvature",
     "Diminishing marginal utility of consumption; governs the income&ndash;time "
     "trade-off. Pooled across sexes.",
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
    "theta_c_singles": "Box&ndash;Cox curvature on consumption. Well inside the unit "
                       "interval, so marginal utility of income falls with income.",
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
    H = []
    W = H.append

    # ===================================================================== 7 ==
    W('<h2 id="s7" class="exempt">7. The estimated model, coefficient by coefficient</h2>')

    W("<p>The preferred specification estimates <b>" + n("n_params_active", "int")
      + "</b> coordinates. Of those, <b>" + n("n_params_interior", "int")
      + "</b> are interior at the optimum and <b>" + n("n_params_at_bound", "int")
      + "</b> are free but sit at an active bound. The log-likelihood at the optimum is "
      "<b>" + n("negll_singles_final", "f4") + "</b>, and standard errors are the "
      "household-clustered robust sandwich over " + n("n_households_singles", "int")
      + " clusters.</p>")

    W(_param_table())

    W("<h3>The two boundary-active coefficients</h3>")
    W("<p>The quadratic age terms in both leisure weights, <code>beta_l_age2_sm</code> "
      "and <code>beta_l_age2_sf</code>, are <b>free parameters that happen to rest on an "
      "active bound at the optimum</b>. They are not pinned and they were not fixed by "
      "hand: the optimiser was free to move them and did not.</p>")
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
      "not a specification choice: the earlier convention optimised a likelihood in the "
      "labelled space rather than the job space. Everything downstream is on the "
      "corrected convention, and pre-correction results are retained as history rather "
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
      + "</b> in log-likelihood for <b>one</b> degree of freedom, and repairs the "
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
    W("<p><b>The economic reason it belongs in the opportunity block and not in "
      "preferences.</b> A spike at one hours value is a property of what employers post "
      "under a statutory norm. No smooth, well-behaved utility function generates a "
      "point mass at a single hours value for a quarter of the workforce; you would "
      "need a kink in preferences located at exactly the institutional threshold, for "
      "everyone, which is an assumption about tastes that happens to coincide with a "
      "law. Placing it in the offer density says instead that the law shapes what is "
      "offered. Section&nbsp;10 shows the same concentration in an independent "
      "labour-force survey, which is what makes the reading credible rather than "
      "convenient.</p>")
    W("<p>It is also the <em>most parsimonious</em> admitted extension, not the "
      "richest: it costs exactly one free coefficient over the nested benchmark, and it "
      "is the only variant in the whole search whose robust intervals all stay clear of "
      "their bounds.</p>")

    W("<h3>Stage 6 &mdash; the five-hour support correction</h3>")
    W("<p>The employed alternatives&rsquo; hours support carries a floor of "
      + lit("5", "hours floor of the corrected support") + " hours per week: below "
      "that, the alternative is the non-employment state rather than a nominal job. "
      "Without the floor, the sampler places density on economically meaningless "
      "near-zero-hours jobs whose simulated budgets are dominated by benefit "
      "withdrawal. The correction required re-pricing and re-estimation; it defines the "
      "frame all current results are on, and results predating it are history.</p>")

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
      + ", and the Bayesian criterion moves the wrong way under both conventions. The "
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
      "female shifters come out with opposite signs, neither reaches conventional "
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
          "independent data source that entered no likelihood, no gate and no merge. "
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
          "<p>This is an argmax-relocation artefact. Redistributing probability mass "
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
      "and sex.</p>")

    W(box("warn", "Validation is not identification",
          "<p><b>No moment from the labour force survey enters the likelihood.</b> It is "
          "not an instrument, it enters no gate, no merge and no covariate, and it does "
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
      "rather than as a fitted artefact.</p>")

    W(_hours_table())
    W(F.fig("figX1_external_hours_lfs_validation",
            "Hours-band shares: the independent labour force survey, the estimation "
            "sample, and the model. Shares are of the five priced bands, the only base "
            "on which the three sources are commensurable."))

    W("<h3>The wish-to-work-more gradient, and its caveat</h3>")
    W("<p>The survey asks employed people whether they would like to work more hours. "
      "The reported rate falls monotonically as hours rise &mdash; short-hours workers "
      "are far more likely to say yes &mdash; which is the direction the model implies. "
      "Independently, mean desired hours exceed the <em>upper bound</em> of the "
      "short-hours bands, meaning every worker in those bands wants more hours, with no "
      "distributional assumption at all.</p>")
    W(box("warn", "A coding ambiguity that is disclosed, not resolved",
          "<p>The delivered survey export&rsquo;s own note gives the opposite code map "
          "for the wish-to-work-more variable from the published codebook. The status "
          "carried is <code>" + n("external_validation_wishmore_status", "raw")
          + "</code>. The <em>direction</em> of the gradient is robust either way; which "
          "absolute level is correct is not resolved. Nothing in the paper rests on "
          "it &mdash; but it should be volunteered rather than discovered.</p>"))

    W("<h3>Why occupation cannot be validated the same way</h3>")
    W("<p>The obvious external check &mdash; compare modelled occupation shares to "
      "published French occupation aggregates &mdash; <b>cannot be done cleanly</b>, "
      "and the reason is structural rather than a matter of effort.</p>")
    W("<ul>")
    W("<li>Published French aggregates are on the national socio-professional "
      "classification. The model&rsquo;s groups are a <em>task-based</em> aggregation of "
      "the international standard classification.</li>")
    W("<li>No official crosswalk exists between the relevant vintages of the two "
      "schemes. Building the link needs four intermediate tables, not two, and each "
      "step is many-to-many.</li>")
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
      + " two-adult households, with a log-likelihood at the optimum of "
      + n("negll_couples_final", "f4") + ".</p>")

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
      "marginal proposals with the same exact-marginal convention.</p>")
    W("<p>Preferences are the natural extension: each spouse has a leisure weight with "
      "its own intercept and age profile, and the household has a single consumption "
      "term over the joint budget. It is a <b>unitary</b> model &mdash; one household "
      "objective, not a bargaining problem.</p>")

    W(F.fig("r240_couples_participation_obs_vs_pred",
            "Observed and predicted participation, couples, by spouse."))
    W(F.fig("r240_couples_hours_obs_vs_pred_by_spouse",
            "Observed and predicted hours by spouse."))
    W(F.fig("r240_couples_coefficients_by_block",
            "Couples coefficients by economic block."))

    W(box("warn", "The cross-leisure term is absent, and this is the first thing to "
                  "volunteer about couples",
          "<p>The natural interaction in a joint labour-supply model is a term in "
          "<em>both</em> spouses&rsquo; leisure:</p>"
          '<div class="eq">'
          "u_household  =  ... +  beta_ll · BC( leisure_male )  ·  BC( leisure_female )"
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
          "to zero imposes that a spouse&rsquo;s hours affect the other only through the "
          "household <em>budget</em>, never through the value of time itself. For a "
          "model of joint labour supply that is a real restriction, and it is the "
          "restriction most likely to be challenged.</p>"
          "<p><b>Why it is zero.</b> Including it made the joint estimation problem "
          "ill-conditioned: the curvature at the optimum lost positive definiteness. "
          "Fixing it at zero restored a well-behaved optimum, but the weak direction "
          "then <em>moved</em> to the male leisure block rather than disappearing &mdash; "
          "which is why the male-leisure sensitivity below is material. Identifying the "
          "interaction is an <b>immediate post-seminar extension</b>, and the right "
          "answer to a question about it is that the model as it stands cannot separate "
          "it, not that it was found to be zero.</p>"))

    W("<h3>Couples welfare, and why singles remain the headline</h3>")
    W("<p>The same welfare machinery runs on couples. It is exhaustive in the same "
      "sense: equalizing everything drives measured inequality to "
      + n("couples_state_I1111_equivalized", "sci", 1)
      + " Gini points from a baseline of "
      + n("couples_state_I0000_equivalized", "f3") + ".</p>")
    W('<div class="scroll"><table><thead><tr><th>Channel</th>'
      '<th class="num">Gini points</th><th>Reading</th></tr></thead><tbody>'
      "<tr><td><b>Preferences</b></td>"
      '<td class="num">' + n("couples_C_P_equivalized", "f4") + "</td>"
      "<td>Small, as in singles &mdash; but the least stable quantity in the couples "
      "model.</td></tr>"
      "<tr><td><b>Job access</b></td>"
      '<td class="num">' + n("couples_C_A_equivalized", "f4") + "</td>"
      "<td>The employment and hours opportunity margin.</td></tr>"
      "<tr><td><b>Earning opportunities</b></td>"
      '<td class="num">' + n("couples_C_B_equivalized", "f4") + "</td>"
      "<td>The wage-offer technology, both spouses.</td></tr>"
      "<tr><td><b>Endowments and needs</b></td>"
      '<td class="num">' + n("couples_C_D_equivalized", "f4") + "</td>"
      "<td>Non-labour resources and household composition.</td></tr>"
      "<tr><td><b>The environment, total</b></td>"
      '<td class="num">' + n("couples_C_E_equivalized", "f4") + "</td>"
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

    W("<p>The female term is positive and economically sizeable: each dependent child "
      "raises the weight a single mother places on time at home, which lowers her "
      "labour supply at any given budget. It is on the edge of conventional "
      "significance rather than comfortably inside it, and that should be said before "
      "it is asked.</p>")
    W("<p>The male term was estimated and rejected. The point estimate is larger than "
      "the female one, but its standard error is larger still, and both information "
      "criteria penalise the extra parameter. Substantively, single fathers are a small "
      "and selected group; the data do not support a separate male child effect, and "
      "the model imposes a structural zero rather than carrying a noisy coefficient. "
      "Its status is <code>" + n("beta_l_nkids_male_status", "raw") + "</code>.</p>")

    W(box("key", "What child age would add, and why it is not in the seminar baseline",
          "<p><b>The construction is available.</b> The raw frame of "
          + n("n_households_raw_frame", "int") + " households carries parent&ndash;child "
          "links and each child&rsquo;s date of birth, so child ages &mdash; and "
          "therefore an indicator for a pre-school child &mdash; can be built without "
          "any new data.</p>"
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
