---

title: "Valuing Alternative Work Arrangements"
authors: ["Alexandre Mas", "Amanda Pallais"]
year: 2017
outlet: "American Economic Review"
country_or_context: "United States"
population: "Job applicants to a national call-center position; supplementary nationally representative U.S. survey respondents in the Understanding America Study"
data_period: "Field experiment conducted during 2016 hiring; CPS comparison data from 2001, 2004, and 2016; UAS survey contemporaneous to the study"
shelf: "work_arrangements_labor_supply_job_attributes"
tags: ["work arrangements", "discrete choice experiment", "compensating differentials", "working from home", "schedule flexibility", "irregular schedules", "job amenities", "willingness to pay", "United States"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Mas, Alexandre, and Amanda Pallais. 2017. “Valuing Alternative Work Arrangements.” *American Economic Review* 107(12): 3722–3759. 

# One-sentence contribution

The paper estimates workers’ willingness to pay for alternative job arrangements using a discrete choice experiment embedded in an actual hiring process, and finds very low average valuation of worker-controlled scheduling flexibility, substantial valuation of work-from-home options, and very strong aversion to employer-controlled irregular schedules. 

# Why this paper matters

This paper matters because it identifies valuations of specific job attributes in a setting much closer to actual labor-market choice than standard hedonic wage regressions. It is explicitly motivated by the fragility of observational compensating-differential estimates and replaces them with a field-based discrete choice design. That makes it methodologically important for any project that wants to treat work arrangements as genuine components of jobs rather than as noisy correlates in cross-sectional wage equations. 

For your project, its strongest relevance is on the positive side of job attributes and worker valuation. It shows how workers value specific work arrangements—schedule predictability, working from home, control over hours, and employer discretion—without inferring these from observed wages alone. It is not a paper about feasible job sets (A) in the strong normative sense, but it is very useful for thinking of jobs as bundles of attributes rather than as wage-hour pairs only. 

# Core research question

How much are workers willing to pay, in wage terms, for alternative work arrangements such as flexible scheduling, the ability to choose hours, work from home, and avoidance of employer-controlled irregular schedules? 

# Economic setting and context

The empirical setting is a national U.S. call-center hiring campaign. The authors posted ads in 68 metro areas for telephone interviewer positions and embedded a discrete choice experiment directly into the application process. Job seekers compared a standard Monday–Friday 9 am–5 pm on-site job to alternative work arrangements with randomized wage differences. This is the central field setting of the paper. 

The broader context is the U.S. policy and employer debate over flexibility, telecommuting, overtime regulation, and unpredictable scheduling. The paper explicitly links its question to debates over work-life balance, scheduling laws, telecommuting policies, and the emerging “gig economy.” Pages 3722–3724 frame the paper in exactly these terms. 

# Model / theoretical framework

The model class is a discrete choice experiment interpreted through a compensating-differentials / random-utility framework. Individuals choose between two jobs that are identical except for wages and one job amenity. If job (A=1) has the amenity and job (A=0) does not, the key latent object is worker (i)’s willingness to pay (WTP_i) for the amenity. The worker chooses the amenity job when (WTP_i > -\Delta w), where (\Delta w=w_1-w_0). The paper then estimates the distribution of (WTP_i) from observed choices. This is developed in Section II. 

The framework is positive, not normative. The paper does not construct welfare criteria or social rankings. It estimates valuations over job attributes in a way that can inform compensating-differential interpretation and employer or policy decisions. It therefore belongs much more to labor economics of job amenities than to welfare economics in the Fleurbaey–Maniquet sense. 

The feasible set is not modeled explicitly as a set (A). Instead, the analyst presents workers with paired job options whose attributes are experimentally varied. So the paper does not model opportunities as latent job-arrival processes or individualized feasible menus; it observes stated-but-market-embedded choices over experimentally described alternatives. 

# Key objects

The central economic objects are the willingness-to-pay distribution (WTP_i), the wage difference (\Delta w), the job amenity indicator (A), and the probability of choosing the amenity job:
[
P_{\Delta w} \equiv \Pr(WTP_i > -\Delta w).
]
Equation (1) then modifies this with an inattention parameter (\alpha), producing a mixture-choice probability that combines attentive and inattentive applicants. This is the main econometric object of the paper. 

The main job attributes studied are flexible scheduling, flexible number of hours, working from home, a combined flexible arrangement, and employer discretion over schedules. Supplementary treatments further isolate consistent irregular schedules, early shifts, evening shifts, weekend work, and overtime. Table 2 on page 3731 lists the main treatment descriptions. 

# Data

The main data come from approximately 7,000 job seekers who entered the application process for the call-center positions; the main-treatment analysis uses subsamples of roughly 600–700 applicants per treatment, as shown in Table 2 and Table 5. The application data include choices over job descriptions, age, zip code, race/ethnicity, gender, education, and a short cognitive test. Pages 3728–3731 describe the field design. 

The paper supplements the field experiment with nationally representative U.S. survey data from the Understanding America Study. That survey is used to probe external validity and heterogeneity, especially by parental status and current job arrangements. Table 8 on page 3749 is central for those comparisons. 

The paper also uses CPS and CPS Work Schedules Supplement data for descriptive comparisons and to show the difficulty of estimating compensating differentials observationally. Table 1 on page 3724 shows conventional wage regressions in which more worker-friendly arrangements are often positively associated with wages, underscoring the identification problem in hedonic estimates. 

# Identification logic

Identification comes from randomized variation in wages and job attributes across applicants in the choice experiment. Because the baseline and alternative jobs differ only in specific attributes and pay, the observed choice probability as a function of (\Delta w) identifies the willingness-to-pay distribution for that attribute under the maintained random-utility assumptions. This is much cleaner than observational wage-amenity regressions. 

A second identification issue is inattention. The paper is unusually careful here. It implements placebo and dominated-choice checks and shows that many applicants are inattentive. The authors estimate the inattention rate by the share choosing a dominated position when it pays $5 less, compare this to explicit placebo checks, and incorporate the resulting misclassification rate into the ML estimator. Pages 3731–3733 are central. 

This is not causal identification of labor-supply or productivity primitives. It is identification of the distribution of monetary valuations of job attributes conditional on the experimental environment and sample. The paper is explicit that conventional compensating-differential estimates are fragile and that its method is designed precisely to circumvent those omitted-variable and sorting problems. 

# Estimation / empirical strategy

The empirical strategy is maximum likelihood estimation of the willingness-to-pay distribution from discrete choices over randomized job pairs. The baseline parametric assumption is that (WTP_i) follows a logistic distribution. The paper estimates both a standard ML logit and, where needed, a “breakpoint” model that allows mass points in the WTP distribution to capture the sharp nonlinearities visible in the nonparametric choice shares. Pages 3732–3734 explain this in detail. 

The paper also nonparametrically plots the inattention-corrected share choosing the amenity job against the wage premium (\Delta w). Figures 1–5 are very useful because they let the reader visually assess the distributional shape and the quality of fit. The authors then report mean, standard deviation, and selected quantiles of WTP. Table 5 on page 3737 is the main summary table for the field experiment. 

# Treatment of preferences

Preferences are explicit, but in a reduced-form valuation sense rather than through a structural utility function over consumption and leisure. The paper does not estimate labor-supply preferences or a utility representation over income and hours. Instead, it directly estimates willingness to pay for job amenities from binary job choices. Preferences here are valuations over work arrangements. 

A major strength is that the paper estimates not only mean valuations but full distributions, emphasizing heterogeneity. The authors stress that average WTP can be misleading because many arrangements show substantial dispersion and thick right tails even when the mean valuation is small. This is especially true for flexibility. Pages 3737–3745 make this point repeatedly, and Table 5 shows it clearly. 

# Treatment of opportunities / constraints

This paper does not model opportunities explicitly as feasible job sets or latent offer distributions. It does not estimate a job-arrival process, hours restrictions, or demand-side constraints in the RURO sense. There is no individualized (A)-object. 

However, the paper is still useful for thinking about opportunities in a weaker but important sense: jobs are not characterized solely by wages. They are bundles of attributes, and workers value those attributes heterogeneously. The paper therefore contributes to the empirical treatment of jobs as multidimensional options. That is highly relevant if one wants later to define opportunity sets over richer job descriptions rather than over wages or hours alone. [reasonable inference for my project] supported by 

The paper does not distinguish preference heterogeneity from opportunity heterogeneity. It measures how workers value different job attributes when those attributes are presented as available alternatives. So it is strong on attribute valuation but weak on the structural distinction between “what jobs are available” and “which jobs are preferred.” 

# Welfare / normative object

The paper is purely positive with policy relevance. Its welfare language is individual willingness to pay, not fairness, compensation, or responsibility. It does not propose a social welfare function, a well-being measure, or an ethically grounded ranking of workers. 

That said, it is relevant for welfare applications indirectly because it provides monetary valuations of job attributes that could enter compensating-variation, equivalent-income, or job-quality analyses. The paper itself discusses implications for employer policy, scheduling regulation, and compensating differentials, but it does not itself carry out a normative welfare exercise. 

It is not useful directly for responsibility for opportunities, compensation for opportunities, actual versus reference opportunity sets, or decomposition of inequality. Those are outside its explicit scope. 

# Main findings

The headline result is that most workers are not willing to pay much for worker-controlled scheduling flexibility. In the field experiment, the estimated mean WTP for flexible scheduling is only $0.48 per hour, with median WTP also $0.48; for flexible number of hours, the mean is slightly negative at (-$0.22). Table 5 on page 3737 is the key source. 

At the same time, the paper finds substantial heterogeneity. For flexible scheduling, the upper tail of the WTP distribution is large enough to support nontrivial compensating differentials even though the average worker values it little. The discussion around Figure 1 on pages 3737–3738 emphasizes that about 60% of workers do not value flexibility at all, yet a right tail remains. 

Workers do value working from home. In the field experiment, the average worker is willing to give up about 8% of wages for the option to work from home; the mean WTP is $1.33 per hour in Table 5. The UAS delivers a very similar mean estimate of 10% of wages overall, and 8.4% when reweighted by the commute distribution in the field experiment. Table 8 on page 3749 and Table 9 on page 3751 are the key sources. 

Workers strongly dislike employer-controlled irregular schedules. In the field experiment, the average worker is willing to give up about 20% of wages to avoid employer discretion, with mean WTP $3.41 per hour; the bottom quartile still requires about 10% of wages to accept that arrangement. Table 5 and Figure 5 on pages 3744–3745 are central. 

The paper then unpacks this aversion. Supplementary treatments show that workers mainly dislike evening and weekend work rather than the instability of having schedules change week to week. Table 7 on page 3746 reports mean WTP of $2.39 to avoid evening schedules and $3.27 to avoid weekend schedules, values close to the aversion to employer discretion itself. This is one of the most important substantive findings. 

The paper also finds that most workers prefer 40-hour jobs to 20-hour jobs at the wages studied. Table 6 on page 3741 shows that the mean WTP for a 40-hour relative to a 20-hour position is $6.00 per hour, implying a low average shadow value of time between 20 and 40 hours. By contrast, workers require a premium for overtime beyond 40 hours. 

On gender, women value working from home more and dislike employer discretion more than men. Table 10 on page 3753 shows mean WTP of $1.59 for women versus $0.68 for men for work from home, and $4.27 versus $2.11 to avoid employer discretion. In the UAS, these differences are especially strong for women with young children, as shown in Table 11 on page 3753. 

# Main limitations

The first limitation is that the sample is selected from applicants to a particular type of call-center job. The authors address external-validity concerns through reweighting and the UAS, but the main field estimates are still conditional on this applicant pool. This matters for generalization to the whole labor market. 

A second limitation is that the paper estimates valuations over described alternatives, not actual long-run job choices with realized productivity consequences, promotion tracks, or dynamic learning. The setup is much more realistic than a purely hypothetical vignette, but it is still not a full revealed-preference labor-market equilibrium. 

A third limitation for your project is that it does not model feasible sets or job availability. It values arrangements conditional on presentation, but it does not study who has access to which jobs or how opportunity sets differ across people. Thus it is much stronger on job-attribute valuation than on opportunities. 

A fourth limitation is that the interpretation of “flexibility” is narrower than some policy rhetoric suggests. The paper’s own results show that many workers do not value flexibility per se; they mainly value avoiding employer-controlled nonstandard hours and, to a lesser extent, working from home. So one must be careful not to collapse all “alternative work arrangements” into one object. 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing if your JMP needs to argue that jobs are multidimensional and that nonwage job characteristics matter empirically, but in highly asymmetric and heterogeneous ways. It is also useful as a critique of naive hedonic-wage inference. 

## possible use for model design

It is useful for model design because it suggests treating jobs as bundles of wage and nonwage attributes, not merely as wage-hour combinations. That is directly relevant if your job-choice framework will include schedule control, remote work, predictability, or weekend work as job characteristics. [reasonable inference for my project] supported by 

## possible use for identification

This is one of the paper’s strongest uses. It provides a clean identification design for willingness-to-pay over job amenities through randomized wage-attribute trade-offs. The treatment of inattention is especially instructive methodologically. 

## possible use for welfare measurement

Indirectly useful. The paper does not build a welfare measure, but it provides monetized valuations of specific work arrangements that could feed into equivalent-income or compensating-differential style welfare objects. [reasonable inference for my project] supported by 

## possible use for decomposition

Limited directly. The paper does not decompose inequality or welfare into opportunities, preferences, and pay components. It does decompose workers’ valuation of “bad schedules” into aversion to evening/weekend work versus unpredictability, which is a useful attribute decomposition. 

## possible use for comparative application

Potentially useful. The design could be replicated across countries, occupations, or institutional settings to compare valuations of the same job attributes across environments. The paper itself does not do this, but it provides a strong template. [reasonable inference for my project] supported by 

# Research questions this paper inspires

Can a RURO-style job-choice model incorporate experimentally estimated willingness-to-pay for schedule attributes as revealed preference restrictions on job utility?

How would the valuation of work arrangements change once one conditions on actual feasible job sets rather than experimentally presented alternatives?

Can one define a well-being measure (W(z,R,A;y)) in which (z) includes nonwage job attributes such as predictability, remote work, and schedule control, rather than only income and hours?

Are cross-group differences in observed job arrangements driven more by differences in valuations or by differences in access to jobs with particular arrangements?

Can the experimental valuation approach be combined with structural estimation of job availability to separate the welfare effects of preferences from those of constrained opportunities?

# Challenge to this paper

The main challenge is that the paper is excellent at measuring valuations conditional on presentation of alternatives, but it leaves unresolved the deeper market-structure question of why many workers who strongly dislike certain arrangements nonetheless remain in such jobs. The authors mention sorting frictions and employer costs, but do not identify them. For a project interested in opportunities, this missing link between valuation and access is central. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper treats jobs as bundles of wages and work-arrangement attributes and estimates willingness to pay for these attributes through experimentally varied job choices. It thereby provides direct evidence that workers value nonwage job characteristics and that these valuations are heterogeneous. 

[reasonable inference for my project] In your notation, the realized bundle (z) could naturally be extended to include not just consumption and labor time but also schedule predictability, work-from-home option, and employer discretion. This paper is valuable precisely because it gives empirical support for thinking that such attributes matter substantively for job valuation. 

[unclear from paper] The paper does not separately model (R), (A), and (y). It estimates valuations over experimentally presented jobs, but it does not tell us whether workers with high WTP for certain arrangements actually have access to them, nor how feasible job sets differ across individuals. It also does not specify how wage schedules over jobs should be represented in a structural model. 

[reasonable inference for my project] In your taxonomy, this paper is closest to the pay-schedule/job-attributes side and to preference heterogeneity over jobs. It is not naturally a paper about independence of (A), reference opportunity sets, or responsibility for opportunities. Its main contribution is to enrich the positive description of jobs that a later opportunity-sensitive welfare framework might build upon. 

# Relation to Bargain et al. (2013)

[not central]

# Relation to opportunities vs preferences

This paper is primarily about preferences over job attributes, not about opportunities. It estimates how much workers value or dislike particular work arrangements when those arrangements are made available in the experimental choice set. 

Its relevance for the opportunities-versus-preferences distinction is therefore indirect but still important. It shows that one cannot infer from observed job choices alone that workers are indifferent to arrangements such as employer discretion or work-from-home options. A worker may be in a bad arrangement not because of preference but because of access constraints or employer costs. That inference goes beyond what the paper explicitly proves, but it is strongly suggested by the gap between measured valuations and observed prevalence. [reasonable inference for my project] supported by 

# Useful quotations / formulas

The key choice condition is:
[
P_{\Delta w}\equiv \Pr(WTP_i > -\Delta w).
]
This is the basic revealed-choice inequality linking wage trade-offs to willingness to pay. 

The main mixture choice probability with inattention is:
[
\Pr(A_i=1\mid \Delta w)=F(b\Delta w+c;\mu,\sigma)(1-2\alpha)+\alpha.
]
This is the central econometric equation because it jointly models latent WTP and inattentive misclassification. 

Table 5 is especially useful. It reports mean WTP of $0.48 for flexible scheduling, (-$0.22) for flexible number of hours, $1.33 for work from home, $1.17 for combined flexibility, and $3.41 to avoid employer discretion. These are the paper’s core quantitative results. 

# Suggested tags

job-amenities, alternative-work-arrangements, work-from-home, schedule-predictability, employer-discretion, discrete-choice-experiment, willingness-to-pay, compensating-differentials, labor-market-frictions

# My quick takeaway

This is a very useful paper for the empirical microeconomics of job attributes. Its main value for your corpus is that it measures willingness to pay for concrete work arrangements in a way that is cleaner than standard hedonic methods and more realistic than generic surveys. For your project, it is especially valuable as evidence that jobs are multidimensional objects and that workers care strongly about some nonwage attributes, especially remote work and avoidance of employer-controlled irregular schedules. Its main limitation is that it measures valuation much better than access, so it does not yet solve the opportunities side of your framework.
