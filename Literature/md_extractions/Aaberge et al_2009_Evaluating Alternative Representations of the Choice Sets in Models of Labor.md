# doi: 10.1111/j.1467-6419.2008.00573.x

## EVALUATING ALTERNATIVE

## REPRESENTATIONS OF THE CHOICE SETS

## IN MODELS OF LABOR SUPPLY

R. Aaberge

Research Department, Statistics Norway

U. Colombino

Department of Economics, University of Turin

T. Wennemo

Research Department, Statistics Norway Abstract. During the last two decades, the discrete choice modeling of labor supply decisions has become increasingly popular. Within the literature adopting this approach, however, there are two potentially important issues that so far have not been given the attention they might deserve. A first issue concerns the procedure by which the discrete alternatives are selected to enter the choice set.

Most authors choose (not probabilistically) a set of fixed points identical for every individual. Some authors adopt instead a sampling procedure and also assume that the choice set may differ across households. A second issue concerns the availability of the alternatives. Most authors assume all the values of hours of work within some range are equally available. At the other extreme, some authors assume only two or three alternatives (for example, nonparticipation, part-time and full-time) are available for everyone. Some studies account instead for the fact that not all the hour opportunities are equally available to everyone specifying a probability density function of opportunities for each individual. In this paper we explore by simulation the implications of (i) the procedure used to build the choice set (fixed alternatives versus sampled alternatives); (ii) accounting or not accounting for a different availability of alternatives. The results of the evaluation performed in this paper show that the way the choice set is represented has little impact on the fitting of observed values, but a more significant and important impact on the out-of-sample prediction performance. Thus, the treatment of the choice sets might have a crucial effect on the result of policy evaluations.

Keywords. Choice set specification; Discrete choice models; Labor supply;

Prediction performance; Random utility models 1. Introduction The idea of modeling labor supply decisions as discrete choices has become more and more popular during the last two decades. In this paper we examine, through Street, Malden, MA 02148, USA.

587 a simulation exercise, an issue that has received much less attention than it might deserve: the implications of alternative methods of representing the choice set within the discrete choice approach. The discrete choice approach has gained a prominent position as the outcome of a process aimed at solving or circumventing some theoretical and computational problems to be faced in micro-econometric research when analyzing choices subject to complicated constraints. The beginning of this process might be traced back to the late 1960s and early 1970s, when a strong interest emerged in designing and evaluating various welfare and ‘anti-poverty’ programs. These policies introduce complications (nonlinearities, nonconvexities) into the budget sets faced by the target population, which are hard to deal with within the standard framework based on demand (or supply) functions. Perhaps Heckman (1974) represents the first contribution that fully clarifies the issue. The policy problem addressed is the evaluation of a child-related welfare policy that introduces significant complications in the budget set. Heckman observed that to make such evaluation one has to estimate the preferences as separated from the constraints: ‘The essence of the problem involves utility comparisons between two or more discrete alternatives. Such comparisons inherently require information about consumer preferences in a way not easily obtained from ordinary labor-supply functions’ (Heckman, 1974, p. S136). Moreover ‘... the ability to make... [the separation between preferences and constraints]... is less important if we are willing to make the conventional assumption that wage rates are independent of hours of work... but becomes quite important when we acknowledge the existence of progressive taxation, welfare regulations, and time and money costs of work’ (Heckman, 1974, p. S142). In that paper, Heckman proposed a particular method of identifying indifference curves as envelopes of tangents. In the same period, Hausman and various coauthors addressed essentially the same problem and proposed a method specifically appropriate for piece-wise linear budget constraints (for example, Hausman, 1979). These contributions work through the implications of the Kuhn–Tucker conditions associated with the maximization of utility subject to inequality constraints. The solution can be located in different ranges of values along the budget constraint. Corresponding to each possible range of values there is a condition involving the preference parameters. Choosing a convenient stochastic specification, we can express the probability that those various conditions alternatively hold, write down the sample likelihood and estimate the preference parameters. Useful presentations of this class of methods have been provided by Moffitt (1986), Blomquist (1988) and Blundell and MaCurdy (1999). The method proposed by Heckman as well as the method proposed by Hausman and co-authors are in principle fairly general but might in practice turn out to be not so easily applicable to problems that are more complicated than those for which they were originally exemplified. More specifically, as far as the Hausman and co-authors’ approach is concerned, experience suggests that the method presents three main problems. First, it works well with convex budget sets (for example, those generated by progressive taxation) and a two-good application (for example, leisure and income in the individual labor supply model) but it tends to become

## EVALUATING ALTERNATIVE REPRESENTATIONS OF THE CHOICE SETS

computationally cumbersome when the decision makers face nonconvex budget sets and when there are more than two goods (for example, in the case of a many-person household). Second, in view of the computational problems, the above approach essentially forces the researcher to choose relatively simple specifications for the utility function or the labor supply functions. Third, computational and statistical consistency of maximum likelihood estimation of the model requires imposing a priori quasi-concavity of the utility function (for example, see MaCurdy et al., 1990). As a response to the problems mentioned above, researchers have since the early 1980s made use of another innovative research effort which matured in the first half of the 1970s, i.e. the random utility maximization (RUM) model developed by McFadden (1974, 1981). It is not often realized in the literature that the advantages of this approach (as we will explain more precisely in Section 2.1) are due to the representation of choice as the maximization of a random utility, rather than to the discreteness of the choice set. In practice, however, the most common implementation of the approach involves a discrete representation of the choice set. As far as the labor supply application is concerned, this approach essentially consists in representing the budget set with a set of discrete alternatives or jobs. The choice of the optimal alternative is modeled in terms of a comparison between utility level and not in terms of conditions involving marginal utilities. Allowing the utility function to be stochastic and using a convenient specification for the stochastic component (i.e. the extreme value distribution) leads to an easy and intuitive expression for the probability that any particular point is chosen (i.e. the multinomial logit model). This approach is very convenient when compared to the previous ones, since it does not require going through complicated Kuhn–Tucker conditions involving derivatives of the utility function and of the budget constraints. As a consequence it is not affected by the complexity of the rule that defines the budget set or by how many goods are contained in the utility function. Equally important, the deterministic part of the utility function can be specified in a very flexible way without worrying about the computational problems. During the last two decades, this approach has become increasingly popular in the labor supply literature, starting with Aaberge et al. (1995) and van Soest (1995). Within the literature adopting this approach there are, however, two issues which have not been given the attention we think they deserve. A first issue concerns the procedure by which the discrete alternatives are included in the choice set. Most authors (for example, among others, van Soest, 1995; Duncan and Weeks, 1997; Blundell et al., 2000; Kornstad and Thoresen, 2004) choose (not probabilistically) a set of fixed points which is identical for each individual. 1 By contrast, Aaberge et al. (1995, 1999) adopt a sampling procedure originally proposed by McFadden (1978). A second issue concerns the availability of the alternatives. Letting H represent the maximum number of hours in the reference period, most authors assume that all the values in [0, H] – or in some discrete subset – are equally available. At the other extreme, some authors (for example, Zabalza et al., 1980) assume only two or three alternatives (for example, nonparticipation, part-time, and full-time) are available for everyone. Aaberge et al. (1995, 1999, 2000a, b, 2004) assume instead that all the hour opportunities in [0, H] are in principle available but not equally accessible for everyone. More specifically, they assume that there is a probability density function of opportunities for each individual. The discrete choice set used in the estimation (and subsequently in the simulations) is built by sampling from that individual-specific density function. Section 2 explains in more detail the implications of alternative procedures used to generate the choice set and defines the different types of models that can be estimated accordingly. Sections 3, 4 and 5 present the simulation exercises. We use a previously estimated model of female labor supply as the ‘true’ model. The model (described in Section 3) is characterized by heterogeneous availability of alternatives (across different hour values and among different individuals). From the ‘population’ described by the ‘true’ model we generate 30 samples for a Monte Carlo exercise. In Section 4, we use the data from these samples to estimate – and compare the prediction performance of – various models that adopt the same specification of preferences as in the ‘true’ model but differ in the way the choice set is represented (sampled versus fixed alternatives, number of alternatives, heterogeneous versus uniform availability of alternatives). In Section 5, we perform a second simulation exercise where we focus more deeply on the systematic impact of different specifications of the choice set upon the in-sample and out-of-sample prediction error. Section 6 contains the conclusions.

2. Alternative Representations of the Choice Sets In this section, after recalling the basic discrete choice version of the labor supply model, we survey the crucial problems to be faced in specifying the choice set, i.e. the selection of the alternatives and the representation of different availability of alternatives.

## 2.1 The Basic RUM Model of Labor Supply

The individuals maximize their utility by choosing from opportunities defined by hours of work and other unobserved (by the analyst) attributes. The utility is assumed to be of the form U (f (wh, I ), h, j) = v(f (wh, I ), h) + ε(j) (1) where w is the wage rate, h is hours of work, I is exogenous income, f is a tax-transfer function that transforms gross income into net income, j is a variable that captures other job and/or individual characteristics, and ε is a random variable. Commuting time or required skill are possible examples of the characteristics captured by j. The model as specified in (1) belongs to the class of the RUM models (see, for example, McFadden, 1981). Let B = [0, H] be the range of possible values for hours of work h and let p(h) be the probability density function of jobs with hours equal to h. The most common distribution to assume for the

## EVALUATING ALTERNATIVE REPRESENTATIONS OF THE CHOICE SETS

random term ε is the type I extreme value. 2 If the range of values of h is continuous, the stochastic assumption leads to the (continuous) multinomial logit expression for the probability that a job with h hours is chosen: 3 exp(v(f (wh, I ), h)) p(h) ϕ(h) ≡ Pr U (f (wh, I ), h) = max U (f (wx, I ), x) = x∈B exp(v(f (wx, I ), x)) p(x) dx (2) Based on (2), the corresponding likelihood function can then be computed and maximized to estimate the parameters of the utility function. The crucial advantage of this approach is that the characterization of the utility maximization problem (i.e. expression (1)) is not affected by the specification of v nor of f. In other words, one can choose relatively general and complicated specifications for v and/or accounting for complex tax-transfer rules f without affecting the characterization of behavior and without significantly affecting the computational burden involved by the estimation or simulation of the model. Expression (2) is a simplified version of the model developed by Dagsvik (1994) and by Aaberge et al. (1999). It is also close to the continuous spatial model developed by BenAkiva and Watanatada (1981). We have chosen to start with the continuous version of the multinomial logit model to highlight the fact that the advantages of the approach are due not so much to a discrete representation of the choice set but to the specification of utility as a random variable. Although in principle the model could be directly managed in the form expressed by (2), in practice, for ease of interpretation, a discrete representation is usually preferred. Clearly the researcher might think that the choice set, at least as it is perceived by the household, is in essence discrete; but even a genuinely continuous range of values can always be represented (to any desirable degree of approximation) by a set of discrete values. The probability that a job with hours equal to h is chosen can therefore be written as follows:

exp(v(f (wh, I ), h)) p(h) ϕ(h) = (3) x∈B exp(v(f (wx, I ), x)) p(x) A further common simplification (mostly implicit in the literature on labor supply) is assuming that all the values in B are equally frequent (or dense), i.e. p(h) = a (constant) for all h. With this assumption we get ϕ(h) = exp(v(f (wh, I ), h)) x∈B exp(v(f (wx, I ), x)) (4)

## 2.2 Selection of Alternatives

As we have already mentioned in Section 1, the first issue in choice set representation concerns the procedure used to select the alternatives. In many applications, including labor supply modeling, the choice set contains a very large (or even infinite) number of alternatives. For instance, if we model labor supply of couples and the decision period is the year, considering 1-hour intervals and This would imply a very heavy computational burden, since for each alternative we must compute the couple’s budget by applying a possibly complicated tax rule. More in general, if the alternatives are characterized by K attributes and the kth

## K

Q k alternatives.

attribute can take Q k different values, the choice set contains k=1 Thus it is convenient to work with a smaller choice set somehow representative of the true one. Ben-Akiva and Lerman (1985) present a detailed treatment based on either aggregating alternatives or sampling alternatives when the number of alternatives contained in the choice set is very large (or even infinite) so that a complete enumeration is computationally too costly. For simplicity, we will in this section refer to the representation expressed by (4), where the assumption is that all the alternative values of h are equally available (i.e. equally frequent in the choice set). The issue of a nonuniform availability of alternatives will be addressed in Section 2.3.

## 2.2.1 Aggregating Alternatives

The procedure consisting in selecting a fixed number of hours values can be interpreted as an aggregation procedure. Instead of using all the possible values between 0 and H, the [0, H] range is divided into sub-intervals and then the mid (or maybe the average) value of h in each interval is chosen to ‘represent’ all the values of that interval. The authors adopting this procedure realize that it introduces measurement errors, but tend to assume they are of minor importance.

For example, van Soest (1995) reports that some experiments with a different number of points did not show significant differences in parameter estimates.

However, a systematic investigation of the implication of that procedure has never been done either theoretically or empirically.

If one interprets the approximation of the choice sets as an aggregation procedure, the analysis provided by Ben-Akiva and Lerman (1985) can be applied to clarify the issue. The interval [0, H] is divided into L sub-intervals. We will assume the average of h in each sub-interval is chosen as representative (instead of the more common procedure of choosing the mid-point: of course the two are very close and in fact coincide if the values of h are continuous or if each interval contains an uneven number of values). Using the terminology introduced in Section 2.1, let v̄ ≡ (1/N) h∈B v(f (wh, I ), h) = average systematic utility in sub-interval, where B is the set of values of hours contained in sub-interval and N is the number of elements contained in B. Ben-Akiva and Lerman (1985) show that the expected maximum utility attained on sub-interval is v = v̄ + ln(N) + ln(D) (5) where D ≡ j exp(v j − v̄ )1/N. This last term is a measure of dispersion of v in sub-interval.

## EVALUATING ALTERNATIVE REPRESENTATIONS OF THE CHOICE SETS

Accordingly, the probability that a value of h belonging to sub-interval is chosen is exp(v̄ + ln(N) + ln(D )) ϕ() = L i i i i=1 exp(v̄ + ln(N) + ln(D )) (6) To compare this with the expression used in the fixed-alternatives approach it is useful to Taylor-expand v j up to second-order terms to get exp(v(f (w h̄, I ), h̄) + 0.5σ hh v hh + ln(N) + ln(D )) ϕ() ≈ L i i i i i i i=1 exp(v(f (w h̄, I ), h̄) + 0.5σ hh v hh + ln(N) + ln(D )) (7) where h̄ i is the average of h in sub-interval i, σ ihh is the variance of h in sub-interval i and v ihh is the second (total) derivative of v(f (w h̄ i, I ), h̄ i) evaluated at h = h̄ i. It would be pointless to use expression (7) for estimation since it requires the very same computations that one wishes to avoid by aggregating alternatives. However, expression (7) is useful to understand the type and the extent of the errors we incur by using various approximations. The expression typically used in the literature is exp(v(f (w h̄, I ), h̄ )) ϕ() ≈ L i i i=1 exp(v(f (w h̄, I ), h̄ )) (8) In expression (8) all the terms 0.5σ hh v hh + ln(N) + ln(D) appearing in (7) are dropped. If these terms were equal across all the sub-intervals they would cancel out from (7) and (8) would be exact. In general, however, they will not be equal, and dropping them will lead to biased estimates. Nonetheless there are ways by which we could improve upon (8) when adopting aggregation as an approximation strategy; ways which, however, have never been considered in the literature on labor supply modeling. (1) The dimension of N i of the sub-intervals – when not equal for all of them – is typically known and can be explicitly accounted for. (2) σ ihh can also be computed. (3) Depending on the functional form used for the utility function, the term v ihh might be explicitly evaluated and accounted for. (4) The terms ln(D i) in general will vary both across sub-intervals and across individuals; however, we might capture at least some of their effects by introducing a set of dummies (as many as the number of sub-intervals – 1). Summing up, the aggregation of alternatives implies biased estimates. The bias could be moderated by using various possible corrections suggested by expression (7). However, it must be said that the literature on labor supply so far has treated this issue in a rather superficial way (as compared, for instance, to the literature on transportation or on location choices). Sampling of alternatives, on the other hand, offers the possibility of working with a relatively small choice set and at the same time preserving the consistency of the estimates. The basic results are established by McFadden (1978). Ben-Akiva and Lerman (1985) also provide a very useful and more practically oriented survey, together with some additional theoretical results. Let us represent the true choice set B with a sample S containing a subset of the alternatives contained in B, where one alternative is the chosen (observed) point and the others are sampled from a probability density function q(h). It can be shown (McFadden, 1978; Ben Akiva and Lerman, 1985) that consistent estimates of v(f (wh, I ), h) can still be obtained when the true choice set B is replaced by S and the probability of observing choice h is evaluated as follows:

exp(v(f (wh, I ), h) − ln(q(h))) ϕ(h | S) = (9) x∈S exp(v(f (wx, I ), x) − ln(q(x))) If a simple random sampling is adopted, all the qs are equal and cancel out. Typically more sophisticated sampling procedures are used since they are expected to be more efficient. For instance, a common procedure consists of using as sampling probabilities the observed relative frequencies of choice possibly differentiated according to personal characteristics of the decision units. Besides Ben-Akiva and Lerman (1985), Train et al. (1987) and Colombino (1998) present a very detailed application of this procedure.

## 2.3 Availability of Alternatives

A second and possibly even more substantial issue is whether account is taken of the different availability of job types on the market. Some authors have made the extreme choice of assuming that the choice set contains only two or three alternatives (for example, nonparticipation, part-time, and full-time). More common, however, is the approach of choosing a few equally spaced points in the interval [0, H], without taking into account the possibility that some type of opportunities might be more easily available than others. Other authors (Aaberge et al., 1995, 1999, 2004) do account for this possibility as well as for the relative density of jobs as a function of personal characteristics. This implies using (3) instead of (4) as the choice probability. In practice, based on a convenient specification of the probability density function p(h) the procedure boils down to ‘augmenting’ the term v with a set of appropriately defined dummy variables. van Soest (1995) introduces similar dummies and interprets them as reflecting costs or benefits and search costs attached to specific ranges of hours values. 4 3. The Simulation Exercise In the following sections, we illustrate the results of two simulation exercises. The first one is a Monte Carlo simulation and consists of three steps. First, we use

## EVALUATING ALTERNATIVE REPRESENTATIONS OF THE CHOICE SETS

a previously estimated model of married women’s labor supply (the ‘true’ model illustrated in Section 3.1) to draw 30 samples, each with 1842 observations. In other words, the parameters of the ‘true’ model are treated as the population parameters. The samples are generated by drawing 30 values of the random component (type I – extreme value distributed) of the utility function for each individual in the original estimation sample (1842 observations). Correspondingly we compute 30 optimal choices for each individual. As a result we obtain 30 samples of 1842 observations. Second, various specific models adopting different representations of the choice set (the details are given in Section 3.2) are estimated on the 30 samples. Thus, for each type of model we obtain a set of 30 estimates. Third, we evaluate the performance of the different models by comparing the models’ predictions with the values – as predicted by the ‘true’ model – of income, participation and hours of work. The evaluation of the prediction performance is made in-sample as well as outof-sample. The in-sample evaluation consists in comparing the values predicted by the ‘true’ model to the values predicted by each alternative model. In the outof-sample exercise we first use the ‘true’ model to simulate the effects of a tax reform (a revenue-constant flat tax); next, we compare the simulated ‘true’ values to those obtained by simulating the various alternative models under the same tax reform. We report the mean and the standard deviation (computed on the 30-sample distribution) of the prediction errors. Since it turns out that the performance of the models differs only in the mean of the prediction error but not in the standard deviation of the prediction error, in the second simulation exercise we focus on the mean prediction error and on its relationship with the characteristics of the different alternative models. In this second exercise we simulate the drawing of a large sample from the population (again defined by the parameters of the ‘true’ model). We use a large sample to minimize the ‘noise’ due to sampling variations and focus on the systematic differences between the models. The sample is formed by drawing six values of the random component (type I – extreme value distributed) of the utility function for each individual in the original estimation sample (1842 observations). Correspondingly we compute six optimal choices for each individual. As a result we get a large sample of 6 × 1842 = 11,052 observations. The different types of models are then estimated on this large sample. For each model we compute an index of prediction performance and then regress the index on a set of variables measuring the different characteristics of the model to identify the contribution of the different characteristics to the prediction performance.

## 3.1 The ‘True’ Model

The ‘true’ model is defined as in expressions (1) and (2) and empirically specified along the lines adopted in Aaberge et al. (1995) as well as in several successive papers. 5 We model the choice of married/cohabitating females, and maintain other household members’ behavior as exogenous. The systematic part of the utility function is specified as follows:

f (wh, I) α 1 − 1 + (α 4 + α 5 log A + α 6 (log A) 2 v(f (wh, I ), h) = α 2 α 1 α 3

## L − 1

+ α 7 C 1 + α 8 C 2 + α 9 C 3) (10) α 3 where L is a measure of leisure, defined as L = 1 − (h/0.8736), h is yearly hours of work, A is age and C 1, C 2 and C 3 are number of children below 3, between 3 and 6, and between 7 and 14 years old. We specify the density of opportunities requiring h hours of work as p (h) = p 0 g(h) if h > 0 1 − p 0 if h = 0 (11) where p 0 is the proportion of market opportunities in the opportunity set, and g is the density of hours conditional upon the opportunity being a market job (i.e. h > 0). Offered hours are assumed to be uniformly distributed except for possible peaks at half-time (corresponding to 18–20 weekly hours) and full-time (corresponding 37–40 weekly hours). Thus, g is given by ⎧ γ if h ∈ (52, 910] ⎪ ⎪ ⎪ ⎪ if h ∈ (910, 1066] ⎪ ⎨ γ exp(π 1) if h ∈ (1066, 1898] g(h) = γ (12) ⎪ ⎪ ⎪ γ exp (π 2) if h ∈ (1898, 2106] ⎪ ⎪ ⎩ γ if h ∈ (2106, 3640] where H is the maximum observed value of h. Thus, this opportunity density for offered hours implies that it is more likely to find jobs with hours that accord with full-time and standard part-time positions than jobs with other working loads. 6 Based on (11) and (10) and using the definitions p 0 = exp(θ 0) (13) 1 − p 0 d 0 (h) = 1 d 1 (h) = 1 d 2 (h) = 1 if if if h > 0; 0 otherwise h ∈ [910, 1066]; 0 otherwise h ∈ [1898, 2106]; 0 otherwise the probability that an opportunity with h hours of work is chosen (i.e. expression (2)) can be rewritten as follows:

exp(v(f (wh, I ), h) + θ 0 d 0 (h) + π 1 d 1 (h) + π 2 d 2 (h)) (14) ϕ(h) = exp(v(f (wx, I ), x) + θ 0 d 0 (x) + π 1 d 1 (x) + π 2 d 2 (x)) dx We refer to π 1, π 2 and θ 0 as the parameters of the opportunity density. In what follows we will refer to d 0 as the ‘job’ dummy, since it captures the relative frequency of market opportunities to nonmarket opportunities; we will refer to d 1

## EVALUATING ALTERNATIVE REPRESENTATIONS OF THE CHOICE SETS

and d 2 as the ‘peaks’ dummies, since they are meant to capture the ‘peaks’ in the density of hours corresponding to part-time and full-time jobs. The parameters of the utility function (10) and the parameters of the job opportunity density defined by (11) and (12) are estimated by maximum likelihood. The continuous choice set is approximated by a discrete choice set S containing the chosen value of h plus 999 values sampled from the empirical probability density function q(h). Then, using one of the procedures explained in McFadden (1978) and Ben Akiva and Lerman (1985), consistent estimates of the parameters can be obtained by using the following expression for the individual contribution to the likelihood function:

exp(v(f (wh, I ), h) + θ 0 d 0 (h) + π 1 d 1 (h) + π 2 d 2 (h) − ln(q(h))) ϕ(h | S) = x∈S exp(v(f (wx, I ), x) + θ 0 d 0 (x) + π 1 d 1 (x) + π 2 d 2 (x) − ln(q(x))) (15) The estimation of the model is based on data for 1842 married/cohabitating females from the 1995 Norwegian Survey of Level of Living. We have restricted the ages of the females to be between 20 and 62 years to minimize the inclusion in the sample of individuals who in principle are eligible for retirement, since analysis of retirement decisions is beyond the scope of this study. Although the model adopted was originally developed for analyzing simultaneous household partners’ behavior, we focus here on women’s behavior to simplify the execution and the interpretation of the simulation exercise. Moreover, the majority of labor supply studies have primarily focused on married/cohabitating females, where husband’s income as well as the couple’s nonlabor income are treated as exogenous and included in disposable income f (wh, I ). 7 The estimates are presented in Table A1 of Appendix A.

## 3.2 Alternative Models

In what follows we use the sample generated according to the true model to estimate various versions of models generated according to the various possible representations of the choice set as discussed in Section 2.

The more general versions of the models are (15) when sampled alternatives are used, and ϕ(h | R) = exp(v(f (wh, I ), h) + θ 0 d 0 (h) + π 1 d 1 (h) + π 2 d 2 (h)) x∈R exp(v(f (wx, I ), x) + θ 0 d 0 (x) + π 1 d 1 (x) + π 2 d 2 (x)) (16) when fixed alternatives are used. R denotes the choice set built as a set of fixed alternatives. The dummies d 0 and (d 1, d 2) are defined as in (13). Dropping the job dummy d 0 and/or the peaks dummies (d 1, d 2) generates a more restrictive version of the model. The choice sets S and R contain alternatively 6 or 24 points. For the model with fixed alternatives, we choose the mid-values of (6 or 24) equally spaced intervals between 0 and 3640. For the model with sampled alternatives, the choice set contains the observed value of h plus 5 or 23 values sampled from the empirical distribution g (defined by (12)) of offered hours. 596 597

Table 1. Types of Models.

Generation of alternative

Model

Model

Model

Model

Model

Model

Model

Model

Model

Model

Model

Model

Model

Model

Model

Model

Ia

Ib

Ic

Id

IIa

IIb

IIc

IId

IIIa

IIIb

IIIc

IIId

IVa

IVb

IVc

IVd

Number of alternatives

Job dummy

Peaks dummies 6 6 6 6 24 24 24 24 6 6 6 6 24 24 24 24

No

Yes

No

Yes

No

Yes

No

Yes

No

Yes

No

Yes

No

Yes

No

Yes

No

No

Yes

Yes

No

No

Yes

Yes

No

No

Yes

Yes

No

No

Yes

Yes

Fixed

Fixed

Fixed

Fixed

Fixed

Fixed

Fixed

Fixed

Sampled

Sampled

Sampled

Sampled

Sampled

Sampled

Sampled

Sampled Altogether we have 16 models resulting from the combinations of the following possibilities:

(1) (2) (3) (4) alternative generation: fixed or sampled number of alternatives: 6 or 24 job dummy: included or dropped peaks dummies: included or dropped The tables that report the results of the 16 models are labeled as in Table 1. The parameter estimates of the 16 models are reported in the Appendix (Table A2). 8 We are interested in the prediction performance of the models, both in-sample and out-of-sample (prediction of policy effects). Clearly, we expect the more flexible and complex models (i.e. those allowing for a different availability of alternatives) to perform better than simpler or more restrictive models. Also, we know that the models based on sampled alternatives are expected to produce consistent estimates, while those based on fixed alternatives are not. Therefore what in fact we want to explore is how much better the more flexible models perform and how much better the models based on sampled alternatives perform.

4. A Monte Carlo Exercise In this exercise, each model is estimated on the 30 samples obtained as explained in Section 3. For each model and each of the 30 repetitions we predict participation rates, hours of work and disposable income. The predictions are obtained individual

## EVALUATING ALTERNATIVE REPRESENTATIONS OF THE CHOICE SETS

Table 2. Mean and Standard Deviation of the Relative Differences Between Disposable Income in the True Model and Four Different Models Under the 1994 Tax System.

Mean

Std dev.

Model

Ia (%)

Model

IIb (%)

Model

IIIc (%)

Model

IVd (%)

Income decile

Model

Ia (%)

Model

IIb (%)

Model

IIIc (%)

Model

IVd (%) 0.9 −0.4 −0.7 0.3 0.7 0.1 −0.4 −0.4 −0.1 2.0 0.3 1.2 −0.4 −0.9 0.2 0.5 0.0 −0.5 −0.7 −0.7 0.8 0.0 1.5 −0.5 −1.2 0.0 0.3 −0.2 −0.7 −0.7 −0.4 0.9 −0.1 1.2 −0.6 −1.1 0.2 0.6 0.1 −0.4 −0.5 −0.4 0.8 0.0 1 2 3 4 5 6 7 8 9 10

All 1.3 0.9 0.6 0.8 0.8 0.7 0.7 0.5 0.5 0.6 0.3 1.3 1.0 0.8 0.7 0.7 0.6 0.6 0.5 0.5 0.5 0.4 1.2 0.8 0.7 0.6 0.5 0.5 0.5 0.5 0.6 0.6 0.3 1.2 0.9 0.8 0.6 0.5 0.5 0.4 0.4 0.6 0.6 0.3 by individual, evaluating the utility function – including the random component drawn from the type I extreme value distribution – at each alternative and identifying the selected alternative as the one with the highest utility level. The individual predictions are then aggregated into the 10 means of the 10 income deciles. We define the relative prediction error as follows:

ỹ k js − y j z k js = j = 1,..., 10; k = 1,..., 4; s = 1,..., 30 (17) y j where y j and ỹ k js denote the outcomes in decile j of the true model and alternative model k in sample s, respectively. The outcomes are alternatively defined to be the job participation rate, hours of work and disposable income after tax. The exercise is done twice, once for predicting the current (1994) values (and comparing them with those predicted by the ‘true’ model) and once for predicting the effects of a hypothetical revenue-constant flat tax (and comparing them with those predicted by the ‘true’ model). To simplify the presentation Tables 2–7 report the results only for the four models Ia, IIb, IIIc and IVd. 9 The left part of each table contains the means of the relative prediction error, i.e. z̄ k j = 30 s=1 z k js /30, while the right part contains the standard deviations, i.e.

30 (z − z̄) 2 /30 k js kj s=1

From the tables we observe the following.

Table 3. Mean and Standard Deviation of the Relative Differences Between

Tax System.

Mean

Std dev.

Model

Ia (%)

Model

IIb (%)

Model

IIIc (%)

Model

IVd (%)

Income decile

Model

Ia (%)

Model

IIb (%)

Model

IIIc (%)

Model

IVd (%) −7.7 5.0 −0.3 2.2 −1.3 1.5 1.2 −0.5 0.4 5.7 0.8 0.5 4.6 −3.6 −1.0 −2.2 −0.1 0.0 −2.1 −0.7 0.9 −0.5 19.9 17.8 3.1 2.4 −0.1 1.8 2.1 −0.8 0.6 5.0 4.1 3.5 5.2 −3.1 −1.6 −2.0 0.2 1.0 −2.4 −0.4 2.4 0.0 1 2 3 4 5 6 7 8 9 10

All 6.3 6.4 3.5 2.9 2.2 1.4 1.4 1.4 1.5 2.3 1.0 4.6 6.4 3.8 2.9 1.8 1.9 1.7 1.5 1.3 2.0 0.9 4.6 6.4 3.2 3.1 2.1 1.6 1.3 2.2 0.9 2.7 0.9 4.7 6.7 3.3 3.3 2.4 1.6 1.3 2.2 1.0 2.5 0.9 Table 4. Mean and Standard Deviation of the Relative Differences Between Hours of Work in the True Model and Four Different Models Under the 1994 Tax System.

Mean

Std dev.

Model

Ia (%)

Model

IIb (%)

Model

IIIc (%)

Model

IVd (%)

Income decile

Model

Ia (%)

Model

IIb (%)

Model

IIIc (%)

Model

IVd (%) 0.0 7.6 4.0 0.6 2.4 −1.1 2.6 1.6 3.0 11.3 3.7 0.0 0.1 −2.7 −2.1 1.2 −3.5 0.3 −1.8 −1.0 3.3 −0.2 0.0 −0.7 −5.4 −4.1 2.2 −3.9 1.1 −2.2 −1.9 6.3 0.0 0.0 −3.4 −5.1 −3.4 4.9 −2.1 2.1 −1.7 −1.0 5.5 0.3 1 2 3 4 5 6 7 8 9 10

All 0.0 8.0 6.0 5.0 4.3 2.9 3.2 2.7 2.3 3.1 1.3 0.0 6.6 6.1 3.9 4.0 3.3 3.1 2.9 2.7 3.0 1.5 0.0 7.4 6.2 5.9 3.5 3.4 2.8 3.3 2.9 3.4 1.2 0.0 7.8 6.8 5.1 3.9 3.5 3.0 3.4 2.9 3.5 1.2 (1) Sampled alternatives models (IIIc and IVd) perform better than fixed alternatives models (Ia and IIb). (2) Predictions tend to be less precise in lower and upper deciles, more notably so with model Ia. This result is in accord with what one would expect because

## EVALUATING ALTERNATIVE REPRESENTATIONS OF THE CHOICE SETS

Table 5. Mean and Standard Deviation of the Relative Differences Between Disposable Income in the True Model and Four Different Models Under a Flat Tax Reform.

Mean

Std dev.

Model

Ia (%)

Model

IIb (%)

Model

IIIc (%)

Model

IVd (%)

Income decile

Model

Ia (%)

Model

IIb (%)

Model

IIIc (%)

Model

IVd (%) −13.2 −12.2 −7.0 −6.8 −4.3 −4.9 −2.0 −4.3 −2.2 0.9 −4.3 −8.4 −8.3 −3.9 −4.4 −1.8 −2.9 −0.3 −3.1 −1.2 0.6 −2.5 −8.8 −7.2 −4.4 −4.5 −2.2 −2.4 −0.4 −3.1 −0.8 1.0 −2.4 −9.0 −7.9 −4.6 −4.7 −2.4 −2.5 −0.4 −3.2 −1.0 0.9 −2.6 1 2 3 4 5 6 7 8 9 10

All 1.9 1.5 1.3 1.1 0.8 0.8 0.8 0.8 0.8 0.6 0.3 2.0 1.6 1.6 1.0 0.8 0.7 1.0 0.7 0.9 0.6 0.4 1.9 1.8 1.5 1.3 0.8 0.9 1.0 1.0 0.9 0.7 0.3 1.9 1.6 1.3 1.2 1.0 0.9 1.0 0.7 0.9 0.8 0.4 Table 6. Mean and Standard Deviation of the Relative Differences Between Participation Rate in the True Model and Four Different Models Under a Flat

Tax Reform.

Mean

Std dev.

Model

Ia (%)

Model

IIb (%)

Model

IIIc (%)

Model

IVd (%)

Income decile

Model

Ia (%)

Model

IIb (%)

Model

IIIc (%)

Model

IVd (%) −14.1 −6.7 −1.5 −0.6 −1.8 −0.2 −0.1 −0.2 0.5 4.9 −1.5 −3.7 −1.8 −1.9 −1.8 −1.5 −0.9 −0.9 −1.5 −0.3 1.0 −1.2 9.4 8.1 3.3 1.4 0.1 0.5 1.4 0.1 1.0 4.6 2.6 −1.5 −1.4 −1.6 −2.3 −1.9 −0.9 0.2 −1.3 0.2 2.4 −0.8 1 2 3 4 5 6 7 8 9 10

All 5.3 5.7 3.4 2.7 2.4 1.3 1.5 1.3 1.3 2.1 1.0 4.4 5.5 3.6 2.7 1.7 1.5 1.7 1.5 1.1 2.0 0.9 3.6 3.8 3.1 2.7 2.0 1.4 1.5 1.9 1.0 2.6 0.7 4.0 5.1 3.2 3.2 2.1 1.6 1.6 2.1 0.9 2.5 0.9 a simplification of a model normally is not costless. A poorer description of the choice set weakens the model’s ability to predict the tails of the distributions. (3) There are no notable differences in the standard deviation of prediction error among the models.

Table 7. Mean and Standard Deviation of the Relative Differences Between Hours of Work in the True Model and Four Different Models Under a Flat Tax Reform.

Mean

Std dev.

Model

Ia (%)

Model

IIb (%)

Model

IIIc (%)

Model

IVd (%)

Income decile

Model

Ia (%)

Model

IIb (%)

Model

IIIc (%)

Model

IVd (%) −18.3 −21.9 −6.5 −9.7 −3.4 −6.2 1.9 −0.6 2.8 10.6 −3.6 −8.2 −15.4 −2.6 −6.7 0.9 −5.1 2.1 −1.6 1.2 4.8 −2.3 −5.3 −13.5 −5.6 −7.6 1.5 −4.8 3.5 −1.6 0.8 8.3 −1.7 −8.5 −16.6 −5.6 −8.3 2.8 −4.2 4.0 −1.2 1.2 7.7 −1.9 1 2 3 4 5 6 7 8 9 10

All 0.6 6.3 5.8 4.4 4.1 2.6 3.4 2.5 2.2 2.9 1.1 13.3 5.4 4.9 3.9 2.9 2.5 3.0 2.9 2.8 3.2 1.1 15.7 5.4 4.5 5.5 3.7 3.2 3.0 3.6 2.7 3.3 1.0 10.7 6.7 6.1 4.9 3.9 3.1 2.7 3.3 2.5 3.5 1.2 5. Choice Set Representation and Prediction Performance: A Systematic Analysis In this section, we evaluate the impact of alternative representations of the choice set on the performance of the models. As explained in Section 3, we use the large sample of 1842 × 6 = 11,052 observations to neglect the effect of sampling variations and focus on the systematic differences among alternative representations of the choice set. First, for each of the 16 models (see Table 1) we predict participation rates, hours of work and disposable income. As with the previous exercise illustrated in Section 4, the predictions are obtained individual by individual, by evaluating the utility function – including the stochastic component drawn from the type I extreme value distribution – at each alternative and identifying the selected alternative as the one with the highest utility level. The individual predictions are then aggregated into the 10 means of the 10 income deciles. We introduce the following summary measure of prediction performance (relative prediction error) z k for model k, 10 (ỹ k j − y j) 2 k = 1, 2..., 16 (18) z k = y j j=1 where y j and ỹ k j denote the outcomes in decile j of the true model and alternative model k, respectively. The outcomes are alternatively defined to be the job participation rate, hours of work and disposable income after tax. We define x 1k = 1 if the choice alternatives are sampled (= 0 if the choice alternatives are fixed), x 2k = 1 if the number of choice alternatives is equal to 24 (= 0 if the number of

## EVALUATING ALTERNATIVE REPRESENTATIONS OF THE CHOICE SETS

alternatives is equal to 6), x 3k = 1 when a job dummy is included (= 0 otherwise) and x 4k = 1 when peaks dummies are included (= 0 otherwise). We then estimate the following regression equation: 10 ln(z k) = α 0 + α 1 x 1k + α 2 x 2k + α 3 x 3k + α 4 x 4k + α 5 (x 1k ∗ x 2k) + α 6 (x 1k ∗ x 3k) + α 7 (x 1k ∗ x 4k) + α 8 (x 2k ∗ x 3k) + α 9 (x 2k ∗ x 4k) + α 10 (x 3k ∗ x 4k) (19) A coefficient with a negative (positive) sign means that the respective variable contributes to a lower (higher) prediction error. Since the most important application of labor supply models is the evaluation of tax and welfare policy reforms, we focus on the prediction performance under alternative tax regimes. More precisely, the steps above are repeated twice, with reference to the prediction of the outcomes under the current tax regime and to the prediction of the outcomes after the introduction of a flat tax. Appendix B (Tables B1–B6) reports, for the true model and for the 16 alternative models, the detailed predictions (by income decile) of participation rates, hours of work and net income, both under the current (1994) tax rule (in-sample predictions) and under the hypothetical flat tax reform (out-of-sample predictions). The results show that the introduction of a flat tax stimulates labor supply, and that the strongest labor supply response comes from females in the lower income deciles. Referring to the true model we find that the participation rates increase from 11% and 10% in the two lowest deciles to 5% in the third decile. For the remaining deciles the rise in participation is rather modest. Changes in hours of work show a similar pattern as for the changes in the participation rates; i.e. the change in hours of work decreases with increasing decile. However, although labor supply of females in the richest deciles are only slightly affected by the flat tax reform these females experience a substantial increase in disposable income, which is actually larger than what can be observed for the lowest deciles. The results of the first prediction performance regression are reported in Table 8. Besides reporting coefficients we also compute 100(exp(α i) − 1), which measures the percentage change in the relative prediction error (i.e. z) when the variable associated with α i changes from 0 to 1. In the notes to Table 8 we also provide the value of z when all the variables are set equal to 0 (which corresponds to model Ia). The estimates suggest that using a sampled alternative procedure and introducing job and peaks dummies contribute to a lower prediction error. However, the only statistically significant characteristic is Job dummy ∗ 24 alternatives. Overall the evidence of an important impact of alternative modes of representing the choice set as far as the replication of current values is concerned is not strong. In the second prediction performance exercise, the models are run after a hypothetical tax reform. A fixed proportional tax (flat tax) replaces the current tax system. The flat tax is determined running the ‘true’ model iteratively until the total tax revenue is the same as under the current system. Next, the ‘true’ outcomes (hours and net disposable income) are compared to the outcomes simulated by 602 −1.444 −0.291 0.638 −0.043 0.159 0.541 −0.890 0.049 −1.736 0.089 −0.111 0.877 −25.3 89.3 −4.23 17.23 71.8 −58.9 5.02 −82.4 9.3 −10.5

Coefficient α −1.606 −0.397 0.400 −0.554 −0.422 0.589 −0.388 −0.118 −1.103 0.239 0.132 0.879

Coefficient α −32.8 49.2 −42.5 −34.4 80.2 −32.2 −11.1 −66.8 27.0 14.1 % change in relative prediction error (z) b

Hours of work −4.153 −0.435 0.440 −0.135 −0.232 0.369 −0.156 0.094 −0.854 0.300 −0.027

Coefficient α 0.823 −35.3 55.3 −12.63 −20.71 44.63 −14.4 9.9 −57.4 35.0 −2.67 % change in relative prediction error (z) c

Net income 603 Notes: Coefficients in bold italics are statistically significant (<10%). a The relative prediction error when all the variables are zero (model Ia) is 0.236. b The relative prediction error when all the variables are zero (model Ia) is 0.201. c The relative prediction error when all the variables are zero (model Ia) is 0.016.

Constant

Sampled alternatives 24 alternatives

Job dummy

Peaks dummy

Sampled alternatives ∗ 24 alternatives

Sampled alternatives ∗ Job dummy

Sampled alternatives ∗ Peaks dummies 24 alternatives ∗ Job dummy 24 alternatives ∗ Peaks dummies

Job dummy ∗ Peaks dummies

## R 2

Variable % change in relative prediction error (z) a

Participation probability Table 8. Estimates of the Prediction Performance Regression Under the Current Tax Regime.

## EVALUATING ALTERNATIVE REPRESENTATIONS OF THE CHOICE SETS

−1.729 −0.524 0.538 0.290 0.189 0.473 −0.716 0.055 −1.394 0.122 −0.178 0.862 −40.8 71.3 33.6 20.8 60.5 −51.3 5.7 −75.2 13.0 −16.3

Coefficient α −1.566 −0.757 −0.358 −0.079 −0.072 0.352 0.120 0.174 0.019 −0.003 0.082 0.996

Coefficient α −83.0 −21.2 −17.6 −26.5 −29.4 10.1 4.1 3.3 −14.6 3.5 % change in relative prediction error (z) b

Hours of work −1.773 –0.238 −0.193 −0.308 −0.348 0.096 0.040 0.032 0.136 0.034 0.291

Coefficient α 0.972 −21.2 −17.6 −26.5 −29.4 10.1 4.1 3.3 14.6 3.5 33.8 % change in relative prediction error (z) c

Net income Note: Coefficients in bold italics are statistically significant (<10%). a The relative prediction error when all the variables are zero (model Ia) is 0.177. b The relative prediction error when all the variables are zero (model Ia) is 0.209. c The relative prediction error when all the variables are zero (model Ia) is 0.170.

Constant

Sampled alternatives 24 alternatives

Job dummy

Peaks dummy

Sampled alternatives ∗ 24 alternatives

Sampled alternatives ∗ Job dummy

Sampled alternatives ∗ Peaks dummies 24 alternatives ∗ Job dummy 24 alternatives ∗ Peaks dummies

Job dummy ∗ Peaks dummies

## R 2

Variable % change in relative prediction error (z) a

Participation probability Table 9. Estimates of the Prediction Performance Regression Under a Flat Tax Reform.

the 16 models and the corresponding values of the z k are computed. When it comes to reform simulations rather than current values replication, the differences in outcomes are more marked. Table 8 is analogous to Table 9, but it refers to post-flat-tax outcomes. In this case we get a much clearer pattern of the effects of the different modeling strategies, in particular on the prediction of hours of work and net income. For example, when all the variables are set equal to 0 (i.e. we use model Ia), hours of work are predicted with a relative error equal to 0.209. If we adopt sampled alternatives instead of fixed alternatives (i.e. we use model IIIa) the relative prediction error is reduced by 83%. As follows from the detailed information provided by Tables B4–B6 the less satisfactory out-ofsample prediction performance arises from discrepancies between the lower parts of the predicted and the ‘observed’ flat tax distributions of hours of work and disposable income.

6. Conclusions We have performed a series of simulation exercises aimed at exploring the performance of different versions of a labor supply model, where different approaches to represent choice sets are used. We first perform a Monte Carlo exercise where we simulate the distribution of the prediction errors of the different types of model. Since the results show that there is no notable difference among models as to the standard deviation of the prediction error distribution, we also perform a second exercise where we focus on the mean of the prediction error distribution and estimate how it is affected by different designs of the choice set representation. In this second exercise the various models are estimated using a large sample generated by a ‘true’ model, to which they can then be compared. The results we have obtained are likely to be application-specific rather than general, yet they produce useful suggestions. It turns out that as far as the replication of the current tax regime outcomes are concerned, there is little statistically significant evidence for important effects of alternative choice set representation procedures. Almost all the models predict well, although there are some indications favoring the sampled alternatives procedure. However, when it comes to predicting the effect of a flat tax reform, the indications are definitely more clear-cut. Using sampled alternatives and accounting for heterogeneity of opportunities seem to significantly reduce the prediction errors. The simulation experiments illustrated in this paper suggest that indeed the issues related to the representation of the choice set in the discrete choice framework are worth a more attentive design than is commonly done in the literature on labor supply. This seems especially relevant in view of using the models for the prediction of policy effects. The prediction performance of current values does not significantly discriminate between different models, but the prediction performance of a post-reform does. These results convey the important message that the ability of a model to replicate observed outcomes is not very informative. Ultimately, the models and the procedures used to develop them should be judged on their

## EVALUATING ALTERNATIVE REPRESENTATIONS OF THE CHOICE SETS

ability to do the job they are built for, i.e. predicting the outcomes of policy changes.

Acknowledgements We would like to acknowledge the Norwegian Research Council (Velferdsprogrammet), the Italian Ministry of University and Research and the Compagnia di San Paolo for financial support. Parts of this paper were written when Rolf Aaberge was visiting ICER in Torino. ICER is gratefully acknowledged for providing financial support and excellent working conditions.

Notes 1. See also Creedy and Kalb (2005) for a survey of alternative approaches to discrete labor supply. 2. A random variable ε has a (standard) type I extreme value distribution if Prob(ε ≤ k) = exp(−exp(−k)). 3. Note that Aaberge et al. (1995, 1999, 2000, 2004) consider B to be the set of market as well non-market opportunities where market opportunities (jobs) are characterized by hours of work as well as by the wage rate and other job attributes. 4. There is still another approach, the so-called Dogit model (Gaudry and Dagenais, 1979), to represent a nonuniform availability of alternatives. It is a generalization of the logit model, where the decision maker may – with a given probability – be ‘captive’ to one of the alternatives or otherwise choose freely from the whole choice set. The Dogit model has been recently used by Harris and Duncan (2002) in a labor supply application. We do not consider the Dogit model in the simulation exercise presented here. 5. See, for example, Aaberge et al. (1999, 2000a, b, 2004) and Aaberge et al. (2000). 6. Since the density values must add up to 1, we can also compute γ according to γ ((910 − 52) + (1066 − 52) exp(π 1) + (1898 − 1066) + (2106 − 1898) exp(π 2) + (3640 − 2106)) = 1 7. For simplicity we presented the model as if the wage rates were given and exogenous. However, as a matter of fact the wages are treated as endogenous and the wage functions are simultaneously estimated by maximum likelihood together with the utility function and the job opportunity density. 8. In the estimation of these models, the actual wage rates are used for the working individuals, while to non-working individuals we impute wages computed on the basis of a wage equation estimated with a two-step Heckman procedure. The estimates of the wage equation are available upon request from the authors. 9. The results for the other models (available upon request from the authors) do not add significant evidence beyond what is revealed by the four models we focus upon. 10. Since z is always positive, a linear specification would not be appropriate. We therefore use ln(z). 606 607

## References

Aaberge, R., Dagsvik, J.K. and Strøm, S. (1995) Labor supply responses and welfare effects of tax reforms. Scandinavian Journal of Economics 97: 635–659.

Aaberge, R., Colombino, U. and Strøm, S. (1999) Labor supply in Italy: an empirical analysis of joint household decisions, with taxes and quantity constraints. Journal of

Applied Econometrics 14: 403–422.

Aaberge, R., Colombino, U. and Strøm, S. (2000a) Labour supply responses and welfare effects from replacing current tax rules by a flat tax: empirical evidence from Italy, Norway and Sweden. Journal of Population Economics 13: 595–621.

Aaberge, R., Colombino, U., Strøm, S. and Wennemo, T. (2000b) Joint labour supply of married couples: efficiency and distributional effects of tax reforms. In L. Mitton, H. Sutherland and M. Weeks (eds), Microsimulation Modelling for Policy Analysis:

Challenges and Innovations. Cambridge: Cambridge University.

Aaberge, R., Colombino, U. and Strøm, S. (2004) Do more equal slices shrink the cake? An empirical investigation of tax-transfer reform proposals in Italy. Journal of

Population Economics 17: 767–785.

Ben-Akiva, M. and Lerman, S.R. (1985) Discrete Choice Analysis. Cambridge, MA: MIT

Press.

Ben-Akiva, M. and Watanatada, T. (1981) Application of a continuous spatial choice logit model. In C.F. Manski and D. McFadden (eds), Structural Analysis of Discrete Data with Econometric Applications. Cambridge, MA: MIT Press.

Blomquist, S. (1988) Non-linear taxes and labor supply. European Economic Review 32:

1213–1226.

Blundell, R. and MaCurdy, T. (1999) Labor supply: a review of alternative approaches.

In O. Ashenfelter and D. Card (eds), Handbook of Labor Economics. Amsterdam:

North-Holland.

Blundell, R., Duncan, A., McRae, J. and Meghir, C. (2000) The labour market impact of the working families’ tax credit. Fiscal Studies 21: 75–100.

Colombino, U. (1998) Evaluating the effects of new telephone tariffs on residential users’ demand and welfare. A model for Italy. Information Economics and Policy 10: 283– 303.

Creedy, J. and Kalb, G. (2005) Discrete hours labour supply modelling: specification, estimation and simulation. Journal of Economic Surveys 19: 697–734.

Dagsvik, J.K. (1994) Discrete and continuous choice, max-stable processes and independence from irrelevant attributes. Econometrica 62: 1179–1205.

Duncan, A. and Weeks, M. (1997) Behavioural tax microsimulation with finite hours choices. European Economic Review 41: 619–626.

Gaudry, M. and Dagenais, M. (1979) The dogit model. Transportation Research 13B:

105–112.

Harris, M.N. and Duncan, A. (2002) Intransigencies in the labour supply choice.

Melbourne Institute Working Paper 17/02.

Hausman, J.A. (1979) The econometrics of labour supply on convex budget sets. Economic

Letters 3: 171–174.

Heckman, J. (1974) Effects of child-care programs on women’s work effort. Journal of

Political Economy 82: 136–163.

Kornstad, T. and Thoresen, T.O. (2004) Means-testing the child benefit. Review of Income and Wealth 50: 29–49.

MaCurdy, T., Green, D. and Paarsch, H. (1990) Assessing empirical approaches for analyzing taxes and labor supply. Journal of Human Resources 25: 415– 449.

McFadden, D. (1974) Conditional logit analysis of qualitative choice behavior. In P.

Zarembka (ed.), Frontiers in Econometrics. New York: Academic Press.

## EVALUATING ALTERNATIVE REPRESENTATIONS OF THE CHOICE SETS

McFadden, D. (1978) Modelling the choice of residential location. In A. Karlquist,

## L. Lundquist, F. Snickard and J.J. Weilbull (eds), Spatial Interaction Theory and

Planning Models. Amsterdam: North-Holland.

McFadden, D. (1981) Structural discrete probability models derived from theories of choice. In C.F. Manski and D. McFadden (eds), Structural Analysis of Discrete Data with Econometric Applications. Cambridge, MA: MIT Press.

Moffitt, R. (1986) The econometrics of piecewise-linear budget constraints: a survey and exposition of the maximum likelihood method. Journal of Business and Economic

Statistics 4: 317–328.

van Soest, A. (1995) Structural models of family labor supply: a discrete choice approach.

Journal of Human Resources 30: 63–88.

Train, K.E., McFadden, D.L. and Ben-Akiva, M. (1987) The demand for local telephone service. Rand Journal of Economics 18: 109–123.

Zabalza, A., Pissarides, C. and Barton, M. (1980) Social security and the choice between full-time work, part-time work and retirement. Journal of Public Economics 14: 245– 276.

## Appendix A

Here we report the parameter estimates of the ‘true’ model and of the 16 alternative models.

Table A1. The ‘True’ Model.

Parameter

Utility function

Consumption

Estimate

Std dev.

α 1 α 2 0.39 4.42 0.11 0.44

Log age

Log age squared

Number of children below 3 years old

Number of children 3–6 years old

Number of children 7–14 years old α 3 α 4 α 5 α 6 α 7 α 8 α 9 −4.57 168.88 −94.29 13.35 0.44 1.23 1.05 0.53 27.47 15.32 2.16 0.23 0.24 0.19

Opportunity density

Job dummy

Part-time dummy

Full-time dummy θ 0 π 1 π 2 −0.60 0.46 1.57 0.10 0.10 0.07

Leisure 608

Model

Ia

Model

IIa

Model

Ib

Model

IIb

Model

Ic

Model

IIc

Model

Id

Model

IId

Model

IIIa

Model

IVa

Model

IIIb

Model

IVb

Model

IIIc

Model

IVc

Model

IIId

Model

IVd 609 α 1 0.39 0.35 0.54 0.43 0.46 0.43 0.50 0.43 0.44 0.54 0.55 0.53 0.54 0.55 0.55 0.52 0.53 α 2 4.42 2.46 3.70 3.97 4.55 4.05 4.64 4.17 4.38 3.96 3.93 4.72 4.64 4.56 4.51 4.70 4.62 α 3 −4.57 −7.53 −3.18 −7.31 −6.72 −2.07 −0.14 −3.99 −4.15 −5.15 −5.27 −5.94 −6.10 −2.40 −2.49 −3.52 −3.60 α 4 168.88

## 54.20 184.85 64.76

## 92.39 232.99 351.30 156.91 171.12 125.90 121.50 112.19 106.31 234.88 231.26 195.26 190.72

α 5 −94.29 −30.46 −102.83 −36.27 −51.64 −128.78 −193.30 −87.38 −95.45 −70.17 −67.75 −62.54 −59.28 −129.94 −128.03 −108.43 −105.95 α 6 13.35 4.32 14.62 5.15 7.33 18.27 27.48 12.40 13.54 9.96 9.62 8.88 8.42 18.46 18.19 15.39 15.04 α 7 0.44 0.13 0.51 0.13 0.19 0.61 0.95 0.38 0.40 0.33 0.30 0.25 0.23 0.66 0.58 0.50 0.44 α 8 1.23 0.48 1.68 0.53 0.76 1.86 2.99 1.25 1.40 1.07 1.05 0.91 0.87 1.94 1.95 1.56 1.57 α 9 1.05 0.40 1.37 0.44 0.62 1.53 2.47 1.04 1.14 0.88 0.88 0.75 0.73 1.61 1.65 1.29 1.33 θ 0 −0.60 – – −1.08 −2.33 – – −0.78 −2.10 – – −0.88 −0.86 – – −0.63 −0.60 π 1 0.46 – – – – −0.23 0.14 0.15 0.28 – – – – 0.44 0.44 0.53 0.52 π 2 1.57 – – – – 0.99 1.53 0.78 1.19 – – – – 1.66 1.63 1.56 1.54

True model Table A2. Estimates of the 16 Alternative Models.

## EVALUATING ALTERNATIVE REPRESENTATIONS OF THE CHOICE SETS

Note that ‘income decile’ in Tables B1–B6 refers to the distribution of disposable income (income after tax) as predicted by the different models under the 1994 tax system.

Table B1. Examples of Predictions of Participation Rates Under the 1994 Tax System.

Income decile 1 2 3 4 5 6 7 8 9 10

Mean

True model

Model

Ia

Model

Id

Model

IIa

Model

IId 58 65 79 86 91 93 93 94 94 88 84 55 73 81 87 92 94 95 94 95 89 86 87 93 95 97 96 98 99 98 99 97 96 87 93 95 97 96 98 99 98 99 97 87 55 67 79 85 90 93 94 93 96 87 84 Table B2. Examples of Predictions of Hours of Work Under the 1994 Tax System.

Income decile

True model

Model

Ia

Model

Id

Model

IIa

Model

IId 1 2 3 4 5 6 7 8 9 10

Mean 568 715 937 1157 1389 1527 1606 1695 1757 1523 1287 627 818 1000 1179 1375 1494 1638 1701 1812 1631 1327 514 730 890 1130 1397 1541 1650 1735 1838 1566 1299 733 837 989 1125 1276 1429 1598 1667 1746 1676 1308 568 708 941 1153 1352 1528 1631 1672 1771 1567 1289 Table B3. Examples of Prediction of Disposable Income (in NOK) Under the 1994

Income decile

True model

Model

Ia

Model

Id

Model

IIa

Model

IId 1 2 3 4 5 6 7 8 9 10

Mean 168915 216080 244914 268880 290441 312088 336247 363833 403513 600841 320575 170648 217801 245504 268308 290083 312113 335829 364607 405063 605283 321524 169098 215357 243740 267340 290556 313719 337305 365453 405654 602163 321038 171945 219415 245176 267880 288798 310410 334374 362513 403401 608705 321262 168690 216333 243672 267659 289893 312446 336148 363739 404046 604516 320714 Table B4. Examples of Predictions of Participation Rates Under a Flat Tax Reform.

Income decile 1 2 3 4 5 6 7 8 9 10

Mean

True model

Model

Ia

Model

Id

Model

IIa

Model

IId

Model

IIIa

Model

IIId

Model

IVa

Model

IVd 69 75 84 89 93 94 94 95 95 88 88 62 77 83 89 93 94 95 94 96 89 87 55 68 76 83 89 92 92 92 94 84 82 89 95 96 97 97 98 99 98 99 97 96 63 74 83 87 91 93 94 93 96 88 86 76 83 90 92 94 95 95 97 98 92 91 65 74 83 88 91 94 93 96 96 88 87 76 84 90 93 94 95 96 97 98 92 91 65 75 83 89 91 94 93 96 96 88 87

## EVALUATING ALTERNATIVE REPRESENTATIONS OF THE CHOICE SETS

Table B5. Examples of Predictions of Hours of Work Under a Flat Tax Reform.

Income decile

True model

Model

Ia

Model

Id

Model

IIa

Model

IId

Model

IIIa

Model

IIId

Model

IVa

Model

IVd 1 2 3 4 5 6 7 8 9 10 987 1022 1160 1315 1491 1609 1659 1742 1794 1549 835 943 1100 1260 1432 1542 1677 1735 1843 1647 826 966 1117 1279 1488 1626 1717 1786 1898 1619 946 1041 1145 1271 1392 1543 1685 1727 1811 1721 890 943 1134 1291 1459 1609 1670 1720 1821 1606 890 943 1134 1291 1459 1609 1670 1720 1821 1606 883 993 1131 1330 1493 1650 1691 1775 1811 1587 921 985 1151 1307 1460 1579 1675 1771 1807 1617 880 992 1133 1338 1485 1646 1695 1774 1814 1586

Mean 1487 1401 1432 1428 1414 1414 1434 Table B6. Examples of Predictions of Net Income Under a Flat Tax Reform.

Income True decile model

Model

Ia

Model

Id

Model

IIa

Model

IId

Model

IIIa

Model

IIId

Model

IVa

Model

IVd 1 2 3 4 5 6 7 8 9 10 194076 234263 259189 279624 301124 323777 350809 383958 431297 651815 171081 214268 242704 266384 289038 314124 342509 375740 426513 649764 177612 220564 250457 272361 294062 320755 349310 379893 431747 651885 173092 222704 247374 271441 293453 319278 346358 378941 430622 657771 177934 220524 248492 271579 294681 319492 344397 377972 428668 652667 175360 221008 248332 272276 293241 318317 346147 377469 430380 651514 178959 223384 249373 275414 296123 321883 348328 379296 430587 650805 175829 220745 247584 273516 293368 318698 346124 378295 429954 652383 178558 222943 249304 275739 295567 321400 348868 378984 431015 650766

Mean 340993 329213 334865 334103 333641 333404 335415 333650 335314 612
