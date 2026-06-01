After considering your broader actual asset base, the strongest choice is still a **narrow France 2016 couples baseline**, but not in the old “because nothing else exists” sense. It is strongest as a **sequenced baseline** that gets the first decomposition result out quickly and then uses 2021, singles, and Germany as disciplined extensions rather than as baseline scope inflation. The documented implementation is still most mature, most coherent, and most explicitly decomposable at **France 2016 couples**; 2021 is available but still secondary, Germany is currently framed as an auxiliary benchmark, and the memos explicitly warn that the France singles runs are where visible pathologies have already appeared.   

A. **France 2016 couples**
Feasibility: **very high**. Clarity of contribution: **very high**. Identification credibility: **medium-high**. Decomposition clarity: **very high**. JMP signal: **high**. Coding and estimation risk: **medium**. Risk of over-expansion: **low**. Suitability for the next 2–4 weeks: **excellent**.
This is the only option for which the documented sample, utility specification, welfare object, inequality index, first table, and first figure already line up cleanly: France 2016, couples, Box-Cox couples utility, household AEI, household welfare Gini, and two-factor Shapley-Shorrocks decomposition. The weakness is not conceptual; it is France-specific instability in the current estimation system.  

B. **France 2016 all household types (couples + single females + single males)**
Feasibility: **medium**. Clarity of contribution: **medium**. Identification credibility: **medium-low**. Decomposition clarity: **medium-low**. JMP signal: **medium-high**. Coding and estimation risk: **high**. Risk of over-expansion: **high**. Suitability for the next 2–4 weeks: **weak**.
Given your own statement, the data and cleaned samples exist. The problem is not raw feasibility; it is integration. The currently documented prototype is built around a household/couples welfare object, while the France memos explicitly state that the visible pathological estimates are on the singles side. So this option would likely turn the next month into a three-model harmonization exercise before the first decomposition result exists.  

C. **France 2016 + 2021**
Feasibility: **medium-high**. Clarity of contribution: **high**. Identification credibility: **medium**. Decomposition clarity: **high**. JMP signal: **high**. Coding and estimation risk: **medium-high**. Risk of over-expansion: **medium**. Suitability for the next 2–4 weeks: **fair**.
This is a serious robustness design, not a bad idea. The issue is sequencing. The documents explicitly say 2021 is available as a secondary year, but they also say that the final data-year / EUROMOD system-year pairing is not yet fully locked. So making 2016+2021 the baseline would duplicate stabilization work before the first clean decomposition object is in hand.  

D. **France + Germany**
Feasibility: **medium**. Clarity of contribution: **medium-low**. Identification credibility: **medium-low**. Decomposition clarity: **medium-low**. JMP signal: **medium**. Coding and estimation risk: **very high**. Risk of over-expansion: **very high**. Suitability for the next 2–4 weeks: **poor**.
This is the most obvious over-expansion risk. The France status memo explicitly frames Germany as an **auxiliary German pooled panel**, and the prototype memo says Germany should remain a **diagnostic benchmark rather than a JMP headline design**. Moving to France+Germany at baseline would also push the paper toward comparative framing just when the project documents insist that decomposition, not ranking, should stay central.   

E. **France 2016 couples as baseline, with staged extensions after the first decomposition result**
Feasibility: **very high**. Clarity of contribution: **very high**. Identification credibility: **high**. Decomposition clarity: **very high**. JMP signal: **very high**. Coding and estimation risk: **medium-low**. Risk of over-expansion: **low**. Suitability for the next 2–4 weeks: **best**.
This is stronger than A because it uses the same empirically coherent baseline while explicitly acknowledging that you already have broader assets. The current memos already define the shortest credible path as: freeze France 2016 couples, stabilize the estimation, compute household AEI, run the region × education equalization and preference neutralization, and produce the one baseline table and one baseline figure. E preserves that discipline while treating 2021, singles, and Germany as sequenced credibility gains rather than distractions.  

## 1. Recommended baseline option

**E. France 2016 couples as baseline, with staged extensions after the first decomposition result.**

That is my recommendation after taking your actual broader implementation seriously. I am **not** recommending couples because the rest does not exist. I am recommending couples because the documented decomposition-ready object is still couples-based, the first table/figure are already defined on that basis, Germany is still explicitly auxiliary, and the singles side is exactly where the current France instability is most visible.  

## 2. Recommended staged extensions

**Stage 1:** **France 2021 couples**, same decomposition design, only after the France 2016 couples result exists and the year/system pairing is locked. This is the cleanest robustness extension because it keeps the unit of analysis, welfare object, and decomposition rule fixed.  

**Stage 2:** **France 2016 single females and single males**, but as **separate model extensions**, not as one pooled “all household types” baseline. That lets you test generality without contaminating the first result with cross-model aggregation issues. The reason this is stage 2 rather than stage 1 is that the current France memos explicitly flag singles as the place where pathological estimates already showed up.  

**Stage 3:** **Germany replication**, preferably starting with the closest analog to the France baseline rather than immediately expanding to all types. Germany should stay a replication / benchmark exercise until the France decomposition is stable.  

## 3. What should be postponed

Postpone these to later versions:

* **B as a pooled baseline**: do not make “all household types” the first empirical object.
* **D as a baseline**: do not make France + Germany the first paper identity.
* **Richer job hierarchies** (`jobloc`, `joblind`, `jobtot`) before the first baseline decomposition table.
* **Latent taste classes** or other richer preference heterogeneity structures before the first stable run.
* **Alternative welfare measures** beyond AEI as the headline object before the baseline couples decomposition exists.
* Any **country-ranking or comparative framing** in the main pitch.    

## 4. Whether I should rewrite the prototype memo

**Yes.**
You should rewrite it, but not because the current memo is wrong on substance. You should rewrite it because it still reads too much like a narrow baseline chosen by default. The new memo should make clear that:

* the baseline is **deliberately** France 2016 couples;
* this is chosen **despite** broader available assets, not because of their absence;
* 2021, singles, and Germany are now **sequenced extensions**, not vague future ideas.

Use a **Thinking chat** for that rewrite. Attach:
`JMP_prototype_memo_v2_france.md`, `JMP_france_status_memo_v1.md`, `JMP_core_packet_v1.md`, and `JMP_project_structure.md`.

Save the result as:
**`JMP_prototype_memo_v3_scope.md`**

## 5. A short decision memo

**Decision:** Use **France 2016 couples** as the empirical baseline, but formalize it as a **staged baseline** rather than as the whole empirical scope.

**Reason:** This is still the only scope for which the documented sample, welfare object, and decomposition design are already tightly aligned. Broadening immediately to all household types, a second year, or a second country would raise integration risk faster than it would raise scientific value in the next 2–4 weeks. The first objective is one stable decomposition result, not maximal coverage.  

**Extension order:**

1. France 2016 couples decomposition result.
2. France 2021 couples robustness.
3. France singles as separate extensions.
4. Germany replication last.

**Implication:** Rewrite the prototype memo so that this sequencing is explicit. Do not rewrite the paper identity around all household types or cross-country scope yet.
