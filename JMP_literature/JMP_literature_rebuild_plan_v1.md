I inspected the four current files you uploaded: `JMP_project_state_v1.md`, `JMP_welfare_spec_v5.md`, `Chat_gpt_lite.md`, and `Claude_lit.md`. Some older files from previous turns have expired, so I am not relying on them.

My recommendation: **yes, rebuild the JMP library now**, but do it as a **targeted JMP empirical-welfare library**, not as another broad theory-paper library. The library should be organized around your current JMP object:

```text
latent jobs / constrained opportunities
→ structural estimation
→ money-metric welfare
→ W¹–W⁶ welfare-family comparison
→ Shapley source decomposition
→ empirical implementation / microsimulation
```

Do **not** let the new library become a general social-choice library or a pure theory-paper bibliography. The separate theory paper already has its own library logic. This JMP library should serve the empirical paper.

## 1. Immediate decision

Proceed with a **three-pass library rebuild**:

```text
Pass 1 — Deep Research discovery
Pass 2 — adversarial audit / missing-source check
Pass 3 — local corpus construction: Zotero + summaries + indexes
```

This is worth doing now because the welfare spec has stabilized. Your library should now support the exact claims in `JMP_welfare_spec_v5.md`: ex-ante money-metric welfare, inclusive value/log-sum utility, latent jobs, opportunity heterogeneity, W¹–W⁶ responsibility spectrum, and Shapley access/ability/preference decomposition.

Do not start by summarizing 80 papers. Start by rebuilding the **map**, then triage.

---

# 2. Folder structure

Create this locally:

```text
JMP_literature/
  00_admin/
    JMP_literature_rebuild_plan_v1.md
    JMP_literature_source_inventory_v1.csv
    JMP_literature_tiers_v1.csv
    JMP_literature_decision_log_v1.md

  01_discovery_reports/
    DR01_JMP_literature_map_v1.md
    DR02_JMP_adversarial_gap_audit_v1.md
    DR03_JMP_final_source_inventory_v1.md

  02_pdfs/
    T1_core/
    T2_supporting/
    T3_background/
    needs_pdf/
    rejected_or_deferred/

  03_summaries/
    T1_core/
    T2_supporting/
    T3_background/

  04_indexes/
    INDEX_01_master_bibliography.md
    INDEX_02_structural_labor_supply_latent_jobs.md
    INDEX_03_welfare_measurement.md
    INDEX_04_opportunity_responsibility_social_choice.md
    INDEX_05_decomposition_and_inequality.md
    INDEX_06_empirical_implementation_microsimulation.md
    INDEX_07_writing_bank.md

  05_zotero_exports/
    JMP_zotero_export_v1.bib
    JMP_zotero_export_v1.csv

  06_prompts/
    prompt_DR01_deep_research.md
    prompt_DR02_adversarial_audit.md
    prompt_T1_summary.md
    prompt_index_builder.md
```

Keep the theory-paper library separate. Do not mix files from `jobs_and_wellbeing` unless a paper is directly useful for the JMP’s empirical welfare framing.

---

# 3. Pass 1 — Deep Research discovery

Tool: **ChatGPT Deep Research**

Attach or paste:

```text
JMP_project_state_v1.md
JMP_welfare_spec_v5.md
```

Optional, only if available:

```text
Literature_collection.md
current JMP bibliography .bib
current JMP draft or concept note
```

Save output as:

```text
JMP_literature/01_discovery_reports/DR01_JMP_literature_map_v1.md
```

Use this prompt:

```text
ROLE
You are a research assistant for an economics job market paper.

PROJECT
The paper studies unequal job opportunities and well-being inequality in a latent-jobs structural labour-supply model. The core question is:

How much of observed inequality in money-metric well-being is attributable to unequal job opportunities rather than heterogeneous preferences, once labour supply is modelled as choice among latent jobs?

The current welfare design computes a family of money-metric welfare measures W¹–W⁶, based on ex-ante attained utility / inclusive value from a structural latent-jobs model, then decomposes inequality through a Shapley–Shorrocks access / ability / preference decomposition.

TASK
Rebuild the literature map for this JMP only. Do not build a generic social-choice library and do not treat the separate theory paper as the target.

I need a structured source inventory for papers relevant to:

1. discrete-choice / structural labour-supply estimation;
2. latent jobs, RURO-type approaches, constrained opportunities, random opportunity sets;
3. wage-offer distributions and opportunity densities;
4. couples labour-supply models and joint opportunity sets;
5. welfare in random utility / discrete-choice models, including inclusive value, compensating variation, equivalent income, and money-metric welfare;
6. microsimulation / tax-benefit simulation linked to structural labour supply;
7. equality of opportunity, responsibility-sensitive welfare, and empirical welfare measurement;
8. Shapley / Shorrocks decomposition of inequality, especially source decomposition;
9. simulation error, importance sampling, effective sample size, and bootstrap inference in structural welfare analysis.

OUTPUT
Produce a Markdown report with exactly these sections:

1. Executive summary
2. Core literatures and how they map to the JMP
3. Tier 1 sources that must be read and summarized
4. Tier 2 sources that support specific claims
5. Tier 3 background sources
6. Missing-source risks
7. Papers that are probably irrelevant or should not be over-centered
8. Search strings used
9. Suggested Zotero tags
10. Recommended first 20 PDFs to collect
11. Source inventory table
12. Next-step plan

SOURCE INVENTORY TABLE
For each source, include:

- author/year/title;
- literature bucket;
- why it matters for the JMP;
- which JMP component it supports:
  estimation / opportunities / welfare / decomposition / inference / couples / microsimulation / writing motivation;
- priority tier T1/T2/T3;
- whether it is theoretical, empirical, methodological, or implementation-focused;
- what I can cite it for;
- what I should not cite it for;
- whether the PDF should be collected immediately.

STRICT RULES
- Do not invent references.
- If unsure about a source, mark it as “[uncertain, verify]”.
- Prefer peer-reviewed papers, working papers only when they are central or current.
- Do not over-center country ranking or beyond-GDP literature unless directly useful for money-metric well-being.
- Do not treat the separate pure theory paper as the JMP.
- The output should help me build a usable Zotero collection and then exhaustive summaries.
```

---

# 4. Pass 2 — adversarial audit

Tool: **Claude Research Mode** or **ChatGPT Deep Research**

Use this after DR01 is done.

Attach:

```text
DR01_JMP_literature_map_v1.md
JMP_project_state_v1.md
JMP_welfare_spec_v5.md
existing JMP bibliography if available
```

Save output as:

```text
JMP_literature/01_discovery_reports/DR02_JMP_adversarial_gap_audit_v1.md
```

Prompt:

```text
ROLE
You are an adversarial literature auditor for an economics job market paper.

TASK
Audit DR01_JMP_literature_map_v1.md against the actual JMP project state and welfare specification.

The paper is about unequal job opportunities and money-metric well-being inequality in a latent-jobs structural labour-supply model. The welfare specification uses W¹–W⁶, ex-ante attained utility / inclusive value, proposal-corrected opportunity integration, and Shapley decomposition into access / ability / preference.

AUDIT QUESTIONS
1. Which relevant literatures are under-covered?
2. Which papers are missing and should be added?
3. Which papers are over-included or not useful for the JMP?
4. Does DR01 confuse the JMP with the separate pure theory paper?
5. Does DR01 over-center beyond-GDP, country ranking, or pure optimal taxation?
6. Does DR01 adequately cover:
   - latent jobs / constrained opportunity sets;
   - structural labour supply;
   - welfare in random utility models;
   - equivalent income / compensating variation;
   - equality of opportunity / responsibility;
   - Shapley inequality decomposition;
   - microsimulation and tax-benefit modelling;
   - couples labour supply;
   - simulation/integration/inference issues?
7. What are the top 20 sources that must be summarized first?

OUTPUT
Produce a Markdown report with exactly these sections:

1. Audit verdict
2. What DR01 gets right
3. What DR01 misses
4. Over-included or distracting sources
5. Missing Tier 1 papers
6. Missing Tier 2 papers
7. Revised source-priority table
8. Revised Zotero tag scheme
9. Recommended first-summary batch
10. Final action list

STRICT RULES
- Do not invent references.
- Mark uncertain references as “[uncertain, verify]”.
- Give reasons for every recommended inclusion.
- Keep the JMP distinct from the separate theory paper.
```

---

# 5. Pass 3 — turn the reports into a local library plan

Tool: **Claude Code Sonnet** or **ChatGPT agent/Codex**

Input files:

```text
DR01_JMP_literature_map_v1.md
DR02_JMP_adversarial_gap_audit_v1.md
JMP_project_state_v1.md
JMP_welfare_spec_v5.md
```

Output files:

```text
JMP_literature/00_admin/JMP_literature_source_inventory_v1.csv
JMP_literature/00_admin/JMP_literature_tiers_v1.csv
JMP_literature/00_admin/JMP_literature_rebuild_plan_v1.md
```

Prompt:

```text
Work locally in my JMP_literature folder.

Read:
- 01_discovery_reports/DR01_JMP_literature_map_v1.md
- 01_discovery_reports/DR02_JMP_adversarial_gap_audit_v1.md
- JMP_project_state_v1.md
- JMP_welfare_spec_v5.md

Task:
Convert the discovery reports into a clean source inventory and tiering plan.

Create:
1. 00_admin/JMP_literature_source_inventory_v1.csv
2. 00_admin/JMP_literature_tiers_v1.csv
3. 00_admin/JMP_literature_rebuild_plan_v1.md

The CSV inventory must include:
- source_id;
- author_year;
- title;
- authors;
- year;
- literature_bucket;
- tier;
- priority_rank;
- JMP_component;
- why_needed;
- cite_for;
- do_not_cite_for;
- pdf_status;
- zotero_status;
- summary_status;
- notes.

Tiering rules:
T1 = must summarize exhaustively.
T2 = summarize selectively.
T3 = background or citation-only.
REJECT = not useful for this JMP.

Literature buckets:
- latent_jobs_RURO_opportunity_sets
- structural_labor_supply
- random_utility_welfare
- money_metric_equivalent_income
- responsibility_equality_of_opportunity
- Shapley_decomposition_inequality
- microsimulation_tax_benefit
- couples_labor_supply
- wage_offer_occupation_distribution
- simulation_inference_bootstrap
- motivation_positioning

The rebuild plan must specify:
- first 20 papers to collect;
- first 12 papers to summarize;
- Zotero tag scheme;
- summary order;
- index-building order;
- what not to do yet.

Do not invent missing metadata. Use placeholders like “[verify]” when needed.
```

---

# 6. Summary template for T1 papers

Use **Claude Project chat** or **ChatGPT Thinking** for individual summaries. Use this for Tier 1 sources.

Save each summary as:

```text
JMP_literature/03_summaries/T1_core/Author_Year_shorttitle.md
```

Prompt:

```text
ROLE
You are summarizing one paper for my economics JMP literature library.

PROJECT CONTEXT
My JMP studies unequal job opportunities and well-being inequality in a latent-jobs structural labour-supply model. The model separates preferences from job opportunities and later computes money-metric welfare W¹–W⁶ and a Shapley access / ability / preference decomposition.

TASK
Produce an exhaustive but structured Markdown summary of the attached paper. The goal is retrieval and later writing, not a short abstract.

Use exactly this structure:

# Author Year — Title

## 0. Metadata
- Full citation:
- Authors:
- Year:
- Journal / working paper:
- DOI / URL if available:
- Keywords:
- Tier:
- JMP component:

## 1. One-paragraph relevance to my JMP
Explain exactly why this paper matters for my JMP.

## 2. Research question and contribution
What problem does the paper solve? What is new?

## 3. Model objects
Define the paper’s choice set, preferences, constraints, opportunity sets, budget sets, welfare objects, and heterogeneity objects.

## 4. Estimation or theoretical method
Explain the method in enough detail that I can connect it to my structural model.

## 5. Treatment of opportunities
Does the paper model opportunities, constraints, feasible sets, latent jobs, job availability, choice-set formation, or random opportunities? If not, state that explicitly.

## 6. Treatment of preferences
How are preferences represented? What is estimated? What heterogeneity is attributed to preferences?

## 7. Welfare objects
Does the paper compute equivalent income, compensating variation, expected maximum utility, inclusive value, money-metric welfare, or social welfare? Give formulas where relevant.

## 8. Decomposition or inequality analysis
Does the paper decompose inequality, welfare changes, or policy effects? Explain.

## 9. Couples / household structure
If relevant, explain how couples or households are modelled.

## 10. Simulation, integration, and inference
Discuss simulation draws, Monte Carlo integration, importance sampling, bootstrap, standard errors, or numerical issues.

## 11. Key equations
List the equations most useful for my JMP.

## 12. Key empirical findings or theoretical results
Summarize only what is useful.

## 13. What I can cite this paper for
Give precise citation uses.

## 14. What I should not cite this paper for
Prevent overclaiming.

## 15. Relationship to JMP welfare spec W¹–W⁶
Explain whether this paper supports the inclusive-value welfare object, money-metric inversion, responsibility stance, opportunity decomposition, or alternative welfare measures.

## 16. Relationship to access / ability / preference decomposition
Explain how the paper maps, or fails to map, to my three-way decomposition.

## 17. Implementation lessons
What coding, estimation, data, or inference lessons should I take?

## 18. Direct quotations or passages to revisit
Do not quote long passages. Identify page/section references if available.

## 19. Open questions for my JMP
List unresolved questions this paper raises.

## 20. Final extraction table
Create a compact table with:
- object;
- paper’s version;
- JMP analogue;
- citation use;
- warning.

STRICT RULES
- Do not invent citations or page numbers.
- If uncertain, write “[uncertain, verify]”.
- Distinguish what the paper says from your interpretation.
```

---

# 7. Index-building prompt

After you have at least 12–20 summaries, build indexes.

Tool: **Claude Code Sonnet** or **ChatGPT agent/Codex**

Input:

```text
03_summaries/T1_core/*.md
03_summaries/T2_supporting/*.md
00_admin/JMP_literature_source_inventory_v1.csv
JMP_project_state_v1.md
JMP_welfare_spec_v5.md
```

Output:

```text
04_indexes/INDEX_01_master_bibliography.md
04_indexes/INDEX_02_structural_labor_supply_latent_jobs.md
04_indexes/INDEX_03_welfare_measurement.md
04_indexes/INDEX_04_opportunity_responsibility_social_choice.md
04_indexes/INDEX_05_decomposition_and_inequality.md
04_indexes/INDEX_06_empirical_implementation_microsimulation.md
04_indexes/INDEX_07_writing_bank.md
```

Prompt:

```text
Work locally in JMP_literature.

Read:
- all summaries in 03_summaries/
- 00_admin/JMP_literature_source_inventory_v1.csv
- JMP_project_state_v1.md
- JMP_welfare_spec_v5.md

Task:
Build the JMP literature indexes.

Create:
1. 04_indexes/INDEX_01_master_bibliography.md
2. 04_indexes/INDEX_02_structural_labor_supply_latent_jobs.md
3. 04_indexes/INDEX_03_welfare_measurement.md
4. 04_indexes/INDEX_04_opportunity_responsibility_social_choice.md
5. 04_indexes/INDEX_05_decomposition_and_inequality.md
6. 04_indexes/INDEX_06_empirical_implementation_microsimulation.md
7. 04_indexes/INDEX_07_writing_bank.md

Index rules:
- Organize by claim, not only by author.
- Every claim must list supporting sources.
- Add warnings where the source does not fully support the claim.
- Separate “citation-ready” from “needs verification”.
- Do not invent references.
- Do not import theory-paper claims unless they support the JMP.

INDEX_07_writing_bank must include paper-ready paragraph skeletons for:
1. why latent jobs matter;
2. why opportunities are not preferences;
3. why money-metric welfare must respect feasible sets;
4. why W¹–W⁶ is a responsibility-sensitivity surface;
5. why Shapley access / ability / preference decomposition is appropriate;
6. why this is not merely microsimulation;
7. why this is not a country-ranking paper.
```

---

# 8. Should you run Deep Research again?

Yes, but only **once initially**, then one adversarial audit. Do not run five broad searches.

The first Deep Research run should answer:

```text
What is the correct literature universe for this empirical JMP?
```

The second audit should answer:

```text
What did the first run miss or overinclude?
```

After that, stop searching and start collecting PDFs + summaries.

## My recommended immediate action

Do this now:

```text
1. Run DR01 in ChatGPT Deep Research.
2. Save as DR01_JMP_literature_map_v1.md.
3. Run DR02 adversarial audit in Claude Research Mode.
4. Save as DR02_JMP_adversarial_gap_audit_v1.md.
5. Then bring both reports back here.
```

I will then help you decide the first 12–20 sources to summarize and produce the exact `tiers.csv` / Zotero tagging plan.

Current output should be saved as:

```text
JMP_literature_rebuild_plan_v1.md
```

Category: **working library-rebuild plan**, not a concept note.
