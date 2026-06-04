# JMP Index Build Report v1

## 1. Index build verdict

**COMPLETE WITH MINOR CITATION-METADATA REPAIRS.**

The first claim-oriented indexes for the accepted T1A/T1B corpus have been
built. They are suitable for reading, retrieval, and targeted follow-up planning.
They are not final manuscript-citation ready because the repair queue still
contains BibTeX, DOI, pagination, and version warnings.

## 2. Files inspected

- `JMP_literature/00_admin/JMP_T1A_T1B_completion_QC_report_v1.md`
- `JMP_literature/00_admin/JMP_T1A_T1B_acceptance_list_v1.csv`
- `JMP_literature/00_admin/JMP_T1A_T1B_remaining_repair_queue_v1.csv`
- `JMP_literature/00_admin/JMP_literature_tiers_expanded_v1.csv`
- `JMP_project_state_v1.md`
- `JMP_welfare_spec_v5.md`
- 13 accepted individual summaries in `JMP_literature/03_summaries/T1A/`
- 10 accepted official individual summaries in `JMP_literature/03_summaries/T1B/`
- 1 accepted supplementary summary in `JMP_literature/03_summaries/T1B/`

## 3. Files excluded

- `JMP_literature/03_summaries/archive/`
- `all_summaries_T1_COMBINED_NONCANONICAL.md`
- `all_summaries_T1A_COMBINED_NONCANONICAL.md`
- `all_summaries_T1B_COMBINED_NONCANONICAL.md`
- Any non-canonical combined summary file

## 4. Index files created

- `JMP_literature/04_indexes/INDEX_00_T1A_T1B_status_v1.md`
- `JMP_literature/04_indexes/INDEX_01_master_bibliography_v1.md`
- `JMP_literature/04_indexes/INDEX_02_latent_jobs_and_opportunities_v1.md`
- `JMP_literature/04_indexes/INDEX_03_welfare_and_money_metric_v1.md`
- `JMP_literature/04_indexes/INDEX_04_responsibility_and_equality_of_opportunity_v1.md`
- `JMP_literature/04_indexes/INDEX_05_decomposition_v1.md`
- `JMP_literature/04_indexes/INDEX_06_microsimulation_and_estimation_v1.md`
- `JMP_literature/04_indexes/INDEX_07_inference_and_computation_v1.md`
- `JMP_literature/04_indexes/INDEX_08_writing_bank_v1.md`

## 5. Accepted T1A/T1B coverage

Coverage is complete for indexing:

- T1A official summaries accepted: 13/13.
- T1B official summaries accepted: 10/10.
- Supplementary accepted summaries: 1 (`Fleurbaey_Maniquet_2018_IJET_inequality_averse.md`).
- Accepted official paths in the acceptance list: 23/23 present.

## 6. Citation metadata warnings carried forward

- Aaberge & Colombino 2018: BibTeX entry missing.
- Aaberge, Dagsvik & Strom 1995: BibTeX entry missing.
- Capeau & Decoster 2016: BibTeX author corruption and year/version ambiguity.
- Capeau et al. 2015/2016 RURO: project key year vs outlet year.
- Beffy et al. 2019: in-press vs published pagination.
- Bhattacharya 2015: DOI/JSTOR metadata pending.
- Dagsvik & Karlstrom 2005: DOI/JSTOR metadata pending.
- Shorrocks 1982: DOI/JSTOR metadata pending.
- Sastre & Trannoy 2002: DOI metadata pending.
- Jacquet, Jia & Thoresen 2026: SSRN/DOI status pending.
- Sutherland & Figari 2013: WP vs journal-version choice pending.
- Several summaries use ad-hoc metadata keys that should be reconciled with
  canonical `.bib` keys.

## 7. Main literature strengths

- Strong latent-jobs/RURO foundation for modeling feasible job packages and
  separating preferences from opportunity density.
- Strong random-utility welfare and equivalent-income foundation for a
  preference-respecting money-metric object.
- Strong Shapley-Shorrocks foundation for exact, order-independent decomposition.
- Strong microsimulation infrastructure support for EUROMOD as the disposable
  income engine.
- Clear nearest-comparator positioning against Bargain et al. 2013 and Jacquet
  et al. 2026.

## 8. Main remaining gaps

- Direct literature support for occupation-as-access is weak; the accepted
  sources mostly omit occupation or contain occupation/sector conflation.
- Direct support for the within-opportunity access/ability split is partial; the
  ability channel is supported through wage-technology objects and normative
  responsibility logic, but the exact three-way cut is the JMP's design.
- The exact computation problem of ex-ante money-metric welfare over sampled,
  heterogeneous feasible sets remains under-covered.
- The accepted literature does not itself contain the W^1-W^6 family; that
  remains imported from the companion theory paper and must be cited/bounded as
  such.

## 9. Whether targeted Deep Research is now ready

**Yes.** The indexes identify targeted search needs clearly:

- occupation-as-access versus occupation-as-preference/industry;
- ability versus access in wage-offer or wage-technology models;
- computation and inference for welfare over sampled heterogeneous opportunity
  sets;
- citation metadata repair for the pending queue.

Deep Research should be targeted, not broad corpus rebuilding.

## 10. Immediate next action

Use the indexes to draft the literature-positioning and method-defense sections,
while separately closing the citation metadata repair queue before final
manuscript citation.
