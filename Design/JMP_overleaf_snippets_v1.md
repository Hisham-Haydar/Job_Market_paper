**Filename: `main.tex`**

```tex
\documentclass[12pt,a4paper]{article}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[english]{babel}

\usepackage{amsmath,amssymb,amsthm}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{float}
\usepackage{caption}
\usepackage{subcaption}
\usepackage{setspace}
\usepackage{geometry}
\usepackage{natbib}
\usepackage{hyperref}
\usepackage{array}
\usepackage{longtable}

\geometry{margin=1in}
\setstretch{1.1}
\hypersetup{
    colorlinks=true,
    linkcolor=black,
    citecolor=black,
    urlcolor=blue
}

\title{}
\author{}
\date{}

\begin{document}

\input{sections/00_title}
\input{sections/01_abstract}
\input{sections/02_extended_abstract}
\input{sections/03_france_prototype}
\input{sections/04_table_stub}
\input{sections/05_figure_stub}

\bibliographystyle{apalike}
\bibliography{refs}

\end{document}
```

**Filename: `sections/00_title.tex`**

```tex
\begin{titlepage}
\centering

\vspace*{2cm}

{\Large \textbf{Opportunity Constraints as a Driver of Welfare Inequality:}}\\[0.3cm]
{\Large \textbf{A Latent-Jobs Structural Decomposition Approach}}\\[1.5cm]

{\large Hisham Haydar}\\[0.2cm]
{\normalsize University of Luxembourg and LISER}\\[2cm]

{\large Short Paper Note}\\[0.4cm]
{\normalsize Job Market Paper Project}\\[2cm]

\begin{minipage}{0.88\textwidth}
\small
\noindent This note consolidates the current abstract, extended abstract, and baseline empirical prototype for the France application of the job market paper. It is a short project note rather than a full paper draft. The empirical baseline is France 2016 couples in a RURO / latent-jobs structural labor-supply framework, with household AEI-style welfare and a two-factor Shapley-Shorrocks decomposition of the household welfare Gini into opportunity and preference components. The note is deliberately provisional and does not present the France decomposition as final.
\end{minipage}

\vfill

{\normalsize \today}

\end{titlepage}
```

**Filename: `sections/01_abstract.tex`**

```tex
\section*{Abstract}

This paper asks whether standard structural labor-supply models overstate preference heterogeneity because they leave unequal job opportunities implicit, and what this implies for the decomposition of welfare inequality. The empirical application is a France-based RURO model estimated on SRCV / EUROMOD-input microdata, in which couples choose among latent job packages rather than from a common unconstrained hours set. The paper's contribution is to build a single empirical framework that treats opportunities consistently in estimation, welfare evaluation, and decomposition. It estimates preferences jointly with an opportunity mechanism for discrete wage-hours opportunities, uses tax-benefit microsimulation only to map those opportunities into disposable income, constructs household money-metric welfare conditional on constrained feasible sets, and then decomposes welfare inequality using counterfactual equalizations and a Shapley-Shorrocks rule.

The paper is therefore not another welfare-ranking exercise. Its central object is the share of welfare inequality attributable to unequal opportunities, relative to preference heterogeneity, under a responsibility-sensitive interpretation in which opportunities are compensation-relevant circumstances. Identification is demanding in this class of models, so the contribution is disciplined measurement in a concrete France implementation rather than a claim of already-settled magnitudes \citep{...}.
```

**Filename: `sections/02_extended_abstract.tex`**

```tex
\section*{Extended Abstract}

\subsection*{Motivation}

Structural labor-supply models are commonly used to estimate preferences and evaluate policy, but they usually treat labor supply as a choice from a common hours menu under a household-specific budget set. In many labor markets, however, individuals do not choose hours directly. They choose among jobs, and the set of feasible job opportunities differs across workers and households. Once this is recognized, observed labor-market outcomes become normatively ambiguous: the same hours--income bundle may reflect unconstrained choice for one household and a constrained second-best for another. The central concern of this project is that, if opportunity heterogeneity is left implicit, structural models will tend to absorb it into preference heterogeneity. That distorts both the positive interpretation of labor-supply behavior and the welfare analysis built on top of it. The paper is therefore motivated by the need to treat opportunities as a first-class empirical object and to quantify their contribution to welfare inequality.

\subsection*{Core Question}

The paper asks how much observed inequality in money-metric well-being is attributable to unequal job opportunities rather than to heterogeneous preferences, once labor supply is modeled as discrete choice among latent job packages and welfare is evaluated conditional on constrained feasible sets. Put differently, the empirical question is whether standard structural labor-supply models overstate preference heterogeneity because unequal access to jobs is left implicit, and whether this matters quantitatively for the decomposition of welfare inequality. The paper is not organized around country ranking or reform incidence. Its central object is the mechanism generating welfare inequality.

\subsection*{Literature Gap}

The literature gap is narrow and specific. The first relevant literature is constrained structural labor supply, including RURO and related latent-jobs approaches, which shows that jobs should be modeled as packages and that opportunity densities matter for behavior \citep{...}. The second is empirical welfare analysis under heterogeneous preferences, which shows that money-metric welfare comparisons are sensitive to the treatment of taste heterogeneity \citep{...}. The third is the inequality-of-opportunity and responsibility-sensitive literature, which supplies the normative language of circumstances and compensation \citep{...}. The gap is not the absence of these ingredients separately. It is the absence of a single empirical pipeline that estimates opportunities, carries them into welfare measurement, and then decomposes welfare inequality in an order-independent way.

\subsection*{Mechanism: Opportunities Versus Preferences}

The empirical mechanism separates preferences from opportunities. Preferences govern how a household ranks consumption--leisure bundles conditional on available jobs. Opportunities govern which job packages are feasible and how their distribution varies across observable circumstances. In reduced form, utility from a sampled alternative depends on disposable income and leisure, while an explicit opportunity term shifts the attractiveness of that alternative through its availability. If the opportunity term is omitted, the model is forced to reinterpret constrained outcomes as tastes. That is the central identification and interpretation problem. The project therefore treats opportunities consistently across the behavioral and welfare layers. Its normative stance is limited but explicit: unequal opportunities are interpreted as compensation-relevant circumstances, while the paper remains an empirical structural project rather than an extension of the separate theory paper.

\subsection*{France Empirical Setting}

The empirical application is a France 2016 structural labor-supply model based on SRCV / EUROMOD-input microdata. The implemented baseline is a household couples sample, not a single-person prototype, and the first decomposition is defined over household welfare levels. In the current France pipeline, the sample is filtered to opposite-sex couples with head and partner aged 16--65, outside full-time education, excluding self-employment and observations with abnormal employee hours or wages; households with additional labour-market-eligible adults are also excluded. This is the most defensible first prototype because it is aligned with the actual France implementation rather than with older fallback designs. France 2021 is available for later robustness, but the baseline writing anchor is France 2016.

\subsection*{Empirical Strategy}

The empirical strategy is a France-based RURO application with sampled latent alternatives. Each spouse faces market alternatives defined at the basic job level as wage-vigintile $\times$ 4-hour-interval packages, plus a non-work option. At the household level, the relevant alternative is therefore a joint bundle of head and partner job packages. Disposable income for each sampled alternative is computed through EUROMOD under French tax-benefit rules. Microsimulation is thus a supporting input to the budget mapping, not the behavioral contribution of the paper. Preferences are modeled using the implemented Box-Cox couples specification, with a common consumption term, spouse-specific leisure terms, and a leisure--leisure interaction term. The opportunity mechanism is modeled separately and shifts the distribution of feasible job packages across observable circumstances. Estimation proceeds by maximum likelihood in the implemented France pipeline, with sampled alternatives and the associated correction for sampled choice sets \citep{...}.

\subsection*{Welfare Object}

The welfare object is a household-level AEI-style money-metric measure implied by the estimated couples model and evaluated relative to a joint non-work reference state. This matters for two reasons. First, it ensures that welfare comparisons are conditional on the constrained feasible set rather than on a universal choice set. Second, it preserves a necessary distinction between estimated behavioral utility and the welfare metric used for interpersonal comparison. In the first version of the paper, the AEI-style measure is the baseline object, while the alternative reference-preference measure remains a robustness exercise. This keeps the welfare layer empirically grounded and distinct from the more abstract axiomatic issues pursued elsewhere.

\subsection*{Decomposition Strategy}

Decomposition is the central empirical object of the paper. The baseline inequality index is the Gini coefficient of household welfare. The first-pass counterfactuals are deliberately narrow. Opportunity heterogeneity is equalized by replacing spouse-specific opportunity distributions across region $\times$ education cells with a pooled reference opportunity structure. Preference heterogeneity is neutralized by replacing household-specific taste shifters with a pooled reference specification. These two counterfactuals are then combined in a two-factor Shapley-Shorrocks decomposition, which attributes the baseline welfare Gini to an opportunity component and a preference component in an order-independent way \citep{...}. This is a stronger object than a welfare ranking. A ranking speaks to levels; the decomposition identifies the mechanisms driving inequality in those levels.

\subsection*{Expected Contribution}

The contribution is specific. The paper contributes to constrained structural labor supply by estimating job opportunities rather than treating all residual heterogeneity as tastes. It contributes to empirical welfare analysis by constructing a money-metric welfare object that is explicitly conditional on constrained opportunities. It contributes to inequality analysis by making the decomposition of welfare inequality, rather than a welfare ranking or a reform table, the primary scientific output. The core novelty is therefore a single empirical pipeline in which opportunities are modeled in estimation, carried into welfare evaluation, and then decomposed.

\subsection*{Current Scope and Caution}

The main challenge is identification under a structurally estimated couples model. The current France implementation still faces normalization and convergence problems, sample-construction and wage-treatment issues, and unresolved details in the welfare and opportunity layers. These constraints do not make the project infeasible, but they imply that the first version of the paper must remain narrow. It should not claim that the France decomposition result is already final. The near-term objective is a disciplined baseline France 2016 couples prototype with one welfare object, one inequality index, one two-factor decomposition rule, one main table, and one main figure.
```

**Filename: `sections/03_france_prototype.tex`**

```tex
\section*{Baseline France Prototype}

The baseline empirical prototype is a France 2016 structural labor-supply application using SRCV / EUROMOD-input microdata and the implemented couples sample. The unit of analysis is the household. This follows the actual France pipeline and keeps the writing aligned with the implemented joint couples model rather than with older simplified prototypes.

Labor supply is modeled in a RURO / latent-jobs framework in which each spouse chooses among sampled latent job packages rather than from a common unconstrained hours grid. The minimal job representation is the basic sampled \emph{job} object already used in the France hierarchy: wage-vigintile $\times$ 4-hour-interval packages, plus non-work. At the household level, an alternative is therefore a joint package for head and partner. Disposable income for each sampled alternative is computed under French tax-benefit rules through EUROMOD. Microsimulation is used only to map job packages into disposable income; it is not the core contribution of the note.

The preference block follows the implemented Box-Cox couples specification. The baseline preference structure uses a common consumption term, spouse-specific leisure terms, and a leisure--leisure interaction term, with parsimonious observed heterogeneity in leisure tastes through demographic shifters. The opportunity block is modeled separately and governs the distribution of feasible job packages across observable circumstances. For the first prototype, the headline circumstance partition for opportunity heterogeneity is spouse-specific region $\times$ education.

The welfare object is household AEI-style money-metric welfare evaluated relative to a joint non-work reference state. The baseline inequality index is the household welfare Gini. The baseline decomposition is a two-factor Shapley-Shorrocks decomposition of the household welfare Gini into an opportunity component and a preference component. Opportunity heterogeneity is equalized by replacing spouse-specific opportunity distributions across region $\times$ education cells with a pooled reference opportunity structure. Preference heterogeneity is neutralized by replacing household-specific taste shifters with a pooled reference specification. The order-independent Shapley-Shorrocks rule then assigns the resulting change in the welfare Gini across the two factors.

This France prototype is deliberately narrow. It is intended to establish a feasible first empirical decomposition, not to present a completed and fully stabilized final result. Richer job hierarchies, alternative welfare measures, additional circumstance partitions, and broader robustness exercises are postponed to later stages once the France 2016 couples baseline is fully stabilized.
```

**Filename: `sections/04_table_stub.tex`**

```tex
\section*{Planned Main Table}

\begin{table}[H]
\centering
\caption{France 2016 couples: planned decomposition of household welfare inequality}
\label{tab:france_decomp_stub}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{p{8.5cm}c}
\toprule
Outcome / component & Value \\
\midrule
Baseline household welfare Gini & [to be filled] \\
Household welfare Gini after opportunity equalization & [to be filled] \\
Household welfare Gini after preference neutralization & [to be filled] \\
Household welfare Gini after both equalizations & [to be filled] \\
\addlinespace
Shapley share attributed to opportunity heterogeneity & [to be filled] \\
Shapley share attributed to preference heterogeneity & [to be filled] \\
\bottomrule
\end{tabular}

\vspace{0.5em}

\begin{minipage}{0.92\textwidth}
\footnotesize
\textit{Notes:} This table is a structural prototype for the France 2016 couples sample. Welfare is measured at the household level using an AEI-style money-metric welfare object evaluated relative to a joint non-work reference state. The inequality statistic is the household welfare Gini. Opportunity heterogeneity is equalized using spouse-specific region $\times$ education opportunity structures. Preference heterogeneity is neutralized using a pooled reference preference specification. Component shares are assigned using a two-factor Shapley-Shorrocks decomposition. Entries are placeholders at this stage and should not be interpreted as final empirical results.
\end{minipage}
\end{table}
```

**Filename: `sections/05_figure_stub.tex`**

```tex
\section*{Planned Main Figure}

\begin{figure}[H]
\centering
\fbox{
    \begin{minipage}[c][6cm][c]{0.82\textwidth}
    \centering
    \vspace{0.3cm}
    \textbf{Figure placeholder}\\[0.4cm]
    Stacked bar chart of the Shapley decomposition of the\\
    France 2016 couples household welfare Gini\\[0.4cm]
    \emph{Opportunity share} + \emph{Preference share}
    \vspace{0.3cm}
    \end{minipage}
}
\caption{Planned stacked-bar decomposition of household welfare inequality}
\label{fig:france_shapley_stub}

\begin{minipage}{0.92\textwidth}
\footnotesize
\textit{Notes:} The figure should display a single stacked bar for the France 2016 couples baseline. The full height of the bar represents the baseline household welfare Gini. The bar is partitioned into two components: the Shapley share attributed to opportunity heterogeneity and the Shapley share attributed to preference heterogeneity. The figure is intended to visualize the mechanism behind welfare inequality rather than to present a final stabilized quantitative result. The displayed shares should therefore be interpreted as provisional until the France estimation and welfare layers are fully locked.
\end{minipage}
\end{figure}
```

**Filename: `refs.bib`**

```bibtex
% Placeholder bibliography file for the short paper note.
% Replace placeholder keys in the LaTeX source with real entries once finalized.

% Example format only:
% @article{AabergeColombinoStrom1999,
%   author  = {Aaberge, Rolf and Colombino, Ugo and Str{\o}m, Steinar},
%   title   = {Labour Supply in Italy: An Empirical Analysis of Joint Household Decisions, with Taxes and Quantity Constraints},
%   journal = {Journal of Applied Econometrics},
%   year    = {1999},
%   volume  = {14},
%   number  = {4},
%   pages   = {403--422}
% }
```
