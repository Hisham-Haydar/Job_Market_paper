# -*- coding: utf-8 -*-
"""Sections 1-11 of the research-story report."""
from common import n, a, lit, box, esc


def sections(F):
    """F is a FigureBank."""
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
      + n("state_I11_female_raw", "sci", 1) + "</span> Gini points, numerically zero. "
      "Nothing is left in an unexplained residual.</li>")
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
      + n("state_I00_female_raw", "f3") + ' Gini points on the raw basis. Of that, '
      'preferences account for ' + n("C_pref_female_raw_share", "pct", 1)
      + ' and the non-preference environment for '
      + n("C_env_female_raw_share", "pct", 1) + '. Inside the environment, household '
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
          "definition and the frozen artefact it was read from. Section&nbsp;23 audits "
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
          "which is why the draw geometry is frozen and digest-pinned.</p>"))

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
    W('<p>These are the final equations, in the order the estimation code evaluates '
      'them. <em>g</em> denotes sex; <em>BC</em> is the Box&ndash;Cox transform '
      '<em>BC(y;&theta;) = (y<sup>&theta;</sup> ' + lit("&minus; 1)/&theta;",
      "the Box-Cox functional form, a definition") + '</em>, which is '
      '<em>log y</em> at <em>' + lit("&theta; = 0", "the Box-Cox limiting case, a definition") + '</em>.</p>')

    W("<h3>Block 1 &mdash; utility / preferences</h3>")
    W('<div class="eq">'
      "u_ij  =  omega_ig  ·  BC( leisure_ij ; theta_l,g )\n"
      "      +  beta_c    ·  BC( consumption_ij ; theta_c )\n"
      "\n"
      "omega_ig  =  beta_l0_g  +  beta_l_age_g · age_i\n"
      "                        +  beta_l_age2_g · age_i^2\n"
      "                        +  beta_l_nkids_g · nkids_i      (single women only)"
      "</div>")
    W("<ul>")
    W("<li><b><em>&omega;<sub>ig</sub></em>, the leisure weight.</b> How much this "
      "household values time, as a function of age, age squared and &mdash; for single "
      "women &mdash; the number of children. This is the taste object the whole paper "
      "is about separating from opportunity.</li>")
    W("<li><b><em>&theta;<sub>l</sub></em> and <em>&theta;<sub>c</sub></em>, the "
      "curvatures.</b> The Box&ndash;Cox exponents on leisure and consumption govern "
      "diminishing marginal utility and hence the willingness to trade income for time. "
      "They are estimated separately by sex for leisure and pooled for consumption.</li>")
    W("<li><b><em>&beta;<sub>c</sub></em> is fixed, not estimated.</b> Utility is only "
      "identified up to scale in a logit model; fixing the consumption coefficient is "
      "the scale normalisation. It is why there is no consumption coefficient in the "
      "parameter table.</li>")
    W("</ul>")

    W("<h3>Block 2 &mdash; job access, <em>g<sup>E</sup></em></h3>")
    W('<div class="eq">'
      "log g^E_ij  =  working_ij · [  beta_E                        the level\n"
      "                            +  beta_E_gsur  · unemployment_rate_i\n"
      "                            +  SUM_r beta_E_drgn_r · region_ir\n"
      "                            +  beta_E_drgur · urban_i\n"
      "                            +  beta_E_drgmd · intermediate_i  ]"
      "</div>")
    W("<p>The employment margin: how much density the opportunity distribution "
      "places on <em>being employed at all</em> rather than on the non-employment "
      "state, and how that level is tilted by circumstance. <b>Local market access "
      "is part of this factor, not a factor of its own</b> &mdash; the intercept is "
      "the level of the access surface and the remaining terms tilt it. Block&nbsp;5 "
      "reads those tilt terms one at a time.</p>")

    W("<h3>Block 3 &mdash; hours access</h3>")
    W('<div class="eq">'
      "log g^H_ij  =  SUM_b  beta_h_b · working_ij · 1[ hours_ij in band b ]\n"
      "\n"
      "bands:   PT1  [17.5, 21.5]      short part time\n"
      "         PT2  [28.5, 30.5]      long part time\n"
      "         F35  [33.5, 36.5)      the statutory week\n"
      "         FT   [36.5, 40.5]      standard full time\n"
      "         LH   [44.5, 70]        long hours\n"
      "         residual bins          normalised to zero"
      "</div>")
    W("<p><b>This block is the institutional content of the model.</b> Each coefficient "
      "is the log density the opportunity distribution places on jobs in that hours "
      "band, relative to the residual bins. The French statutory working week gives "
      "employers a strong reason to post at one particular length, and a spike of that "
      "kind is a property of what is <em>offered</em>, not of anyone&rsquo;s indifference "
      "curve. Section&nbsp;8 shows that adding the statutory-week coefficient is the "
      "single largest specification improvement in the paper.</p>")

    W("<h3>Block 4 &mdash; occupation access</h3>")
    W('<div class="eq">'
      "log g^Occ_ij  =  SUM_k  beta_occ_k,g · working_ij · 1[ occupation_ij = k ]\n"
      "\n"
      "         k in {2,3,4};  group 1 is the dropped reference;  g = sex"
      "</div>")
    W("<p>How reachable each occupation group is, estimated separately for men and "
      "women. This is <b>access</b>, not pay: what each group pays is block&nbsp;6. "
      "Keeping the two apart is what allows the model to say that an occupation is "
      "well paid <em>and</em> hard to get into, which a single occupation coefficient "
      "could not express.</p>")

    W("<h3>Block 5 &mdash; what tilts job access "
      "(the interior of <em>g<sup>E</sup></em>)</h3>")
    W('<div class="eq">'
      "the circumstance terms inside log g^E_ij, read one at a time:\n"
      "\n"
      "     beta_E_gsur  · unemployment_rate_i\n"
      "  +  SUM_r beta_E_drgn_r · region_ir\n"
      "  +  beta_E_drgur · urban_i\n"
      "  +  beta_E_drgmd · intermediate_i\n"
      "\n"
      "  (NOT a separate factor: there is no g^Acc in this model)"
      "</div>")
    W("<p>The circumstances that tilt job access. The local unemployment rate is the "
      "sharpest of them. Region indicators are NUTS-1 with one omitted; urbanisation is "
      "urban and intermediate against rural. <b>None of these variables appears "
      "anywhere in preferences.</b> That exclusion is not incidental &mdash; it is what "
      "makes the geographic exercise of section&nbsp;17 a well-defined operation on "
      "the access block.</p>")

    W("<h3>Block 6 &mdash; earning opportunities / the wage-offer technology</h3>")
    W('<div class="eq">'
      "mu_ij  =  beta_w0\n"
      "       +  beta_w_educL · educ_low_i   +  beta_w_educH · educ_high_i\n"
      "       +  beta_w_pexp  · pexp_i       +  beta_w_pexp2 · pexp_i^2\n"
      "       +  SUM_k delta_occ_k · 1[ occupation_ij = k ]\n"
      "\n"
      "log g^W_ij  =  working_ij · [ -0.5·( (log w_ij - mu_ij) / sigma )^2\n"
      "                              - log sigma  - 0.5·log(2·pi)  - log w_ij ]"
      "</div>")
    W("<ul>")
    W("<li><b>A log-normal offer density</b> with a household-specific location "
      "<em>&mu;</em> and a <b>common dispersion <em>&sigma;</em></b>. The final "
      "<code>&minus;log w</code> term is the Jacobian of the change of variables from "
      "the log wage to the wage level; it is there because the choice object is the "
      "wage, not its logarithm.</li>")
    W("<li><b>Education and experience shift the location only.</b> They are excluded "
      "from preferences and from access. Someone with more schooling faces a "
      "better-located offer distribution; that is an opportunity statement, and "
      "deliberately not an ability statement.</li>")
    W("<li><b>The occupation wage-location shifts <em>&delta;<sub>occ</sub></em></b> "
      "are what makes the wage offer occupation-conditioned: each occupation group has "
      "its own location on the same dispersion. Section&nbsp;8 explains why this was "
      "added and what it repaired.</li>")
    W("</ul>")

    W("<h3>Block 7 &mdash; the proposal density</h3>")
    W('<div class="eq">'
      "log q_i0  =  0                              observed job, deterministic\n"
      "log q_ij  =  log q_E + log q_Occ + log q_H + log q_W      sampled rows\n"
      "\n"
      "                       with q_H the EXACT MARGINAL of the hours mixture"
      "</div>")
    W("<p>Not a behavioural object. It is the sampler, subtracted out. Section&nbsp;5.</p>")

    W("<h3>The assembled likelihood</h3>")
    W('<div class="eq">'
      "g_ij   =  g^E_ij · g^H_ij · g^Occ_ij · g^W_ij        four factors\n"
      "\n"
      "V_ij   =  u_ij + log g_ij  -  log q_ij\n"
      "       =  u_ij + log g^E_ij + log g^H_ij\n"
      "                + log g^Occ_ij + log g^W_ij  -  log q_ij\n"
      "\n"
      "P_i    =  exp(V_i0) / SUM_j exp(V_ij)\n"
      "negLL  =  - SUM_i log P_i"
      "</div>")
    W('<p>Preferences and opportunities enter the <em>same</em> index additively. That '
      'is exactly why separating them needs exclusion restrictions rather than '
      'functional form: without variables that shift one block and not the other, the '
      'sum would be identified but its parts would not.</p>')

    W(box("say", "The one-sentence version for the talk",
          "<p>&ldquo;A household&rsquo;s observed job maximises preferences over a set "
          "it did not choose; the model estimates the density of that set and the "
          "preferences jointly, with the tax system solved exactly at every "
          "alternative.&rdquo;</p>"))

    return H
