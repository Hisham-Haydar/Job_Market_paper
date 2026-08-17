## 1. Current state of the literature

The literature is now strong on the separate building blocks, but still weak on their integration. First, there is a mature structural labor-supply literature that models jobs as constrained packages or latent opportunities rather than as free hours choices on a universal budget set. Second, there is a welfare literature showing that money-metric comparisons become normatively sensitive once preference heterogeneity is taken seriously. Third, there is an inequality-of-opportunity literature that provides the language of circumstances, responsibility, and compensation. What is still missing is a single empirical pipeline that does all three at once: estimate opportunities structurally, carry them into welfare measurement, and then decompose welfare inequality in an order-independent way. That is the gap your France 2016 couples prototype is trying to fill.   

The literature is therefore not waiting for “another structural model” or “another welfare metric” in isolation. It is waiting for a paper that shows that the opportunity primitive matters quantitatively once one moves from behavior to welfare to decomposition. Your own notes are already explicit that this is the unresolved issue left open by the standard RURO/microsimulation survey: the field still sits between a common utility approach that imposes interpersonal comparability by assumption and a preference-respecting approach that respects heterogeneity but does not solve the opportunity problem.  

## 2. Closest neighboring literatures

The first neighboring literature is **constrained structural labor supply / RURO / latent jobs**. This is the literature that gives you the behavioral architecture: jobs as packages, opportunity densities, sampled alternatives, and explicit warnings that choice-set specification matters for counterfactuals. It is the positive backbone of the project.   

The second neighboring literature is **empirical welfare analysis under heterogeneous preferences**. This literature is close because it shows that welfare rankings and money-metric comparisons move when preferences are allowed to differ. But it is also incomplete for your purposes, because it usually lacks an explicit opportunity-set object and therefore risks booking constrained outcomes as “preferences.”  

The third neighboring literature is **inequality of opportunity / responsibility-sensitive measurement**. This is where the project gets its normative interpretation: some differences should be compensated, others respected. But most of that literature works with type partitions or reduced-form circumstances, not with estimated feasible job sets.  

The fourth neighboring literature is **decomposition methodology**, especially Shapley-Shorrocks style decomposition. This is the closest methodological literature to the paper’s headline object, because once the structural model has separated opportunities from preferences, decomposition is what turns that separation into a reportable quantitative result.  

## 3. Closest papers

The closest structural reference is **Aaberge and Colombino (2018)** because it defines the methodological field: RURO plus microsimulation, with the unresolved tension between common welfare functions and preference-respecting welfare measures stated explicitly. In your own notes, this is the paper that most clearly identifies the open problem your JMP is designed to solve. 

The closest empirical RURO analogue is **Aaberge, Colombino and Strøm (1999)**. It is close because it is a couples model with non-convex tax-benefit constraints, explicit opportunity terms, and region-conditioned opportunity heterogeneity. It is the cleanest historical analogue to your France 2016 couples baseline. 

The closest paper on choice-set fragility is **Aaberge, Colombino and Wennemo (2009)**. It is close because it shows that the opportunity block is the empirically fragile component and that poor choice-set representation has first-order consequences for policy counterfactuals. That matters directly for your France design, where the welfare layer inherits any misspecification of the opportunity set.  

The closest conceptual framing paper is **Dagsvik et al. (2014)** and the closest identification paper is **Dagsvik and Jia (2016)**. The first tells you why latent jobs should be read as opportunities rather than disguised hours dummies; the second tells you exactly how far the preferences-opportunities separation can really be taken with cross-sectional data.  

The closest welfare comparator is **Bargain et al. (2013)**. It is close because it is the clearest empirical template for the money-metric welfare layer, and also because it openly concedes that what it labels “preferences” may embed unmodeled opportunity constraints. 

The closest non-RURO identification competitor is **Beffy et al. (2019)**. It is close because it is probably the strongest external evidence that observed labor-supply outcomes conflate preferences and restrictions, and because it gives a credible rival way of identifying opportunity constraints. 

The closest substantive competitor overall is **Jacquet, Jia and Thoresen (2026)**. Your own notes say this explicitly. It already introduces a responsibility cut inside a structural job-choice model and computes a circumstance-only welfare object. Anyone reading your project will ask what is new relative to that paper.  

Finally, the closest decomposition anchor is **Shorrocks (2013)**. It is not a labor-supply paper, but it is the exact decomposition rule that turns your structural distinctions into a quantitative headline.  

## 4. What they do not yet do

The structural RURO papers do **not** make welfare inequality decomposition the main object. They estimate behavior and sometimes evaluate reforms, but the opportunity mechanism usually remains part of the econometric architecture rather than becoming a measured driver of welfare inequality. In your notes on Aaberge, Colombino and Strøm (1999), this is stated very clearly: the paper has constrained opportunities, but no welfare object and no formal Shapley-style opportunity decomposition. 

The welfare papers do **not** model opportunities explicitly. Bargain et al. (2013) is the clearest case: it is close on welfare, but it explicitly concedes that the “preference” component likely absorbs opportunity constraints. That means it cannot answer your actual question, which is whether apparent preference heterogeneity is partly opportunity heterogeneity in disguise. 

The responsibility/fairness papers do **not** complete the full empirical decomposition architecture. Jacquet, Jia and Thoresen (2026) is the most relevant example. It already introduces a responsibility-sensitive comparison inside a RURO-style model, but your own notes emphasize three things it does not yet do: it does not construct the dual object that neutralizes opportunities while keeping preferences, it does not perform a full Shapley decomposition, and it uses a narrower opportunity measure than the one your France design can implement. 

The decomposition papers do **not** provide the substantive economics. Shorrocks gives the rule, not the factor definitions. So the missing step is not the existence of a decomposition formula; it is the economic construction of the factors inside a structural labor-supply and welfare framework. 

So the literature gap is precise: there is still no paper that takes a structurally estimated latent-opportunity labor-supply model, computes a money-metric welfare object conditional on constrained feasible sets, and then decomposes welfare inequality into opportunity and preference components in an order-independent way on a concrete empirical baseline like France 2016 couples.  

## 5. My expected contribution

**Structural contribution.** The project estimates a France 2016 couples RURO / latent-jobs model in which opportunities are modeled explicitly rather than absorbed into residual tastes. Relative to standard discrete-choice labor-supply work, the contribution is not merely to estimate another model, but to keep the opportunity block economically interpretable all the way through the empirical pipeline.  

**Welfare contribution.** The project constructs a household AEI-style money-metric welfare object that is explicitly conditional on constrained feasible sets. Relative to the welfare-ranking literature, the contribution is to stop treating the opportunity environment as implicit. Relative to the common-utility tradition, the contribution is to avoid obtaining comparability simply by assuming away the relevant heterogeneity.  

**Decomposition contribution.** This is the central one. The paper uses a two-factor Shapley-Shorrocks decomposition of the household welfare Gini, with opportunity heterogeneity and preference heterogeneity as the two headline factors. The literature has the pieces, but not this integrated object. That is why the decomposition, not the estimation itself, should be treated as the main scientific output.  

**Empirical prototype contribution.** The first contribution is not universal coverage. It is a disciplined proof of concept on the actual France 2016 couples baseline, with a sampled latent-choice structure, household AEI, and one decomposition table and one decomposition figure. That is a contribution because it shows the mechanism in an implemented structural setting, not because it exhausts every year, household type, or country.  

## 6. Why this project is scientifically meaningful

This is not just another welfare-ranking paper because the main object is **not** the ranking. The main object is the mechanism generating welfare inequality. Rankings tell you who is ahead under a metric. Decompositions tell you what structural forces generate the inequality in that metric. That is a different scientific claim. Your own project documents are already explicit that decomposition is the core contribution and ranking is, at most, a side effect.  

This is not just another structural labour-supply paper because the model is not the endpoint. In the classic structural papers, opportunity densities help fit hours distributions and simulate reforms. In your paper, the opportunity mechanism becomes an attributable component of welfare inequality. The model is therefore an engine for welfare decomposition, not merely a behavior simulator.  

The opportunity/decomposition angle matters scientifically because without it the field cannot distinguish between two very different interpretations of observed heterogeneity: genuine taste differences versus constrained access to jobs. If those are confounded, welfare evaluation is unstable, and policy arguments about responsibility or compensation are built on misclassified variation. The whole point of your paper is to turn that conceptual warning into a measured empirical object.  

## 7. Main vulnerability

The first likely objection is: **the preferences-opportunities split is only partially identified and therefore the decomposition may be parametric bookkeeping.** This is a serious objection, and your own notes on Dagsvik and Jia (2016) say exactly that: the product is identified more cleanly than the factors. The right response is not denial. It is to say that the paper is a disciplined structural decomposition under explicit maintained assumptions, and that the opportunity share is the component that deserves the strongest sensitivity analysis.  

The second likely objection is: **the project may not be sufficiently distinct from Jacquet, Jia and Thoresen (2026).** This is the closest-competitor objection. The answer must be sharper than “France instead of Norway.” The difference is that your paper makes decomposition central, completes the missing dual compensation/responsibility architecture, and turns the comparison into an order-independent attribution exercise rather than a two-way welfare contrast. If that difference does not survive clearly in the writing and tables, the paper will look derivative.  

The third likely objection is: **France 2016 couples is too narrow to support a broad claim.** That is an external-validity objection, and it is legitimate. The answer is that the paper is intentionally staged: France 2016 couples is the narrowest scope on which the structural model, welfare object, and decomposition rule already align. The first contribution is a coherent proof of concept, not maximal coverage. But this remains a real vulnerability until the first extensions—2021 couples, then singles, then Germany—are delivered.  

## 8. One-paragraph contribution statement

This paper contributes to four literatures at once, but in one tightly connected way. Structurally, it estimates labor supply in a France 2016 couples RURO / latent-jobs framework in which opportunities are modeled explicitly rather than absorbed into residual tastes. On the welfare side, it constructs household AEI-style money-metric welfare conditional on constrained feasible sets. On the decomposition side, it uses a Shapley-Shorrocks rule to decompose the household welfare Gini into an opportunity component and a preference component in an order-independent way. Empirically, it delivers this contribution in the narrowest fully coherent prototype currently available—France 2016 couples—so the paper is neither another welfare-ranking exercise nor another structural labor-supply application, but a first empirical demonstration of how unequal job opportunities can be measured as a distinct driver of welfare inequality.  
