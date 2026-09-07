# -*- coding: utf-8 -*-
"""Sections 13-18: the welfare measure, the decomposition, the headline results,
endowments and needs, geography, and the common-opportunity benchmark."""
from common import n, a, lit, box


def sections(F):
    H = []
    W = H.append

    # ==================================================================== 13 ==
    W('<h2 id="s13" class="exempt">13. The welfare measure</h2>')

    W("<p>Before anything can be decomposed there has to be a scalar, comparable across "
      "households, that respects the fact that people have different preferences. That "
      "is what this section builds.</p>")

    W("<h3>The problem a money metric has to solve</h3>")
    W("<p>Two households with the same disposable income are not equally well off if "
      "one of them had to work sixty hours to get it. Income is not welfare in a "
      "labour-supply model. But utility is not comparable across people either: each "
      "household has its own preference parameters, and the numbers its own utility "
      "function produces have no meaning next to anyone else&rsquo;s.</p>")
    W("<p>The standard resolution is a <b>money metric</b>: convert each "
      "household&rsquo;s situation into the amount of money that would make a common "
      "<em>reference</em> household equally well off. That number is in euros, so it is "
      "comparable; and it is computed by inverting the household&rsquo;s <em>own</em> "
      "preferences, so it respects them.</p>")

    W("<h3>The measure, precisely</h3>")
    W('<div class="eq">'
      "Find the flat consumption level  w_i  that solves\n"
      "\n"
      "    log SUM_j exp[ u_leisure(l_ij)  +  beta_c · BC( w_i / needs_i ; theta_c )\n"
      "                                    +  log g_ij ]   =   V_i\n"
      "\n"
      "where  V_i  is the household's actual expected-maximum utility\n"
      "       g_ij is the household's own opportunity density over its own job set\n"
      "       needs_i is the equivalence scale of the household's composition\n"
      "\n"
      "        W1_i  =  w_i          in euros per month"
      "</div>")
    W("<p>In words: <b>hold the household&rsquo;s own job set, its own opportunity "
      "density and its own preferences fixed, strip the variation in pay across jobs "
      "and replace it with a single flat consumption level, and ask what that level has "
      "to be to leave the household exactly as well off as it actually is.</b></p>")

    W("<h3>What it neutralizes and what it retains</h3>")
    W('<div class="scroll"><table><thead><tr>'
      "<th>Neutralized by the measure itself</th><th>Retained by the measure itself</th>"
      "</tr></thead><tbody><tr><td>"
      "<ul><li><b>The dispersion of pay across the jobs in a household&rsquo;s set.</b> "
      "Pay enters only through one flat scalar, so a household is not rewarded in the "
      "measure for facing a steep wage gradient it did not take up.</li>"
      "<li><b>The unit of utility.</b> Everything is expressed in euros.</li>"
      "<li><b>Household size, in the equivalized version.</b> Two adults needing more "
      "than one does not count as being better off.</li></ul>"
      "</td><td>"
      "<ul><li><b>The household&rsquo;s own preferences.</b> A person who genuinely "
      "values time is not penalised for working less.</li>"
      "<li><b>The household&rsquo;s own opportunity density.</b> Someone facing a thin "
      "set of offers has a lower expected maximum, and therefore a lower "
      "measure.</li>"
      "<li><b>Non-labour resources and the tax-benefit system.</b> They enter the "
      "budget at every alternative.</li></ul>"
      "</td></tr></tbody></table></div>")

    W(box("key", "The most important property, and the one that makes the paper work",
          "<p><b>The measure is opportunity-sensitive.</b> Because it inverts the "
          "expected maximum over the household&rsquo;s <em>whole reachable "
          "distribution</em> rather than evaluating the one job it took, a household "
          "with a wider or better-located opportunity density scores higher even when "
          "its observed job is identical to someone else&rsquo;s.</p>"
          "<p>This is precisely what a common-choice-set model cannot express, and it is "
          "why section&nbsp;18&rsquo;s benchmark measures substantially less inequality: "
          "having removed the variation in reachable sets, there is less for the "
          "measure to see.</p>"))

    W(box("warn", "Three things this is not",
          "<ul>"
          "<li><b>It is not a compensating variation and it requires no tax reform.</b> "
          "The four states of section&nbsp;14 are common-reference well-being "
          "<em>levels</em>, not the welfare effects of a policy change. No reform is "
          "simulated anywhere in this paper.</li>"
          "<li><b>It is not an income measure.</b> Two households with identical "
          "disposable income get different values if their hours, their reachable sets "
          "or their preferences differ.</li>"
          "<li><b>It is not the only defensible measure.</b> It is the most conservative "
          "of a family. Measures that compensate more fully for opportunity differences "
          "produce roughly double the inequality. Choosing the conservative member means "
          "the paper&rsquo;s inequality findings are a lower bound within its own "
          "family.</li>"
          "</ul>"))

    W("<h3>Raw and equivalized, and why equivalization has to be coalition-consistent</h3>")
    W("<p>Every result is reported on two bases. <b>Raw</b> is the measure in euros. "
      "<b>Equivalized</b> divides by an equivalence scale reflecting household "
      "composition, so a lone parent with two children is not counted as well off as a "
      "childless single on the same money.</p>")
    W("<p>The equivalization contains a trap that is worth understanding because it "
      "determines whether the decomposition closes at all. The equivalence scale is a "
      "function of household composition &mdash; and household composition is <em>one of "
      "the things the decomposition equalizes</em>, inside the endowments-and-needs "
      "channel. So the scale cannot be frozen at each household&rsquo;s observed value "
      "while the channels move around it.</p>")
    W("<p>If it is frozen, the state in which everything has been equalized still shows "
      "residual inequality &mdash; the inequality of the frozen scales themselves &mdash; "
      "and the decomposition no longer closes. <b>Coalition-consistent equivalization</b> "
      "means the scale moves with the composition channel: when composition is "
      "equalized, so is the scale. That is what makes the fully-equalized state "
      "numerically zero, at " + n("state_I11_female_raw", "sci", 1)
      + " Gini points, and hence what makes the decomposition exhaustive.</p>")

    W(F.fig("figW01_welfare_distributions",
            "The welfare distribution in the four principal states. The baseline and "
            "the preferences-equalized state are close together and wide; the "
            "environment-equalized state is dramatically narrower; the fully-equalized "
            "state is a point mass."))

    # ==================================================================== 14 ==
    W('<h2 id="s14" class="exempt">14. Building the decomposition</h2>')

    W("<h3>Step one: two factors, four states</h3>")
    W("<p>Split everything that determines a household&rsquo;s welfare into two "
      "factors: <b>preferences</b> and <b>the non-preference environment</b>. "
      "Then compute the welfare distribution in each of four states, replacing the "
      "household&rsquo;s own value with a common reference value where indicated.</p>")

    W('<div class="scroll"><table><thead><tr><th>State</th><th>Preferences</th>'
      "<th>Environment</th><th>Inequality (Gini points, raw)</th>"
      "<th>What it means</th></tr></thead><tbody>"
      "<tr><td><b>Baseline</b></td><td>own</td><td>own</td>"
      '<td class="num">' + n("state_I00_female_raw", "f4") + "</td>"
      "<td>The world as it is.</td></tr>"
      "<tr><td><b>Preferences equalized</b></td><td>reference</td><td>own</td>"
      '<td class="num">' + n("state_I10_female_raw", "f4") + "</td>"
      "<td>Everyone wants the same things; environments still differ.</td></tr>"
      "<tr><td><b>Environment equalized</b></td><td>own</td><td>reference</td>"
      '<td class="num">' + n("state_I01_female_raw", "f4") + "</td>"
      "<td>Everyone faces the same world; tastes still differ.</td></tr>"
      "<tr><td><b>Both equalized</b></td><td>reference</td><td>reference</td>"
      '<td class="num">' + n("state_I11_female_raw", "sci", 1) + "</td>"
      "<td>Identical people in an identical world. Must be zero if the two factors "
      "are exhaustive.</td></tr>"
      "</tbody></table></div>")

    W(box("key", "Read the second row before going any further",
          "<p><b>Equalizing preferences alone makes measured inequality go up, not "
          "down.</b> The preferences-equalized state is <em>higher</em> than the "
          "baseline.</p>"
          "<p>The reason is straightforward once stated. In the real world, preferences "
          "and environments are correlated in a partly offsetting way: people adapt to "
          "the environment they face. Imposing a single reference preference on everyone "
          "removes that adaptation, so households in bad environments no longer make the "
          "best of them, and the spread widens. This is not a numerical artefact and it "
          "is not a bug &mdash; it is the single most important thing to understand "
          "about the decomposition, because it is why the two methods below give "
          "different answers.</p>"))

    W("<h3>Step two, method A: one-factor equalization counterfactuals</h3>")
    W("<p>The most intuitive question: <em>how much inequality disappears if I equalize "
      "just this one factor and leave everything else alone?</em> Read straight off the "
      "table above.</p>")
    W('<div class="scroll"><table><thead><tr><th>Equalize&hellip;</th>'
      '<th class="num">Change in inequality</th><th>Reading</th></tr></thead><tbody>'
      "<tr><td><b>Preferences only</b></td>"
      '<td class="num">' + n("equalization_pref_only", "signpct", 1) + "</td>"
      "<td>Inequality <b>rises</b> by " + n("equalization_pref_only", "pctabs", 1)
      + ". Removing preference heterogeneity removes the adaptation that partly "
      "offsets environmental disadvantage.</td></tr>"
      "<tr><td><b>Environment only</b></td>"
      '<td class="num">' + n("equalization_env_only", "signpct", 1) + "</td>"
      "<td>Inequality <b>falls</b> by " + n("equalization_env_only", "pctabs", 1)
      + ". Most of the observed spread is environmental.</td></tr>"
      "</tbody></table></div>")
    W("<p><b>The weakness of this method</b> is that the two numbers do not add up to "
      "anything. They sum to neither one hundred per cent nor to the total, because "
      "each is computed holding the other factor at its actual, unequal value. There is "
      "no accounting identity here, and it would be wrong to present these as shares of "
      "a whole.</p>")

    W("<h3>Step two, method B: Shapley attribution</h3>")
    W("<p>The Shapley value fixes exactly that. Treat the two factors as players in a "
      "cooperative game whose value is inequality removed. A player&rsquo;s contribution "
      "is its <b>marginal contribution averaged over every order in which the players "
      "could be brought in</b>. With two players there are two orders.</p>")
    W('<div class="scroll"><table><thead><tr><th>Order</th>'
      "<th>What preferences contribute</th><th>Size</th></tr></thead><tbody>"
      "<tr><td><b>Preferences first</b></td>"
      "<td>Move from the baseline to the preferences-equalized state.</td>"
      "<td><b>Negative</b> &mdash; inequality rises, so preferences contribute "
      "<em>less</em> than nothing when brought in first.</td></tr>"
      "<tr><td><b>Preferences last</b></td>"
      "<td>Move from the environment-equalized state to the fully-equalized state: "
      "from " + n("state_I01_female_raw", "f4") + " down to "
      + n("state_I11_female_raw", "sci", 1) + ".</td>"
      "<td><b>Positive and substantial</b> &mdash; once environments are common, all "
      "remaining inequality is preference-driven by construction.</td></tr>"
      "</tbody></table></div>")
    W("<p>The Shapley value for preferences is the average of those two marginal "
      "contributions: " + n("C_pref_female_raw", "f4") + " Gini points, which is "
      + n("C_pref_female_raw_share", "pct", 2) + " of baseline inequality. The "
      "environment takes the rest, " + n("C_env_female_raw", "f4") + " points or "
      + n("C_env_female_raw_share", "pct", 2) + ". By construction the two <b>sum "
      "exactly to the total</b>: that is the property the one-factor method lacks.</p>")

    W(box("warn", "The two methods are different objects. Do not mix the language.",
          '<div class="scroll"><table><thead><tr><th></th>'
          "<th>Shapley attribution</th><th>One-factor equalization</th>"
          "</tr></thead><tbody>"
          "<tr><td><b>Preferences</b></td>"
          '<td class="num">' + n("C_pref_female_raw_share", "pct", 1) + " of the total</td>"
          '<td class="num">' + n("equalization_pref_only", "signpct", 1) + " of baseline</td></tr>"
          "<tr><td><b>Environment</b></td>"
          '<td class="num">' + n("C_env_female_raw_share", "pct", 1) + " of the total</td>"
          '<td class="num">' + n("equalization_env_only", "signpct", 1) + " of baseline</td></tr>"
          "<tr><td><b>Do they sum to the whole?</b></td><td>Yes, by construction.</td>"
          "<td>No. There is no identity.</td></tr>"
          "<tr><td><b>The question answered</b></td>"
          "<td>&ldquo;How should credit for total inequality be divided between the two "
          "factors, fairly across all orderings?&rdquo;</td>"
          "<td>&ldquo;What happens if I intervene on this one factor and change nothing "
          "else?&rdquo;</td></tr>"
          "</tbody></table></div>"
          "<p><b>Why they differ here, specifically.</b> The environment&rsquo;s Shapley "
          "share, " + n("C_env_female_raw_share", "pct", 1) + ", is well above its "
          "single-order equalization effect of "
          + n("equalization_env_only", "pctabs", 1) + ". The gap is the "
          "preference&ndash;environment interaction: bringing the environment in "
          "<em>after</em> preferences have been equalized removes more inequality than "
          "bringing it in first, and the Shapley value counts both orders.</p>"
          "<p><b>The sentence to avoid.</b> Never say a Shapley share &ldquo;removes "
          "<em>x</em> per cent of inequality&rdquo;. It is an average over orders, not "
          "the result of any single intervention. The number that answers &ldquo;what if "
          "we equalized the environment&rdquo; is "
          + n("equalization_env_only", "pctabs", 1) + ", not "
          + n("C_env_female_raw_share", "pct", 1) + ".</p>"))

    W(F.fig("figW02_headline_decomposition",
            "The preference and environment contributions with uncertainty bands, raw "
            "and equivalized."))

    W("<h3>Step three: opening up the environment</h3>")
    W("<p>The environment is not one thing. It is split into three sub-players, and the "
      "same Shapley machinery is applied one level down &mdash; a nesting, not a "
      "re-decomposition, so the level above is left bitwise unchanged.</p>")
    W('<div class="scroll"><table><thead><tr><th>Sub-channel</th><th>What is in it</th>'
      "</tr></thead><tbody>"
      "<tr><td><b>Job access</b></td><td>The employment margin, the hours-band offer "
      "density, occupation access, and the local-market and geographic access "
      "regressors. Everything governing <em>which jobs are reachable</em>.</td></tr>"
      "<tr><td><b>Earning opportunities</b></td><td>The wage-offer technology: the "
      "location and dispersion of the hourly offer density, including its education, "
      "experience and occupation shifts. Everything governing <em>what reachable jobs "
      "pay</em>.</td></tr>"
      "<tr><td><b>Household endowments and needs</b></td><td>Non-labour resources, and "
      "household composition together with the needs it generates. Everything that "
      "shapes the budget without being about the labour market at all.</td></tr>"
      "</tbody></table></div>")
    W("<p>The nesting closes as an exact identity: the three sub-channels sum to the "
      "environment total, to within about ten to the minus fourteen. Job access is "
      "then split once more, into its geographic and non-geographic parts, and that "
      "closes too. Section&nbsp;17.</p>")
    W(F.fig("figW03_nested_environment",
            "The environment opened into job access, earning opportunities, and "
            "household endowments and needs."))

    # ==================================================================== 15 ==
    W('<h2 id="s15" class="exempt">15. Headline results</h2>')

    W("<p>Single-adult households, France, the reference year. The primary reference "
      "convention is the female reference; the male structural-zero reference is the "
      "official sensitivity, and the two are <b>never averaged</b>.</p>")

    W('<div class="scroll"><table><thead><tr><th>Quantity</th>'
      '<th class="num">Raw</th><th class="num">Share of baseline</th>'
      '<th class="num">Equivalized</th><th class="num">Share of baseline</th>'
      "</tr></thead><tbody>"

      '<tr class="grouphead"><td colspan="5">Total</td></tr>'
      "<tr><td><b>Baseline inequality</b></td>"
      '<td class="num">' + n("state_I00_female_raw", "f4") + "</td>"
      '<td class="num">&mdash;</td>'
      '<td class="num">' + n("state_I00_female_equivalized", "f4") + "</td>"
      '<td class="num">&mdash;</td></tr>'

      '<tr class="grouphead"><td colspan="5">First level: preferences against the environment</td></tr>'
      "<tr><td><b>Preferences</b></td>"
      '<td class="num">' + n("C_pref_female_raw", "f4") + "</td>"
      '<td class="num">' + n("C_pref_female_raw_share", "pct", 2) + "</td>"
      '<td class="num">' + n("C_pref_female_equivalized", "f4") + "</td>"
      '<td class="num">' + n("C_pref_female_equivalized_share", "pct", 2) + "</td></tr>"
      "<tr><td><b>Non-preference environment</b></td>"
      '<td class="num">' + n("C_env_female_raw", "f4") + "</td>"
      '<td class="num">' + n("C_env_female_raw_share", "pct", 2) + "</td>"
      '<td class="num">' + n("C_env_female_equivalized", "f4") + "</td>"
      '<td class="num">' + n("C_env_female_equivalized_share", "pct", 2) + "</td></tr>"

      '<tr class="grouphead"><td colspan="5">Second level: inside the environment</td></tr>'
      "<tr><td><b>Job access</b></td>"
      '<td class="num">' + n("C_acc_female_raw", "f4") + "</td>"
      '<td class="num">' + n("C_acc_female_raw_share", "pct", 2) + "</td>"
      '<td class="num">' + n("C_acc_female_equivalized", "f4") + "</td>"
      '<td class="num">' + n("C_acc_female_equivalized_share", "pct", 2) + "</td></tr>"
      "<tr><td><b>Earning opportunities</b></td>"
      '<td class="num">' + n("C_earn_female_raw", "f4") + "</td>"
      '<td class="num">' + n("C_earn_female_raw_share", "pct", 2) + "</td>"
      '<td class="num">' + n("C_earn_female_equivalized", "f4") + "</td>"
      '<td class="num">' + n("C_earn_female_equivalized_share", "pct", 2) + "</td></tr>"
      "<tr><td><b>Endowments and needs</b></td>"
      '<td class="num">' + n("C_needs_female_raw", "f4") + "</td>"
      '<td class="num">' + n("C_needs_female_raw_share", "pct", 2) + "</td>"
      '<td class="num">' + n("C_needs_female_equivalized", "f4") + "</td>"
      '<td class="num">' + n("C_needs_female_equivalized_share", "pct", 2) + "</td></tr>"

      '<tr class="grouphead"><td colspan="5">Third level: inside job access</td></tr>'
      "<tr><td><b>Geographic access</b></td>"
      '<td class="num">&mdash;</td>'
      '<td class="num">' + n("geo_share_of_I00_raw", "pct", 2) + "</td>"
      '<td class="num">&mdash;</td>'
      '<td class="num">' + n("geo_share_of_I00_equivalized", "pct", 2) + "</td></tr>"
      "</tbody></table></div>")

    W("<h3>What to say about each of these</h3>")
    W("<ul>")
    W("<li><b>Total welfare inequality</b> is " + n("state_I00_female_raw", "f4")
      + " Gini points on the raw basis and " + n("state_I00_female_equivalized", "f4")
      + " equivalized. Equivalizing <em>raises</em> measured inequality, because "
      "household composition and the money available are not independent.</li>")
    W("<li><b>Preferences</b> account for " + n("C_pref_female_raw_share", "pct", 2)
      + " raw and " + n("C_pref_female_equivalized_share", "pct", 2) + " equivalized. "
      "This is the paper&rsquo;s most striking number and the one to state most "
      "carefully &mdash; see the reference-sensitivity caveat below.</li>")
    W("<li><b>The environment</b> takes " + n("C_env_female_raw_share", "pct", 2)
      + " raw. Under the male reference it is " + n("C_env_male_raw_share", "pct", 2)
      + " &mdash; still overwhelming, which is why the <em>qualitative</em> conclusion "
      "is robust even though the preference level is not.</li>")
    W("<li><b>Job access</b> is " + n("C_acc_female_raw_share", "pct", 2)
      + " of baseline inequality, and almost all of it is geographic.</li>")
    W("<li><b>Earning opportunities</b> are " + n("C_earn_female_raw_share", "pct", 2)
      + ", larger than job access. Differences in what reachable jobs <em>pay</em> "
      "matter more than differences in which jobs are reachable.</li>")
    W("<li><b>Endowments and needs</b> are the largest single component at "
      + n("C_needs_female_raw_share", "pct", 2) + " raw, rising to "
      + n("C_needs_female_equivalized_share", "pct", 2) + " equivalized. "
      "Section&nbsp;16 explains what is in it and how far the interpretation can be "
      "pushed.</li>")
    W("<li><b>The combined market-side contribution</b> &mdash; job access plus earning "
      "opportunities &mdash; is " + n("C_acc_female_raw_share", "pp", 2) + " plus "
      + n("C_earn_female_raw_share", "pp", 2) + " percentage points of baseline "
      "inequality. It must be jackknifed as a single quantity rather than by adding the "
      "two channels&rsquo; bands: across resampling the two move against each other, so "
      "adding their separate bands overstates the uncertainty on the total by roughly a "
      "factor of three.</li>")
    W("</ul>")

    W(box("warn", "Reference sensitivity: the caveat that must be stated with the "
                  "headline, not after it",
          "<p>The welfare states require a <b>reference household</b> whose preferences "
          "everyone is given in the equalized states. That choice is not innocuous for "
          "the preference channel.</p>"
          '<div class="scroll"><table><thead><tr><th>Reference</th>'
          '<th class="num">Preference share, raw</th>'
          '<th class="num">Environment share, raw</th></tr></thead><tbody>'
          "<tr><td><b>Female (primary)</b></td>"
          '<td class="num">' + n("C_pref_female_raw_share", "pct", 2) + "</td>"
          '<td class="num">' + n("C_env_female_raw_share", "pct", 2) + "</td></tr>"
          "<tr><td><b>Male structural zero (sensitivity)</b></td>"
          '<td class="num">' + n("C_pref_male_raw_share", "pct", 2) + "</td>"
          '<td class="num">' + n("C_env_male_raw_share", "pct", 2) + "</td></tr>"
          "</tbody></table></div>"
          "<p>The preference share nearly doubles between the two. <b>That movement is "
          "real, not numerical noise</b>, and it dwarfs both the resampling band and the "
          "parameter-uncertainty interval. It is why the paper reports a preference "
          "contribution that is <em>small</em> rather than one that is a specific "
          "number, and why the two references are never averaged &mdash; averaging two "
          "different normative conventions produces a quantity that answers no "
          "question.</p>"
          "<p><b>What survives.</b> The environment dominates under both references. The "
          "ordering of the three environment sub-channels is unchanged. In the subgroup "
          "results the male preference share even <em>changes sign</em> between "
          "references, from " + n("subgroup_men_pref_share_female_ref", "signpct", 2)
          + " to " + n("subgroup_men_pref_share_male_ref", "signpct", 2)
          + " &mdash; which is exactly why no claim in this paper rests on a "
          "subgroup-level preference level.</p>"))

    W(box("key", "Two kinds of uncertainty, and why they are never merged",
          "<p><b>Numerical resampling uncertainty</b> is the band from "
          + a("defs.n_scrambles", "int") + " randomized quasi-Monte-Carlo scrambles, "
          "delete-one jackknifed. It measures how precisely the integrals were "
          "computed. It is narrow.</p>"
          "<p><b>Parameter uncertainty</b> propagates the estimated coefficients&rsquo; "
          "clustered sampling distribution through the entire welfare pipeline. It "
          "measures how well the parameters are known. It is <b>three to six times "
          "wider</b>.</p>"
          "<p>For the preference channel the resampling band is "
          + n("C_pref_female_raw__rqmc_band", "range")
          + " while the parameter interval is "
          + n("C_pref_female_raw__cr1_interval", "range")
          + ". The two are reported side by side and never combined: they answer "
          "different questions, and a merged interval would misrepresent both.</p>"))

    W(F.fig("figU01_headline_two_intervals",
            "Each headline quantity with both intervals shown separately: the narrow "
            "resampling band and the wider parameter-uncertainty interval."))
    W(F.fig("figW04_raw_vs_equivalized",
            "Every headline object, raw against equivalized."))

    # ==================================================================== 16 ==
    W('<h2 id="s16" class="exempt">16. Endowments and needs</h2>')

    W("<p>The largest single environment channel, at "
      + n("C_needs_female_raw_share", "pct", 2) + " of baseline inequality raw and "
      + n("C_needs_female_equivalized_share", "pct", 2) + " equivalized. It is also the "
      "one most easily over-interpreted, so this section says exactly what is in it and "
      "stops there.</p>")

    W("<h3>What enters the channel</h3>")
    W("<ol>")
    W("<li><b>Non-labour resources.</b> Capital income, private transfers, and any "
      "household income that does not vary with the job taken. Two otherwise identical "
      "households with different asset income have different budgets at every "
      "alternative.</li>")
    W("<li><b>Household composition, and the needs it generates.</b> The number of "
      "dependants determines both what the tax-benefit system pays and what the "
      "household requires to reach a given standard of living. In the equivalized "
      "results the equivalence scale moves with this sub-player, which is what makes "
      "the decomposition close.</li>")
    W("<li><b>The tax-benefit system&rsquo;s operation on both of the above.</b> The "
      "simulator applies the actual French rules; family benefits, housing benefit and "
      "social assistance all respond to composition and to non-labour income.</li>")
    W("</ol>")

    W(box("warn", "There is no &ldquo;contribution of the tax system&rdquo; here, and "
                  "it must not be invented",
          "<p>The tax-benefit system is <b>held fixed at the actual French rules in "
          "every state of the decomposition</b>. It is never varied, so nothing in this "
          "channel &mdash; or in any other &mdash; is the effect of the tax system, the "
          "effect of a reform, or a measure of redistribution achieved.</p>"
          "<p>The channel measures the inequality attributable to households "
          "<em>differing</em> in non-labour resources and composition, <em>under</em> "
          "the actual system. A system that redistributed more would change the "
          "number, and the paper cannot say by how much, because no alternative system "
          "is ever simulated. If someone asks &ldquo;so how much does the French tax "
          "system reduce inequality of opportunity?&rdquo;, the honest answer is that "
          "this paper does not answer that question and would need a policy module to "
          "do so.</p>"))

    W("<h3>Splitting it further: the current status</h3>")
    W("<p>The obvious next question is which of the two ingredients &mdash; resources or "
      "composition &mdash; carries the channel. A nested split of exactly that kind, "
      "using the same Owen machinery one level deeper, has been constructed and run. Its "
      "structural checks pass: the coalition states are coherent, the sub-players act "
      "through distinct budget panels rather than being mechanically indistinguishable, "
      "and the split is a genuine nesting rather than a re-decomposition.</p>")
    W(box("warn", "Status at the time of writing: provisional, and therefore not "
                  "reported as a result",
          "<p>The nested endowments-and-needs split carries a <b>provisional</b> label "
          "pending economics review. It has not been admitted, and no ADMITTED verdict "
          "exists for it on disk at build time.</p>"
          "<p><b>Its numbers are therefore not printed in this document.</b> Reporting a "
          "provisional split alongside admitted results would put two different evidential "
          "standards in the same table. If it is admitted before the seminar, this "
          "section gains a table; if it is not, the qualitative account above is what "
          "should be said.</p>"
          "<p><b>What to say if asked in the meantime:</b> that the channel combines "
          "non-labour resources with composition and needs; that separating them is a "
          "well-posed exercise using the same machinery, already built; and that it is "
          "under review rather than complete. That is a better answer than a "
          "number.</p>"))

    W("<h3>Why the channel is as large as it is</h3>")
    W("<p>The magnitude surprises people, so it is worth having the intuition ready. "
      "Three reasons, none of which requires the provisional split:</p>")
    W("<ul>")
    W("<li><b>It is the only channel that operates on non-employed households.</b> Job "
      "access and earning opportunities work through the labour market. For a household "
      "with no earner, the entire budget is non-labour resources and transfers, so all "
      "of its position is in this channel.</li>")
    W("<li><b>It acts on the level of the budget, not on its slope.</b> The market "
      "channels shift the <em>distribution of achievable</em> outcomes; non-labour "
      "income shifts the budget at <em>every</em> alternative simultaneously. A "
      "level shift moves the money-metric measure more than a change in the shape of "
      "the reachable set does.</li>")
    W("<li><b>It absorbs composition, which is highly unequal and strongly correlated "
      "with everything else.</b> Lone parenthood raises needs and constrains labour "
      "supply at the same time.</li>")
    W("</ul>")
    W("<p>Section&nbsp;18 sharpens this: under the common-opportunity benchmark, a "
      "substantial part of the market-side contribution the benchmark cannot represent "
      "<b>reappears inside this channel</b>, at "
      + n("rum_omitted_share_relabelled_as_needs", "pct", 1)
      + " of the omitted share. Endowments and needs is where a model that ignores "
      "opportunity heterogeneity puts what it cannot see.</p>")

    # ==================================================================== 17 ==
    W('<h2 id="s17" class="exempt">17. Geographic access</h2>')

    W("<p>Job access splits cleanly into a geographic part &mdash; region, urbanisation "
      "and the local unemployment rate &mdash; and everything else the access block "
      "owns. The split is exact: the two sub-players partition the access "
      "block&rsquo;s regressors with no overlap and no remainder, so equalizing both "
      "reproduces the whole access channel bitwise.</p>")

    W('<div class="scroll"><table><thead><tr><th>Quantity</th>'
      '<th class="num">Raw</th><th class="num">Equivalized</th></tr></thead><tbody>'
      "<tr><td><b>Geographic access, share of baseline inequality</b></td>"
      '<td class="num">' + n("geo_share_of_I00_raw", "pct", 2) + " &plusmn; "
      + n("geo_share_of_I00_raw__band", "pp", 2) + "</td>"
      '<td class="num">' + n("geo_share_of_I00_equivalized", "pct", 2) + " &plusmn; "
      + n("geo_share_of_I00_equivalized__band", "pp", 2) + "</td></tr>"
      "<tr><td><b>Geographic access, share of the job-access channel</b></td>"
      '<td class="num">' + n("geo_share_of_C_acc_raw", "pct", 1) + "</td>"
      '<td class="num">' + n("geo_share_of_C_acc_equivalized", "pct", 1) + "</td></tr>"
      "<tr><td><b>Parameter-uncertainty interval on the geographic share</b></td>"
      '<td class="num">' + n("C_geo_over_I00_female_raw__cr1_interval", "rangepct", 1)
      + "</td><td class=\"num\">&mdash;</td></tr>"
      "</tbody></table></div>")

    W("<p><b>Geography is essentially the whole of the job-access channel.</b> On the "
      "raw basis it is " + n("geo_share_of_C_acc_raw", "pct", 1)
      + " of it; on the equivalized basis it is "
      + n("geo_share_of_C_acc_equivalized", "pct", 1) + " &mdash; slightly above one "
      "hundred per cent, because the non-geographic remainder turns marginally negative "
      "there. A negative sub-channel is not an error: Shapley contributions to a "
      "nested split are not constrained to be positive, and a remainder this close to "
      "zero with a band that covers it is the arithmetic saying <em>the non-geographic "
      "part of job access contributes essentially nothing</em>.</p>")

    W("<h3>The same-profile, different-region illustration</h3>")
    W("<p>The cleanest way to convey what the geographic channel <em>is</em>: take a "
      "household and move it across the " + n("n_regional_environments", "int")
      + " regional environments the model estimates, changing nothing else about it.</p>")
    W('<div class="scroll"><table><thead><tr><th>Household</th>'
      "<th>Employment-opportunity mass across regional environments</th>"
      "<th>Reading</th></tr></thead><tbody>"
      "<tr><td><b>First matched household</b></td>"
      '<td class="num">' + n("regional_opportunity_mass_range_A", "range")
      + "</td><td>Strong access almost everywhere; region matters little for this "
      "profile.</td></tr>"
      "<tr><td><b>Second matched household</b></td>"
      '<td class="num">' + n("regional_opportunity_mass_range_B", "range")
      + "</td><td>Access nearly doubles between the weakest and strongest environment, "
      "for the <em>same person</em>.</td></tr>"
      "</tbody></table></div>")
    W("<p>This is the illustration to use in the talk. The second household&rsquo;s "
      "employment opportunity is a different object depending only on where it lives, "
      "and none of that difference is a preference.</p>")

    W(F.fig("figG01_nested_geographic_access",
            "The nested split of job access into its geographic and non-geographic "
            "parts, with bands."))
    W(F.fig("figG02_regional_access_environments",
            "The regional employment-opportunity environments the illustration moves "
            "a household across."))
    W(F.fig("figE1R_reverse_pair",
            "The reverse matched pair: two households given nearly the same opportunity "
            "distribution and the same observed job, ranked on the distance between "
            "their preference profiles. The companion to the forward pair in "
            "section&nbsp;4."))

    W(box("warn", "What the geographic result is and is not",
          "<ul>"
          "<li><b>It operates through the employment-access margin only.</b> In this "
          "model region, urbanisation and local slack enter <em>only</em> the "
          "employment-access block. The exercise therefore moves how likely employment "
          "is, and nothing else.</li>"
          "<li><b>Hours, occupation and wage distributions are held invariant.</b> The "
          "counterfactual does not give a household another region&rsquo;s wage "
          "structure or hours composition. Those channels are separately identified and "
          "separately equalized elsewhere; here they are fixed. The number is therefore "
          "a <em>lower</em> bound on anything one might mean by the total importance of "
          "place.</li>"
          "<li><b>It is a structural counterfactual, not a causal region effect.</b> It "
          "asks what the estimated model implies if the geographic access arguments took "
          "a common value. It does <b>not</b> say what would happen if someone moved, or "
          "if a region&rsquo;s labour market improved. Those questions need exogenous "
          "variation in location, which a single cross-section with self-selected "
          "residence does not provide. Anyone who lives in a strong labour market may "
          "have moved there.</li>"
          "<li><b>The subgroup pattern is worth knowing.</b> The geographic share is "
          + n("subgroup_men_geo_share", "pct", 1) + " for men and "
          + n("subgroup_women_geo_share", "pct", 1) + " for women &mdash; close, unlike "
          "the total access channel, which is much larger for men at "
          + n("subgroup_men_acc_share_raw", "pct", 1) + " against "
          + n("subgroup_women_acc_share_raw", "pct", 1) + ".</li>"
          "</ul>"))

    # ==================================================================== 18 ==
    W('<h2 id="s18" class="exempt">18. The common-opportunity benchmark</h2>')

    W("<p>This is the section that prices the modelling convention the paper argues "
      "against, and it produced the most interesting negative result in the "
      "project.</p>")

    W("<h3>Exactly what is changed</h3>")
    W("<p><b>One thing.</b> The heterogeneous opportunity density is replaced by a "
      "<em>common</em> one: every household faces the same offer environment. Everything "
      "else &mdash; the preference specification, the budget from the simulator, the "
      "sample, the frame, the estimation protocol, the welfare measure, the "
      "decomposition machinery &mdash; is held identical, and the benchmark is "
      "<b>re-estimated</b> rather than being the preferred model with terms switched "
      "off. That matters: a fair comparison must let the restricted model do the best it "
      "can.</p>")
    W("<p>The result is a conventional random-utility labour-supply model of the kind "
      "the literature standardly estimates. The comparison is therefore not a straw man; "
      "it is the alternative most readers already have in mind.</p>")

    W('<div class="scroll"><table><thead><tr><th></th>'
      "<th>Estimated model, heterogeneous opportunities</th>"
      "<th>Common-opportunity benchmark</th></tr></thead><tbody>"
      "<tr><td><b>Log-likelihood</b></td>"
      '<td class="num">' + n("rum_pref_model_negll", "f2") + "</td>"
      '<td class="num">' + n("rum_bench_negll", "f2") + "</td></tr>"
      "<tr><td><b>Free parameters</b></td>"
      '<td class="num">' + n("rum_pref_model_n_free", "int") + "</td>"
      '<td class="num">&mdash;</td></tr>'
      "<tr><td><b>Likelihood-ratio statistic</b></td>"
      '<td class="num" colspan="2">' + n("rum_bench_LR_statistic", "f1")
      + " on " + n("rum_bench_df", "int") + " degrees of freedom &mdash; the "
      "restriction is decisively rejected</td></tr>"
      "<tr><td><b>Measured inequality, change</b></td>"
      '<td class="num">&mdash;</td>'
      '<td class="num">' + n("rum_inequality_drop_raw", "signpct", 1) + " raw, "
      + n("rum_inequality_drop_equivalized", "signpct", 1) + " equivalized</td></tr>"
      "<tr><td><b>Preference share of baseline</b></td>"
      '<td class="num">' + n("rum_share_pref_RURO_raw", "pct", 2) + " raw, "
      + n("rum_share_pref_RURO_equivalized", "pct", 2) + " equivalized</td>"
      '<td class="num">' + n("rum_share_pref_RUMB_raw", "pct", 2) + " raw, "
      + n("rum_share_pref_RUMB_equivalized", "pct", 2) + " equivalized</td></tr>"
      "</tbody></table></div>")

    W("<h3>The behavioural finding: opportunities come back as tastes</h3>")
    W("<p>Deprived of an opportunity block, the benchmark has to explain the same "
      "observed choices using preferences alone &mdash; and it does, by <b>absorbing the "
      "availability structure into the taste parameters</b>.</p>")
    W("<ul>")
    W("<li><b>The hours-band availability constants reappear as tastes.</b> Comparing "
      "the " + n("rum_bench_n_constants", "int") + " hours-band availability constants "
      "of the estimated model with their relocated counterparts in the benchmark, the "
      "mean absolute difference is " + n("rum_bench_const_mad", "f4")
      + ". They are recovered almost exactly &mdash; but now labelled as preferences. "
      "The statutory-week concentration, which the estimated model attributes to what "
      "employers offer, becomes in the benchmark a widely shared <em>preference</em> for "
      "working exactly the statutory week.</li>")
    W("<li><b>The estimated sex difference in the valuation of leisure reverses "
      "sign.</b> The male-minus-female leisure intercept gap is "
      + n("rum_leisure_gap_final", "sf4") + " in the estimated model and "
      + n("rum_leisure_gap_benchmark", "sf4") + " in the benchmark. Not smaller &mdash; "
      "<b>opposite</b>. A researcher using the conventional model would conclude the "
      "opposite thing about male and female tastes for time from the very same "
      "data.</li>")
    W("</ul>")
    W("<p>This is the paper&rsquo;s strongest positive-side argument, and it does not "
      "depend on any welfare judgement. Even a reader with no interest in inequality of "
      "opportunity should care that the sign of an estimated taste parameter is an "
      "artefact of the choice-set assumption.</p>")

    W("<h3>The welfare finding, including the part that did not go as expected</h3>")
    W("<p>Measured inequality falls sharply: " + n("rum_inequality_drop_raw", "pctabs", 1)
      + " on the raw basis. Having removed the variation in reachable sets, there is "
      "genuinely less inequality for an opportunity-sensitive measure to find. And by "
      "construction job access and earning opportunities contribute exactly zero &mdash; "
      "those zeros are the benchmark&rsquo;s definition made arithmetic, not estimates "
      "that happened to vanish.</p>")

    W(box("key", "The honest result: the preference share barely moves",
          "<p>The natural expectation is that a model without opportunity heterogeneity "
          "must attribute far more to preferences. <b>In this application it does "
          "not.</b> The preference share goes from "
          + n("rum_share_pref_RURO_raw", "pct", 2) + " to "
          + n("rum_share_pref_RUMB_raw", "pct", 2) + " raw &mdash; and on the "
          "equivalized basis it actually goes <em>down</em>, from "
          + n("rum_share_pref_RURO_equivalized", "pct", 2) + " to "
          + n("rum_share_pref_RUMB_equivalized", "pct", 2) + ".</p>"
          "<p>This is reported prominently because it cuts against the paper&rsquo;s own "
          "most convenient story. The convenient story would be &lsquo;ignore "
          "opportunities and you will blame the poor for their own poverty&rsquo;. That "
          "is <b>not</b> what happens here, and saying so is more useful than "
          "overclaiming.</p>"))

    W("<h3>Where the missing attribution actually goes</h3>")
    W("<p>If the market-side share the benchmark cannot represent does not become "
      "preferences, where does it go? The decomposition answers this exactly.</p>")
    W('<div class="scroll"><table><thead><tr><th>Destination</th>'
      '<th class="num">Share of the omitted market-side contribution</th>'
      "<th>Reading</th></tr></thead><tbody>"
      "<tr><td><b>Leaves the measured total entirely</b></td>"
      '<td class="num">' + n("rum_omitted_share_leaves_measured_total", "pct", 1) + "</td>"
      "<td>The dominant destination. The inequality is not reattributed &mdash; it "
      "<em>stops being measured</em>. A model that cannot see opportunity differences "
      "cannot see the inequality they generate.</td></tr>"
      "<tr><td><b>Reappears as endowments and needs</b></td>"
      '<td class="num">' + n("rum_omitted_share_relabelled_as_needs", "pct", 1) + "</td>"
      "<td>Just over a third is relabelled into the non-market channel. This is a "
      "genuine misclassification: labour-market opportunity presented as household "
      "circumstance.</td></tr>"
      "<tr><td><b>Reappears as preferences</b></td>"
      '<td class="num">' + n("rum_omitted_share_relabelled_as_preferences", "signpct", 1)
      + "</td><td><b>Slightly negative.</b> The preference channel takes on marginally "
      "<em>less</em>, not more.</td></tr>"
      "</tbody></table></div>")

    W(box("say", "The result stated correctly, in one paragraph",
          "<p>&ldquo;Omitting heterogeneous opportunities changes the behavioural "
          "interpretation substantially &mdash; availability constants come back as "
          "tastes, and the estimated sex difference in the valuation of leisure reverses "
          "sign &mdash; and it reduces measured welfare inequality by about a quarter. "
          "But it does <b>not</b> materially raise the preference share of the welfare "
          "decomposition. The bulk of what is lost, roughly two thirds, leaves the "
          "measured total altogether rather than being reattributed; about a third "
          "reappears as household endowments and needs; and the preference channel takes "
          "on marginally less, not more.&rdquo;</p>"))

    W(F.fig("figR01_benchmark_decomposition",
            "The decomposition under the estimated model and under the "
            "common-opportunity benchmark. The market-side channels are identically zero "
            "in the benchmark by construction."))

    return H
