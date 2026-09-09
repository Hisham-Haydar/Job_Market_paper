# Current results gallery

The gallery is generated and self-contained. Displayed non-welfare values are
copied into the `gallery` block of `numbers_of_record_v5.json`; current welfare
and decomposition tables are read directly from the S12 CSV records.

Rebuild after reviewed source changes:

```powershell
..\..\..\MNL\.venv\Scripts\python.exe build.py --refresh-registry
..\..\..\MNL\.venv\Scripts\python.exe verify.py
```

A routine rebuild that must not change the registry omits
`--refresh-registry`.
