---

title: "Equality of Opportunity: Theory and Measurement"
authors: ["John E. Roemer", "Alain Trannoy"]
year: 2016
outlet: "Journal of Economic Literature"
country_or_context: "General theoretical and measurement survey with illustrations from Europe, the United States, Latin America, Africa, and Turkey"
population: "General populations partitioned by circumstance types; empirical illustrations include male workers, children, and adult populations across multiple countries"
data_period: "Survey article; illustrative datasets include EU-SILC 2005 and various panel and cross-sectional datasets from earlier empirical studies"
shelf: "equality_of_opportunity_theory_measurement_survey"
tags: ["equality of opportunity", "responsibility-sensitive egalitarianism", "circumstances and effort", "Roemer identification assumption", "Fleurbaey-Maniquet", "measurement", "fairness gap", "direct unfairness", "economic development", "inequality of opportunity"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Roemer, John E., and Alain Trannoy. 2016. “Equality of Opportunity: Theory and Measurement.” *Journal of Economic Literature* 54(4): 1288–1332. 

# One-sentence contribution

The paper is a major survey that synthesizes the philosophical foundations, economic models, empirical measurement strategies, and development applications of equality of opportunity, with particular emphasis on the distinction between circumstances and responsibility-sensitive factors. 

# Why this paper matters

This paper matters because it is not merely another contribution inside the equality-of-opportunity literature; it is an organizing synthesis of the field. It connects the philosophical move away from pure welfarism to the economic construction of policy criteria, then to econometric measurement and comparative evidence. For research design, it is especially valuable because it lays out both what the theory is trying to do and where the measurement problems are severe. 

For your project, this is one of the most important background papers because it helps separate several issues that are often blurred together: compensation versus responsibility, Roemer versus Fleurbaey–Maniquet, type-based versus tranche-based measurement, direct unfairness versus fairness gap, and lower-bound versus upper-bound empirical interpretations. It is less useful as a direct structural labour-supply paper, but extremely useful as a map of the normative and measurement landscape around opportunity-sensitive evaluation.

# Core research question

How should equality of opportunity be theorized and measured once one rejects purely outcome-based welfarism and instead insists that only some kinds of inequality are ethically objectionable—namely, those due to circumstances rather than to responsibility-sensitive factors? 

# Economic setting and context

The paper is a survey article rather than a single-country study or one-model contribution. Its context is the broad late-twentieth-century shift from equality of outcomes toward equality of opportunity in political philosophy and economics. Roemer and Trannoy present the paper explicitly as an interdisciplinary synthesis linking philosophy, economic modeling, and empirical measurement. 

Empirically, the article draws on a large comparative literature. The illustrative graphs on pages 1295–1296 compare Danish and Hungarian male workers by parental-education types using EU-SILC 2005 data, and later sections review evidence from Sweden, Norway, the United States, Germany, Italy, Latin America, Africa, Turkey, and health datasets for Europe. The paper is therefore broad and comparative, not tied to a single institutional application. 

# Model / theoretical framework

The central model class in section 3 is Roemer’s equal-opportunity framework. A population is partitioned into circumstance types (T={1,\dots,T}). There is a desirable outcome (u^t(e,\varphi)), where (e) is effort and (\varphi) is policy, and there are type-specific effort distributions (G_\varphi^t). The key normative move is that because effort distributions themselves are shaped by circumstances, “accountable” effort is measured by rank within the type-specific effort distribution, not by raw effort level. The outcome quantile functions are then (v^t(\pi,\varphi)), and inequality of opportunity is reflected in their differences across types. 

Roemer’s baseline policy criterion is the “mean-of-mins” objective
[
\max_\varphi \int_0^1 \min_{t\in T} v^t(\pi,\varphi), d\pi,
]
which chooses the policy that maximizes the area under the lower envelope of the type-specific outcome quantile functions. This is interpreted as nullifying, as far as possible, the effect of circumstances while preserving sensitivity of outcomes to effort. Pages 1294–1295, including the Denmark–Hungary graphs on pages 1295–1296, are the core statement. 

The paper then contrasts this with Van de gaer’s “min-of-means” criterion and with the Fleurbaey–Maniquet approach. Van de gaer replaces Roemer’s mean-of-mins with a maximin over type means, which the paper links to an “equalizing opportunity sets” interpretation. Fleurbaey and Maniquet, by contrast, weaken and recombine compensation and reward principles, emphasizing natural or liberal reward and ordinal allocation rules such as conditional equality and egalitarian equivalence. Pages 1296–1303 summarize these differences.

The framework is explicitly normative, not positive. It is about ordering policies and assessing injustice, not about estimating a behavioural labour-supply model. Even the measurement sections are not structural choice models in your sense; they are econometric and distributional techniques designed to quantify inequality attributable to circumstances.

# Key objects

The core objects are circumstances, effort, type, outcome, and policy. In Roemer’s formulation, types collect individuals with the same circumstances; effort is responsibility-sensitive; and the policy problem is to choose (\varphi) so as to reduce type-based differences in outcome prospects. This is the paper’s main conceptual architecture. 

A second key object is Roemer’s accountable effort rank, often referred to in the later literature as the Roemer Identification Assumption. Under that assumption, the morally relevant effort variable is the rank of an individual in the type-specific effort distribution. This object allows inter-type effort comparability in poor-information settings, but the paper is clear that it is analytically contestable and empirically vulnerable when circumstances are imperfectly observed.

A third key set of objects is the family of empirical measurement tools. These include direct unfairness (DU), fairness gap (FG), inequality-of-opportunity ratios based on decomposable inequality indices, type and tranche approaches, stochastic-dominance conditions, and the human opportunity index. Section 6 systematizes these objects and explains what each is measuring.

A fourth key object is the proposed development index (d=(Y_D,\eta)), where (Y_D) is the average income of the most disadvantaged type and (\eta=Y_D/Y) measures how close average income of the worst-off type is to overall average income. This is the article’s most explicit development proposal. Figure 2 on page 1307 plots this index for European countries. 

# Data

The paper is not based on one dataset. It is a survey article drawing on many empirical studies and data sources. The illustrative figure comparing Denmark and Hungary uses EU-SILC 2005 male worker data with three parental-education types, shown on pages 1295–1296. Section 6 then reviews results from PSID, GSOEP, Scandinavian administrative and panel data, SHARELIFE, Latin American and African surveys, and Turkish datasets.

Because this is a survey, the paper’s empirical contribution lies more in classifying measurement strategies than in producing one unified database. The authors repeatedly stress that most datasets remain poor for equality-of-opportunity analysis because they lack either rich circumstance variables, credible effort variables, or both. That diagnosis is one of the main takeaways of section 6. 

# Identification logic

Identification is one of the paper’s central concerns, especially in the measurement section. The paper repeatedly argues that equality-of-opportunity analysis is more demanding than standard inequality measurement because it is inherently multidimensional and often requires a first-stage econometric model before any second-stage inequality assessment can be attempted. The authors explicitly present EOp analysis as a two-stage exercise: estimate the process that generates outcomes, then measure the part attributable to circumstances. 

In rich-data settings, the recommended logic is structural or semi-structural econometric estimation. One estimates an outcome equation and reaction equations for effort variables, allowing circumstances to affect effort and possibly allowing demographic shifters to mediate responses. The authors stress that using only a reduced form may be enough to quantify the overall impact of observable circumstances, but it sacrifices the ability to distinguish direct from indirect channels or to interpret demographics cleanly. Pages 1313–1316 are especially important here. 

In poor-data settings, one may rely on Roemer’s identification axiom or weaker forms of type-independent effort-distribution assumptions. But the paper is careful: if relevant circumstances are omitted, identifying effort with rank in the type-conditional outcome distribution can be incorrect. This is a major warning. The paper treats most empirical estimates of inequality of opportunity as lower bounds precisely because of incomplete information on circumstances. 

The paper is therefore quite explicit that much of the empirical literature does not establish causal effects of circumstances in a strong policy-evaluation sense. Correlations with past circumstances may still be ethically relevant for inequality-of-opportunity measurement, but they are not the same as validated policy elasticities. This distinction is one of the paper’s methodological strengths. 

# Estimation / empirical strategy

The paper does not estimate a single model, but it offers a taxonomy of empirical strategies. In rich-data settings, it recommends estimating a system consisting of an outcome equation plus effort “reaction” equations. In poor-data settings, it emphasizes type-based or tranche-based approaches, nonparametric or semiparametric estimates of conditional distributions, and direct use of type-conditional outcome distributions under Roemer-style assumptions. 

The survey highlights the contrast between reduced-form and structural approaches. Reduced forms can recover the total association of circumstances with outcomes, but they cannot cleanly decompose direct and indirect effects or separate demographic factors that act as circumstances from those operating through preferences or responsibility-sensitive channels. Structural systems are preferred when feasible, but the paper is realistic that the data often do not support them. 

A recurring theme is that residuals are difficult to interpret. Depending on the study, residual variation has been assigned to effort, to circumstances, or to neither. The authors are skeptical of ad hoc treatment and often recommend working with the explained part of the outcome when the residual is too large and conceptually mixed. This is a very important caution for any empirical adaptation. 

# Treatment of preferences

Preferences are treated in two different ways in the paper, depending on which strand of the literature is under discussion. In the philosophical and Fleurbaey–Maniquet sections, preferences can themselves be responsibility-relevant objects, especially under Dworkin’s or Fleurbaey’s preference-sensitive frameworks. In those approaches, one may be held responsible for preference-based choices, at least under demanding conditions.

In Roemer’s framework, by contrast, preferences are not primitive normative objects. What matters is the decomposition into circumstances and effort, and accountable effort is measured by rank in the type distribution. This reflects a control or access view rather than a strict preference view. The paper explicitly contrasts these two understandings in section 6.1.3. 

For your project, one important point is that the paper explicitly notes the empirical difficulty of estimating preferences in a way that would justify the preference-view approach. It even cites work such as Bargain et al. (2013) as rare attempts to estimate cross-country heterogeneity in the consumption–leisure trade-off. So the survey is clear that preference-sensitive EOp theory is conceptually rich but empirically demanding. 

# Treatment of opportunities / constraints

This section is crucial for your agenda. The paper is fundamentally about opportunities, but not in the same structural sense as a latent-jobs or feasible-job-set model. “Opportunity” is typically represented by outcome prospects conditional on circumstance types, not by an explicit individual feasible-set object (A_i). Thus, the paper is opportunity-sensitive in a normative and distributional sense, but not menu-explicit in a structural labour-market sense.

In Roemer’s approach, opportunities are effectively the type-specific outcome distributions or quantile functions faced by agents once morally comparable effort is defined. In Van de gaer’s interpretation, the type mean may be viewed as summarizing an opportunity set. In Fleurbaey–Maniquet, the language shifts toward compensation and reward principles rather than type-specific prospect distributions. But across all these approaches, the paper does not model actual job offers, hours restrictions, or latent opportunity densities.

The survey is therefore very helpful for thinking about compensation for truncated opportunity prospects, but much less helpful for representing actual feasible job sets. It helps distinguish ethically compensable inequality from responsibility-sensitive inequality; it does not by itself separate preferences from observed opportunity sets in a structural labour-supply model. [reasonable inference for my project] supported by

# Welfare / normative object

The paper is explicitly non-welfarist. It opens by emphasizing that more than final welfare outcomes is needed for ethically salient judgment and that classical welfarism ignores the responsibility-relevant structure behind outcomes. This is a central thesis of the paper, already present in the introduction and reaffirmed in the Roemer model section.

There is not one welfare object in the article. Rather, the survey reviews several classes of evaluative objects. Roemer’s framework uses lower-envelope-based policy criteria over type-specific outcome quantiles; Van de gaer uses opportunity-set or type-mean criteria; Fleurbaey–Maniquet use ordinal fairness criteria such as conditional equality and egalitarian equivalence; empirical measurement sections use direct unfairness and fairness-gap concepts; the development section proposes a two-dimensional index based on the worst-off type’s average income and the ratio of that average to aggregate income.

This makes the paper highly useful for welfare measurement under heterogeneous circumstances and responsibility conceptions. It is not, however, a paper about equivalent variation, compensating variation, or a structural utility-based labour-supply welfare metric. Nor is it explicitly about responsibility for opportunity sets in the jobs-and-wellbeing sense. It is broader and more foundational than that.

# Main findings

The paper’s first main finding is synthetic rather than theorem-level: the equality-of-opportunity literature replaces outcome-only ethics with a framework in which some inequalities are objectionable and others are not, depending on whether they derive from circumstances or responsibility-sensitive factors. The introduction and philosophical review make this the governing claim of the survey. 

The second main finding is that Roemer’s policy criterion is best understood as a compensating-outcomes approach built on type-specific accountable-effort ranks, whereas Van de gaer’s criterion is closer to an equalizing-opportunity-sets approach. The paper makes this distinction explicitly and uses the simple two-type, two-effort example on pages 1297–1298 to show that Van de gaer’s objective can violate the compensation principle even when it yields a higher sum of outcomes. Table 1 and Table 2 on page 1298 are central. 

The third main finding is that the Roemer and Fleurbaey–Maniquet traditions differ importantly on reward. Roemer’s mean-of-mins criterion embeds utilitarian reward in one-type societies and allows a broader family of reward aggregators ( \Gamma^{(p)} ), while Fleurbaey–Maniquet privilege natural or liberal reward and ordinal fairness rules. Table 4 on page 1303 neatly summarizes this contrast: egalitarian-equivalent and conditional equality prioritize natural reward; mean-of-mins and min-of-means prioritize utilitarian reward.

The fourth main finding is empirical. The Denmark–Hungary comparison in figure 1 shows visibly closer parental-education income distributions in Denmark than in Hungary, illustrating lower inequality of opportunity in Denmark with respect to that one circumstance. The paper also stresses that such exercises are lower bounds because many relevant circumstances remain omitted. Pages 1295–1296 make both points clearly. 

The fifth main finding is that when development is redefined opportunity-sensitively, GDP per capita is no longer sufficient. The proposed development pair (d=(Y_D,\eta)) places emphasis on the worst-off type and on the degree of opportunity equalization. Figure 2 on page 1307 shows that no European country dominates all others on both dimensions, though Denmark performs especially strongly. 

The sixth main finding is methodological and empirical together: most existing empirical measures of inequality of opportunity are lower bounds, because data on relevant circumstances and effort are incomplete. Yet even with this limitation, the literature suggests that inequality of opportunity accounts for a large share of total inequality. The survey reports shares around 15–30 percent in several developed-country income studies without IQ, around 30 percent in Sweden once IQ is included, around 30 percent in the United States and Germany in some specifications, much higher upper bounds in Niehues and Peichl, and often even larger shares in Latin America and Africa. Pages 1322–1327 summarize these results. 

# Main limitations

The paper’s first limitation for your project is the absence of an explicit feasible-set or latent-opportunity-set model. Opportunity is measured largely through outcome distributions across circumstance types, not through structural job opportunities. For a project centered on (A), that is a real boundary. [reasonable inference for my project] supported by

A second limitation is the unresolved theory of reward to effort. The paper is quite explicit that equality-of-opportunity theory by itself does not fully determine the ethically correct reward structure. Roemer’s (\Gamma^{(p)}) family leaves room for different inequality aversions with respect to effort-generated outcomes, and the survey openly says this is an incomplete part of the theory. 

A third limitation is empirical fragility. The survey repeatedly emphasizes omitted circumstances, noisy or conceptually dubious effort proxies, and the difficulty of causal identification. In practice, this means that many headline numbers are not only model-dependent but also information-dependent lower bounds. 

A fourth limitation is that the field remains normatively plural. Roemer, Van de gaer, and Fleurbaey–Maniquet do not generate the same policy rankings, because they make different trade-offs between compensation and reward, or between ex ante and ex post perspectives. The survey is strong precisely because it does not hide this non-uniqueness.

# Relevance for my JMP

## possible use for framing

This paper is excellent for framing. It provides the cleanest broad statement of why pure outcome inequality is ethically insufficient and why the decomposition of inequality into compensable and responsibility-sensitive components matters. If your JMP needs a paragraph motivating why a jobs-and-wellbeing framework cannot be outcome-only, this paper is a core source. 

## possible use for model design

It is useful for model design mainly at the normative and measurement level. It helps you decide whether your project is conceptually closer to Roemer’s rank-based compensating-outcomes logic or to a Fleurbaey–Maniquet-style ordinal fairness logic. It does not offer a direct structural labour-supply specification, but it tells you what your structural model would need to speak to normatively. [reasonable inference for my project] supported by

## possible use for identification

This is one of the most useful parts for your JMP. The paper gives a sober map of what can and cannot be identified in practice, clarifies the role of reduced forms versus structural systems, and warns against naive use of residuals and crude effort proxies. For a paper trying to separate preferences from opportunities, these warnings are directly relevant. 

## possible use for welfare measurement

Very high. The paper does not hand you one definitive welfare measure, but it provides a menu of principled non-welfarist evaluative approaches and shows how they connect to measurement practice. It is especially useful for clarifying what an opportunity-sensitive welfare statistic would have to do differently from GDP, mean income, or standard utilitarian welfare.

## possible use for decomposition

Very high. This is one of the main strengths of the survey. It systematizes decomposition between circumstances, effort, and residual luck, and reviews direct-unfairness, fairness-gap, entropy-based, and Shapley-style decomposition methods. Even if your decomposition target differs, the paper is a key methodological reference.

## possible use for comparative application

High. The paper shows how opportunity-sensitive measures can be used comparatively across countries and how rankings can differ from standard inequality or development rankings. For a later comparative application of your framework, especially across welfare states or tax-benefit systems, this is an important precedent.

# Research questions this paper inspires

Can one reformulate Roemer’s type-based outcome-prospect framework so that type differences are partly generated by explicit feasible job sets (A_i) rather than only by background circumstances?

How would the Roemer–Van de gaer–Fleurbaey–Maniquet taxonomy change in a labour-market model where job opportunities, not only effort distributions, vary by type?

Can a jobs-and-wellbeing measure (W(z,R,A;y)) generate direct-unfairness or fairness-gap decompositions that are structurally interpretable rather than only distributional?

What empirical design would let one distinguish true opportunity deprivation from omitted circumstances currently absorbed into residuals in equality-of-opportunity measurement?

How much of observed cross-country inequality of opportunity in income would survive once one conditions on explicit labour-market opportunity measures rather than only parental background, IQ, or education?

# Challenge to this paper

The sharpest challenge, from your perspective, is that although the paper is about opportunities, its dominant formal objects are still type-conditional outcome distributions rather than concrete feasible-set structures. That is sufficient for many normative and measurement exercises, but it may be insufficient when the key question is whether unequal outcomes arise because people faced different menus of jobs, hours, or wages. In that sense, the paper is strongest on the ethical architecture of opportunity-sensitive evaluation and weaker on the microeconomic representation of opportunities themselves. [reasonable inference for my project] supported by

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The survey insists that ethically salient evaluation requires more than final outcomes, because one must know how responsibility-sensitive factors and non-responsibility factors contributed to those outcomes. That is deeply aligned with the spirit of a jobs-and-wellbeing project. 

[reasonable inference for my project] In your notation, the paper is strongest on how (z)-like realized outcomes should be normatively interpreted once one has a partition between compensable and non-compensable heterogeneity. It is much weaker on giving a structural account of (A), and only partially informative on (R), because “effort” is often measured behaviorally or distributionally rather than through fully specified preference primitives.

[explicit in paper] The survey does not define a well-being measure (W(z,R,A;y)), does not use person-specific feasible-job-set notation, and does not develop a labour-supply or RURO model. Its main formal objects are types, outcome distributions, effort ranks, and policy orderings. 

[reasonable inference for my project] In your taxonomy, the paper is closest to responsibility-versus-compensation, compensation for opportunities in a broad background sense, and decomposition of inequality into ethically distinct sources. It is not close to independence of (A) if (A) is treated as normatively relevant, and it has no direct analogue of independence of (y). It is also not a laissez-faire framework, except where Fleurbaey–Maniquet’s natural reward principle or one-type benchmark is discussed.

[unclear from paper] It remains unclear how the survey’s measurement and policy criteria would change if actual feasible job sets (A_i) were explicitly modeled and ethically assessed, rather than inferred indirectly through observed outcome distributions across circumstance types. 

# Relation to Bargain et al. (2013)

The relation is real but not central. The survey cites Bargain et al. (2013) as a rare effort to estimate cross-country heterogeneity in the consumption–leisure trade-off, which matters because preference-sensitive equality-of-opportunity theories require unusually demanding empirical information. In that sense, Bargain et al. appear here as part of the empirical frontier on estimating responsibility-relevant heterogeneity, not as the main organizing literature of the survey. 

# Relation to opportunities vs preferences

This paper is strongly about the opportunities-versus-preferences problem, but mainly at the normative and measurement level, not the structural job-choice level. It repeatedly contrasts views that emphasize control, access, or rank-based effort with views that emphasize identified preferences, and it is very clear that the empirical treatment of effort depends on which view one adopts.

For your project, the key takeaway is that the literature has not settled this issue. Roemerian measurement tends to operationalize responsibility through type-relative effort ranks; Fleurbaey–Maniquet and Dworkinian approaches move closer to preference-sensitive responsibility; empirical work often lacks the data to implement either side cleanly. That diagnosis is directly relevant to any attempt to separate (R) from (A) rigorously.

# Useful quotations / formulas

The core Roemer criterion is
[
\max_\varphi \int_0^1 \min_{t\in T} v^t(\pi,\varphi), d\pi,
]
presented on pages 1294–1295. This is the formal expression of the mean-of-mins approach. 

The survey’s alternative generalized reward family is
[
\Gamma^{(p)}(\theta)=\left(\int_0^1 \theta(\pi)^p, d\pi\right)^{1/p},
]
for the lower-envelope function (\theta(\pi)=\min_t v^t(\pi,\varphi)). This is the main formal device used to show that reward-to-effort remains underdetermined inside the theory. Page 1299 is the key location. 

Table 4 on page 1303 is especially useful because it summarizes the four main allocation rules in one place: egalitarian-equivalent and conditional equality under natural reward; mean-of-mins and min-of-means under utilitarian reward. This table is one of the most efficient conceptual maps in the paper. 

The development section’s proposed index is
[
d=(Y_D,\eta), \qquad \eta=\frac{Y_D}{Y},
]
with (Y_D) the average income of the most disadvantaged type and (Y) average income overall. Figure 2 on page 1307 plots European countries in this two-dimensional space. 

The measurement section’s dual notions of direct unfairness and fairness gap are also central. DU measures the inequality present in a counterfactual distribution in which each type is collapsed to its mean outcome; FG measures the difference between total inequality and the inequality attributable to effort-counterfactual equalization across types. Section 6.3.2 is the main reference.

# Suggested tags

equality-of-opportunity-survey, circumstances-vs-effort, responsibility-sensitive-egalitarianism, Roemer-identification-assumption, mean-of-mins, min-of-means, conditional-equality, egalitarian-equivalence, direct-unfairness, fairness-gap, opportunity-sensitive-development

# My quick takeaway

This is probably the single best survey paper to keep at hand while designing an opportunity-sensitive research program. It does not solve your jobs-and-wellbeing problem directly, because it lacks an explicit feasible-job-set representation. But it gives you the conceptual map you need: how responsibility enters, why opportunity-sensitive evaluation is non-welfarist, how different authors trade compensation against reward, how empirical measurement is constrained by weak data, and why many existing numbers are lower bounds. For your JMP, it is best treated as the master survey on the normative and empirical equality-of-opportunity literature, to be complemented by structurally richer latent-job papers when you want to operationalize the (A)-dimension.
