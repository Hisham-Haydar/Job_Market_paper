# V16 complete release gate summary

Overall: **PASS**

| Gate | Status | Evidence |
|---|---:|---|
| report build | **PASS** | [WARNING] Deprecated: --mathjax. Use --math-method=mathjax[:URL] instead. |
| correction scope and negative control | **PASS** | V16 CORRECTION SCOPE PASS: {'markdown_equals_v15_plus_corrections': True, 'registry_entries_unchanged': True, 'embedded_images_identical': True, 'corrections_rendered': True}; negative control observed FAIL |
| figure captions use the current access definition, negative control | **PASS** | V16 FIGURE CAPTIONS PASS: report 34 captions (8 naming access), gallery 45 (8); negative control observed FAIL; theory caption alone PASS, with planted violation FAIL |
| rendered-text language and negative control | **PASS** | RENDERED-LANGUAGE AUDIT PASS: 0 outside-appendix hits; negative control observed FAIL |
| Stage A ex-ante status and negative control | **PASS** | V16 STAGE A STATUS PASS: report 7 stale / 0 unlabelled; gallery 3 / 0; negative control observed FAIL |
| body/appendix section-title uniqueness and negative control | **PASS** | V16 SECTION TITLES PASS: report shared [], gallery shared []; negative control observed FAIL |
| reader structure and economic derivation | **PASS** | V16 READER GATES PASS: 61 checks, 0 failures |
| number-to-source | **PASS** | V16 NUMBER-TO-SOURCE PASS: 41 checks, 0 failures |
| offline HTML render | **PASS** | temporary screenshots captured for visual inspection |
| cross-surface synchronisation | **PASS** | PASS: notebook_executed |
| deck verification (R11, unchanged) | **PASS** | PASS: rendered_comparison |
| executed notebook verification (V11, unchanged) | **PASS** | PASS: record_certified |
| Python source compilation | **PASS** | completed |
| V9 to V15 byte-preservation | **PASS** | completed |
