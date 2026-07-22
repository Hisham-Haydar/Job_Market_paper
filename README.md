# Job Market Paper — Access, Ability, and Preference in Welfare Inequality

> **Working title:** *Unequal Job Opportunities as a Driver of Welfare Inequality: A Latent-Jobs Structural Decomposition Approach*

This repository is the **research/writing** environment for an economics **job market paper (JMP)**. It is not a software project: the content is research material — PDFs, Markdown notes, LaTeX, design documents, and a small set of Python/PowerShell utility scripts that maintain a literature corpus and presentation assets. There is no application to build and no test suite here. **The estimation code, the certified structural estimate, and its provenance live in the separate `MNL` and `MNL/dclaborsupply-monorepo` repositories, not in this repository.**

For the authoritative project framing and current state, see **[JMP_project_state_v1.md](JMP_project_state_v1.md)**; the welfare design is fixed in **[JMP_welfare_spec_v5.md](JMP_welfare_spec_v5.md)** and the canonical literature framing in **[docs/JMP_literature_review_skeleton_v1.md](docs/JMP_literature_review_skeleton_v1.md)** (root copy: `JMP_literature_review_skeleton_v1.md`).

## The paper in one paragraph

The JMP asks: *how much of observed inequality in money-metric well-being is due to unequal job **access** and differences in **ability**, rather than heterogeneous **preferences**?* It models labor supply as a choice among **latent job packages** (a RURO / latent-jobs discrete-choice model) rather than as free choice of hours on a common budget line. It computes a money-metric welfare measure relative to the **constrained feasible job set**, and decomposes welfare inequality into **access**, **ability**, and **preference** components using an order-independent (Shapley-style) rule. Tax-benefit microsimulation feeds the budget mapping but is an input, not the contribution. The single-country empirical setting is **France** (EUROMOD, pooled 2015–2017).

The three-way **access / ability / preference** cut is central throughout the materials (wage technology = **ability**; market/job/hours/region/occupation availability = **access**; the obsolete two-way "opportunity vs preference" split is retired). The figure color scheme reflects the observed-vs-predicted contrast (observed = dark blue, predicted = orange).

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
| `Theory_other_project/` | A *separate* theory project (the axiomatic Haydar–Maniquet theory paper) — kept distinct from this empirical JMP. |
| `Code/` | Reserved for writing-side analysis/figure code. The **structural estimation code and the certified estimate do not live here** — they are in the `MNL` and `MNL/dclaborsupply-monorepo` repositories. |

## Method and empirical strategy

- **Model:** a RURO / latent-jobs discrete-choice model in which households choose among job packages (defined parsimoniously by hours and wage/earnings categories, with limited additional attributes).
- **Budget mapping:** disposable income for each job package is computed via **tax-benefit microsimulation** — an input, not the headline.
- **Estimation target:** separately, as far as identification allows, (i) preferences over consumption and leisure and (ii) the opportunity mechanism governing which job packages are feasible — itself split into an **ability** channel (the wage/Mincer technology) and an **access** channel (market/participation, hours, region/urbanisation, and occupation availability), varying with observable circumstances.
- **Welfare:** a money-metric measure defined relative to the **constrained feasible set**, not a universal choice set.
- **Decomposition:** counterfactual equalizations of the access and ability channels and comparable treatments of preference heterogeneity, with inequality shares attributed via an **order-independent (Shapley-style)** rule.

## Status

The structural model **is estimated and certified**: the formal active baseline is the **47-parameter pooled specification `joint_pooled_v1_bll0_tlmpin`** (France 2015–2017 pooled; JAX; singles 101 / couples 901 alternatives; negLL 238504.6360973987; synthetic-recovery certified; real-data Hessian positive definite; clustered inference on `idorighh`). That estimate, its theta, and its provenance live in the `MNL` and `MNL/dclaborsupply-monorepo` repositories.

The **welfare design is fixed** (`JMP_welfare_spec_v5.md`, the W¹–W⁶ family), but **headline welfare and decomposition results are not yet certified** — the welfare computational core is validated on the W³ reference only, and the FR-2016 singles P2a work and any welfare numbers built on it are **provisional** pending a production rebuild with strict diagnostics. On the writing side, a synthesized literature corpus and a seminar-ready skeleton exist. Any figures, elasticities, or decomposition shares in `Presentation_mock/03_assets/` and the beamer deck remain **mock/illustrative placeholders** and are not the certified estimate.

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

- [JMP_project_state_v1.md](JMP_project_state_v1.md) — **authoritative** current project state (question, methods, certified baseline, welfare, next steps)
- [JMP_welfare_spec_v5.md](JMP_welfare_spec_v5.md) — canonical welfare design (W¹–W⁶ family; design fixed, results not yet certified)
- [docs/JMP_literature_review_skeleton_v1.md](docs/JMP_literature_review_skeleton_v1.md) — canonical literature-review framing (access/ability/preference)
- [JMP.md](JMP.md) — earlier narrative framing (retained as background; superseded by `JMP_project_state_v1.md`)
- [CLAUDE.md](CLAUDE.md) — guidance for working in this repository
- [Design/README_JMP_workspace.md](Design/README_JMP_workspace.md) — directory roles
- [notes.md](notes.md) — early research questions and direction (historical)
