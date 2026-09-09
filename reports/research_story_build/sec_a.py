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
    W('<p class="lede"><b>Random Utility&ndash;Random Opportunity (RURO)</b> is a '
      'job-choice model in which random utility ranks alternatives while a separate, '
      'household-specific opportunity density governs which jobs are available. This '
      'paper asks how much inequality in money-metric well-being is associated with '
      'unequal job access and unequal earning opportunities rather than heterogeneous '
      'preferences, after separately accounting for non-labour resources and household '
      'composition.</p>')

    W("<h3>The research question</h3>")
    W('<p>Standard discrete-choice labour-supply models can allow '
      'household-specific budgets and heterogeneous tastes while using a common menu '
      'of hours or placing limited structure on job availability. When '
      'household-specific access restrictions are omitted, estimated preference '
      'parameters may partly capture those restrictions. This paper makes the '
      'opportunity mechanism explicit and examines its consequences for welfare '
      'measurement and attribution.</p>')
    W('<p>This paper asks what happens when the common-opportunity restriction is relaxed. It estimates a '
      'model in which available alternatives are generated from an '
      '<em>individual-specific opportunity distribution</em> &mdash; how likely '
      'employment is at all, which '
      'hours are on offer, which occupations are reachable, and what pay each of them '
      'carries &mdash; jointly with the preferences that rank the jobs that are '
      'reachable. It then asks how much of the inequality in a preference-respecting '
      'welfare measure is attributable to preferences and how much to the environment '
      'people face.</p>')

    W("<h3>The contribution</h3>")
    W("<ol>")
    W('<li><b>An integrated empirical architecture.</b> Joint estimation of tastes and '
      'opportunities is inherited from the RURO and latent-jobs literature. The exact '
      'increment here is to carry explicitly modelled job access and wage-offer '
      'opportunities through estimation, money-metric welfare and nested inequality '
      'attribution, and then compare that accounting with a re-estimated '
      'common-opportunity model.</li>')
    W('<li><b>A welfare decomposition that respects preferences and is algebraically exhaustive.</b> '
      'The preference and environment contributions are Shapley/Owen values on an '
      'explicit cooperative game. Under the current implementation, the grand coalition closes: '
      'equalizing everything drives measured inequality to <span class="mono">'
      + n("state_I11_female_raw", "sci", 1) + "</span> Gini points (RQMC band "
      + n("state_I11_female_raw__rqmc_band", "range")
      + "), numerically zero. This is an accounting identity, not identification, and "
      "must be recomputed after the estimator, support and resource corrections.</li>")
    W('<li><b>A benchmark that prices the common-opportunity restriction itself.</b> The same '
      'welfare machinery is run on a re-estimated model in which everyone faces the '
      'same opportunities. The comparison shows exactly what is lost, and &mdash; the '
      'more surprising result &mdash; where the lost attribution actually goes.</li>')
    W('<li><b>A nested reading of the environment</b> into job access, earning '
      'opportunities and household endowments and needs, and of job access further '
      'into its geographic and non-geographic parts, each closing as an exact '
      'identity rather than as an approximation.</li>')
    W("</ol>")

    W(box("key", "Weights and three uncertainties, defined before the results",
          "<div class=\"exempt\"><p><b>Survey weights</b> make descriptive and welfare aggregates represent "
          "the target population; they do not enter the unweighted summed estimation "
          "criterion. <b>Household-cluster-robust CR1 inference</b> uses one score per "
          "household, permits arbitrary dependence among that household's alternative "
          "rows, assumes independence across households, and applies the adopted "
          "finite-sample factor " + imath(r"G/(G-K_I)") + " on interior coordinates. "
          "A <b>conditional parameter interval</b> propagates that CR1 covariance while "
          "holding the active set, model, data, policy build and normative reference "
          "fixed.</p><p><b>Randomized quasi-Monte Carlo (RQMC)</b> uses randomized, "
          "deliberately well-spread integration points for latent-job integrals. A "
          "<b>leave-one-scramble-out jackknife</b> omits one complete independent "
          "scramble, recomputes the entire statistic and uses variation across those "
          "replicates as a numerical-integration band&mdash;not a sampling confidence "
          "interval. The third uncertainty is a <b>normative-reference range</b>, the "
          "movement across defensible reference households. Numerical RQMC bands, "
          "conditional CR1 parameter intervals and normative-reference ranges answer "
          "different questions and are never pooled.</p></div>"))

    W("<h3>What the current-implementation results say &mdash; and do not say</h3>")
    W('<p><b>Status: historical bridge, not a corrected estimate.</b> Under the '
      'criterion and unbounded wage density presently implemented for single-adult '
      'households in France, measured welfare inequality is '
      + n("state_I00_female_raw", "f3") + ' Gini points on the raw basis (RQMC band '
      + n("state_I00_female_raw__rqmc_band", "range") + '). Of that, '
      'preferences account for ' + n("C_pref_female_raw_share", "pct", 1)
      + ' &mdash; parameter interval '
      + n("s_pref_female_raw__cr1_interval", "rangepct", 1)
      + ' &mdash; and the non-preference environment for '
      + n("C_env_female_raw_share", "pct", 1) + ', parameter interval '
      + n("s_env_female_raw__cr1_interval", "rangepct", 1)
      + '. Integration bands and parameter intervals are two different objects '
      'and are never merged. The older nested resource/composition split is stale '
      'after the field reclassification and is not a current finding. In that historical split, household '
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
      'moves with the choice of reference household. Normative-reference ranges, '
      'conditional parameter intervals and numerical-integration bands are reported '
      'as three different uncertainty objects; the evidence does not rank one as '
      'uniformly dominant. The corrected estimator, support and dependent downstream '
      'statistics are pending, so no final magnitude or component ordering can yet be drawn.</p>')

    W(box("warn", "The one claim this paper does not make",
          "<p>None of this is causal. No component is the effect of the French "
          "tax-benefit system, of living in one region rather than another, or of any "
          "policy. Every contribution is a model-implied attribution under a "
          "<em>fixed</em> policy system, holding estimated preferences and the observed "
          "sample frame constant. Section&nbsp;20 states the full list of what is not "
          "identified.</p>"))

    W(F.fig("figT1_conceptual",
            "The whole paper in one picture. A household ranks the alternatives "
            "generated by its opportunity process using its preferences; the chosen "
            "job is therefore not itself an unselected opportunity draw. Two households "
            "can end up in the same job for opposite "
            "reasons, and in different jobs for no preference reason at all. The "
            "estimation separates the two surfaces; the welfare stage equalizes them "
            "one at a time.",
            "Schematic. Drawn from stylised parameters chosen for legibility; no axis "
            "carries an estimated quantity."))

    W(box("key", "How to use this document",
          "<p>The report moves from question and literature through data, the shared "
          "household framework, both applications, estimation and fit. It then builds "
          "money-metric welfare and inequality attribution step by step before turning "
          "to results, comparisons, uncertainty and limitations. A compact scientific "
          "history follows the limitations. Section 21 is the "
          "hands-on reproduction guide keyed to the research notebook; and section 22 "
      "seminar question bank. Literature positioning and the bibliography are in "
      "section&nbsp;2. Every numeral in the document is rendered from an embedded "
          "data block at page load &mdash; hover any bolded number to see its key, its "
          "definition and the data file it was read from. Section&nbsp;23 audits "
          "that claim mechanically.</p>"))

    # ===================================================================== 2 ==
    W('<h2 id="s2" class="exempt">2. The original economic problem</h2>')

    W('<p>Everything in the paper follows from one distinction, and the whole '
      'identification argument is about whether that distinction can be made from '
      'choice data at all.</p>')

    W("<h3>Four literature strands and the exact incremental contribution</h3>")
    W('<p><b>Latent jobs and constrained labour supply.</b> Aaberge, Dagsvik and '
      'Str&oslash;m; Aaberge, Colombino and Wennemo; Dagsvik and Jia; and Cap&eacute;au, '
      'Decoster and Dekkers establish the random-job/opportunity tradition and its '
      'identification restrictions. Jointly estimating preferences and opportunities '
      'is not invented here. <b>Heterogeneous-preference welfare.</b> Decoster and Haan, '
      'Bargain and coauthors, and Decancq, Fleurbaey and Schokkaert show why welfare '
      'measurement depends on heterogeneous tastes and an explicit normative reference. '
      '<b>Responsibility-sensitive job-choice welfare.</b> Jacquet, Jia and Thoresen '
      'compare standard and circumstance-only compensating variation for a tax reform; '
      'this paper instead studies cross-sectional well-being levels and counterfactual '
      'inequality attribution. <b>Distributional decomposition.</b> Shorrocks and the '
      'grouped Owen implementation described by Audoly and coauthors allocate '
      'interactions; they neither identify the structural blocks nor determine the '
      'ethical responsibility boundary.</p>')
    W('<p><b>Incremental contribution.</b> The paper integrates these strands by '
      'carrying estimated job-access and wage-offer opportunities into a '
      'coalition-consistent money metric and a nested inequality decomposition, with a '
      're-estimated household-common opportunity benchmark. No claim is made that any '
      'single ingredient is new.</p>')

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

    W('<details class="technical"><summary><b>Bibliography (existing literature '
      'corpus)</b></summary><div class="exempt"><ul>'
      '<li>Aaberge, Rolf, John K. Dagsvik, and Steinar Str&oslash;m. 1995. '
      '&ldquo;Labor Supply Responses and Welfare Effects of Tax Reforms.&rdquo; '
      '<i>Scandinavian Journal of Economics</i> 97(4): 635&ndash;659.</li>'
      '<li>Aaberge, R., U. Colombino, and T. Wennemo. 2009. &ldquo;Evaluating '
      'Alternative Representations of the Choice Sets in Models of Labor '
      'Supply.&rdquo; <i>Journal of Economic Surveys</i> 23(3): 586&ndash;612.</li>'
      '<li>Audoly, R., R. McGee, S. Ocampo, and G. Paz-Pardo. 2025. &ldquo;A '
      'Practitioner&rsquo;s Note on the Shapley-Owen-Shorrocks Decomposition.&rdquo; '
      'Federal Reserve Bank of New York Staff Report 1163.</li>'
      '<li>Bargain, Olivier, Andr&eacute; Decoster, Mathias Dolls, Dirk Neumann, '
      'Andreas Peichl, and Sebastian Siegloch. 2013. &ldquo;Welfare, labor supply '
      'and heterogeneous preferences: evidence for Europe and the US.&rdquo; '
      '<i>Social Choice and Welfare</i> 41: 789&ndash;817.</li>'
      '<li>Cap&eacute;au, B., A. Decoster, and G. Dekkers. 2016. &ldquo;Estimating '
      'and Simulating with a Random Utility Random Opportunity Model of Job '
      'Choice.&rdquo; <i>International Journal of Microsimulation</i> 9(2): '
      '144&ndash;191.</li>'
      '<li>Dagsvik, John K., and Zhiyang Jia. 2016. &ldquo;Labor Supply as a '
      'Choice Among Latent Jobs: Unobserved Heterogeneity and Identification.&rdquo; '
      '<i>Journal of Applied Econometrics</i> 31(3): 487&ndash;506.</li>'
      '<li>Decancq, Koen, Marc Fleurbaey, and Erik Schokkaert. 2015. '
      '&ldquo;Happiness, Equivalent Incomes and Respect for Individual '
      'Preferences.&rdquo; <i>Economica</i> 82(S1): 1082&ndash;1106.</li>'
      '<li>Decoster, Andr&eacute;, and Peter Haan. 2015. &ldquo;Empirical Welfare '
      'Analysis with Preference Heterogeneity.&rdquo; <i>International Tax and '
      'Public Finance</i> 22(2): 224&ndash;251.</li>'
      '<li>Jacquet, Laurence, Zhiyang Jia, and Thor O. Thoresen. 2026. '
      '&ldquo;How Much Does Responsibility Matter in Fairness Measurement?&rdquo; '
      'CESifo Working Paper 12418.</li>'
      '<li>Shorrocks, Anthony F. 2013. &ldquo;Decomposition Procedures for '
      'Distributional Analysis.&rdquo; <i>Journal of Economic Inequality</i> 11: '
      '99&ndash;126.</li>'
      '<li>Sutherland, Holly, and Francesco Figari. 2013. &ldquo;EUROMOD: The '
      'European Union Tax-Benefit Microsimulation Model.&rdquo; EUROMOD Working '
      'Paper EM8/13.</li>'
      '<li>van Soest, Arthur. 1995. &ldquo;Structural Models of Family Labor '
      'Supply.&rdquo; <i>Journal of Human Resources</i> 30(1): 63&ndash;88.</li>'
      '</ul><p>Entries are copied from <code>Literature/Literature_collection.md</code>; '
      'this is the report bibliography, not a claim-complete literature survey.</p>'
      '</div></details>')

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
      "disposable income for that household under the coded policy rules, inputs and "
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
          "would generate for that household under the coded France policy system. "
          "Those incomes are frozen into the estimation frame. Estimation then reads "
          "them. The source audit establishes the connector release, model root, "
          "production policy-file digest and the <code>FR_2015</code> system binding; the compact "
          "reproducibility appendix records those identifiers.</p><p>The consequence "
          "is that the budget constraint is <b>non-linear "
          "and exactly evaluated within the frozen build</b>, with every coded kink, "
          "benefit withdrawal and interaction, rather than a linearised net wage. "
          "This does not claim that actual taxes, take-up or incomes are observed "
          "without error. The cost "
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
        "restricted to the model support and capped, and an employed decider&rsquo;s "
        "hourly wage must lie inside the research support. These are estimation "
        "restrictions, not limits on what EUROMOD can calculate.",
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
            "One common sample-construction funnel branching to the corrected final "
            "single-adult and couple samples. The correction preserves the observed "
            "six-to-nine-hour choices of seven workers; it does not impose a ten-hour "
            "minimum.",
            "Regenerated from the certified funnel and both frozen final frames."))

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
      "&mdash; high partly because the screens exclude students, retirees and other "
      "out-of-scope households. Estimates describe these retained prime-age decision "
      "units and need not generalize to the excluded population. Nearly three "
      "quarters of these households have no resident child. And the hours "
      "distribution is not smooth: the band containing the statutory week holds "
      "more households than any other, which is the institutional fact "
      "section&nbsp;6 has to represent.</p>")

    W("<p>The legacy singles table below is retained as a frozen descriptive export. "
      "The refreshed plots that follow are computed from the final corrected chosen "
      "rows for both populations; the final singles minimum employed hours is "
      + a("final_desc.minimum_employed_hours.singles", "f0") + ", not ten.</p>")
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
            "Observed continuous weekly hours for employed singles and, separately, "
            "men and women in couples. Histogram bins are descriptive; the shaded "
            "interval is the distinct structural density band from "
            + a("defs.f35_lo", "f1") + " to " + a("defs.f35_hi", "f1") + ".",
            "Regenerated from the corrected floor-five final chosen rows."))
    W(F.fig("rg_fig2_3_wage_age",
            "Separate final-sample distributions of age and observed hourly wages for "
            "workers. This is not a wage-against-age profile; observed-worker wages "
            "are selected outcomes rather than the latent wage-offer density.",
            "Regenerated from corrected singles and clean-couples chosen rows."))
    W(F.fig("rg_fig2_4_occupation_by_sex",
            "Survey-weighted occupation composition among employed singles, coupled "
            "men and coupled women. Categories are the paper's research aggregation "
            "of ISCO-08, not official ILO task classes.",
            "Regenerated from both final chosen-row samples."))
    W(F.fig("rg_fig2_1_income_distributions",
            "Final-sample household disposable consumption, shown raw within "
            "household type and after the disclosed modified-OECD scale. Household "
            "income is counted once per couple. This is neither earned income nor a "
            "decomposition of resource inputs.",
            "Regenerated from final chosen rows and the executed equivalence rule."))
    W(F.fig("rg_fig2_5_resource_inputs",
            "Actual frozen resource inputs ypp, yse, yiy, ypr, ypt and yot: the "
            "survey-weighted share of final households with a non-zero recorded value, "
            "by household type. Newly simulated means-tested benefits are outputs and "
            "are not relabelled as fixed resources.",
            "Regenerated from the frozen France input and final household identifiers. "
            "Field-level units and time bases are UNRESOLVED B1, so the plot reports "
            "incidence rather than guessing units."))

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
            "Survey-weighted Lorenz curves of final-sample disposable consumption for "
            "singles and couples, raw within type and modified-OECD equivalized. "
            "Descriptive only; no welfare quantity appears on either axis.",
            "Regenerated from both final chosen-row samples using survey weights."))

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
      "<tr><td><b>Occupation</b></td><td class=\"exempt\">The International Standard Classification "
      "of Occupations, 2008 vintage (ISCO-08), is collapsed into a "
      + lit("four", "number of research occupation groups") + "-group research "
      "aggregation: group 1 combines major groups 6&ndash;9; group 2 is major "
      "group 5; group 3 is major group 4; and group 4 combines major groups "
      "1&ndash;3. The task labels are broad proxies&mdash;not every job in groups "
      "6&ndash;9 is literally routine. Group "
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
      "<td>The operative count is every household member younger than "
      + lit("20", "model child-age cutoff") + ", without a parent-link requirement. Parent&ndash;child "
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
      "<tr><td><b>Non-labour resources</b></td><td>The exact frozen input block is "
      "listed in section&nbsp;16 and copied across a household's alternatives. It "
      "includes reported benefit and tax inputs. Newly simulated means-tested "
      "benefits remain outputs that can change with earnings and composition; they "
      "are not fixed resources. Field-level units are <span class=\"exempt\">UNRESOLVED B1</span>.</td><td>The "
      "budget at every alternative &mdash; hence the "
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
            "<b>Similar estimated preferences, different employment-access "
            "environments.</b> The two employed single men share observed occupation "
            "group 4, a model hours band and observed-wage quintile 4. Their "
            "leisure-preference curves satisfy the forward rule's lowest-decile "
            "distance tolerance; they are close, not identical. Panel (a) plots the "
            "deterministic leisure component of utility. Panel (b) plots the "
            "unconditional employment-hours opportunity density and reports the "
            "non-employment atom. Panel (c) plots unconditional employment-occupation "
            "opportunity probabilities. Panel (d) plots the occupation-mixture wage-"
            "offer density conditional on employment and marks observed wages. In this "
            "same-sex comparison, conditional hours and occupation profiles are common, "
            "so unconditional mass differences arise primarily at employment access. "
            "Median conditional wage offers are "
            + "&euro;" + n("fd_matched_pair_median_conditional_wage_offer__household_a", "f2")
            + " and &euro;"
            + n("fd_matched_pair_median_conditional_wage_offer__household_b", "f2")
            + ", similar rather than dramatically different. The forward rule restricts "
            "preference distance to its admissible-set tenth percentile and maximises "
            "total-variation opportunity distance. "
            "The example is model-conditional, not a causal regional effect, ability "
            "ranking or count of available jobs. The clean rule additionally requires "
            "the maximized opportunity distance to be at least 1.5 times its "
            "admissible-set median; no identifier is displayed."))

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
    W('<li><b>Hours.</b> If working, draw weekly hours from a <em>continuous mixture</em>: '
      'narrow uniform components around focal schedules (the statutory week, standard '
      'full time and common part-time schedules), plus a broad uniform component over '
      'the support.</li>')
    W('<li><b>Wage.</b> Draw an hourly offer conditional on the drawn occupation.</li>')
    W("</ol>")
    W('<p>The proposal is a <em>sampler</em>, not a model. It only has to cover the '
      'support and be known exactly. It is deliberately close to the observed '
      'distribution so that draws land where the likelihood has mass, which is a '
      'variance-reduction device and nothing more.</p>')

    W("<h3>The observed job, the historical hybrid and the corrective estimator</h3>")
    W('<p class="exempt">The observed job is <b>inserted deterministically</b> in every '
      'household&rsquo;s estimation set. The historical code assigns that row zero correction, '
      'assigns stochastic rows minus log of their exact marginal proposal density, and '
      'includes every row in the denominator. The criterion audit establishes that this '
      'is a hybrid: it is a finite-draw approximation to the direct simulated population '
      'log-density, not the exact conditional sampled-alternatives likelihood.</p>')
    W('<p>The authorised correction generates new iid joint alternatives and applies '
      'the conditional sampling derivation. If ' + imath(r'D_i') + ' is the sampled '
      'multiset and ' + imath(r'\pi(D_i\mid j)') + ' its sampling law when candidate '
      + imath(r'j') + ' is treated as chosen, then ' + imath(r'P(j\mid D_i)\propto '
      r'e^{a_i(j)}\pi(D_i\mid j)') + '. Under iid draws from ' + imath(r'q_i') + ', '
      'factorisation gives a correction ' + imath(r'-\log q_i(j)') + ' on every '
      'candidate, including the chosen one, with multiplicities retained. The current '
      'scrambled-Halton wage point set is dependent within household, so merely changing '
      'the stored chosen-row correction would not create that estimator. Pilot-proposal '
      'independence or a cross-fitted construction also remains to be fixed and documented.</p>')
    W('<p>If a sampled row happens to land on the same economic job as the '
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
    W('<p>The earlier implementation used the joint density. Because focal hours values can be '
      'produced by more than one mixture component, that understated the density at '
      'exactly the values where most of the data sit, and the resulting objective was a '
      'likelihood in the <em>labelled</em> space rather than in the job space the model '
      'is about. Correcting it to the exact marginal changed the proposal correction '
      'and nothing else in the specification, and improved the fit substantially. '
      '<b>Exact marginal <em>q</em> is the retained rule</b> for every stochastic '
      'row.</p>')

    W(box("key", "Exact singles proposal",
          "<p>For a stochastic row the extracted proposal is "
          + imath(r"q_i(j)=q_E(e)[q_O(k\mid dgn_i,educ3_i)q_H(h)q_W(w\mid i,k)]^e")
          + ". The employment masses are " + imath(r"q_E(0)=0.10") + " and "
          + imath(r"q_E(1)=0.90") + ". The hours proposal is the continuous mixture "
          + imath(r"q_H(h)=\sum_b \omega_b(b_b-a_b)^{-1}\mathbf 1_{[a_b,b_b)}(h)")
          + " over " + imath(r"PT1,PT2,F35,FT,LH,BG[5,70]") + " with weights "
          + imath(r"(.15,.10,.24,.20,.10,.21)") + ". Overlapping component contributions "
          "are summed under the same Lebesgue base measure; no atom mass is added to a "
          "density height. Occupation is conditioned on sex and education group, and "
          "the wage proposal is the extracted occupation-conditioned lognormal.</p>"))
    W("<h3>Where the correction sits in the historical and successor likelihoods</h3>")
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
    W('<p class="exempt">This display is the exact <b>historically coded criterion</b>, a negative sum rather than '
      'an average. At finite sampling resolution, the proposal changes stochastic-row '
      'weights, probabilities and generally the optimizer; it does not simply cancel. '
      'The usual conditional sampled-alternatives derivation would apply minus log q to '
      'every candidate, including the observed candidate, while the usual simulated-'
      'integral identity omits the extra chosen-row denominator term. Neither yields '
      'the historical code. The corrected estimator is pending, so the existing '
      'parameters and downstream statistics are not presented as corrected.</p>')

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

    W("<p>The executed applications use the following type-specific utilities:</p>")
    W(math(r"u_{ig}(j)=\omega_{ig}BC(\ell_i(j);\theta_{\ell g})"
           r"+BC(c_i(j);\theta_c),\quad "
           r"\omega_{ig}=\beta_{\ell0,g}+\beta_{\ell a,g}a_i"
           r"+\beta_{\ell a^2,g}a_i^2+1\{g=sf\}\beta_{\ell n,g}n_i,",
           "singles utility"))
    W(math(r"u_i(j)=\omega_{im}BC(\ell_{im}(j);\theta_{\ell m})"
           r"+\omega_{if}BC(\ell_{if}(j);\theta_{\ell f})+\log c_i(j),",
           "clean-couples utility",
           "The direct cross-leisure term beta_ll is absent and structurally zero. "
           "Joint consumption, non-linear taxes and transfers, income effects and the "
           "joint choice still connect spouses; their decisions are not independent."))
    W(math(r"c_i(j)=C_i(j)/\lambda_c,\qquad "
           r"\ell_{is}(j)=\max\{80-h_{is}(j),1\}/\lambda_{\ell s},\qquad "
           r"a_{is}=(A_{is}-\bar A_s)/10,",
           "utility inputs and units",
           "C is post-take-up disposable consumption in euros per month; h is weekly "
           "hours; each spouse uses own age. The time endowment is eighty weekly hours "
           "and the positive-domain leisure floor is one hour."))
    W("<p>The model child count " + imath("n_i") + " is the number of all household "
      "members younger than twenty, without requiring a biological or legal parent "
      "link. <b>"
      + imath(r"\beta_c\equiv 1") + " is a normalisation, not an estimate</b>: "
      "utility in a discrete-choice model is identified only up to scale, and "
      "fixing the consumption coefficient fixes utility scale. It does <em>not</em> "
      "by itself put utility in euros. Euros arise from the separately defined "
      "flat-consumption reference and inversion in section&nbsp;13.</p>")
    W("<p><b>Budget.</b> The job-varying labour inputs and the post-simulation "
      "consumption transformation are:</p>")
    W(math(r"Y_i^D(j)=T_{FR,2015}(y_i^L(j),r_i,d_i,z_i;\tau)=ils\_dispy_i(j),"
           r"\qquad y_i^L(j)=\{lhw,yivwg,yem00,yemxp,yem\},",
           "executed budget map"))
    W(math(r"yem00=\min(h,35)w\,52/12,\quad yemxp=\max(h-35,0)w\,52/12,"
           r"\quad yem=yem00+yemxp,",
           "monthly labour earnings from weekly hours and hourly wages"))
    W(math(r"C_i^{raw}(j)=ils\_dispy_i(j)-bsa00\_s_i(j)[1-t_i(e_j)],\qquad "
           r"C_i(j)=\max\{C_i^{raw}(j),1\},",
           "take-up adjustment and positive-domain floor",
           "<span class='exempt'>Non-positive simulated disposable incomes are floored at one real-2016 "
           "euro per month, not discarded.</span>"))
    W("<p><b>The opportunity kernel and density.</b> Availability begins as a product "
      "of four unnormalised relative factors. A reference-category index may equal "
      "one, but the lognormal wage density is not a reference-normalised ratio. The "
      "kernel is divided by its full mixed-support integral for welfare:</p>")
    W(math(r"g_{ij}\;=\;g^{E}_{ij}\cdot g^{H}_{ij}\cdot g^{\mathrm{Occ}}_{ij}"
           r"\cdot g^{W}_{ij},\qquad "
           r"E_{ij}=\mathbb{1}\{\text{the package involves work}\}.",
           "the opportunity density, four factors"))
    W(math(r"\widehat g_i(j)=\widetilde g_i(j)/G_i,\qquad "
           r"G_i=\int_{\mathcal J}\widetilde g_i(z)\,\nu(dz),",
           "full-support opportunity normalisation",
           "The base measure has one counting atom at non-employment and, under "
           "employment, counting measure over occupations times Lebesgue measure "
           "over weekly hours and hourly wages. The historical fitted model has "
           "unbounded positive wage support. The initial corrective candidate uses "
           "a bounded, renormalised truncated-lognormal offer density on two to one "
           "hundred fifty euros per hour, with upper-cap sensitivity at one hundred "
           "twenty and one hundred seventy-five. This is a disclosed support "
           "assumption for the trimmed target population, not an identified offer maximum."))
    W(math(r"g_i^{W,B}(w\mid k)=g_i^W(w\mid k)"
           r"\,\mathbf 1\{2\le w\le w_{max}\}/D_i(k),\quad "
           r"D_i(k)=\Phi((\log w_{max}-\mu_i(k))/\sigma)-"
           r"\Phi((\log 2-\mu_i(k))/\sigma),",
           "bounded wage-offer correction",
           "The occupation- and parameter-dependent divisor stays inside estimation, "
           "derivatives and welfare. Simply dropping outside nodes would define a "
           "different model. The corrected fit and cap sensitivity are pending."))
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
      "the local group unemployment rate, region and urbanisation are assigned to "
      "employment access and excluded from preferences. Identification nevertheless "
      "depends on functional-form restrictions, channel assignments, observed "
      "variation and the economic validity of those exclusions. Sorting and omitted "
      "local preferences or amenities can violate the interpretation. Age also enters "
      "earning opportunities through potential experience, so a raw characteristic "
      "may affect several structural paths.</p>")

    W("<p><b>The sampled-alternatives likelihood.</b> The set of conceivable job "
      "packages is far too large to enumerate, so it is sampled. Each unit "
      "carries its observed package plus " + n("n_alternatives", "int")
      + " packages in all &mdash; the observed one plus drawn alternatives "
      "from a known <b>proposal density</b> "
      + imath("q_{ij}") + ", giving a choice set of " + n("n_alternatives", "int")
      + ". Subtracting " + imath(r"\log q_{ij}") + " from the index &mdash; the "
      "<b>historical sampling correction</b> gives the implemented criterion below. "
      "The criterion audit identifies this as a hybrid finite-draw approximation, "
      "not an exact conditional likelihood:</p>")
    W(math(r"P_i\;=\;\frac{\exp V_{i j^{*}_i}}{\sum_{j\in\mathcal{C}_i}\exp V_{ij}},"
           r"\qquad \hat\theta=\arg\min_\theta\;-\!\sum_{i=1}^{N}\log P_i(\theta).",
           "the historically implemented sampled-alternatives criterion"))
    W("<p>The successor conditional estimator requires newly generated iid joint "
      "alternatives. Under that sampling law, every candidate receives "
      + imath(r"-\log q_i(j)") + ", including the chosen candidate, and repeated "
      "atoms retain their multiplicities. Conditional exactness concerns the "
      "conditioned sampling experiment; it does not make the finite-sample maximiser "
      "unbiased or remove sampling uncertainty.</p>")
    W("<p>The proposal density is <b>computation, not economics</b>. It is chosen "
      "by the analyst and carries no parameter of interest. At finite resolution it "
      "affects numerical weights and generally does not cancel. It is never an opportunity, an offer or an "
      "availability: those words belong to " + imath("g_{ij}") + " alone.</p>")

    # ============================================================ instantiation
    W("<h3>6.2 The same model, applied twice</h3>")
    W("<p>The applications share a RURO architecture but differ in consequential "
      "specification details. The table makes those differences explicit.</p>")

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

      "<tr><td><b>Consumption transformation</b></td>"
      "<td>Box&ndash;Cox consumption with an estimated curvature maintained common "
      "across single men and women; sex-specific curvature was not tested.</td>"
      "<td>Log consumption: theta_c is fixed at zero and beta_c at one.</td></tr>"

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
          "on a parallel final frame with common screens but a joint-quadrant proposal, "
          "spouse-specific hours mixtures and joint household alternatives. Its coded "
          "correction and likelihood have the analogous form. Its parameters appear beside the "
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
    W("<p>Each factor is assigned a market role rather than a taste role. Index "
      "coefficients exponentiate into relative <em>density heights</em> where the "
      "formula warrants it; they are not automatically probability or mass ratios. "
      "The product receives one full-support normalisation.</p>")

    # ---- (a) employment access
    W("<h4>(a) Employment access &mdash; is work available at all?</h4>")
    W("<p><b>What it says about the market.</b> How much density the opportunity "
      "distribution places on <em>being employed at all</em> rather than on the "
      "non-employment package, and how that level is tilted by the labour market "
      "the household lives in. It is a level shift applied to every working "
      "package alike.</p>")
    W(math(r"\log g^{E}_{ij}=E_{ij}\Bigl[\beta_{E}"
           r"+10\beta_{s}\,s_i"
           r"+\textstyle\sum_{r=2}^{8}\beta_{r}\mathbb{1}\{R_i=r\}"
           r"+\beta_{u}U_i+\beta_{m}M_i\Bigr]",
           "employment access"))
    W("<p><b>Reference.</b> The non-employment package, at which the factor is "
      "one by construction, and &mdash; among working packages &mdash; a "
      "household in the omitted region living in a rural zone. <b>Regressors.</b> "
      + imath("s_i") + " is the <b>unemployment rate of the household's own "
      "group</b>, defined by region, education and sex, and looked up from an "
      "external source rather than estimated. A one-percentage-point increase changes "
      "the log working-opportunity factor by " + imath(r"10\beta_s\times0.01")
      + "; it is not a percentage-point change in employment. The exclusion is an "
      "economic identifying assumption, not proof. " + imath("R_i") + " is the "
      "region of residence, seven indicators against an omitted eighth. "
      + imath("U_i") + " and " + imath("M_i") + " are urban and intermediate "
      "residence against rural. <b>None of these appears in preferences</b>, "
      "which is what makes the geographic exercise of section&nbsp;17 a "
      "well-defined operation.</p>")

    # ---- (b) hours
    W("<h4>(b) Hours &mdash; at which hours is work available?</h4>")
    W("<p><b>What it says about the market.</b> Employers do not post a smooth "
      "continuum of weekly hours. They post a few common lengths, and in "
      "France one of them is written into the statute. This factor is a step "
      "density over disjoint hours bands. The statutory feature is an elevated "
      "continuous density over the narrow interval around thirty-five hours, not an "
      "atom at exactly thirty-five.</p>")
    W(math(r"H(h)=\beta_{pt1}1_{[17.5,21.5)}+\beta_{pt2}1_{[28.5,30.5)}"
           r"+\beta_{35}1_{[33.5,36.5)}+\beta_{ft}1_{[36.5,40.5]}"
           r"+\beta_{lh}1_{[44.5,70]},",
           "the hours-offer density"))
    W(math(r"I_H=26.5+4e^{\beta_{pt1}}+2e^{\beta_{pt2}}+3e^{\beta_{35}}"
           r"+4e^{\beta_{ft}}+25.5e^{\beta_{lh}},\qquad p_H(h)=e^{H(h)}/I_H,",
           "hours normaliser and conditional density",
           "Integrated band mass equals density height times band width. A height "
           "ratio is therefore not a probability ratio across unequal-width bands."))

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
    W(math(r"\operatorname{median}(W\mid i,k)=e^{\mu_i(k)},\quad "
           r"E[W\mid i,k]=e^{\mu_i(k)+\sigma^2/2},\quad "
           r"\operatorname{mode}(W\mid i,k)=e^{\mu_i(k)-\sigma^2},",
           "lognormal location is not its mean"))
    W(box("key", "Why this is an <em>opportunity</em> and not a Mincer regression",
          "<p>The same variables &mdash; schooling, experience &mdash; appear in "
          "a standard wage regression. The difference is the object being "
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
