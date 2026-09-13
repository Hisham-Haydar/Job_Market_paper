# Current results gallery

The gallery is generated and self-contained. Displayed non-welfare values are
copied into the `gallery` block of `numbers_of_record_v5.json`; current welfare
tables are read directly from the S12 CSV records. The decomposition section
reports the preliminary three-factor P/A/B decomposition (DECOMP-2) and is
read directly from the CSV/JSON records under
`../../../MNL_decomp/outputs/welfare/preseminar_pab_v1/` (a worktree of MNL on
branch `welfare/preseminar-pab`). It deliberately does not read
`headline_decomposition_v1.csv` or any `ss8*`/`cw_step3*`/`gn_step2*` state
file -- those remain excluded pending a separate lineage verdict.

Rebuild after reviewed source changes:

```powershell
..\..\..\MNL\.venv\Scripts\python.exe build.py --refresh-registry
..\..\..\MNL\.venv\Scripts\python.exe verify.py
```

A routine rebuild that must not change the registry omits
`--refresh-registry`.
