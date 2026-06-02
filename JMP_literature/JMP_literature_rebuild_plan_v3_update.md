I inspected the new files. They **do not overturn the plan**, but they change the immediate execution order.

The main change is this: you already have more infrastructure than I assumed. You now have:

```text
summary_T1.md
summary_T2.md
tiers.csv
```

So we should **not start with Phase 0 from scratch** and we should **not run Deep Research first**. The correct next action is a **protocol-alignment audit**: reconcile the existing T1/T2 prompts and tier list with the current JMP state and welfare spec, then start extracting.

## 1. What the new files imply

`summary_T1.md` is already a strong project-oriented extraction prompt. It is much better than a generic paper-summary template. It correctly emphasizes structural labor supply, RURO / latent jobs, welfare, Shapley–Shorrocks, and overclaim risks.

But it is **not sufficient as the canonical prompt for the current JMP**. It is too compressed relative to the welfare spec and the current estimator state. It has only 16 sections. It does not force enough extraction on:

```text
W¹–W⁶ welfare-family mapping,
inclusive value / money-metric inversion,
proposal correction,
access / ability / preference decomposition,
couples joint-choice structure,
occupation-conditioned wage draws,
active constraints / inference / simulation error,
implementation lessons for the JAX / CONOPT / bootstrap pipeline.
```

More importantly, it contains an outdated project anchor:

```text
two-factor Shapley-Shorrocks decomposition:
opportunity-driven component and preference-driven component
```

Your current welfare/decomposition plan is richer. It is not only opportunity versus preference. The active JMP direction is closer to:

```text
access / ability / preference
```

with (W^1,\dots,W^6) as a responsibility-sensitivity surface. So this must be corrected before using the prompt systematically.

`summary_T2.md` is useful as a supporting-paper prompt. Keep it, but revise the same outdated two-factor language. It is appropriate for T2/T3 sources, not for core papers.

`tiers.csv` is useful. It has 84 entries: 15 T1, 25 T2, and 44 T3. That means local tiering has already started. But the file is too thin: it only has `bibkey,tier`. For a real literature library, it must be expanded with component, citation use, overclaim warning, PDF status, and summary status.

The T1 list is reasonable but needs audit. Some likely changes:

```text
Likely promote to T1:
- Capéau / Decoster / Dekkers random opportunities, if this is the RURO benchmark.
- Bhattacharya empirical welfare analysis in discrete choice, if available.
- Bargain et al. 2013 may need T1 if it is the closest welfare + labor supply comparator.
- Hufe et al. may need T1 if the fairness/opportunity component is central to writing.

Likely verify:
- Jacquet 2026 should be checked carefully before relying on it.
- Bhattacharya 2015 vs 2018 metadata should be verified.
- Duplicate-check entries should not remain in final tiers.
```

So the plan changes from “build inventory first” to:

```text
1. Align prompts + tiers with current JMP.
2. Expand tiers.csv into a full source inventory.
3. Start T1 extraction.
4. Run targeted Deep Research gap audit after the first inventory, not before.
```

## 2. Revised immediate plan

### Step 1 — Protocol and tier alignment audit

Tool/chat: **Claude Code Sonnet** if you want it done locally over files. Use **Claude Project chat / ChatGPT Thinking** if you want a methodological review.

Files to attach/place in workspace:

```text
summary_T1.md
summary_T2.md
tiers.csv
JMP_project_state_v1.md
JMP_welfare_spec_v5.md
JMP_lit_collection.bib
deep-research-report_update.md
JMP_gap_check_v1.md
```

Save output as:

```text
JMP_literature/00_admin/JMP_literature_protocol_alignment_audit_v1.md
JMP_literature/00_admin/JMP_literature_tiers_expanded_v1.csv
JMP_literature/06_prompts/JMP_T1_exhaustive_extraction_prompt_v2.md
JMP_literature/06_prompts/JMP_T2_focused_extraction_prompt_v2.md
```

Prompt:

```text
Work locally in my JMP_literature workspace.

This is for my economics JMP literature library.

Read:
- summary_T1.md
- summary_T2.md
- tiers.csv
- JMP_project_state_v1.md
- JMP_welfare_spec_v5.md
- JMP_lit_collection.bib
- deep-research-report_update.md
- JMP_gap_check_v1.md

Task:
Audit and align the existing literature-extraction prompts and tier file with the current JMP project state and welfare specification.

Create:
1. JMP_literature/00_admin/JMP_literature_protocol_alignment_audit_v1.md
2. JMP_literature/00_admin/JMP_literature_tiers_expanded_v1.csv
3. JMP_literature/06_prompts/JMP_T1_exhaustive_extraction_prompt_v2.md
4. JMP_literature/06_prompts/JMP_T2_focused_extraction_prompt_v2.md

The audit must answer:
1. Whether summary_T1.md is sufficient as the canonical T1 prompt.
2. Whether summary_T2.md is sufficient as the canonical T2 prompt.
3. Which wording is outdated relative to JMP_project_state_v1.md and JMP_welfare_spec_v5.md.
4. Whether the two-factor opportunity/preference decomposition language must be replaced by access / ability / preference language.
5. Whether W¹–W⁶, inclusive value, money-metric inversion, and Shapley decomposition are adequately covered.
6. Whether couples, occupation-conditioned wage draws, proposal correction, and inference are adequately covered.
7. Which T1/T2/T3 tier assignments in tiers.csv should be reviewed.
8. Which sources should be promoted or demoted.

For the expanded tier CSV, include:
- bibkey
- current_tier
- recommended_tier
- author_year
- title
- JMP_component
- literature_bucket
- priority_rank
- cite_for
- do_not_cite_for
- extraction_prompt
- pdf_status
- summary_status
- notes
- metadata_needs_verification

For the revised T1 prompt:
- Keep the retrieval-oriented style of summary_T1.md.
- Expand it to cover:
  W¹–W⁶,
  inclusive value,
  money-metric inversion,
  proposal correction,
  access / ability / preference decomposition,
  couples joint choice,
  occupation-conditioned wage draws,
  inference,
  numerical implementation,
  contribution mapping.
- Remove or correct the outdated two-factor decomposition language.
- Do not confuse this empirical JMP with the separate theory paper.

For the revised T2 prompt:
- Keep it shorter than the T1 prompt.
- Preserve alignment with the T1 prompt section numbers where useful.
- Correct the decomposition language.
- Make it suitable for supporting papers only.

Do not invent metadata. Use [verify] where needed.
Do not run external searches.
```

### Step 2 — Start extraction only after the revised prompts exist

Tool/chat: **Claude Project chat** or **ChatGPT Thinking** for individual papers. Use file attachments.

First target should be the **first T1 batch**, but after the tier audit. Tentatively:

```text
1. Dagsvik et al. 2014
2. Dagsvik and Jia 2016
3. Aaberge et al. 2009
4. Aaberge and Colombino 2013
5. Van Soest 1995
6. Capéau et al. random opportunities / RURO
7. Bhattacharya empirical welfare analysis
8. Bargain et al. welfare and labor supply
9. Dagsvik and Karlström 2005
10. Shorrocks 2013
11. Hufe et al. 2022
12. Sutherland and Figari 2013
```

Do not rigidly follow the current `tiers.csv` if the alignment audit recommends changes.

### Step 3 — Targeted Deep Research only after the tier audit

Tool/chat: **ChatGPT Deep Research**

Inputs:

```text
JMP_literature_tiers_expanded_v1.csv
JMP_literature_protocol_alignment_audit_v1.md
JMP_project_state_v1.md
JMP_welfare_spec_v5.md
```

Save as:

```text
JMP_literature/01_discovery_reports/DR03_JMP_targeted_gap_audit_v1.md
```

Purpose:

```text
Find missing core papers, not rebuild the whole library.
```

## 3. Do these files change the extraction prompt?

Yes. They make it clear that your extraction system already has a good base, but the **canonical T1 prompt should be the longer enhanced version**, not `summary_T1.md` as-is.

`summary_T1.md` is a good lean version. I would keep it as:

```text
JMP_T1_lean_extraction_prompt_v1.md
```

But for the core 12–20 papers, use the enhanced prompt from the previous plan, revised with the decomposition correction:

```text
opportunity / preference
```

should become:

```text
access / ability / preference
```

where appropriate.

The core extraction prompt must force the model to answer:

```text
Does this source support:
- latent jobs?
- opportunity sets?
- estimated opportunity density?
- proposal correction?
- money-metric welfare?
- inclusive value?
- W¹–W⁶ responsibility surface?
- access / ability / preference decomposition?
- couples product choice?
- occupation-conditioned wage offers?
- inference / bootstrap / simulation error?
```

That is the key difference between a usable JMP library and a generic literature review.

## 4. Updated decision

Use this as the operating decision:

```text
Do not run Deep Research yet.
Do not start summarizing with summary_T1.md as-is.
First run a prompt/tier alignment audit.
Then use the revised T1/T2 prompts.
Then summarize the first T1 batch.
Then run one targeted Deep Research gap audit.
```

Save this reply as:

```text
JMP_literature_rebuild_plan_v3_update.md
```

Category: **working library-rebuild plan update**, not a concept note.
