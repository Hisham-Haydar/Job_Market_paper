---
title: "Valuing Alternative Work Arrangements"
authors: [Alexandre Mas, Amanda Pallais]
year: 2017
outlet: "American Economic Review, 107(12), 3722--3759"
country_or_context: "United States"
population: "Job applicants to a national call center (telephone interviewer positions); Understanding America Study (UAS) nationally representative panel"
data_period: "2016 (field experiment and UAS survey)"
shelf: "job amenities / WTP / discrete choice experiment / compensating differentials / work arrangements / scheduling / work from home"
tags: [WTP, willingness-to-pay, discrete-choice-experiment, compensating-differentials, work-arrangements, flexible-scheduling, work-from-home, employer-discretion, irregular-schedules, inattention, field-experiment, gender, call-center, hedonic, Mas, Pallais]
priority: "medium"
read_status: "extracted"
---

# Full citation

Mas, A., & Pallais, A. (2017). Valuing alternative work arrangements. *American Economic Review*, 107(12), 3722--3759.

# One-sentence contribution

Embeds a discrete choice experiment in a real job application process for a national call center to estimate the WTP distribution for alternative work arrangements, finding that most workers do not value scheduling flexibility or hours choice but are willing to give up ~8% of wages for working from home and ~20% to avoid employer-set irregular schedules, with substantial heterogeneity and ~25% applicant inattention.

# Why this paper matters

This paper provides clean experimental evidence on how workers value non-wage job attributes -- the exact objects that matter for the opportunity dimension in my RURO framework. The finding that WTP distributions are highly heterogeneous (mean WTP can differ substantially from marginal WTP) implies that compensating differential estimates from observational data are unreliable guides to the full distribution of worker valuations. For my JMP, this motivates modelling job attributes beyond wages in the opportunity density $g(h, w, a)$, where $a$ captures amenities like schedule flexibility and work-from-home options.

# Core research question

What is the distribution of workers' willingness to pay for alternative work arrangements (flexible scheduling, flexible hours, work from home, employer discretion over schedules), and how do these valuations vary across worker subgroups?

# Economic setting and context

The authors staffed a national call center to implement telephone surveys. They posted job ads on a major US job board in 68 metro areas for telephone interviewer positions in 2016. During the application process, applicants were shown two job descriptions differing in work arrangements and wages, and asked to choose. This embeds a discrete choice experiment in a real market transaction, overcoming the hypothetical bias concern of standard stated preference methods. The Understanding America Study (UAS), a nationally representative internet panel, provides external validation.

# Model / theoretical framework

**Discrete choice with inattention:**
Individual $i$ chooses between job $A = 1$ (with amenity) and $A = 0$ (without) based on WTP$_i$ vs wage difference $\Delta w$. With inattention rate $\alpha$ (fraction making random choices):

$$\Pr(A_i = 1 | \Delta w) = P_{\Delta w}(1 - \alpha) + (1 - P_{\Delta w})\alpha$$
$$= F(b\Delta w + c; \mu, \sigma)(1 - 2\alpha) + \alpha$$

where $F$ is logistic CDF, $\mu = -c/b$ is mean WTP, $\sigma = 1/(0.55b)$ is WTP standard deviation. Inattention $\alpha \approx 0.145$ estimated from dominated-choice tests ($\Delta w = 5$).

**Breakpoint model:** Nests a mass point $w^*$ in the WTP distribution to capture the large fraction of workers with zero or near-zero valuation for some amenities:

$$E[\tilde{Y} | \Delta w] = \begin{cases} 1 & \text{if } \Delta w > w^* \\ F(b\Delta w_i + c; \mu, \sigma)(1-2\alpha) + \alpha & \text{if } \Delta w \leq w^* \end{cases}$$

# Key objects

- **WTP for flexible scheduling:** Mean $0.48/hr (s.e. 0.24), median $0.48. ~60% of workers have WTP near zero; a right tail values it at 10%+ of wages.
- **WTP for flexible number of hours:** Mean $-0.22/hr (s.e. 0.22), median $-0.22. Most workers prefer the fixed 40-hour M-F schedule.
- **WTP for work from home:** Mean $1.33/hr (s.e. 0.29), median $1.33. Average worker willing to give up ~8% of wages. 25% willing to pay $2.45+/hr (~14% of wages).
- **WTP for combined flexible:** Mean $1.17/hr (s.e. 0.32), close to sum of components ($1.59), suggesting no complementarity.
- **WTP to avoid employer discretion:** Mean $3.41/hr (s.e. 0.47), median $3.41. Average worker gives up ~20% of wages. 40% would not take the job even at 25% premium. Driven by aversion to evening/weekend work, not schedule inconsistency.
- **Shadow value of time (20→40 hrs):** $4.01/hr. Workers prefer full-time at substantially lower hourly wages.
- **Inattention rate:** ~25% of applicants are inattentive (choose dominated options, answer recall questions incorrectly, or select "unavailable" positions).

# Data

**Field experiment:** ~7,000 applicants to call center positions across 68 US metro areas, 2016. ~3,245 in main treatments. Five treatment arms: flexible schedule (640), flexible hours (663), work from home (608), combined flexible (694), employer discretion (640). Wages: maximum $16 or $19/hr, with randomly assigned increments $0-$5.

**UAS survey:** 2,318 respondents (84% response rate) from nationally representative Understanding America Study panel. Vignette-based choice experiments for flexible scheduling, work from home, and employer discretion.

# Identification logic

Random assignment of wage differentials and work arrangement characteristics within the application process. Each applicant sees one pair of jobs with randomly assigned attributes. The WTP distribution is identified from the relationship between the wage gap $\Delta w$ and the probability of choosing the amenity job, after correcting for inattention. External validity from UAS replication.

# Estimation / empirical strategy

1. **Inattention correction:** Estimate $\alpha$ from share choosing dominated position at $\Delta w = 5$ (position without amenity pays $5 more). $\hat{\alpha} \approx 0.145$.

2. **Maximum likelihood logit:** Estimate WTP distribution parameters $(\mu, \sigma)$ from equation (1), fixing $\alpha$.

3. **Breakpoint model:** Allow mass point in WTP distribution for arrangements with apparent discontinuity at $\Delta w = 0$ (flexible scheduling, flexible hours).

4. **Nonparametric validation:** Plot inattention-corrected shares $\tilde{Y}_{\Delta w}$ against $\Delta w$ to visually assess distributional assumptions.

5. **UAS replication:** Same framework applied to nationally representative vignette data, with inattention correction based on dominated choice at 30% wage gap.

# Treatment of preferences

Preferences over work arrangements are elicited through revealed preference in a real job choice setting. The paper documents substantial heterogeneity in valuations: for every arrangement, mean WTP differs substantially from marginal WTP, and the distribution has long tails. Key heterogeneity: (1) women value work from home more than men ($1.59 vs $0.68) and are more averse to employer discretion ($4.27 vs $2.11); (2) women with young children are especially averse to irregular schedules (WTP ~40% of wages); (3) surprisingly, neither education, cognitive ability (ACT scores), nor age significantly predict WTP for flexibility (Table 12). The focus group evidence reveals that some workers prefer fixed schedules as commitment devices -- they worry they would not work enough if given flexibility (echoing Kaur, Kremer, and Mullainathan 2015).

# Treatment of opportunities / constraints

The paper does not model demand-side constraints. Workers are assumed to face two job options and freely choose between them. The key insight for opportunity modelling is implicit: the paper documents that many workers are in jobs with attributes they would pay to change (e.g., 20% of workers would pay to avoid their current irregular schedule, but only 10% are in formal work-from-home arrangements despite 21% of workers willing to take a pay cut for it). This gap between WTP and observed arrangements implies either employer-side constraints (it is costly for firms to offer these arrangements), search frictions, or both. The paper interprets this through the Rosen (1986) hedonic framework: under perfect sorting, the compensating differential equals the marginal worker's valuation, but frictions and heterogeneity in costs break this.

# Welfare / normative object

No explicit welfare analysis. The paper estimates WTP distributions, which are the building blocks for welfare analysis (compensating variation, equivalent income). The estimated WTP distributions could be used to compute the welfare cost of suboptimal job matching in the presence of frictions.

# Main findings

1. **Most workers do not value scheduling flexibility:** ~60% have near-zero WTP for flexible scheduling. The median WTP is close to $0. But a right tail (top 25%) is willing to give up 10%+ of wages.

2. **Workers do not value hours flexibility:** The median worker slightly prefers the fixed 40-hour M-F job over choosing their own hours. This is partly due to self-control concerns (preference for commitment).

3. **Workers value working from home:** Average WTP ~8% of wages ($1.33/hr). 20% prefer on-site even at equal pay.

4. **Strong aversion to employer-set schedules:** Average WTP to avoid ~20% of wages ($3.41/hr). 40% would reject even at 25% premium. Driven by aversion to evening/weekend work, not schedule unpredictability per se.

5. **Women value amenities more:** Especially work from home (+$0.91 gender gap) and avoiding employer discretion (+$2.16 gender gap). But differences in work arrangement prevalence by gender are too small to explain much of the gender wage gap (at most 1.7-2.0 ppt).

6. **Inattention is pervasive:** ~25% of applicants are inattentive. This affects tail estimates of WTP distributions but not means. First paper to explicitly incorporate inattention into WTP estimation from discrete choice experiments.

7. **Field experiment and survey agree:** UAS vignette estimates are very close to field experiment results, validating the survey approach when well-designed.

8. **Large implied compensating differentials:** Under perfect sorting, work-from-home jobs would pay 21% less; flexible-schedule jobs 11% less; employer-discretion jobs 20% more. Actual differentials are much smaller, implying imperfect sorting.

# Main limitations

- Call center applicants: specific population (disproportionately female, younger, less educated than workforce average), though UAS replication suggests generalizability.
- Binary choice only: no rich choice sets or trade-offs among multiple attributes simultaneously.
- No demand-side modelling: cannot say whether observed arrangement prevalence reflects employer costs or worker preferences.
- Static: no dynamics (learning about job attributes, career concerns, human capital effects of flexibility).
- Partial equilibrium: does not account for general equilibrium effects of widespread adoption of alternative arrangements.
- Cannot distinguish taste for specific hours from taste for schedule commitment (though focus group evidence helps).

# Relevance for my JMP

## possible use for non-wage job attributes in the opportunity density
The paper provides direct evidence that non-wage job attributes (schedule flexibility, work location, employer discretion over schedules) have substantial monetary valuations that vary enormously across workers. In my RURO framework, the opportunity density $g(h, w)$ describes the distribution of available jobs over hours and wages. This paper motivates extending $g$ to $g(h, w, a)$ where $a$ captures amenity bundles. The welfare cost of limited opportunities depends not just on the (h, w) distribution but on the amenity packages attached to available jobs.

## possible use for the heterogeneity finding
The finding that WTP heterogeneity is very large (mean and marginal WTP differ substantially) implies that representative-agent welfare analysis would misstate the welfare effects of changes in the opportunity set. In my equivalent income framework, individual-level preference heterogeneity over job attributes translates into heterogeneous equivalent incomes and different identifications of who is worst-off.

## possible use for the gap between WTP and observed arrangements
The paper documents that many workers are in suboptimal arrangements (would pay to change them), implying demand-side or frictional constraints on the opportunity set. This is exactly the RURO motivation: the opportunity set $A_i$ constrains workers to jobs that may not match their preferred attributes.

# Research questions this paper inspires

1. How would the equivalent income computation change if the opportunity density $g(h, w, a)$ included amenity dimensions? Workers in jobs with employer-set irregular schedules have lower equivalent income (after subtracting WTP to avoid the arrangement) than their wage suggests. The magnitude is large: 20% of wages for employer discretion.

2. Can the WTP distribution be used to calibrate the disutility of non-standard work arrangements in a structural labour supply model? The paper provides reduced-form WTP estimates; a structural model would integrate these with budget constraint computation and preference estimation.

# Challenge to this paper

The paper assumes free choice between two job descriptions, but in reality workers face a constrained opportunity set. A worker who dislikes irregular schedules may have no choice but to accept such a job if no regular-schedule jobs are available in her local labour market. The WTP estimates capture preferences conditional on having two options; they do not capture the welfare cost of having only one option (no choice). In the RURO framework, the welfare cost of limited opportunities depends on the probability that a worker encounters jobs with desirable attributes, not just on her WTP conditional on having a choice. A worker with high WTP to avoid employer discretion but who faces an opportunity set where all available jobs have employer discretion suffers a larger welfare loss than the WTP estimate suggests, because the WTP is estimated at the margin of having both options available.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The WTP for job attributes maps directly to the marginal rate of substitution between wages and amenities in my utility specification. The paper's $\mu$ (mean WTP) and $\sigma$ (WTP dispersion) characterize the preference distribution over job attributes, which would be an input to the well-being function $W(z, R, A; y)$ where $z$ includes amenity dimensions.

[Reasonable inference for my project] The large WTP heterogeneity implies that job quality (as measured by equivalent income) depends heavily on the amenity bundle, not just on hours and wages. The gap between the worker's preferred and actual arrangement, valued at the individual WTP, is a component of the equivalent income correction for non-income dimensions (analogous to the leisure correction in Fleurbaey & Gaulier 2009, but for job amenities rather than hours).

[Unclear from paper] Whether the WTP estimates from a binary choice experiment can be directly used in a discrete-choice labour supply model where workers choose from a multidimensional opportunity set including hours, wages, and multiple amenity dimensions. The binary design identifies one dimension at a time but does not capture interactions among attributes in a rich choice setting.

# Relation to Bargain et al. (2013)

Indirect connection. Bargain et al. (2013) estimate preferences over hours and consumption only, abstracting from non-wage job attributes. Mas & Pallais show that non-wage attributes have large valuations, suggesting that the Bargain et al. framework understates the welfare costs of limited labour market opportunities by ignoring amenity heterogeneity across jobs. In the equivalent income framework, a worker who is forced into a job with employer discretion over scheduling has lower equivalent income than Bargain et al. would compute, because the disamenity value (~20% of wages) is not captured by their hours-consumption utility.

# Relation to opportunities vs preferences

The paper is fundamentally about preferences (WTP for job attributes), but its implications are about opportunities. The key finding -- that many workers are in arrangements they would pay to change -- implies that the opportunity set constrains workers' ability to realize their preferred job attributes. The paper interprets this through the hedonic/compensating differentials framework (Rosen 1986), where sorting is imperfect due to frictions or heterogeneous employer costs. In my RURO framework, this would be captured by the opportunity density $g(h, w, a)$: not all $(h, w, a)$ combinations are available to all workers, and the welfare cost of limited opportunities includes the amenity mismatch valued at individual WTP.

# Useful quotations / formulas

**On heterogeneity in valuations (p. 3726):**
"We find evidence of heterogeneity in valuations in all of the job attributes we consider; mean WTP estimates may differ substantially from marginal WTP estimates. Caution is therefore warranted when interpreting cost-benefit analyses that are based on average valuations alone."

**On most workers not valuing flexibility (p. 3726):**
"Our first, surprising, finding is that the great majority of workers do not value scheduling flexibility: either the ability to set their own days and times of work at a fixed number of hours, or the ability to choose the number of hours they work."

**On employer discretion (p. 3745):**
"The average worker is willing to give up 20 percent of wages to avoid this work arrangement, and almost 40 percent of applicants would not take this job even if it paid 25 percent more than a M-F 9 AM-5 PM position."

**On inattention (p. 3725):**
"We implemented several placebo tests which confirmed that approximately 25 percent of applicants are inattentive. By estimating the inattention rate, we can account for misclassification in the econometric model and recover the unbiased WTP distribution."

**On commitment (p. 3740, footnote 33):**
"Although being able to choose my hours would be nice, I would kind of have to force myself to work the 40 hours a week"; "I prefer to have set hours so I will know for sure what my schedule will be."

**On gender (p. 3727):**
"While, on average, women do not tend to value flexible schedules, they do place a higher value on working from home and avoiding irregular work schedules than do men."

# Suggested tags

WTP, willingness-to-pay, discrete-choice-experiment, compensating-differentials, work-arrangements, flexible-scheduling, work-from-home, employer-discretion, irregular-schedules, inattention, field-experiment, gender, call-center, hedonic, Rosen, Mas, Pallais, UAS, commitment-device, heterogeneity

# My quick takeaway

A landmark experimental paper showing that (1) most workers don't value scheduling flexibility, (2) workers value working from home at ~8% of wages, (3) workers are strongly averse to employer-set irregular schedules (~20% of wages), and (4) WTP heterogeneity is very large, making mean-based analyses misleading. For my JMP, the key implication is that the opportunity density should include amenity dimensions beyond hours and wages, and that the welfare cost of limited opportunities includes amenity mismatch valued at heterogeneous individual WTP. The gap between observed arrangements and WTP-implied optimal arrangements directly motivates the RURO approach: workers face constrained opportunity sets that prevent realization of preferred job attributes.
