Below is the consolidated plan from **this moment onward**. This supersedes the earlier v1/v2/v3 variants.

Save this as:

```text
JMP_literature_rebuild_master_plan_v1.md
```

Category: **working library-rebuild plan**.

## Current state

Phase 0 is complete. Do not repeat it.

You already have:

```text
JMP_literature/00_admin/JMP_existing_corpus_inventory_v1.csv
JMP_literature/00_admin/JMP_existing_bibtex_audit_v1.md
JMP_literature/00_admin/JMP_pdf_inventory_v1.csv
JMP_literature/00_admin/JMP_literature_rebuild_decision_log_v1.md
```

Phase 0 found a large but imperfect corpus:

```text
87 BibTeX entries
73 PDFs in Literature/
72 markdown extractions
17 essential papers in bib but no portable PDF in Literature/
2+ PDF/MD papers with no BibTeX entry
~20 BibTeX metadata repairs
1 duplicate bib entry to delete
```

So the task is no longer “discover the literature.” The task is:

```text
discipline existing corpus
→ lock tiers and prompts
→ summarize first core batch
→ then run one targeted gap audit
```

Do **not** start Deep Research yet.
Do **not** start T1 summaries yet.
Do **not** redo Phase 0.

---

# The one plan

## Phase 1 — Protocol, tiering, and repair queues

This is the immediate next step.

Purpose: turn the Phase 0 audit into an operational extraction system.

Tool: **Claude Code Sonnet**.

Input files to place in the workspace:

```text
JMP_literature/00_admin/JMP_existing_corpus_inventory_v1.csv
JMP_literature/00_admin/JMP_existing_bibtex_audit_v1.md
JMP_literature/00_admin/JMP_pdf_inventory_v1.csv
JMP_literature/00_admin/JMP_literature_rebuild_decision_log_v1.md

summary_T1.md
summary_T2.md
tiers.csv

JMP_project_state_v1.md
JMP_welfare_spec_v5.md
JMP_lit_collection.bib
```

If `summary_T1.md`, `summary_T2.md`, or `tiers.csv` are not in the local workspace, reattach or copy them there. Some older uploads in this chat have expired, but if the files exist locally, use those local versions.

Expected outputs:

```text
JMP_literature/00_admin/JMP_phase1_protocol_tiering_report_v1.md
JMP_literature/00_admin/JMP_literature_tiers_expanded_v1.csv
JMP_literature/00_admin/JMP_missing_pdf_acquisition_queue_v1.csv
JMP_literature/00_admin/JMP_bibtex_repair_queue_v1.md
JMP_literature/06_prompts/JMP_T1_exhaustive_extraction_prompt_v2.md
JMP_literature/06_prompts/JMP_T2_focused_extraction_prompt_v2.md
JMP_literature/00_admin/JMP_first_extraction_batch_v1.md
```

Send this prompt to Claude Code Sonnet:

```text
Work locally in my JMP literature workspace.

This is Phase 1 of rebuilding the literature library for my economics JMP.

Phase 0 is complete. Do not repeat Phase 0. Do not summarize papers yet. Do not run external searches.

Read:
- JMP_literature/00_admin/JMP_existing_corpus_inventory_v1.csv
- JMP_literature/00_admin/JMP_existing_bibtex_audit_v1.md
- JMP_literature/00_admin/JMP_pdf_inventory_v1.csv
- JMP_literature/00_admin/JMP_literature_rebuild_decision_log_v1.md
- summary_T1.md
- summary_T2.md
- tiers.csv
- JMP_project_state_v1.md
- JMP_welfare_spec_v5.md
- JMP_lit_collection.bib

Task:
Use the Phase 0 audit to create the operational Phase 1 literature-rebuild files.

Create:
1. JMP_literature/00_admin/JMP_phase1_protocol_tiering_report_v1.md
2. JMP_literature/00_admin/JMP_literature_tiers_expanded_v1.csv
3. JMP_literature/00_admin/JMP_missing_pdf_acquisition_queue_v1.csv
4. JMP_literature/00_admin/JMP_bibtex_repair_queue_v1.md
5. JMP_literature/06_prompts/JMP_T1_exhaustive_extraction_prompt_v2.md
6. JMP_literature/06_prompts/JMP_T2_focused_extraction_prompt_v2.md
7. JMP_literature/00_admin/JMP_first_extraction_batch_v1.md

Main objectives:
- Reconcile the Phase 0 inventory with the existing tiers.csv.
- Do not treat all preliminary Tier 1 labels as final Tier 1. Produce disciplined final tiers.
- Correct the extraction protocol so it matches the current JMP welfare specification.
- Replace outdated two-factor opportunity/preference language with the current access / ability / preference decomposition wherever appropriate.
- Preserve the distinction between this empirical JMP and the separate pure theory paper.
- Build a practical first extraction batch.

The expanded tiers CSV must include:
- bibkey
- author_year
- title
- current_tier_from_tiers_csv
- preliminary_tier_from_inventory
- final_recommended_tier
- priority_rank
- JMP_component
- literature_bucket
- extraction_prompt
- pdf_status
- md_extraction_status
- bibtex_status
- cite_for
- do_not_cite_for
- overclaim_warning
- extraction_status
- notes
- metadata_needs_verification

Use these final tiers:
- T1A = summarize immediately; core to JMP identification/model/welfare/decomposition.
- T1B = summarize after T1A; important but not first batch.
- T2 = selective summary.
- T3 = background/citation only.
- DEFER = later extension.
- REJECT = not useful for this JMP.

The missing-PDF acquisition queue must prioritize:
1. essential T1A/T1B papers with bib but no portable PDF in Literature/;
2. essential papers with PDF in Zotero files path but not in Literature/;
3. papers added from gap-check but lacking PDFs or MD extractions.

The BibTeX repair queue must include:
- delete GDPQuestMeasure duplicate stub;
- fix corrupted Capéau / Decoster author names;
- add missing BibTeX for Aaberge, Dagsvik & Strøm 1995 if confirmed;
- verify chapter_10 and chapter_11 identities;
- verify Aaberge & Colombino 2018 bib entry;
- fix stubs and missing author/title metadata;
- list DOI/URL repairs separately.

The T1 extraction prompt must be exhaustive and retrieval-oriented. It must cover:
- latent jobs / RURO;
- constrained opportunities;
- opportunity density;
- proposal correction;
- wage ability;
- access / market opportunity;
- occupation-conditioned wage draws;
- couples joint choice;
- inclusive value;
- money-metric welfare;
- W¹–W⁶ welfare family;
- responsibility and equality of opportunity;
- Shapley access / ability / preference decomposition;
- microsimulation / EUROMOD;
- inference, bootstrap, simulation error, numerical implementation;
- contribution mapping and overclaim warnings.

The T2 prompt must be shorter, but aligned with the same JMP components.

The first extraction batch must include:
- first 12 papers to summarize now;
- next 8 papers to summarize after that;
- reason for each;
- whether PDF and MD extraction exist;
- whether missing PDF blocks extraction.

Do not invent metadata. Use [verify] where uncertain.
Do not summarize papers.
Do not run external searches.
```

After Claude Code returns Phase 1, bring back exactly these files:

```text
JMP_phase1_protocol_tiering_report_v1.md
JMP_literature_tiers_expanded_v1.csv
JMP_missing_pdf_acquisition_queue_v1.csv
JMP_bibtex_repair_queue_v1.md
JMP_first_extraction_batch_v1.md
JMP_T1_exhaustive_extraction_prompt_v2.md
JMP_T2_focused_extraction_prompt_v2.md
```

Then I will review whether the first extraction batch is correct before you start summarizing.

---

## Phase 1 review — before extraction

Tool: **this chat / Thinking chat**.

Purpose: check whether the Phase 1 output is sane.

I will review:

```text
1. Whether T1A/T1B tiers are sensible.
2. Whether the first 12 papers are the right first batch.
3. Whether decomposition / EOp gaps are blocking.
4. Whether the T1 prompt is sufficiently aligned with JMP_welfare_spec_v5.
5. Whether missing PDFs should be acquired before extraction begins.
```

Decision after review:

```text
A. begin T1A extraction immediately from available PDFs; or
B. first collect missing decomposition/EOp PDFs; or
C. revise tiers/prompt before extraction.
```

Do not skip this review.

---

## Phase 2 — T1A extraction

Start only after Phase 1 review.

Tool: **Claude Project chat** or **ChatGPT Thinking** for each paper. Use **one paper per run**.

Use:

```text
JMP_literature/06_prompts/JMP_T1_exhaustive_extraction_prompt_v2.md
```

Inputs for each paper:

```text
PDF of the paper
JMP_project_state_v1.md
JMP_welfare_spec_v5.md
JMP_T1_exhaustive_extraction_prompt_v2.md
```

Output folder:

```text
JMP_literature/03_summaries/T1A/
```

Filename pattern:

```text
AuthorYear_shorttitle_T1A.md
```

The first batch should come from:

```text
JMP_literature/00_admin/JMP_first_extraction_batch_v1.md
```

Do not use the old `summary_T1.md` as-is unless Phase 1 explicitly preserves it. The current project needs the expanded v2 prompt, because it must extract:

```text
W¹–W⁶
inclusive value
money-metric inversion
access / ability / preference Shapley decomposition
proposal correction
couples joint choice
occupation-conditioned wage draws
inference / bootstrap / simulation error
```

After the first 3 summaries, bring them back here for quality control before summarizing all 12.

Expected first quality-control files:

```text
JMP_literature/03_summaries/T1A/<paper1>.md
JMP_literature/03_summaries/T1A/<paper2>.md
JMP_literature/03_summaries/T1A/<paper3>.md
```

I will check whether the prompt is producing useful extractions or whether it needs tightening.

---

## Phase 2A — missing PDF acquisition, parallel but bounded

Tool: **manual / Zotero / browser**, or **Claude Code for file inventory only**.

Do this only for papers in:

```text
JMP_missing_pdf_acquisition_queue_v1.csv
```

Priority:

```text
1. T1A missing PDFs.
2. T1B missing PDFs.
3. decomposition / Shorrocks / Sastre-Trannoy / EOp papers needed for welfare spec.
4. remaining T2.
```

Do not spend time collecting every T3 paper now.

Expected output:

```text
JMP_literature/00_admin/JMP_pdf_acquisition_log_v1.md
```

Minimal log structure:

```text
source_id | bibkey | title | status | PDF path | notes
```

---

## Phase 3 — Targeted Deep Research gap audit

Run this **after Phase 1 and after at least the first T1A batch has started**. Do not run it now.

Tool: **ChatGPT Deep Research**.

Inputs:

```text
JMP_project_state_v1.md
JMP_welfare_spec_v5.md
JMP_literature_tiers_expanded_v1.csv
JMP_phase1_protocol_tiering_report_v1.md
JMP_missing_pdf_acquisition_queue_v1.csv
JMP_first_extraction_batch_v1.md
```

Save as:

```text
JMP_literature/01_discovery_reports/DR03_JMP_targeted_gap_audit_v1.md
```

Prompt:

```text
ROLE
You are a targeted literature-gap auditor for an economics job market paper.

PROJECT
The JMP studies unequal job opportunities and money-metric well-being inequality in a latent-jobs structural labour-supply model. It estimates opportunity heterogeneity, computes W¹–W⁶ money-metric welfare measures from inclusive value, and decomposes welfare inequality into access, ability, and preference using Shapley–Shorrocks.

INPUTS
I provide:
- JMP_project_state_v1.md
- JMP_welfare_spec_v5.md
- JMP_literature_tiers_expanded_v1.csv
- JMP_phase1_protocol_tiering_report_v1.md
- JMP_missing_pdf_acquisition_queue_v1.csv
- JMP_first_extraction_batch_v1.md

TASK
Do not produce a broad literature review. Audit the existing corpus for missing or under-covered papers needed for this specific JMP.

Focus only on:
1. latent jobs / RURO / constrained opportunity sets;
2. structural labour supply with random opportunities;
3. wage-offer distributions and occupation-conditioned wage draws;
4. couples labour supply and joint choice sets;
5. random utility welfare, inclusive value, compensating variation, equivalent variation;
6. money-metric welfare / equivalent income;
7. responsibility-sensitive welfare and equality of opportunity;
8. Shapley / Shorrocks decomposition;
9. microsimulation / EUROMOD linked to behavioural labour supply;
10. sampling of alternatives, simulation error, bootstrap inference.

OUTPUT
Use exactly these sections:
1. Audit verdict
2. Existing corpus strengths
3. Missing Tier 1 candidates
4. Missing Tier 2 candidates
5. Sources currently over-weighted
6. Sources to demote or defer
7. Missing methods papers for inference
8. Missing welfare papers for inclusive value / money metric
9. Missing decomposition papers
10. Missing couples / joint-choice papers
11. Revised first-summary batch
12. Exact sources to add to Zotero
13. Exact sources to search manually
14. Final action list

RULES
- Do not invent references.
- If uncertain, write [uncertain, verify].
- Do not confuse this JMP with the separate theory paper.
- Do not recommend broad beyond-GDP sources unless directly useful.
- Do not recommend pure optimal-tax papers unless they support structural labour-supply or welfare.
```

After Deep Research returns, bring back:

```text
DR03_JMP_targeted_gap_audit_v1.md
```

Then I will decide whether to update tiers or continue extraction.

---

## Phase 4 — Index construction

Run this only after at least 12–20 summaries exist.

Tool: **Claude Code Sonnet**.

Inputs:

```text
JMP_literature/03_summaries/T1A/*.md
JMP_literature/03_summaries/T1B/*.md
JMP_literature/00_admin/JMP_literature_tiers_expanded_v1.csv
JMP_project_state_v1.md
JMP_welfare_spec_v5.md
```

Outputs:

```text
JMP_literature/04_indexes/INDEX_01_master_bibliography.md
JMP_literature/04_indexes/INDEX_02_latent_jobs_and_opportunities.md
JMP_literature/04_indexes/INDEX_03_welfare_and_money_metric.md
JMP_literature/04_indexes/INDEX_04_responsibility_and_equality_of_opportunity.md
JMP_literature/04_indexes/INDEX_05_decomposition.md
JMP_literature/04_indexes/INDEX_06_microsimulation_and_estimation.md
JMP_literature/04_indexes/INDEX_07_inference_and_computation.md
JMP_literature/04_indexes/INDEX_08_writing_bank.md
```

Prompt:

```text
Work locally in JMP_literature.

Read:
- all summaries in JMP_literature/03_summaries/
- JMP_literature/00_admin/JMP_literature_tiers_expanded_v1.csv
- JMP_project_state_v1.md
- JMP_welfare_spec_v5.md

Task:
Build retrieval indexes for writing the JMP.

Create:
1. INDEX_01_master_bibliography.md
2. INDEX_02_latent_jobs_and_opportunities.md
3. INDEX_03_welfare_and_money_metric.md
4. INDEX_04_responsibility_and_equality_of_opportunity.md
5. INDEX_05_decomposition.md
6. INDEX_06_microsimulation_and_estimation.md
7. INDEX_07_inference_and_computation.md
8. INDEX_08_writing_bank.md

Rules:
- Organize by claim, not only by author.
- Every claim must list supporting sources.
- Mark each source support as:
  explicit / analogy / background / weak.
- Add “do not overclaim” warnings.
- Do not invent citations.
- Keep the JMP separate from the theory paper.

INDEX_08_writing_bank must include paragraph skeletons for:
1. latent jobs as the empirical unit;
2. opportunity heterogeneity versus preference heterogeneity;
3. why occupation belongs in the opportunity layer;
4. why money-metric welfare must read feasible sets;
5. why W¹–W⁶ is a responsibility-sensitivity surface;
6. why Shapley access/ability/preference decomposition is appropriate;
7. why microsimulation is supporting infrastructure, not the paper’s identity;
8. why the paper is not a country-ranking exercise;
9. why the paper is not merely another structural labour-supply application.
```

---

# Short operational checklist

From this moment, do exactly this:

```text
1. Run Phase 1 in Claude Code Sonnet.
2. Bring Phase 1 outputs back here.
3. I review the first extraction batch and prompts.
4. Start the first 3 T1A summaries.
5. Bring first 3 summaries back here for quality control.
6. Continue first 12 T1A summaries.
7. Run targeted Deep Research gap audit.
8. Update tiers if needed.
9. Build indexes after 12–20 summaries.
```

Do not do these yet:

```text
Do not run Deep Research now.
Do not summarize papers before Phase 1 prompt/tier lock.
Do not build indexes now.
Do not collect every missing PDF indiscriminately.
Do not mix the theory-paper library into this JMP library.
```

The immediate next task is therefore unambiguous:

```text
Run Phase 1 protocol/tiering and repair queues in Claude Code Sonnet.
```
