# reports/INDEX.md — Job_Market_paper reports/ retirement record

> Created by QUARANTINE-2 (2026-09-14). This is the first version of this
> INDEX; it does not yet cover every file under `reports/` (see
> `check_reports_dir_lineage.py` for the fuller, machine-checked inventory
> of that directory). Following the convention set by
> `docs/normative/INDEX.md`: **this INDEX is the place supersession and
> retirement is recorded for `reports/`.** Files are not edited to carry
> status prose beyond the in-page banner described below; this table
> governs.

**Status vocabulary.** CURRENT — the version to read. RETIRED-LINEAGE, DO
NOT CIRCULATE — superseded, carries an in-page SUPERSEDED banner naming the
current surface, kept only for historical reference; never send this file
to a discussant. untracked/retired — never committed to this repo, no
longer live, preserved as a byte-identical copy in the restricted store.
VERIFIED — a binary file that cannot be machine-scanned by
`check_reports_dir_lineage.py` was manually checked against the same
lineage rules and the result is recorded here.

## Research-story report versions

| Order | Path | Status | Contents |
|---:|---|---|---|
| 1 | `JMP_research_story_report_v1.html` | RETIRED-LINEAGE, DO NOT CIRCULATE | Earliest research-story snapshot. In-page banner (`id="retired-lineage-banner"`) added 2026-09-14, naming v5 as the current surface. Known, disclosed debt (does not fail `check_reports_dir_lineage.py`): retired-path references to `headline_decomposition_v1`/`ss8_step1_states_v1`, and a four-factor P/A/B/D content-signature hit. |
| 2 | `JMP_research_story_report_v2.html` | RETIRED-LINEAGE, DO NOT CIRCULATE | Same treatment as v1: banner added, same disclosed debt (retired-path references, four-factor signature). |
| 3 | `JMP_research_story_report_v3.html` | RETIRED-LINEAGE, DO NOT CIRCULATE | Banner added. Scans clean under the current lineage gate (no retired-path or four-factor hits). |
| 4 | `JMP_research_story_report_v4.html` | RETIRED-LINEAGE, DO NOT CIRCULATE | Banner added. Known, disclosed debt: a four-factor P/A/B/D content-signature hit. |
| 5 | `JMP_research_story_report_v5.html` | **CURRENT** | The surface every v1-v4 banner points to. Not modified by QUARANTINE-2. |

Nothing was deleted or rebuilt. Each banner is a single `<div id="retired-lineage-banner">` inserted immediately after `<body>`, styled inline (no dependency on the file's own stylesheet), stating the file is superseded, naming `JMP_research_story_report_v5.html` as the current surface, and carrying the words "RETIRED-LINEAGE — DO NOT CIRCULATE". `check_reports_dir_lineage.py` looks for this same marker (`BANNER_MARKER`) and reports any lineage violation inside a marked file as `EXCL` (disclosed, does not fail the gate) rather than `FAIL`; unmarked files are unaffected and keep failing on a violation as before.

## Untracked reports/ deliverables (quarantined 2026-09-14)

| Order | Path | Status | Contents |
|---:|---|---|---|
| 1 | `JMP_reference_profiles_v1.md` | untracked/retired | Reference-profiles narrative. Never committed. Left in place in the working tree; byte-identical copy quarantined. |
| 2 | `JMP_reference_profiles_v1.csv` | untracked/retired | Reference-profiles data table, twin of the .md above. Never committed. Left in place; quarantined. |
| 3 | `JMP_reference_profiles_v1.tex` | untracked/retired | Reference-profiles LaTeX table source, twin of the above. Never committed. Left in place; quarantined. |
| 4 | `JMP_v5_review_and_modular_revision_plan_v1.md` | untracked/retired | v5 review and modular revision plan. Never committed. Left in place; quarantined. |

Quarantine copies (SHA-256 verified byte-identical to the working-tree originals immediately after copy) live at
`C:/Users/hisham/MNL/EUROMOD-STORAGE/restricted/jmp_reports_untracked_quarantine_2026-09-14/`,
with a manifest at `MANIFEST_v1.json` in that directory (per-file SHA-256 and byte count). Nothing was deleted from the working tree; these four files remain exactly where they were.

## Binary documents verified

| Order | Path | Status | Contents |
|---:|---|---|---|
| 1 | `novelty-audit-structural-well-being-inequality.docx` | VERIFIED | Literature/novelty positioning memo for the P/A/B/D Shapley-Owen-Shorrocks decomposition. Binary; `check_reports_dir_lineage.py` cannot scan it as text, so it previously showed as UNVERIFIED. Manually resolved 2026-09-14 (see verdict below). Nothing in `reports/` remains UNVERIFIED. |
| 2 | `novelty-audit-structural-well-being-inequality.md` | LIVE, no successor | The already-tracked text twin of the .docx above, unchanged by this task. |

**Verdict on the .docx (2026-09-14).** Extracted `word/document.xml` from the
`.docx` zip container, stripped XML markup (paragraph boundaries → newlines,
tags dropped, entities unescaped), and ran the plain text through the same
two checks `check_reports_dir_lineage.py` applies to the `.md` twin:
`retired_lineage_gate.scan_text()` (path-based retired-lineage check) and
`retired_lineage_gate.scan_four_factor()` (supplementary content-signature
check).

- `scan_text()`: **0 hits** — no reference to any retired artifact path
  (`headline_decomposition_v1`, `ss8_step1_states_v1`, `cw_step3_states_v1`,
  `gn_step2_nested_v1`, the `s12_*_attributions`/`*headline_shares`
  families, `s12_welfare_record_report_v1`). Identical result to the `.md`
  twin.
- `scan_four_factor()`: **one hit**, the same "co-occurring
  Access/Earning-opportunities/resources-needs rows" content signature
  already disclosed for the `.md` twin. This is expected, not new drift:
  the document's entire subject is the P/A/B/D framework itself (a
  literature-novelty ruling on it), not a read of retired welfare-pricing
  data.
- Structural check: extracted text is 5,643 words across the same section
  structure (Bottom line → Executive rulings A-E → paper-by-paper rulings →
  adjacent literatures → numbered sources) as the 5,662-word `.md` twin —
  consistent with the `.docx` being the original source the `.md` was
  transcribed from, not a divergent version.

**Disposition:** same status as its `.md` twin — `LIVE, no successor`,
carrying the one disclosed four-factor content-signature note. Not a
retired-lineage violation. `check_reports_dir_lineage.py` now reports this
file as `VERIFIED` with this verdict instead of `UNVERIFIED`.
