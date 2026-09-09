# Consistency gate, v5

Artifacts: `JMP_working_paper_for_seminar_v5.tex`, `JMP_research_story_report_v5.html`, `story_v5.generated.md`, `numbers_of_record_v5.json`.

Scope note. This gate carries forward the content rules of `consistency_gate_spec_v1.md` that still apply to the S11 specifications of record, adds the rules of `canonical_notation_v5.md`, and adds the single-current-model check. `run_consistency_gate.py` is NOT re-run against v5: it is bound to the v1/v2 artifact family and to two clauses of its own specification that the current model contradicts. See `canonical_notation_v5.md` for the clause-by-clause disposition.

| # | Item | Verdict |
|---|---|---|
| 1 | SINGLE CURRENT MODEL: one specification, everywhere | **PASS** |
| 2 | Notation: forbidden symbol variants and the four-factor rule | **PASS** |
| 3 | The hours density: five bands over one residual reference | **PASS** |
| 4 | The W1 statement: all three clauses, and the power-mean order | **PASS** |
| 5 | Pay neutrality is stated as the property established | **PASS** |
| 6 | Shapley wording: attributed to, not removed | **PASS** |
| 7 | The six-index statement matches the computed counts | **PASS** |
| 8 | Parameter intervals and integration bands are never merged | **PASS** |
| 9 | Resources and needs: couples reported jointly, never imputed | **PASS** |
| 10 | No machine labels, status tokens, private paths or slogans | **PASS** |
| 11 | Every number is bound to a registered source | **PASS** |
| 12 | The funnel ends where the estimation begins | **PASS** |
| 13 | Figures and tables are present, captioned and rendered | **PASS** |
| 14 | The report carries the explanatory apparatus | **PASS** |
| 15 | The novelty claim is conservative and fully conjoined | **PASS** |
| 16 | No causal claim; the genuinely unresolved items are retained | **PASS** |

## 1. SINGLE CURRENT MODEL: one specification, everywhere — PASS

- beta_c = 1: absent outside history in all three artifacts
- theta_c = 0.168: absent outside history in all three artifacts
- current model: tau = 1, theta_c = 0 exactly, beta_c estimated

## 2. Notation: forbidden symbol variants and the four-factor rule — PASS

- paper v5 (LaTeX): four-factor product stated with the canonical names
- report v5 (markdown source): four-factor product stated with the canonical names

## 3. The hours density: five bands over one residual reference — PASS

- no findings

## 4. The W1 statement: all three clauses, and the power-mean order — PASS

- no findings

## 5. Pay neutrality is stated as the property established — PASS

- no findings

## 6. Shapley wording: attributed to, not removed — PASS

- no findings

## 7. The six-index statement matches the computed counts — PASS

- A_gt_B singles: 6 of six, as stated
- B_gt_A couples: 6 of six, as stated
- A_gt_D singles: 4 of six, as stated
- AB_gt_D singles: 5 of six, as stated
- D largest couples: 6 of six, as stated
- P negative singles: 5 of six, as stated

## 8. Parameter intervals and integration bands are never merged — PASS

- registry: 20 parameter-interval and 20 integration-band entries, separately typed

## 9. Resources and needs: couples reported jointly, never imputed — PASS

- registry: no couples resources/composition subdivision is registered

## 10. No machine labels, status tokens, private paths or slogans — PASS

- no findings

## 11. Every number is bound to a registered source — PASS

- registry: 447 entries, 107 used by the two documents, every used entry typed and sourced

## 12. The funnel ends where the estimation begins — PASS

- no findings

## 13. Figures and tables are present, captioned and rendered — PASS

- paper: 13 figures, 20 tables, 33 captions; report: 16 embedded figures, 20 tables

## 14. The report carries the explanatory apparatus — PASS

- report: 20 questions, history and notebook collapsed, worked household present

## 15. The novelty claim is conservative and fully conjoined — PASS

- no findings

## 16. No causal claim; the genuinely unresolved items are retained — PASS

- the two open econometric questions and the couples D limitation are all retained

**Overall: PASS**
