# Economic Theory (2019) 68:765–786

## RESEARCH ARTICLE

Well-being measurement with non-classical goods Marc Fleurbaey 1 · François Maniquet 2 Received: 28 September 2017 / Accepted: 10 August 2018 / Published online: 17 August 2018

## Abstract

As in Fleurbaey and Maniquet (Math Soc Sci 90:119–126, 2017, Int J Econ Theory 14(1):35–50, 2018), we construct individual well-being measures that respect individual preferences and depend on the bundles of goods consumed by the individual. We show that the results obtained under the assumption that all available goods are desirable (more is preferred) and cardinal (convex combination of bundles are meaningful) do not generalize to the case in which goods are ordinal or not always desirable. We justify new measures. We conclude by showing that in a general case with goods of all natures, putting all results together allows us to define a short list of families of well-being measures.

Keywords Fairness · Well-being measure · Preferences · Non-classical goods

JEL Classification D63 · I32

1 Introduction There is a long tradition in economics consisting in comparing individuals on the basis of the bundles they consume. Income inequality measurement is clearly the main origin of this tradition. Following Tinbergen (1953), Foley (1967) and Kolm We thank two reviewers for their excellent comments. The research leading to these results has received funding from the European Research Council under the European Union’s Seventh Framework Programme (FP7/2007-2013)/ERC Grant Agreement No. 269831. The revision of the paper was carried out, while Maniquet was visiting the Department of Economics at University College London. Partial financial support from the Leverhulme Trust is gratefully acknowledged.

## B

François Maniquet francois.maniquet@uclouvain.be

Marc Fleurbaey mfleurba@princeton.edu 1 Woodrow Wilson School, Princeton University, Princeton, NJ 08544, USA 2 CORE, Université catholique de Louvain, Voie du Roman Pays 34, 1348 Louvain-la-Neuve, Belgium (1968), the theory has also developed without immediate reference to income but on the basis of the description of the different dimensions of individuals’ consumption and by taking account of agents’ preferences. We follow this tradition here by raising the question of well-being measurement. That is, we raise the question of how to construct interpersonal comparisons of wellbeing on the basis of fairness principles bearing on the quantities of goods agents consume and on their preferences. The possibility of constructing well-being measures on the basis of fairness principles was explored in Fleurbaey and Maniquet (2011, 2017, 2018). As an outcome of these works, two main families of well-being measures were characterized. The first family contains (but is larger than) the ray utility measures. They measure well-being by reference to the fraction of a reference bundle to which the agent is indifferent. This well-being measure bears some clear relationship with the Pazner and Schmeidler (1978) egalitarian equivalent allocation rule that has played a prominent role in the theory of resource allocation (see Thomson 2010). The second family contains (but is larger than) the money-metric utility measures. They measure well-being of an individual by reference to the income that would be necessary to buy a bundle equivalent to their actual consumption at fixed prices. This well-being measure bears some clear relationship with the equal-income Walrasian allocation rule that has also played a prominent role in the theory of resource allocation (see Thomson 2010). Ray utility and money-metric utility are actually classical concepts (see, among others, Samuelson 1974, Samuelson and Swamy 1974, and Deaton 1979). For instance, Samuelson 1977 mentions the former as an example of a utility function that could be used in a Bergson–Samuelson social welfare function. The latter has been criticized by Donaldson (1992) and recently defended by Fleurbaey and Blanchet (2013). In this paper, we continue the analysis of Fleurbaey and Maniquet (2011, 2017, 2018) by relaxing the assumptions on the nature of the goods. Indeed, these previous works were developed under the assumption that goods are classical, that is, they are desirable in the sense that more of each good is always preferred, and they are cardinal in the sense that convex combinations of quantities are meaningful. We relax these two assumptions here. In a first model, we assume that goods are ordinal, that is, it is meaningful to rank quantities but differences in quantities cannot be compared, so that convex combinations of goods are not meaningful. An example is the quality of a commodity of which agents typically consume one unit, such as housing or car. We then show that the same basic properties that characterize two families of well-being measures in the classical case only characterize one family in this case. This compatibility between the two basic requirements is reminiscent of Chambers and Miller (2014a, b) analysis of indices of efficiency of production and influence of scientists. We explain the similarity in Sect. 4. In a second model, we assume that goods are not necessarily desirable, that is, more is not always better. We also assume that goods may come in discrete quantities. Formally, we assume that quantities of goods take values in a compact set and preferences are such that satiation can occur. Typical examples are health, for which we may see perfect health as a natural upper bound, hours of work, theater tickets, etc. We prove that our two basic properties still characterize one and only one family of well-being

Well-being measurement with non-classical goods measures but, at the same time, another family, which we also characterize, seems to capture equally well the particular nature of the goods. Finally, we show that when there are goods of different types so that the relevant model should be one that encompasses all the others, then the different families of well-being measures can be combined to define four families. We view the contribution of this paper (and companion papers Fleurbaey and Maniquet 2017, 2018) as consisting of providing well-being indices that can be (and should be) used to compute social indices, in particular inequality and poverty measures (as in Decancq et al. forthcoming, 2015). Interestingly, the theoretical literature on inequality and poverty measurement is almost entirely developed under the assumption that goods are classical (see Bosmans et al. 2017 and Gravel et al. 2015, for recent exceptions), whereas it is common in applications to have information about goods the nature of which is among the ones we study in this paper. The paper is organized as follows. In the next section, we first introduce the classical model with divisible goods and recall the results obtained by Fleurbaey and Maniquet (2017, 2018) with the two basic properties. Then, in Sect. 3, we relax the assumption that convex combinations of goods are meaningful. In Sect. 4, we study the case in which quantities of goods take values in a compact set and preferences are not necessarily monotonic in all dimensions. In Sect. 5, we combine the models and their solutions. In Sect. 6, we present all the formal proofs. In Sect. 7, we give some concluding comments.

2 Two general families In the classical model, as in Fleurbaey and Maniquet (2017, 2018), there are K divis-

K and over this set, individual preferences ible goods. The consumption set is X = R + are assumed to be classical, that is, continuous, convex and monotonic. 1 These are the assumptions that we relax in the next sections. Let R cl denote the set of all such preferences.

A well-being measure is a function W: X × R cl → R, such that W (x, R) is the well-being level of an agent consuming bundle x with preferences R. Observe that W does not depend on any additional data; in particular, it does not depend on subjective well-being of the sort measured by happiness surveys, as the only subjective information used by W is contained in the ordinal preference ordering

## R.

Throughout the paper, we require W to respect individual preferences, in the sense that for all x, x ∈ X, R ∈ R cl, x R x ⇔ W (x, R) ≥ W (x, R).

The latter condition is reminiscent of Pareto efficiency in the social choice literature. Here, it represents our desire to define well-being in a way that is consistent with 1 We use >, and to denote the vector inequalities. Preferences R are monotonic if and only if x > x implies x R x and x x implies x P x.

what agents themselves think about how the different dimensions of life should be For x ∈ X, R ∈ R cl, we let L(x, R), U (x, R) and I (x, R) denote the lower, upper and indifference contour of R at x, respectively:

## K

|x R x },

L(x, R) = {x ∈ R +

## K

|x R x}, U (x, R) = {x ∈ R + I (x, R) = L(x, R) ∩ U (x, R).

We now present the two basic properties that we would like to impose on wellbeing measures. Supremum Nested Contour requires that if the lower contour set of one agent lies in the interior of the union of the lower contour sets of two other agents, then the well-being of the former agent is strictly lower than that of at least one of the latter agents. Axiom 1 Supremum Nested Contour For all x, x, x ∈ X, all R, R, R ∈ R cl, if L(x, R) ⊂ interior[L(x, R) ∪ L(x, R )], then W (x, R) < max{W (x, R ), W (x, R )}. Figure 1 illustrates this property. According to Supremum Nested Contour, the situation (x, R) cannot be at least as good as the two other situations. Indeed, as soon as the agent with preferences R consumes a bundle indifferent to x, then either she agrees with an agent with preferences R that x is a better bundle, or with an agent with preferences R that x is a better bundle, or with both. The normative meaning of the axiom is discussed in Fleurbaey and Maniquet (2017). We summarize it here. First, because well-being measures are required to respect preferences, the well-being level associated to all bundles in one indifference surface needs to be the same. We can even think of well-being measures as associating numbers to lower (or upper) contour sets. Second, for every bundle on the indifference surface of R through x there is a bundle on the indifference surface of R through x that is strictly preferred by both R and R, or a bundle on the indifference surface of R through x that is strictly preferred by both R and R, or both. As a result, consuming x with preferences R cannot be associated to a larger well-being level than both consuming x with preferences R and x with preferences R. The characterization of well-being measures satisfying Supremum Nested Contour is recalled in the following lemma (Th. 1 in Fleurbaey and Maniquet 2017). When a well-being measure W satisfies Supremum Nested Contour, well-being is measured according to a maximization process involving some reference preferences, called R w in the lemma. Such reference preferences need to satisfy some conditions in order to make this maximization process a well-defined one. The definition of these conditions requires the following terminology. The Leontief envelope of a set A ⊂ X is defined as

## LE(A) = ∂

{y ∈ X | y ≥ x}, x∈X ,x≤A

2 As W represents continuous monotonic preferences, it must be continuous almost everywhere. As a consequence, it is unlikely that interesting cases can emerge in absence of continuity. We explain the role it plays in our result in footnote 4 after Lemma 1.

Well-being measurement with non-classical goods

## R

x x

## R

0 x

## R

good 1 Fig. 1 Supremum Nested Contour: W (x, R) < max{W(x, R ),W(x, R )} where x ≤ A means that x ≤ a for every a ∈ A, and ∂ A denotes the lower frontier of A. The Leontief envelope can alternatively be defined as the lower frontier of the smallest set (with respect to set inclusion) that contains A and is a translation of the positive orthant. We are now equipped to define the conditions that reference preferences R w need to satisfy. These conditions define the subset R w of preferences. Preferences R belong to R w if and only if: (i) for every x ∈ X, there exists a compact C ⊂ X such that I (x, R) \ C = LE (U (x, R)) \ C; (ii) for every x ∈ X, there exists z ∈ X such that x ≤ U (z, R). Condition (i) says that I (x, R) has the shape of a Leontief indifference set beyond a certain distance from the origin (that is, beyond some compact C). Condition (ii) says that U (z, R) goes to infinity in all directions when z goes to infinity. Fleurbaey and Maniquet (2017) prove in an appendix that conditions (i) and (ii) are necessary and sufficient for the following property: all R w ∈ R w have a maximal bundle over each lower contour set of each R ∈ R cl, and W (·, R w) increases continuously with these lower contour sets. 3 For instance, linear preferences do not have maximal bundles over lower contours drawn from Cobb–Douglas preferences, nor from any other preferences with non-compact lower contour sets. Consequently, linear preferences do not belong to the subdomain R w. Cobb–Douglas preferences do not have maximal bundles over lower contours drawn from Leontieff preferences, for instance, and, therefore, cannot be used as reference preferences either. Leontieff preferences, on the contrary, do belong to R w. 3 We can state this property more formally as follows: for all R ∈ R, max{W (x, R w) | x ∈ L(x ∗, R)} exists for all x ∗ ∈ X and is continuous in x ∗.

This definition of subdomain R w allows us to state the following characterization of well-being measures satisfying Supremum Nested Contour. Lemma 1 A well-being measure W over X satisfies Supremum Nested Contour if and only if there exists R w ∈ R w such that W satisfies: for all x ∈ X and R ∈ R cl:

W (x, R) = max x ∈L(x,R)

W (x, R w ).

Observe that the reference preferences R w have the property that for all bundle x ∈ X and preferences R, W (x, R) ≥ W (x, R w ), that is having preferences R w makes the experience of consuming x the worst experience in terms of well-being.

Consequently, R w may qualify as the worst preferences in the domain.

Ray utility is the well-being measure one obtains if R w are of the Leontief type. Let

## K

S −1 denote the (K − 1)-dimensional simplex. Preferences R are Leontief if there exists ∈ interior[S K −1 ], such that x R x ⇔ min k∈K x x k ≥ min k.

k∈K k k If a well-being measure satisfies Supremum Nested Contour with R w = R for some ∈ interior[S K −1 ], then the well-being of an agent is measured by the bundle that is proportional to and to which this agent is indifferent. To put it differently, we say that W (x, R) = W (x, R) if and only if there exists some number λ ∈ R + such that x I λ and x I λ as well. All the well-being measures satisfying this property are ordinally equivalent to the ray utility W, defined by: for all x ∈ X, all R ∈ R cl, W (x, R) = w ⇔ x I w.

Ray utility is illustrated in Fig. 2. In this family, Fleurbaey and Maniquet (2018) prove that all concave transforms of the ray utility do satisfy and are the only ones to satisfy an inequality aversion property

K of goods increases well-being requiring that the allocation of an increment ∈ R ++ 4,5 more the lower the initial well-being of the agent. The second property, Infimum Nested Contour, is dual to Supremum Nested Contour with respect to the lattice structure 6 of the set of lower, or upper or indifference contours associated to R cl (a complete analysis of the influence of this lattice structure on 4 More precisely, the contribution of Fleurbaey and Maniquet (2018) consists in studying several versions of this inequality aversion property and identify the ones that are compatible with Supremum Nested Contour and Infimum Nested Contour that we define below. 5 Lemma 1 is no longer true in absence of the assumption of continuity of W. Take the Leontief R preferences as worst preferences, and take a representation of R that has a right-continuous jump at, and assume that non-Leontief indifference surfaces containing have a strictly lower value than the Leontief curve at, equal to the left limit of the R representation at. Everywhere else W is the standard function with R as worst preferences. This violates the Lemma, but satisfies Supremum Nested Contour. 6 A lattice structure consists of a partially ordered set in which every two elements have a unique supremum and a unique infimum.

Well-being measurement with non-classical goods

## R

p v p 2 x 0 good 1 Fig. 2 Illustration of W: W (x, R) = w, and W p: W p (x, R) = v our result of well-being measurement is proposed in Fleurbaey and Maniquet 2017). Infimum Nested Contour requires that if the upper contour set of one agent lies in the interior of the convex hull 7 of the union of the upper contour sets of two other agents, then the well-being of the former agent is strictly larger than that of at least one of the latter agents. Let C H denote the convex hull operator. Axiom 2 Infimum Nested Contour For all x, x, x ∈ X, all R, R, R ∈ R cl, if U (x, R) ⊂ interior[C H (U (x, R) ∪ U (x, R ))], then W (x, R) > min{W (x, R ), W (x, R )}. Figure 3 illustrates the property. The situation (x, R) cannot be as bad as the two other situations. The normative justification of this axiom builds on the observation that any bundle on the indifference surface of R through x can be obtained as a convex combination of a bundle on the indifference surface of R through x and a bundle on the indifference surface of R through x (whereas the converse is not true). In this sense, the indifference surface of R through x is intermediary of the two others, so that it cannot be associated to a lower well-being than both of them. For a similar reason as for Supremum Nested Contour above, the characterization of well-being measures satisfying Infimum Nested Contour requires that we define a subdomain of preferences. We denote R b the subdomain of preferences R b exhibiting the property that L(x, R b) is compact for all x ∈ X. The following lemma is Theorem 2 in Fleurbaey and Maniquet (2017).

7 The convex hull of a set is the smallest convex set, with respect to inclusion, that contains that set.

## R

x x

## R

x 0

## R

good 1 Fig. 3 Infimum Nested Contour: W (x, R) > min{W (x, R ), W (x, R )} Lemma 2 A well-being measure W over X satisfies Infimum Nested Contour if and only if there exists R b ∈ R b such that W satisfies: for all x ∈ X and R ∈ R cl:

W (x, R) = min x ∈U (x,R)

W (x, R b ).

Observe that the reference preferences R b have the property that for all bundle x ∈ X and preferences R, W (x, R) ≤ W (x, R b ), that is having preferences R b makes the experience of consuming x the best experience in terms of well-being. Consequently, R b may qualify as the best preferences in the domain. In a parallel way to Supremum Nested Contour, Fleurbaey and Maniquet (2018) study the consequences of combining Infimum Nested Contour with requirements of inequality aversion. 8 They prove that it leads to preferences R b being linear. Preferences R p are linear if there exists p ∈ interior[S K −1] such that x R p x ⇔ k∈K p k x k ≥ p k x k.

k∈K With linear R b, the well-being measures are ordinally equivalent to the moneymetric utility, introduced by Samuelson (1974) and Samuelson and Swamy (1974). In their definition, the p vector stands for a vector of prices, and the money-metric utility at (x, R) is the minimal expenditure a consumer with preferences R would incur, facing price vector p, to reach the same satisfaction as at x. Instead on relying on the expenditure function terminology, we can define W p by using the following 8 In this case too, inequality aversion requires that the allocation of an increment ∈ R K of goods ++ increases well-being more the lower the initial well-being of the agent.

Well-being measurement with non-classical goods function: for a set of bundles B ⊂ X, for R ∈ R, we write max(R, B) to denote any bundle in B that maximizes R over B, that is, max(R, B) = x only if x ∈ B and x R x for all x ∈ B. For all x ∈ X, all R ∈ R cl, W p (x, R) = w ⇔ x I max(R, {x ∈ X | px ≤ w}).

Money-metric utility is illustrated in Fig. 2. The well-being functions characterized in Fleurbaey and Maniquet (2018) are strictly concave transforms of W p. The normative justification of Infimum Nested Contour presented above may draw our attention on the following fact: bundle x may be a convex combination of bundles x and x, whereas x is strictly preferred to x according to R and x is strictly preferred to x according to R. We can get rid of this case by simply requesting that the upper contour at x be contained in the union (instead of the convex hull of the union) of the upper contours of the two other bundles. As a result, every bundle on the indifference surface of R through x is either strictly preferred to x by R or to x by R or both. We obtain the following weakening of Infimum Nested Contour. 9 Axiom 3 Infimum Nested Contour* For all x, x, x ∈ X, all R, R, R ∈ R cl, if U (x, R) ⊂ interior[U (x, R) ∪ U (x, R )], then W (x, R) > min{W (x, R ), W (x, R )}. From now on, we will refer to Infimum Nested Contour when the convex hull condition is imposed, and to Infimum Nested Contour* when it is not. Contrary to Infimum Nested Contour, Infimum Nested Contour* is compatible with Supremum Nested Contour. The main result of this section is a characterization of the family of well-being measures that satisfy Supremum Nested Contour and Infimum Nested Contour*. The key notion is that of a monotone consumption path. It is a set of bundles, starting at the origin of the consumption set and increasing continuously and unboundedly

K is a monotone consumption path toward strictly larger bundles. We say that P ⊂ R + if – – – –

## 0 K = (0,..., 0) ∈ P,

x, or x x or x = x, for all x, x ∈ P, either x

P is homeomorphic to R +, K, there exists x ∈ P such that r x.

for all r ∈ R + Rays are special examples of monotone consumption paths. Observe that a monotone

K, all R ∈ R cl, consumption path P is constructed in such a way that for all x ∈ R + there exists one and only one p ∈ P such that x I p. Theorem 1 A well-being measure W satisfies Supremum Nested Contour and Infimum Nested Contour* if and only if there exists a monotone consumption path P and a

K, all R ∈ R, strictly increasing function w: P → R + such that for all x ∈ R + W (x, R) = w(p) for p ∈ P such that x I p. 9 We thank an anonymous referee for having suggested this axiom.

The careful reader may have realized that Infimum Nested Contour* is no longer grounded on the lattice structure of indifference surfaces over the classical domain of preferences. A different kind of proof than the ones developed in Fleurbaey and Maniquet (2017) is therefore needed. We present this proof in Sect. 6.

3 Ordinal desirable goods In this section, we drop the assumption that convex combinations of goods are meaningful, that is we keep the assumption that all goods are desirable (preferences are monotonic), but the measure of amounts of the available goods is purely ordinal. Typical examples of such goods include subjective assessments of particular domains of life such as health, environment, social relations.

K, and we extend the domain of preferences We stick to the assumption that X = R + to all monotonic and continuous preferences R od. Supremum Nested Contour does not need any rewriting. We redefine Infimum Nested Contour by removing the convex hull requirement, that is, we adopt the definition of Infimum Nested Contour* above. It should be clear, though, that a crucial difference is that in the domain R od, the union of two arbitrary upper contour sets is itself an upper contour for some preferences in the domain. As a result, this version of the axiom respects the lattice structure of the space of upper contour sets, so that similar proofs as the ones developed in Fleurbaey and Maniquet (2017) can be obtained. Axiom 4 Infimum Nested Contour* For all x, x, x ∈ X, all R, R, R ∈ R od, if U (x, R) ⊂ interior[U (x, R) ∪ U (x, R )], then W (x, R) > min{W (x, R ), W (x, R )}. The main result of this section is that the two main axioms, Supremum and Infimum Nested Contour, turn out to be compatible with each other over this larger domain. We characterize the family of well-being measures satisfying both axioms below. This family is also the family of monotone consumption path well-being measures: wellbeing is measured by the intersection between the indifference surface of an agent at a bundle and a fixed monotone consumption path. Theorem 2 A well-being measure W satisfies Supremum Nested Contour and Infimum Nested Contour* if and only if there exists a monotone consumption path P and a

K, all R ∈ R, strictly increasing function w: P → R + such that for all x ∈ R + W (x, R) = w(p) for p ∈ P such that x I p. This theorem can be proven in a similar way as the proof of Theorem 1 above, or the proofs of Chambers and Miller (2014a, b), using the lattice structure of the domain. Indeed, when we combine Supremum Nested Contour (resp., Infimum Nested Contour*) with continuity, we obtain the requirement that the well-being associated to a bundle on an indifference surface that is the supremum (resp., infimum) of two other indifference surfaces is exactly the maximum (resp. minimum) between the well-being levels associated to these two indifference surfaces. Chambers and Miller show that the combination of these two requirements leads to measures that have the

Well-being measurement with non-classical goods following structure: there should be a chain of nested sets and the measure associated to an arbitrary set is equal to the measure associated to the largest element of the chain contained in this arbitrary set. In the case of monotone consumption path well-being measures, we can think of this chain of sets as the chain {x ∈ X |x ≤ p} for all p ∈ P (more details can be found in Fleurbaey and Maniquet 2017, addendum). In Sect. 6, we give a different proof, building on the existence in the preferences domain of preferences for which the consumption of one good only is desirable. We show that the intersection of the indifference sets of this kind (there are as many of these as there are goods) draws a monotone consumption path, which must be used for the well-being measure of all preferences.

4 Satiation In this section, we assume that quantities of available goods take values in a compact set. We see this assumption as capturing the idea that the contemplated goods are not always desirable (the preferred quantity of them may be finite, as in the case of the preferred distance between one’s housing location and the center of a city), or come in discrete quantities (such as being employed or not), or have a natural upper bound (such as perfect health). In addition to these goods, we assume that one good, good 1, is a classical good. In many applications, this is the role played by income (such as in Decancq et al. forthcoming, or Decancq et al. 2015). We will come back on the precise meaning of this good in the next section.

## K −1

. The Formally, we assume that X = R + × A, where A is a compact subset of R + domain of preferences we are now considering, R s contains all preferences that are continuous in all goods and monotonic in good 1. We call a ∈ A a list of attributes. We further assume that no attribute a can be infinitely better than another attribute, that is, for all x = (m, a) ∈ X, all a ∈ A, all R ∈ R s, there exists x = (m, a) ∈ X such that x P x. This is a common assumption, especially when goods are indivisible (see for instance, Thomson 2016). Supremum Nested Contour and Infimum Nested Contour* still turn out to be compatible in this model. Here is an example of a well-being measure that satisfies both axioms, illustrated in Fig. 4. Let ã ∈ A be a fixed reference parameter. The well-being measure W ã defined by W ã ((m, a), R) = w if and only if (m, a) I (w, ã) satisfies Supremum Nested Contour and Infimum Nested Contour*. Observe that for R ∈ R s, this well-being measure is well-defined only over the subset of X containing all bundles x = (m, a) at least as good as (0, ã). We denote this subset as X ã (R). We prove in the following theorem that all well-being measures satisfying these two axioms are strictly increasing transforms of this fixed attribute measure on the relevant set of bundles. Theorem 3 A well-being measure W satisfies Supremum Nested Contour and Infimum Nested Contour* if and only if there exists a fixed attribute ã ∈ A and a strictly increasing function f: R + → R + such that for all R ∈ R s, all x = (m, a) ∈ X ã (R), W (x, R) = f (W ã (x, R)). This result is a corollary, mutatis mutandis, of Chambers and Miller (2014a, b) results. For the sake of completeness, we provide a different proof in Sect. 6.

x

## R

w (x, a) (x, a)

## R

w 0 ã

## A

Fig. 4 Illustration of W ã: W ã ((x, a), R) = w, W ã ((x, a ), R) = w We may also be interested in this model in the requirement that the same amount of resources increases well-being more the lower the well-being level of the agent who gets it. The natural requirement, here, would be that an additional amount of good 1 has this property when it is assigned to agents with attributes equal to ã. No stronger requirement can be satisfied. It requires that function f in the statement of the theorem be concave. We do consider, however, that there is another way of defining well-being that captures the particular nature of the goods that we study in this section. Indeed, let us assume that two agents consume the attribute that they prefer, or more precisely, the attribute that, given their consumption of good one, they consider optimal (their preferred labor time, their preferred health level, distance of their housing to the center of the city, size of their housing, etc.). These two agents could be declared equally well-off. Assume, on the contrary, that one of them is declared better-off. If we apply an egalitarian aggregator to these two agents, the conclusion would be that we need to redistribute the first good among them, to compensate the worse-off agent. Compensate for what, if she has her preferred attribute? That would be hard to justify. It is convenient to use the following terminology in the definition of the axiom. For m ∈ R + and R ∈ R s, we write a max (m, R) to denote the set of preferred attributes of agent R when she consumes the quantity m of the first good, that is, (m, a max (m, R)) R (m, a) for all a ∈ A.

Well-being measurement with non-classical goods x

## R

## R

x 0

## A

a Fig. 5 This property is illustrated in Fig. 5. Equal Well-Being at Preferred Attribute: W((x, a), R) = W((x, a), R) Axiom 5 Equal Well-Being at Preferred Attribute For all x = (m, a) ∈ X, all R, R ∈ R, if a ∈ a max (x, R) and a ∈ a max (x, R ), then W ((x, a), R) = W ((x, a), R ). Our last result characterizes the family of well-being measures that satisfy Equal Well-Being at Preferred Attribute. It echoes a similar characterization developed by Fleurbaey and Blanchet (2013). Theorem 4 A well-being measure W satisfies Equal Well-Being at Preferred Attribute if and only if for all (m, a), (m, a) ∈ R + × A, all R, R ∈ R, min (y,b)∈U ((m,a),R) y = min (y ,b )∈U ((m ,a ),R) y ⇔ W ((m, a), R) = W (m, a ), R ).

The characterization of Fleurbaey and Blanchet (2013) is based on the axiom requiring that an agent who is equally well-off independently of the value of the attribute this agent consumes be always declared among the best-off at any bundle. Their axiom is logically stronger than Equal Well-Being at Preferred Attribute. All the well-being measures satisfying the axiom of the theorem are ordinally equivalent to W a max defined by: for all x = (m, a) ∈ R + × A, all R ∈ R, W a max (x, R) = w ⇔ x I (w, a max (x, R)).

m

## R

(m, a) (m, a)

## R

w w 0

## A

Fig. 6 Illustration of W a max: W a max ((m, a), R) = w, W a max ((m, a ), R) = w Note that all these measures, illustrated in Fig. 6, satisfy Infimum Nested Contour* as well. To complete this section, let us note that a special case of the consumption set and preference domain studied in this section is the case of a compact and convex set A and convex preferences over X (which, of course, does not exclude satiation over A). A careful reading of the proofs of Theorems 3 and 4 will prove that they remain valid under these additional assumptions. We need to observe as well that W ã satisfies Infimum Nested Contour* but not Infimum Nested Contour over this domain. Like in the classical domain Supremum Nested Contour and Infimum Nested Contour are incompatible. On the other hand, all well-being measures ordinally equivalent to W a max do satisfy Infimum Nested Contour, whether or not we restrict our attention to a compact and convex set A and convex preferences over X.

5 The general case It may be tempting to interpret good m in the model of the previous section as income. Using income as a good, however, assumes that prices are fixed and the same for all agents, since otherwise two agents having the same preferences and consuming bundles on the same indifference surface would be declared enjoying different wellbeing levels. Interpreting m as income also cannot accommodate non-market goods. Therefore, it is important to be able to analyze bundles at the level of individual goods rather than with composite commodities or income. We should rather assume that there

Well-being measurement with non-classical goods are classical goods that agents can buy together with non-classical ones. The difficulty is, therefore, to combine the two well-being measures defined in the previous section with the ones defined in Sect. 2 and which aim at providing a suitable alternative to income. This section studies this combination.

K being the Let the consumption set of the agents now be X × A, with X ⊆ R + set of possible consumptions of divisible goods of which convex combinations are

K being a compact set of meaningful and for which more is always better, and A ⊂ R + attributes. Our objective is to combine the well-being measures W and W p defined over X and W ã and W a max defined over R + × A. The other types of goods, those for which quantities are only ordinally measurable, are skipped in this section. Indeed, the combination of the only solution to that case with the other solutions turns out to be easy after it has been shown that these other solutions can be combined with each other, as we do below.

The main message of this section is that combining either W or W p with either ã W or W a max is possible and gives us four different well-being measures. Let us review the resulting measures in turn.

1. Combining W and W ã, we can define W ã as follows: for all (x, a) ∈ X × A, all

## R ∈ R,

W ã (x, a) = w ⇔ (x, a) I (w, ã).

2. Combining W and W a max, we can define W a max as follows: for all (x, a) ∈ X × A, all R ∈ R, W a max (x, a) = w ⇔ (x, a) I (w, a max (w, R)).

3. Combining W p and W ã, we can define W pã as follows: for all (x, a) ∈ X × A, all R ∈ R, W pã (x, a) = w ⇔ (x, a) I max R, {(x, ã) ∈ X × A| px ≤ w}.

4. Combining W p and W a max, we can define W pa max as follows: for all (x, a) ∈ X × A, all R ∈ R, W pa max (x, a) = w ⇔ (x, a) I max R, {(x, a) ∈ X × A| px ≤ w, a ∈ A}.

6 Proofs Proof of Theorem 1 (1) Let us begin by proving that W, as defined in the statement of the theorem, satisfies Infimum Nested Contour*. Let x, x, x ∈ X and R, R, R ∈ R cl satisfy the conditions of the definition of the axiom. Assume, w.l.o.g., that min{W (x, R ), W (x, R )} = W (x, R ). That means that there exists p ∈ P such that x I p and x R p. Consequently, x

## R

R w x ∗ x

## R

0 good 1

Fig. 7 Illustration of Theorem 1 p ∈ / interior[U (x, R) ∪ U (x, R )].

/ U (x, R), Because U (x, R) ⊂ interior[U (x, R) ∪ U (x, R )], we have p ∈ which means that x P p, that is W (x, R) > W (x, R ), and the axiom is satisfied. (2) We now prove the “only if” statement. Assume that W satisfies Supremum Nested Contour and Infimum Nested Contour*, but W is not as defined in the statement of the theorem. By Lemma 1, there exists R w ∈ R w such that W satisfies: for all x ∈ X and R ∈ R cl:

W (x, R) = max x ∈L(x,R)

W (x, R w ).

Observe that the theorem can be restated as requiring that R w = R P defined by: for all p ∈ P:

U (p, R P) = {x ∈ X |x ≥ p}, that is R P is such that all upper contour sets are similar to Leontieff type upper contour sets with kinks at elements of P. Also observe that the arguments that maximize W (·, R P) over L(x, R) in the property of Lemma 1 are always elements of P (tangencies between indifference contours of R P and lower contour sets take place at the kinks of indifference contours of R P ). If R w = R P, then there exist, as illustrated in Fig. 7, x, x ∈ X and R, R ∈ R cl such that W (x, R) = W (x, R) = w, but tangencies do not take place at the same bundles:

arg max x ∈L(x,R)

W (x, R w) = arg max x ∈L(x ,R)

W (x, R w ).

Well-being measurement with non-classical goods Then there exists w < w and x ∗ ∈ X such that

W (x ∗, R w) = w and U (x ∗, R w) ⊂ interior U (x, R) ∪ U x, R, contradicting Infimum Nested Contour*. Proof of Theorem 2 We begin with the if part. Assume there exists a monotone consumption path P and a strictly increasing function w: P → R + such that for all K, all R ∈ R od, W (x, R) = w(p) for p ∈ P such that x I p. To prove that x ∈ R + W satisfies Supremum Nested Contour and Infimum Nested Contour*, we resort to Lemmas 1 and 2 and we limit ourselves to constructing the appropriate R w and R b. 10 Let us define R w as follows. For all x ∈ X, there exists p ∈ P such that U (x, R w) = x ∈ X |x > p.

Let us define R b as follows. For all x ∈ X, there exists p ∈ P such that L(x, R b) = x ∈ X |x < p.

We also define W (·, R w) and W (·, R b) so that W (p, R w) = W (p, R b) = w(p). The claim is proven by observing that, for all x ∈ X, R ∈ R and p ∈ P such that x I p, by monotonicity of R, we have both

W (x, R) = max

W (x, R w) min

W (x, R b ).

x ∈L(x,R) and

W (x, R) = x ∈U (x,R) We now prove the only if part. Let W satisfy Supremum Nested Contour and Infimum Nested Contour*. We need to prove that W is of the monotone consumption path type. Observe that it is equivalent to proving that for some path P, preferences R w and R b have the property that for all p ∈ P, U (p, R w) = {x ∈ X |x > p} and L(p, R b) = {x ∈ X |x < p}. Indeed, by monotonicity of the preferences, each maximization or minimization operation over lower or upper contour sets of R w and R b will be reached with bundles of P. For each ∈ {1,..., K }, let R ∈ R be defined by: for all x = (x k) k∈{1,...,K}, x = (x k) k∈{1,...,K}, x R x ⇔ x ≥ x,

10 The immediate proof that a variant of Lemmas 1 and 2 hold over R od, which lies on the lattice structure of the set of upper or lower contour sets, is omitted.

that is agents with preferences R are only interested in consuming good. Let r ∈ R and x r ∈ X for ∈ {1,..., K} be such that ∀ ∈ {1,..., K }, W (x r, R) = r.

Let p r ∈ X be defined by p r = ∩ ∈{1,...,K} I (x r, R ).

Note that by continuity and monotonicity of W, P = ∪ r ∈R p r is a monotone consumption path. We can fix w(p r) = r. By Supremum Nested Contour and Infimum Nested Contour* there exist R w, R b ∈ R such that for all ∈ {1,..., K },

W (x r, R) = max x ∈L(x r ,R)

W (x, R w) so that for all x r w such that W (x r w, R w) = r, U (x r w, R w) ⊆ {x ∈ X |x ≥ p r }, and

W (x r, R) = min x ∈U (x r ,R)

W (x, R b) so that for all x r b such that W (x r b, R b) = r, L(x r b, R b) ⊆ {x ∈ X |x ≤ p r }.

Now, by Supremum Nested Contour,

W (x r b, R b) = max

W (x, R w) min

W (x, R b) x ∈L(x r b ,R b) as well as, by Infimum Nested Contour*,

W (x r w, R w) = x ∈U (x r w ,R w) so that the only possibility is that both U (x r w, R w) = {x ∈ X |x ≥ p r} and L(x r b, R b) = {x ∈ X |x ≤ p r }, the desired outcome.

Well-being measurement with non-classical goods Proof of Theorem 3 It is useful to notice that Supremum Nested Contour and Infimum Nested Contour* both imply the very basic property that an indifference set that is everywhere above another corresponds to a greater level of well-being: Axiom 6 Nested Contour For all x, x ∈ X, R, R ∈ R s, if U (x, R) ∩ L(x, R) = ∅, then W (x, R) > W (x, R ). We divide the proof of the theorem in two claims. First, we claim that all indifference curves associated to a given well-being level cross in one point: for all w ∈ R, there exists x(w) ∈ ∩ R∈ R X ã (R) such that for all R ∈ R, W (x(w), R) = w. Assume not. Then, we can find R, R, R ∈ R s such that for all x ∈ ∩ R∈ R X ã (R), either W (x, R) = w or W (x, R) = w or W (x, R) = w. Let L, L, L be defined as follows.

L = {x ∈ X |W (x, R) ≤ w} L = {x ∈ X |W (x, R) ≤ w} L = {x ∈ X |W (x, R) ≤ w}.

Let L̃ = L ∩ L ∩ L. Looking at upper contour sets, we define in a similar way U, U, U. Let R̃ ∈ R be such that there exists x ∈ X such that L(x, R̃) = L̃. By Supremum Nested Contour and continuity, W (x, R̃) = w. By construction of R, R, R, we can find x ∈ interior L̃ such that U (x, R̃) ⊂ [U ∪ U ∪ U ]. By Infimum Nested Contour* and continuity, W (x, R̃) ≥ w, a contradiction, because x ∈ interior L̃ implies W (x, R̃) < w. This first claim can be restated as: for all w ∈ R, there exists ã(w) ∈ A and m ∈ R + such that for all R ∈ R s, W (m, ã(w), R) = w. The second claim consists in stating that ã(w) does actually not depend on w. Let us assume, on the contrary, that there exist w, w ∈ R, ã(w), ã(w) ∈ A, with w = w and ã(w) = ã(w ), and m, m ∈ R + such that for all R ∈ R s, W (m, ã(w), R) = w and W (m, ã(w ), R) = w. Because R s contains all preferences satisfying the constraints, we can find R, R ∈ R s such that (m, ã(w)) P (m, ã(w )) and (m, ã(w )) P (m, ã(w)), so that W cannot respect both R and R. Proof of Theorem 4 Let (m, a), (m, a) ∈ R + × A and R, R ∈ R be such that min (y,b)∈U ((m,a),R) y ≥ min (y ,b )∈U ((m ,a ),R) y.

Let (m̄, ā), (m̄, ā) ∈ R + × A be such that m̄ = m̄ = min (y,b)∈U ((m,a),R) min y (y ,b )∈U ((m ,a ),R) y (m, a) I (m̄, ā) (m, a) I (m̄, ā ).

As W respects preferences, we have both W ((m, a), R) = W ((m̄, ā), R) (1) W ((m, a ), R) = W ((m̄, ā ), R ).

(2) Let R̄ ∈ R s be defined by: for all (y, b), (y, b) ∈ R + × A, (y, b) R̄ (y, b) ⇔ y ≥ y.

By Equal Well-Being at Preferred Attribute, W ((m̄, ā), R̄) = W ((m̄, ā), R) and W ((m̄, ā ), R̄) = W ((m̄, ā ), R ).

As W respects preferences, W ((m̄, ā), R̄) ≥ W ((m̄, ā ), R̄).

Gathering these last inequalities and equalities, we obtain W ((m, a), R) ≥ W (m, a ), R ), the desired outcome.

7 Concluding comments In this paper, we have studied the construction of well-being measures in different models. What was common across models was the fact that the only ingredients that were used were the description of the good consumed by an agent and her preferences. That is, no a priori information on subjective utility, welfare or happiness was considered relevant. Our approach is thus consistent with the view of justice as fairness. What was different across models was the set of assumptions on the nature of the goods that agents consume. The main objective of the paper, indeed, was to relax the assumption that all goods are desirable in the sense that more of them is always preferred, and the assumption that the measure of quantities is cardinal, that is quantity differences and convex combinations of bundles are meaningful. Under different sets of assumptions on the nature of the goods, we have studied the construction of well-being measures on the basis of two axioms, creating well-being comparability across agents with different preferences on the basis of what they consume. We have axiomatically characterized several families of well-being measures. As a result of this inquiry, the well-being of each agent can be measured in isolation. This has two consequences. The first consequence is that the aggregation of well-being

Well-being measurement with non-classical goods levels can be operated using any kind of aggregator, from the utilitarian to the leximin one. Any degree of inequality aversion is acceptable. The second consequence is that whether goods are private or public, whether they are tradable or not, whether their consumption exhibits congestion or exclusion phenomena, is unrelated to the way well-being has to be measured. These aspects need to enter the description of the allocation problem as feasibility constraints and not as relevant variables at the stage of the definition of well-being. Together with the companion papers Fleurbaey and Maniquet (2017, 2018), we believe this undertaking provides strong justification to well-being measures based on fairness principles. These measures are ready to be applied in the context of, for instance, poverty or inequality measurement, or, more generally, in the context of the evaluation of the impact of policies on the distribution of well-being. Indeed, building well-being measures the way we do here amounts to building inter and intrapersonal comparability. If, for instance, a social observer wishes to apply an aggregator that satisfies a scale invariance property to these well-being measures, all the axioms that we have used to construct them will still be satisfied. However, to satisfy fairness axioms, that is, axioms that directly bear on the allocation of resources, like transfer axioms, in the evaluation of allocations, the choice of the aggregator is not in general independent of the choice of well-being measures. Fleurbaey and Maniquet (2018) prove, indeed, that different well-being measures do satisfy different transfer axioms.

## References

Bosmans, K., Lauwers, L., Ooghe, E.: Prioritarian poverty comparisons with cardinal and ordinal attributes.

Scand. J. Econ. 119(3), 79–92 (2017) Chambers, C.P., Miller, A.D.: Inefficiency measurement. Am. Econ. J. Microecon. 6, 79–92 (2014a) Chambers, C.P., Miller, A.D.: Scholarly influence. J. Econ. Theory 151, 571–583 (2014b) Deaton, A.: The distance function in consumer behaviour with applications to index numbers and optimal taxation. Rev. Econ. Stud. 46, 391–405 (1979) Decancq K., Fleurbaey, M., Maniquet, F.: Multidimensional poverty measurement with individual preferences. J Econ Inequal, forthcoming Decancq, K., Fleurbaey, M., Schokkaert, E.: Happiness, equivalent incomes and respect for individual preferences. Economica 82(s1), 1082–1106 (2015) Donaldson, D.: On the aggregation of money measures of well-being in applied welfare economics. J. Agric.

Resour. Econ. 17, 88–102 (1992) Fleurbaey, M., Blanchet, D.: Beyond GDP: Measuring Welfare and Assessing Sustainability. Oxford University Press, New York (2013) Fleurbaey, M., Maniquet, F.: A Theory of Fairness and Social Welfare. Cambridge University Press, Cambridge (2011) Fleurbaey, M., Maniquet, F.: Fairness and well-being measurement. Math. Soc. Sci. 90, 127–128 (2017) Fleurbaey, M., Maniquet, F.: Inequality-averse well-being measurement. Int. J. Econ. Theory 14(1), 35–50 (2018) Foley, D.: Resource allocation and the public sector. Yale Econ. Essays 7, 45–98 (1967) Gravel, N., Magdalou, B., Moyes, P.: Ranking distributions of an ordinal attribute. AMSE working paper no 2015-15 (2015) Kolm, S.C.: The optimal production of social justice. In: Guitton, H., Margolis, J. (eds.) Economie Publique.

CNRS, Paris (1968) Pazner, E., Schmeidler, D.: Egalitarian equivalent allocations: a new concept of economic equity. Q. J. Econ.

92, 671–687 (1978) Samuelson, P.A.: Complementarity: an essay on the 40th anniversary of the Hicks-Allen Revolution in demand theory. J Econ Lit 12, 1255–1289 (1974) Samuelson, P.A.: Reaffirming the existence of ‘reasonable’ Bergson–Samuelson social welfare functions. Economica 44, 81–88 (1977) Samuelson, P.A., Swamy, S.: Invariant economic index numbers and canonical duality: survey and synthesis. Am Econ Rev 64, 566–593 (1974) Thomson, W.: Fair allocation rules. In: Arrow, K., Sen, A., Suzumura, K. (eds.) Handbook of Social Choice and Welfare, pp. 393–506. North-Holland, Amsterdam (2010) Thomson, W.: Fair allocation. In: Adler, M., Fleurbaey, M. (eds.) Handbook of Well-Being and Public Policy, pp. 193–226. Oxford University Press, Oxford (2016) Tinbergen, J.: Redelijke inkomensverdeling, 2nd edn. N. V. DeGulden Pers, Haarlem (1953)
