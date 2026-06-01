Yes. This is the right revision. Belgium in your current prototype memo is a feasibility anchor, not a substantive commitment, so shifting the actual implementation to France does not change the paper’s identity. The key is to rewrite the empirical part so that the application is explicitly French, EUROMOD is clearly described as the disposable-income engine rather than the behavioral model, and the structural estimation step is stated explicitly. That is fully consistent with your current JMP logic and with the EUROMOD-based structural labor-supply literature that already includes France, even if your own contribution is to push further on constrained opportunities and decomposition.   

Below is the cleanest text to add or substitute in the extended abstract.

**5. Empirical strategy**

Empirically, the paper is implemented on French microdata combined with EUROMOD input files. The design remains single-country and deliberately structural: individuals are modeled as choosing among a non-market option and a finite set of latent job packages rather than from a common unconstrained hours schedule. Job packages are defined parsimoniously by hours categories and wage or earnings categories, with richer job attributes added only if the data support them. For each individual–alternative pair, EUROMOD maps the job package into disposable income under the French tax-benefit system. Microsimulation is therefore essential for the budget mapping, but secondary to the paper’s core contribution, which is the joint estimation of preferences and opportunities. The key estimated objects are an income–leisure preference component, an opportunity mechanism that shifts the distribution of feasible job packages across observable circumstances, and, if needed, a parsimonious wage or earnings offer structure. The main empirical output is not a reform table or a country ranking, but a structural decomposition of welfare inequality built on those estimated objects.   

**5A. Structural model and estimation**

The positive model is a latent-jobs or RURO-style job-choice framework. Individual (i) chooses among non-employment and a finite set of job packages (j \in J_i). Each package is characterized minimally by hours (h_j) and wage or earnings (w_j), with the possibility of adding further job attributes later. For each package, disposable income (C_{ij}) is computed through EUROMOD under French tax-benefit rules, and leisure is (L_{ij}=\bar T-h_j). Conditional on latent preference type (r), utility can be written as
[
U_{ijr}=v(C_{ij},L_{ij},X_i;\beta_r)+\xi_{ijr},
]
where (\beta_r) captures consumption–leisure preferences, fixed costs of work, and observed or unobserved heterogeneity. Opportunities enter separately through an availability term (a_{ij}(S_i;\gamma)), where (S_i) denotes observable circumstances; in a richer RURO interpretation, this term can be decomposed into market-offer intensity and wage- and hours-offer densities. In a finite-alternative implementation, the conditional choice probability takes the form
[
P_{ijr}=\frac{a_{ij}(S_i;\gamma)\exp(v(C_{ij},L_{ij},X_i;\beta_r))}{\sum_k a_{ik}(S_i;\gamma)\exp(v(C_{ik},L_{ik},X_i;\beta_r))}.
]
The sample likelihood is then
[
\mathcal L(\beta,\gamma,\pi)=\prod_i \sum_r \pi_r \prod_j P_{ijr}^{d_{ij}},
]
where (d_{ij}) indicates the observed choice and (\pi_r) are latent-type probabilities. This makes the contribution logic transparent: preferences determine how individuals rank feasible jobs, while the opportunity mechanism determines which jobs are likely to be available. Estimation by maximum likelihood jointly recovers both objects, subject to the standard identification warning that preferences and opportunities become difficult to separate when the same observables drive both sides too flexibly.     

**10. First empirical prototype**

The first empirical implementation should now be described as a French application using EUROMOD input data. It should remain deliberately narrow. A sensible first pass is to focus on working-age individuals attached to the labor market, exclude the self-employed, and represent labor supply through a small grid of latent job packages obtained by crossing discrete hours categories with wage or earnings groups. This finite job grid is not the conceptual endpoint of the paper; it is the smallest estimable representation of unequal opportunities that still allows opportunities to enter estimation, welfare evaluation, and decomposition in a consistent way. The first output should be one decomposition table reporting baseline inequality in opportunity-sensitive money-metric welfare, inequality after equalizing the opportunity mechanism across circumstance groups, inequality after neutralizing preference heterogeneity, and the corresponding Shapley decomposition shares. For the JMP, the relevant proof of concept is not a full policy simulation for France, but evidence that the opportunity component of welfare inequality is quantitatively nontrivial and robust to reasonable changes in the opportunity partition and welfare inequality index.   

Two drafting comments. First, this estimation subsection should appear in the extended abstract, but in a compact form: one utility equation, one choice-probability equation, and one likelihood equation are enough. Second, for supervisor-facing writing, the discrete finite-job version is the safest presentation. It makes clear that the paper is estimable on French data now, while still leaving room later to discuss the fuller RURO interpretation in terms of offer intensity and wage/hours densities.  
