# Consistency gate, v5

Artifacts: `JMP_working_paper_for_seminar_v5.tex`, `JMP_research_story_report_v5.html`, `story_v5.generated.md`, `numbers_of_record_v5.json`.

Scope note. This gate carries forward the content rules of `consistency_gate_spec_v1.md` that still apply to the S11 specifications of record, adds the rules of `canonical_notation_v5.md`, and adds the single-current-model check. `run_consistency_gate.py` is NOT re-run against v5: it is bound to the v1/v2 artifact family and to two clauses of its own specification that the current model contradicts. See `canonical_notation_v5.md` for the clause-by-clause disposition.

| # | Item | Verdict |
|---|---|---|
| 1 | SINGLE CURRENT MODEL: one specification, everywhere | **PASS** |
| 2 | Notation: forbidden symbol variants and the four-factor rule | **PASS** |
| 3 | The hours density: five bands over one residual reference | **PASS** |
| 4 | The W1 statement: all three clauses, and the accepted closed form | **PASS** |
| 5 | Pay neutrality is stated as the property established | **PASS** |
| 6 | Shapley wording: attributed to, not removed | **PASS** |
| 7 | The preliminary P/A/B scale statement matches the computed shares (DECOMP-2) | **PASS** |
| 8 | The two decomposition uncertainty summaries (Monte Carlo range, second-seed check) are never called a confidence interval | **PASS** |
| 9 | DECOMP-2 is bounded: resources, needs and composition are held fixed; no total-inequality claim | **PASS** |
| 10 | No machine labels, status tokens, private paths or slogans | **PASS** |
| 11 | Every number is bound to a registered source | **PASS** |
| 12 | The funnel ends where the estimation begins | **PASS** |
| 13 | Figures and tables are present, captioned and rendered | **PASS** |
| 14 | The report carries the explanatory apparatus | **PASS** |
| 15 | The novelty claim is conservative and fully conjoined | **PASS** |
| 16 | No causal claim; the genuinely unresolved items are retained | **PASS** |
| 17 | Retired welfare-decomposition lineage: no read by path (DECOMP-PRESEMINAR-1) | **PASS** |
| 18 | Retired ex-ante inclusive-value welfare construction: not presented as the measure (MEASURE-MAP-1R / Deputy ruling R2) | **PASS** |

## 1. SINGLE CURRENT MODEL: one specification, everywhere — PASS

- beta_c = 1: absent outside history in all three artifacts
- theta_c = 0.168: absent outside history in all three artifacts
- current model: tau = 1, theta_c = 0 exactly, beta_c estimated

## 2. Notation: forbidden symbol variants and the four-factor rule — PASS

- paper v5 (LaTeX): four-factor product stated with the canonical names
- report v5 (markdown source): four-factor product stated with the canonical names

## 3. The hours density: five bands over one residual reference — PASS

- no findings

## 4. The W1 statement: all three clauses, and the accepted closed form — PASS

- no findings

## 5. Pay neutrality is stated as the property established — PASS

- no findings

## 6. Shapley wording: attributed to, not removed — PASS

- no findings

## 7. The preliminary P/A/B scale statement matches the computed shares (DECOMP-2) — PASS

- B (earning opportunities) exceeds A (coarse geographic/temporal access) in all 4 sample x scale cells, recomputed from DECOMP-2

## 8. The two decomposition uncertainty summaries (Monte Carlo range, second-seed check) are never called a confidence interval — PASS

- registry: 12 DECOMP-2 Gini-point contributions registered, all sourced from shapley_PAB_*.csv (Monte Carlo simulation, not a parameter draw)

## 9. DECOMP-2 is bounded: resources, needs and composition are held fixed; no total-inequality claim — PASS

- paper v5 (LaTeX): ΔI-share range 1.8 to 9.9 per cent matches the registry
- report v5 (markdown source): ΔI-share range 1.8 to 9.9 per cent matches the registry

## 10. No machine labels, status tokens, private paths or slogans — PASS

- no findings

## 11. Every number is bound to a registered source — PASS

- registry: 125 entries, 64 used by the two documents, every used entry typed and sourced

## 12. The funnel ends where the estimation begins — PASS

- no findings

## 13. Figures and tables are present, captioned and rendered — PASS

- paper: 10 figures, 14 tables, 24 captions; report: 15 embedded figures, 19 tables

## 14. The report carries the explanatory apparatus — PASS

- report: 24 questions, history and notebook collapsed, worked household present, notebook generation gap disclosed

## 15. The novelty claim is conservative and fully conjoined — PASS

- no findings

## 16. No causal claim; the genuinely unresolved items are retained — PASS

- the two open econometric questions and the couples D limitation are all retained

## 17. Retired welfare-decomposition lineage: no read by path (DECOMP-PRESEMINAR-1) — PASS

- no retired-lineage path reference found in build_v5.py, v5_sections.py, common.py, numbers_of_record_v5.json (entries/gallery only), JMP_working_paper_for_seminar_v5.tex, or JMP_research_story_report_v5.html

## 18. Retired ex-ante inclusive-value welfare construction: not presented as the measure (MEASURE-MAP-1R / Deputy ruling R2) — PASS

- no undisclaimed ex-ante J/H construction found in JMP_working_paper_for_seminar_v5.tex or JMP_research_story_report_v5.html

**Overall: PASS**
