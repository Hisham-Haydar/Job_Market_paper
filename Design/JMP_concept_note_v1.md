# JMP Concept Note v1
Date: 2026-04-14
Source: Prompt B / topic-lock run
Status: draft


Below is a draft concept note based on the uploaded design memo and literature synthesis. It keeps the JMP centered on constrained opportunities / latent jobs, welfare measurement, and decomposition, with microsimulation in a supporting role rather than as the core identity of the paper.  

**1. Provisional title**

**Opportunity Constraints as a Driver of Welfare Inequality: A Latent-Jobs Structural Decomposition Approach**. This title is deliberately narrower than a generic welfare-ranking project: it signals that the paper’s central object is the decomposition of welfare inequality in a structural labor-supply setting where feasible job opportunities are heterogeneous and partly latent.  

**2. Core question**

How much of observed inequality in money-metric well-being in a labor-supply setting is attributable to unequal job opportunities rather than to heterogeneous preferences, once labor supply is modeled as discrete choice over latent job packages and welfare is evaluated consistently with constrained feasible sets? Put differently, the paper asks whether standard structural labor-supply models overstate “preference heterogeneity” because they absorb unequal opportunities into tastes.  

**3. Why this matters**

Structural labor-supply models are routinely used to evaluate reforms and compute welfare effects, but the opportunity environment is often treated as implicit or secondary. If workers face unequal and partly unobserved job opportunities, then both behavioral estimates and welfare comparisons can be systematically distorted: a constrained second-best outcome may be misread as a chosen optimum, and welfare inequality may be misattributed to tastes rather than opportunities. This is exactly why decomposition is more scientifically useful than a simple ranking exercise: it identifies the mechanism driving inequality and connects directly to policy-relevant counterfactuals such as equalizing opportunities or relaxing constraints.  

**4. Main contribution**

The paper’s contribution is to build a unified empirical pipeline in which opportunities are treated consistently across three stages: estimation, welfare evaluation, and decomposition. First, I estimate a latent-jobs / RURO-style structural labor-supply model with heterogeneous opportunity sets. Second, I construct a money-metric welfare measure that is defined relative to the constrained feasible set rather than to a universal choice set. Third, I decompose welfare inequality into an opportunity component and a preference component using transparent counterfactual equalizations and an order-independent decomposition rule. The normative interpretation is explicit: unequal opportunities are treated as compensation-relevant, while preference heterogeneity is treated separately under a responsibility-sensitive reading.  

**5. Empirical strategy**

The baseline design is a single-country structural application on working-age individuals or households, excluding the self-employed in the first pass. Labor supply is modeled as choice among discrete job packages defined minimally by hours categories and wage or earnings categories, with the possibility of adding a small number of job attributes if the data support it. Disposable income for each package is computed using tax-benefit simulation, but microsimulation enters only as an input into the budget mapping, not as the paper’s main contribution. The key estimated objects are preferences over consumption and leisure, an opportunity mechanism that varies with observable circumstances such as region and education, and, if needed, an offer structure linking wages to job packages. The main empirical output is a decomposition table or figure showing baseline welfare inequality and its change under opportunity equalization, preference neutralization, and both together.   

**6. Relation to literature**

The paper sits at the intersection of four strands. The first is the constrained structural labor-supply literature that models work as choice over job packages or latent jobs rather than as free choice over hours on a universal budget set; this is the positive foundation for treating opportunities as a first-class object. The second is the restricted-choice and identification literature showing that observed labor-supply outcomes confound tastes and opportunities unless the offer process is modeled explicitly. The third is the welfare-analysis literature for discrete choice, which provides the basis for computing money-metric welfare objects rather than stopping at behavioral elasticities. The fourth is the inequality-of-opportunity literature, which motivates counterfactual equalization and the normative distinction between what should be compensated and what may be treated as the individual’s responsibility. Relative to these literatures, the novelty here is not another tax-reform simulation or another welfare ranking, but a structural decomposition of welfare inequality into opportunity-driven and preference-driven components.    

**7. Main risk**

The main risk is identification. In this class of models, preferences and opportunities are difficult to separate unless the opportunity mechanism is disciplined by sufficient structure or exclusion restrictions; weak identification would make the decomposition look mechanical rather than substantive. A second risk is normative vulnerability: any welfare decomposition can be challenged if the welfare metric or responsibility stance is not stated clearly. The practical response is to be explicit about the ethical interpretation, keep the prototype parsimonious, and report sensitivity to alternative circumstance partitions and alternative welfare specifications while maintaining the same opportunity structure.  

**8. Immediate next step**

The immediate next step is to implement a prototype with the smallest defensible job-package definition: hours categories by wage or earnings categories, optionally augmented by sector. I would estimate a simple opportunity mechanism that varies by a small set of circumstances such as region by education, compute baseline welfare inequality, and then produce one decomposition figure and one robustness check under an alternative circumstance partition or opportunity parameterization. If the opportunity share of welfare inequality is quantitatively nontrivial and reasonably stable, the JMP topic is effectively locked. 

If you want, I can now turn this into a tighter supervisor memo version with more formal economics wording, or a slightly more persuasive version for discussion in a meeting.
