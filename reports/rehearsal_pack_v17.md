# Seminar rehearsal script — V17

16 main slides (the title slide plus 15 numbered slides) and 4 backup slides after the conclusion. Slide numbers match the footline of JMP_seminar_beamer_v17.pdf; the title slide is unnumbered.

EA is presented first, as the prospect perspective; ATT is the attained-outcome benchmark. That is an order of presentation: neither perspective is designated primary.

## Title slide — Title

On slide: Unequal Job Opportunities and Well-Being Inequality A Latent-Jobs Structural Decomposition Hisham Haydar University of Luxembourg and LISER

Say:

Thank you. This talk asks how much of the inequality in money-metric well-being goes with unequal job opportunities rather than with differences in what people prefer. I build the answer in four steps: a model of labour supply as choice among latent jobs, which separates preferences from opportunities; two ways of turning choices into euros of well-being; counterfactuals that equalise one source of heterogeneity at a time; and a Shapley rule that allocates the change. The punchline is that the answer depends on the welfare question: prospects or attained outcomes.

## Slide 1 — Motivation

On slide: Motivation Observed Ci Gini of consumption single adults 0.2633 couples 0.2268 Well-being Mi Gini of the attained-bundle money metric single adults 0.2498 couples 0.1974 low earnings ⇐= tastes or opportunities or resources equivalised, household-weighted, within each population 1/15

Say:

Two people can work the same hours for the same hourly pay and be very differently placed. One chose that job from several that were open; the other took the only offer available. Their incomes are identical and their circumstances are not.

Low earnings can describe someone who values leisure and chose short hours, someone who cannot obtain a well-paid job, or someone whose household resources make a different arrangement affordable. An income distribution records outcomes with these explanations already mixed in.

The numbers make the point in the French data: once the leisure a job costs is valued, the dispersion of well-being is not the dispersion of consumption. These are within-population dispersion comparisons, not welfare-loss estimates, and single-adult and couple households are separate populations that I never compare with each other.

## Slide 2 — The conflict

On slide: The conflict Compensation unequal job opportunities should not become unequal well-being Responsibility preference-based choices should not be compensated Compensation vs. Responsibility ∄W : Full Compensation ∧Full Responsibility [Fleurbaey & Maniquet] 2/15

Say:

Before any data, the conflict that makes this paper necessary.

A fair well-being comparison would like to respect two principles. The first is compensation: people should not end up worse off because they face worse job opportunities. The second is responsibility: people should be held responsible for their preferences, their tastes for work, leisure and consumption, so a choice that reflects taste should not generate a compensation claim.

Each principle is attractive on its own, but they cannot both be imposed in full: no well-being measure satisfies full compensation and full responsibility together. The literature, following Fleurbaey and Maniquet, is organised around compromises.

The empirical consequence is the reason for this paper. To know what to compensate, we must separate what people prefer from what they can reach. And observed choices mix the two.

## Slide 3 — Research question

On slide: Research question How much inequality in money-metric well-being is associated with unequal job opportunities rather than heterogeneous preferences, once labour supply is modelled as choice among latent jobs? 1. Do observed labour-supply choices reflect preferences alone, or also heterogeneous latent job opportunities? 2. How do conclusions differ when welfare evaluates the attained bundle versus the ex-ante opportunity prospect? 3. In a restricted P/A/B decomposition, how much welfare inequality is associated with preferences, local access, and earning opportunities? 3/15

Say:

The whole talk on one slide. The first subquestion is behavioural: can we read preferences off choices, or do opportunities get in the way? The second is normative: once well-being is valued in euros, does it matter whether we value the prospect a household faces or the outcome it attains? The third is the accounting: in a restricted decomposition with preferences, local access and earning opportunities as the three channels, how is inequality allocated?

Note the word associated. Nothing in this talk is a causal claim.

## Slide 4 — Literature and gap

On slide: Literature and gap Latent jobs Aaberge, Dagsvik & Strøm Dagsvik & Jia Cap´eau, Decoster & Dekkers Money metrics Fleurbaey & Maniquet Decoster & Haan Jacquet, Jia & Thoresen Decomposition Shorrocks Creedy & H´erault M¨uhlhan reforms and changes −→ a level of well-being inequality preferences vs. opportunities, inside an estimated latent-jobs model 4/15

Say:

Every ingredient has antecedents; the contribution is the combination and the empirical answer.

Labour supply as choice among latent jobs, with preference and opportunity components jointly estimated under maintained restrictions, is due to Aaberge, Dagsvik and Strøm, developed by Dagsvik and Strøm and by Dagsvik and Jia, and set out for applied work by Capéau, Decoster and Dekkers, who already cover singles and couples.

Money-metric evaluation with such models exists, but it evaluates a change between policy regimes. The normative literature following Fleurbaey and Maniquet, with Decoster and Haan and Bargain and co-authors, shows how the reference encodes compensation and responsibility.

The closest decompositions, Creedy and Hérault and Mühlhan, decompose a change between situations. Our object is a cross-sectional level of well-being inequality, decomposed into preferences and opportunities inside an estimated latent-jobs model. The Shapley rule itself is inherited from Shorrocks; no new allocation principle is claimed.

## Slide 5 — Job packages

On slide: Job packages j = (e, k, h, w) 4 occupation groups Ci(j) priced through EUROMOD vi(j) = Li(j) + βc log Ci(j) λc  Li value of leisure: age; children for women βc weight on log consumption, estimated λc units convention 5/15

Say:

In words: a household's systematic value of a job is the value of the leisure it leaves plus the log of the consumption it pays.

A job is a package: an employment state, one of four occupation groups, weekly hours and an hourly wage. Every package is run through the French tax-benefit system, so consumption is the household's actual disposable income at that job. A single adult chooses one package; a couple chooses a pair under a shared budget, and the leisure term sums both spouses' terms.

The split between leisure and consumption matters later: consumption is observable in euros and leisure is not, and the split is what turns a utility gap into a proportional consumption adjustment in both welfare measures. The household-specific leisure coefficients are the preference channel. The child term is a reduced-form time-constraint shifter, not pure taste.

## Slide 6 — Opportunities: the choice probability

On slide: Opportunities: the choice probability Pi(j) = exp{vi(j)} gi(j) Z exp{vi(k)} gi(k) dν(k) access employment mass hours bands occupation by sex wage offers education, experience valued or plentiful 6/15

Say:

In words: the probability of being seen in a job is its value times its availability, normalised over all jobs.

The function g is the household's opportunity density: how intensely a package is available to it before any choice. A job is chosen often when it is valued or when it is plentiful. If everyone faced the same density we would be back to a standard model, in which every difference in behaviour must be a difference in taste. Because the density is household-specific, part of behaviour can be attributed to reachability.

The density has four blocks. Access, the employment mass, moves with local unemployment exposure, region, urban or rural location, and year. Hours are a step function over bands. Occupation availability is sex-specific. Wage offers are log-normal, located by education and experience.

Separation rests on maintained restrictions, not tested ones: smooth preferences against banded hours opportunities; local shifters excluded from preferences; wage offers independent of hours given occupation. The regional variation is not a causal design.

## Slide 7 — Data and EUROMOD

On slide: Data and EUROMOD EU-SILC France collected 2016, incomes 2015 1,540 single-adult households 2,223 couple households EUROMOD French 2015 policy system h ∈[5, 70] w ∈[2, 590] 100 priced alternatives per household 7/15

Say:

The data are French EU-SILC, collected in the year on the slide, with incomes referring to the previous year. Taxes, benefits and disposable income come from EUROMOD under the policy system in force over the income period.

The samples are single-adult and couple households with every adult of working age, not in education and not receiving a pension. Multi-generational households and same-sex couples are outside the estimated population, so no result extends to them. The two samples are estimated separately.

Hours are in hours per week and wages in euros per hour; those are the supports the opportunity densities are defined on. Each household's likelihood is evaluated on its observed job plus a set of sampled alternatives, each run through the tax-benefit model. Sampling is a computational device, not an offer: it enters no welfare measure.

## Slide 8 — Estimation

On slide: Estimation Household-specific opportunities free coordinates 41 population fit 0.0140 Common opportunities free coordinates 10 / 16 population fit 0.0273 / 0.0264 criterion worse by at least 141.64 choices reflect opportunities, not preferences alone single adults; population fit is the mean absolute deviation of predicted from observed moments 8/15

Say:

The first subquestion. Take away the household-specific opportunity block, re-estimate everything else, and the model does worse: on the same households, the same sampled alternatives and the same criterion.

The two benchmarks are a common opportunity distribution with re-estimated preferences, and a common opportunity shape with employment and hours moved into utility. The deterioration is concentrated where the opportunity block does its work: population fit roughly doubles its error, and occupation margins deteriorate by an order of magnitude.

I do not turn this into a likelihood-ratio test, because the sampled-alternative criterion is not the likelihood of the observed data. A better criterion does not by itself establish that a mechanism has been identified.

Fit is not perfect either. The observed concentration at exactly thirty-seven hours is underpredicted in every group, and extensive-margin accuracy for men is withheld because numerical integration error is too large relative to sampling variation.

## Slide 9 — Welfare

On slide: Welfare Own-set equal-consumption equivalents: each individual gets a common consumption on every job in their own ability set; the level at which the preferred job is indifferent to the attained bundle is their money metric, comparable across individuals. Adapted from Haydar and Maniquet (2026), work in progress. 9/15

Say:

Estimated utility is not an interpersonal welfare index: preferences differ, so the same utility number means different things for different people. To compare households, each situation is translated into euros through an indifference condition with an explicit reference. The choice of reference is the welfare question.

Both money metrics in this paper descend from this construction in the companion theory paper. Each individual is evaluated with their own preferences and their own set of jobs. Give every job in that set the same consumption; the individual then prefers one of them, and the consumption at which that job is exactly as good as the attained bundle is their money metric. The point is that these metrics are comparable across people whose preferences and job sets differ.

The figure is a theoretical illustration with no estimated value in it. The next two slides take the construction to the data in two ways: applied to the whole estimated prospect, and applied to the outcome attained.

## Slide 10 — Ex-ante prospect welfare

On slide: Ex-ante prospect welfare Ji = Z eLi(j) Ci(j) λc βc bgi(j) dν(j), Hi = Z eLi(j) bgi(j) dν(j), MEA i = λc exp n log Ji−log Hi βc o Ji the actual prospect Hi same jobs, equal pay MEA i flat-consumption equivalent 10/15

Say:

In words: EA is the constant monthly consumption at which a prospect with the household's own jobs and availability, but equal pay everywhere, is worth exactly as much as the prospect it actually faces.

J values the household's actual prospect over its whole estimated opportunity environment: every job enters, weighted by how available it is and how much it is valued. H is the reference: the same jobs, the same availability and the same preferences, with pay differences removed. Opportunities enter welfare directly: access moves which jobs carry weight; earning opportunities move what they pay. A common rescaling of the opportunity density cancels.

I show this perspective first because this talk is about opportunities; that is an order of presentation, not a ranking.

Under the extreme-value shocks, log J is the expected utility of the best reachable job up to a constant, so the measure treats taste-shock variety as part of what makes a rich prospect valuable. That is a normative position, not a consequence of estimation, and I flag it. The ex-ante calculation passed its numerical checks, which certifies the computation, not the model's assumptions.

## Slide 11 — Attained-bundle welfare

On slide: Attained-bundle welfare Matt i = C obs i exp Li(jobs i ) −Li(o) βc  o non-employment, reachable by all jobs i the only route for opportunities 11/15

Say:

In words: ATT is observed consumption, adjusted by the leisure the job costs relative to not working, converted at the rate one over the consumption weight.

The reference is non-employment, which every household can reach. The general construction evaluates the attained bundle against the job the household would most prefer if all jobs paid the same; on the current empirical domain that job is non-employment for every household, so the measure coincides with the staying-home equivalent. That is a verified property of this specification, not a general theorem.

Opportunities matter only through which job is attained and what it pays; once that job is fixed, jobs not taken play no role. For non-workers the measure equals observed consumption; for workers it lies below by the value of the leisure given up.

The two measures answer different welfare questions: one values the prospect, the other the attained outcome. Neither corrects the other.

## Slide 12 — Inequality and Shapley decomposition

On slide: Inequality and Shapley decomposition P preferences: age, children A local unemployment exposure, region, urban or rural location, year B wage-offer location held fixed household resources, needs and composition ϕp k = X S⊆{P,A,B}\{k} |S|! (3 −|S| −1)! 3! h v p(S ∪{k}) −v p(S) i v p(S) = I p(∅) −I p(S) I p: household-weighted Gini of Mp 12/15

Say:

In words: a channel's Shapley contribution is its marginal effect on inequality, averaged over every order in which the three equalisations can be introduced; the three contributions add up exactly to the total change.

P equalises the systematic preference shifters: age profiles and the child-related shifter. A equalises local access: local unemployment exposure, region, urban or rural location, and year. It is local access, not total opportunity: personal occupation access and the hours density are left as estimated. B equalises the systematic wage-offer location, not wage dispersion. Household resources, needs and composition are held fixed in every coalition and receive no share.

Each coalition is a full structural counterfactual: coefficients never change, welfare is recomputed for every household under each perspective, and inequality is measured again. The same operators and rule are applied to both perspectives, which is what makes their orderings comparable. Contributions are signed. Adding resources, needs and composition as a fourth channel is a planned extension; access plus earnings would remain the opportunity component.

## Slide 13 — Results: prospects versus attained outcomes

On slide: Results: prospects versus attained outcomes EA: prospects access + earnings 7.9–21.3% of baseline Gini single adults: access > earnings; couples: no reversal ATT: attained outcomes access + earnings 1.9–6.7% of baseline Gini earnings > access, both household types 13/15

Say:

This is the result. Each panel shows the same two operators, local access and earning opportunities, as a percentage of each perspective's own baseline Gini, evaluated under the two welfare questions.

For single adults, access is the larger channel when welfare values the prospect, about three times earning opportunities on both reporting scales, and earning opportunities are the larger channel when welfare values the attained outcome. For couples, earning opportunities stay in front under both: no reversal.

The mechanism is the route by which opportunities enter. The attained-bundle measure sees only the realised job, where the wage drives consumption, so systematic differences in wage offers dominate. The ex-ante measure weights every job by its availability, so the access environment enters welfare directly. Why single adults reverse and couples do not is not tested here; one reading is that a single adult's participation rests on one earner's access.

Prospects versus attained outcomes: two different welfare questions, and neither perspective is designated primary. The comparison is also not a pure contrast of definitions, because the two integrations use different designs. The full tables are in the backup.

## Slide 14 — What is not claimed

On slide: What is not claimed Scope Household resources, needs and composition held fixed Access: local access, not total opportunity Preliminary decomposition Not claimed Not causal No parameter uncertainty yet Preferences are not responsibility Neither perspective is designated primary prospects versus attained outcomes: two different welfare questions 14/15

Say:

All the boundaries in one place.

The decomposition is preliminary: a restricted structural accounting exercise, and the attained-bundle counterfactual integration is still being validated, with short hours sparsely covered.

Nothing is causal. Separation rests on maintained functional-form and exclusion restrictions, and no causal effect of geography, education or occupation is estimated.

Parameter uncertainty has not been propagated through either decomposition, so there are no confidence intervals on any share; repeat runs are simulation checks.

The preference channel is not a responsibility channel. It contains a reduced-form child term that can capture childcare constraints as well as tastes, and deciding what people should be held responsible for is a normative step this paper does not take.

Household resources, needs and composition are held fixed, and access is local access, not total opportunity, so the shares are neither a complete decomposition nor an estimate of everything unequal opportunity does. Equivalisation is a convention and changes the couples results, which is why both scales are reported. And the two welfare perspectives answer different questions; choosing between them is a normative decision not made here.

## Slide 15 — Conclusion

On slide: Conclusion 1. Choices reflect opportunities, not preferences alone. 2. Prospects: access leads for single adults. Attained outcomes: earnings lead. Couples: no reversal. 3. Restricted P/A/B: a bounded part of well-being inequality; preference sign not robust. next: resources and needs as a fourth channel · parameter uncertainty · validation 15/15

Say:

To close, the three answers.

First, observed choices carry information about opportunities: a model that gives everyone the same jobs fits worse on the same households.

Second, the importance assigned to different labour-market inequalities depends on whether welfare evaluates the opportunity prospect or the realised outcome. Access leads for single adults when we value the prospect; earning opportunities lead when we value the attained bundle; couples do not reverse.

Third, within the restricted decomposition, with resources, needs and composition held fixed, local access and earning opportunities are a bounded part of well-being inequality, and the preference contribution is not sign-robust to equivalisation.

Next steps: household resources, needs and composition as a fourth channel; propagating parameter uncertainty; completing validation of the attained-bundle integration. Neither perspective is designated primary. Thank you.

# Backup

## Backup B1 — Backup: ex-ante decomposition

On slide: Backup: ex-ante decomposition scale access earnings access + earnings ordering Gini points Gini points % of baseline Single adults raw 0.01812 0.00555 14.8 access > earnings equivalised 0.02183 0.00673 20.3 access > earnings Couples raw 0.00667 0.02049 21.3 earnings > access equivalised 0.00449 0.00504 7.9 earnings > access single adults: access = 3.3 × earnings (raw), 3.2 × (equivalised)

Say:

The ex-ante numbers behind the central figure. Access plus earnings range from 7.9 to 21.3 per cent of baseline ex-ante inequality, depending on household type and scale. The calculation passed its numerical checks, including an independent implementation. These are restricted accounting shares with resources, needs and composition held fixed.

## Backup B2 — Backup: attained-bundle decomposition

On slide: Backup: attained-bundle decomposition scale access earnings access + earnings ordering Gini points Gini points % of baseline Single adults raw 0.0016 0.0040 2.4 earnings > access equivalised 0.0013 0.0034 1.9 earnings > access Couples raw 0.0009 0.0128 6.7 earnings > access equivalised 0.0007 0.0062 3.5 earnings > access

Say:

The attained-bundle benchmark. Earning opportunities are larger than local access for both household types and on both scales. Every coalition Gini and contribution reproduces closely under an independent simulation run, and the allocation closes to numerical precision; those checks validate the calculation for the stated game, not its maintained assumptions. The preference contribution changes sign with equivalisation in both samples, so no directional claim is made about it. The lower part of the hours range is sparsely represented in the integration sample, which is why this exercise stays explicitly preliminary.

## Backup B3 — Backup: matched households

On slide: Backup: matched households access: A = 14.5 × B wage-offer location: B +11.5 log points

Say:

What unequal opportunity means inside the model. Two employed single men in the same occupation group, hours band and wage quintile, with nearly identical estimated leisure profiles, selected by a stated rule: a teaching example, not causal and not representative. If both were indifferent between all jobs and not working, employment would be 0.75 of A's opportunity mass and 0.17 of B's; the gap comes from local unemployment exposure and region. B's wage offers are better, yet A faces more offers paying at least any given wage over essentially all offer mass. Neither is better placed on every margin; which one is better off depends on the welfare question.

## Backup B4 — Backup: equivalisation

On slide: Backup: equivalisation Couples, ex ante: access + earnings 21.3% −→ 7.9% raw → equivalised Couples, ex ante: preferences 0.00291 −→ −0.00212 Gini points, raw → equivalised modified-OECD scale: a convention, reported both ways

Say:

Equivalisation is a normative convention and it is materially consequential for couples under the ex-ante perspective: it moves the access-plus-earnings share and turns the preference contribution negative. A negative Shapley term means that, averaged over orders, equalising preferences raises inequality; it does not show that preference heterogeneity is equalising in any causal or welfare sense. That is why both scales are always reported and no directional claim about preferences is made.

# Extended Q&A

## Is the ex-ante measure your preferred welfare measure?

No. The two measures answer different welfare questions: prospects versus attained outcomes. EA is shown first because this talk is about opportunities. Choosing between them is a substantive normative decision that the paper does not make.

## Are these causal shares of inequality due to unequal opportunities?

No. They are restricted structural accounting shares. Household resources, needs and composition are held fixed, access is local access rather than total opportunity, identification rests on maintained restrictions, and parameter uncertainty has not been propagated.

## How does the compensation-responsibility conflict connect to the estimates?

No measure satisfies full compensation and full responsibility, so any welfare comparison takes a position on what to compensate. Taking that position empirically requires separating preferences from opportunities, which is what the latent-jobs model does. The preference channel is still not equated with responsibility.

## Why does equivalisation matter so much for couples under EA?

Dividing by the modified-OECD scale moves the ex-ante access-plus-earnings share from 21.3% to 7.9% of baseline inequality and moves the preference contribution from 0.00291 to −0.00212 Gini points. Both scales are reported and no directional claim about preferences is made.

## Why do single adults reverse and couples not?

It is not tested. One reading is that a single adult's participation depends on one earner's access, while a couple's joint budget and second earner leave earning opportunities in front. The reversal is a finding for single-adult households only.

<!-- Generated by beamer/build_rehearsal_script_v17.py from beamer/JMP_seminar_beamer_v17.tex and build/JMP_seminar_beamer_v17.pdf. -->
