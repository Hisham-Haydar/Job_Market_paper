# Job Market Paper — Opportunity vs. Preference in Welfare Inequality

> **Working title:** *Opportunity Constraints as a Driver of Welfare Inequality: A Latent-Jobs Structural Decomposition Approach*

This repository is the working environment for an economics **job market paper (JMP)**. It is not a software project: the content is research material — PDFs, Markdown notes, LaTeX, design documents, and a small set of Python/PowerShell utility scripts that maintain a literature corpus and presentation assets. There is no application to build and no test suite.

For the authoritative project framing, see **[JMP.md](JMP.md)**.

## The paper in one paragraph

The JMP asks: *how much of observed inequality in money-metric well-being is due to unequal job opportunities rather than heterogeneous preferences?* It models labor supply as a choice among **latent job packages** (a RURO / latent-jobs discrete-choice model) rather than as free choice of hours on a common budget line. It computes a money-metric welfare measure relative to the **constrained feasible job set**, and decomposes welfare inequality into an **opportunity** component and a **preference** component using an order-independent (Shapley-style) rule. Tax-benefit microsimulation feeds the budget mapping but is an input, not the contribution. The single-country empirical setting is **France**.

The opportunity-vs-preference distinction is central throughout the materials and even drives the figure color scheme (opportunity/observed = dark blue, preference/predicted = orange).

## Central question and sub-questions

**How much of observed inequality in money-metric well-being is attributable to unequal job opportunities rather than heterogeneous preferences, once labor supply is modeled as choice among latent jobs?**

This decomposes into three questions:

1. To what extent do standard labor supply models that do not model constrained opportunities explicitly **overstate preference heterogeneity** by absorbing opportunity differences into tastes?
2. How should money-metric welfare be computed when individuals face **different feasible job sets**?
3. Under the view that opportunities are not fully the individual's responsibility, how much of welfare inequality can be attributed to **unequal opportunities**, and how much remains attributable to **preferences**?

## Directory roles

Content is organized by *function*, not by topic:

| Directory | Role |
|-----------|------|
| `Literature/` | The literature corpus: source PDFs, per-paper Markdown extractions, and the scripts that process them. Organized into six conceptual "shelves" (RURO/latent-jobs labor supply, welfare measurement for discrete choice, equivalent income / beyond-GDP, responsibility/compensation/fairness, inequality of opportunity & decomposition, microsimulation & tax-benefit policy). |
| `Design/` | Framing and concept documents (abstracts, concept notes, intro skeleton, positioning memos). Versioned by filename suffix; the highest version / `_france` variant is current. |
| `Prototype/` | Early empirical/scope memos (France setting, status, scope decisions) before they become production work. |
| `Deep_reports/` | Long-form deep research reports (gap checks, roadmap, lit reviews). |
| `Presentation_mock/` | Seminar deck: `beamer/` (LaTeX deck) and `03_assets/` (figure-generation scripts + generated PNG/CSV outputs). |
| `Theory_other_project/` | A *separate* theory project — kept distinct from the JMP literature stream. |
| `Code/` | Intended for reproducible analysis code; currently the empirical model is not yet implemented. |

## Method and empirical strategy

- **Model:** a RURO / latent-jobs discrete-choice model in which households choose among job packages (defined parsimoniously by hours and wage/earnings categories, with limited additional attributes).
- **Budget mapping:** disposable income for each job package is computed via **tax-benefit microsimulation** — an input, not the headline.
- **Estimation target:** separately, as far as identification allows, (i) preferences over consumption and leisure and (ii) the **opportunity mechanism** governing which job packages are feasible, varying with observable circumstances (region, education, demographic type).
- **Welfare:** a money-metric measure defined relative to the **constrained feasible set**, not a universal choice set.
- **Decomposition:** counterfactual equalizations of the opportunity mechanism and comparable treatments of preference heterogeneity, with inequality shares attributed via an **order-independent (Shapley-style)** rule.

## Status

The project has a locked JMP identity, a synthesized literature corpus, and a seminar-ready skeleton (concept note, decision memo, roadmap, prototype memo, mock slides/figures/tables). What remains is implementing the minimal empirical prototype, producing a first decomposition output, and robustness/identification work. **The empirical model is not yet estimated** — all figures, elasticities, and decomposition shares in `Presentation_mock/03_assets/` and the beamer deck are mock/illustrative placeholders.

## Working with this repository

All utility scripts assume Windows with PowerShell and use only the Python standard library plus `matplotlib`/`numpy` (figures) and `openpyxl` (shelves spreadsheet).

**Literature pipeline** (paths are relative to the repository root):

- Re-extract Markdown from source PDFs (requires MiKTeX `pdftotext`): `python Literature/improve_md_extractions.py`
- Concatenate per-paper extractions into `full_literaterature.md`: `python Literature/build_full_literaterature.py`
- Convert `Literature_collection.md` → compilable `.tex`: `python Literature/md_to_tex.py`
- Regenerate the six-shelf library spreadsheet: `python Literature/make_shelves.py`
- Batch-print the PDF corpus (Windows-only): `Literature/Printing.ps1`

**Presentation figures** (paths are relative to the repository root):

- `python Presentation_mock/03_assets/_make_figures.py`
- `python Presentation_mock/03_assets/_make_elasticity_figure.py`

**Presentation deck:**

- `Presentation_mock/beamer/main.tex` is a self-contained Beamer deck (compile with pdfLaTeX, Overleaf-ready).

### Conventions and gotchas

- **Versioning** is in filenames (`_v1`, `_v2`, `_v3_france`), not git history. When revising a document, prefer creating the next `_vN`; `_france`-suffixed variants supersede generic ones.
- **Hardcoded absolute paths.** Most scripts embed `C:\Users\hisham\Desktop\Job_Market_paper\...` paths and tool locations; portability means changing those constants.
- **Encoding.** Some structure files (e.g. `JMP_project_files_structure.md`) are UTF-16.
- **`full_literaterature`** — the misspelling is intentional and consistent across the script and its output; do not "fix" it.

## Key documents

- [JMP.md](JMP.md) — authoritative project framing (central question, methods, what's done, what remains)
- [CLAUDE.md](CLAUDE.md) — guidance for working in this repository
- [Design/README_JMP_workspace.md](Design/README_JMP_workspace.md) — directory roles
- [notes.md](notes.md) — research questions and direction
