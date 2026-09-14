# Report v6 release gates

**FAIL**

Report: `reports/JMP_research_story_report_v6.html`

SHA-256: `a5cb0e23d2b0cc28c88bfbbd85ebad287b6dc37a78980ab5307207df4b51f72c`

| Gate | Result |
|---|---|
| `reports/run_v5_gate.py` | PASS |
| `reports/run_v5_gate_negative_control.py` | PASS |
| `reports/check_v5_numbers_against_source.py` | PASS |
| `reports/check_v5_pdf_layout.py` | PASS |
| `reports/check_v6_render.py` | PASS |
| `beamer/verify_deck_r6.py` | PASS |
| `reports/results_gallery_build/verify.py` | PASS |
| `reports/check_reports_dir_lineage.py` | FAIL |
| `reports/run_final_claim_wording_gate.py` | PASS |
| `reports/check_report_v6_framing.py` | PASS |
| `reports/run_final_claim_evidence_gate.py` | PASS |

The number-to-source gate reads all six current surfaces, including the untouched gallery and canonical notebook. The historical v1/v2 consistency runner is superseded for the current model by the maintained 18-item runner, as documented in canonical_notation_v5.md; its incompatible beta_c=1 and historical hours-density clauses are not reintroduced.
