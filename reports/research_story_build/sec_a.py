# -*- coding: utf-8 -*-
"""Sections 1-11 of the research-story report."""
from common import n, a, lit, box, esc, math, imath, aux_data


def sections(F):
    """F is a FigureBank."""
    _AUX = aux_data()
    H = []
    W = H.append

    # ===================================================================== 1 ==
    W('<h2 id="s1" class="exempt">1. Executive overview</h2>')
    W('<p class="lede">Two people hold different jobs. One of them earns less, works '
      'fewer hours, and lives in a weaker local labour market. How much of the gap '
      'between them is something they chose, and how much is something they faced?</p>')

    W("<h3>The research question</h3>")
    W('<p>Standard labour-supply models answer that question by assumption. They give '
      'every worker the same budget set and let observed differences in hours, '
      'occupation and pay fall out of differences in taste. Anyone who works part time '
      'is revealed to prefer leisure; anyone in a low-paying occupation is revealed to '
      'prefer it. That is a modelling convention, not a finding, and it does most of '
      'the normative work in any welfare statement built on top of it.</p>')
    W('<p>This paper asks what happens when the convention is dropped. It estimates a '
      'model in which each household draws its job from an <em>individual-specific '
      'opportunity distribution</em> &mdash; how likely employment is at all, which '
      'hours are on offer, which occupations are reachable, and what pay each of them '
      'carries &mdash; jointly with the preferences that rank the jobs that are '
      'reachable. It then asks how much of the inequality in a preference-respecting '
      'welfare measure is attributable to preferences and how much to the environment '
      'people face.</p>')

    W("<h3>The contribution</h3>")
    W("<ol>")
    W('<li><b>A jointly estimated random-opportunity labour-supply model on French '
      'micro-data</b>, in which the opportunity side is not calibrated or imposed but '
      'estimated from the same choice outcomes, with the tax-benefit system solved '
      'exactly at every alternative rather than approximated.</li>')
    W('<li><b>A welfare decomposition that respects preferences and is exhaustive.</b> '
      'The preference and environment contributions are Shapley/Owen values on an '
      'explicit cooperative game whose grand coalition is verified to close: '
      'equalizing everything drives measured inequality to <span class="mono">'
      + n("state_I11_female_raw", "sci", 1) + "</span> Gini points (RQMC band "
      + n("state_I11_female_raw__rqmc_band", "range")
      + "), numerically zero. Nothing is left in an unexplained residual.</li>")
    W('<li><b>A benchmark that prices the modelling convention itself.</b> The same '
      'welfare machinery is run on a re-estimated model in which everyone faces the '
      'same opportunities. The comparison shows exactly what is lost, and &mdash; the '
      'more surprising result &mdash; where the lost attribution actually goes.</li>')
    W('<li><b>A nested reading of the environment</b> into job access, earning '
      'opportunities and household endowments and needs, and of job access further '
      'into its geographic and non-geographic parts, each closing as an exact '
      'identity rather than as an approximation.</li>')
    W("</ol>")

    W("<h3>The result, in one paragraph</h3>")
    W('<p>On single-adult households in France, measured welfare inequality is '
      + n("state_I00_female_raw", "f3") + ' Gini points on the raw basis (RQMC band '
      + n("state_I00_female_raw__rqmc_band", "range") + '). Of that, '
      'preferences account for ' + n("C_pref_female_raw_share", "pct", 1)
      + ' &mdash; parameter interval '
      + n("s_pref_female_raw__cr1_interval", "rangepct", 1)
      + ' &mdash; and the non-preference environment for '
      + n("C_env_female_raw_share", "pct", 1) + ', parameter interval '
      + n("s_env_female_raw__cr1_interval", "rangepct", 1)
      + '. Integration bands and parameter intervals are two different objects '
      'and are never merged. Inside the environment, household '
      'endowments and needs are the largest single component at '
      + n("C_needs_female_raw_share", "pct", 1) + ' of baseline inequality, with the '
      'two market-side channels &mdash; job access '
      + n("C_acc_female_raw_share", "pct", 1) + ' and earning opportunities '
      + n("C_earn_female_raw_share", "pct", 1) + ' &mdash; together accounting for '
      'rather more than a third of it. Almost all of the '
      'job-access contribution is geographic: local labour-market conditions and where '
      'a household lives account for ' + n("geo_share_of_C_acc_raw", "pct", 1)
      + ' of the job-access channel on the raw basis. The attribution shares are '
      'considerably more robust than the preference level: the preference contribution '
      'moves materially with the choice of reference household, whereas the broad '
      'structure of the environment does not.</p>')

    W(box("warn", "The one claim this paper does not make",
          "<p>None of this is causal. No component is the effect of the French "
          "tax-benefit system, of living in one region rather than another, or of any "
          "policy. Every contribution is a model-implied attribution under a "
          "<em>fixed</em> policy system, holding estimated preferences and the observed "
          "sample frame constant. Section&nbsp;20 states the full list of what is not "
          "identified.</p>"))

    W(F.fig("figT1_conceptual",
            "The whole paper in one picture. A household&rsquo;s observed job is one "
            "draw from a personal opportunity distribution, evaluated by personal "
            "preferences. Two households can end up in the same job for opposite "
            "reasons, and in different jobs for no preference reason at all. The "
            "estimation separates the two surfaces; the welfare stage equalizes them "
            "one at a time.",
            "Schematic. Drawn from stylised parameters chosen for legibility; no axis "
            "carries an estimated quantity."))

    W(box("key", "How to use this document",
          "<p>Sections 2&ndash;6 are the model and the data; sections 7&ndash;8 the "
          "specification and how it was reached; sections 9&ndash;10 fit and external "
          "evidence; sections 11&ndash;12 couples and children; sections 13&ndash;18 the "
          "welfare results; sections 19&ndash;20 robustness and limits; section 21 the "
          "hands-on reproduction guide keyed to the research notebook; and section 22 "
          "the seminar question bank. Every numeral in the document is rendered from an embedded "
          "data block at page load &mdash; hover any bolded number to see its key, its "
          "definition and the data file it was read from. Section&nbsp;23 audits "
          "that claim mechanically.</p>"))

    # ===================================================================== 2 ==
    W('<h2 id="s2" class="exempt">2. The original economic problem</h2>')

    W('<p>Everything in the paper follows from one distinction, and the whole '
      'identification argument is about whether that distinction can be made from '
      'choice data at all.</p>')

    W('<div class="scroll"><table><thead><tr>'
      "<th>Two reasons a job is not observed</th><th>What it means</th>"
      "<th>What a standard model does with it</th></tr></thead><tbody>"
      "<tr><td><b>Not preferred.</b> The job was available and the household ranked "
      "something else above it.</td>"
      "<td>A genuine expression of taste over hours, occupation, pay and time.</td>"
      "<td>Records it as taste. Correctly.</td></tr>"
      "<tr><td><b>Not accessible.</b> The job was not on offer to this household, or "
      "was on offer with low probability.</td>"
      "<td>A feature of the environment: local demand, the hours employers post, the "
      "occupations reachable given schooling and experience.</td>"
      "<td>Also records it as taste. Incorrectly &mdash; and this is the whole "
      "problem.</td></tr>"
      "</tbody></table></div>")

    W('<p>The confusion is not innocuous for welfare. If a woman in a weak local labour '
      'market works part time because full-time work is scarce where she lives, a model '
      'that reads that as a preference for leisure will conclude she is getting what '
      'she wants, and will therefore see no inequality to be concerned about. The same '
      'observation, read as a constraint, is inequality of opportunity. Section&nbsp;18 '
      'shows that this is not a hypothetical worry: re-estimating the model with common '
      'opportunities recovers availability constants as tastes, and reverses the sign '
      'of the estimated male-female difference in the valuation of leisure.</p>')

    W("<h3>The theoretical object and the estimated one</h3>")
    W('<p>In the theory, each individual <em>i</em> has an <b>opportunity set</b> '
      '<em>A<sub>i</sub></em>: the set of jobs actually open to them. Welfare and '
      'responsibility statements in the equality-of-opportunity literature are written '
      'over that object. It is a set &mdash; a job is in it or it is not.</p>')

    W(box("warn", "What is and is not recovered",
          "<p><b>This paper does not recover <em>A<sub>i</sub></em>.</b> Deterministic "
          "individual opportunity sets are not identified from choice data, and no "
          "claim in the paper depends on their being identified.</p>"
          "<p>What is estimated is an <b>opportunity density</b>: a probability "
          "distribution <em>g<sub>i</sub></em> over the job space, whose parameters are "
          "functions of observable circumstances &mdash; sex, age, education, "
          "experience, region, urbanisation, the local unemployment rate. It says how "
          "likely a job of a given kind is to be available to someone in "
          "<em>i</em>&rsquo;s circumstances. It does not say which jobs "
          "<em>i</em> personally could have taken.</p>"
          "<p>The relation between them is the one the paper is careful to state and "
          "careful not to overstate: the estimated density is a <b>population-level "
          "smoothing</b> of the unobserved individual sets. Two households with "
          "identical observed circumstances receive identical opportunity densities by "
          "construction, however different their true sets may be. Everything that "
          "distinguishes them beyond circumstances is, in this model, either preference "
          "or noise.</p>"))

    W('<p>This is why the paper&rsquo;s language throughout is <em>job access</em> and '
      '<em>earning capacity</em> or <em>wage-offer technology</em>, and never '
      'unqualified &ldquo;ability&rdquo;. The wage block estimates the location and '
      'dispersion of the offer distribution a household faces. It does not measure how '
      'productive anyone is.</p>')

    W("<h3>Why choice data can separate the two surfaces at all</h3>")
    W("<p>The separation does not come from functional form alone. Three features "
      "of the data carry it:</p>")
    W("<ul>")
    W('<li><b>Circumstances shift the opportunity side and are excluded from '
      'preferences.</b> The local unemployment rate, region and urbanisation enter '
      'job access and nothing else. A household that works less when its local market '
      'is slack, holding its own characteristics fixed, moves the access block, not '
      'the taste block.</li>')
    W('<li><b>The wage is observed for workers and modelled as an offer density.</b> '
      'That pins the earning-opportunity surface directly rather than through the '
      'labour-supply response, which is what makes it separable from the valuation of '
      'consumption.</li>')
    W('<li><b>The hours distribution has institutional structure that preferences '
      'cannot generate.</b> A sharp spike at the statutory week is a property of what '
      'employers post, not of a smooth utility function. Section&nbsp;8 shows this is '
      'the single largest specification gain in the paper.</li>')
    W("</ul>")
    W('<p>What choice data cannot do is separate <em>unobserved heterogeneity</em> in '
      'preferences from <em>unobserved heterogeneity</em> in opportunities. Three '
      'independent attempts to add persistent unobserved heterogeneity all failed to '
      'be identified, for three different reasons; the joint version was never '
      'authorized. Sections&nbsp;8 and 20 give the evidence.</p>')

    # ===================================================================== 3 ==
    W('<h2 id="s3" class="exempt">3. Data</h2>')

    W("<h3>Country, year and sources</h3>")
    W('<div class="scroll"><table><thead><tr><th>Element</th><th>What it is</th>'
      "<th>Role</th></tr></thead><tbody>"
      "<tr><td><b>Country and year</b></td>"
      "<td>France, income reference year " + lit("2016", "calendar year of the sample")
      + " (EU-SILC / SRCV).</td>"
      "<td>The single cross-section everything is estimated on.</td></tr>"
      "<tr><td><b>EU-SILC / SRCV</b></td>"
      "<td>The French national component of EU statistics on income and living "
      "conditions: household and person records with demographics, education, labour "
      "status, hours, earnings and household composition.</td>"
      "<td><b>The observed sample.</b> Supplies who exists, what they chose, and every "
      "circumstance the opportunity side conditions on.</td></tr>"
      "<tr><td><b>EUROMOD</b></td>"
      "<td>The EU tax-benefit microsimulation model, run on the French system.</td>"
      "<td><b>The budget constraint.</b> Converts a (hours, wage, occupation) job into "
      "disposable income for that household, under the actual French rules including "
      "income tax, social contributions, family benefits, housing benefit and social "
      "assistance.</td></tr>"
      "<tr><td><b>EU-LFS (Enqu&ecirc;te Emploi) " + lit("2016", "calendar year of the benchmark")
      + "</b></td>"
      "<td>The French labour force survey, person records.</td>"
      "<td><b>External benchmark only.</b> No moment from it enters the likelihood. "
      "Section&nbsp;10.</td></tr>"
      "</tbody></table></div>")

    W(box("key", "Where EUROMOD actually enters",
          "<p>This is worth being precise about, because it is a standard seminar "
          "question. EUROMOD is <b>not</b> called inside the likelihood. It is called "
          "<b>once, in advance</b>, to price every alternative in every household&rsquo;s "
          "choice set: for each of the " + n("n_priced_rows_singles", "int")
          + " priced rows &mdash; " + n("n_households_singles", "int")
          + " households &times; " + n("n_alternatives", "int")
          + " alternatives &mdash; the simulator returns the disposable income that job "
          "would generate for that household under the actual French rules. Those "
          "incomes are frozen into the estimation frame. Estimation then reads them.</p>"
          "<p>The consequence is that the budget constraint is <b>exact and "
          "non-linear</b>, with every kink, benefit withdrawal and interaction the real "
          "system contains, rather than a linearised or approximated net wage. The cost "
          "is that the choice sets cannot be changed without re-running the simulator, "
          "which is why the drawn alternatives are generated once and then held "
          "fixed.</p>"))

    W("<h3>Samples and restrictions</h3>")
    W('<div class="scroll"><table><thead><tr><th>Sample</th><th class="num">Households</th>'
      "<th>Definition and restrictions</th></tr></thead><tbody>"
      "<tr><td><b>Raw frame</b></td>"
      '<td class="num">' + n("n_households_raw_frame", "int") + "</td>"
      "<td>All French households on the frame before estimation-sample filtering, "
      "singles and couples pooled. This is the base on which parent&ndash;child links "
      "and household composition are constructed.</td></tr>"
      "<tr><td><b>Singles &mdash; the estimation sample</b></td>"
      '<td class="num">' + n("n_households_singles", "int") + "</td>"
      "<td>Single-adult households with a flexible decision-maker aged "
      + lit("20", "lower age bound of the estimation sample") + "&ndash;"
      + lit("60", "upper age bound of the estimation sample")
      + ". This is the headline sample: every welfare result in "
      "sections 13&ndash;18 is computed on it. It is also the cluster count for "
      "inference &mdash; standard errors are clustered on the household.</td></tr>"
      "<tr><td><b>Couples</b></td>"
      '<td class="num">' + n("n_households_couples", "int") + "</td>"
      "<td>Two-adult households, both spouses flexible, estimated as a joint decision "
      "problem. Section&nbsp;11.</td></tr>"
      "</tbody></table></div>")

    W('<p>The single-adult sample is the headline for a reason that is substantive and '
      'not a convenience: in a one-adult household the welfare unit and the '
      'decision-maker coincide, so a money-metric welfare level is well defined without '
      'taking a position on how a couple shares its resources. Section&nbsp;11 explains '
      'why the couples results are reported as a companion rather than as the '
      'headline.</p>')

    # ---- the sample-construction waterfall ------------------------------- #
    W("<h3>How the estimation sample is built, screen by screen</h3>")
    W("<p>Nothing is dropped for convenience, and every screen has an economic "
      "reason. The model describes the labour supply of prime-age adults who are "
      "in a position to work, facing a household budget that depends on their own "
      "job and on nobody else&rsquo;s. Each row below removes the households for "
      "which that description fails, and says why. The <b>same</b> screens are "
      "applied to single-adult and to couple households, so the two samples are "
      "the output of one construction rather than two.</p>")

    WHY = [
        "The starting file: every French household in the income reference year.",
        "<b>A classification step, not a behavioural one.</b> The model is written "
        "for a decision unit of one adult, or of two partnered adults; a household "
        "with three or more adults, or with two adults who are not partners, does "
        "not have one. Itemised below.",
        "<b>Age.</b> Below " + lit("20", "lower age bound of the estimation sample")
        + " and above " + lit("60", "upper age bound of the estimation sample")
        + " the labour-supply margin is dominated by "
        "schooling and by retirement, which this model does not represent. For a "
        "couple the screen binds on <em>both</em> adults.",
        "<b>Still in education.</b> A full-time student&rsquo;s hours are a "
        "schooling decision rather than a choice from an offer set.",
        "<b>Retirement or disability income.</b> A household drawing a pension, a "
        "disability benefit or a survivor&rsquo;s benefit faces a different "
        "participation margin, and its non-employment state is not the same "
        "object as a job-seeker&rsquo;s.",
        "<b>Labour status in scope.</b> Keeps deciders who are employed, unemployed "
        "or inactive, and drops statuses for which an offer set is not defined.",
        "<b>No other earning or employable member.</b> If a non-decider in the "
        "household is work-capable or is earning, the household budget depends on a "
        "labour supply the model does not represent, and the decision unit would no "
        "longer be the household.",
        "<b>Hours and wage inside the modelled support.</b> Working hours are "
        "floored and capped, and an employed decider&rsquo;s hourly wage must lie "
        "inside the priced range; outside it the alternative cannot be priced "
        "through the tax-benefit simulator at all.",
        "<b>The estimation sample</b>, split by decision unit.",
    ]

    def _flowrow(i):
        b = "sample.flow.%d." % i
        drop = ('<td class="num">&mdash;</td>' if i in (0, 8)
                else '<td class="num">' + a(b + "dropped", "int") + "</td>")
        return ("<tr><td>" + a(b + "step", "raw") + "</td>"
                '<td class="num">' + a(b + "households", "int") + "</td>"
                + drop
                + '<td class="num">' + a(b + "share_of_file", "pct", 1) + "</td>"
                + "<td>" + WHY[i] + "</td></tr>")

    W('<div class="scroll"><table><thead><tr><th>Screen</th>'
      '<th class="num">Households remaining</th><th class="num">Dropped</th>'
      '<th class="num">Share of the file</th><th>Why this screen exists</th>'
      "</tr></thead><tbody>"
      + "".join(_flowrow(i) for i in range(9))
      + "</tbody></table></div>")

    W("<p>The composition screen at the second row removes "
      + a("sample.composition_screen.4.households", "int")
      + " households, and it is worth itemising, because it is the only screen a "
      "reader might mistake for a behavioural restriction:</p>")
    W("<ul>"
      + "".join("<li><b>" + a("sample.composition_screen.%d.households" % i, "int")
                + "</b> &mdash; " + a("sample.composition_screen.%d.reason" % i, "raw")
                + "</li>" for i in range(4))
      + "</ul>")

    W(F.fig("rg_fig1_1_sample_funnel",
            "The sample-construction waterfall: the number of households "
            "surviving each screen, and what each screen removes.",
            "Reproduced from the reader's-guide notebook's frozen export."))

    W("<h3>The two samples come out of one waterfall</h3>")
    W("<p>The table below carries the single-adult and the couple counts side by "
      "side at every step, so the couple sample is visibly the second application "
      "of the same construction. The right-hand column states the screen in the "
      "terms the construction actually uses.</p>")

    def _cwrow(i):
        b = "sample.couples_flow.%d." % i
        return ("<tr><td>" + a(b + "step", "raw") + "</td>"
                '<td class="num">' + a(b + "all", "int") + "</td>"
                '<td class="num">' + a(b + "singles", "int") + "</td>"
                '<td class="num">' + a(b + "couples", "int") + "</td>"
                '<td class="num">' + a(b + "couples_dropped", "int") + "</td>"
                "<td>" + a(b + "screen", "raw") + "</td></tr>")

    W('<div class="scroll"><table><thead><tr><th>Step</th>'
      '<th class="num">All</th><th class="num">Single-adult</th>'
      '<th class="num">Couples</th><th class="num">Couples dropped</th>'
      "<th>What the screen is</th></tr></thead><tbody>"
      + "".join(_cwrow(i) for i in range(8))
      + "</tbody></table></div>")
    W(F.fig("rg_fig11_1_couples_waterfall",
            "The same waterfall with the couple households traced separately.",
            "Reproduced from the reader's-guide notebook's frozen export."))

    # ---- descriptive distributions ---------------------------------------- #
    W("<h3>What the sample looks like</h3>")
    W("<p>Every share below is weighted by the survey weight, so it describes the "
      "population the sample stands for; the counts beside it are unweighted "
      "households. Read these as the setting the model has to reproduce, not as "
      "results.</p>")

    CAT = _AUX["sample"]["categorical"]
    DIM_TITLE = [
        ("sex", "Sex of the decider"),
        ("education", "Education, in three groups"),
        ("employment", "Employment"),
        ("hours band", "Weekly hours, in the bands the model uses"),
        ("occupation (loc4)", "Occupation of the observed job"),
        ("region (drgn1 code categories)", "Region"),
    ]
    body = []
    for dim, title in DIM_TITLE:
        rr = [i for i, r in enumerate(CAT) if r["dimension"] == dim]
        if not rr:
            continue
        body.append('<tr class="grouphead"><td colspan="4">%s</td></tr>' % title)
        for i in rr:
            b = "sample.categorical.%d." % i
            label = a(b + "category", "raw")
            if dim.startswith("region"):
                code = int(str(CAT[i]["category"]).split("=")[-1])
                label = a("sample.region_key.%d.name" % (code - 1), "raw")
            body.append("<tr><td>" + label + "</td>"
                        + '<td class="num">' + a(b + "n", "int") + "</td>"
                        + '<td class="num">' + a(b + "share_unweighted", "pct", 1)
                        + "</td>"
                        + '<td class="num">' + a(b + "share_weighted", "pct", 1)
                        + "</td></tr>")
    body.append('<tr class="grouphead"><td colspan="4">Children in the household'
                "</td></tr>")
    for i in range(len(_AUX["sample"]["children"])):
        b = "sample.children.%d." % i
        body.append("<tr><td>" + a(b + "n_children", "int") + " children</td>"
                    + '<td class="num">' + a(b + "households", "int") + "</td>"
                    + '<td class="num">' + a(b + "share_unweighted", "pct", 1)
                    + "</td>"
                    + '<td class="num">' + a(b + "share_weighted", "pct", 1)
                    + "</td></tr>")
    body.append('<tr class="grouphead"><td colspan="4">Urbanisation of the place '
                "of residence</td></tr>")
    for i in range(3):
        b = "sample.urbanisation.%d." % i
        body.append("<tr><td>" + a(b + "zone", "raw") + "</td>"
                    + '<td class="num">' + a(b + "households", "int") + "</td>"
                    + '<td class="num">' + a(b + "share_unweighted", "pct", 1)
                    + "</td>"
                    + '<td class="num">' + a(b + "share_weighted", "pct", 1)
                    + "</td></tr>")
    W('<div class="scroll"><table><thead><tr><th>Category</th>'
      '<th class="num">Households</th><th class="num">Share, unweighted</th>'
      '<th class="num">Share, weighted</th></tr></thead><tbody>'
      + "".join(body) + "</tbody></table></div>")

    W("<p>Three of those rows are worth a sentence. The sample is majority female "
      "and highly educated, and "
      + a("sample.categorical.5.share_weighted", "pct", 0) + " are employed "
      "&mdash; high, because the screens above removed exactly the groups with low "
      "attachment, which makes this the right denominator for a model of the "
      "labour supply of people who could plausibly be working. Nearly three "
      "quarters of these households have no resident child. And the hours "
      "distribution is not smooth: the band containing the statutory week holds "
      "more households than any other, which is the institutional fact "
      "section&nbsp;6 has to represent.</p>")

    W("<p>The continuous variables, weighted:</p>")
    W('<div class="scroll"><table><thead><tr><th>Variable</th><th>Unit</th>'
      '<th class="num">Mean</th><th class="num">Median</th>'
      '<th class="num">10th pct</th><th class="num">90th pct</th>'
      '<th class="num">Min</th><th class="num">Max</th></tr></thead><tbody>'
      + "".join(
          "<tr><td>" + a("sample.continuous.%d.dimension" % i, "raw") + "</td>"
          + "<td>" + a("sample.continuous.%d.unit" % i, "raw") + "</td>"
          + '<td class="num">' + a("sample.continuous.%d.mean_weighted" % i, "f2")
          + "</td>"
          + '<td class="num">' + a("sample.continuous.%d.median_weighted" % i, "f2")
          + "</td>"
          + '<td class="num">' + a("sample.continuous.%d.p10_weighted" % i, "f2")
          + "</td>"
          + '<td class="num">' + a("sample.continuous.%d.p90_weighted" % i, "f2")
          + "</td>"
          + '<td class="num">' + a("sample.continuous.%d.min" % i, "f2") + "</td>"
          + '<td class="num">' + a("sample.continuous.%d.max" % i, "f2") + "</td>"
          "</tr>" for i in range(len(_AUX["sample"]["continuous"])))
      + "</tbody></table></div>")

    W(F.fig("rg_fig2_2_hours_bands",
            "The observed distribution of weekly hours, with the band structure "
            "the hours factor of the opportunity density uses. The concentration "
            "at the statutory week is the most visible institutional feature in "
            "these data, and section&nbsp;6 explains how the model represents it.",
            "Reproduced from the reader's-guide notebook's frozen export."))
    W(F.fig("rg_fig2_3_wage_age",
            "Observed hourly wages against age, by education group. The level "
            "difference across education and the concavity in experience are what "
            "the wage-offer location of section&nbsp;6 estimates &mdash; there as "
            "a density over the pay a household could be offered, rather than as "
            "a regression on the pay the employed are observed at.",
            "Reproduced from the reader's-guide notebook's frozen export."))
    W(F.fig("rg_fig2_4_occupation_by_sex",
            "Occupation composition of the observed jobs, by sex. The strong sex "
            "difference here is what the occupation factor of the opportunity "
            "density is estimated against.",
            "Reproduced from the reader's-guide notebook's frozen export."))
    W(F.fig("rg_fig2_1_income_distributions",
            "The income distributions in this sample: earned income, non-labour "
            "income, and disposable income after the tax-benefit system. "
            "Non-labour income is the part of the budget that does not move with "
            "the job taken; it enters the endowments-and-needs channel of "
            "section&nbsp;16.",
            "Reproduced from the reader's-guide notebook's frozen export."))

    W("<h3>Observed inequality, before any model</h3>")
    W("<p>The decomposition of sections&nbsp;14&ndash;16 is carried on a "
      "model-based welfare measure rather than on income. It is still worth "
      "knowing what inequality looks like in the raw data, because that is the "
      "quantity a reader arrives with. On <b>observed disposable income</b> in "
      "this sample the weighted <b>Gini coefficient</b> &mdash; a summary of "
      "dispersion running from "
      + lit("0", "the lower limit of the Gini coefficient, a definition")
      + ", when every household has the same income, to "
      + lit("1", "the upper limit of the Gini coefficient, a definition")
      + ", when one household has all of it &mdash; is "
      + a("sample.observed.Gini (weighted)", "f3") + ", with a mean of "
      + a("sample.observed.mean", "f0") + " and a median of "
      + a("sample.observed.median", "f0")
      + " euros a month, and a ratio of the "
      + lit("90th", "a percentile of the observed income distribution")
      + " to the " + lit("10th", "a percentile of the observed income distribution")
      + " percentile of "
      + a("sample.observed.P90/P10", "f2") + ".</p>")
    W(box("warn", "This is not the paper's headline number, and the difference "
                  "is not presentational",
          "<p>Observed disposable income and the welfare measure of "
          "section&nbsp;13 are different objects, and their inequality figures are "
          "not comparable. Disposable income counts the money a household "
          "receives. The welfare measure asks what uniform pay, offered across the "
          "jobs that household can reach, would leave it exactly as well off as it "
          "actually is &mdash; so it credits time not spent working, and it "
          "credits a wide set of reachable jobs even when the job actually taken "
          "is identical. A household working sixty hours for a given income is not "
          "as well off as one working thirty for the same income, and the Gini of "
          "income cannot see that.</p>"))
    W(F.fig("rg_fig3_1_lorenz_and_deciles",
            "Observed disposable income: the Lorenz curve and the decile means. "
            "Descriptive only; no model quantity appears on either axis.",
            "Reproduced from the reader's-guide notebook's frozen export."))

    W("<h3>The variables, and what each one does</h3>")
    W('<div class="scroll"><table><thead><tr><th>Variable</th><th>Construction</th>'
      "<th>Where it enters</th></tr></thead><tbody>"
      "<tr><td><b>Employment</b></td><td>A binary indicator on the alternative: "
      "working or not. The non-employment alternative is structural, not a "
      "zero-hours job.</td><td>Job access (the employment margin) and, through "
      "consumption and leisure, preferences.</td></tr>"
      "<tr><td><b>Hours</b></td><td>Usual weekly hours. Employed alternatives carry a "
      "floor of " + lit("5", "hours floor of the corrected support")
      + " hours per week; below that the alternative is "
      "non-employment rather than a very short job. Priced through "
      + lit("5", "number of hours bands carried by the opportunity block")
      + " mutually exclusive bands plus a residual.</td>"
      "<td>Job access (the hours-opportunity block), leisure, and the budget.</td></tr>"
      "<tr><td><b>Occupation</b></td><td>A "
      + lit("four", "number of task-based occupation groups") + "-group "
      "task-based aggregation of ISCO, with group "
      + lit("1", "the dropped reference occupation group")
      + " the dropped reference.</td>"
      "<td>Occupation access (which groups are reachable) and the wage-offer location "
      "(what each group pays). Both, separately &mdash; that separation is one of the "
      "specification results.</td></tr>"
      "<tr><td><b>Education</b></td><td>Three levels; the middle level is the omitted "
      "reference, with low and high entering as shifters.</td>"
      "<td>The wage-offer location only. It is deliberately excluded from "
      "preferences.</td></tr>"
      "<tr><td><b>Potential experience</b></td><td>Years, entering in levels and "
      "squared.</td><td>The wage-offer location only.</td></tr>"
      "<tr><td><b>Wages</b></td><td>The observed hourly wage for workers, derived from "
      "annual earnings, months worked and usual weekly hours. Modelled as an offer "
      "density, so it is a dependent object, not a regressor.</td>"
      "<td>Earning opportunities; and the budget, through earnings.</td></tr>"
      "<tr><td><b>Household composition and children</b></td>"
      "<td>Number of dependent children, from the household roster. Parent&ndash;child "
      "links are available on the raw frame, so child <em>ages</em> could be "
      "constructed &mdash; see section&nbsp;12.</td>"
      "<td>Preferences (the leisure weight, single women only) and the budget, through "
      "family benefits and the equivalence scale.</td></tr>"
      "<tr><td><b>Region</b></td><td>NUTS-1 indicators, "
      + lit("eight", "number of NUTS-1 region indicators in the access block")
      + " of them in the access block with the omitted one as reference.</td>"
      "<td>Job access only. Excluded from preferences by construction &mdash; that "
      "exclusion is what section&nbsp;17 rests on.</td></tr>"
      "<tr><td><b>Urbanisation</b></td><td>Urban and intermediate indicators, rural "
      "the dropped reference.</td><td>Job access only.</td></tr>"
      "<tr><td><b>Local unemployment rate</b></td><td>A continuous regional "
      "labour-market slack measure.</td><td>Job access only. It is the sharpest "
      "single access regressor in the model.</td></tr>"
      "<tr><td><b>Non-labour resources</b></td><td>Capital income, transfers not "
      "conditioned on work, and other household income that does not vary with the job "
      "taken.</td><td>The budget at every alternative &mdash; hence the "
      "endowments-and-needs channel of section&nbsp;16.</td></tr>"
      "</tbody></table></div>")

    W("<h3>How engine-ready data differ from source data</h3>")
    W('<p>This is the step that most often confuses a reader coming from a reduced-form '
      'paper, and it is worth stating plainly. The source data have <b>one row per '
      'person</b>: the job actually held. The engine-ready data have <b>one row per '
      'alternative</b>: '
      + n("n_alternatives", "int") + ' rows per household, '
      + n("n_priced_rows_singles", "int") + ' rows in total for the singles sample.</p>')
    W("<p>Four things happen between the two:</p>")
    W("<ol>")
    W('<li><b>The choice set is constructed.</b> Each household is given its observed '
      'job plus a set of sampled counterfactual jobs drawn from a proposal '
      'distribution. Section&nbsp;5.</li>')
    W('<li><b>Every alternative is priced.</b> EUROMOD is run on all of them, so each '
      'row carries the disposable income that job would actually deliver.</li>')
    W('<li><b>Consumption and leisure are formed and normalised.</b> Consumption is '
      'disposable income; leisure is the time endowment net of hours; both are scaled '
      'by fixed normalising constants that the estimates are invariant to.</li>')
    W('<li><b>The proposal correction is attached.</b> Each sampled row carries its '
      'log proposal density; the observed row carries zero. Section&nbsp;5.</li>')
    W("</ol>")
    W(box("prov", "Frame provenance",
          "<p>The estimation frame is content-addressed. The frame of record is "
          "<code>fr_p2a_singles2016_regionlive_margqh_floor5_v1</code>, geometry digest "
          "<code>a91b1f81&hellip;</code>, stem digest <code>6f558f5e&hellip;</code>, "
          "at " + n("n_priced_rows_singles", "int") + " rows over "
          + n("n_households_singles", "int") + " households. Every result in this "
          "document binds to those digests. The <code>floor5</code> element is the "
          "five-hour support correction of section&nbsp;8; results produced before it "
          "are retained as history and are not comparable.</p>"))

    # ===================================================================== 4 ==
    W('<h2 id="s4" class="exempt">4. What a latent job is</h2>')

    W('<p>The choice object is not &ldquo;hours&rdquo;. It is a <b>job</b>: a bundle '
      'that has to be fully specified before the tax-benefit system can price it.</p>')

    W('<div class="scroll"><table><thead><tr><th>Component</th><th>Singles</th>'
      "<th>Couples</th></tr></thead><tbody>"
      "<tr><td><b>Employment</b></td><td>Work or not.</td>"
      "<td>A joint pair: each spouse works or not.</td></tr>"
      "<tr><td><b>Hours</b></td><td>Weekly hours if working.</td>"
      "<td>Two hours values, one per spouse.</td></tr>"
      "<tr><td><b>Occupation</b></td><td>One of "
      + lit("four", "number of task-based occupation groups")
      + " task-based groups.</td><td>One group per working spouse.</td></tr>"
      "<tr><td><b>Wage</b></td><td>An hourly offer.</td>"
      "<td>An offer for each working spouse.</td></tr>"
      "<tr><td><b>Consumption</b></td><td>Household disposable income at that job, "
      "from EUROMOD.</td>"
      "<td>Household disposable income at that <em>joint</em> alternative &mdash; a "
      "single household budget, jointly taxed and jointly means-tested.</td></tr>"
      "<tr><td><b>Leisure</b></td><td>Time endowment net of hours.</td>"
      "<td>Two leisure values, one per spouse.</td></tr>"
      "</tbody></table></div>")

    W("<h3>The choice set, and what <em>R</em> is</h3>")
    W('<p>Each household is given ' + n("n_alternatives", "int") + ' alternatives: '
      '<b>R = ' + a("defs.R_reference", "int")
      + '</b> sampled latent jobs, plus the observed one inserted deterministically.</p>')

    W(box("warn", "R is a resolution, not an opportunity count",
          "<p>This is the single most common misreading of the model and it should be "
          "corrected pre-emptively in the talk.</p>"
          "<p><b>R is the number of draws used to approximate an integral.</b> The "
          "model says a household chooses from a <em>continuum</em> of potential jobs "
          "&mdash; hours are continuous, wages are continuous. The likelihood of that "
          "model contains an integral over the job space that has no closed form. "
          "Sampled-choice estimation replaces the integral with a weighted sum over "
          "draws from a known proposal density, with each draw carrying a correction "
          "that removes the sampler&rsquo;s own influence.</p>"
          "<p><b>R is therefore a numerical-integration resolution.</b> It is not a "
          "claim that anyone had " + n("n_alternatives", "int") + " job offers. It is "
          "not a labour-demand object. Raising it makes the integral more accurate and "
          "changes nothing about the economics. Section&nbsp;19 shows what happens "
          "when it is raised: over the ladder "
          + n("drawcount_ladder", "list") + ", the largest movement in any coefficient "
          "at or above the reference resolution is "
          + n("drawcount_max_deviation_geq_reference", "f2") + " of a standard "
          "error &mdash; a fifth of one SE.</p>"
          "<p>The economic opportunity object is the <em>density</em> "
          "<em>g<sub>i</sub></em>, not the sample from it. The density is what has "
          "parameters, what varies with circumstances, and what the welfare "
          "decomposition equalizes.</p>"))

    W(F.fig("figE1_matched_pair",
            "Two real households the model gives the <em>same</em> preference profile "
            "and that took the <em>same</em> observed job, ranked first on the distance "
            "between their estimated opportunity distributions. Same taste, same "
            "outcome, different reachable sets &mdash; the case a common-choice-set "
            "model cannot represent at all."))

    # ===================================================================== 5 ==
    W('<h2 id="s5" class="exempt">5. Proposal sampling and the correction</h2>')

    W('<p>The sampled alternatives have to come from somewhere. That somewhere is the '
      '<b>proposal density</b> <em>q</em>, and the whole validity of the estimator '
      'rests on removing it cleanly from the likelihood afterwards.</p>')

    W("<h3>The four proposal blocks</h3>")
    W("<ol>")
    W('<li><b>Employment.</b> Draw whether the alternative is a working job or the '
      'non-employment state.</li>')
    W('<li><b>Occupation.</b> If working, draw one of the '
      + lit("four", "number of task-based occupation groups") + ' task-based groups.</li>')
    W('<li><b>Hours.</b> If working, draw weekly hours from a <em>mixture</em>: mass '
      'concentrated on focal values (the statutory week, standard full time, common '
      'part-time schedules) together with a spread-out component covering the rest of '
      'the support.</li>')
    W('<li><b>Wage.</b> Draw an hourly offer conditional on the drawn occupation.</li>')
    W("</ol>")
    W('<p>The proposal is a <em>sampler</em>, not a model. It only has to cover the '
      'support and be known exactly. It is deliberately close to the observed '
      'distribution so that draws land where the likelihood has mass, which is a '
      'variance-reduction device and nothing more.</p>')

    W("<h3>The observed job, and why its correction is zero</h3>")
    W('<p>The observed job is <b>inserted deterministically</b> in every '
      'household&rsquo;s set. It is not drawn. Its inclusion probability is one, and '
      'the logarithm of one is zero, so its proposal correction is exactly zero.</p>')
    W('<p>Two things follow, and both get asked. First, this is not a convenience: if '
      'the chosen row were sampled, the likelihood would be conditional on the chosen '
      'row happening to be drawn, which is a different and much worse estimator. '
      'Second, if a sampled row happens to land on the same economic job as the '
      'observed one, the two rows are <b>kept separately with their own '
      'corrections</b> and are not silently deduplicated &mdash; they play different '
      'roles in the estimator.</p>')

    W("<h3>Exact marginal <em>q</em>, and the error it replaced</h3>")
    W('<p>The hours proposal is a mixture, and mixtures have a subtlety that is easy to '
      'get wrong. When a value is drawn from a mixture, the sampler knows which '
      'component produced it &mdash; the <em>label</em>. The density that belongs in '
      'the correction is the <b>marginal</b> density of the value, summing over every '
      'component that could have produced it. It is not the joint density of the '
      'value <em>and</em> its label.</p>')
    W('<p>The earlier convention used the joint. Because focal hours values can be '
      'produced by more than one mixture component, that understated the density at '
      'exactly the values where most of the data sit, and the resulting objective was a '
      'likelihood in the <em>labelled</em> space rather than in the job space the model '
      'is about. Correcting it to the exact marginal changed the proposal correction '
      'and nothing else in the specification, and improved the fit substantially. '
      '<b>Exact marginal <em>q</em> is the final convention</b> for every stochastic '
      'row.</p>')

    W(box("key", "A simple numerical example",
          "<p>Suppose the hours proposal is a two-component mixture and a draw returns "
          "exactly the statutory week. Suppose the focal component would produce that "
          "value with density " + lit("0.30", "illustrative arithmetic, not an estimate")
          + " and the spread-out component would produce it with density "
          + lit("0.05", "illustrative arithmetic, not an estimate") + ".</p>"
          "<div class=\"eq\">"
          "WRONG (joint, labelled space)   q = 0.30          log q = -1.204\n"
          "RIGHT (exact marginal)          q = 0.30 + 0.05   log q = -1.050\n"
          "                                  = 0.35\n"
          "difference in the correction    log(0.35/0.30)    = +0.154 per affected row"
          "</div>"
          "<p>The correction enters the value of every alternative with a minus sign, "
          "so understating <em>q</em> at focal hours <em>inflates</em> those "
          "alternatives&rsquo; values. The model then has to work against an artificial "
          "boost at exactly the hours values where the data concentrate, and the "
          "hours-opportunity coefficients absorb the distortion. That is why the error "
          "mattered for the economics and not only for the arithmetic.</p>"))

    W("<h3>Where the correction sits in the likelihood</h3>")
    W("<p>The value of alternative <em>j</em> to household <em>i</em> is the structural "
      "index minus the log proposal density:</p>")
    W('<div class="eq">'
      "V_ij  =  u_ij                 preferences over consumption and leisure\n"
      "       +  log g^E_ij           job access, including local market access\n"
      "       +  log g^H_ij           the hours-band opportunity\n"
      "       +  log g^Occ_ij         occupation opportunity\n"
      "       +  log g^W_ij           the wage offer's density\n"
      "       -  log q_ij             the proposal correction\n"
      "\n"
      "with   log q_i0 = 0            the observed job, inserted deterministically\n"
      "       log q_ij = log q_marginal(job_ij)   for every sampled row\n"
      "\n"
      "P_i(observed)  =  exp(V_i0) / SUM_j exp(V_ij)\n"
      "negLL          =  - SUM_i  log P_i(observed)"
      "</div>")
    W('<p>The subtraction is the entire content of sampled-choice correction: it makes '
      'the estimator consistent for the parameters of the true continuous model, and '
      'it makes the answer independent of the sampler in the limit. Because it enters '
      'additively and is <em>known</em>, an error in it is not a nuisance &mdash; it is '
      'a misspecification of every alternative&rsquo;s value.</p>')

    # ===================================================================== 6 ==
    W('<h2 id="s6" class="exempt">6. The structural model, complete</h2>')

    W('<p class="lede">The model is written once, for a generic <b>decision '
      'unit</b>, and then applied twice: to a single adult, and to a couple. '
      'Everything in this section is the model itself; the estimates are '
      'section&nbsp;7.</p>')

    W(box("key", "The shape of the argument, before any algebra",
          "<p>A decision unit faces a set of <b>job packages</b>. A package is a "
          "bundle of hours, an occupation and an hourly wage &mdash; and, once the "
          "tax-benefit system has been solved for it, a disposable income. Two "
          "objects govern which package is observed.</p>"
          "<ul>"
          "<li><b>Preferences</b> say how the unit <em>ranks</em> the packages it "
          "can reach. This is a utility function over consumption and time.</li>"
          "<li><b>The opportunity density</b> says how <em>available</em> each "
          "package is to that unit. This is a probability density over the space "
          "of packages, and it differs from one unit to another.</li>"
          "</ul>"
          "<p>The observed job is the package that maximises the sum of the two, "
          "up to an extreme-value shock. Every question in this paper is about "
          "how much of the dispersion in outcomes comes from the first object and "
          "how much from the second.</p>"))

    # ================================================================= generic
    W("<h3>6.1 The generic decision unit</h3>")

    W("<p><b>Utility.</b> The unit values consumption and time, both through a "
      "<b>Box&ndash;Cox transformation</b> &mdash; a flexible one-parameter family "
      "that nests the logarithm and the linear case, and whose parameter measures "
      "how fast marginal value falls off:</p>")
    W(math(r"\mathcal{B}(z;\theta)=\frac{z^{\theta}-1}{\theta},\qquad "
           r"\mathcal{B}(z;0)=\log z .",
           "the Box-Cox transformation",
           "At " + imath(r"\theta=1") + " the transformation is linear and the "
           "marginal value of the good is constant. As " + imath(r"\theta") +
           " falls the function bends: the lower it goes, the faster the value of "
           "an extra unit declines. At " + imath(r"\theta=0") + " it is the "
           "logarithm. Negative values are admissible and mean sharper concavity "
           "still."))

    W("<p>Utility over a package " + imath("j") + " for unit " + imath("i")
      + " is a weighted sum of transformed leisure and transformed consumption:</p>")
    W(math(r"u_{ij}\;=\;\sum_{s\in S_i}\beta_{\ell}^{g(s)}(\mathbf{x}_i)\,"
           r"\mathcal{B}\!\left(\tilde{\ell}_{sij};\theta_{\ell}^{g(s)}\right)"
           r"\;+\;\beta_c\,\mathcal{B}\!\left(\tilde{c}_{ij};\theta_c\right),",
           "utility of a package"))
    W("<p>where " + imath(r"S_i") + " is the set of adults in the decision unit, "
      + imath(r"g(s)") + " is the sex of adult " + imath("s") + ", "
      + imath(r"\tilde\ell_{sij}=(\bar L-h_{sij})/\lambda_\ell") + " is that "
      "adult's leisure in the package (total time less hours worked, in units of "
      + imath(r"\lambda_\ell=10") + " hours), and " + imath(r"\tilde c_{ij}") +
      " is the household's disposable income in the package. The leisure weight "
      "is itself a function of the unit's characteristics:</p>")
    W(math(r"\beta_{\ell}^{g}(\mathbf{x}_i)\;=\;\beta_{\ell 0}^{g}"
           r"+\beta_{\ell a}^{g}a_i+\beta_{\ell a^{2}}^{g}a_i^{2}"
           r"+\mathbb{1}\{g=\text{women}\}\,\beta_{\ell k}^{g}k_i ,",
           "how the value of time varies across units"))
    W("<p>with " + imath("a_i") + " age, centred and measured in decades, and "
      + imath("k_i") + " the number of resident children. <b>"
      + imath(r"\beta_c\equiv 1") + " is a normalisation, not an estimate</b>: "
      "utility in a discrete-choice model is identified only up to scale, and "
      "fixing the consumption coefficient is what fixes that scale. It is also "
      "what makes the money metric of section&nbsp;13 well defined, because it "
      "puts utility on a euro footing.</p>")

    W("<p><b>The opportunity density.</b> Availability is a product of four "
      "factors, each equal to one at its own reference, and the last three "
      "switched off on the non-employment package:</p>")
    W(math(r"g_{ij}\;=\;g^{E}_{ij}\cdot g^{H}_{ij}\cdot g^{\mathrm{Occ}}_{ij}"
           r"\cdot g^{W}_{ij},\qquad "
           r"E_{ij}=\mathbb{1}\{\text{the package involves work}\}.",
           "the opportunity density, four factors"))
    W("<p>They answer four different questions about the market a unit faces: "
      "<b>is work available at all</b>, <b>at which hours</b>, <b>in which "
      "occupation</b>, and <b>at what pay</b>. Section&nbsp;6.3 takes them one at "
      "a time.</p>")

    W("<p><b>The index, and why the two objects must be separated by exclusion "
      "restrictions.</b> Preferences and availability enter one index "
      "additively:</p>")
    W(math(r"V_{ij}\;=\;\underbrace{u_{ij}}_{\text{how it is ranked}}"
           r"+\underbrace{\log g_{ij}}_{\text{how available it is}}"
           r"-\underbrace{\log q_{ij}}_{\text{sampling correction}} .",
           "the index of a package"))
    W("<p>Because the two enter as a sum, their <em>total</em> is identified by "
      "the choices, but their <em>parts</em> are not &mdash; unless some variables "
      "move one and not the other. That is what the exclusion restrictions do: "
      "the local unemployment rate, the region and the urbanisation of the place "
      "of residence enter availability and never preferences; age and children "
      "enter preferences and never availability. Nothing about the functional "
      "form does this work.</p>")

    W("<p><b>The sampled-alternatives likelihood.</b> The set of conceivable job "
      "packages is far too large to enumerate, so it is sampled. Each unit "
      "carries its observed package plus " + n("n_alternatives", "int")
      + " packages in all &mdash; the observed one plus drawn alternatives "
      "from a known <b>proposal density</b> "
      + imath("q_{ij}") + ", giving a choice set of " + n("n_alternatives", "int")
      + ". Subtracting " + imath(r"\log q_{ij}") + " from the index &mdash; the "
      "<b>sampling correction</b> &mdash; makes the likelihood over the sampled "
      "set consistent for the model over the full set:</p>")
    W(math(r"P_i\;=\;\frac{\exp V_{i j^{*}_i}}{\sum_{j\in\mathcal{C}_i}\exp V_{ij}},"
           r"\qquad \hat\theta=\arg\min_\theta\;-\!\sum_{i=1}^{N}\log P_i(\theta).",
           "the sampled-alternatives likelihood"))
    W("<p>The proposal density is <b>computation, not economics</b>. It is chosen "
      "by the analyst, it carries no parameter of interest, and it cancels from "
      "everything the paper reports. It is never an opportunity, an offer or an "
      "availability: those words belong to " + imath("g_{ij}") + " alone.</p>")

    # ============================================================ instantiation
    W("<h3>6.2 The same model, applied twice</h3>")
    W("<p>Only the decision unit changes. Everything above is untouched.</p>")

    W('<div class="scroll"><table><thead><tr><th></th>'
      "<th>Application 1 &mdash; the single adult</th>"
      "<th>Application 2 &mdash; the couple</th></tr></thead><tbody>"

      "<tr><td><b>The unit</b></td>"
      "<td>One adult. " + n("n_households_singles", "int") + " households.</td>"
      "<td>Two partnered adults, decided jointly. "
      + n("n_households_couples", "int") + " households.</td></tr>"

      "<tr><td><b>Leisure terms in utility</b></td>"
      "<td><b>One.</b> The sum over " + imath("S_i") + " has a single term, so "
      "utility is a function of one leisure and one consumption.</td>"
      "<td><b>Two.</b> The sum has a male and a female term, each with its own "
      "leisure weight and its own curvature. Consumption remains a single "
      "household-level argument.</td></tr>"

      "<tr><td><b>An alternative</b></td>"
      "<td>A job package for the adult, or non-employment.</td>"
      "<td>A <b>joint alternative</b>: a package for <em>each</em> spouse "
      "simultaneously, including the case where one or both do not work. The "
      "couple chooses a pair, not two things separately.</td></tr>"

      "<tr><td><b>The budget</b></td>"
      "<td>The household's disposable income under the actual tax-benefit rules, "
      "given that adult's earnings and the household's non-labour income.</td>"
      "<td>The <b>household</b> budget, priced once for the pair. This is not "
      "presentational: French income tax and means-tested benefits are assessed "
      "on the household, so one spouse's earnings change the other's effective "
      "return to work. Pricing the pair jointly is the only way to represent "
      "that.</td></tr>"

      "<tr><td><b>Participation regimes</b></td>"
      "<td>Two: works, or does not.</td>"
      "<td><b>Four</b>, and the draws respect them. A joint alternative falls "
      "into one of the four regimes &mdash; neither works, only the man works, "
      "only the woman works, both work &mdash; and the sampler is constructed so "
      "that each regime receives its own share of the drawn alternatives rather "
      "than being left to chance. Without that, the rare regimes would be "
      "represented by too few draws to estimate against.</td></tr>"

      "<tr><td><b>Opportunity density</b></td>"
      "<td>The four factors, once.</td>"
      "<td>The four factors, <b>per spouse</b>, on a shared parameter vector with "
      "per-sex coordinates: each spouse has an employment margin, an hours "
      "profile and an occupation profile of their own, while the wage-offer "
      "technology and the local access terms are common.</td></tr>"

      "<tr><td><b>What is <em>not</em> in the couple model</b></td>"
      "<td>&mdash;</td>"
      "<td>A term in <em>both</em> spouses' leisure &mdash; the natural way for "
      "one spouse's time at home to change the value of the other's. It is "
      "<b>absent from the specification</b>, not estimated and set to zero. "
      "Section&nbsp;11 gives the reason and the consequence.</td></tr>"
      "</tbody></table></div>")

    W(box("warn", "One model, two applications - and why the couple is not an "
                  "appendix",
          "<p>The couple is the second application of the model above, estimated "
          "on the same frame with the same screens, the same proposal, the same "
          "correction and the same likelihood. Its parameters appear beside the "
          "singles parameters in section&nbsp;7, block by block, for that "
          "reason.</p>"
          "<p>What makes the single-adult sample the headline is not that it came "
          "first. It is that in a one-adult household the <b>welfare unit and the "
          "decision unit coincide</b>, so a money-metric welfare level is well "
          "defined without taking a position on how a couple divides its "
          "resources. Section&nbsp;11 states the couple's own limitation "
          "plainly.</p>"))

    # ============================================================ the densities
    W("<h3>6.3 The four factors of the opportunity density</h3>")
    W("<p>Each factor is a statement about the market, not about the person's "
      "taste. Each is normalised so that it equals one at a stated reference, "
      "which is what makes its coefficients readable as ratios.</p>")

    # ---- (a) employment access
    W("<h4>(a) Employment access &mdash; is work available at all?</h4>")
    W("<p><b>What it says about the market.</b> How much density the opportunity "
      "distribution places on <em>being employed at all</em> rather than on the "
      "non-employment package, and how that level is tilted by the labour market "
      "the household lives in. It is a level shift applied to every working "
      "package alike.</p>")
    W(math(r"\log g^{E}_{ij}=E_{ij}\Bigl[\beta_{E}"
           r"+\beta_{s}\,s_i"
           r"+\textstyle\sum_{r=2}^{8}\beta_{r}\mathbb{1}\{R_i=r\}"
           r"+\beta_{u}U_i+\beta_{m}M_i\Bigr]",
           "employment access"))
    W("<p><b>Reference.</b> The non-employment package, at which the factor is "
      "one by construction, and &mdash; among working packages &mdash; a "
      "household in the omitted region living in a rural zone. <b>Regressors.</b> "
      + imath("s_i") + " is the <b>unemployment rate of the household's own "
      "group</b>, defined by region, education and sex, and looked up from an "
      "external source rather than estimated: it is the exclusion restriction "
      "that identifies access separately from taste. " + imath("R_i") + " is the "
      "region of residence, seven indicators against an omitted eighth. "
      + imath("U_i") + " and " + imath("M_i") + " are urban and intermediate "
      "residence against rural. <b>None of these appears in preferences</b>, "
      "which is what makes the geographic exercise of section&nbsp;17 a "
      "well-defined operation.</p>")

    # ---- (b) hours
    W("<h4>(b) Hours &mdash; at which hours is work available?</h4>")
    W("<p><b>What it says about the market.</b> Employers do not post a smooth "
      "continuum of weekly hours. They post a few conventional lengths, and in "
      "France one of them is written into the statute. This factor is a step "
      "density over hours bands, plus a separate mass point at the statutory "
      "week.</p>")
    W(math(r"\log g^{H}_{ij}=\sum_{b}\beta_{b}\,\mathbb{1}\{h_{ij}\in B_b\}"
           r"\;+\;\beta_{h,\mathrm{F35}}\,\mathbb{1}\{h_{ij}\in B_{\mathrm{F35}}\},"
           r"\qquad \beta_{\mathrm{F35}}\equiv 0 \ \text{as a band step}",
           "the hours-offer density"))
    W("<p><b>Reference and normalisation, kept apart.</b> The step structure is "
      "read against the hours regions the bands do not cover <em>and</em> against "
      "the statutory band, both at zero: that is the meaning of "
      + imath(r"\beta_{\mathrm{F35}}\equiv 0") + ", and it is why only four band "
      "coefficients are estimated. The preferred specification then adds "
      "<b>one separate coefficient</b> on the statutory-week indicator, over and "
      "above the band structure. The two are different objects and the report "
      "never conflates them: the first fixes the origin, the second is an "
      "estimated feature of the offer distribution.</p>")

    # ---- (c) occupation
    W("<h4>(c) Occupation &mdash; which kinds of job are reachable?</h4>")
    W("<p><b>What it says about the market.</b> How reachable each of four "
      "occupation groups is, estimated separately for men and for women. This is "
      "<b>access, not pay</b>: what each group pays is the next factor. Keeping "
      "them apart is what lets the model say that an occupation is well paid "
      "<em>and</em> hard to get into &mdash; something a single occupation "
      "coefficient could not express.</p>")
    W(math(r"\log g^{\mathrm{Occ}}_{ij}=E_{ij}\sum_{k=2}^{4}"
           r"\beta^{\mathrm{occ}}_{k,g}\,\mathbb{1}\{o_{ij}=k\},"
           r"\qquad \beta^{\mathrm{occ}}_{1,g}\equiv 0",
           "occupation availability"))
    W("<p><b>Reference.</b> Occupation group " + lit("1", "an occupation group label")
      + ", whose coefficient is fixed at zero for each sex; the other three "
      "are read against it. <b>Regressor.</b> "
      "The occupation of the package, in four groups built from the standard "
      "occupational classification.</p>")

    # ---- (d) wage offers
    W("<h4>(d) Wage offers &mdash; at what pay?</h4>")
    W("<p><b>What it says about the market.</b> Conditional on an occupation, the "
      "pay a household could be offered is a distribution, not a number. This "
      "factor is a log-normal density over the hourly wage whose <em>centre</em> "
      "depends on the household's schooling and experience and on the occupation "
      "of the package, and whose spread is common to everyone.</p>")
    W(math(r"\mu_{ij}=\beta_{w0}+\beta_{wL}L_i+\beta_{wH}H_i+\beta_{wx}x_i"
           r"+\beta_{wx^{2}}x_i^{2}+\textstyle\sum_{k}\delta_{\mathrm{occ},k}"
           r"\mathbb{1}\{o_{ij}=k\}",
           "the centre of the wage-offer distribution"))
    W(math(r"\log g^{W}_{ij}=E_{ij}\Bigl[-\tfrac12\Bigl("
           r"\tfrac{\log w_{ij}-\mu_{ij}}{\sigma}\Bigr)^{2}"
           r"-\log\sigma-\tfrac12\log 2\pi-\log w_{ij}\Bigr]",
           "the wage-offer density"))
    W("<p><b>Reference.</b> Middle education, occupation group "
      + lit("1", "an occupation group label") + ", at the "
      "experience profile's origin. <b>Regressors.</b> " + imath("L_i")
      + " and " + imath("H_i") + " are low and high education against the middle "
      "group; " + imath("x_i") + " is potential experience, entering as a "
      "quadratic so the profile can rise and then flatten. The final "
      + imath(r"-\log w_{ij}") + " term is the <b>Jacobian</b> of the change of "
      "variable from the log wage to the wage itself &mdash; it is there because "
      "the object being chosen is the wage, not its logarithm, and omitting it "
      "would tilt the density.</p>")
    W(box("key", "Why this is an <em>opportunity</em> and not a Mincer regression",
          "<p>The same variables &mdash; schooling, experience &mdash; appear in "
          "a conventional wage regression. The difference is the object being "
          "described. A wage regression describes the pay of <b>the people "
          "observed working</b>. This density describes the pay attached to a "
          "package <b>a household could be offered</b>, including packages it did "
          "not take and occupations it is not in. It is estimated jointly with "
          "the rest of the model from choices, not fitted to observed earnings, "
          "and it is carried <em>inside</em> the opportunity set.</p>"
          "<p>The reading that follows is deliberate: education shifts where a "
          "household's offer distribution sits. That is a statement about "
          "<b>observed earning capacity</b>, and section&nbsp;14.4 is explicit "
          "that it is not a statement about ability.</p>"))

    # ---- the worked household
    W("<h3>6.4 One household, one package, all four factors</h3>")
    W("<p>The four factors multiply. Because each is normalised to one at its own "
      "reference, the availability weight of a package can be read as a product "
      "of ratios against a reference package, and each ratio is "
      + imath(r"e^{\beta}") + " for the coefficient concerned. That is the whole "
      "arithmetic, and it is worth doing once explicitly.</p>")
    W("<p><b>The reference package</b> is: work is available; hours in the region "
      "the bands do not cover; occupation group "
      + lit("1", "an occupation group label") + "; and a wage at the centre of "
      "the offer distribution for that household. <b>The package we build</b> is "
      "a full-time job just above the statutory week, in occupation group "
      + lit("4", "an occupation group label") + ", for "
      "a man, at the centre of his own offer distribution. Reading down the "
      "column, each row multiplies the one above it.</p>")

    def _wrow(label, key, what):
        return ("<tr><td>" + label + "</td>"
                "<td><code>" + key + "</code></td>"
                '<td class="num">' + a("params41." + key + ".estimate", "f4")
                + "</td>"
                '<td class="num">' + a("ratio." + key + ".exp", "f2") + "&times;</td>"
                "<td>" + what + "</td></tr>")

    W('<div class="scroll"><table><thead><tr><th>Step</th><th>Coefficient</th>'
      '<th class="num">Estimate</th><th class="num">Multiplies availability by</th>'
      "<th>What that step says</th></tr></thead><tbody>"
      + _wrow("<b>" + lit("1", "a step number in the worked example") + ". Is work available at all?</b>", "beta_E",
              "The employment level. Working packages start far below the "
              "non-employment package in availability: this is the fixed cost of "
              "having a job at all, on the offer side.")
      + _wrow("<b>" + lit("2", "a step number in the worked example") + ". Tilt for the local market</b>", "beta_E_gsur",
              "Multiplied for each unit of the household's own group unemployment "
              "rate. A worse local market for this region, education and sex "
              "lowers the availability of every working package.")
      + _wrow("<b>" + lit("3", "a step number in the worked example") + ". At which hours?</b>", "beta_h_ft",
              "The band just above the statutory week, against the uncovered "
              "hours region. Full-time work is an order of magnitude more "
              "available than the hours nobody posts.")
      + _wrow("<b>" + lit("4", "a step number in the worked example") + ". In which occupation?</b>", "beta_occ_4_m",
              "Occupation group " + lit("4", "an occupation group label") + " against group "
              + lit("1", "an occupation group label") + ", for a man. Close to one here: "
              "for men these two groups are about equally reachable.")
      + "<tr><td><b>" + lit("5", "a step number in the worked example") + ". At what pay?</b></td>"
      "<td><code>sigma</code></td>"
      '<td class="num">' + a("params41.sigma.estimate", "f4") + "</td>"
      '<td class="num">&mdash;</td>'
      "<td>The wage factor is a density rather than a ratio against a reference "
      "category: it is highest at the centre of the household's own offer "
      "distribution and falls away from it at a rate set by the common spread. "
      "A package paying far above or below that centre is correspondingly less "
      "available.</td></tr>"
      "</tbody></table></div>")
    W("<p>Multiply the four ratios and you have how much more, or less, available "
      "this package is for this household than the reference package &mdash; "
      "before any preference has been consulted. The household's <em>choice</em> "
      "then weighs that availability against how it ranks the package. Two "
      "households with identical tastes and different values of the group "
      "unemployment rate face different products at step 2, and that difference "
      "is exactly what the decomposition of sections&nbsp;14&ndash;16 "
      "attributes.</p>")
    W(box("warn", "What these ratios are, and are not",
          "<p>They are properties of the <b>estimated offer density</b>: how much "
          "weight the fitted distribution of available packages places on one "
          "region of the package space relative to another. They are not "
          "vacancy counts, they are not causal effects of any policy or "
          "characteristic, and they are conditional on the specification and the "
          "exclusion restrictions above.</p>"))

    W(box("say", "The one-sentence version",
          "<p>&ldquo;A household&rsquo;s observed job maximises its preferences "
          "over a set of jobs it did not choose; the model estimates the density "
          "of that set and the preferences jointly, with the tax-benefit system "
          "solved exactly at every alternative.&rdquo;</p>"))

    return H
