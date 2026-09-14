# REPORT-V6 release record

Current report: `reports/JMP_research_story_report_v6.html`.

SHA-256: `a5cb0e23d2b0cc28c88bfbbd85ebad287b6dc37a78980ab5307207df4b51f72c`.

Editable prose: `reports/research_story_build/v6_sections.py`; renderer: `build_v6.py`; fully resolved source: `story_v6.generated.md`. The renderer uses frozen v5 evidence and does not run estimation, diagnostics, pricing or ex-ante numerical work.

## What moved

- Report and paper: the decomposition operators, simulation rule, all coalition/Shapley tables and figures, numerical interpretations and decomposition-specific sensitivity text are in Appendix D, **Preliminary restricted-operator decomposition**. The old abstract, introduction and conclusion no longer carry a decomposition result.
- Deck: the former main operators, simulation-route and decomposition-result slides are in backup. Exact scope wording and the wage-offer-location diagnostic are separate backup frames. The standalone script follows 16 main frames and 10 backup frames; section dividers make the projection PDF 32 pages.
- The paper successor is `manuscript/JMP_working_paper_for_seminar_v6.tex` and `.pdf`. The report, paper, source and registry for v5 are preserved unchanged.
- All 18 report tables, 15 embedded figures and 125 predecessor scalar registry entries, including their provenance, are unchanged. Two diagnostic scalars were added from the supplied note. No historical ex-ante percentages were introduced.

## New appendix opening (verbatim)

A preliminary P/A/B decomposition has been computed for the attained-bundle money metric, holding resources, needs and composition fixed. It is a restricted counterfactual exercise, not a comprehensive share of inequality due to all opportunities. A separately defined ex-ante metric is being reconstructed for comparison; neither historical ex-ante percentages nor a settled cross-estimand conclusion are reported here.

The earning-opportunity channel equalises wage-offer location only: the systematic differences associated with education and potential experience, which shift offer locations by at most about 0.10 log points. The common offer spread (about 0.37 log points), wage-draw luck and selection remain in the residual and are quantitatively larger than the location differences removed by this operator. This is a definitional boundary of the exercise, not a measurement error. Equalising locations can change attained wages; it does not equalise the whole wage distribution. The diagnostic comparison that also compresses the common spread and selection is a bound, not an additional decomposition result. Thin effective support for couples leaves individual wage attainment noisy and remains a numerical limitation.

## Verification

10 of 11 gate commands pass. The number-to-source gate resolves all 6149 displayed result numerals, with zero unresolved values, sign mismatches, critical failures, retired-welfare hits or cross-surface conflicts. Offline rendering confirms 243 body math expressions, 3 additional navigation formulas, all images loaded, no JavaScript/math errors and no unresolved PDF citations. Paper layout passes; both deck builds have zero overfull or underfull boxes.

**Full suite status remains FAIL** because `check_reports_dir_lineage.py` flags ten older files outside this change. Six tracked files are byte-identical to task-start commit `61af387`; four files were untracked at task start and remain untouched. No lineage rule or exclusion was relaxed. The exact files and hashes are in `reports/report_v6_preexisting_lineage_findings.json`; command output is preserved in `reports/report_v6_gate_results.json`. The dedicated current-model, current-surface and appendix checks all pass.

## Authority and provenance

User REPORT-V6 explicitly authorizes commit and push of Job_Market_paper. Scope is the immediate report correction and companion presentation changes; no ex-ante numerical branch was started.
Mission input: `MNL/docs/JMP_WEA_reconstruction_and_discussant_update_mission_v1.md`; SHA-256 `65a9ba56a0b2943f618e60ed7ed17740d57f1936be160f5bb7137c3627fd29d8`.
Diagnostic input: `docs/Decomposition_diag_1.txt`; SHA-256 `ead1b7c8243fe1498f00dcf287331beec94165332aa3bb64041a0f645d339a74`.
Task-start Job_Market_paper commit: `61af387`. Source-only provenance blocks retain the accepted model, welfare, diagnostic and decomposition artifact locators and hashes.
