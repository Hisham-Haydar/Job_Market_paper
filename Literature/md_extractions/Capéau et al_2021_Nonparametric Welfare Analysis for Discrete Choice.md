# Discrete Choice: Levels and Differences of

Individual and Social Welfare

## Abstract

Empirical welfare analyses often impose stringent parametric assumptions on individuals’ preferences and neglect unobserved preference heterogeneity. In this paper, we develop a framework to conduct individual and social welfare analysis for discrete choice that does not suffer from these drawbacks. We first adapt the broad class of individual welfare measures introduced by Fleurbaey (2009) to settings where individual choice is discrete. Allowing for unrestricted, unobserved preference heterogeneity, these measures become random variables. We then show that the distribution of these objects can be derived from choice probabilities, which can be estimated nonparametrically from cross-sectional data. In addition, we derive nonparametric results for the joint distribution of welfare and welfare differences, as well as for social welfare. The former is an important tool in determining whether those who benefit from a price change belong disproportionately to those who were initially well-off. An empirical application illustrates the methods.

JEL-Codes: C140, C350, D120, D630, H220, I310.

Keywords: discrete choice, nonparametric welfare analysis, individual welfare, social welfare,

money metric utility, compensating variation, equivalent variation.

Bart Capéau

Department of Economics

KU Leuven / Belgium bart.capeau@kuleuven.be

Liebrecht De Sadeleer

Department of Economics

KU Leuven / Belgium liebrecht.desadeleer@kuleuven.be

Sebastiaan Maes

Department of Economics

KU Leuven / Belgium sebastiaan.maes@kuleuven.be

André Decoster

Department of Economics

KU Leuven / Belgium andre.decoster@kuleuven.be 3 rd May 2021 We thank Debopam Bhattacharya, Geert Dhaene, Erik Schokkaert, and Frederic Vermeulen, as well as conference and workshop participants at KU Leuven, IAAE, IIPF, and NESG for useful comments on previous versions of this paper. We are grateful to Peter Haan for providing us with a tax-benefit calculator for Germany. Bart Capéau acknowledges support from the FWO and the F.R.S.-FNRS (project number EOS 30544469). Liebrecht De Sadeleer acknowledges support from the FWO (project number G073020N). Sebastiaan Maes benefited from a PhD Fellowship of the FWO. The results and their interpretation are the authors’ sole responsibilities.

## Introduction

Discrete choice random utility models (DC-RUMs) have a long tradition in both theoretical and applied microeconometric research. Since the pioneering work of McFadden (1974), these models have been applied to a wide range of problems in transportation, education, health care, industrial organisation, marketing, labour, and public finance. This success can be explained by DC-RUMs’ ability to model individual demand among a discrete set of alternatives in a flexible way, allowing for the presence of unobserved preference heterogeneity. Some models within this class, such as the binary and multinomial logit models, also yield convenient closed-form choice probabilities, which considerably reduces the computational burden in both estimation and simulation (for a comprehensive overview, see Train, 2003). These parametric models are, therefore, widely used in empirical research. The structural modelling of individual preferences in DC-RUMs renders this class of models especially suitable for the welfare analysis of price changes. In such an endeavour, the use of welfare measures (metrics) based on the expenditure function, the so-called money metric utilities (MMUs), is a wellestablished practice (for seminal contributions, see Diamond and McFadden, 1974; Dixit, 1975; King, 1983). Indeed, the reporting of deadweight losses, compensating variations (CV), and equivalent variations (EV), which are all related to the expenditure function, are ubiquitous in the applied welfare literature. MMUs facilitate interpersonal comparisons of welfare in the presence of individual preference heterogeneity over important life dimensions such as health, housing quality, emotional well-being, and material welfare. In DC-RUMs, preferences are random from the point of view of the econometrician. Therefore, preference-based welfare measures also become stochastic objects, which complicates the analysis considerably (for an early discussion, see Small and Rosen, 1981). Over the last fifteen years, a methodological literature has emerged that derives closed-form expressions for the distribution of the CV and EV, which are both measures of changes in welfare, under ever less parametric assumptions on the nature of individuals’ preferences. 1 For the class of additive DC-RUMs, Dagsvik and Karlström (2005) provide expressions for the distribution of the CV based on compensated (Hicksian) choice probabilities. The authors provide analytical results for models where unobserved heterogeneity is generalised extreme value distributed. Alternatively, de Palma and Kilani (2011) advance a direct approach for this class, in which they express this distribution in terms of uncompensated (Marshallian) choice probabilities. More recently, Bhattacharya (2015, 2018) showed that the marginal distributions of the CV and EV can be written as a functional of uncompensated choice probabilities,

1 Before, no closed-form expressions existed, even for the expected values of the CV and EV. Therefore, researchers had to resort to approximations, except for the most simple of DC-RUMs in which individuals have constant marginal utility of income and unobserved heterogeneity is additive and generalised extreme value distributed (Small and Rosen, 1981; McFadden, 1999). These approximations are either biased (Morey et al., 1993), rather uninformative (Herriges and Kling, 1999), or computationally burdensome (McFadden, 1999).

even when unobserved heterogeneity is essentially unrestricted, and therefore possibly nonadditive. 2 His results readily imply that these objects are nonparametrically identified from cross-sectional data with sufficient relative price variation. The analysis of levels of welfare in DC-RUMs, however, has received much less attention from econometricians. Characterising these levels is of first-order importance to applied welfare analysis for at least three reasons. First, knowledge on these levels enables researchers to rank individuals according to their well-being in any given situation, identifying those who are well-off from those who are poor. Second, in aggregating welfare levels across individuals, overall social welfare can be calculated and compared between two situations. Third, joint knowledge on levels and differences of welfare enables the investigation of the association between individuals’ gains or losses from a price change and their position in terms of initial welfare. This allows for the assessment of, for example, whether the winners of a price change belong disproportionately to those who were initially well-off. In recent years, the fairness literature has made substantial progress in developing a comprehensive theoretical framework that encompasses both the classical MMUs (Samuelson, 1974), adaptations of other measures like Pazner’s (1979) ray utilities, and measures like the equivalent income and wage metrics (among others, see Pencavel, 1977; Fleurbaey, 2006; Fleurbaey, 2007; Fleurbaey and Gaulier, 2009; Fleurbaey, 2009; Fleurbaey and Blanchet, 2013; Decancq et al., 2015; and Fleurbaey and Maniquet, 2017). A large subset of these measures cardinalise preferences by associating their indifference sets with members of a family of nested opportunity sets; i.e. a lower ranked indifference set is associated with a smaller opportunity set. The sizes of those budget sets are argued to be an ethically more meaningful basis for interpersonal comparisons of well-being than income or reports on subjective satisfaction levels. Indeed, contrary to income and subjective satisfaction, such measures ensure that individuals with the same preferences and in a situation which makes them indifferent among each other are always considered to be equally well-off. We call these metrics nested opportunity set (NOS) measures and show how they relate to what is typically observed in cross-sectional and panel data.

Contributions We adapt the class of NOS measures (Fleurbaey, 2009, Fleurbaey and Maniquet, 2017) to a setting where the choice set is discrete instead of continuous. This allows us to study welfare levels and differences in DC-RUMs, taking into account unrestricted, unobserved heterogeneity in individuals’ preferences. We then prove that the marginal distribution of NOS measures can be recovered nonparametrically from cross-sectional data by evaluating the observed choice probabilities at counterfactual prices. This allows researchers to study levels of individual welfare in any given situation. Likewise, we show that the joint distribution of welfare levels and welfare differences can 2 This result only holds for price changes. When quality changes occur, Bhattacharya (2018) demonstrates that functionals of the choice probabilities only set-identify the distribution of the CV (or EV).

be recovered nonparametrically from panel data by evaluating the observed transition probabilities at counterfactual prices. 3 Building on these two results, we are able to nonparametrically characterise levels and differences in aggregate welfare for any additively separable social welfare function. In addition, we show that Samuelson’s (1974) money metric utilities (MMUs) are within the class of the discrete NOS measures, and use them as a leading example to illustrate our approach. This also implies that we can specialise our results to cases where welfare differences are measured by the CV or EV. In doing so, we generalise the results of Dagsvik and Karlström (2005) and de Palma and Kilani (2011) to settings where unobserved heterogeneity is essentially unrestricted. As a by-product, we also present all our results conditional on the endogenous pre-or post-price change choices, which allows researchers to take the additional information conveyed by the observed choices into account. This conditioning might also be important from a political economy perspective. These results allow researchers to conduct individual and social welfare analyses without resorting to stringent parametric assumptions on preferences or unobserved heterogeneity. Our identificationresults are constructive and can be implemented in empirical work using only nonparametric regression. We also demonstrate how Boole-Fréchet inequalities (Fréchet, 1935) and stochastic revealed preference restrictions can be exploited to construct bounds on the transition probabilities in the common event when only cross-sectional data is available. These bounds are functionals of the choice probabilities and are, as such, straightforward to implement. They can be readily used to set-identify the concepts that are expressed in terms of transition probabilities. To illustrate the empirical usefulness of our results, we revisit the classical trade-off between leisure and consumption. For this purpose, we make use of micro-data from the 2018 wave of the German Socio-Economic Panel (SOEP), which contains detailed information on households’ demographics, labour supply, wages, and out-of-work income. Single females’ labour supply is modelled as a choice between three discrete alternatives: non-working, part-time employment, and full-time employment. Using a MMU, we present nonparametric, distributional estimates of individual and social welfare for the tax schedule that is currently in place in Germany. We also study the effects of replacing this nonlinear and progressive schedule with a basic income flat tax. In the baseline, we find that for approximately 25% of the single females in our estimation sample, the distribution of the MMU is a step function. This means that we can determine their welfare level exactly. Aggregating these individual distributions in groups based on gross hourly wage quartiles, we find that the distribution of high-wage individuals who work full-time tends to first-order dominate that of those who are non-working or work part-time. The reverse is true for low-wage individuals. This is explained by a mismatch between these individuals’ preferences and wages. Moreover,

3 These transition probabilities are derived under the assumption that (unobserved) individual preferences are unaltered by the price change. Alternatively, Dagsvik (2002) and Delle Site and Salucci (2013) consider models where there is imperfect correlation in unobserved heterogeneity before and after the change.

irrespective of the baseline choice, the distribution of high-wage individuals dominates that of the groups with lower wages. For the latter, the distributions are more intermingled, which is suggestive evidence that besides wages, (unobserved) preferences do play an important role in assessing the welfare level of individuals. For the entire population of single females, the distribution of welfare in the reform first-order dominates that in the baseline. 4 This does not imply, however, that every individual gains from the reform. Around 15% of single females find their welfare diminished; this is especially the case for those that are well-off in the baseline. Large gains are more prevalent among those that were initially poor. Among the bottom two-thirds of the population in terms of baseline welfare, almost 98% advance as a result of the reform. Approximately half of the single females gain up to 200 euro on a monthly basis.

Other related literature Over the last decades, several semiparametric methods have been developed to relax functional form assumptions on either deterministic preferences or the distribution of unobserved heterogeneity in DC-RUMs (e.g., for early results see Manski, 1975; Matzkin, 1991; and Klein and Spady, 1993). Other contributions introduce entirely nonparametric methods that do not impose functional form restrictions on either of these components for this class of models, based on either shape restrictions (e.g., see Matzkin, 1993) or the availability of a large-support special regressor (e.g., see Lewbel, 2000 and Briesch et al., 2010). The approach we follow in this paper deviates from this literature as our objective is not to recover deterministic preferences and the distribution of unobserved heterogeneity, but instead to identify individual welfare measures which are functions of both these model primitives. Another strand of literature focuses on the nonparametric identification of counterfactual choices and welfare under unobserved heterogeneity in models where demand is continuous instead of discrete. Most results exploit the smoothness of the underlying individual demand functions to arrive at Slutsky-like restrictions on average and quantile demands (e.g., see Dette et al., 2016; Hausman and Newey, 2016; Blundell et al., 2017; and Hoderlein and Vanhems, 2018). Other results exploit the axioms of revealed preference (RP) to attain identification under the presence of unobserved heterogeneity (e.g., see Blundell et al., 2014; and Cosaert and Demuynck, 2018). In contrast to our results, however, the availability of cross-sectional and short panel data is generally not sufficient to point-identify the distribution of welfare levels and differences in settings where demand is continuous and unobserved heterogeneity is unrestricted. Finally, this paper contributes to the literature that applies NOS measures empirically. Using SOEP microdata, Decoster and Haan (2015) estimate a parameasure DC-RUM of labour supply and con-

4 This is partially due to the fact that we constructed the reform to be revenue-neutral for the entire SOEP sample.

Therefore, revenue neutrality does not necessarily hold for our subsample of single females.

struct rankings of households based on NOS measures. Carpantier and Sapata (2016) extend the approach of Decoster and Haan (2015) by integrating unobserved preference heterogeneity through a numerical procedure (comparable to the approach of Herriges and Kling (1999) for welfare differences). Our results show that the parametric assumptions imposed in these papers are not necessary to obtain identification. The remainder of this paper is organised as follows. In the second section, we introduce the class of NOS welfare measures originally developed by Fleurbaey (2009) for settings where choice is continuous. In section three, our conceptual framework is laid out. We first specify the DC-RUM and impose some mild restrictions on individuals’ preferences. We then adapt the class of NOS welfare measures to this discrete setting. Since preferences are random from the point of view of the econometrician, these welfare measures are also random variables. In the fourth section, we present our main results. We derive the distribution of the NOS measures, either conditional or unconditional on the initial and final choices. We also study welfare differences induced by a price change and derive the joint distribution of welfare in the initial choice and these welfare differences, again either conditional or unconditional on the initial and final choices. Moreover, we discuss how measures for social welfare can be constructed from these results. In section five, we discuss how the choice and transition probabilities by which the welfare concepts are identified, can be retrieved from cross-sectional data. In the sixth section, we illustrate our results by means of an application on female labour supply, using the German SOEP microdata. The final section contains concluding remarks.

2

NOS welfare measures in a continuous setting In this section, we briefly explain and motivate the class of NOS welfare measures, which have been introduced by Fleurbaey (2009) for settings where choice is continuous. These measures cardinalise preferences by associating each indifference set with a member of a family of nested opportunity sets, which is common for all individuals. A lower ranked indifference set is associated with a smaller set from that family, such that the size of the opportunity set acts as a measure of individual well-being, respecting that individual’s preferences. Formally, let B ⊆ R n + be the set of all bundles b an agent can possibly obtain, and let {B λ (B | λ ∈ Λ ⊆ R} denote a family of nested budget sets indexed with a parameter λ such that λ i < λ j =⇒ B λ i (B λ j. Given a well-behaved utility function U (b): B → R, the NOS welfare measure evaluated in a bundle b ∈ B is then defined as W (b) = max λ | U (b) ≥ max

U (b 0), 0 b ∈B λ λ (1) that is, the largest value of λ — or, equivalently, the largest opportunity set — for which the individual still weakly prefers bundle b above all bundles b 0 in the virtual opportunity set B λ. 5 5 Note that the discussion here is informal as additional assumptions are needed to guarantee the existence and the uniqueness of the NOS welfare measure. A more rigorous treatment is provided in Section 3.2.

good 2 good 2

## R

## R 0

B λ 2 y x 0

M M U p R ref (x)

B λ 1

M M U p R ref (x) x good 1 good 1 (a) NOS as a measure of well-being (b) The MMU measure Figure 1: NOS welfare measures in a continuous choice setting This definition is illustrated by means of a classical trade-off between two goods in Figure 1a. Suppose first an individual obtains a bundle x, and let the thick blue line denote her indifference curve passing through x. This indifference curve is associated with the opportunity set B λ 1, which is shaded in dark red. In accordance with the definition in Equation (1), this set is designed such that the individual could obtain, at best, a bundle equally as good as x, when she would be faced with the opportunity set B λ 1. Suppose now that the individual obtains a bundle y, which is better than x, according to her own preferences. Then the associated opportunity set B λ 2, which is shaded in light red, is again such that the best bundle in this set is equally good as y, and includes the set B λ 1. From this illustration, it is clear that the size of these opportunity sets serves as a measure of individual well-being that respects preferences, in the sense that the well-being level of an individual in situation y is higher than the well-being level in situation x, if and only if that individual prefers y to x. The size of an opportunity set is measured by its indexing parameter λ.

Example: the MMU measures One important set of welfare measures within the NOS class is the set of money metric utilities (MMUs) (Samuelson, 1974). In this case, the NOS are of the form n o B λ ≡ b ∈ B b 0 p ref ≤ λ, (2) where p ref is a vector of reference prices that are fixed by the researcher. In this specification, the indexing parameter λ can be interpreted as a monetary amount. Applying the definition in Equation (1), we find that the MMU measure evaluated in a bundle x, denoted by M M U p ref (x), measures well-being by the maximal monetary amount that can be granted to an individual faced with reference prices p ref, such that she would at most be equally well-off as in

point x. This coincides with the expenditure function representation of preferences, which is how MMUs were originally presented in the literature. In Figure 1b, this is illustrated by means of a classical trade-off between two goods. The slope of the dashed lines equals minus the reference price p ref for good 1, as good 2 serves as numeraire 1 0 here. The welfare levels M M U p R ref (x) of an individual with preferences R and M M U p R ref (x) of an individual with preferences R 0 are determined such that the best point in the opportunity set is a point on the indifference curve through their actual, common situation x (denoted by the red and blue point, respectively). With the chosen reference price, the individual with preference R 0 is better off than the one with preferences R. Other examples of NOS measures are the ray utilities of Pazner (1979) and the equivalent income metrics introduced in Decancq et al. (2015). In the former, one fixes a reference bundle b ref and determines the NOS as the sets of bundles that lie on the ray from the origin through this n o reference bundle, that is B λ = b ∈ B | b = αb ref, α ≤ λ. In the latter, one measures well-being by the minimal amount of a numeraire good which is needed, given a reference value for the other commodities or dimensions of well-being in order to make an agent equally well-off as in her actual situation. We discuss the equivalent income metrics in more detail in Appendix A.1.

3

Conceptual framework Our conceptual framework is similar to that of Bhattacharya (2015, 2018) and allows for unrestricted, unobserved heterogeneity in DC-RUMs. As this set-up does not impose any restrictions on observed individual characteristics, all results in this paper can be thought of as being conditional on these covariates.

3.1

Discrete choice model

Preferences Let Ω denote the universe of preference types and let the associated probability space (Ω, F, Pr ω [{ω | ·}]) represent the distribution of these preference types in the population. 6 Every preference type can be thought of as a different individual, who has idiosyncratic preferences over a finite (and common) set of alternatives C, with |C|:= n ∈ N 0, and a numeraire. These idiosyncratic preferences are assumed to be representable by a utility function U c ω (y − p c):= U (y − p c, c, ω): R × C × Ω → R, in which y denotes exogenous income and p c the price of alternative c ∈ C. 7 A given set of prices for all alternatives, (p c, c ∈ C), are recollected in a vector denoted by p and we will call (p, y) a budget set. Note that our formulation of preferences is very flexible as it allows them to differ arbitrarily across

6 In the remainder of the paper, we will abbreviate Pr ω [{ω | ·}] as Pr [{·}]. 7 For the sake of technical rigour, U (y − p c, c, ·) is required to be a F-measurable function.

ω

individuals. The only economically substantial restriction we will impose on this function is that utility is continuous and strictly increasing in the numeraire y − p.

Assumption 1 Individual preferences are represented by a utility function U c ω (y − p c) that is continuous and strictly increasing in the numeraire for every preference type ω ∈ Ω and every alternative c ∈ C. Moreover, preferences satisfy the following regularity conditions: (R1) For each pair of alternatives c, c 0 ∈ C, and for each fixed y and p c, it holds that U c ω (y − p c) > lim p c 0 →∞ U c ω 0 (y − p c 0) and that U c ω (y − p c) < lim p c 0 →−∞ U c ω 0 (y − p c 0 ). (R2) For every budget set (p, y), the set of types which are indifferent between two or more alternatives in the choice set C has probability measure zero.

This assumption is ubiquitous in empirical work that employs (semi)parametric DC-RUMs. Monotonicity in the numeraire establishes the existence and uniqueness of our welfare measures and yields stochastic revealed preference conditions that we will exploit to obtain the identification results. Regularity condition (R1) ensures that when the price of a given alternative goes to infinity, it will never be preferred above another alternative with a finite price. Analogously, when the price of a given alternative goes to minus infinity, or residual income in that alternative goes to plus infinity, it will always be preferred above another alternative with a finite price. The negligibility of indifferences between alternatives (R2) ensures that no tie-breaking rule has to be established. In addition, we also assume that the distribution of the preference types, denoted by F (ω), is independent of the budget set (p, y).

Assumption 2 The distribution of unobserved heterogeneity F (ω) is independent of prices p and exogenous income y: i.e. F (ω | p, y) = F (ω).

The exogeneity of budget sets is a strong, but standard, assumption in the literature on nonparametric identification of individual demand and welfare (e.g., see Hausman and Newey, 2016). Indeed, to the best of our knowledge, there are no theoretical results that allow for general forms of endogeneity in the presence of unrestricted, unobserved heterogeneity. Some forms of endogeneity, however, can be mitigated by using a control function approach (see Section 5).

Individual choice behaviour Finally, we assume that observed choice behaviour is actually generated by a DC-RUM (for a detailed technical overview on RUMs, see McFadden (1981, 2005)). This assumption entails that an individual ω chooses a given alternative i, if and only if this alternative yields the highest utility among the elements in her choice set C.

Assumption 3 Let J ω (p, y) ≡ J(p, y, ω): R n+1 × Ω → C denote the individual demand function.

It holds that J ω (p, y) = i ⇐⇒ U i ω (y − p i) ≥ max c6 = i {U c ω (y − p c )}.

Note that individual demand is single-valued with probability one as one can neglect indifferences

between alternatives by regularity condition (R2) in Assumption 1.

Choice and transition probabilities The individual choices induced by a DC-RUM are stochastic from the point of view of the econometrician, as the preferences types are non-observable. When this random variation is averaged out across types, one obtains a set {P i (p, y)} i∈C of uncompensated (Marshallian) conditional choice probabilities,

P i (p, y) = Pr ω

## Z

= ω

## Z

= ω n U i ω (y − p i) ≥ max {U c ω (y − p c )} o c6 = i I U i ω (y − p i) ≥ max {U c ω (y − p c )} dF (ω | p, y) (3) c6 = i I [J ω (p, y) = i] dF (ω), where I[·] denotes the indicator function. 8 The last expression asymptotically coincides with the observed choice frequency for every alternative i ∈ C, conditional on the budget set (p, y). 9 If cross-sectional data contains enough relative price and exogenous income variation, these objects are nonparametrically estimable. 10 Another concept induced by DC-RUMs is the set {P i,j (p, p 0, y)} i,j∈C of uncompensated conditional transition probabilities. These probabilities are formally defined as 0

P i,j (p, p, y) = Pr n

U i ω (y ω − p i) ≥ max {U c ω (y c6 = i = Pr i = J ω (p, y), j = J ω (p 0, y) o − p c )} ∩ n

U j ω (y − p 0 j) ≥ max {U c ω (y c6 = j − p 0 c )} o ω

## Z

= ω I [J ω (p, y) = i] I J ω (p 0, y) = j dF (ω), which asymptotically coincide with the transition frequencies from alternative i to alternative j after an exogenous price change from p to p 0. 11 Naturally, if there is no price change, there are no transitions between different choices. In principle, these objects are nonparametrically estimable

8 These choice probabilities are designated conditional as they depend on a vector of prices and income. In the interest of brevity, this qualification will be dropped in the sequel. 9 This concept is also known as the average structural function (e.g., see Blundell and Powell, 2004). The asymptotic equivalence follows from the law of large numbers as the choice probabilities are essentially conditional expectation functions. 10 It is clear from the second equality in Equation (3) that these probabilities are composed of both the utility function ω U c and the distribution of unobserved heterogeneity F. As such, they are not sufficiently informative to separately identify these two model primitives. Fortunately, knowledge on such primitives is not necessary for our purposes. 11 Note, however, that transition probabilities do not impose any temporal structure. In other words, P i,j (p, p 0, y) = P j,i (p 0, p, y). Furthermore, the assumption that the exogenous income y is common to both situations with prices p and p 0 imposes no constraint. Indeed, if exogenous incomes are different when faced with prices p and p 0 (denoted by y and y 0 ), we can redefine prices and incomes in order to obtain a common exogenous income. Defining p 00 = p 0 − y 0 + y, we obtain Pr i = J ω (p, y), j = J ω (p 0, y 0) = Pr i = J ω (p, y), j = J ω (p 0 − y 0 + y, y) = P i,j (p, p 00, y). ω ω

from panel data with at least two periods. In addition, Section 5.1 shows how transition probabilities can be set-identified when only cross-sectional data is available. Implicit in our definition of the transition probabilities is the assumption that individuals’ preferences are unaffected by the price change. The perfect correlation between the preference types before and after the price change implies that transition probabilities are not simply equal to the product of their marginals: i.e. P i,j (p, p 0, y) 6 = P i (p, y)P j (p 0, y).

3.2 NOS welfare measures in a discrete choice setting

In Section 2, the family of NOS welfare measures is introduced in a setting of continuously divisible goods. In this subsection, we will redefine them rigorously for settings where choice is determined by a DC-RUM that satisfies Assumptions 1–3.

Nested opportunity sets in DC-RUMs The for all preference types ω ∈ Ω common family of nested opportunity sets is defined as follows. Let there be a closed set Λ ⊆ R, and define for every λ ∈ Λ a non-empty opportunity set B λ ⊂ R × C, such that B λ (B λ 0 if λ < λ 0, and such that with y c λ:= sup{y | (y, c) ∈ B λ} 12 and y λ:= (y 1 λ,..., y c λ,..., y n λ ): (a) λ < λ 0 =⇒    ∀c ∈ C: y λ ≤ y λ 0, c c   ∃c ∈ C: y λ < y λ 0, c c (4) (b) the function Λ → R n: λ 7→ y λ is continuous, (5) inf y c λ 0 = −∞, (6) sup y c λ = +∞.

(7) (c) for all options c 0, λ∈Λ (d) and for at least one option c, λ∈Λ Then (B λ) λ∈Λ is called a family of nested opportunity sets. Note that the family is common to all individuals. Conditions (4) and (5) ensure that the family (B λ) λ∈Λ is continuously increasing, while conditions (6) and (7) ensure that for every bundle x and preference type ω, there exists a member of the family of which all bundles are considered worse than x by ω, and one which contains a bundle considered to be better than x by ω. This latter property will prove necessary to define the welfare measure.

12 We define the supremum of the empty set in this context to be equal to −∞.

The vector y λ can be seen as the upper bound of B λ. Below, we will see that welfare measures associated to families of nested opportunity sets with the same upper bounds are identical. Hence, we will only consider opportunity sets of the form n o B λ:= (y 0, c) | c ∈ C, y 0 ∈ R, y 0 ≤ y c λ.

(8) It is often more convenient to characterise the opportunity sets in terms of virtual prices p e c (λ):= y − y c λ. In particular, we have that B λ:= (y 0, c) | c ∈ C, y 0 ∈ R, y 0 ≤ y − p e c (λ).

(9) e (λ) = p e 1 (λ),..., p e n (λ).

For future reference, we denote the vector of virtual prices as follows: p e (λ) is decreasing in λ in the Note that as y λ is increasing in λ, as described in Equation (4), p e (λ) is continuous by (5), sup λ∈Λ p e c 0 (λ) = +∞ for all c 0 by (6) and same way. Moreover, λ → p inf λ∈Λ p e c (λ) = −∞ for at least one c by (7). The fact that those virtual prices can become negative might seem strange at first. However, in a discrete choice context, one can always redefine prices and exogenous income by increasing both by an equal amount of the numeraire. As a result, negative prices can be converted into positive prices. The intuition behind the definition of nested opportunity sets can be illustrated using the famous ‘Matryoshka dolls’. If one has several boxes of different dimensions, one can measure their size in different ways. One possible way is defining the size of these boxes by the biggest Matryoshka doll of the set fitting in the box. Sets of Matryoshka dolls of different shape constitute different ‘metrics’. Analogously, we use families of nested opportunity sets to construct welfare measures. Families of opportunity sets with different shapes will define different metrics.

Welfare measures in DC-RUMs In the continuous setting, the NOS welfare measure evaluated in a bundle was defined as the largest value of λ, or the largest opportunity set B λ, such that this bundle was weakly preferred over all bundles in B λ. The same idea can be applied to a setting where choice is discrete. More precisely, we define a NOS welfare measure as n W ω (y − p k, k) = sup λ | U k ω (y − p k) ≥ λ o max U c ω (y 0), 0 (y,c)∈B λ (10) that is, the largest value of λ such that option k is weakly preferred over all bundles in B λ. Note that the dependence on the preference type ω implies that this welfare measure is a random variable 13. According to Assumption 1, the utility function is strictly increasing in the numeraire, which allows us to restate this definition in terms of the upper bound of the opportunity sets. Formally, we have 13 As the utility function U is F-measurable, W is also F-measurable.

that n W ω (y − p k, k) = sup λ | U k ω (y − p k) ≥ λ max U c ω (y 0) 0 o (y,c)∈B λ n o = sup λ | U k ω (y − p k) ≥ max max U c ω (y 0) c λ (11) y 0 ≤y c λ n o = sup λ | U k ω (y − p k) ≥ max U c ω (y c λ).

c λ This expression highlights that the value of the welfare measure only depends on the upper bound of the opportunity sets and that the assumption that the opportunity sets are of the form of (8) is not a genuine restriction. Furthermore, by conditions (6) and (7) and Assumption (R1), there exists (i) a λ min ∈ Λ such that U k ω (y − p k) ≥ max c U c ω (y c λ min ), and (ii) a λ max ∈ Λ such that U k ω (y − p k) < max c U c ω (y c λ max ). This implies that the set n o λ | U k ω (y − p k) ≥ max c U c ω (y c λ) is not empty by (i), and bounded by (ii). Moreover, by continuity of the utility function and of the function λ 7→ y λ, λ 7→ max c U c ω (y c λ) is also continuous, which implies, together with the closedness n o of Λ, that (iii) λ | U k ω (y − p k) ≥ max c U c ω (y c λ) is closed. As this set is not empty, bounded and closed, one can conclude that the suprema in Equations (10) and (11) are in fact attained and can be replaced by maxima. Equivalently, when opportunity sets are characterised in terms of virtual prices, we can write that n o W ω (y − p k, k) = max λ | U k ω (y − p k) ≥ max U c ω (y − p e c (λ)).

(12) c λ For notational convenience, the characterisation in terms of virtual prices p e c (λ) instead of the numeraire y c λ will be used in the remainder of the paper. The key insight of this paper is that the statement ‘W ω (y − p k, k) ≥ w’ is equivalent with k (at its original price) being the optimal choice among all options with a virtual vector of prices that is welfare measure specific. This result is made precise in Lemma 1. For didactic purposes, the proof is included here.

Lemma 1 ω | w ≤ W ω (y − p k, k) = ω | U k ω (y − p k) ≥ max U c ω (y − p e c (w)) c Proof. Take an arbitrary ω ∈ Ω such that w ≤ W ω (y − p k, k). Then there exists a λ ≥ w such that U k ω (y − p k) ≥ max c U c ω (y − p e c (λ)). As λ ≥ w, p e c (λ) ≤ p e c (w) for all c ∈ C and, hence, max U c ω (y − p e c (λ)) ≥ max U c ω (y − p e c (w)), c c because U c ω is an increasing function by Assumption 1. It follows that U k ω (y − p k) ≥ max U c ω (y − p e c (w)). The other inclusion follows immediately from the definition of W ω (y − p k, k).

c This equivalence is obtained without imposing any assumption on preferences besides Assumptions 1 and 2, and is, therefore, entirely nonparametric. 14 As will be shown below, its main practical implication is that the entire distribution of objects based on NOS measures can be obtained by only evaluating choice and transition probabilities at virtual prices. This entails that these distributions can be identified from cross-sectional and panel data in a nonparametric way. Figure 2 provides a graphical illustration. The choice set C consists of three options: i, j, and k. For each option, the amount of the numeraire, y − p i, y − p j, and y − p k is shown on the vertical axis. The blue points indicate the indifference set of the point (y − p k, k). Three members of a family of nested opportunity sets B λ∈Λ are shown in red. For example, all option-numeraire combinations 0 in dark red belong to B λ 1. For illustrative convenience, we choose y c λ < y c λ whenever λ < λ 0, and this for all c ∈ C. Finally, the figure shows how to calculate the NOS welfare measure for option k. The welfare measure is defined by the nested opportunity sets B λ∈Λ shown in red in the figure. The upper bound of B λ 3, consisting of the points y c λ 3, is denoted by the red dots. It is clear that λ 3 is the maximand of Equation (10) because the red dot of y j λ 3 coincides with the blue point at position j. This means that U j ω (y j λ 3) = U k ω (y − p k ), and hence W ω (y − p k, k) = λ 3 in this example.

numeraire y − p j y i λ 3 y − p i

B λ 3 y j λ 3 y − p k y k λ 3

B λ 3

B λ 3

B λ 2

B λ 2

B λ 2

B λ 1 option i

B λ 1

B λ 1 option k option j Figure 2: A graphical illustration of a NOS welfare measure in a discrete choice context

Example: the MMU measures Fix a set of n reference prices p ref, one for each option and let e c (λ) = y − λ + p ref the upper bound of the opportunity sets be y c λ = λ − p ref c, or equivalently, p c.

The crucial property is that the upper bounds increase by the same amount for every option: i.e. y c λ 1 − y c λ 2 = λ 1 − λ 2 for all c ∈ C. The MMU evaluated in option k (with price p k) at reference prices p ref is then defined as n o M M U p ω ref (y − p k, k) = max λ | U k ω (y − p k) ≥ max U c ω y − (y − λ + p ref c) c λ 14.

(13) This result is similar in nature to the result Bhattacharya (2018) obtains for the marginal distribution of the CV.

This can also be defined implicitly as U k ω (y − p k) = max U c ω M M U p ω ref (y − p k, k) − p ref.

c c Similar to the continuous case, this highlights the equivalence of the MMUs with the expenditure function representation of preferences, as each of them evaluates the expenditure function at a given set of reference prices. From Equation (13), it can be seen that M M U p ω (y − p k, k) = y if k = J ω (p, y). When the reference prices coincide with the actual prices, the level of well-being according to the MMU of the optimal choice in the actual situation is equal to the actual amount of the numeraire (see also Corollary 2 below).

4 Distribution of the NOS welfare measures, welfare differences, and social welfare As discussed before, the presence of unobserved preference heterogeneity entails that NOS welfare measures are random variables from the point of view of the econometrician. This randomness can be interpreted in two distinct ways. In the first interpretation, as the econometrician does not observe an individual’s preference type, they can only derive the distribution of welfare for this particular individual and not its exact realisation. That is, the distribution reflects uncertainty for the econometrician. In the second interpretation, an observed individual in the sample represents the class of individuals in the population that share the same observable characteristics. In this case, the distribution reflects inequality in welfare among the members of this class. Our theoretical results are valid for both interpretations. For notational convenience, we will present all our expressions in terms of the complementary cumulative distribution function (CCDF) instead of the more common cumulative distribution function (i.e. 1 − F (x) for a CDF F ). The proofs in this section and the following ones are deferred to Appendix B.

4.1

Distribution of the NOS welfare measures In this section the marginal distribution for the NOS measures is derived in terms of choice probabilities. We also provide distributional results joint with, and conditional on, the optimal observed choice. Under Assumptions 1–3, which were introduced in Section 3, we can prove the following theorem.

Theorem 1 The joint distribution of the NOS welfare measure W, evaluated in an option k with

price p k, and choosing j at prices p 0 and exogenous income y can be expressed in terms of transition probabilities as follows:

e −k (w)), y I [p k ≤ p e k (w)], Pr w ≤ W ω (y − p k, k), j = J ω (p 0, y) = P j,k p 0, (p k, p ω (14) e −k (w)) = (p e 1 (w),..., p e k−1 (w), p k, p e k+1 (w),..., p e n (w)).

where (p k, p See proof on page 47. The crucial insight here is that, by Lemma 1, the event W ω (y − p k, k) ≥ w is translated into a statement on k being optimal under virtual prices. The joint distribution in Equation (14) can, therefore, be expressed in terms of transition probabilities, evaluated at both actual prices p 0 and p k e.

and virtual prices p Theorem 1 is formulated in the most general form; it considers a joint distribution, and not a marginal nor a conditional, and allows the price at which the welfare in alternative k is evaluated, p k, to be different from the prices p 0. For example, if one wants to evaluate welfare levels after a price change from p to p 0 when only information on choices before the price changed is available, p 0 and p will typically not coincide. However, if one wants to evaluate welfare in a setting with only one actual price p 0, the latter can be set equal to the actual prices p. Usually, one wants to evaluate welfare in an optimal bundle; then k can be set equal to j in Equation 14. In Corollary 1 below, we will derive some related distributions which are more directly relevant for applied work.

e (w) depends, as explained in Section 3.2, on the specific choice of the The exact formulation of p welfare measure. Nonetheless, we can give some intuition on the role of p k and the overall course of the distribution of welfare. We know that the lower the price p k, the higher is the residual numeraire y −p k in option k and hence, the more the indifference set containing (y −p k, k) is shifted upwards in the numeraire dimension. As the indifference set is an upper bound of the (virtual) nested opportunity sets, a higher indifference set implies higher welfare. Hence, the lower price p k, the higher is the CCDF of welfare in option k and the more the distribution of welfare is shifted to the right. Now, we examine the overall course of the CCDF in more detail by considering a typical plot of the CCDF for fixed prices p k and p 0 in Figure 3a. When w is negative and large in absolute value, the p̃ c (w) are large (and positive). Hence p k ≤ p̃ k (w) and the CCDF approaches P j (p 0) as expected. As e −k (w) decreases and the probability of choosing k at prices (p k, p e −k (w)) decreases.

w increases, p Therefore, Pr ω [w ≤ W ω (y − p k, k), j = J ω (p, y)] decreases until w reaches its highest value at which point p k = p̃ k (w), called w k ∗. There the CCDF drops to zero discontinuously, as the indicator function becomes zero. This means that w k ∗ is an upper bound for welfare and that the probability distribution has a mass point. As a corollary, we can immediately derive some associated distributions, such as the marginal and

## CCDF

## CCDF

1

P j (p 0) w k ∗ welfare w ∗ (a) Unconditional CCDF w k ∗ welfare (b) Conditional CCDF Figure 3: The course of the (un)conditional CCDF of welfare conditional CCDFs, which are more relevant in empirical applications.

Corollary 1 h i Pr w ≤ W ω (y − p k, k) | j = J ω (p 0, y) = e −k (w)), y

P j,k p 0, (p k, p

P j (p 0, y) ω h i Pr w ≤ W ω (y − p k, k) | k = J ω (p, y) = e (w), y

P k min p, p (15) I [p k ≤ p e k (w)], (16)

P k (p, y) ω I [p k ≤ p e k (w)], e (w) = min(p 1, p e 1 (w)),..., min(p n, p e n (w)), where min p, p e −k (w)), y I [p k ≤ p e k (w)], Pr w ≤ W ω (y − p k, k) = P k (p k, p (17) ω and h Pr w ≤ W ω y − p J ω (p,y), J ω (p, y) ω i =

## X

e (w), y I [p k ≤ p e k (w)].

P k min p, p (18) k See proof on page 47. We find again that the different derived distributions can be expressed in terms of choice and transition probabilities. Equations (15) and (16) can be used to assess the distribution of welfare when the researcher observes which bundle is optimal and wants to take this information into account. Equation (17) describes the marginal distribution of welfare evaluated in a specific bundle, not taking into account which bundle is optimal. Finally, Equation (18) specialises this result to a setting where welfare is evaluated in the optimal bundle. A typical example of the distribution of welfare in bundle k conditional on bundle k being optimal is plotted in Figure 3b. As before, define for an option c, w c ∗ to be the highest value of w such that p c = p̃ c (w), and also define w ∗ to be min c {w c ∗ }. Then we observe that for w ≤ w ∗, p c ≤ p e c (w) for h i e (w)) = p. It follows that Pr ω w ≤ W ω (y − p k, k) | k = J ω (p, y) = 1.

all c, and hence, min(p, p

Hence, w ∗ is a lower bound for welfare in option k, conditionally on k being optimal. For w > w ∗, h i h Pr ω w ≤ W ω (y − p k, k) | k = J ω (p, y) decreases continuously until w reaches w k ∗ where Pr ω w ≤ i W ω (y − p k, k) | k = J ω (p, y) drops to 0, as seen in Figure 3a. Hence, w k ∗ is an upper bound for welfare in option k, conditional on k being optimal, and the distribution has a mass point at w k ∗. If w k ∗ = w ∗, the distribution is thus a step function and, hence, the welfare level in bundle k, conditional on k being optimal at prices p and exogenous income y, is deterministic and equals w k ∗.

Example: the MMU measures For the MMUs, we obtain the following result.

Corollary 2 When using reference prices p ref, we have h i h i ref.

Pr w ≤ M M U p ω ref (y − p k, k), j = J ω (p 0, y) = P j,k p 0, (p k, y−w+p ref −k ), y I p k ≤ y − w + p k ω When p k = p 0 k, and the reference prices equal the actual prices p 0 and k is the optimal choice, this simplifies to h i Pr w ≤ M M U p ω 0 y − p 0 k, k, k = J ω (p 0, y) = P k (p 0, y)I [w ≤ y] ω and, hence, h i Pr w ≤ M M U p ω 0 y − p 0 k, k | k = J ω (p 0, y) = I [w ≤ y], ω h Pr w ≤ M M U p ω 0 y − p 0 J ω (p 0,y), J ω (p 0, y) ω i = I [w ≤ y].

See proof on page 49. Both the MMU in the optimal bundle and the MMU in bundle k, conditional on k being optimal, are, therefore, deterministic and equal the initial exogenous income y when reference equal actual prices.

4.2 Joint distribution of welfare levels and welfare differences

In this section, we derive the joint distribution of welfare levels and welfare differences. Joint knowledge on levels and differences of welfare enables investigation of the association between individuals’ gains or losses from a price change and their position in terms of initial welfare. Assessment can be carried out on, for example, whether the winners of a price change belong disproportionately to those who were well-off in the first place. A price change is defined as an exogenous shift in prices from p to p 0. As discussed in Section 3.1, we will assume throughout that the unobserved preference type ω is unaltered by the price change. Firstly, we study the general case in which welfare differences are defined on the basis of changes in NOS welfare measures (evaluated in optimal choices). We show that the joint distribution of levels and differences can be expressed in terms of transition probabilities. Secondly, we specialise our

results to the joint distribution of the MMU and the CV, which is a popular choice among applied welfare economists. 15 In doing so, we extend the results of Dagsvik and Karlström (2005) and de Palma and Kilani (2011) to a nonparametric setting.

4.2.1

Welfare differences in terms of NOS measures As an intermediate step, we first derive the joint distribution of welfare before and after a price change in Proposition 1.

Proposition 1 The joint distribution of welfare in the optimal bundle i, before a price change, and welfare in the optimal bundle j, after the price change, is as follows:

Pr [w ≤ W 0 ω (y − p i, i), z ≤ W 1 ω (y − p 0 j, j), i = J ω (p, y), j = J ω (p 0, y)] ω h (19) i e (w), min p 0, p e (z), y I [p i ≤ p e i (w)] I p 0 j ≤ p e j (z).

= P i,j min p, p See proof on page 49. Proposition 1 shows that this joint distribution can be written in terms of transition probabilities, evaluated at initial, final, and virtual prices. Using this proposition, the joint distribution of welfare levels and differences can be derived.

Theorem 2

The function h is defined by:

h i e (max(w, x)), min p 0, p e (s), y I p 0 j ≤ p e j (s) h i,j,p,p 0 (w, x, s) = P i,j min p, p h i e (w), p e (x), min p 0, p e (s), y I p 0 j ≤ p e j (s).

= P i,j min p, p Then, the joint distribution of the stochastic welfare measure and the difference before and after the price change of this measure becomes, Pr [w ≤ W 0 ω (y − p i, i), W 1 ω (y − p 0 j, j) − W 0 ω (y − p i, i) ≤ z, i = J ω (p, y), j = J ω (p 0, y)] = ω −

## Z +∞

−∞ (20) ∂ 3 h i,j,p,p 0 (w, x, x + z)I [p i ≤ min(p e i (w), p e i (x))] dx.

See proof on page 50. Unfortunately, it seems that this expression cannot be simplified. However, even though expression (20) seems technically complicated, only the transition probabilities are used as input. This object is nonparametrically identified from panel data.

4.2.2

Welfare differences in terms of the CV We can specialise our results to the joint distribution of welfare and the CV, which is a popular choice among applied welfare economists. The CV refers to the (possibly negative) amount of the

15 The derivation for the EV is similar and can be found in Appendix A.2.

numeraire an individual wants to give up after a price change to be equally well-off as before this change. For an individual of type ω, the compensating variation CV ω is implicitly defined as max {U c ω (y − p c )} = max {U c ω (y − p 0 c − CV ω )}, c (21) c where, as before, p are initial prices and p 0 final prices. 16 In fact this definition of the CV is equivalent to M M U p ω 0 (y − p 0 J ω (p 0,y), J ω (p 0, y)) − M M U p ω 0 (y − p J ω (p,y), J ω (p, y)), i.e. the difference between the MMU with the final prices as reference price vector, in the optimal bundle after the price change, and the same MMU in the optimal bundle before the price change. 17 Note that the CV for a composition of two or more price changes cannot be calculated from the CV for each price change separately. In our more general general approach of measuring a change in welfare by the difference between two valuations of a welfare metric, this problem is inherently nonexistent. Note that the results in Theorems 3 and 4, and in Corollaries 3 and 4 below, can in fact be seen as applications of Theorem 2. However, to give more insight, we also give direct proofs in Appendix B.

Distribution of the CV In order to derive the distribution of the CV when the choice is equal to option i under initial prices and option j under final prices, we can follow a similar strategy as Bhattacharya (2015) and de Palma and Kilani (2011). Analogously to Lemma 1, the condition CV ω ≤ z, i = J ω (p, y), j = J ω (p 0, y) can be translated in i being the optimal bundle when faced with a counterfactual price vector.

Lemma 2 We have n o ω | CV ω ≤ z, i = J ω (p, y), j = J ω (p 0, y) n o = ω | U i ω (y − p i) ≥ max {U c ω (y − p 0 c − z)}, i = J ω (p, y), j = J ω (p 0, y).

(22) c See proof on page 51. With Lemma 2, we can state the following theorem.

16 Note that in our definition, the CV has the opposite sign of that in Bhattacharya (2015), but our results are completely equivalent. 17 Indeed, defining CV ω by M M U p ω 0 (y−p 0 J ω (p 0,y), J ω (p 0, y))−M M U p ω 0 (y−p J ω (p,y), J ω (p, y)), we get M M U p ω 0 (y− p J ω (p,y), J ω (p, y)) = y − CV ω by Corollary 2. Moreover, as i is the optimal bundle before the price change, we get max {U c ω (y − p c )} = U J ω ω (p,y) (y − p J ω (p,y)) c = max {U c ω (M M U p ω 0 (y − p J ω (p,y), J ω (p, y)) − p 0 c )} c = max {U c ω (y − p 0 c − CV ω )}.

c

Theorem 3 The joint distribution of the CV and the optimal choices before and after the price change is as follows:

Pr [CV ω ≤ z, i = J ω (p, y), j = J ω (p 0, y)] = P i,j (min(p, p 0 + z), p 0, y)I p i ≤ p 0 i + z. ω (23) See proof on page 51. We observe that Pr [CV ω ≤ z, i = J ω (p, y), j = J ω (p 0, y)] is bounded from below by p i − p 0 i. This ω is as expected; if the initial optimal bundle was i and the price of p i drops to p 0 i, the numeraire must drop with at least this amount to be equally well-off as in the initial situation. This means that the minimal compensation, in terms of the joint distribution, is p i −p 0 i. Moreover, for z ≥ max k {p k −p 0 k }, Pr [CV ω ≤ z | i = J ω (p, y), j = J ω (p 0, y)] = 1. This means that the maximal compensation, in ω terms of the conditional distribution, cannot be higher than the maximal price difference, which is also as expected. The next corollary follows immediately and may again be more useful to the applied researcher.

Corollary 3 Pr [CV ω ≤ z | i = J ω (p, y), j = J ω (p 0, y)] = ω Pr [CV ω ≤ z | i = J ω (p, y)] = ω Pr [CV ω ≤ z | j = J ω (p 0, y)] = ω P i,j (min(p, p 0 + z), p 0, y) I p i ≤ p 0 i + z, 0

P i,j (p, p, y) P i (min(p, p 0 + z), y) I p i ≤ p 0 i + z,

P i (p, y) X P i,j (min(p, p 0 + z), p 0, y)

P j (p 0, y) i (24) (25) I p i ≤ p 0 i + z, (26) and

Pr [CV ω ≤ z] = ω

## X

P i (min(p, p 0 + z), y)I p i ≤ p 0 i + z. 18 (27) i Equation (27) gives an expression for the marginal distribution of CV. Equations (24), (25) and (26), which present conditional distributions, can be used to calculate the distribution of CV when (i) the optimal bundles before and after price change are known, (ii) only before the price change is known, and (iii) only after the price change is known.

Joint distribution of the MMU and the CV We now apply Theorem 2 to the case where one chooses the MMU with final prices as the reference price vector, as a welfare measure. The difference in welfare before and after the price change is then equal to the CV.

18 Note that Equation (27) is the main result of Bhattacharya (2015).

Theorem 4 The joint distribution of the MMU and the CV is as follows:

Pr [w ≤ M M U p ω 0 (y − p i, i), CV ω ≤ z, i = J ω (p, y), j = J ω (p 0, y)] ω (28) = P i,j min p, p 0 + min(z, y − w), p 0, y I p i ≤ p 0 i + min(z, y − w).

See proof on page 52.

Again, Corollary 4 follows immediately.

Corollary 4 h i Pr w ≤ M M U p ω 0, CV ω ≤ z | i = J ω (p, y), j = J ω (p 0, y) ω P i,j min p, p 0 + min(z, y − w), p 0, y =

P i,j I p i ≤ p 0 i + min(z, y − w), (29) (p, p 0, y) Pr [w ≤ M M U p ω 0 (y − p i, i), CV ω ≤ z | i = J ω (p, y)] ω P i min p, p 0 + min(z, y − w), y = I p i ≤ p 0 i + min(z, y − w), (30)

P i (p, y) Pr [w ≤ M M U p ω 0 y − p J ω (p,y), J ω (p, y), CV ω ≤ z | j = J ω (p 0, y)] ω = 0 0 X P i,j min p, p + min(z, y − w), p, y

P j i (p 0, y) I p i ≤ p 0 i + min(z, y − w), (31) and, Pr [w ≤ M M U p ω 0 y − p J ω (p,y), J ω (p, y), CV ω ≤ z] ω =

## X

P i min p, p 0 + min(z, y − w), y I p i ≤ p 0 i + min(z, y − w). (32) i The joint cumulative distribution can again be written as (a sum of) choice or transition probabilities. Each choice and transition probability is calculated using up to three price vectors: the initial price vector p, the final price vector p 0, and a translation of the p 0 vector for the combined MMU and CV part.

.3

Social welfare A classical additively, separable Bergson-Samuelson social welfare function (SWF) takes the form

## Z

## SW F =

h(u) dG U (u), (33) where u is the value of a utility function representing the well-being of an individual in a particular state of the world, h is a concave function expressing the inequality aversion, and G U is the CDF of the well-being distribution in the population in a given state of the world. 19 For example, in the utilitarian case, we have that h(u) = u. Since the seminal work of Sen (1970), it is well known that in order to be able to meaningfully formulate a SWF, stringent assumptions on the measurability and degree of interpersonal comparability of such utility functions are required. 20 As a first option, researchers sought for conditions to make welfare prescriptions in terms of the income distributions instead (see, e.g. Roberts, 1980). These conditions turned out to be restrictive; preferences should be identical and homothetic, and the social welfare function in terms of incomes should be homothetic too. A second option is to use the NOS welfare measures as a representation of preferences. Fortunately, they are known to satisfy a set of attractive principles of interpersonal comparability (see Fleurbaey and Maniquet, 2017; 2018). We can, therefore, use these measures directly as building blocks in the SWF in Equation (33). More specifically, the equivalent to the Bergson-Samuelson SWF in our framework reads as

## Z Z

## SW F =

h(w) dF W (w | p, y) dG(p, y), (34) where G is the CDF of the joint distribution of prices and exogenous income in the population, which can be observed from the data, and F W (w | p, y) is the conditional CDF of the NOS measure W, h i and equals Pr W ω y − p J ω (p,y), J ω (p, y) ≤ w. 21 ω Proposition 2 illustrates how the results on the distribution of welfare levels in Corollary 1 lead to the calculation of social welfare as defined in Equation (34), using only choice probabilities.

Proposition 2 The conditional CDF of individual welfare in the optimal bundle can be calculated using choice probabilities:

F W (w | p, y) = 1 −

## X

e (w), y I [p k ≤ p e k (w)].

P k min p, p (35) k 19

## P

A function f is additively separable when it can be written in the form f (x 1,..., x n) = i f i (x i ). In a context of demand under a linear budget constraint, an indirect utility function in terms of prices and income may be a natural candidate to serve as utility function. However, such utility functions are only determined up to a positive monotone transformation and economists did not find agreement on which representative is the most suitable to serve as a basis for making interpersonal utility comparisons (for an overview of the debate, see Hammond, 1991). 21 As social welfare is a population level concept, we rely on the second interpretation of the randomness in the welfare measure (see the discussion at the beginning of Section 4).

20

See proof on page 54.

Hence, social welfare can be computed from these probabilities. The joint distribution of prices and exogenous income G can be estimated separately using standard nonparametric tools.

Moreover, this expression can be used to identify if a price change, for example, due to a policy reform, has a desirable effect on social welfare. Indeed, the difference in social welfare can be calculated as follows:

## SW F 0 − SW F =

## Z Z

h(w) dF W (w | p 0, y) dG 0 (p 0, y) −

## Z Z

h(w) dF W (w | p + ∆p, y) dG 0 (p + ∆p, y) = −

## Z Z

=

## Z Z

## Z Z

h(w) dF W (w | p, y) dG(p, y) (36) h(w) dF W (w | p, y) dG(p, y) h(w) d F W (w | p + ∆p, y) − F W (w | p, y) dG(p, y).

where G (G 0) is the joint distribution of initial (final) prices and exogenous income, and ∆p = p 0 −p. With Equations (36) and (35), one can asses the desirability of a potential price change without parametric assumptions and only using choice probabilities and the initial distribution of prices and exogenous income. Interestingly, in the spirit of Roberts (1980), we can derive conditions under which the expression for the SWF can be formulated in terms of incomes alone. In particular, when prices are equal for everyone and one uses the MMU with reference prices equal to those common prices, as individual welfare measure, one obtains a price independent SWF in terms of income.

Corollary 5 When prices are equal for everyone and when one uses the MMU with reference prices equal to those common prices as the welfare measure, the SWF can be written solely in terms of income.

See proof on page 54.

5 5.1

Discussion on implementation

Set-identifying transition probabilities from cross-sectional data As mentioned before, the transition probabilities are nonparametrically identifiable and estimable from panel data that contains sufficient relative price and exogenous income variation. This immediately implies that all the results from previous subsections are also nonparametrically identified in such a data setting. One simply has to evaluate the estimated transition probabilities at virtual price vectors.

In many empirical applications, however, researchers only have access to (repeated) cross-sectional data. This type of data nonparametrically identifies the choice probabilities, but not the associated transition probabilities. However, by exploiting Boole-Fréchet (Fréchet, 1935) and stochastic revealed preference inequalities, one can derive bounds on the now unobserved transition probabilities based on the observed choice probabilities.

Proposition 3 Suppose Assumptions 1 – 3 hold. Then the transition probabilities {P i,j (p, p 0, y)} are set identified from the choice probabilities {P i} with bounds n

## L

P i,i (p, p 0, y) = max P i (p, y) + P i (p 0, y) − 1, P i max{p i, p 0 i }, min{p −i, p 0−i}, y o,

## U

P i,i (p, p 0, y) = min P i (p, y), P i (p 0, y).

For i 6 = j, P i,j (p, p 0, y) = 0 if p i ≥ p 0 i and p j ≤ p 0 j and

## L

P i,j (p, p 0, y) = max{P i (p, y) + P j (p 0, y) − 1, 0},

## U

P i,j (p, p 0, y) = min P i (p, y), P j (p 0, y), elsewhere.

See proof on page 55. The Boole-Fréchet inequalities ensure that the transition probabilities are weakly smaller than their associated marginal choice probabilities P i (p, y) and P j (p 0, y). When P i (p, y)+P j (p 0, y)−1 > 0 they also deliver nontrivial lower bounds. The stochastic revealed preference inequalities, which stem from the strong monotonicity of the utility function (see Assumption 1), provide additional identificational power in two particular instances. Firstly, by evaluating the choice probabilities at the least-favourable price vector (max{p i, p 0 j }, min{p −i, p 0−i }), they yield an informative lower bound for the transition probabilities in the no-transition case where i = j. Secondly, when i becomes weakly less expensive and j 6 = i becomes weakly more expensive, the transition probability should equal zero, as it is irrational for individuals to make this transition within the context of our model.

5.2

Estimating choice probabilities Given the exogeneity of budget sets presupposed in Assumption 3, the choice probabilities can be readily estimated using nonparametric regression, as they are essentially conditional expectation functions. Standard tools, such as kernel and series based regression, are available in most modern statistical software. One particular attractive feature of the Nadaraya-Watson kernel estimator is that the estimated choice probabilities add up to one for all price vectors when the same bandwidth is selected for every choice probability function. When only samples of modest size are available, it might be useful to impose additional struc-

ture to mitigate the curse of dimensionality. In particular, in a setting with high-dimensional regressors, which arises when there are many goods or many choice and individual level characteristics, a (semi)parametric estimator can be used to increase efficiency at the expense of functional form misspecification. In particular, our empirical illustration in Section 6 will make use of a semiparametric estimator that can be interpreted as a sieve approximation.

Shape restrictions One point that needs further attention is that sampling noise might cause the non-or semiparametric estimates to be inconsistent with the monotonicity condition in Assumption 1 over some ranges of the data. When this condition is violated, the CDFs of our distributional results might be decreasing over some sections of their support. To avoid these inconsistencies, researchers can impose the following shape restrictions on the estimated choice probabilities:

Proposition 4 Suppose Assumptions 1-3 hold. Then the estimated choice probabilities {P i} should satisfy the following shape restrictions at all (p, y) for all i, j ∈ C:

∂P i (p, y) ≤ 0, ∂p i ∂P i (p, y) ≥ 0, ∂p j See proof on page 56. It is easy to see that, even under the presence of unrestricted, unobserved heterogeneity, utility maximisation yields restrictions on the partial derivatives of the choice probabilities. In particular, rationality implies that the choice probability for any given good is decreasing in its own price and increasing in the price of the other alternatives. In addition, the adding-up requirement for probabilities also imposes a restriction across choice probabilities.

Endogeneity of prices and income In some circumstances, it might be unreasonable to assume that the budget set (p, y) is independent of the preference type ω. When a vector of instruments is available, however, some forms of endogeneity can be handled by using a standard control function approach (Blundell and Powell, 2004).

Ordered choice and outside good Similar to Bhattacharya (2015), it is important to stress that identification generally fails in settings where choice is ordered and where the prices of alternatives are multiples of one another. In such a setting, there is no relative price variation in the data that identifies the effect of a price change in some alternative(s) while keeping the prices of the other alternatives fixed. Moreover, in some applications, there is an outside good that exhibits no independent price variation, which also hinders the direct empirical implementation of our approach. However, this difficulty can be circumvented by exploiting variation in the exogenous income y. Suppose good c o ∈ C is the

outside good for which one has to evaluate the effect of a price change ∆p o = p 0 o − p o. By a change of variables, it then always holds that P i (p 0, y) = P i (p 0 − ∆p o, y − ∆p o ). Note that the expression at the right-hand side does not require price variation for c o, as p 0 o − ∆p o = p o by construction.

5.3

Average welfare A well-known implication of Fubini’s theorem is that the mean of any random variable X, given that it exists, can be directly derived from its cumulative density function F X, i.e.

## Z ∞

## E(X) =

(1 − F X (u))du − 0

## Z 0

−∞

F X (u)du.

This result allows us to calculate average welfare from any of the distributional results derived above. Note that when only bounds on the distribution of interest are available (see Section 5.1), the expected value can be bounded by

## Z ∞

0 (1 − F X U (u))du −

## Z 0

−∞

F X U (u)du ≤ E(X) ≤

## Z ∞

0 (1 − F X L (u))du −

## Z 0

−∞

F X L (u)du, where F X L and F X U denote the CDF of the lower and upper bound respectively. This result allows us to calculate average welfare from any of the distributional results derived above.

6

Empirical illustration We highlight the empirical applicability of our results by revisiting the classical trade-off between leisure and consumption. The goal of this illustration is two-fold. Firstly, we demonstrate how the results in this paper enable researchers to assess the distribution of welfare within and across different groups in society. Secondly, we show how our results allow to evaluate the effects of an income tax reform on individual and social welfare. Thereby, we concentrate on two particular aspects: (i) a comparison of the welfare distribution before and after the reform, and (ii) the extent to which the winners and losers are (un)equally spread across the initial welfare distribution. For this purpose, we make use of microdata from the 2018 wave of the German Socio-Economic Panel (SOEP), which contains detailed information on households’ demographics, labour supply, wages, and out-of-work income. We model single females’ labour supply as a choice between three discrete alternatives: non-working (NW), part-time employment (PT), and full-time employment (FT). As an income tax reform, we consider the introduction of a basic income flat tax in Germany, which would replace the current nonlinear tax schedule.

.1

Setting and implementation German tax system and a basic income flat tax reform

The German personal income tax system is distinctly progressive. Taxes and social security contributions are paid on both earned, capital, and transfer income. After a basic tax-free allowance (8,820 euro in 2017), statutory marginal tax rates increase almost continuously from 14 to 45%. The system also has deductions for work related expenses, and allowances for lone parents and childcare expenses. There are no refundable tax credits; taxes, therefore, cannot become negative. Parents with dependent children are eligible for child benefits. For those who are not able to work, a subsistence income level is guaranteed by social assistance, which includes allowances for housing and heating costs. These benefits are means tested for income and wealth, and depend on the composition of the household. As a policy reform, we consider the introduction of a basic income flat tax. In this exercise, the current nonlinear tax schedule is replaced by one where only a single rate is applied to every individual’s taxable income. This does not yield a fully proportional tax schedule, however, as we leave the current deductions and reductions unchanged. The rate is set to 42%, which makes the reform revenue neutral from the point of the government. 22 In addition, we remove the means test for social assistance with regard to earned income, such that it acts as a basic income.

Data selection and estimation From the SOEP sample, we construct a subsample with single females that are available to the labour market. That is, we restrict the analysis to those below 60 years old. To reduce the effect of outliers, we also drop individuals with gross hourly wages outside of 4-90 euro and gross yearly asset income above 12,000 euro. Individuals with missing working hours are also discarded. Our final subsample consists of 1,922 single females; Appendix C.1 contains descriptive statistics for this subsample. We map observed working hours into three discrete alternatives: non-working (i.e. hours strictly lower than 5 hours/week); part-time employment (i.e. hours higher than 5 hours/week and strictly lower than 32 hours/week); and full-time employment (i.e. hours higher than 32 hours/week). For each of these alternatives, we calculate disposable income by means of a tax-benefit calculator. 23 The disposable income for the unemployment alternative is at least at the level guaranteed by social assistance. We model the choice probabilities for alternatives PT and FT semiparametrically, as we estimate for each a flexible binary logit model that contains cubic polynomials in the disposable income d of all 22 Revenue neutrality is here defined without taking labour supply responses into account. It is also calculated on the whole sample, not just on the subsample of single females for which we conduct the welfare analysis. We find that behavioural reactions have little impact on tax revenues. 23 Missing wages for the non-working are imputed using a Heckman-type selection model, with variables on the number of children acting as exclusion restrictions, as they are only included in the selection equation and not in the wage equation. For each individual, monthly disposable income is calculated for 0 (i.e. NW), 20 (i.e. PT), and 40 (i.e. FT) hours of work per week.

three alternatives and a linear index with demographic variables, such as age, years of education, number of children, and region. The choice probability for NW is defined as the complement. By means of an arbitrary normalisation, we fix an individual’s exogenous income to y = d F T, that is to the amount of disposable income she would obtain when working full-time. This is convenient, as it ensures that all prices are non-negative: i.e. p N W = d F T − d N W, p P T = d F T − d P T, and p F T = 0. For each alternative, the shape restrictions in Proposition 4 are imposed by means of a penalty function. This penalty function also ensures that the choice probability for NW is nowhere negative in the support of the data. For more details on the estimation procedure, we refer to Appendix C.2.

Welfare measure and reference prices All our results are calculated on the basis of a MMU (see Equation (13) for a definition). We fix the reference price for each alternative at the sample median of the difference in disposable income between working full-time and that respective alternative: i.e.

ref ref p ref N W = med(d F T − d N W ), p P T = med(d F T − d P T ), and p F T = 0. The virtual prices, therefore, become p e c (w) = d F T − w + p ref c, for c in {N W, P T, F T }.

6.2

Results

Individual and grouped welfare distributions We first study the distribution of individual welfare in the baseline, conditional on the chosen alternative (i.e. Equation (16) in Corollary 1). Figure 4 shows estimates of this distribution for all females in our subsample, partitioned in quartiles of gross hourly wages. Hourly wages reflect potential earning capacity and can be thought of as a proxy for ability. As was noted at the outset of Section 4, each individual distribution either reflects the econometician’s uncertainty about the welfare level of an individual with such observable characteristics (i.e. choice, prices, exogenous income, and demographic variables) or it reflects the distribution of actually realised welfare levels in the population of single females with such observable characteristics. In either case, possible differences in welfare for an individual with given observable characteristics are due to unobserved preference heterogeneity. For simplicity of exposition, we will maintain the second interpretation in the remainder of this empirical illustration. Visual inspection of Figure 4 reveals that these distribution functions have the expected shape (see Figure 3b). 24 On the one hand, there is a critical welfare level w ∗ below which the virtual prices of all three alternatives are higher than the actual price, and the welfare level will surely exceed that level. On the other hand, the welfare level w c ∗, for which the virtual price of the actually chosen alternative equals its actual price, is the highest welfare one can obtain. When w c ∗ ∗ = w ∗, the distribution degenerates to a step function, and we can determine the individual’s welfare level

24 Note that Figure 3b plots the CCDF, while the figures we present here are CDFs.

Figure 4: Individual welfare distributions for all females by alternative chosen and wage quartile exactly, whatever her preferences are. This happens to be the case for approximately 25% of the females in our subsample. It predominantly occurs for low-wage individuals who choose FT and high-wage individuals who choose NW. Figure 10 in Appendix C.5 also displays the individual unconditional welfare distributions, that is the welfare distribution of individuals with the same observable characteristics (i.e. prices, exogenous income, and demographic variables), whatever their optimal choice would have been (i.e. Equation (18) in Corollary 1). While these distributions turn out to exhibit several mass points, the deterministic cases seem to vanish. This is to be expected, as conditioning on observed choices introduces information that restricts the set of preference types. Therefore, the conditional distributions are ‘less stochastic’ than their associated marginal distributions. In Figure 5, we present the welfare distribution for groups based on the alternative chosen and wage quartile. These grouped distributions are obtained by aggregating the individual distributions within each of the panels of Figure 4. 25 The figure, thus, represents the welfare distribution in society for

25 In Figure 4, we plotted individual CDFs, i.e. for an individual `, Pr ω [W ω ≤ w | p `, y `, x `, i = J ω (p `, y `, x ` ), q].

When aggregating these distributions to a group level, we lower the level of conditioning by integrating out over prices, exogenous income, and demographic characteristics. At the sample level, we obtained the aggregation as follows: Pr [W ω ≤ w | i = J ω (p, y, x), q] =

## X

ω Pr [W ω ≤ w | p `, y `, x `, i = J ω (p `, y `, x ` ), q = q `] ω ` 1, #{` | i = J ω (p `, y `, x ` ), q = q `} where x is a vector that contains demographic variables, and q indicates the wage quartile. Asymptotically, this is

each of these twelve groups. The welfare distribution of high-wage (i.e. fourth quartile) individuals who choose FT tends to first-order dominate the welfare distribution of those who choose alternative PT, and the latter dominates that of NW. Notwithstanding some exceptions at the bottom part of the distribution, the opposite is true for the low-wage individuals (i.e. first quartile). This can be explained as follows. Low-wage individuals have a relatively low gain in disposable income from choosing PT or FT compared with NW. As a consequence, low-wage individuals who choose FT must have more intense preference for income relative to leisure than other low-wage individuals. But because their disposable income is relatively low, this implies that their welfare is relatively low. One could say that, for those individuals, their preferences are less adapted to their wages. The reverse is the case for persons with high gross hourly wages.

Figure 5: Grouped welfare distributions by alternative chosen and wage quartile In Figure 6, we further aggregate these distributions by integrating out the chosen alternative. The group with the highest wages tends to first-order dominate the other groups. 26 Substantially higher wages thus lead to increased welfare, despite the large degree of unobserved preference variation we allow for. However, systematic preference differences between the populations of different wage quartiles, due to different composition of demographic variables (age, education, household size) equivalent to the population concept

## Z

p,y,x 26 Pr [W ω ≤ w | p, y, x, i = J ω (p, y, x), q] dG(p, y, x | i = J ω (p, y, x), q). ω Inequality also seems to be higher in the highest wage group compared to the others.

among the wage quartiles, might play a role too in explaining the welfare dominance of the fourth quartile. In contrast, welfare levels obtained by individuals belonging to the lower three wage quartiles turn out to be more intermingled. This suggests that, besides wages, both systematic and unobserved preference differences do play an important role in assessing the welfare of an individual.

Figure 6: Grouped welfare distribution by wage quartile

Social welfare and reform Our next point is to discuss the effects of the simulated reform, where the existing nonlinear tax system is replaced with a basic income flat tax. Figure 7 compares the overall welfare distribution for the baseline and the reform. The welfare distribution is computed by further aggregating the distributions for the different wage groups of Figure 6 into one overall welfare distribution for the entire population of single females. The reform welfare distribution tends to first-order dominate the baseline welfare distribution. 27 It is well known that this implies that all the members of the class of SWFs we propose in Equation (34) will unanimously prefer the reform welfare distribution over that for the baseline. For completeness, we present some estimates for different inequality aversion parameters of the Atkinson SWF in Table 4 of Appendix C.5.

27 This may be partly due to the fact that the reform is not budget neutral for this specific subsample. We leave a detailed analysis of this result for future research, as it is beyond the scope of this illustration.

Figure 7: Welfare distribution in the baseline and reform Winners and losers The presence of first-order dominance does not imply that everybody gains. 28 We further analyse, therefore, the extent to which the winners and losers are (un)equally spread across the baseline welfare distribution. For this purpose, we approximate the over all individuals and their baseline and reform choices aggregated joint distribution of welfare and welfare differences (i.e. Equation (20)) numerically. 29 Finally, we transform this joint distribution into the distribution of welfare differences conditional on the baseline welfare level. We refer to Appendix C.4 for more details on this procedure. Figure 8 depicts a smoothed version of the 10th, 50th, and 90th iso-percentile contours (Figures 13 and 14 in Appendix C.5 show a more detailed picture). Each point (w, z) on the qth contour indicates the minimal welfare gain z (or a loss, if z is negative) that is reached by q% of the population with baseline welfare level w. First, observe that, despite the first-order dominance, there are a considerable amount of losers. For example, welfare levels at which the 90th iso-percentile curve lies below the zero point on the vertical axis, indicate that at least 10% of the persons with this baseline welfare level exhibit a loss. This occurs especially for welfare levels above 2,000 euro (this is above the mean, see Table 4 in Appendix C.5). Secondly, among the richer persons in the baseline, in terms of

28 This is because first-order dominance is a combination of both Pareto-dominance and anonymity. Notice that we cannot use the simplified versions based on the CV (i.e. Equation (28) of Theorem 4) or the EV (i.e. Equation (48) of Theorem 6). Indeed, in our application the actual baseline and reform prices are individual specific. Using these as reference prices would imply that the resulting welfare measure does not any longer comply with our definition, which requires that the nested opportunity sets are common to all individuals. 29

well-being, there is a majority of losers. Thirdly, there is a small tendency for the number of losers to increase with welfare. However, the distribution of losses and gains varies a lot across baseline welfare levels, as might be seen from the more detailed pictures in Appendix C.5.

Figure 8: Distribution of welfare gains and losses conditional on baseline welfare In Table 1, we distribute the population over three, roughly equal, groups of initial welfare levels, and three categories of winners and losers (losers, small gains, and big gains). About 90% of the losers turn out to belong to the initially best-off group. Overall, the losers form a minority of about 15%. Large gains are more prevalent for the initially worst-off third. Moderate gains occur at an equal frequency among the initially worst-off third and the middle group, and occur almost twice as much these groups compared to the initially best-off third. Over 40% of the initially best-off third are losers, while the latter account for only 3% in the middle group, and just 2% in the initially worst-off.

Table 1: Distribution of the winners and losers in terms of baseline welfare (in %)

Baseline welfare (euro)

Welfare gain (euro) (−1000, 0] (0, 200] (200, 1000] (800, 1500] (1500, 2000] (2000, 4000] 0.6 0.9 13.1 19.1 19.1 11.2 14.8 12.2 8.9

Column sums 14.6 49.4 35.9

Row sums 34.5 32.2 31.7

Concluding remarks In this paper, we provided a coherent framework to conduct individual and social welfare analysis for discrete choice. Allowing for unrestricted, unobserved preference heterogeneity, we argue that individual welfare measures become random variables from the point of view of the econometrician. For the broad class of NOS measures, we developed nonparametric methods to retrieve their distributions from observational data. In particular, we proved that all relevant marginal, conditional, and joint distributions can be expressed in terms of choice and transition probabilities, which are nonparametrically point-identified from cross-sectional and panel data, respectively. We also showed how transition probabilities can be set-identified when only cross-sectional data is available, which is important in empirical applications. To illustrate the empirical usefulness of our results, we revisited the classical trade-off between leisure and consumption, using microdata from the 2018 wave of the German Socio-Economic Panel (SOEP). We modelled single females’ labour supply as a choice between three discrete alternatives: nonworking, part-time employment, and full-time employment. Using a MMU, we present nonparametric distributional estimates of individual and social welfare for the nonlinear and progressive tax schedule that is currently in place in Germany. In particular, we found that (unobserved) preferences do play an important role in assessing the welfare levels of single females: the welfare distributions of the lowest three wage quartiles are intermingled. Only the distribution of welfare of high-wage individuals tends to first-order dominate that of the other three groups. We also studied the welfare effects of replacing the current schedule with a basic income flat tax. We found that around 15% of the single females would see their welfare diminished; this is especially the case for those that are well-off in the baseline. Large gains were more prevalent among those that were initially poor. Among the bottom two-thirds of the population in terms of baseline welfare, almost 98% would advance as a result of the reform. There are several avenues for future research. Firstly, one could extend our results to settings where, besides prices, other attributes of the alternatives are changed. In the same strand of thinking, the welfare cost of the introduction, and removal, of some alternatives could be studied. This will likely lead to set-identification, instead of point-identification, of the distributions of interest. 30 Secondly, another methodological innovation could allow for measurement and optimisation errors in the formal analysis. Depending on the specific application, a significant part of the variation in outcomes can be driven by these errors, which might bias welfare estimates. Lastly, future research is needed to assess the sensitivity of empirical welfare estimates, with respect to the choice of the welfare measure and the corresponding reference prices.

30 Bhattacharya (2018) shows that this is indeed the case for the marginal distribution of the CV and EV.

## References

Debopam Bhattacharya. Nonparametric Welfare Analysis for Discrete Choice. Econometrica, 83(2):

617–649, 2015. ISSN 0012-9682. doi: 10.3982/ECTA12574.

Debopam Bhattacharya. Empirical welfare analysis for discrete choice: Some general results. Quantitative Economics, 9(2):571–615, 2018. ISSN 1759-7323. doi: 10.3982/QE931.

Richard Blundell and James L. Powell. Endogeneity in Semiparametric Binary Response Models.

Review of Economic Studies, 71:655–679, 2004.

Richard Blundell, Dennis Kristensen, and Rosa Matzkin. Bounding quantile demand functions using revealed preference inequalities. Journal of Econometrics, 179(2):112–127, April 2014. ISSN 03044076. doi: 10.1016/j.jeconom.2014.01.005.

Richard Blundell, Joel Horowitz, and Matthias Parey. Nonparametric Estimation of a Nonseparable Demand Function under the Slutsky Inequality Restriction. The Review of Economics and Statistics, 99(2):291–304, May 2017. ISSN 0034-6535, 1530-9142. doi: 10.1162/REST a 00636.

Richard A. Briesch, Pradeep K. Chintagunta, and Rosa L. Matzkin. Nonparametric Discrete Choice Models With Unobserved Heterogeneity. Journal of Business & Economic Statistics, 28(2):291– 307, April 2010. ISSN 0735-0015, 1537-2707. doi: 10.1198/jbes.2009.07219.

Jean François Carpantier and Christelle Sapata.

Empirical welfare analysis: when preferences matter. Social Choice and Welfare, 46(3):521–542, 2016. ISSN 01761714. doi: 10.1007/ s00355-015-0927-y.

Sam Cosaert and Thomas Demuynck. Nonparametric Welfare and Demand Analysis with Unobserved Individual Heterogeneity. The Review of Economics and Statistics, 100(2):349–361, May 2018.

ISSN 0034-6535, 1530-9142. doi: 10.1162/REST a 00672.

John K. Dagsvik. Discrete Choice in Continuous Time: Implications of an Intertemporal Version of the IIA Property. Econometrica, 70(2):817–831, 2002.

John K. Dagsvik and Anders Karlström. Compensating Variation and Hicksian Choice Probabilities in Random Utility Models That Are Nonlinear in Income. The Review of Economic Studies, 72 (1):57–76, 2005.

André de Palma and Karim Kilani. Transition choice probabilities and welfare analysis in additive random utility models. Economic Theory, 46(3):427–454, April 2011. ISSN 0938-2259, 1432-0479.

doi: 10.1007/s00199-009-0513-6.

Koen Decancq, Marc Fleurbaey, and Erik Schokkaert. Happiness, equivalent incomes and respect for individual preferences. Economica, 82:1082–1106, 2015.

André M.J. Decoster and Peter Haan. Empirical welfare analysis with preference heterogeneity. International Tax and Public Finance, 22(2):224–251, 2015. ISSN 15736970. doi: 10.1007/ s10797-014-9304-5. Paolo Delle Site and Marco Valerio Salucci. Transition choice probabilities and welfare analysis in random utility models with imperfect before–after correlation. Transportation Research Part B: Methodological, 58:215–242, December 2013. ISSN 01912615. doi: 10.1016/j.trb.2013.09.003. Holger Dette, Stefan Hoderlein, and Natalie Neumeyer. Testing multivariate economic restrictions using quantiles: The example of Slutsky negative semidefiniteness. Journal of Econometrics, 191 (1):129–144, March 2016. ISSN 03044076. doi: 10.1016/j.jeconom.2015.07.004. Peter Diamond and Daniel McFadden. Some uses of the expenditure function in public finance. Journal of Public Economics, 3(1):2–21, 1974. ISSN 0047-2727. doi: 10.1016/0047-2727(74) 90020-6. Avinash Dixit. Welfare effects of tax and price changes. Journal of Public Economics, 4(2):103–123, 1975. Marc Fleurbaey. Social welfare, priority to the worst-off and the dimensions of individual well-being. In Francesco Farina and Ernesto Savaglio, editors, Inequality and Economic Integration, pages 236–277. Routledge, 2006. Marc Fleurbaey. Two criteria for social decisions. Journal of economic Theory, 134(1):421–447, 2007. Marc Fleurbaey. Beyond GDP: The quest for a measure of social welfare. Journal of Economic Literature, 47(4):1029–1075, 2009. ISSN 00220515. Marc Fleurbaey and Didier Blanchet. Beyond GDP: Measuring welfare and assessing sustainability. Oxford University Press, 2013. Marc Fleurbaey and Guillaume Gaulier. International comparisons of living standards by equivalent incomes. Scandinavian Journal of Economics, 111(3):597–624, 2009. Marc Fleurbaey and François Maniquet. Fairness and well-being measurement. Mathematical Social Sciences, 90:119–126, 2017. ISSN 01654896. doi: 10.1016/j.mathsocsci.2016.11.003. URL http://dx.doi.org/10.1016/j.mathsocsci.2016.11.003. Marc Fleurbaey and François Maniquet. Optimal income taxation theory and principles of fariness. Journal of Economic Literature, 56(3):1029–1079, 2018. doi: 10.1257/jel.20171238. URL https: //doi.org/10.1257/jel.20171238. Maurice Fréchet. Généralisation du théorème des probabilités totales. Fundamenta Mathematicae, 25(1):379–387, 1935.

Peter J. Hammond. Interpersonal comparisons of utility: Why and how they are and should be made. In J Elster and JE Roemer, editors, Interpersonal Comparisons of Well-being, pages 200– 253. Cambridge University Press, Cambridge, 1991.

Jerry A. Hausman and Whitney K. Newey. Individual Heterogeneity and Average Welfare. Econometrica, 84(3):1225–1248, 2016. ISSN 0012-9682. doi: 10.3982/ECTA11899.

Joseph A. Herriges and Catherine L. Kling. Nonlinear Income Effects in Random Utility Models.

Review of Economics and Statistics, 81(1):62–72, February 1999. ISSN 0034-6535, 1530-9142.

doi: 10.1162/003465399767923827.

Stefan Hoderlein and Anne Vanhems. Estimating the distribution of welfare effects using quantiles.

Journal of Applied Econometrics, 33(1):52–72, January 2018. ISSN 08837252. doi: 10.1002/jae.

2587.

Mervyn King. Welfare analysis of tax reforms using household data. Journal of Public Economics, 21(2):183–214, 1983.

Roger W. Klein and Richard H. Spady. An Efficient Semiparametric Estimator for Binary Response Models. Econometrica, 61(2):387–421, March 1993. ISSN 00129682. doi: 10.2307/2951556.

Arthur Lewbel. Semiparametric qualitative response model estimation with unknown heteroscedasticity or instrumental variables. Journal of Econometrics, 97(1):145–177, July 2000. ISSN 03044076.

doi: 10.1016/S0304-4076(00)00015-4.

Charles F. Manski. Maximum score estimation of the stochastic utility model of choice. Journal of

Econometrics, 3:205–228, 1975.

Rosa L. Matzkin. Semiparametric Estimation of Monotone and Concave Utility Functions for Polychotomous Choice Models. Econometrica, 59(5):1315, September 1991. ISSN 00129682. doi:

10.2307/2938369.

Rosa L. Matzkin.

Nonparametric identification and estimation of polychotomous choice models. Journal of Econometrics, 58(1-2):137–168, July 1993. ISSN 03044076. doi: 10.1016/

## 0304-4076(93)90116-M.

Daniel McFadden. Conditional logit analysis of qualitative choice behavior. In P Zarembka, editor, Frontiers in Econometrics. Academic Press, New York, NY, 1974.

Daniel McFadden. Econometric models of probabilistic choice. In Charles F Manski and Daniel McFadden, editors, Structural analysis of discrete data with econometric applications, pages 198– 272. MIT press Cambridge, MA, 1981.

Daniel McFadden. Computing Willingness-to-Pay in Random Utility Models. In James Melvin, Raymond Riezman, and James Moore, editors, Trade, Theory and Econometrics, volume 15. Rout-

ledge, August 1999. ISBN 978-0-415-14831-3 978-0-203-07420-6. doi: 10.4324/9780203074206. ch15. Daniel McFadden. Revealed Stochastic Preference: A Synthesis. Economic Theory, 26(2):245–264, 2005. Edward R. Morey, Robert D. Rowe, and Michael Watson. A Repeated Nested-Logit Model of Atlantic Salmon Fishing. American Journal of Agricultural Economics, 75(3):578, August 1993. ISSN 00029092. doi: 10.2307/1243565. Elisha Pazner. Equity, nonfeasible alternatives and social choice: A reconsideration of the concept of social welfare. In JJ Laffont, editor, Aggregation and revelation of preferences. Elsevier, NorthHolland, Amsterdam and New York, 1979. John H Pencavel. Constant-utility index numbers of real wages. The American Economic Review, 67(2):91–100, 1977. Ian Preston and Ian Walker. Welfare measurement in labour supply models with nonlinear budget constraints. Journal of Population Economics, 12(3):343–361, 1999. Kevin Roberts. Price-independent welfare prescriptions. Journal of Public Economics, 13(3):277–297, 1980. Paul A Samuelson. Complementarity: An essay on the 40th anniversary of the hicks-allen revolution in demand theory. Journal of Economic literature, 12(4):1255–1289, 1974. Amartya K Sen. Collective Choice and Social Welfare. Holden–Day, San Francisco, 1970. Kenneth A. Small and Harvey S. Rosen. Applied Welfare Economics with Discrete Choice Models. Econometrica, 49(1):105–130, January 1981. ISSN 00129682. doi: 10.2307/1911129. Kenneth E Train. Discrete Choice Methods with Simulation. Cambridge University Press, Cambridge, 2003.

## A

Additional results

## A.1

Additional NOS measures: the equivalent income metric and the wage metric Fleurbaey (2006) discusses two additional NOS metrics: the equivalent income (EI) metric and the wage rate (WR) metric. 31 These measures are especially useful in situations where there is a good, such as leisure time or health for example, the consumption of which is bounded above.

## A.1.1

Continuous setting In the two-good continuous setting, we will call this capacity-constrained good as good 1 and the other good, which acts as the numeraire, as good 2.

Equivalent income metric The EI metric measures an individual’s well-being by the amount of good 2 necessary to enjoy the full amount of good 1, denoted by T, and to be equally well-off as per her actual situation, denoted by x. Denote this amount by EI R (x), where R denotes the individual’s preferences.

The associated opportunity set is then the set of bundles B λ ≡ {(g 1, g 2) |g 2 ≤ λ, g 1 = T }. This is illustrated in Figure 9a for two persons, an individual with preferences R, who more intensely values good 1, and an individual with preferences R 0, who more intensely values good 2. Suppose both receive the same bundle x. The individual with preferences R, for example, is considered to be worse-off because she gets an equal compensation for not having good 1 at full capacity while she values that good more.

Wage metric Consider the price a person with preferences R and bundle x should earn per unit of good 1, such that she would be able to reach a point that is equally as good as x if offering good 1 (e.g. labour time, in which case the price is a wage, hence the name of the criterion) were her sole source of income. The level of this price or wage rate, denoted by WR R (x), is the WR metric of well-being. The associated opportunity set is B λ ≡ {(c, `) |c ≤ λ (T − `) }. Figure 9b illustrates that according to this measure, the individual with preferences R 0, who values good 2 (e.g. consumption) relatively more than the individual with preferences R, is now considered to be worse-off than the other one, in contrast to the previous case.

## A.1.2

Discrete setting We now describe how these measures can be adjusted to the discrete choice setting and present some distributional results. 31 This last measure was originally developed by Pencavel (1977) and is also mentioned in Preston and Walker (1999).

good 2 good 2

## R

## R

## R 0

## R 0

x 0

EI R (x) x

EI R (x) 0

WR R (x)

WR R (x) good 1 good 1 (a) The EI metric (b) The WR metric

Figure 9: Additional NOS measures Equivalent income metrics Fix a reference option, which we denote by 0. Well-being of an individual obtaining option k at price p k is then defined as the amount of the numeraire good necessary to be equally well-off in the reference option 0 as in the point (y − p k, k). To obtain this, let Λ = R, and let y c λ = −∞ for all λ, when c 6 = 0, and y 0 λ = λ. The family of opportunity sets can n o then be defined as B λ = (y 0, 0) | y 0 ≤ y 0 λ. It is a collection of growing spikes for the 0-option. Equivalently, p e c (λ) = +∞ for all λ, when c 6 = 0, and p e 0 (λ) = y − λ. The EI metric EI ω (y − p k, k) is equal to:

n o EI ω (y − p k, k) = max λ | U k ω (y − p k) ≥ max U c ω (y − p e c (λ)) λ n = max λ | λ

U k ω (y − p k) ≥ c

U 0 ω o (37) (λ).

Given a reference option 0, the equivalent income level of well-being of a type ω individual who obtains option k at price p k, denoted by EI ω (y − p k, k), is thus implicitly defined by:

U 0 ω (EI ω (y − p k, k)) = U k ω (y − p k).

Corollary 6 (38) When using an EI metric, we have for k = 0 h i Pr w ≤ EI ω (y − p 0, 0), j = J ω (p, y) = P j (p, y)I [w ≤ y − p 0], ω

(39) and, hence, h i Pr w ≤ EI ω (y − p 0, 0) = Pr w ≤ EI ω (y − p 0, 0) | j = J ω (p, y) = I [w ≤ y − p 0]. ω ω (40)

For k 6 = 0, we have Pr w ≤ EI ω (y − p k, k) | k = J ω (p, y) =

P k min(y − w, p 0 ), p −0, y (41)

P k (p, y) ω and h i Pr w ≤ EI ω (y − p k, k) = Pr U k ω (y − p k) ≥ U 0 ω (w).

ω (42) ω

Moreover, Pr w ≤EI ω y − p J ω (p,y), J ω (p, y) ω =

## X

P k min(y − w, p 0 ), p −0, y + P 0 (p, y)I [w ≤ y − p 0] (43) k6 =0 = I [w ≤ y − p 0] + I [w > y − p 0]

## X

P k y − w, p −0, y k6 =0 The marginal and conditional EI in bundle 0 are deterministic and equal to y − p 0. The marginal CDF of EI in bundle k equals the probability of choosing k, when the options are k with price p k and option 0 with price y − w.

Proof. When using an EI metric, we have for general k ∈ C Pr w ≤ EI ω (y − p k, k), j = J ω (p, y) ω h i = Pr U k ω (y − p k) ≥ max U i ω (y − p e i (w)), U j ω (y − p j) ≥ max U c ω (y − p c) ω i c6 = j h i = Pr U k ω (y − p k) ≥ U 0 ω (w), U j ω (y − p j) ≥ max U c ω (y − p c) ω c6 = j as p e i (w) = +∞ for i 6 = 0. Hence, for k = 0, this reduces to h i Pr w ≤ EI ω (y − p 0, 0), j = J ω (p, y) = P j (p, y)I [w ≤ y − p 0]. ω

Equations (40) follow immediately.

(44) For k 6 = 0, (44) implies that Pr ω w ≤ EI ω (y − p k, k), k = J ω (p, y) Pr w ≤ EI (y − p k, k) | k = J (p, y) = ω

P k (p, y) ω ω h Pr ω U k ω (y − p k) ≥ max U 0 ω (w), max c6 = k U c ω (y − p c) = i

P k (p, y)

P k min(y − w, p 0 ), p −0, y =,

P k (p, y) and Pr [w ≤ EI ω (y − p k, k)] =

## X

ω j Pr w ≤ EI ω (y − p k, k), j = J ω (p, y) ω = Pr [U k ω (y − p k) ≥ U 0 ω (w)].

ω Wage metric Let x c reflect the number of units in option c of a good that is only available in discrete amounts (e.g. labour time). Let Λ = R + and y c λ = λx c 32 where λ can be seen as the unit price of that good. Equivalently, we have p e c (λ) = y − λx c. The wage metric WR ω (y − p k, k) equals n o WR ω (y − p k, k) = max λ | U k ω (y − p k) ≥ max U c ω (λx c).

c λ (45) Let an option c be characterised by the availability of x c units of a good. The WR level of well-being of a type ω individual who obtains option k at price p k, denoted by WR ω (y − p k, k), is defined implicitly by:

U k ω (y − p k) = max U c ω (WR ω (y − p k, k) x c).

c

Corollary 7 (46)

When using the WR metric, we have Pr w ≤ WR ω (y − p k, k), j = J ω (p, y) = P j,k p, (p k, y − wx −k), y I [w ≤ (y − p k )/x k] (47) ω

32 Strictly, this definition is not compatible with condition (6), as the infimum of y c λ is not −∞, but 0, for all c.

However, a straightforward adaption to R + is possible.

and, hence, Pr w ≤ WR ω (y − p k, k) | j = J ω (p, y) = P j,k p, (p k, y − wx −k), y

P j (p, y) ω Pr w ≤ WR ω (y − p k, k) | k = J ω (p, y) =

P k min(p, y − wx), y

P k (p, y) ω I [w ≤ (y − p k )/x k] I [w ≤ (y − p k )/x k] Pr w ≤ WR ω (y − p k, k) = P k (p k, y − wx −k), y I [w ≤ (y − p k )/x k] ω Pr w ≤ WR ω y − p J ω (p,y), J ω (p, y) ω =

## X

P k min(p, y − wx), y I [w ≤ (y − p k )/x k].

k Proof. As p e c (w) = y − wx c, we have e −k (w)), y I [p k ≤ p e k (w)] Pr w ≤ WR ω (y − p k, k), j = J ω (p, y) = P j,k p, (p k, p ω = P j,k p, (p k, y − wx −k), y I [p k ≤ y − wx k] = P j,k p, (p k, y − wx −k), y I [w ≤ (y − p k )/x k].

The conditional and marginal distributions follow immediately.

## A.2

Results for the equivalent variation This section derives analogue results to Theorem 3, Corollary 3, and Theorem 4, but now for the EV instead of the CV. For an individual of type ω, the equivalent variation EV ω is defined as max {U c ω (y − p c − EV ω )} = max U c ω y − p 0 c c c, i.e, the amount of money (possibly negative) an individual has to pay before the reform to be equally well-off as after the reform.

Theorem 5 For the distribution of the EV, we have the following results:

h i Pr [EV ω ≤ z, i = J ω (p, y), j = J ω (p 0, y)] = P i,j (p, min(p + z, p 0 ), y)I p 0 j ≤ p j + z, ω Pr [EV ω ≤ z | i = J ω (p, y), j = J ω (p 0, y)] = ω Pr [EV ω ≤ z | i = J ω (p, y)] = ω i P i,j (p, min(p + z, p 0 ), y) h 0

## I

p ≤ p + z, j j

P i,j (p, p 0, y) i X P i,j (p, min(p + z, p 0 ), y) h I p 0 j ≤ p j + z,

P i (p, y) j Pr [EV ω ≤ z | j = J ω (p 0, y)] = ω

Pr [EV ω ≤ z] = ω i P j (min(p + z, p 0 ), y) h 0

## I

p ≤ p + z, j j

P j (p 0, y)

## X

h i P j (min(p + z, p 0 ), y)I p 0 j ≤ p j + z.

j

Proof. We have that n EV ω ≤ z, i = J ω (p, y), j = J ω (p 0, y) = n = n o max {U c ω (y − p c − EV ω )} ≥ max {U c ω (y − p c − z)}, i = J ω (p, y), j = J ω (p 0, y) c o c o max U c ω y − p 0 c ≥ max {U c ω (y − p c − z)}, i = J ω (p, y), j = J ω (p 0, y), c c such that, Pr [EV ω ≤ z, i = J ω (p, y), j = J ω (p 0, y)] ω h = Pr U i ω (y − p i) ≥ max U k ω (y − p k ), ω k6 = i U j ω (y − p 0 j) ≥ max U l ω (y − p 0 l ), l6 = j i max U c ω (y − p 0 c) ≥ max {U c ω (y − p c − z)} c c h = Pr U j ω (y − p 0 j) ≥ max U k ω (y − min(p k + z, p 0 k )), ω k6 = j h i h U i ω (y − p i) ≥ max U l ω (y − p l) I p 0 j ≤ p j + z l6 = i i = P i,j (p, min(p + z, p 0 ), y)I p 0 j ≤ p j + z.

The other equalities follow directly.

Theorem 6 The joint distribution of the MMU, with initial prices as reference prices, and the EV is expressed as:

Pr [w ≤ M M U p ω (y − p i, i), EV ω ≤ z, i = J ω (p, y), j = J ω (p 0, y)] ω h i = P i,j p, min(p 0, p + z), y I p 0 j ≤ p j + z I [w ≤ y].

(48) i

Proof. We have Pr [w ≤ M M U p ω (y − p i, i), EV ω ≤ z, i = J ω (p, y), j = J ω (p 0, y)] ω h U c ω 0 (y − (p c 0 + y − w)), = Pr U i ω (y − p i) ≥ max 0 ω c

U j ω (y − p 0 j) ≥ max U l ω (y l6 = j − p 0 l ),

U j ω (y − U i ω (y − p i) ≥ max U k ω (y − p k ), k6 = i p 0 j) h ≥ = Pr U i ω (y − p i) ≥ max U k ω (y − min(p k, p k + y − w)), ω k6 = i h

## I

p 0 j max {U c ω (y c − p c − z)} i U j ω (y − p 0 j) ≥ max U l ω (y − min(p 0 l, p l + z)) l6 = j i ≤ p j + z I [p i ≤ p i + y − w)] h i = P i,j p, (p 0 j, min(p 0−j, p −j + z)), y I p 0 j ≤ p j + z I [w ≤ y] h i i = P i,j p, min(p 0, p + z), y I p 0 j ≤ p j + z I [w ≤ y].

## B

Proofs

Theorem 1 The joint distribution of the NOS welfare measure W, evaluated in an option k with price p k, and choosing j at prices p 0 and exogenous income y can be expressed in terms of transition probabilities as follows:

e −k (w)), y I [p k ≤ p e k (w)], Pr w ≤ W ω (y − p k, k), j = J ω (p 0, y) = P j,k p 0, (p k, p ω (14) e −k (w)) = (p e 1 (w),..., p e k−1 (w), p k, p e k+1 (w),..., p e n (w)).

where (p k, p Proof of Theorem 1. Using Lemma 1, we have that Pr w ≤ W ω (y − p k, k), j = J ω (p 0, y) ω = Pr U k ω (y − p k) ≥ max U c ω (y − p e c (w)), U j ω (y − p 0 j) ≥ max U c ω 0 (y − p 0 c 0) 0 ω c c 6 = j = Pr U k ω (y − p k) ≥ max U c ω (y − p e c (w)), U j ω (y − p 0 j) ≥ max U c ω 0 (y − p 0 c 0) I [p k ≤ p e k (w)] 0 ω c 6 = j c6 = k e −k (w)), y I [p k ≤ p e k (w)].

= P j,k p 0, (p k, p

Corollary 1 h i Pr w ≤ W ω (y − p k, k) | j = J ω (p 0, y) = e −k (w)), y

P j,k p 0, (p k, p

P j (p 0, y) ω h i Pr w ≤ W ω (y − p k, k) | k = J ω (p, y) = e (w), y

P k min p, p (15) I [p k ≤ p e k (w)], (16)

P k (p, y) ω I [p k ≤ p e k (w)], e (w) = min(p 1, p e 1 (w)),..., min(p n, p e n (w)), where min p, p e −k (w)), y I [p k ≤ p e k (w)], Pr w ≤ W ω (y − p k, k) = P k (p k, p ω (17) and h Pr w ≤ W ω y − p J ω (p,y), J ω (p, y) ω i =

## X

e (w), y I [p k ≤ p e k (w)].

P k min p, p k

(18)

Proof of Corollary 1.

(a) For the conditional distribution on option j being chosen, we have h Pr ω [w ≤ W ω (y − p k, k), j = J ω (p 0, y)]

P j (p 0, y) i Pr w ≤ W ω (y − p k, k) | j = J ω (p 0, y) = ω e −k (w)), y

P j,k p 0, (p k, p =

P j (p 0, y) I [p k ≤ p e k (w)].

(b) For the conditional distribution on option k being chosen, we have h h Pr ω w ≤ W ω (y − p k, k), k = J ω (p, y) i Pr w ≤ W ω (y − p k, k) | k = J ω (p, y) = i

P k (p, y) ω e −k (w)), y I [p k ≤ p e k (w)]

P k,k p, (p k, p =

P k (p, y) h = Pr U k ω (y − p k) ≥ max U c ω (y − p c ), ω c6 = k

U k ω (y i − p k) ≥ max U c ω (y − p e c (w) I [p k ≤ p e k (w)] /P k (p, y) c6 = k = Pr U k ω (y − p k) ≥ max U c ω y − min(p c, p e c (w)) ω c6 = k I [p k ≤ p e k (w)] /P k (p, y) e −k (w)), y I [p k ≤ p e k (w)]

P k min p, (p k, p =

P k (p, y) e (w), y

P k min p, p =

P k (p, y) I [p k ≤ p e k (w)].

(c) For the marginal distribution in option k, we have Pr w ≤ W ω (y − p k, k) =

## X

ω Pr w ≤ W ω (y − p k, k), j = J ω (p 0, y) ω j =

## X

e −k (w)), y I [p k ≤ p e k (w)]

P j,k p 0, (p k, p j e −k (w)), y I [p k ≤ p e k (w)].

= P k (p k, p (d) Finally, for the marginal distribution, in the optimal option, we have h i Pr w ≤ W ω y − p J ω (p,y), J ω (p, y) ω =

## X

=

## X

k Pr w ≤ W ω (y − p k, k), k = J ω (p, y) ω e (w), y I [p k ≤ p e k (w)].

P k min p, p k

Corollary 2 When using reference prices p ref, we have h i i h ref.

Pr w ≤ M M U p ω ref (y − p k, k), j = J ω (p 0, y) = P j,k p 0, (p k, y−w+p ref −k ), y I p k ≤ y − w + p k ω When p k = p 0 k, and the reference prices equal the actual prices p 0 and k is the optimal choice, this simplifies to h i Pr w ≤ M M U p ω 0 y − p 0 k, k, k = J ω (p 0, y) = P k (p 0, y)I [w ≤ y] ω and, hence, h i Pr w ≤ M M U p ω 0 y − p 0 k, k | k = J ω (p 0, y) = I [w ≤ y], ω h Pr w ≤ M M U p ω 0 y − p 0 J ω (p 0,y), J ω (p 0, y) ω i = I [w ≤ y].

e (w) = y − w + p ref (w) into EquaProof of Corollary 2. The first equation follows from plugging p h i tion (14). Moreover, using actual prices p 0 as reference prices and taking p k = p 0 k, I p k ≤ y − w + p ref k implies that w ≤ y. Therefore, h i Pr w ≤ M M U p ω 0 y − p 0 k, k, k = J ω (p 0, y) = P k min p 0, y − w + p 0, y I [w ≤ y)] ω 0 (49) = P k (p, y)I [w ≤ y)].

The last two equations then immediately follow from Bayes’ theorem and summing over k.

Proposition 1 The joint distribution of welfare in the optimal bundle i, before a price change, and welfare in the optimal bundle j, after the price change, is as follows:

Pr [w ≤ W 0 ω (y − p i, i), z ≤ W 1 ω (y − p 0 j, j), i = J ω (p, y), j = J ω (p 0, y)] ω h i e (w), min p 0, p e (z), y I [p i ≤ p e i (w)] I p 0 j ≤ p e j (z).

= P i,j min p, p

(19) Proof of Proposition 1. Pr [w ≤ W 0 ω (y − p i, i), z ≤ W 1 ω (y − p 0 j, j), i = J ω (p, y), j = J ω (p 0, y)] ω h U c ω 0 (y − p e c 0 (w)), = Pr U i ω (y − p i) ≥ max 0 ω c U j ω (y − p 0 j) ≥ max U l ω (y − p 0 l ), l6 = j = Pr h ω

U i ω (y − p i) ≥ max U k ω (y k6 = i U i ω (y − p i) ≥ max U k ω (y − p k ), k6 = i U j ω (y − p 0 j) ≥ max U c ω (y − p e c (z)), c

U j ω (y − min(p k, p e k (w))), h i i − p 0 j) ≥ max U l ω (y − min(p 0 l, p e l (z))) l6 = j i I [p i ≤ p e i (w)] I p 0 j ≤ p e j (z) = P i,j h i e −i (w), p 0 j, min p 0−j, p e −j (z), y I [p i ≤ p e i (w)] I p 0 j ≤ p e j (z) p i, min p −i, p h i e (w), min p 0, p e (z), y I [p i ≤ p e i (w)] I p 0 j ≤ p e j (z).

= P i,j min p, p

Theorem 2

The function h is defined by:

h i e (max(w, x)), min p 0, p e (s), y I p 0 j ≤ p e j (s) h i,j,p,p 0 (w, x, s) = P i,j min p, p h i e (w), p e (x), min p 0, p e (s), y I p 0 j ≤ p e j (s).

= P i,j min p, p Then, the joint distribution of the stochastic welfare measure and the difference before and after the price change of this measure becomes, Pr [w ≤ W 0 ω (y − p i, i), W 1 ω (y − p 0 j, j) − W 0 ω (y − p i, i) ≤ z, i = J ω (p, y), j = J ω (p 0, y)] = ω −

## Z +∞

−∞ (20) ∂ 3 h i,j,p,p 0 (w, x, x + z)I [p i ≤ min(p e i (w), p e i (x))] dx.

Proof of Theorem 2. Fix i and j and define g(w, z) = Pr ω [w ≤ W 0 ω (y−p i, i), z ≤ W 1 ω (y−p 0 j, j), i = J ω (p, y), j = J ω (p 0, y)]. Then we have Pr [w ≤ W 0 ω (y − p i, i), W 1 ω (y − p 0 j, j) − W 0 ω (y − p i, i) ≤ z, i = J ω (p, y), j = J ω (p 0, y)] ω = − = − = −

## Z +∞

−∞

## Z +∞

−∞

## Z +∞

−∞ ∂ 2 g (max(w, x), x + z) dx ∂ 3 h i,j,p,p 0 (w, x, x + z)I [p i ≤ p e i (max(w, x))] dx ∂ 3 h i,j,p,p 0 (w, x, x + z)I [p i ≤ min(p e i (w), p e i (x))] dx.

Lemma 2 We have n ω | CV ω ≤ z, i = J ω (p, y), j = J ω (p 0, y) o n (22) o = ω | U i ω (y − p i) ≥ max {U c ω (y − p 0 c − z)}, i = J ω (p, y), j = J ω (p 0, y).

c

Proof of Lemma 2.

n o ω | CV ω ≤ z, i = J ω (p, y), j = J ω (p 0, y) n = ω | max {U c ω (y − p 0 c − CV ω )} ≥ max {U c ω (y − p 0 c − z)}, i = J ω (p, y), j = J ω (p 0, y) c n = ω | o c max {U c ω (y c − p c )} ≥ max {U c ω (y c − p 0 c − z)}, i = J ω (p, y), j = J ω (p 0, y) n o o = ω | U i ω (y − p i) ≥ max {U c ω (y − p 0 c − z)}, i = J ω (p, y), j = J ω (p 0, y), c where the second equality follows from (21) and the last from i = J ω (p, y).

Theorem 3 The joint distribution of the CV and the optimal choices before and after the price change is as follows:

Pr [CV ω ≤ z, i = J ω (p, y), j = J ω (p 0, y)] = P i,j (min(p, p 0 + z), p 0, y)I p i ≤ p 0 i + z.

(23) ω

Proof of Theorem 3. We have Pr [CV ω ≤ z, i = J ω (p, y), j = J ω (p 0, y)] ω h = Pr U i ω (y − p i) ≥ max U k ω (y − p k ), ω k6 = i U j ω (y − p 0 j) ≥ max U l ω (y − p 0 l ), l6 = j i U i ω (y − p i) ≥ max U c ω (y − p 0 c − z) c = Pr ω h

U i ω (y − p i) ≥

I p i ≤ max U k ω (y k6 = i p 0 i + z − min(p k, p 0 k + z)), U j ω (y − p 0 j) ≥ max U l ω (y − p 0 l) i l6 = j = P i,j (min(p, p 0 + z), p 0, y)I p i ≤ p 0 i + z.

Corollary 3 Pr [CV ω ≤ z | i = J ω (p, y), j = J ω (p 0, y)] = ω Pr [CV ω ≤ z | i = J ω (p, y)] = ω P i,j (min(p, p 0 + z), p 0, y) I p i ≤ p 0 i + z, 0

P i,j (p, p, y) P i (min(p, p 0 + z), y) I p i ≤ p 0 i + z,

P i (p, y)

(24) (25) Pr [CV ω ≤ z | j = J ω (p 0, y)] = X P i,j (min(p, p 0 + z), p 0, y) ω

P j i I p i ≤ p 0 i + z, (p 0, y) (26) and

Pr [CV ω ≤ z] =

## X

ω

Theorem 4 P i (min(p, p 0 + z), y)I p i ≤ p 0 i + z. 33 (27) i The joint distribution of the MMU and the CV is as follows:

Pr [w ≤ M M U p ω 0 (y − p i, i), CV ω ≤ z, i = J ω (p, y), j = J ω (p 0, y)] ω = P i,j min p, p 0 + min(z, y − w), p 0, y I p i ≤ p 0 i + min(z, y − w).

(28) Proof of Theorem 4. A direct proof of Theorem 4

We have Pr [w ≤ M M U p ω 0 (y − p i, i), CV ω ≤ z, i = J ω (p, y), j = J ω (p 0, y)] ω h U c ω 0 (y − (y − w + p c 0 )), = Pr U i ω (y − p i) ≥ max 0 ω c

U j ω (y − p 0 j) ≥ max U l ω (y l6 = j − p 0 l ),

U i ω (y U i ω (y − p i) ≥ max U k ω (y − p k ), k6 = i − p i) ≥ max U c ω (y c h = Pr U i ω (y − p i) ≥ max U k ω (y − min(p k, p 0 k + y − w, p 0 k + z)), ω k6 = i

I p i ≤ = P i,j p 0 i + z I p i ≤ p 0 i + y − w i − p 0 c − z) i U j ω (y − p 0 j) ≥ max U l ω (y − p 0 l) l6 = j p i, min p −i, p 0−i + min(z, y − w), p 0, y I p i ≤ p 0 i + min(z, y − w) = P i,j min p, p 0 + min(z, y − w), p 0, y I p i ≤ p 0 i + min(z, y − w).

Theorem 4 as implied by Theorem 2 When choosing the MMU with the final prices as reference prices, Theorem 2 implies:

Pr [w ≤ M M U p ω 0 (y − p i, i), CV ω ≤ z, i = J ω (p, y), j = J ω (p 0, y)] ω = −

## Z +∞

−∞ ∂ 3 h i,j,p,p 0 (w, x, x + z)I p i ≤ min(p 0 i + y − w, p 0 i + y − x) dx.

(50) where the function h is defined by h i h i,j,p,p 0 (w, x, s) = P i,j min p, p 0 + y − max(w, x), min p 0, p 0 + y − s, y I p 0 j ≤ p 0 j + y − s.

(51) 33 Note that Equation (27) is the main result of Bhattacharya (2015).

Rewriting, (51), we obtain h h i,j,p,p 0 (w, x, s) = P i,j min p, p 0 + y − max(w, x), min p 0, p 0 + y − s, y I p 0 j ≤ p 0 j + y − s i = P i,j min p, p 0 + y − max(w, x), p 0, y I [s ≤ y], and hence ∂ 3 h i,j,p,p 0 (w, x, x + z) = −P i,j min p, p 0 + y − max(w, x), p 0, y δ(x + z − y), where δ is a Dirac delta function. Plugging this in in (50), we obtain Pr [w ≤ M M U p ω 0 (y − p i, i), CV ω ≤ z, i = J ω (p, y), j = J ω (p 0, y)] ω = −

## Z +∞

−∞ ∂ 3 h i,j,p,p 0 (w, x, x + z)I p i ≤ min(p 0 i + y − w, p 0 i + y − x) dx = P i,j min p, p 0 + y − max(w, y − z), p 0, y I p i ≤ min(p 0 i + y − w, p 0 i + y − (y − z)) = P i,j min p, p 0 + min(y − w, z), p 0, y I p i ≤ p 0 i + min(y − w, z) as in Theorem 4.

Corollary 4 h i Pr w ≤ M M U p ω 0, CV ω ≤ z | i = J ω (p, y), j = J ω (p 0, y) ω P i,j min p, p 0 + min(z, y − w), p 0, y =

P i,j I p i ≤ p 0 i + min(z, y − w), (29) (p, p 0, y) Pr [w ≤ M M U p ω 0 (y − p i, i), CV ω ≤ z | i = J ω (p, y)] ω P i min p, p 0 + min(z, y − w), y =

P i (p, y) I p i ≤ p 0 i + min(z, y − w), (30) Pr [w ≤ M M U p ω 0 y − p J ω (p,y), J ω (p, y), CV ω ≤ z | j = J ω (p 0, y)] ω = 0 0 X P i,j min p, p + min(z, y − w), p, y i

P j (p 0, y) I p i ≤ p 0 i + min(z, y − w), (31)

and, Pr [w ≤ M M U p ω 0 y − p J ω (p,y), J ω (p, y), CV ω ≤ z] ω =

## X

P i min p, p 0 + min(z, y − w), y I p i ≤ p 0 i + min(z, y − w). (32) i Proposition 2 The conditional CDF of individual welfare in the optimal bundle can be calculated using choice probabilities:

F W (w | p, y) = 1 −

## X

e (w), y I [p k ≤ p e k (w)].

P k min p, p (35) k

Proof of Proposition 2.

h F W (w | p, y) = Pr W ω y − p J ω (p,y), J ω (p, y) ≤ w i ω h = 1 − Pr w ≤ W ω y − p J ω (p,y), J ω (p, y) i ω =1 −

## X

(52) e (w), y I [p k ≤ p e k (w)],

P k min p, p k where the last equality follows from Equation (18) in Corollary 1.

Corollary 5 When prices are equal for everyone and when one uses the MMU with reference prices equal to those common prices as the welfare measure, the SWF can be written solely in terms of income.

Proof of Corollary 5. From Proposition 2 and the definition of the virtual prices in case of an MMU e (w) = y − w + p), it follows that with actual prices p as reference prices (p F W (w | p, y) = 1 −

## X

=1 −

## X

=1 −

## X

e (w), y I [p k ≤ p e k (w)]

P k min p, p k P k min p, y − w + p, y I [p k ≤ y − w + p k )] k P k p, y I [w ≤ y] k = I [y ≤ w].

Hence,

## Z Z

## SW F =

## Z Z

= h(w) dF W (w | p, y) dG(p, y) h(w)dI [y ≤ w] dG(p, y)

## Z

= h(y) dG(p, y).

Notice that p in the argument of G is redundant, as prices are assumed to be identical for all persons in this case. This completes the proof.

Proposition 3 Suppose Assumptions 1 – 3 hold. Then the transition probabilities {P i,j (p, p 0, y)} are set identified from the choice probabilities {P i} with bounds n

## L

P i,i (p, p 0, y) = max P i (p, y) + P i (p 0, y) − 1, P i max{p i, p 0 i }, min{p −i, p 0−i}, y o,

## U

(p, p 0, y) = min P i (p, y), P i (p 0, y).

P i,i For i 6 = j, P i,j (p, p 0, y) = 0 if p i ≥ p 0 i and p j ≤ p 0 j and

## L

P i,j (p, p 0, y) = max{P i (p, y) + P j (p 0, y) − 1, 0},

## U

P i,j (p, p 0, y) = min P i (p, y), P j (p 0, y), elsewhere.

Proof of Proposition 3. We will first derive upper and lower bounds that are implied by elementary probability theory. Denoting by A the set {ω|i = J ω (p, y)} and B the set {ω|j = J ω (p 0, y)}, we have P (A ∩ B) = P i,j (p, p 0; y), P (A) = P i (p; y) and P (B) = P j (p 0; y). For the lower bound, note that 1 ≥ P (A ∪ B) = P (A) + P (B) − P (A ∩ B) (53) and hence P (A ∩ B) ≥ P (A) + P (B) − 1 which translates into P i,j (p, p 0; y) ≥ P i (p; y) + P j (p 0; y) − 1.

(54) For the upper bound, note that P (A ∩ B) ≤ P (A) and P (A ∩ B) ≤ P (B) and hence P i,j (p, p 0; y) ≤ min(P i (p; y), P j (p 0; y)) (55) We will now exploit the monotonicity condition imposed on the utility function U c ω to construct tighter bounds based on revealed preference restrictions. First consider the no-transition case.

Note therefore that if U i ω (y − max{p i, p 0 i }) > U k ω (y − min{p k, p 0 k }), (56) then U i ω (y − p i) > U k ω (y − p k) and U i ω (y − p 0 i) > U k ω (y − p 0 k) and hence h P i (max{p i, p 0 i }, min{p −i, p 0−i }; y = Pr ∩ k6 = i U i ω (y − max{p i, p 0 i }) > U k ω (y − min{p k, p 0 k }) i ω (57) is a lower bound of P i,i (p, p 0; y). Finally, for the transition case, some transitions are ruled out by monotonicity. Indeed, if p i ≥ p 0 i and p j ≤ p 0 j, good i becomes weakly less and good j weakly more expensive after the price change. By monotonicity, it holds that U i ω (y − p i) ≤ U i ω (y − p 0 i) and U j ω (y − p j) ≥ U j ω (y − p 0 j) and hence, if moreover U i ω (y − p i) > U k ω (y − p k) for all k 6 = i and U j ω (y − p 0 j) > U k ω (y − p 0 k) for all k 6 = j, then U i ω (y − p 0 i) ≥ U i ω (y − p i) > U j ω (y − p j) > U i ω (y − p 0 i) (58) which is a contradiction. Hence, if p i ≥ p 0 i and p j ≤ p 0 j, then P i,j (p, p 0, y) = 0.

Proposition 4 Suppose Assumptions 1-3 hold. Then the estimated choice probabilities {P i} should satisfy the following shape restrictions at all (p, y) for all i, j ∈ C:

∂P i (p, y) ≤ 0, ∂p i ∂P i (p, y) ≥ 0, ∂p j Proof of Proposition 4. Remember that the choice probabilities are defined as

P i (p, y) = Pr ω n

U i ω (y − p i) ≥ max {U c ω (y c6 = i o − p c )}.

Given Assumption 1, the first restriction immediately follows from observing that an increase in p i would shrink the set {ω | U i ω (y − p i) ≥ max {U c ω (y − p c )} c6 = i and, hence, lowers the probability

Pr ω n o U i ω (y − p i) ≥ max {U c ω (y − p c )} c6 = i.

Analogously, an increase in p j with j 6 = i would increase P i (p, y).

## C

Empirical illustration

## C.1

Sample description

Table 2: Descriptive statistics estimation subsample

Variable

Weekly hours worked

Hourly gross wage

Yearly income from assets

Age

Years education

Number of children (all)

Number of children (0-1)

Number of children (2-4)

Number of children (5-7)

East Germany

## C.2

## N

Min

## Q 1

Median

Mean

## Q 3

Max

## SD

## IQR

## #NA

1922 1492 1922 1922 1922 1922 1922 1922 1922 1922 0.0 4.1 -5.0 18.0 7.0 0.0 0.0 0.0 0.0 0.0 0.0 9.5 0.0 34.0 10.5 0.0 0.0 0.0 0.0 0.0 30.0 14.0 3.0 45.0 11.5 0.0 0.0 0.0 0.0 0.0 25.2 14.9 260.8 43.3 12.2 0.5 0.0 0.0 0.1 0.2 40.0 19.0 131.5 53.0 14.0 1.0 0.0 0.0 0.0 0.0 80.0 39.7 11998.0 60.0 18.0 3.0 2.0 2.0 2.0 1.0 18.3 6.9 1085.5 11.1 2.8 0.8 0.1 0.2 0.3 0.4 40.0 9.5 131.5 19.0 3.5 1.0 0.0 0.0 0.0 0.0 0 430 0 0 0 0 0 0 0 0

Estimation procedure Choice probabilities To model the choice probabilities for alternatives PT and FT, we specify for each a flexible binary logit model that contains cubic polynomials for the disposable income of all three alternatives, and a linear index with demographic variables, such as individual `’s age, years of education, number of children, and region. Formally, we have for c ∈ {P T, F T} that ω Pr [c = J (d `) | x `]:= Λ c (d `, x `; θ c) = 1 + exp − α c + ω 3

## X X

!!! −1 β c,c 0,m d m `,c 0 + x ` 0 γ c, c 0 m=1 where d `:= (d N W,`, d P T,`, d F T,`) is a vector with disposable incomes, x ` a vector with demographic characteristics, and θ c = (α c, β c, γ c) a vector with parameters. Alternative NW is defined as the complement of these two probabilities, Pr [N W = J ω (d `) | x `]:= 1 − Pr [P T = J ω (d `) | x `] − Pr [F T = J ω (d `) | x `] ω ω ω = 1 − Λ P T (d `, x `; θ P T) − Λ F T (d `, x `; θ F T ), which ensures that for every pair (d `, x ` ), the choice probabilities add up to one. The model is then estimated by nonlinear least squares b θ

## N LS

= arg min (θ P T,θ F T)

X h [Y N W,` − (1 − Λ P T (d `, x `; θ P T) − Λ F T (d `, x `; θ F T ))] 2 ` i + [Y P T,` − Λ P T (d `, x ` ); θ P T )] 2 + [Y F T,` − Λ F T (d `, x ` ); θ F T )] 2 + π(x `; θ P T, θ F T), where {Y c,`, c ∈ {N W, P T, F T }} are dummy variables that encode individual `’s observed choice. The last term, i.e. π(x `; θ HT, θ F T ), contains a positive-valued penalty function that imposes nonnegativity of Pr ω [N W = J ω (d `) | x `] and the shape constraints discussed in Section 5.2.

Penalty function The penalty function consists of three components. Since some of these components depend in a complex way on both the data and the parameters, we opt to impose these on a three dimensional grid D G of disposable incomes: i.e. D G ⊂ D:= supp(d N W) × supp(d P T) × supp(d F T ). The first component of the penalty function ensures that the choice probability of alternative NW is non-zero for every pair (d g, x `) ∈ D G × X: i.e. 1 − Λ P T (d g, x `; θ P T) − Λ F T (d g, x `; θ F T) ≥ 0. The contribution to the penalty function then is defined as:

π 1 (x `; θ P T, θ F T):= −|D G | −1

## X

min(0, 1 − Λ P T (d g, x `; θ P T) − Λ F T (d g, x `; θ F T )).

d g ∈D G The second component of the penalty function ensures that choice probabilities for alternatives PT and FT are increasing in their own disposable income and decreasing in the disposable income of the other alternatives. To be precise, we have for every c ∈ {P T, F T} and for every pair (d g, x `) ∈ D G × X that ∂Λ c (d g, x `; θ c) = (β c,c,1 + 2β c,c,2 d g,c + 3β c,c,3 d 2 g,c )Γ c (d g, x `; θ c) ≥ 0 ∂d g,c ∂Λ c (d g, x `; θ c) = (β c,c 0,1 + 2β c,c 0,2 d g,c 0 + 3β c,c 0,3 d 2 g,c 0 )Γ c (d g, x `; θ c) ≤ 0, ∂d g,c 0 in which Γ c (d g, x `; θ c):= Λ c (d g, x `; θ c) 1 + exp α c +

## P P 3

c 0 m m=1 β c,c 0,m d g,c 0 ∀c 0 6 = c, + x ` 0 γ c −1, or equivalently that β c,c,1 + 2β c,c,2 d g,c + 3β c,c,3 d 2 g,c) ≥ 0 (β c,c 0,1 + 2β c,c 0,2 d g,c 0 + 3β c,c 0,3 d 2 g,c 0) ≤ 0, ∀c 0 6 = c.

The contribution to the penalty function is defined as:

π 2,c (θ P T, θ F T):= −|D G | −1

## X

min(0, β c,c,1 + 2β c,c,2 d g,c + 3β c,c,3 d 2 g,c )) d g ∈D G −1 π 2,c,c 0 (θ P T, θ F T):= |D G |

## X

max(0, β c,c 0,1 + 2β c,c 0,2 d g,c 0 + 3β c,c 0,3 d 2 g,c 0 )).

d g ∈D G Finally, the third part of the penalty function ensures that the choice probability of alternative NW is decreasing in the disposable income of the other alternatives. 34 For every c, c 0 ∈ {P T, F T} with

34 Note that the second part of the penalty function also ensures that the choice probability of alternative NW is increasing in its own disposable income.

c 6 = c 0 and for every pair (d g, x `) ∈ D G × X, we have that ∂Λ c (d g, x `) ∂Λ c 0 (d g, x `) + = (β c,c,1 + 2β c,c,2 d g,c + 3β c,c,3 d 2 g,c )Γ c (d c, x `; θ c) ∂d g,c ∂d g,c + (β c 0,c,1 + 2β c 0,c,2 d g,c + 3β c 0,c,3 d 2 g,c )Γ c 0 (d g, x `; θ c 0) ≥ 0.

The contribution to the penalty function is defined as:

π 3,c,c 0 (x `; θ P T, θ F T):= −|D G | −1

## X

min(0, (β c,c,1 + 2β c,c,2 d g,c + 3β c,c,3 d 2 g,c )Γ c (d g, x `; θ c) d g ∈D G + (β c 0,c,1 + 2β c 0,c,2 d g,c + 3β c 0,c,3 d 2 g,c )Γ c 0 (d g, x `; θ c 0 )).

Arranging all components, the composite penalty function is then  π(x `; θ P T, θ F T) = π 1 (x `; θ P T, θ F T) +

## X



## X

 π 2,c (θ P T, θ F T) + π 2,c,c 0 (θ P T, θ F T)  c 0 ∈{N W,P T,F T },c 0 6 = c c∈{P T,F T} + π 3,P T,F T (x `; θ P T, θ F T) + π 3,F T,P T (x `; θ P T, θ F T ).

## C.3

Estimates Table 3 contains the estimates for the choice probabilities of alternatives PT and FT. The 90% confidence intervals are obtained by a bootstrap procedure, in which the model was re-estimated on 200 samples randomly drawn with replacement.

Table 3: Estimates choice probabilities

## PT

Parameter

Constant (d 0 /1000) (d 0 /1000) 2 (d 0 /1000) 3 (d 20 /1000) (d 20 /1000) 2 (d 20 /1000) 3 (d 40 /1000) (d 40 /1000) 2 (d 40 /1000) 3

Age

Years education

Number of children

Number of children

Number of children

Number of children

East Germany

Estimate (0-1) (2-4) (5-7) (all) -1.82 0.00 0.00 0.00 0.51 -0.29 0.06 0.00 -0.05 0.01 0.01 -0.01 -2.72 -0.67 0.26 0.17 -0.06

## FT

## 90% CI

[-2.18, [-0.06, [-0.01, [-0.08, [0.01, [-0.27, [0.00, [-0.06, [-0.22, [0.00, [0.00, [-0.03, [-3.50, [-1.29, [-0.15, [0.06, [-0.37, -1.25] 0.00] 0.08] 0.00] 0.65] 0.00] 0.07] 0.00] 0.00] 0.03] 0.02] 0.03] -2.29] -0.42] 0.45] 0.39] 0.04]

Estimate -2.41 -0.01 -0.08 -0.04 -0.14 0.06 -0.01 1.09 -0.27 0.03 -0.01 0.13 -2.62 -1.08 -0.29 -0.20 0.13

## 90% CI

[-4.00, [-0.02, [-0.20, [-0.13, [-0.20, [-0.02, [-0.06, [0.95, [-0.60, [0.01, [-0.01, [0.10, [-3.42, [-1.18, [-0.50, [-0.49, [-0.02,

-2.30] 0.00] 0.06] 0.04] 0.00] 0.14] 0.00] 2.50] -0.16] 0.05] 0.00] 0.15] -2.26] -0.55] -0.01] -0.13] 0.35]

## C.4

Calculation distribution of welfare differences conditional on initial welfare The practical implementation of the results in Theorem 2 poses some difficulties. Firstly, the distribution depends on transition probabilities. As was noted in Section 5, with only cross-sectional data available, these transition probabilities can only be set-identified. We, therefore, calculated upper and lower bounds for the joint distribution of baseline and reform welfare levels (i.e. Equation (19) of Proposition 1). As lower and upper bounds in the aggregate are not far apart (at most a 4 percentage point difference), we continue the analysis using only the upper bound. Secondly, Equation (20) requires integration over the derivative of a transition probability, which is quite cumbersome.

Implementation We first calculate the joint distribution of baseline and reform welfare by integrating out the optimal baseline and reform choices in Equation (19) of Proposition 1. The resulting joint distribution function of initial and post reform welfare is denoted by H 0 (w, s), that is:

H 0 (w, s) = P r (w ≤ W 0, s ≤ W 1) =

## P

i,j∈{N W,P T,F T} Pr ω h i w ≤ W 0 ω (y − p i, i), s ≤ W 1 ω (y − p 0 j, j), i = J ω (p, y), j = J ω (p 0, y).

(59) As we are interested in this distribution at the population level rather than at the individual level, we aggregate the distribution H 0 by defining

## Z

H(w, s) = H 0 (w, s) dG(p, p 0, y), (60) where G is the distribution of prices and exogenous income in the population. The joint distribution of baseline welfare and the welfare gain, P r (w ≤ W 0, z ≥ W 1 − W 0 ), is then calculated by:

P r (w ≤ W 0, z ≥ W 1 − W 0) =

## R

P r (w ≤ W 0, s − z ≤ W 0, s = W 1) ds

## R

= − ∂ 2 H(max(w, s − z), s) ds.

(61) The integral and derivative in this equation can be approximated numerically. Note that this is an approximation of Equation (20), aggregated across the population. The distribution of gains and losses conditional on the initial welfare level can then be calculated as follows:

P r (z ≤ W 1 − W 0 |w = W 0) = P r (z + w ≤ W 1 |w = W 0) =

P r(z+w≤W 1,w=W 0)

P r(w=W 0) = ∂ 1 H(w,z+w) ∂ 1 H(w,−∞).

Again, derivatives can be computed numerically.

(62)

## C.5

Additional tables and figures Individual welfare distribution Figure 10 shows the estimates of the individual unconditional welfare distributions (i.e. Equation (18) in Corollary 1). Similarly as for the individual conditional distributions in the main text (i.e. Figure 4), these distributions reflect either the econometrician’s uncertainty about an individual’s welfare level, or the distribution of the actual levels obtained by individuals in the population with the same observable characteristics (i.e. prices, exogenous income, and demographic variables). The difference is, however, that now we take into account that some may have found another optimal alternative instead of that chosen by the sampled individual, contrary to what was the case for the conditional individual welfare distributions in Figure 4 of the main text.

Figure 10: Unconditional individual welfare distribution by wage quartile

Social welfare In Table 4, we present baseline and post-reform estimates of social welfare, i.e.

Equation (34), for some members of the Atkinson-Kolm-Sen class of social welfare functions. This class is defined by specifying the concave transformation h(w) in Equation (34) as h(w) = ε ≥ 0. 35 w 1−ε 1−ε for The calculations are performed using the result of Proposition 2.

As the class of Atkinson-Kolm-Sen functions obeys the first-order stochastic dominance criterion, i.e. all members of the class rank a distribution that first-order dominates another as the better one of 35 The parameter ε is called the degree of inequality aversion. When ε equals zero, the social welfare function amounts to the average individual welfare level. As ε increases, more weight is given to individuals with lower welfare.

the two, it stands to reason that the reform distribution generates higher social welfare than the one for the baseline for all values of ε.

Table 4: Social welfare of the Atkinson form for baseline and reform (in euro)

Winners and losers ε 0 0.5 5

Baseline

Reform 1,815 1,925 1,783 1,897 1,530 1,673 Figures 11 and 12 plot the joint distribution of baseline welfare and welfare differences (i.e. Equation (61)). In Figure 11, the coordinates (w, z) of a point on the x-th isocontour indicate the initial welfare level w and welfare gain z (or loss if z is negative) such that x% of the population obtains at least that initial welfare level w and does not gain more than z. In Figure 12, the initial welfare level w denotes the maximum level, rather than the minimum, that that number of people reach.

Figure 11: Joint distribution of baseline welfare and welfare gains/losses: W 0 ≥ w Figure 13 shows a more detailed, and less smoothed, version of the distribution of gains and losses conditional on baseline welfare (Figure 8 of the main text). The upper boundary of the yellow region tends to be lower than zero for higher welfare levels. For higher initial welfare levels, there are several regions where the median, that is the lower bound of the blue region, falls under the zero of the vertical axis. This confirms the findings highlighted in the main text.

Figure 12: Joint distribution of baseline welfare and welfare gains/losses: W 0 ≤ w Figure 14 shows the same conditional distribution of gains and losses, but now disaggregated per wage quartile and baseline choice. Gainers seem to be predominantly situated among individuals choosing alternatives PT and FT, especially in the lower half of the wage distribution, and among the initially poor persons with higher wages. Remarkably, high wage persons who initially choose NW tend to lose out.

Figure 13: Distribution of welfare gains and losses, conditional on baseline welfare Figure 14: Distribution of welfare gains and losses, conditional on baseline welfare: by alternative chosen and wage quartile
