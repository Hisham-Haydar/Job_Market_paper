# Cameron & Miller 2015 — A Practitioner's Guide to Cluster-Robust Inference

## 0. Metadata
- **BibTeX key:** `cameron_miller_2015_cluster_robust`
- **Authors:** A. Colin Cameron; Douglas L. Miller
- **Year:** 2015
- **Outlet:** *Journal of Human Resources* 50(2): 317–372
- **DOI/URL:** https://www.jstor.org/stable/24735989
- **PDF filename:** `Cameron_Miller_2015_A_Practitioner_s_Guide_to_Cluster-Robust_Inference.pdf`
- **Tier:** T2 (inference infrastructure / methods reference)
- **JMP block(s) served:** *data-infrastructure / inference only* — specifically the cluster-robust standard errors and cluster-bootstrap machinery that the JMP's decomposition CIs and any estimation-side SEs rely on. It serves **none** of the estimation-structure, identification, welfare, decomposition, or opportunity-mechanism content; it is purely the SE/inference toolbox.

## 1. One-paragraph relevance to my JMP
This is a methods survey on obtaining valid standard errors and tests when regression errors are correlated within clusters but independent across them. It is the citation backbone for the JMP's inference layer: the welfare spec commits to a **cluster-robust bootstrap on `idorighh`** (9,657 clusters) as the inference procedure for per-component, per-measure welfare/decomposition CIs, and the project state anticipates **per-component cluster-robust CIs** for the Shapley–Shorrocks decomposition (tight for the opportunity component, wide for the preference component). Cameron–Miller justifies *why* clustered SEs are needed at all (within-cluster error correlation downward-biases default SEs), gives the CRVE sandwich formula, the pairs/wild cluster bootstrap, and the few-clusters caveats. It does **not** speak to any channel (access/ability/preference) or any welfare measure ($W^1$–$W^6$); it speaks only to how the eventual numbers should carry uncertainty.

## 2. Data, setting, and model in brief
Methods paper, not an application; illustrated with U.S. March CPS log-wage regressions (individual-level cross-section clustered on state, $G=51$; and a 1977–2012 state-year DiD panel, $G=51$, $T=36$). The core object is the linear model $y_{ig}=x_{ig}'\beta+u_{ig}$ with errors uncorrelated across the $G$ clusters but arbitrarily correlated within. The maintained method is OLS (and FGLS) followed by the cluster-robust variance estimator (CRVE) and, for few clusters, the wild cluster bootstrap. **Feature I do not have:** the paper's leading worked cases are panel/DiD with a policy regressor; my baseline is a **pooled cross-section with no panel and no DiD design**, so the serial-correlation and few-treated-groups material is context, not template.

## 5. Opportunity mechanism
N/A. The paper has no opportunity, feasibility, or job-set content. (Kept per template: it is load-bearing that this source contributes *nothing* to the opportunity layer — it is inference machinery only.)

## 6. Welfare object
N/A. No welfare object, no money-metric construction, no constrained-vs-universal set, no ex-ante/ex-post distinction. **This paper does not support, inform, or sit anywhere on the $W^1$–$W^6$ map.** Its only contact with the welfare layer is downstream and purely statistical: once a welfare/decomposition point estimate exists, the CRVE/cluster-bootstrap logic here governs its standard error. It says nothing about which welfare measure to compute or how.

## 7. Inequality / decomposition content
N/A as to *decomposition method*: the paper contains no inequality index, no Shapley–Shorrocks rule, no counterfactual construction, and **does not support the structural opportunity/ability/preference decomposition** in any way. Its relevance is confined to attaching valid uncertainty to whatever the decomposition produces. Two transferable points: (i) the CRVE for the OLS estimator is the sandwich $\hat V_{\mathrm{clu}}[\hat\beta]=(X'X)^{-1}\hat B_{\mathrm{clu}}(X'X)^{-1}$ with $\hat B_{\mathrm{clu}}=\sum_{g}X_g'\hat u_g\hat u_g'X_g$ formed from per-cluster OLS residuals; (ii) the cluster-robust variance is consistent as the **number of clusters** (not observations) grows, since the averaging that makes $\hat V[\hat\beta]$ accurate is an average over the $G$ clusters, so few-cluster settings are where it degrades. For my use this means CIs should be read as resting on the count of `idorighh` clusters (≈9,657), which is comfortably in the many-clusters regime where the bootstrap and CRVE are well-behaved.

## 8. Identification and separation of preferences from opportunities
N/A. The paper does not identify anything substantive; it does not separate tastes from constraints and offers no leverage on the JMP's preference-vs-opportunity identification problem (no panel, no instrument transportability questions are addressed here). The only "identification"-adjacent caution worth carrying: with cluster-specific dummies/fixed effects the CRVE rank is limited, so the rank of the cluster-robust variance is at most $\min(K,\,G-1)$, capping how many joint restrictions can be Wald-tested. Not binding for the JMP's single-component CIs, but relevant if any joint test across many parameters is attempted.

## 9. Key results and magnitudes
- In the CPS cross-section ($G=51$ states), clustering on state inflated the policy-variable standard error to roughly 5.5 times the default (0.0229 vs 0.0042), flipping a spuriously "highly significant" placebo regressor to insignificant.
- Magnitude of bias is captured by the Moulton-type inflation: it rises with within-cluster correlation of the regressor, within-cluster error correlation, and cluster size; with weak error correlation (≈0.032) and large groups the SE multiple still reached ~3.7 in Moulton's example.
- "Few clusters" has no sharp threshold: depending on the case it ranges from under 20 to under 50 clusters in the balanced design, and current consensus treats $G=50$ as adequate for state-year panels. **My ≈9,657 clusters are far above any few-clusters concern**, so the few-clusters corrections (wild bootstrap, $T(G-1)$/$T(v^*)$ critical values, CR2/CR3) are background, not requirements.

## 12. What I can cite this paper for
- The basic motivation: within-cluster error correlation makes default/heteroskedastic-robust SEs too small, producing over-narrow CIs and over-rejection — hence cluster-robust SEs are needed.
- The CRVE sandwich formula and the fact that it is heteroskedastic- **and** cluster-robust.
- The principle that cluster-robust inference relies on the **number of clusters** growing, and the associated few-clusters problems.
- The **pairs cluster bootstrap** and **wild cluster bootstrap** as cluster-robust resampling procedures — directly relevant since the JMP's headline inference is a cluster-robust bootstrap on `idorighh`. The wild cluster bootstrap is cited specifically as the preferred few-clusters remedy, and the pairs cluster bootstrap as the general-purpose cluster-robust resample.
- Guidance on **what to cluster over** (cluster broadly enough to capture correlated regressors and errors; the bias–variance trade-off between larger/fewer and smaller/more clusters) — supports the choice of `idorighh` as the cluster unit.
- Clustering arising from **complex survey design** (PSU-level sampling) as a reason to cluster — relevant given EU-SILC/EUROMOD survey structure.

## 13. What I should NOT cite this paper for (overclaim risks)
- **Not** for anything about welfare, equivalent income, or money-metric measurement. It is silent on welfare; it does **not** support $W^1$–$W^6$.
- **Not** for the structural opportunity/ability/preference decomposition, Shapley–Shorrocks attribution, or any inequality index. It supplies the *standard errors around* such objects, never the objects.
- **Not** as evidence on the JMP's preference-vs-opportunity **identification** (no panel/instrument transportability claims).
- **Two-way vs three-way:** the paper's "multiway clustering" is about clustering *dimensions* of the error covariance (e.g. state and year), **not** the JMP's three-channel (access/ability/preference) decomposition. Do not let the word "two-way/multiway" bleed into the channel framing — different objects entirely.
- **Occupation vs industry:** the paper uses "industry" and "occupation" only as illustrative *clustering levels* (e.g. Hersch industry/occupation example). This carries **no** implication for the JMP's `loc4` (ISCO, access) vs `lindi` (NACE, reserved) distinction; do not cite it on that distinction.
- **Random vs deterministic:** the paper's "random effects" is an error-component model for FGLS, unrelated to the JMP's deterministic opportunities. Do not conflate.
- **Theory-paper boundary:** this is a generic econometrics survey; it has no contact with the Haydar–Maniquet characterisation and must never be cited near it.
- **Few-clusters apparatus** (wild bootstrap as a *necessity*, CR2/CR3, $T(v^*)$, effective-number-of-clusters): do not present these as required for the JMP — with ≈9,657 clusters they are not. Cite them, if at all, only as established fallback methods, not as the JMP's situation.

## 16. TL;DR for retrieval
Cameron & Miller (2015) is the JMP's *inference-infrastructure* citation only: it establishes that within-cluster error correlation downward-biases default SEs, gives the CRVE sandwich and the pairs/wild **cluster bootstrap**, and supports clustering on `idorighh` and reading uncertainty off the cluster count (≈9,657, firmly many-clusters). It contributes nothing to the latent-jobs estimation structure, the equivalent-income welfare object ($W^1$–$W^6$), or the access/ability/preference decomposition — cite it strictly for clustered-data inference and cluster-bootstrap logic, never for welfare or the structural decomposition.
