# John K. Dagsvik * and Steinar Strøm **

## Abstract

In this paper we discuss a general framework for analyzing labor supply behavior in the presence of complicated budget-and quantity constraints of which some are unobserved. The point of departure is that an individual’s labor supply decision can be considered as a choice from a set of discrete alternatives (jobs). These jobs are characterized by attributes such as hours of work, sector specific wages and other sector specific aspects of the jobs. We focus in particular on theoretical justification of functional form assumptions and properties of the random components of the model.

The paper includes an empirical application based on Norwegian data, in which the labor supply of married women is estimated.

JEL classification: J22,C51.

Key words: Labor supply, non-convex budget sets, non-pecuniary job-attributes, sector-specific wages.

___________________________________ *

Statistics Norway, Oslo. E-mail: john.dagsvik@ssb.no Department of Economics, University of Oslo. E-mail: steinar.strom@econ.uio.no We are indebted to Tom Wennemo for skillful programming assistance and Rolf Aaberge for constructive critisism throughout the revision process. We thank two anonymous referees and the editor for useful comments and helpful suggestions.We also thank James J. Heckman for valuable comments on an earlier version of the paper and Anne Skoglund for proof reading and word processing. S.Strøm is grateful to

ICER, Turin, for providing excellent working conditions.

** 1. Introduction The purpose of our study is to develop a particular framework for modeling labor supply behavior in the presence of complicated budget sets, qualitative job attributes and restrictions on hours of work, and to apply this framework to analyze data on workers’ observed choice of sector and hours in the labor market. Compared to earlier attempts, our framework for estimating labor supply allows for a more complete empirical strategy in circumstances where job choices are not adequately summarized in hours and wages. Moreover, it provides a consistent and flexible framework for estimating labor supply elasticitiesuncompensated as well as compensatedin the presence of complex budget constraint and random utilities.

In the 1970s and 1980s labor supply studies applied the traditional textbook model for labor supply, extended to allow for convex and smooth tax functions (cf. contributions such as Rosen (1976), Wales and Woodland (1979), Nakamura and Nakamura (1981), Kohlase (1986) and Ransom (1987)). However, in most western countries the tax system and social benefit rules imply a nonconvex budget set. 1 Fixed costs of working and tax deductions if working contribute to these nonconvexities. Attempts to take the non-convexity properties of the tax structure into account include Burtless and Hausman (1978), Blomquist (1983), (1992), Arrufat and Zabalza (1986), Hausman (1980), (1981), (1985), and Hausman and Ruud (1984). In principle it is possible to apply the “Hausman approach” to account for nonlinear and non-convex budget sets. That approach, however, is rather cumbersome when there are more than one adult in the household or when complicated social benefit-and tax deduction rules are present. In contrast, the particular approach advocated in our paper, and which we shall describe in a moment, has the advantage that it becomes simple to handle complicated nonlinear tax and transfer systems. This is also the case for many-persons households.

In the studies mentioned above the mathematical structure of the modeling framework rests upon the assumption that the fundamental choice variables of the household in this context are “consumption” (composite) and “leisure” (hours of work), which can be chosen freely subject to the economic budget constraint. Yet, it seems apparent that hours of work and income are only two out of several job-related attributes which are important for individual behavior in the labor market. “Type of work”, and other “non-pecuniary job attributes”, do often matter a great deal and may even be more important than hours of work. An extreme example of the latter phenomenon is found among scientists, artists and government bureaucrats for whom specific work activities represents major means for self-realization. Another characteristic of the labor market is that hours of work is fixed for many type of jobs. Thus, if an individual wishes to change his workload he would in this case have to change job. 2 This assumption is consistent with the findings of Altonji and Paxson (1988).

In view of the arguments above it may be more appropriate to consider labor supply behavior as the outcome of households choosing from a finite set of job “packages”, each of which are characterized by an offered wage rate, offered hours of work, and non-pecuniary attributes. The individual specific choice sets of job opportunities may be thought of as being determined by employers or in negotiation between employers and unions and they are thus exogenous to the individuals. The qualitative job attributes are often unobservable, or at most only partly observable to the analyst. This is the point of departure taken in this paper. Specifically, the choice environment is assumed to consist of a latent, individual specific set of jobs. A job is characterized by a combination of fixed hours of work, wage rate and non-pecuniary job-attributes (such as type of work and working conditions). The notion of individual specific choice sets is important for our modeling of choice constraints. In our setup there are thus two sources of unobserved heterogeneity, unobserved heterogeneity in tastes and in opportunities.

In Dagsvik (1994) a general framework for modeling this type of settings was developed.

Simplified versions of this framework have been applied by Anderson et al (1988) and Aaberge et al. (1990), (1995) and (1999) to analyze labor supply behavior. In contrast, this paper is more theoretical in that it focuses on a detailed discussion and interpretation of underlying assumptions of the framework in the context of modeling labor supply behavior, and relates the present approach to previous ones. In particular, we discuss how functional form and the probability law of unobservables can be justified from behavioral arguments.

Previous attempts to take (quantity) constraints on the choice set into account have been restricted solely to one job attribute, namely hours of work. Contributions by Ilmakunnas and Pudney (1990), Kapteyn et al. (1990), Dickens and Lundberg (1993), and van Soest (1994) emphasize the inability of standard empirical labor supply models to account for observed peaks in the hours of work distribution at part-time and full-time hours. They have discussed approaches to take account of this type of constraints in the econometric modeling of labor supply. These approaches are, however, different from the one developed in this paper.

Ilmakunnas and Pudney (1990) formulate a labor supply model which is a mixture of logittype models across unobservable choice sets, where the choice sets consist of the alternatives “part time”, “full time” and “non-participation”.

Van Soest (1994) on the contrary, assumes that the choice set consists of a finite (given) number of hours of work options and he specifies a model which is a mixture of logit-type models across unobservable taste-shifters. He interprets the observed concentrations of hours of work as resulting from agents having strong preferences for “full-time” and/or “part-time” hours of work.

Dickens and Lundberg (1993) formulate a model which, similarly to Ilmakunnas and Pudney (1990), is a mixture of discrete choice models across unobservable and finite choice sets. Compared to Ilmakunnas and Pudney the assumptions they make about the choice sets are more general. Specifically, they assume that the number of job offers is generated by a binomial distribution with a fixed maximum (10). Moreover, each job has fixed and unobservable hours of work generated by a discrete distribution with a fixed maximum. Thus, while Ilmakunnas and Pudney, as well as Dickens and Lundberg, assume that the agents face choice constraints which rationalize the observed concentration of hours of work in the data, van Soest assumes that all agents face the same finite choice set. Van Soest thus assumes that the concentration of hours of work at “full-time” and “parttime” follow from preferences.

In all of these recent labor supply contributions the individuals are assumed to have the same wage across jobs. Thus, in previous labor supply studies it is assumed that an individual has a fixed wage rate, and the possibility of job-specific wages are ignored. Recent labor market theories, like the theories of efficient wages and trade unions, suggest that wages may differ across jobs. And more important, wage dispersion among observationally identical workers seems to be a well established empirical fact, see for example Krueger and Summers (1988) and Edin and Zetterberg (1992). In the labor supply literature there are approaches that allow offered job-specific wage rates to vary systematically with hours worked (Moffitt, 1984).

A serious problem with most structural econometric models is the lack of theoretical support for the choice of functional forms and distributional assumptions of the unobservables. In this paper the distributional properties of the agents’ preferences, in the presence of latent choice sets of jobs, follow from an assumption; “Independence from Irrelevant Attributes”, proposed by Dagsvik (1994). This assumption is an extension of the familiar IIA assumption proposed by Luce (1959a). Under this assumption and a particular Poisson process representation of the distribution of the latent choice sets of jobs, the implied distribution of realized hours and wage rates turns out to be analogous to the continuous logit model introduced by Ben-Akiva et al. (1985). IIA is clearly a theoretical axiom which captures the notion of idealized probabilistic rationality in the following sense: Provided the alternatives are “properly” defined, only alternatives in the (current) choice set are relevant for the choice outcome. It is true that IIA is unrealistic in some situations, which it shares with many theoretical assumptions in economics. It should be emphasized that IIA is a theory related to choices made by a single individual or household. To test IIA properly one has to perform test based on stated preference data. If tests are performed on labor market data, joint hypotheses are tested in which the IIA is assumed jointly with assumptions about functional form and the distribution of unobservables. It is well known that IIA may not hold if unobserved heterogeneity is not explicitly accounted for.

An important challenge is to provide a justification for the choice of functional form of the deterministic components in the probability model of realized hours and wage rates. In this respect the attitude among economists seems to be a general resignation: It is believed to be a hopeless task to achieve useful results on a purely theoretical basis, that is from first principles. As a consequence, the functional form problem is “solved” by selecting a convenient mathematical structure and applying data and statistical methods to choose between competing candidates. Unfortunately, without theoretical principles almost any form is a priori possible and the correct one is difficult to determine because of the problem of unobserved variables and measurement errors. What seems to be little known among economists is that there is a tradition within the field of psychophysics to justify functional forms based on invariance principles. These principles are similar to certain invariance principles applied in physics, which typically are invariant under uniform translation and rotation of the coordinate system. In this paper we discuss how results in Falmagne (1985) apply in our context and lead to theoretically justified functional forms.

The empirical part of the paper deals with labor supply among married females in Norway in 1994, who can choose between working in the public and the private sector of the economy. Other authors that analyze agents’ choice of sector are Magnac (1991) and Heckman and Sedlacek (1990). Magnac also allows for rationing in the sense that workers face costs of entry into a sector. However, neither Heckman and Sedlacek nor Magnac consider workers’ choice of hours.

The labor supply model developed here can easily be extended to deal with joint decisions of wife and husband and for the sake of completeness this extension is shown in Appendix A.

This paper is organized as follows. In the next section we present the model which includes a characterization of the stochastic properties of the unobserved variables and the functional form of the deterministic part of the utility function of the agents. In Section 3 we demonstrate how some previous labor supply models follow as a special case from our model. In Section 4 we discuss an empirical application.

2. The modeling framework As alluded to above, the choice environment of a worker is assumed to consist of a set of latent joband non-market opportunities. Each job is characterized by fixed observed attribute variables that describe the contract (wage rate and hours of work) and unobserved attributes that describe the jobtype. We shall first discuss the case where qualitative attributes are latent. Later, we extend the framework to accommodate sector-specific jobs (public sector versus private sector).

2.1. Preferences and choice sets Let U(C,h,z) be the (ordinal) utility function of the household where C denotes household consumption, z indexes the market and non-market opportunities, or job-types, and h is the realized hours of work of the married female. Let positive indices, z = 1, 2 ,..., refer to market opportunities (jobs) and non-positive ones refer to non-market opportunities. To a market opportunity z, there are associated fixed hours of work, H(z), and wage rate, W(z). The opportunity index z in the utility function accommodates the notion that workers may have preferences over job-types (which includes preferences for working in specific sectors of the economy) in addition to income and hours of work. For a given wage rate, w, the economic budget constraint is represented by (2.1)

C = f (hw, I) where I is non-labor income, which includes the income of the husband, and f(⋅) is the function that transforms gross income into after-tax household income. Here, the income of the husband is treated as given. The function f(⋅) will capture all details of the tax and benefit system. The price index for the composite good, C, is set equal to one. Our first assumption concerns the structure of the preferences.

Assumption 1

The utility function has the structure

U(C,h,z) = v (C,h) ε (z) where v(⋅) is a deterministic function and ε(z) is a random taste-shifter.

The random taste-shifter is assumed to account for the unobservable individual characteristics and non-pecuniary job-type attributes that affect utility. For notational simplicity we will use the notation ψ (h, w;I) ≡ v (f (hw, I), h).

(2.2) In addition to (2.1), there are restrictions on the set of feasible market opportunities a specific worker faces because there are job-types for which the worker is not qualified and there may not be jobs available for which he is qualified.

We will next discuss the distribution of the hours and wages associated with market opportunities and the distribution of the associated taste-shifters. The taste-shifters {ε(z)} may vary across opportunities as well as across agents because different agents may value a specific opportunity differently. The non-market opportunities have zero hours of work and zero wage rates. Thus, the agent's opportunity set can be represented by ℘= {(H (z ), W (z ), ε (z)); z = ..., − 2, − 1, 0, 1, 2 ,...}.

Assumption 2 The triples in ℘ are realizations from a non-homogeneous Poisson process on [0,h] × [0, ∞) × (0, ∞), where h is an upper bound on hours of work. The taste-shifters {ε(z)} are distributed independently of {(H(z),W(z))}. Moreover, different agents face different choice sets, which are realizations from independent copies of the Poisson process.

The Poisson process framework offers a very convenient and flexible representation of sets consisting of points that are independently and randomly scattered in some given space. It can be demonstrated that the multidimensional Poisson process follows from a set of postulates, see for [] example Karlin (1966). To describe these postulates, let Ω = 0, h × [0, ∞) × (0, ∞), and let A be a (Borel) set in Ω. Furthermore, let N(A) be the number of triples {(H(z), W(z), ε(z))} within A. The postulates are as follows: (i) The probability P(N(A) = 0), lies between zero and one. (ii) The random variable N(A) has a distribution that depends on A only through the mean number of points, EN(A), within A, with the further property that if EN(A) tends towards zero, then P(N(A)≥1) tends towards zero. (iii) If A 1 and A 2 are disjoint sets in Ω then N(A 1) and N(A 2) are independent. Moreover N(A 1 ∪A 2) = N(A 1) + N(A 2 ). (iv) When EN(A) tends towards zero then P(N(A)≥1)/P(N(A) = 1) tends towards one. The interpretation of these postulates is rather evident. Postulate (ii) asserts that in the homogeneous case N(A) does not depend on the shape of A but only on its "volume". In the nonhomogeneous case N(A) will also depend on the location of A within Ω. Furthermore, the points of the process are isolated points. Postulate (iii) means that the points of the process are independently and randomly scattered in Ω. Postulates (i) and (iv) are rather intuitive and self-explanatory.

The probability law of a Poisson process can be represented by the associated intensity measure, dλ(h,w,ε). This means that the probability that there is a point of the process for which H (z) ∈ (h, h + dh), W (z) ∈ (w, w + dw), ε (z) ∈ (ε, ε + d ε), equals dλ(h,w,ε). Moreover, in a Poisson process the points of the process are independently distributed and the probability that there is more than one point within (h, h + dh) × (w, w + dw) × (ε, ε + d ε) is negligible.

Assumption 3 The intensity measure d λ (h,w, ε) has the structure (2.3)   θ g(h,w) ε − 2 dh dw d ε when h > 0, w > 0, ε > 0, d λ (h,w, ε) =  1   (1 − θ 1) ε − 2 d ε when h = w = 0, ε > 0, where g(h,w) is a probability density on (0,∞)×(0,∞), and θ 1 ∈ (0,1) is a constant.

A justification for the structure (2.3) is given in Dagsvik (1994). There it is demonstrated that under Assumption 2, if the choice among jobs satisfies the IIA property then particular structure on the particular structure of the marginal intensity measure of ε(z), ε -2 dε, in (2.3) follows. Recall that the underlying intuition of the IIA assumption is, loosely speaking, that the agent's ranking of job opportunities from a subset B (say), within the choice set of feasible jobs with the same level of hours of work and wage rate, does not change if the choice set of feasible jobs is altered. Recall also that the stochastic formulation of IIA adopted by the psychologists, means that this property only is claimed to hold on average, for an agent that is exposed to a large number of repeated choice experiments, cf. Thurstone (1927). In Appendix A we demonstrate that IIA in fact seems to be less restrictive than the implications for constrained demand that follow from standard consumer theory. The reason why it is commonly believed that IIA is a very strong assumption is because it is rejected in some empirical tests. Typically, these tests depend crucially on additional ad hoc hypotheses about functional form and parameters that are equal across the sample. Thus, what is typically tested are joint hypotheses about a mixture of functional forms, equal parameters across individuals and IIA. For serious empirical tests of IIA it is therefore required to have detailed stated preference type of data at the individual level (which is beyond the scope of our article). It is in our view natural to use IIA as a basic postulate of individual probabilistic rationality. Recall that here, "probabilistic" is related to our view that behavior is stochastic at the individual level in the sense that if an agent is exposed to repeated choice experiments he may choose different alternatives each time; see for example Tversky (1969). Without such a postulate it will be hard to justify the probabilistic structures of the choice model. It is of crucial importance to be able to pin down a theoretically justified individual model, because otherwise we surely will not be able to identify the distribution of the model parameters across the sample. If we cannot separate the individual model structure from unobserved population heterogeneity we cannot test several interesting hypotheses about behavior and choice constraints. As mentioned in the introduction, we shall in our empirical model specification (Section 4) allow for a random effect in the empirical model specification which means that in the empirical application below IIA only is assumed to hold conditional on the random effect.

The structure of the intensity measure means that the taste-shifters {ε(z)} are distributed independently of {(H (z ), W (z))} (cf. Section 2.5 where we return briefly to this issue). The above formalism implies that the choice sets are allowed to vary randomly across observationally identical agents, because two different agents face independent realizations from the Poisson process. From the properties of the Poisson process it follows that the expected number of points of the process with taste-shifters above any arbitrary threshold r > 0, and (H(z), W(z)) belonging to some set A in R 2 + ≡ (0, ∞) × (0, ∞), is given by (2.4) ∫ (h,w) ∈ A, ε> r d λ (h, w, ε) = θ 1 r − 1 ∫ g (h, w) dh dw.

## A

It therefore follows from (2.4) that the expected number of Poisson points for which (H(z) ∈ (h, h + dh), W(z) ∈ (w, w + dw), ε (z) > r), h > 0, w > 0, equals (2.5) ∫ (h,w) ∈ R 2 +, ε> r d λ (h, w, ε) = θ 1 r − 1 g (h, w) dh dw while the expected number of Poisson points for which (H(z) > 0, W(z) > 0, ε (z) > 0), equals (2.6) θ 1 r − 1 ∫ g (h, w) dh dw = θ 1 r − 1.

## R 2 +

When we form the ratio of (2.4) to (2.6) we get g(h, w)dhdw. Therefore, one can interpret g (h, w) dh dw as the average number of Poisson points with hours and wage rates within (h, h + dh) × (w, w + dw) and with taste-shifters above r, to the average number of Poisson points with positive hours, wage rates and taste-shifters above r. By “average” we mean the average taken over a large number of realizations of the Poisson process. Since r can be chosen arbitrarily small the requirement ε (z) > r represents no essential constraint.

Similarly, if we integrate the intensity measure over the set D ≡ {(h, w, ε): h ≥ 0, w ≥ 0, ε > r} we get (2.7) ∫ d λ (h, w, ε) = r − 1

## D

which is the expected number of points of the Poisson process with taste-shifters greater than r. With A = (0, ∞) × (0, ∞) in (2.4) we get from (2.6) and (2.7) that θ 1 can be interpreted as the average number of Poisson points with positive hours and wage rates to the average number of Poisson points. Thus, in the context of the present application we can interpret g (h, w) dh dw as the fraction of jobs with hours and wage rates within (h, h + dw) × (w, w + dw) thaton averageare feasible to the agent. In other words, g(h, w)dhdw yields the probability that a market opportunity with H (z) ∈ (h, h + dh) and W (z) ∈ (w, w + dw) shall be feasible (cf. Dagsvik, 1994). The term θ 1 can be interpreted as the fraction of the feasible opportunities that are market opportunities. Hence 1 − θ 1 is the corresponding fraction of feasible opportunities that are non-market opportunities. The density defined by θ 1 g(h, w) when h > 0, w > 0, and by 1 − θ 1 when h = w = 0, will be called the opportunity density. Note that although the non-market opportunities look the same to the analyst due to the fact that they have observable attributes (wages and hours) equal to zero, they are perceived as different by the agent since he may have preferences over qualitative unobservable attributes. Recall that the agents themselves are assumed to be perfectly certain about their opportunities, so the opportunity density is just an aggregate representation of unobserved heterogeneity in the set of opportunities from the econometrician’s point of view.

In Dagsvik (1994) it is demonstrated that the set of Poisson points for which the utilities lie above any given positive level is finite (with probability one). Thus the set of “interesting” feasible jobs is (almost surely) finite, and it varies from one agent to another.

2.2. A discrete/continuous choice model with heterogeneous opportunity sets We are now ready to express the probability distribution of realized hours and wages, including the probability of not working. Let Φ(h,w;I) be the joint cumulative distribution of realized hours and wages that follow from utility maximizing behavior, i.e., (2.8)   Φ (h, w;I) ≡ P  max z (ψ (H(z), W(z)) ε (z)) = max z (ψ (H(z), W(z)) ε (z)) .

 H(z) ≤ h, W (z) ≤ w  Equation (2.8) defines the probability that the chosen opportunity (i.e. job) has hours of work less than or equal to h and wage rate less than or equal to w.

Theorem 1 Assume that Assumptions 1 to 3 hold. Then the probability density ϕ(h,w;I) is given by ϕ (h,w;I) = (2.9) ψ (h,w; I) g(h,w) θ ψ (0,0; I )+ θ ∫ ∫ ψ (x, y; I) g(x, y)dx dy

## D

for h > 0, w > 0, and (2.10) ϕ (0,0; I) = ψ (0,0; I) ψ (0,0; I )+ θ ∫∫ ψ (x, y; I) g(x, y)dx dy ,

## D

for h = w = 0, where θ = θ 1 (1 − θ 1), and D = (0,h   × R +.

The proof of Theorem 1 follows from Dagsvik (1994), but to make the paper self-contained we have outlined the proof in Appendix B.

The parameter θ can be interpreted as the ratio of the mean number of feasible market opportunities to the mean number of feasible non-market opportunities.

Although we have assumed that the agent's taste-shifters are (stochastically) independent of offered hours and wage rates, the distribution function of the preferences and the opportunity density are allowed to be dependent. In other words, the market forces that regulate the balance between supply and demand, be it a market clearing regime or not, are assumed to operate solely on an aggregate level. The opportunity density may depend on the production technology of the firms as well as of the contract and wage setting policies of the unions and the firms. It is beyond the scope of this paper to discuss how the opportunity density θg(⋅), through market equilibrium processes, depend on the systematic part of the utility function, ψ(⋅). This means of course that the estimated model only can be applied to simulate behavior conditional on the opportunity density. In Dagsvik (2000), it is suggested how an explicit equilibrium model version can be specified and how the opportunity density depends on workers’ preferences and firms’ technologies.

Let us consider the particular case where the agent perceives no constraints on behavior. If in this case, preferences are solely governed by i.i.d. random terms, then the probability of working will be equal to 0.5. The case with totally random preferences corresponds to the case with ψ (h, w;I) = ψ (0,0;I) for all h and w. Hence, in this case (2.10) reduces to ϕ (0,0;I) = 1 . Thus, for ϕ (0,0;I) to be equal to 0.5, θ 1 + θ must be equal to one. Thus, 1 is the upper bound on θ.

So far, we have demonstrated that the formulation above allows for a particular type of quantity constraints, which typically are rather difficult to account for by means of the econometric formulations used in traditional labor supply studies.

Let g 1 (w|h) be the conditional density of offered wages given the level of offered hours, and g 2 (h) the unconditional density of offered hours. Provided v(C,h) is multiplicatively separable in hours and consumption, i.e., v (C, h) = v 1 (C) v 2 (h ), and that fixed cost of working is observed, Dagsvik and Strøm (1997) demonstrate that v 1 (C) and g 1 (w|h) are non-parametrically identified. A more difficult task is to separate v 2 (h) from g 2 (h). Due to the fact that (2.11) ψ (h, w;I) g(h, w) = v 1 (f (hw, I)) v 2 (h)g 1 (w h) g 2 (h) we can only identify v 2 (h)g 2 (h) non-parametrically. Thus, to disentangle v 2 (h) from g 2 (h) one needs to make additional assumptions. Below we make functional form assumptions that ensures identification. 3 However, it is important to be aware of the fact that if the purpose is to carry out policy simulations for which the distribution of offered hours is kept fixed, it is not necessary to identify v 2 (h) and g 2 (h), separately. 4 2.3. Functional form Current quantitative economic research often suffers from the lack of theoretical principles on which assumptions about functional form can be made. While elaborate and sophisticated theoretical models of behavior exist, such models are often not detailed enough to be useful for purposes other than qualitative predictions. The standard approach in this case is either to “let the data determine” functional forms within ad hoc selected parametric classes, or to resort to semi-parametric methods. This is clearly unsatisfactory in the context of structural modeling. In the preceding sections we have insisted on a theoretical foundation for the stochastic properties of our model. These properties led to a particular representation of the labor supply choice probabilities ((2.9) and (2.10)) in terms of functions that represent preferences and opportunities. However, unless we are able to justify the choice of functional form of the systematic part of the utility function and the opportunity distribution, the implications may, as regards structural empirical analyses, be ambiguous. This is due to the fact that the class of a priori admissible opportunity distributions and utility functions is very large. In this section we shall discuss some interesting implications from the theory of psychophysical measurement and dimensionality analysis. The point of departure taken and exploited in some of the literature of psychophysical measurement is that numerical representations of sensory perceptions and physical stimuli can only be measured up to a scale 5. For example, if the relevant stimuli are quantities or money, this type of variables are measured on a ratio scale. There is by now a considerable literature that addresses the issue of meaningfulness and dimensional invariance of scientific laws. We shall apply a typical approach within the field of psychophysics, as presented in Falmagne (1985), to restrict the class of functional forms for the systematic part of the utility function.

To this end, consider now the particular case with an opportunity distribution that has all mass in two points (h, w 1) and (h, w 2), with probability mass equal to 0.5 in either point. (Since preferences are assumed independent of opportunities, the analyst is, for the sake of interpretation and theoretical analysis, free to select any opportunity distribution he finds suitable for a specific purpose while keeping the function v(⋅) unchanged.) Then from (2.9) it follows that v (C 1, h 1) (2.12) v (C 1, h 1) + v (C 2, h 2) ≡ ϕ% (C 1, L 1 ;C 2, L 2) where ϕ% (C 1, L 1 ;C 2, L 2) is the probability that (C 1, L 1) is preferred to (C 2, L 2). It is understood that consumption in this context means disposable income minus subsistence expenditure and leisure means leisure minus subsistence leisure.

Assumption 4 Suppose C 1, C 2, C 1 *, C 2 *, L 1, L 2, are such that ( ) ϕ% (C 1 ,L 1 ;C 2 ,L 2) ≤ ϕ% C 1 * ,L 1 ;C 2 * ,L 2.

Then ( ϕ% (r C 1 ,L 1 ;r C 2 ,L 2) ≤ ϕ% r C 1 * ,L 1 ;r C 2 * ,L 2 ) for any positive r.

Assumption 4 states that if the fraction of workers that prefer jobs that yield (C 1, L 1) to jobs ( ) that yield (C 2, L 2) is less than the fraction of workers that prefer jobs that yield C 1 *, L 1 to jobs that ( ) yield C *2, L 2, then the same is true when the respective consumption levels are scale transformations of the original levels. Recall that the nonpecuniary characteristics of the jobs are represented by random terms that are independent of the systematic terms {v (C, h)}. Assumption 4 captures the notion that once basic needs (subsistence) are fulfilled, then the absolute levels of quantities tend not to be essential, rather the individuals relate to relative consumption levels. Note, however, that Assumption 4 does not claim that ϕ% (r C 1, L 1 ;r C 2, L 2) is independent of r. It expresses instead that if ( ) ( ) the number of individuals that prefer C 1 *, L 1 to C *2, L 2 is greater than the number of individuals that prefer (C 1, L 1) to (C 2, L 2), this inequality remains true when consumption levels are increased or decreased by the same factor. For the sake of understanding the limitation of Assumption 4, we can think of two objections against this assumption. One objection is that the individual’s perception about his personal subsistence level may be somewhat vague and may not be identified by a single fixed amount. Rather it may vary from one moment to the next according to fluctuations in his mood and state of mind. Another objection is related to satiation. If satiation is present and rC 1 * and rC *2 are close to satiation levels for sufficiently large r and L 1 = L 2 = L (which means that the deterministic part of the utility approaches a constant), the second inequality in Assumption 4 may be reversed because ϕ% (rC 1 *, L;rC * 2, L) will be close to 0.5, independent of the levels of C 1 *, C * 2 and L. In the absence of satiation it seems to us to be highly unreasonable that the inequality ϕ% (C 1, L 1 ;C 1, L 2) ≤ ϕ% (C 1 *, L 1 ;C * 2, L 2) should be reversed if the consumption levels are rescaled; i.e., that Assumption 4 is violated.

The notion that relative stimuli levels matter rather than absolute ones is supported by numerous stated preference experiments, see for example Stevens (1975).

Assumption 5 Suppose L 1, L 2, L * 1, L * 2, C 1, C 2, are such that ϕ% (C 1 ,L 1 ;C 2 ,L 2) ≤ ϕ% (C 1 ,L * 1 ;C 2 ,L * 2).

Then ϕ% (C 1 ,rL 1 ;C 2 ,rL 2) ≤ ϕ% (C 1 ,rL * 1 ;C 2 ,rL * 2) for any positive r.

We realize that Assumption 5 is completely analogous to Assumption 4 and thus the motivation is similar. 6

Theorem 2

If Assumptions 4 and 5 hold, then log v (C ,h) = β 1 (2.13)

## (C

α 1 − 1 α 1 ) + β (L α 2 2 − 1 α 2 ) + β (C α 1 3 )( − 1 L α 2 − 1 α 1 α 2 ) where {α j} and {β j} are constants, α j < 1 and β j > 0.

A proof of Theorem 2 is given in Appendix C. If one imposes the stronger assumption that ϕ% (r C 1, L 1; r C 2, L 2) is independent of r > 0, it can easily be demonstrated that this implies that α 1 = 0. If one imposes the assumption that ϕ% (r C 1 ,s L 1 ;r C 2 ,s L 2) is independent of r and s, for all r > 0, s > 0, it is easily seen that this yields that α 1 = α 2 = β 3 = 0 so that (2.13) reduces to log v (C, h) = β 1 log C + β 2 log L (2.14) which is the well known Stone Geary utility function. (Recall that C and L are defined as consumption and leisure minus the respective subsistence levels.) There is a number of studies in experimental psychophysics that are concerned with the measurement of the utility of income. Consistent with the result of Theorem 2, Stevens (1975) and his followers have found that a power function fits the data well, 7 cf. Stevens (1975), p. 246. See also Breault (1981).

The result of Theorem 2 does not depend on the particular form of ϕ% (⋅) given in (2.12). In fact, it can easily be verified that it is enough to assume that ϕ% has the form  v (C 1, h 2)  ϕ% (C 1, L 1 ;C 2, L 2) = F      v (C 2, h 2)  where F is any strictly increasing c.d.f. on R +. This is so because the proof does not depend on the form of F(·).

2.4. Extension to several sectors An essential motivation for the framework discussed in this paper is that it is particularly convenient for modeling workers’ choice among jobs with observable non-pecuniary job attributes. In general, jobs in different sectors may differ with respect to job non-pecuniary attributes, such as job-security (with the government sector at one extreme, and private export industries at the other) and the nature of the tasks to be performed.

In this section we shall outline how the model can be extended to a multisectoral setting. To this end, we now suppose that the agent can choose among m sectors. The utility function in this case is assumed to have the structure U (C, h, j, z) = v (C, h) µ j ε j (z) (2.15) where j indexes sector, j = 0,1,..., m, and j = 0 represents “not working”, and µ j > 0 is a constant that represents the pure average preference of working with sector j specific tasks. The extension of the intensity measure in (2.3) is given by (2.16) θ 1j g j (h, w) ε − 2, when h > 0, w > 0, ε > 0  m d λ j (h, w, ε) =    θ 1k  ε − 2, when h = w = 0, ε > 0   1 −    k = 1 ∑ where dλ j is the sector-specific intensity measure and g j (h, w) is the corresponding opportunity density. That is, g j (h, w) dh dw is the mean fraction of feasible jobs in sector j with offered hours of m   work and wage rates within (h, h + dw) × (w, w + dw). Let θ j = θ 1j  1 − θ 1k , where θ j is the  k = 1  ∑ mean fraction of non-market opportunities related to sector j. Let ϕ j (h, w) dh dw denote the probability of choosing a job in sector j with hours of work and wage rate within (h, h + dw) × (w, w + dw). Similarly to Theorem 2 it follows that (2.17) ϕ j (h, w;I) = ψ (h, w;I) µ j θ j g j (h, w) ψ (0,0;I) + m ∑ µ θ ∫∫ ψ (x, y;I) g (x, y) dx dy k = 1 k k k

## D

for h > 0, w > 0, and (2.18) ϕ (0,0;I) = ψ (0,0;I) + m ψ (0,0;I) ∑ µ θ ∫∫ ψ (x, y;I) g (x, y) dx dy k = 1 k k .

k

## D

3. The relationship between the present framework and previous labor supply models 3.1. Relation to the Hausman-and similar approaches It is interesting to note that a specification of the labor supply model based on the Hausman type approach, follows as a special case of a random coefficient version of the present framework. To realize this, assume for expository simplicity and in complete accordance with the assumptions made in the Hausman type of models, that the wage rate is fixed for a given individual and that the opportunity distribution of hours is uniform. Suppose furthermore that the coefficients of ψ(⋅) are random and let the error term ε(z) be replaced by ε(z) σ, where σ is a constant. From (2.8) it now follows that the corresponding choice probability density of hours can be expressed as 1 σ   ψ (h, w;I)   ϕ (h | w) = E   1/ σ 1/ σ   ψ (0,0;I) + ∫ ψ (x, w;I) dx   * (3.1) where the expectation operator now is taken with respect to the random coefficients of the utility function.

%, of The choice probability density given in (3.1) corresponds to the maximization of a utility function, U the form % (h, w) = ψ (h, w;I) ε% (h, w) σ

## U

(3.2) where the distribution of the random terms {ε% (h, w)} is independent of the systematic term, ψ. We % (h, w) → ψ (h, w;I), in which case the utility maximization problem realize that when σ → 0 then U reduces to the conventional marginal calculus approach. However, when σ > 0 eq. (3.1) will not be differentiable because the error term ε% (h, w) depends on h and is not differentiable in h. Furthermore, since the supply function in this case will be stochastic in a non-trivial way the corresponding Slutsky matrix will not necessarily be positive definite in this case.

To illustrate this point further let us consider a typical specification that has been applied by Hausman and several other researchers. This specification is given by the utility function (3.3)  α 2 (C + α 3)   h − α 1  

U * (C, h) =   exp   α 2   h − α 1  where α 1 and α 3 are unknown parameters and α 2 ≤ 0, is a random coefficient. The utility function (3.3) implies that the labor supply function is linear in the marginal wage rate and virtual income. 8 Eq. (3.3) implies that (3.4) ψ (h, w;I) 1 σ 1 σ  α 2 (C + α 3)   h − α 1  =   .

 exp    α 2   σ (h − α 1)  From (3.4) it follows (under suitable identification conditions) that σ, α 1, α 3 and the distribution of α 2 can be estimated from a likelihood function based on (3.1). In other words, the Hausman type of models can be viewed as embedded in a particular random coefficient version of the framework developed in this paper.

3.2. Relation to studies with latent constraints on hours of work For the sake of comparison with some recent studies in labor supply econometrics that discuss modeling strategies for dealing with constraints, consider for a moment the following setting: The agent has a utility ~ function U (C, h, ε) where ε is a random taste-shifter (independent of (C,h)). The budget constraint is given by (2.1) and the offered wage rate is fixed for each agent. Assume that hours of work take values in a finite set B (say). Let ~ V (h, w, ε) = U (f (hw, I ), h, ε).

(3.5) Then it follows that the probability density of hours, conditional on the wage rate and the set B, is given by ϕ $ (h w, B) ≡ P   V (h, w, ε) = max V (x, w, ε)  .

  x ∈ B (3.6) Suppose now that B is unobserved by the analyst and can take any value in the set {B 1, B 2 ,..., B m}. For example B could consist of the options “full-time”, “part-time” and “not working”, or of “part-time” and “not working”. To account for this, assume that B is random. Let q j be the probability that B = B j. The unconditional probability density that corresponds to the data the analyst has at hand therefore equals 9 ϕ $ (h w) ≡ E B ϕ $ (h w, B) = (3.7) ∑ q

B j ⊃ h j   P  V (h, w, ε) = max V (x, w, ε) .

x ∈ B j   In (3.7) it is the quantity “hours of work” that is rationed, whereas in our model, presented in section 2 above, a latent choice variable, “job opportunity”, is introduced. Possible rationing of hours may occur because there may be few or no feasible jobs with the desired hours of work. The models developed by Ilmakunnas and Pudney (1990), and Dickens and Lundberg (1993) fall within the framework represented by (3.7).

Our notion of unobservable choice variables proposed in this paper has several attractive features.

First, the framework with unobservable job opportunities introduced in section 2 allows for the interpretation that the outcome of an agent's labor supply decision is the result of the agent maximizing utility over “job-packages” with several attributes of which hours of work is only one of them. Second, the framework is convenient for dealing with latent opportunity sets, while the type of formulation represented by (3.7) is a mixture of multinomial logit type densities and becomes rapidly intractable when m increases.

4. An empirical application 4.1. Empirical specification The present application does not exploit the full potential of the methodology: The only non-pecuniary attribute that is recorded in the data is which sector of the economy the jobs belong to. For simplicity, we only consider the case with two sectors, private and public sector, and for the following reasons. For women with higher level of education there are more job opportunities in the public than in the private sector. Moreover, in the public sector more emphasize has been put on facilitating combination of work and childcare, and thus one is more likely to find a job with a subsidized day-care center in the public than in the private sector. The public sector is more unionized than the private sector. Wages are more compressed and hours are more constrained. However, the job security tends to be higher in the public sector than in the private sector. Finally, some job types are only found in the public sectors (such as colleges and universities) while others are found solely in the private sector (a large number of manufacturing firms). Thus, there are important differences between the private and the public sector that could influence the labor supply decisions of married women. Some of these differences are observed (like wages) while others are not. The modeling framework appropriate for this application is the one outlined in subsection 2.4, where sector one is the public sector and sector two is the private sector and m = 2.

We will assume that offered hours and offered wages are independent, i.e.

g j (h, w) = g j1 (w)g j2 (h) (4.1) for j = 1, 2. Although offered wages and hours vary across jobs, our assumption is that hours are set independent of wages. The justification for this assumption is that offered wages, in the unionized part of economy, are set in yearly wage settlements. Normal working hours, on the other side, is determined more infrequently, typically once or twice every decade. The density of offered hours, g 2 j (h) is assumed uniform except for peaks at full-time and part-time hours. Recall that uniformly distributed offered hours corresponds to the notion of a perfect competitive economy. Thus, the fulltime peak in the hours distribution captures institutional restrictions and hence market imperfections in the economy. We allow the sizes of the full-time and part-time peaks to vary across sectors. The rationale is that the public sector is more regulated than the private sector, also because the private sector is more heterogeneous and less unionized. Thus we expect the full-time peaks associated with the public sector to be higher than the full-time peak associated with the private sector. Note also that normal working hours may vary across jobs according to how strenuous the jobs are considered to be. For example nurses, fire-workers and police officers have typically lower normal working hours than the average worker.

In the absence of random effects, it would have been possible to apply McFadden’s (1978) estimation procedure to estimate continuous logit models. McFadden’s estimation procedure replaces the integrals in the denominators of the densities in (2.17) and (2.18) by a sum over a small set of random points, where each term is adjusted by appropriate weights. In other words, the continuous logit model is replaced by a discrete logit version. McFadden has demonstrated that this method yields consistent and asymptotically normal parameter estimates. However, as will be discussed shortly, our empirical model will be modified to allow for particular random effects and this implies that the logit structure is lost and consequently, McFadden’s procedure can no longer be applied.

To facilitate estimation, we have discretisized observations on hours of work. For each sector we have specified 7 hours of work intervals. The medians of the intervals range from 420 annual hours in the first interval to 2808 in the 7 th interval. For each sector the full-time peak occurs in the 5 th interval where the median is 1950 annual hours. The part-time peak is related to the 3 rd interval with a median equal to 1040 annual hours. These intervals correspond to the most common agreements of what constitutes full time and half time annual hours of work.

In section 2.3 we postulated particular invariance properties that allowed us to characterize the functional form of the structural part of the utility function. Unfortunately, we have not been able to provide similar principle to characterize the functional form of g j1 (w). Recall that g j1 (w) is the subjective density of offered wage rates, as perceived by the agent. We shall therefore, in the present application, abandon the specification and estimation of g j1 (w), which implies that we can only estimate the marginal density of chosen hours of work and sector.

Let w j be the subjective mean in the offered wage rate distribution in sector j, i.e., w j = (4.2) ∫ y g j (y)dy.

y > 0 By the mean value theorem we have that ∫ ψ (h, y;I) g (4.3) j1 (y)dy ( ) ≅ ψ h, w j ;I.

y > 0 The approximation in (4.3) is good if the variance in the subjective opportunity density g j1 (w) is small.

To allow for unobserved heterogeneity in the opportunity densities we assume that w j = w * j η j (4.4) {} for j = 1, 2, where η j are random effects. We assume that log η j, j = 1, 2, are independent and ( ) normally distributed, N 0,σ j.

The systematic term of the subjective mean wage rate, w *j, is assumed to vary across sectors and log w *j is assumed to be a linear function of length of schooling, work experience and work experiences squared.

Thus, when accounting for the unobserved heterogeneity in the opportunity densities, it follows from (2.17), (2.18) and (4.2) to (4.4) that the resulting choice probabilities that corresponds to our observations are (4.5)   ψ (h, w *j η j ;I) g j2 (h)b j  , ϕ j (h; w, w, I) ≡ ∫ ϕ j (h, y;I) g j1 (y)dy = E * *  ψ (0,0;I) + b 1 ∑ ψ (x, w 1 η 1 ;I) g 12 (x) + b 2 ∑ ψ (x, w 2 η 2 ;I) g 22 (x)  y > 0     x > 0 x > 0 * 1 * 2 for h > 0, j = 1, 2, and (4.6)   ψ (0,0;I)  , ϕ (0; w, w, I) = E  ψ (0,0;I) + b ∑ ψ (x, w * η ;I) g (x) + b ∑ ψ (x, w * η ;I) g (x)  1 1 1 12 2 2 2 22     x > 0 x > 0 * 1 * 2 where expectation is taken with respect to {η 1, η 2}, and b j = µ j θ j.

For many reasons, most women are working in the service branch of the economy and thus for women there are more feasible jobs available in firms that provide services than elsewhere. In Norway, most of the services are provided by the public sector (health services, education etc) and many of the jobs here require higher education, while the services provided in the private sector say, in retail sale, are typically based on low-skill labor. Thus it is reasonable to assume that b j may depend on education. We will expect that the higher the education is, the higher is the number of feasible jobs in the public sector. We have assumed that log b j = f j1 + f j2 S (4.7) where S is the length of education.

We have chosen log v(⋅) to be of the form given in Theorem 2.

(4.8) α  10 − 5 (C − C 0) α 1 − 1   (L − L 0) 3 − 1   α + α log A + α (log A) 2 + α CU6 + α CO6 log v(C, h) = α 2   +  4 5 6 7 8   α α 1 3     ( )  10 − 5 (C − C 0) α 1 − 1  (L − L 0) α 3 − 1    + α 9     α 1 α 3    where A, is the age of the married woman, CU6 and CO6 are the number of children less than 6 and above 6 years, C is given by f (hw, I), L is leisure, defined as (4.9) L − L 0 = 1 − h 3640, and α j, j = 1, 2,...,8, are unknown parameters. Observe that we have subtracted from total annual hours a “subsistence” level, L 0 = 1.407, that allows for sleep and rest. This corresponds to about 14 hours per day reserved for sleep and rest.

Consistent with psychophysical evidence, we have also introduced a subsistence threshold level, C 0 for consumption in the v(⋅) function. We have chosen C 0 to be close to the official estimate of a subsistence level in Norway (NOK 60 000). If α 1 < 1, α 3 < 1, α 2 > 0, and α 4 + α 5 log A + α 6 (log A) + α 7 CU6 + α 8 CO6 > 0 2 (4.10) then log v (C, h) is increasing in C, decreasing in (h) for fixed C and strictly concave in (C, h).

To facilitate the estimation procedure we have estimated the wage equation (regressed log w *j against the observed covariates mentioned above) in a first step by applying a version of the two stage Heckman approach to control for selectivity. Conditional on these estimates the remaining parameters of the model are estimated by the maximum likelihood procedure. To compute the expectations in (4.5) and (4.6) we have generated a large number of independent random variables; {η jk , k = 1, 2,..., M}, for j = 1, 2, where {log η jk} are normally distributed, N(0,σ j ). Hence, we can write (4.11) ϕ 1 (h; w 1 *, w * 2, I) = ψ (h, w 1 * η 1k ;I) g 12 (h)b 1

## 1 M M

∑∑ M 2 k = 1 t = 1 ψ (0,0;I) + b 1 ∑ ψ (x, w 1 * η 1k ;I) g 12 (x) + b 2 ∑ ψ (x, w * 2 η 2t ;I) g 22 (x) x > 0 x > 0 and similarly for ϕ 2 (h; w 1 *, w * 2, I) and ϕ (0; w 1 *, w * 2, I).

4.2. Data Data on the labor supply of married women in Norway used in this study consists of a merged sample from “Survey of Income and Wealth, 1994”, Statistics Norway (1994) and “Level of living conditions, 1995”, Statistics Norway (1995). Data covers married couples as well as cohabiting couples with common children. The age of the spouses ranges from 25 to 64. None of the spouses are self-employed and none of them are on disability or other type of benefits. All taxes paid are observed and in the assessment of disposable income, at hours not observed, all details of the tax system are accounted for. Observed hours of work are related to main job as well as possible side jobs. The size of the sample used in estimating the labor supply model is 824. Wage rates above NOK 350 or below NOK 40 are not utilized when estimating the wage equations. The wage rates are computed as the ratio of annual wage income to hours worked. The sample used to estimate the wage equation is larger than the sample used to estimate the labor supply model, due to the fact that we have used wage rate data for single women, while the labor supply model only holds for married women. (The data set used here is different than the one used in Dagsvik and Strøm, 2002).

In Table 1 we report the summary statistics for the sample used in estimating the labor supply model.

Table 1. Summary statistics for married women, Norway 1994

Not working

Public sector

Private sector

Mean

Std.

Mean

Std.

Mean

Std

Age in years 40.44 9.92 41.24 8.68 38.68 9.08

Education in years 11.02 2.01 12.36 2.34 10.88 1.62

No of children, 0-6 0.73 0.83 0.44 0.74 0.63 0.81

No of children, 7-17 1.00 1.01 0.75 0.86 0.53 0.80

Annual hours of work 0 0 1641 489 1570 571

Disposable household income, NOK per year 322 131 200 684 329 064 122 616 331 354 125 754 104.30 28.52 100.56 30.46

Wage rate, NOK per hours

Number of observations

Fractions 66 405 353 0.080 0.492 0.428 4.3. Estimation results for the wage equations In this section we report estimates of the wage equation and the structural model.

Table 2. Estimates of wage equations. Married women, Norway 1994

Public sector

Private sector

Variables

Estimates t-values

Estimates t-values

Constant 3.37 13.5 3.70 25.2 3.21 6.0 2.55 5.1 (Experience in years) /100 -4.75 -5.3 -3.80 -4.2

Education in years/100 5.57 4.9 5.26 4.2

Log (Probability of working in the chosen sector) -0.12 -2.0 0.06 0.9

Variance 0.059 18.6 0.075 17.0

Experience in years/100 2

No of observations 2

## R

691 580 0.14 0.08 In the wage equations, the logarithm of observed wage rates, log W k, k = 1, 2, is regressed against working experience, working experience squared, education level and a term capturing possible selectivity. It can be demonstrated that one can control for selectivity bias by applying log P j as an additional independent variable where P j is a reduced form trinomial logit model for being in sector j, j = 0,1, 2, (where j = 0 means not working). The explanatory variables in the reduced form trinomial logit are the same as the ones that enter in (4.5) and (4.6). Estimates of the wage equations are given in Table 2, and we observe that on the margin workers get slightly better paid for experience and education in the public sector than in the private sector. However, the differences in returns across sectors are not significant. On a much larger sample Barth and Røed (2001) reports similar results for 1995.

Judged by R 2 the explanatory power of the wage equations is low. Thus, it seems important to account for unobservables in the wage equation when estimating the structural model. In Section 4.1 we have explained how we account for the unobservables in the wage equations. This is done by introducing random effects when we estimate the structural model.

## 4.4 Estimates of labor supply probabilities

Estimates of the parameters in the structural choice model are given in Table 3. Both exponents are significantly below 1 and the estimates thus imply that the deterministic part of the utility function is quasi-concave. We note that the parameter associated with the interaction term between consumption and leisure is not significantly different from zero. Hence, we cannot reject the hypothesis that the deterministic part of the utility function is additively separable in consumption and leisure.

Marginal utilities of consumption and leisure (for all relevant age of the women) are both positive. The latter depends significantly on age and number of children. Marginal utility of leisure is a convex function of age, with marginal utility increasing with age after 31-32 years of age. Marginal utility of leisure is positively affected by number of children. We observe that the number of young and “old” children has the same impact on the marginal utility of leisure. It is interesting to note that when the women are young and have children this reduces their incentive to participate in labor market activities, and when they are older and without children the age effects gradually reduces their incentives to participate in labor market activities.

The exponent α 1 is significantly different from zero, which means that agents do not only care about relative consumption levels (beyond subsistence). Absolute levels also matter. The exponent α 3 is not significantly different from zero (at a 5 per cent level or less), which means that we cannot reject the hypothesis that the deterministic part of the utility function is log-linear in leisure.

The estimates of the opportunity density confirm the conjecture that there are more jobs available in the public sector for higher educated women than for women with little education. This means that if length of schooling is increased while wage rates are kept fixed, participation in the public sector will increase. In the private sector education does seem to have the opposite effect. At first glance this seems to indicate that high educated women tend to be “overqualified” in the private sector. However, this may also be due to a neglected preference effect: If preferences depend on schooling such that highly educated women tend to prefer jobs in the public sector (university, etc.) this would imply that b 2 is decreasing in S. Moreover, the full-time peak is more distinct in the public sector than in the private. As mentioned above this may be due to the fact that the public sector is more unionized than the private one.

Table 3. Estimation results for the parameters of the labor supply probabilities Variables

Parameters

Estimates t-values α 1 α 2 0.64 1.77 60 000 6.5 4.2 α 3 α 4 α 5 α 6 α 7 α 8 -0.53 115.02 -63.61 9.20 1.27 0.97 -1.9 3.2 -3.2 3.3 4.2 3.9 α 9 -0.12 1.407 -1.4 f 11 f 21 f 12 f 22 -4.20 1.14 0.22 -0.33 -4.3 1.0 2.7 -3.0

Full-time peak, public sector (sector 1) * log (g 12 (h Full) g 12 (h 0)) 1.58 11.4

Full-time peak, private sector (sector 2) log (g 22 (h Full) g 22 (h 0)) 1.06 7.8

Part-time peak, public sector log (g 12 (h Part) g 12 (h 0)) 0.68 4.6

Part-time peak, private sector log (g 22 (h Part) g 22 (h 0)) 0.80 5.1

Preferences:

Consumption:

Exponent

Scale · 10 -5

Subsistence level C 0

Leisure:

Exponent

Constant

Log age (log age) 2 # children 0-6 # children 7-17

Consumption and Leisure, interaction

Subsistence level L 0

The parameters b 1 and b 2;

log b j = f j1 + f j2 S

Constant public sector (sector 1)

Constant private sector (sector 2)

Education public sector (sector 1)

Education private sector (sector 2)

Opportunity density of offered hours, g k2 (h), k=1,2 # observations 824

Log likelihood -1760.9 * The notation h 0 refers to an arbitrary level of hours of work different from full-time and part-time hours.

The number of random draws (M) used in the simulations used to compute the likelihood function equals 50.

Table 4 compares observed and predicted aggregates, and we note that the model predicts these aggregates pretty well.

Table 4. Observed and predicted aggregates. Married women, Norway 1994.

Not working

Variables

Choice probabilities

Annual hours

McFadden’s ρ

Public sector

Private sector

Observed

Predicted

Observed

Predicted

Observed

Predicted 0.080 0.079 0.492 0.483 0.428 0.438 0 0 1641 1585 1570 1632 2 0.21 As noted above, we can only identify the product v 2 (h)g 2 (h) non-parametrically. To disentangle v 2 (h) from g 2 (h) we have assumed that the clustering of hours of work at part-time and full-time work is due to technological organizational constraints and/or regulation of hours introduced by unions and/or the government. The term g 2 (h) is meant to capture this aspect of the labor market in the highly unionized Norwegian economy. Thus, through parametric identification our model implies that observed concentration of hours of work around part-time and full-time work arise because there are institutional constraints in the labor market rather than because individuals have strong preferences for full-time and part-time hours of work. If the parameters of the utility function are robust with respect to our assumption, then our empirical model may be applied also to simulate the impact of a change in the institutional constraints on available working hours in the market.

To contrast our approach with the more familiar one with uniformly distributed offered hours we have reestimated the model under the assumption that offered hours are uniformly distributed. It goes without saying that the parameters attached to the leisure term will be affected when we force the clustering of hours to be explained solely by preferences.

Of greater interest is how the estimates of the other parameters of the utility function is affected when offered hours are assumed to be uniformly distributed.

From Table 5 we observe that the estimates of the parameters related to consumption are the same in the two cases. The significance of the parameter associated with the interaction between consumption and leisure is improved, but the estimate is the same. We also note that the parameters in the sector-specific opportunity densities do not change.

The exponent related to the leisure term is significantly different from zero and negative when offered hours are uniformly distributed. The numerical value is higher when offered hours are uniformly distributed. This is natural, because when the clustering of hours is due to spikes in the distribution of offered hours, labor supply responses to marginal wage changes becomes weak, given a full time job. To reflect the same type of behaviour when offered hours are assumed to be uniformly distributed, the utility function has to change. A negative, and higher numerical, value of the exponent related to leisure gives the warranted result. Moreover, and for the same reason, when offered hours are uniformly distributed, all of the other parameters in front of the leisure term will be scaled down, as can bee seen from Table 5. As in the preceding case marginal utility of leisure is positive for all relevant ages and marginal leisure is at a minimum for the same age as before, around 32 years of age. It is important to note that if offered hours are not uniformly distributed, which there are good reason to believe, then a change in this institutional constraint will be considered wrongly to yield a shift in preferences in labor supply models that assume uniformly distributed offered hours.

Table 5

Uniformly distributed offered hours except at part-time and full-time hours

Preferences:

Consumption:

Exponent

Scale ⋅ 10 -5

Consumption and leisure, interaction

Leisure:

Exponent

Constant log age (log age) 2 # children 0-6 # children 7-17 b 1 and b 2:

Constant, sector 1

Constant, sector 2

Education, sector 1

Education, sector 2

Log likelihood f 11 f 21 f 12 f 22

Uniformly distributed offered hours

Estimates t-values

Estimates t-values 0.64 1.77 6.5 4.2 0.54 1.96 6.0 4.0 -0.12 -1.4 -0.08 -1.9 -0.53 115.02 -63.61 9.20 1.27 0.97 -1.9 3.2 -3.2 3.3 4.2 3.9 -1.88 40.92 -22.50 3.23 0.43 0.30 -5.1 2.5 -2.5 2.5 2.9 2.7 -4.20 1.14 0.22 -0.33 -4.3 1.0 2.7 -3.0 -4.87 -0.02 0.24 -0.26 -5.4 -0.1 3.1 -2.8 -1760.9 -1862.0 4.5. Wage elasticities The mean utility, ψ j (.), is the utility concept that comes closest to the one often used by others in the calculation of elasticities. To calculate these elasticities one has to assume that the labor supply of the mean sample household can be simulated by maximizing the deterministic part of the utility function under the constraint represented by a linearized version of the budget constraint. Of course, this approach is rather crude since it implies that the stochastic structure of the model is ignored.

Another set of elasticities arises when we consider how the mean in the distribution of labor supply is affected by changes in say, wage levels. We denote these elasticities as aggregate ones since they take into account unobserved and observed heterogeneity in the population. Moreover, they also account for the non-convexity of the budget constraint due to taxation and hours restrictions, and are thus consistent with the structure of the model.

In Table 6 we report what we have called aggregate uncompensated elasticities. They are calculated as follows: The model is used to simulate the labor supply for each female under the current regime and when the wage rates in each sector, and in both sectors, respectively, are increased by one per cent. The aggregate elasticity of female labor supply is obtained by calculating the relative change in the mean female labor supply (over all females in the sample) that results from a one percent wage increase for the females, ceteris paribus. The “estimates” in Table 6 are based on 10 sets of simulations.

Table 6. Aggregate uncompensated wage elasticities

Variables

Choice probabilities and mean hours before wage changes

Elasticities with respect to changes in wage rates

Public sector

Private sector

Both sectors

Participation probabilities:

Working

Working in public sector

Working in private sector 0.921 0.483 0.438 0.15 1.47 -1.32 0.15 -1.38 1.82 0.26 0.07 0.47

Mean annual hours of work, conditional on sector:

Public sector

Private sector 1585 1632 0.32 0.03 0.03 0.29 0.35 0.32

Mean total annual hours of work:

Conditional on job in any sector

Unconditional 1607 1480 0.18 0.33 0.20 0.35 0.34 0.61 Elasticities are numerically small with the exception of how sector specific participation probabilities respond when wage levels are changed. The reasons why overall responses are small are high overall labor market participation among married Norwegian women and a regulated and rigid market for hours. However, we note that when the wage level in the public sector is increased by 1 per cent, the participation probability in this sector increases by as much as 1.47 per cent. Most of this increase comes at the expense of a decrease in the participation probability in the private sector of 1.32 per cent. Overall participation increases by a minor 0.15 per cent. A similar pattern emerges when the wage level in the private sector is raised by 1 per cent. The probability of working in the private sector increases by 1.82 per cent and as in the preceding case, most of the increase comes from a reduction of the probability of working in the other sector, the public sector (1.38 per cent). A similar pattern emerges for annual hours of work, conditional on sector, but the impact is smaller. From the last row in Table 6 we notice that an overall increase of 1 per cent is estimated to raise supplied hours in the total population of married females by 0.61 per cent, with an almost equal split on increased participation and increased supply of hours, conditional on working.

5. Conclusion In this paper we have discussed a particular approach for labor supply modeling, with special reference to the inadequacy of traditional econometric approaches to deal with; (i) The notion that households have preferences over jobs, characterized by job-and sector-specific non-pecuniary attributes, hours of work, and wage rates, including convenient representations of the set of feasible job attributes, (ii) exact representation of complicated and non-convex budget constraints, (iii) justification of the functional form of the utility function and the distribution of unobserved variables. We have demonstrated that the framework presented proves to be practical for dealing with (i) and (ii). A more fundamental theoretical issue is the problem of characterizing the functional form of the empirical model on the basis of theoretical principles. By drawing on the recent literature in measurement theory and theoretical psychophysics, we have shown that it is possible to apply invariance principles to constrain and justify the class of admissible functional forms.

An empirical version of the model has been estimated on a recent sample of Norwegian married women. The estimated model turns out to reproduce the data quite well. It is demonstrated that it is of empirical importance to distinguish between job opportunities across sectors of the economy. The estimated model is used in stochastic simulations to calculate sector specific as well as overall elasticities of labor supply with respect to wage levels. Apparently, weak responses in overall female labor supply shadow for much stronger inter-sector mobility.

Constrained demand and IIA Here the purpose is to show that the traditional theory of consumer behavior yields restrictions that appear (in some sense) more restrictive than IIA.

Consumer i has quasi-concave, increasing utility function U i (x). The utilities vary randomly across consumers due to unobserved heterogeneity in tastes. Let B be the choice set, i.e. a set of quantity restrictions on x in addition to the budget constraint, and let x *i (p, y, B) denote the constrained demand function of price p, income y and choice set B. Let A ⊂ B, and define ( ) P(A, B) = P x *i (p, y, B) ∈ A.

The empirical counterpart to P(A,B) is the fraction of consumers that choose a vector of consumption quantities within A, conditional on quantity constraints represented by B. Now it follows from quasiconcavity and monotonicity of utility that for two choice sets, B 1 and B 2, that P (A, B 1) = P (A, B 2) provided A belongs to the interior B 1 ∩ B 2. This is due to the fact that only the point of tangency between the budget line and the indifference curve matter for the determination of the demand. In other words, when A belongs to the interior of the choice set the theory predicts that the choice probability P(A,B) is independent of B as long as A belongs to the interior of B. Thus, the conventional theory yields restrictions that are similar to IIA and appear even more restrictive than IIA, since IIA only predicts that P (A 1, B) P (A 2, B) is independent of B, where A 1, A 2 ⊂ B. An equivalent statement of IIA is that P (A 1, B 1) P (A 1, B 2) = P (A 2, B 1) P (A 2, B 2), which of course is a weaker condition than P (A, B 1) = P (A, B 2).

Extension of the model to two-person households (married couples) Let U (C, h F, h M, z) denote the household's utility function where h F and h M denote the wife's and the husband's hours of work, respectively, and z = (z F, z M) indexes the market and non-market opportunities of the wife and the husband. Similarly to Assumption 1 we assume that U (C, h F, h M, z) = v (C, h F, h M) ε (z)

## (B.1)

where v(⋅) is a deterministic term and ε(z) is a random taste-shifter. For given wage rates, w F and w M, the economic budget constraint can be written as C = f (h F w F, h M w M, I)

## (B.2)

where f(⋅) is the function on R 3 + that transforms wage-and non-wage incomes of the household to household income after taxes. Let

## (B.3)

( ψ (h F, h M, w F, w M) = v f (h F w F, h M w M, I), h F, h M).

The household's opportunity set can be represented by { } ℘ = (H F (z ), H M (z ), W F (z ), W M (z ), ε (z)); z = .. − 2, − 1, 0, 1, 2 ...

where H F (z) = H M (z) = W F (z) = W M (z) = 0 for z ≤ 0. The five-tuple in ℘ are realizations from a [] [] non-homogeneous Poisson process on 0, h × 0, h × [0, ∞) × [0, ∞) × [0, ∞). The intensity measure of the Poisson process is given by

## (B.4)

 θ 11 g F (h F, w F) g M (h M, w M) ε − 2 dh F dh M dw F dw M d ε,   when h F > 0, w F > 0, h M > 0, w M > 0, ε > 0, d λ (h F, h M, w F, w M, ε) =  − 2  θ 01 g M (h M, w M) ε dh M dw M d ε,   when h > 0, w > 0, h = w = 0, ε > 0.

## M

## M

## F

## F

For notational simplicity the case where the husband does not work is ruled out in this presentation. The interpretation of g F (⋅) and g M (⋅) is completely similar to the interpretation in the case of single person households. In the formulation in (B.4) it is assumed that (conditional on observed household characteristics) the offered hours and wage rates of the husband are independent of the offered hours and wage rates of the wife. This assumption can easily be relaxed at the cost of difficult identification problems. However, the market opportunities of the wife and the husband (represented by θ 11 and θ 01) may be dependent. The parameter θ 11 is the fraction of the feasible opportunities that are market opportunities to the household, while θ 01 is the fraction of the feasible opportunities that are nonmarket opportunities to the wife and market opportunities to the husband. As in Section 2, it follows that the joint density of realized hours and wages, ϕ (h F, h M, w F, w M), equals

## (B.5)

ϕ (h F, h M, w F, w M) = θ ψ (h F, h M, w F, w M) g F (h F, w F) g M (h M, w M)

## K

for h F > 0, h M > 0, w F > 0, w M > 0, and ϕ (0, h M, 0, w M) =

## (B.6)

ψ (0, h M, 0, w M) g M (h M, w M)

## K

when h F = w F = 0, where θ = θ 11 θ 01, and h

K = θ h + ∞ ∫ ∫ ∫ ∫ ψ (x, x 1 0

## (B.7)

∞ 0 h ∞ 0 0 0 2, y 1, y 2 ) g F (x 1, y 1) g M (x 2, y 2) dx 1 dx 2 dy 1 dy 2 0 ∫ ∫ ψ (0, x 2, 0, y 2 ) g M (x 2, y 2) dx 2 dy 2.

Proof of Theorem 1 By Assumption 1 and (2.2)

U(z) = v (H(z), W(z)) ε (z).

## (C.1)

The proof is completely analogous to the proof of Theorem 7 in Dagsvik (1994), but for the sake of completeness we outline the proof here.

Assume that {(H(z), W(z), ε(z)), z=1,2,…} are realizations of a Poisson process on   0, h   × R 2 + with intensity measure as in (2.3).

Let  θ g(h, w)dh dw d µ (h, w) =  1  1 − θ 1

## (C.2)

when h > 0, w > 0 when h = w = 0.

Let A be a Borel set on   0, h   × R +, and define

## (C.3)

U A = max z (ψ (H(z), W(z)) ε (z)) subject to (H(z), W(z)) ∈ A.

U A is the highest utility the agent can attain, subject to (H(z), W(z))∈A. We shall now derive the c.d.f. of U A. Let

## (C.4)

{ } B = (h, w, ε): v(h, w) ε > u, h, w ∈ A,(h, w, ε) ∈   0, h   × R 2 +, and let N(B) be the number of Poisson points within B. By the Poisson law

P (N(B) = n) =

## (C.5)

Λ (B) n exp (−Λ (B)) n!

where Λ (B) = EN(B), and is given by

## (C.6)

Λ (B) = ∫ d λ (h, w, ε) =

## B

∫ ∫ d µ (x, y) ε − 2 d ε = (x,y) ∈ A, ψ (x,y) ε> u 1 ψ (x, y)d µ (x, y) u A ∫

Now it follows from (C.5) P (U A ≤ u) = P (There are no points of the Poisson processin B)

## (C.7)

 1  = P (N(B) = 0) = exp (−Λ (B)) = exp  − ∫ ψ (x, y)d µ (x, y)   u A  Eq. (C.7) proves that U A is type I extreme value distributed. 10 Let A be the complement of A. Since the Poisson realizations are independently distributed, it follows that U A and U A are independent and type I extreme value distributed.

Let ẑ be the index of the alternative that maximizes utility, i.e., ψ (H (z ˆ), W (z ˆ)) ε (z ˆ) = max z (ψ (H(z), W(z)) ε (z)).

## (C.8)

Obviously

## (C.9)

( ) P (H (z ˆ), W (z ˆ)) ∈ A = P (U A = max z (ψ (H(z), W(z)) ε (z)) = P (U A > U A) From (C.7) it follows by straight forward calculus that

## P (U A > U A) =

## (C.10)

∫ d µ (x, y)

## A

∫ d µ (x, y) .

## R 2 +

Hence, with A = (0, h] × (0, w], we get from (C.10) that hw Φ (h, w)P (H (z ˆ) ≤ h, W (z ˆ) ≤ w) =

## (C.11)

∫ ∫ ψ (x, y)d µ (x, y) 0 0 ∫ ψ (x, y)d µ (x, y) .

## R 2 +

From (C.11) it follows that for h > 0, w > 0 ϕ (h, w) =

## (C.12)

θ 1 ψ (h, w)g(h, w) ∫ ψ (x, y)d µ (x, y)

## R 2 +

which yields (2.5).

## Q.E.D.

Proof of Theorem 2 Assume first that Assumption 4 holds. In this case leisure L is kept fixed, and we shall for simplicity drop it in the notation, i.e., we write v (C, h) = v(C) and ϕ% (C 1, L;C 2, L) = ϕ% (C 1, C 2). In this case we can write

## (C.13)

ϕ% (C 1 ,C 2) = F (v (C 1) v (C 2)) where

F (y) =

## (C.14)

y 1 + y for y > 0. Recall also that the input stimuli (consumption C), is measured on a ratio scale. Hence, Theorem 14.19 in Falmagne, p. 338, (see also his discussion on an application following the theorem) implies that

## (C.15)

 β 1 (C 1 α 1 − 1) β% 1 (C α 2 1 − 1)   % ϕ (C 1 ,C 2) = F *  −   α 1 α 1   where β 1 > 0, β 2 > 0, and α are constants, and F * is a strictly increasing continuous function. 11 Recall, however, that α, β 1 and β% 1 may depend on L. Since C 1 and C 2 can attain any positive value and can vary independently, it follows that the domain of F * must be R. Also the balance condition ~ C, C + ϕ ϕ

## (1 2) ~ (C 2, C 1) = 1

~ (C, C) = 0. 5, for all C, which by (C.15) must hold. In particular with C 1 = C 2 = C, we obtain that ϕ ( ) implies that β 1 = β% 1 ≡ β 1. Let M (x) = F −1 F * (x). Since F * is continuous, and F is continuous and strictly increasing, it follows that M(x) is continuous. Thus, from (C.14) and (C.15) we get that

## (C.16)

 β 1 (C 1 α 1 − 1) β 1 (C α 2 1 − 1)  v (C) 1  =

## M 

.

−   v (C 2) α 1 α 1   In particular, with C 2 = 1, we obtain

## (C.17)

 β 1 (C 1 α 1 − 1)  .

v (C 1) = v(1) M    α 1  

By letting x = β 1 (C 1 α 1 − 1) α 1 − β 1 (C α 2 1 − 1) α 1 and y = β 1 (C α 2 1 − 1) α 1 , (C.16) and (C.17) lead to the following functional equation M (x) M (y) = M (x + y)

## (C.18)

for x, y ∈ R. But (C.18) is the well-known Cauchy equation which solution is the exponential function, cf. Theorem 3.2 and Remark 3.3 in Falmagne (1985), p. 82. Consequently, it follows from (C.18) that log v(C) = γ 1 + β 1 (C α 1 − 1) α 1

## (C.19)

where γ 1 is a constant. We now need to re-enter L into the notation. Thus, (C.19) will now be written as  C α 1 (L) − 1  log v (C,1 − L) = γ 1 (L) + β 1 (L)  ,  α 1 (L) 

## (C.20)

since α 1 and β 1 may depend on L, and where total number of feasible hours is normalized to one. In a completely analogous way we get from Assumption 5 that  L α 2 (C) − 1  log v (C,1 − L) = γ 2 (C) + β 2 (C)    α 2 (C) 

## (C.21)

where γ 2 (C), β 2 (C) and α 2 (C) are unspecified functions of C. The remaining part of the proof will be divided into 6 cases.

Case (i): α 1 (L) = α 2 (C) = 0. In this case (C.20) and (C.21) imply that

## (C.22)

γ 1 (L) + β 1 (L) log C = γ 2 (C) + β 2 (C) log L.

We can write β 1 (L) = β 1 * + β% 1 (L) and β 2 (C) = β * 2 + β% 2 (C) where β 1 * and β *2 are constants. This implies

## (C.23)

γ 1 (L) + β 1 * log C + β% 1 (L) log C = γ 2 (C) + β * 2 log L + β% 2 (C) log L.

Evidently, (C.23) implies that γ 1 (L) = β * 2 log L, γ 2 (C) = β 1 * log C, β% 1 (L) = β 3 log L and β% 2 (C) = β 3 log C where β 3 is a constant. Hence

## (C.24)

log v (C,1 − L) = β * 2 log L + β 1 * log C + β 3 log L log C.

Case (ii): α 1 (L) ≠ 0, α 2 (C) ≠ 0, γ 1 (L) and γ 2 (C) are not constants. In this case (C.20) and (C.21) imply a relation of the form

## (C.25)

γ 1 (L) + β 1 * C α 1 (L) + β 1 (L)C α 1 (L) = γ 2 (C) + β * 2 L α 2 (C) + β 2 (C)L α 2 (C) where β 1 (L) and γ 1 (L) are zero or depend on L and γ 2 (C) and β 2 (C) are zero or depend on C. The only term on the right hand side of (C.25) that can vary solely with L is the term β *2 L α 2 (C) when α 2 (C) is a constant, α 2. Similarly, since γ 2 (C) vary with C it follows that α 1 (L) must be a constant, α 1. This implies that γ 1 (L) = β * 2 L α 2, γ 2 (C) = β 1 * C α 1 and β 1 (L)C α 1 = β 2 (C)L α 2 which imply that β 1 (L)C α 1 = β 2 (C)L α 2 = β 3 C α 1 L α 2 where β 3 is a constant.

Case (iii): α 1 (L) ≠ 0, α 2 (C) ≠ 0, γ 1 (L) is a constant, γ 2 (C) is not a constant. Since γ 1 (L) is a constant we can without loss of generality set it equal to zero. As a result (C.25) reduces to

## (C.26)

β 1 * C α 1 (L) + β 1 (L)C α 1 (L) = γ 2 (C) + β * 2 L α 2 (C) + β 2 (C)L α 2 (C).

Since γ 2 (C) is not a constant and α 2 (L) is different from zero, then (C.26) can only hold if α 1 (L) is a constant, α 1, and γ 2 (C) = β 1 * C α 1. Hence

## (C.27)

β 1 (L)C α 1 = (β * 2 + β 2 (C)) L α 2 (C).

Note that the left hand side of (C.27) is multiplicatively separable. This can only be true if α 2 (C) is a constant, α 2, so that β 1 (L) = β 3 L α 2 for some constant β 3. But then β *2 = 0 and β 2 (C) = β 3 C α 1.

Case (iv): α 1 (L) ≠ 0, α 2 (C) ≠ 0, γ 1 (L) and γ 2 (C) are constants. In this case we can set γ 1 (L) = γ 2 (C) = 0. Then (C.25) becomes β 1 * C α 1 (L) + β 1 (L)C α 1 (L) = β * 2 L α 2 (C) + β 2 (C)L α 2 (C) which is equivalent to

## (C.28)

log (β 1 * + β 1 (L)) + α 1 (L) log C = log (β * 2 + β 2 (C)) + α 2 (C) log L.

Suppose β 1 (L) is not a constant. Then evidently (C.28) implies that log (β 1 * + β 1 (L)) = α 2 (C) log L + constant with α 2 (C) being a constant α 2, β 1 * = 0 and β 1 (L) = L α 2. Moreover, this yields that α 1 (L) is a constant, α 1, β *2 = 0 and β 2 (C) = C α 1.

In the case where both β 1 (L) and β 2 (C) are equal to zero, (C.28) implies that α 1 (L) = log L and α 2 (C) = log C, so that

## (C.29)

log v (C,1 − L) = β 3 log L ⋅ log C.

Thus this case coincides with a special case of Case (i) above.

The remaining cases are Case (v): α 1 (L) = 0, α 2 (C) ≠ 0 and Case (vi): α 1 (L) ≠ 0, α 2 (C) = 0.

The analysis of these cases is completely analogous to the previous cases and is therefore omitted. We therefore conclude that all the cases considered above yield the functional form of the theorem.

## Q.E.D.

Footnotes 1 In recent years the tax and benefit system has been simplified in many countries. Most budget sets are, however, still non-convex. 2 Alternatively, the worker may have to change the content of his current job. 3 In most of the previous work in labor supply modeling, for instance in the various applications of the Hausman type approach referred to in the introduction or in Van Soest (1994), it is (tacitly) assumed that the observed clustering of hours around so called “part-time” and “full-time” work is due to preferences. There are no restrictions on offered hours, which in the context of our framework can be interpreted as the distribution of offered hours being uniform. This can be justified if data have been generated in a free market economy with no regulation of offered hours. If offered hours are uniformly distributed, then in our framework g 2 (h) is equal to a constant and v 2 (h) is identified up to a multiplicative constant. However, it can be questioned whether the assumption of uniformly distributed offered hours is a good approximation to the conditions in the unionized and government regulated labor market in many west European countries. It seems more reasonable to assume that offered hours are determined to a large extent by institutional regulations and/or negotiations at an aggregate level and, of course, by the technology of firms. These characteristics of an unionized industrial society will typically imply that jobs with “parttime” and “full-time” hours of work are more frequently available in the labor market than jobs with other hours of work.

Some researchers, see for example Van Soest (1994) argue that one may assume that the peak at full time hours are due to preferences, since possible constraints on hours are unobserved. This argument will in general be flawed, because if in fact there are restrictions on hours of work then this may have important implications for the structural model. That it is not evident how one should deal with choice constraints is illustrated by the fact that a number of authors have demonstrated considerably ingenuity to deal with different approaches to rationing, cf. Section 2.4. 4 The observed concentrations of hours of work at “part-time” and “full-time” hours may be due to both preferences and choice constraints. See Hamermesh (1986) for a theoretical motivation for this. 5 Recall that the scale types are: Ordinal scale, Ratio scale, Interval scale and Logarithmic interval scale, cf. Falmagne (1985). 6 Stevens and others have observed the power law in innumerable experiments. Sinn (1983) has compressed the content of Stevens' Psychophysical power law into the following statement: “Equal relative changes in stimulus intensity bring about equal relative changes in sensation intensity”. 7 Although Luce (1959b) derived the power law as the functional relation between subjective continua and physical continua from the assumption of dimensional invariance, his approach nor Steven's empirical method do not apply directly to aggregate relations. Recall that the challenge faced here is to characterize choice probabilities, or equivalently, the mathematical and stochastic structure of a random utility function. If only the approach discussed by Luce (1959b) was available, then we would not be able to discriminate between specifications such as for example v 1 (C) = β C α and () v 1 (C) = m C α, where m(⋅) is an increasing function since in our context, utility, U(C,h,z), is ordinal and only determined up to a monotone transform. Thanks to the approach developed by Falmagne and Narens (cf. Falmagne, 1985, ch. 14) we are, however, able to get rather sharp results as demonstrated above. 8 The labor-supply function is h = (α 1 + α 3) + α 1 α 2 w * -α 2 I *, where w * is the marginal wage rate and I * is virtual income. Unfortunately, the functional form of (3.3) cannot be justified by theoretical arguments of the type given in Section 2.4.

The notation B j ⊃ h, means that the summation takes place across all j for which B j ⊃ h. 10 Recall that the standard type I distribution function has the form exp(-1/y), y>0, cf. Resnick (1987). There is, however, some confusion in the literature, since other authors call this distribution type III. 11 From Falmagne's Theorem 14.19 it follows that α ≥ 0. It is, however, easy to verify that the proof of the theorem also applies when α is negative.

Note that the above results do not depend on the particular structure of the function F(⋅) given by (2.11). It is sufficient that this function is strictly increasing and continuous and (2.10) holds.

## References

Aaberge, R., J.K. Dagsvik and S. Strøm (1990): Labor Supply, Income Distribution and Excess Burden of Personal Income Taxation in Sweden. Discussion Papers, no. 53, Statistics Norway.

Aaberge, R., J.K. Dagsvik and S. Strøm (1995): Labor Supply Responses and Welfare Effects of Tax

Reforms. Scandinavian Journal of Economics, 97, 635-659.

Aaberge, R., U. Colombino and S. Strøm (1999): Labor Supply in Italy: An Empirical Analysis of Joint Household Decisions, with Taxes and Quantity Constraints. Journal of Applied Econometrics, 14, 403-422.

Altonji, J.G. and C.H. Paxson (1988): Labor Supply Preferences, Hours Constraints and Hours-Wage

Trade-Offs. Journal of Labor Economics, 6, 254-276.

Anderson, I., J.K. Dagsvik, S. Strøm and T. Wennemo (1988): Non-convex Budget Sets, Hours Restrictions and Labor Supply in Sweden. Discussion Papers, Statistics Norway.

Arrufat, J.L. and A. Zabalza (1986): Female Labor supply with Taxation, Random Preferences and

Optimization Errors. Econometrica, 54, 47-63.

Barth, E. And M. Røed(2001): Norway. In C. Harmon, I. Walker and N. Westergaard-Nielsen(eds), Education and Earnings in Europe,pp.198-212, Edward Elgar, Cheltenham, UK, Northampton, MA,

## USA.

Ben-Akiva, M., N. Litinas and K. Tsunokawa (1985): Spatial choice: The Continuous Logit-Model and Distribution of Trips and Urban Densities. Transportation Research A, 19A, 119-154.

Blomquist, S. (1983): The Effect of Income Taxation on the Labor Supply of Married Men in Sweden.

Journal of Public Economics, 17, 169-197.

Blomquist, S. (1992): Estimation Methods for Male Labor Supply Functions. How to take account of

Nonlinear Taxes. Journal of Econometrics, 70, 383-405.

Breault, K.D. (1981): Modern Psychophysical Measurement of Marginal Utility: A Return to

Introspective Cardinality? Social Science Quarterly, 62, 672-684.

Burtless, G. and J.A. Hausmann (1978): The Effects of Taxation on Labor Supply. Journal of Political

Economy, 86, 1103-1130.

Dagsvik, J.K. (1994): Discrete and Continuous Choice, Max-stable Processes and Independence from

Irrelevant Attributes. Econometrica, 62, 1179-1205.

Dagsvik, J.K. (2000): Aggregation in Matching Markets. International Economic Review, 41, 27-57.

Dagsvik, J.K. and S. Strøm (1997): A Framework for Labor Supply Analysis in the Presence of Complicated Budget Restrictions and Qualitative Opportunity Aspects. Memorandum from Department of Economics, University of Oslo, No 22.

Dagsvik, J.K. and S. Strøm (2002): Analyzing Labor Supply Behavior with Latent Job Opportunity Sets and Institutional Choice Constraints. Working Paper no. 15/2002, International Centre for

Economic Research, Turin, Italy.

Dickens, W. and S. Lundberg (1993): Hours Restrictions and Labor Supply. International Economic Review, 34, 169-191. Edin, P.-A. and Zetterberg, J. (1992): Inter-Industry Wage Differentials: Evidence from Sweden and a Comparison with the United States, American Economic Review 82, 5: 1341-1349. Falmagne, J.C. (1985): Elements of psychophysical theory. Oxford University Press, New York. Hamermesh, D.S. (1986): Incentives for the Homogenization of Time Use. In B. Belassa and H. Giersch (eds.), Economic Incentives, pp. 124-139, Macmillan Press, Ltd., London. Hausman, J.A. (1980): The Effects of Wages, Taxes and Fixed Costs on Women's Labor Force Participation. Journal of Public Economics, 14, 161-192. Hausman, J.A. (1981): Labor Supply. In H. Aaron and J. Pechman (eds.), How Taxes Affect Behavior, Washington, D.C.: Brookings Institution. Hausman, J.A. (1985): The Econometrics of Non-Linear Budget Sets. Econometrica, 53, 1255-1282. Hausman, J.A. and P. Ruud (1984): Family Labor Supply with Taxes. American Economic Review, 74, 242-253. Heckman, J.J. and G. Sedlacek (1990): Self-Selection and the Distribution of Hourly Wages. Journal of Labor Economics, 8, S329-S363. Ilmakunnas, S. and S. Pudney (1990): A Model of Female Labour Supply in the Presence of Hours Restrictions. Journal of Public Economics, 41, 183-210. Kapteyn, A., P. Kooreman and A. van Soest (1990): Quantity Rationing and Concavity in a Flexible Household Labor Supply Model. The Review of Economics and Statistics, 62, 55-62. Karlin, S. (1966): A first course in stochastic processes. Academic Press, New York Kohlase, J.E. (1986): Labor Supply and Housing Demand for One-and Two-earners Households. The Review of Economics and Statistics, 58, 48-56. Krueger, A.B. and Summers, L.H. (1988): Efficiency Wages and the Inter-Industry Wage Structure, Econometrica, 56, 2: 259-293. Luce, R.D. (1959a): Individual choice behavior. Wiley, New york. Luce, R.D. (1959b): On the Possible Psychophysical Laws. Psychological Review, 66, 81-95. Magnac, T. (1991): Segmented or Competitive Labor Markets? Econometrica, 59, 165-187. McFadden, D. (1978): Modelling the Choice of Residential Location. In A. Karlquist, L. Lundquist, F, Snickars and J.J. Weibull (eds.), Spatial Interaction Theory and Planning Models, North Holland, Amsterdam. Moffitt, R. (1984): The Estimation of a Joint Wage Hours Labor Supply Model. Journal of Labor Economics, 2, 550-566.

Nakamura, A. and M. Nakamura (1981): A Comparison of the Labor Force Behavior of Married Women in the United States and Canada, with Special Attention to the Impact of Income Taxes. Econometrica, 49, 451-488. Ransom, M.R. (1987): An Empirical Model of Discrete and Continuous Choice in Family Labor Supply. The Review of Economics and Statistics, 59, 465-472. Resnick, S. (1987): Extreme value, regular variation and point processes. Springer Verlag, New York. Rosen, H.S. (1976): Taxes in a Labor Supply Model with Joint Wage-Hours Determination. Econometrica, 44, 485-508. Sinn, H.-W. (1983): Economic decisions under uncertainty. North-Holland, Amsterdam. Statistics Norway (1994): Survey of Income and Wealth. www.ssb.no/emner/05/01/ Statistics Norway (1995): Level of Living Conditions. www.ssb.no/emner/00/02/ Stevens, S.S. (1975): Psychophysics: Introduction to its perceptual neural, and social prospects, Wiley, New York. Tversky, A. (1969): Intransitivity of Preferences. Psychological Review, 76, 31-48. Thurstone, L.L. (1927: A Law of Comparative Judgment. Psychological Review, 34, 273-286. van Soest, A. (1994): Structural Models of Family Labor Supply. A Discrete Choice Approach. The Journal of Human Resources, XXX, 63-88. Wales, T.J. and A.D. Woodland (1979): Labor Supply and Progressive Taxes. Review of Economic Studies, 46, 83-95.
