Here is a complete summary and Q&A drawn exclusively from your project knowledge files.

---

## 12-Bullet Summary of the JMP

1. **Core question:** How much of observed money-metric well-being inequality is driven by unequal job opportunities rather than heterogeneous preferences, once labor supply is modeled as discrete choice over latent job packages?

2. **Empirical anchor:** France 2016, using SRCV / EUROMOD-input microdata, with the household couples sample as the baseline empirical unit.

3. **Structural model:** A RURO (Random Utility Random Opportunity) / latent-jobs framework in which each spouse faces sampled job packages defined as wage-vigintile × 4-hour-interval bundles plus non-employment; disposable income for each alternative is computed via EUROMOD.

4. **Preference component:** Box-Cox utility over household consumption and individual leisure, including a leisure–leisure interaction term for couples; preferences are estimated separately from the opportunity mechanism.

5. **Opportunity component:** A probabilistic job-offer mechanism parameterized to vary across observable circumstances (region × education), separating hours-offer and wage-offer heterogeneity from preference heterogeneity.

6. **Welfare object:** Household AEI-style money-metric welfare evaluated relative to a joint non-work reference state; a second reference-preference measure serves as robustness.

7. **Inequality object:** The Gini coefficient of household welfare is the baseline inequality measure.

8. **Decomposition:** A two-factor Shapley-Shorrocks decomposition attributes the household welfare Gini to an opportunity component and a preference component in an order-independent and residual-free way.

9. **Pipeline status:** A full France RURO pipeline is implemented (data prep, EUROMOD simulation, MNL dataset creation, L-BFGS-B estimation with analytical gradients, post-estimation diagnostics); estimation is running but not yet fully stabilized.

10. **Normative interpretation:** Opportunity-driven inequality is treated as compensation-relevant; preferences may be preference-respecting or responsibility-relevant depending on the adopted welfare criterion.

11. **What the paper is not:** Not a country-ranking exercise, not a tax-reform simulation paper, not a microsimulation-led paper, and not the separate axiomatic theory paper with François Maniquet.

12. **Immediate priority:** Produce one stable baseline decomposition table and one baseline figure showing the opportunity and preference shares of the France 2016 household welfare Gini.

---

## Answers to the Ten Questions

**1. Main research question**
How much of observed inequality in money-metric well-being is attributable to unequal job opportunities rather than heterogeneous preferences, once labor supply is modeled as discrete choice over latent job packages and welfare is evaluated under constrained feasible sets? The central object is the decomposition of the welfare distribution, not a ranking or a reform simulation.

**2. Current empirical baseline**
France 2016, SRCV / EUROMOD-input cross-section, household/couples sample (~4,253 households), RURO estimation with sampled latent alternatives and EUROMOD-computed disposable income. France 2021 is available for later robustness. The old Belgium / prime-age childless single-woman prototype is obsolete and should not be used in new writing.

**3. Main expected contribution**
A unified empirical pipeline that treats opportunities consistently across three stages: (i) structural estimation recovering a separate preference component and opportunity component from latent job choices; (ii) household AEI-style money-metric welfare measurement under constrained feasible sets; and (iii) a two-factor Shapley-Shorrocks decomposition of the household welfare Gini into opportunity-driven and preference-driven shares. The novelty is the integration of all three stages, not any single stage in isolation.

**4. Role of RURO / latent jobs**
RURO is the structural identification engine. It distinguishes preferences (utility over consumption and leisure) from opportunities (the probability distribution over feasible job packages), which is necessary to decompose welfare inequality into these two components. Without explicit latent-jobs modeling, opportunity differences are absorbed into estimated preferences, overstating preference heterogeneity. The sampled-alternative likelihood with McFadden correction is the estimator; L-BFGS-B with analytical gradients is the optimizer.

**5. Role of welfare measurement**
Welfare measurement bridges estimation and decomposition. The household AEI-style money-metric measure converts the estimated structural model into a cardinal, comparable welfare level for each household, defined relative to a joint non-work reference state and evaluated under the household's own constrained feasible set. This ensures that welfare comparisons reflect actual opportunity constraints rather than a hypothetical universal choice set, and keeps the welfare layer distinct from behavioral utility.

**6. Role of decomposition**
Decomposition is the paper's central empirical contribution. The two-factor Shapley-Shorrocks rule assigns shares of the household welfare Gini to the opportunity component and the preference component in an order-independent, residual-free, and symmetric way. The key counterfactuals are: (i) equalize opportunity distributions across region × education cells while holding preferences fixed; (ii) neutralize preference heterogeneity while holding opportunities fixed. These are then combined via the Shapley rule. This is a stronger object than a welfare ranking or a reform table.

**7. Why this should not be framed as a country-ranking paper**
Country-ranking papers use welfare measures to produce headline ordinal rankings across countries or years, with policy implications following from the rank. This JMP's contribution is instead explanatory and decompositional: it asks what fraction of welfare inequality within France is generated by the opportunity mechanism versus the preference mechanism. Country-ranking language would misdescribe the paper's object, weaken its methodological identity, and blur the normative interpretation of the decomposition. Extensions to France 2021, Germany, or other countries may come later but must remain extensions, not the core.

**8. The separate theory paper**
A separate pure theory paper exists with François Maniquet on jobs and well-being. That paper is axiomatic and develops the formal theory of well-being measurement when individuals face constrained job sets. The JMP is intellectually related but must remain distinct: it is an empirical structural paper, not an axiomatic theory paper. The project files are explicit that the JMP should not reproduce or directly implement the theory paper, should not center on axiomatics, and should not drift toward that paper's language or agenda unless explicitly asked. The theory paper provides conceptual grounding; the JMP must stand on its own empirical contribution.

**9. Next empirical step**
The immediate coding priority is to produce one stable baseline decomposition run. Concretely: freeze the France 2016 couples sample with one definitive filter and one data-year / EUROMOD system-year pairing; lock the basic `job` representation (wage vigintile × 4-hour interval); rerun couples RURO estimation with convergence diagnostics; implement household AEI welfare under the joint non-work reference state; code the region × education opportunity equalization and the reference-preference neutralization; then compute the household welfare Gini and the two-factor Shapley-Shorrocks decomposition; and produce one baseline table and one baseline figure. This should be done in Claude Code, not in this chat.

**10. Files to use when asking for writing help**
The most important files to attach or reference for writing help are:
- `JMP_core_packet_v1.md` — the master writing anchor (title, safe claims, abstract, table/figure specs)
- `JMP_france_status_memo_v1.md` — what is implemented, what is credible, what should not be claimed
- `JMP_intro_skeleton_v1.md` — paragraph-by-paragraph skeleton for the introduction
- `JMP_abstract_v4_france.md` — current abstract
- `JMP_topic_lock_v1.md` — locked research question and boundaries
- `JMP_literature_positioning_memo_v2.md` — literature positioning and gap statement

Do not attach obsolete prototype memos (v1, v2 Belgium/singles prototypes) to new writing requests unless explicitly comparing old and new framing.

---

**Verdict: Project memory is coherent.**

The project files are internally consistent. The research question, empirical anchor, structural model, welfare object, decomposition strategy, and paper boundaries all tell the same story across the core documents. The only systematic issue — which the files themselves flag explicitly — is the gap between what is designed (the decomposition) and what is empirically completed (stable France estimates). The files are honest about this gap and give clear instructions on what to claim and what not to claim. No contradictions between files were found on the core framing.