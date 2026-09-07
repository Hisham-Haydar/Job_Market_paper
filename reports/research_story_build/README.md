# Generator for `JMP_research_story_report_v1.html`

The report is **generated, not hand-written**. No numeral is typed into the prose:
every one is emitted as a placeholder bound to a key and filled in the browser from
one of two embedded JSON blocks.

## Rebuild

```
python build.py       # writes ../JMP_research_story_report_v1.html
python verify.py      # gate: both self-checks must PASS
node   jscheck.js     # gate: page JS parses; every bound span renders
node   render_text.js rendered.txt   # proof-reading dump with values substituted
```

`build.py` reads:

| input | path | used for |
|---|---|---|
| numbers of record | `../numbers_of_record_v1.json` | every scalar result |
| coefficient table | `MNL/experiments/JMP_SEMINAR_SPRINT/figures/fig08_coefficients_by_block.csv` | the 41-coordinate table |
| external validation | `MNL/experiments/JMP_SEMINAR_SPRINT/tables/external_hours_validation_v1.csv` | the hours-band cells |
| figures | `MNL/experiments/JMP_SEMINAR_SPRINT/figures/*.png` | 31 embedded, downscaled to 1200px |

Chronology quantities and structural definitions are transcribed in `common.py`
(`aux["chron"]`, `aux["defs"]`) from `MNL/experiments/JMP_PS1/decision_note.md`
sections 2 and 31; that is the only group not read from a machine-readable
artefact, and it is flagged as such in the report's own register.

## The two data blocks

- `NOR-DATA` — `numbers_of_record_v1.json`, embedded **verbatim**.
- `AUX-DATA` — per-row artefacts the numbers file does not carry as scalars,
  read from their own frozen files at build time.

Both render through the same mechanism, with the same tooltips and the same
register in section 23.

## The self-check

Section 23 audits the document in the browser on every load. `verify.py`
replicates that audit in Python so the build can be gated. Every numeral in the
body is classified as one of:

- **bound** — rendered from a key (must resolve; Check A)
- **literal** — a declared non-result numeral, carrying its reason
- **structural** — inside a code span, heading, column label or figure caption
- **cross-reference** — "section 12", "blocks 2 to 5", a "13–18" range
- **unclassified** — must be zero (Check B)

## Editing

Prose lives in `sec_a.py` (§1–6), `sec_b.py` (§7–12), `sec_c.py` (§13–18),
`sec_d.py` (§19–23). Emit numbers with `n("key", fmt, digits)` for the numbers
file and `a("group.path", fmt, digits)` for the auxiliary block; use `lit(text,
why)` for a declared non-result numeral. Spell small non-result integers as
words. Styling and the render/audit engine are in `shell.py`.
