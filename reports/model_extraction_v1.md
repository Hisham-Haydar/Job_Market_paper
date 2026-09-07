# Model extraction v1

## Scope and evidentiary rule

This note was prepared after first reading sections 6.5, 8, 9, 10, 11, 12, 13, 16 and 17 of `reports/JMP_research_story_report_review_v1.md`. Every model statement below is then re-extracted from executed code or a frozen executable specification/artifact. Names are used only as labels after the code establishes their role. Claims not established that way are marked **UNRESOLVED**.

The final singles object is S8 on 1,555 households and 101 rows per household (one observed row plus 100 stochastic rows); the frozen declaration identifies the executable base and extensions and records the retained estimates and inference dimensions (`../MNL/experiments/JMP_SEMINAR_SPRINT/export/gpu_research_bundle_v1/spec/estimation_spec_S8_corrected_floor5_v1.yaml:3-20`, `../MNL/experiments/JMP_SEMINAR_SPRINT/export/gpu_research_bundle_v1/spec/estimation_spec_S8_corrected_floor5_v1.yaml:45-56`, `../MNL/experiments/JMP_SEMINAR_SPRINT/export/gpu_research_bundle_v1/spec/estimation_spec_S8_corrected_floor5_v1.yaml:99-108`). The clean-couples object has 2,275 households and the same 101-row geometry (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/couples_clean_baseline/r240_step0_gates_v1.json:147-160`).

## Notation and units

- (i): household; (s\in\{m,f\}): male/female decision maker; (j): alternative.
- (e\in\{0,1\}): non-employment/employment; under employment (k\in\{1,2,3,4\}), (h\in[5,70]) weekly hours, and (w\in(0,\infty)) hourly wage.
- Money is euros per month in the 2016 frame; the proposal and structural wage are euros per hour. Hours are hours per week. The executed earnings conversion is \(52/12\) weeks per month (`../MNL/scripts/enhanced/enh_RURO_euromod.py:79-82`, `../MNL/scripts/enhanced/enh_RURO_euromod.py:662-678`).
- \(X_i\) denotes raw potential-experience years; \(x_i=X_i/20\) is the dimensionless structural wage regressor and \(x_i^2\) is recomputed after scaling (`../MNL/scripts/bpool/harmonise_bpool_engine_ready.py:64-81`). Proposal wage equations below use raw \(X_i\), as their executed calibration requires.
- \(BC(x;\theta)=(x^\theta-1)/\theta\) for \(|\theta|\ge10^{-8}\), and \(BC(x;0)=\log x\) (`../MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py:64-70`).
- (\nu), the structural mixed base measure, is counting mass on the single (e=0) point plus counting measure on (k=1,\ldots,4), Lebesgue measure (dh) on ([5,70]), and Lebesgue measure (dw) on ((0,\infty)) when (e=1) (`../MNL/scripts/welfare/m08_normalisation.py:21-32`).

## 1. Utility

### Singles

For sex group (g\in\{sm,sf\}), the executed deterministic utility is

\[
u_{ig}(j)=\omega_{ig}\,BC\!\left(\ell_i(j);\theta_{\ell g}\right)
             +BC\!\left(c_i(j);\theta_c\right),
\]

\[
\omega_{ig}=\beta_{\ell0,g}+\beta_{\ell a,g}a_i
             +\beta_{\ell a^2,g}a_i^2
             +\mathbf 1\{g=sf\}\beta_{\ell n,g}n_i.
\]

The engine constructs the coefficient and the two Box--Cox terms exactly this way; the child term is suppressed for males by the specification's gender-specific guard (`../MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py:232-241`; `../MNL/scripts/bpool/specs/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml:61-87`). Consumption is the numeraire: (\beta_c=1), not estimated (`../MNL/experiments/JMP_SEMINAR_SPRINT/export/gpu_research_bundle_v1/spec/estimation_spec_S8_corrected_floor5_v1.yaml:34-43`).

The arguments supplied to utility are dimensionless:

\[
c_i(j)=\frac{C_i(j)}{\lambda_c},\qquad
\ell_i(j)=\frac{\max\{80-h_i(j),1\}}{\lambda_\ell}.
\]

Here (C_i(j)) is post-take-up disposable consumption in euros/month, the time endowment is 80 hours/week, and the lower positive-domain floor is 1 hour. On the final singles frame,

\[
\lambda_c=1911.108057855561\ \text{euros/month},\qquad
\lambda_\ell=10\ \text{hours/week}.
\]

The transformer computes the floor, both normalizations and their logs (`../MNL/experiments/JMP_PS1/runs/ps1r222_floor5/run_ps1r222_s5a_stem.py:147-183`); the constants are fixed in the engine-ready module and frozen metadata (`../MNL/dclaborsupply-monorepo/packages/dclaborsupply_app/src/dclaborsupply_app/de/engine_ready.py:43-44`; `../MNL/outputs/p2a_singles2016/region_live_margqh_floor5_v1/fr_p2a_singles2016_regionlive_margqh_floor5_v1__mnlmeta.json:7-12`). Thus (\lambda_c) is the mean of floored (C) over all final rows, while (\lambda_\ell) is the minimum positive chosen leisure; that is the executed normalization rule (`../MNL/dclaborsupply-monorepo/packages/dclaborsupply_app/src/dclaborsupply_app/de/engine_ready.py:197-216`).

Age enters as

\[
a_i=\frac{A_i-\bar A}{10},\qquad a_i^2=\left(\frac{A_i-\bar A}{10}\right)^2,
\]

where (A_i) is the decider's age in years and (\bar A) is the mean decider age in the assembled sample. The feature builder computes the decider-mean centering (`../MNL/scripts/p2a/run_p2a_regionlive_rebuild.py:605-608`), and final singles assembly recomputes the divided-by-ten term and its square rather than merely trusting an inherited column (`../MNL/scripts/p2a/run_p2a_regionlive_rebuild.py:776-783`); the general harmonizer independently enforces the division by ten and recomputes the square (`../MNL/scripts/bpool/harmonise_bpool_engine_ready.py:64-81`).

For couples, the wide builder carries the centered age term separately for each decider into `age_norm_m` and `age_norm_f` (`../MNL/experiments/JMP_PS1/runs/ps1h_couples_p1/build_couples_phase1.py:300-324`), and the same harmonizer applies the division by ten and square recomputation to both spouse columns (`../MNL/scripts/bpool/harmonise_bpool_engine_ready.py:73-81`).

The model child count is

\[
n_i=\sum_{p\in\mathcal H_i}\mathbf 1\{A_p<20\},
\]

the number of **all** household members younger than 20, with no parent-link requirement (cutoff: `../MNL/scripts/p2a/run_p2a_regionlive_rebuild.py:185-186`; singles count: `../MNL/scripts/p2a/run_p2a_regionlive_rebuild.py:781-783`; clean couples: `../MNL/experiments/JMP_PS1/runs/ps1h_couples_p1/build_couples_phase1.py:721-725`).

### Couples

The clean-couples deterministic utility is additive across spouses and has no leisure interaction:

\[
u_i(j)=\omega_{im}BC(\ell_{im}(j);\theta_{\ell m})
      +\omega_{if}BC(\ell_{if}(j);\theta_{\ell f})
      +\log c_i(j).
\]

The engine's general couples expression contains a possible cross term, but the clean specification omits it; the executed branch therefore sets it to zero (`../MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py:438-454`; `../MNL/experiments/JMP_SEMINAR_SPRINT/configs/estimation_spec_couples_clean_r240_v1.yaml:1-10`). The log restriction is exact because (\theta_c=0) and (\beta_c=1) (`../MNL/experiments/JMP_SEMINAR_SPRINT/configs/estimation_spec_couples_clean_r240_v1.yaml:39-49`). Consumption is the tax-unit sum over all members. The frozen clean frame has

\[
\lambda_c=3821.448012098882\ \text{euros/month},\qquad
\lambda_{\ell m}=\lambda_{\ell f}=10\ \text{hours/week},
\]

and records the all-member aggregation (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/couples_clean_baseline/r240_step0_gates_v1.json:147-160`; aggregation code: `../MNL/dclaborsupply-monorepo/packages/dclaborsupply_app/src/dclaborsupply_app/de/engine_ready.py:106-142`).

### Shock scale

The likelihood is the unit-temperature softmax, and the recovery implementation generates (\varepsilon=-\log[-\log U]) without a multiplier. Hence the operational random-utility normalization is iid type-I extreme value with scale (1), so utility is in unit-Gumbel/nat units (`../MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py:73-91`; `../MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/gates/recovery.py:64-74`).

## 2. Budget mapping and its actual inputs

The implemented map must distinguish EUROMOD output from the utility argument. It is

\[
Y_i^D(j)=T_{FR,2016}\!\left(y_i^L(j),r_i,d_i,z_i;\tau\right)
=ils\_dispy_i(j),
\]

followed by the take-up adjustment, positive-domain floor, and division by (lambda_c) described below. Thus the prose shorthand (c_i(j)=T(cdot)) is not literally the utility input in executed code: utility receives (c_i(j)=C_i(j)/lambda_c). The job-varying input block is

\[
y_i^L(j)=\{lhw,yivwg,yem00,yemxp,yem\},
\]

with (lhw=h) in hours/week, (yivwg=w) in euros/hour, and

\[
yem00=\min(h,35)w\frac{52}{12},\quad
yemxp=\max(h-35,0)w\frac{52}{12},\quad
yem=yem00+yemxp,
\]

in euros/month. Only deciders receive these counterfactual overrides; non-deciders retain baseline values. A non-working decider has zero (yem00,yemxp,yem), but retains baseline (yivwg) in the EUROMOD input (`../MNL/scripts/enhanced/enh_RURO_euromod.py:573-622`, `../MNL/scripts/enhanced/enh_RURO_euromod.py:645-678`). Occupation is also overridden for deciders where present (`../MNL/scripts/enhanced/enh_RURO_euromod.py:624-638`).

The executed schema forms EUROMOD inputs as template columns plus forced job/input columns, then removes only known output prefixes; therefore the benefit/tax variables below are **inputs**, not returned outputs (`../MNL/scripts/enhanced/enh_RURO_euromod.py:776-803`). The frozen exhaustive gate verifies that zero D-equalized fields are engine outputs and that the common schedule is France 2016, with `ils_dispy` the household-specific output (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/nested_endowments/run_ne_step1_gate_v1.py:298-317`).

### (r_i): non-labour resources and budget-side housing inputs

The exact frozen list is:

```text
ypp, yse, ysemy, yiy, ypr, ypt, yptmp, yot, yds, ydses_o,
yempv, yemmy, bed, bun, bunmy, bunmt, bunct, bhl, bho, bhotn,
bhoot, bsa, bsa00, bsaot, bsaoa, bdi, bsuwd, pdi, pdimy, pdi00,
poa, poamy, poa00, psu, psumy, twl, tad, tis, tscer, xmp, xpp,
xhc, xhcrt, xhcmomi, xhcot, amrrm, amrtn, aca, ate, aco, afc,
yem_f, yse_f, bsa00yn_a
```

This is the executable frozen dictionary used by the exhaustive partition gate (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/nested_endowments/run_ne_step1_gate_v1.py:165-222`). Each is held fixed across a household's simulated jobs: the draw builder copies every household-constant field and changes only the job/proposal fields (`../MNL/scripts/bpool/build_bpool_singles.py:179-210`). The EUROMOD connector likewise overrides only deciders' job fields (`../MNL/scripts/enhanced/enh_RURO_euromod.py:573-622`). These are inputs, including reported benefit and tax fields, not the new simulated output.

**UNRESOLVED B1 (units):** the frozen code does not carry a field-level unit/time-basis dictionary for this list. It establishes the job-input and final-output units above, but not whether each resource/benefit/tax/month-count/flag field is, for example, euros/month, euros/year, months, or a code. That dictionary must come from the exact EUROMOD input data dictionary used to build `FR_2016_a3`, tied field-by-field to this execution.

### (d_i): composition and needs inputs

The exact frozen list is:

```text
dms, dcz, dag, dmb, dgn, dcu, dncsy, kfb, kfbmy, kfbcc, kivho,
bfa, bch00, bchlg, bched, bchyc, bchcc, bchot, deh, dehde, dey,
dew, dec, decde, ddi, dsu00, dsu01, dsu02, dct, les, lcs, lfs,
lindi, liwmy, liwftmy, liwptmy, liwwh, lunmy, lpemy, lowas, lse,
loc, liwmy_f, lhw_f, liwwh_f, lunmy_f, e20ps_o, e20pspo_o,
e20psmd_o, e20pslw_o
```

The frozen gate defines and exhaustively checks this block (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/nested_endowments/run_ne_step1_gate_v1.py:109-163`, `../MNL/experiments/JMP_SEMINAR_SPRINT/runs/nested_endowments/run_ne_step1_gate_v1.py:274-296`). The actual call also carries geography (z_i=\{drgn1,drgn2,drg01,drgur,drgmd,drgru\}) (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/nested_endowments/run_ne_step1_gate_v1.py:224-235`). Identifiers `idhh,idperson,idfather,idmother,idpartner,idorighh,idorigperson,ruro_decider` and instruments `dwt,ddt` are schema/merge variables, not economic resource arguments; the executed gate records them separately (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/nested_endowments/run_ne_step1_gate_v1.py:92-101`). As with (r_i), these fields are fixed across jobs.

**UNRESOLVED B2 (policy build):** the frozen sources establish the France-2016 policy system but not an exact EUROMOD software/model release, policy-file digest, or executable build for (\tau). Reproduction of (T(\cdot;\tau)) requires that identifier/digest.

### Non-positive income and take-up

EUROMOD-legitimate non-positive disposable incomes are not discarded. After take-up, the final transformation is

\[
C_i^{raw}(j)=ils\_dispy_i(j)-bsa00\_s_i(j)[1-t_i(e_j)],
\qquad C_i(j)=\max\{C_i^{raw}(j),1\}.
\]

Thus the positive-domain floor is exactly EUR 1/month and precedes (c=C/\lambda_c). The executed clean-couples gate found 425 floored nodes and no exclusion (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/couples_clean_baseline/step0_frame_gates_v1.py:189-207`; frozen counts: `../MNL/experiments/JMP_SEMINAR_SPRINT/runs/couples_clean_baseline/r240_step0_gates_v1.json:153-160`).

For singles, two household traits (t_i(0)) and (t_i(1)) are drawn once with seed 20162016 from exact revealed rates 0.5480225988700564 for non-workers and 0.2653061224489796 for workers; households whose entitlement/reporting reveals behavior retain observed take-up, otherwise the Bernoulli trait is used. The alternative's employment state selects the trait (`../MNL/scripts/p2a/run_p2a_regionlive_rebuild.py:729-764`; exact frozen rates: `../MNL/experiments/JMP_PS1/runs/ps1r222_floor5/ps1r222_s5a_stem_record_v1.json:96-105`; application: `../MNL/experiments/JMP_PS1/runs/ps1r222_floor5/run_ps1r222_s5a_stem.py:156-166`).

For couples, rates were re-estimated, not copied: (0.4375) for NN and (0.3508771929824561) for any-working households. NN alternatives use (t_i(0)); MO, WO and BB use (t_i(1)). EUROMOD is run with take-up neutralized and the adjustment is applied once afterward (`../MNL/experiments/JMP_PS1/runs/ps1h_couples_p1/stage_bc_price.py:375-425`, `../MNL/experiments/JMP_PS1/runs/ps1h_couples_p1/stage_bc_price.py:427-436`; frozen rates: `../MNL/experiments/JMP_PS1/runs/ps1h_couples_p1/ps1h_stage_bc_manifest_v1.json:4-25`).

## 3. The four structural opportunity factors

For a single decision maker, the executed unnormalized kernel can be written exactly as

\[
\log\widetilde g_i(e=0)=-(c_{E,i}+c_{O,i}),
\]

\[
\begin{aligned}
\log\widetilde g_i(1,k,h,w)
={}&\beta_E+x_i^E{}'\gamma-c_{E,i}
 +\xi_{k,g}-c_{O,i}+H(h)+\log\phi_{LN}(w\mid\mu_i(k),\sigma).
\end{aligned}
\]

This is the row-by-row factorization asserted against the accepted engine arrays (`../MNL/scripts/welfare/m08_qw_normalisation.py:151-164`). (c_{E,i}) and (c_{O,i}) are the proposal-weighted within-sampled-set means of the raw employment-market and occupation indices; the engine computes (c=\sum_jq_{ij}x_{ij}/\sum_jq_{ij}) (`../MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py:94-100`), and the factor binding checks working-gating and extracts both constants (`../MNL/scripts/welfare/m08_qw_normalisation.py:204-243`). They are additive centering constants, not factor normalizers.

The normalized density is

\[
\widehat g_i(j)=\frac{\widetilde g_i(j)}{Z_i},\qquad
Z_i=\int_{\mathcal J}\widetilde g_i(j)\,\nu(dj),
\]

\[
Z_i=e^{-(c_{E,i}+c_{O,i})}
\left[1+e^{\beta_E+x_i^E{}'\gamma}S_{occ}I_HI_W\right],
\]

where

\[
S_{occ}=\sum_{k=1}^4e^{\xi_{k,g}},\quad
I_H=\int_5^{70}e^{H(h)}dh,\quad
I_W=\int_0^\infty\phi_{LN}(w\mid\mu_i(k),\sigma)dw=1.
\]

Equivalently,

\[
\log Z_i=-(c_{E,i}+c_{O,i})+
\log\!\left[1+\exp\{\beta_E+x_i^E{}'\gamma+\log S_{occ}+\log I_H\}\right].
\]

The code evaluates this atom-plus-employed integral and records `log_S_occ`, `log_I_H` and `log_I_W=0`, then subtracts `log_Z` rowwise (`../MNL/scripts/welfare/m08_normalisation.py:200-224`, `../MNL/scripts/welfare/m08_normalisation.py:266-286`).

### (i) Employment/access factor (g^E)

Before normalization, (e=0) has factor 1 and (e=1) has

\[
g_i^E(1)=\exp\{\beta_E+x_i^E{}'\gamma\}.
\]

For final singles,

\[
x_i^E{}'\gamma=
10\beta_{E,gsur}gsur_i
+\sum_{r=2}^8\beta_{E,r}reg_{ir}
+\beta_{E,u}drgur_i+\beta_{E,m}drgmd_i
+\beta_{E,15}y15_i+\beta_{E,17}y17_i.
\]

All terms are multiplied by the working indicator in the engine. Region 1, rural status, and year 2016 are omitted references. Crucially, `gsur` is multiplied by 10 in the singles base specification (`../MNL/scripts/bpool/specs/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml:179-239`). The clean-couples specification independently retains the same `gsur: 10.0` scale (`../MNL/experiments/JMP_SEMINAR_SPRINT/configs/estimation_spec_couples_clean_r240_v1.yaml:161-175`); it is not inferred from the singles spec. In couples, household market terms multiply the number of working spouses, while sex-specific terms multiply the respective spouse's working indicator (`../MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py:391-425`).

`gsur` is the local group unemployment rate stored as a fraction (the frozen 2016 range is 0.05--0.23), so the regressor entering the index is ten times that dimensionless fraction (`../MNL/scripts/p2a/configs/p2a_regionlive_rebuild_v1.yaml:149-152`).

This factor is not a Bernoulli probability before the full (Z_i) normalization (`../MNL/scripts/welfare/m08_qw_normalisation.py:341-359`).

### (ii) Hours density (g^H)

On (h\in[5,70]), with all intervals understood up to Lebesgue-null endpoints,

\[
H(h)=\beta_{pt1}\mathbf1_{[17.5,21.5)}(h)
+\beta_{pt2}\mathbf1_{[28.5,30.5)}(h)
+\beta_{35}\mathbf1_{[33.5,36.5)}(h)
+\beta_{ft}\mathbf1_{[36.5,40.5]}(h)
+\beta_{lh}\mathbf1_{[44.5,70]}(h).
\]

The reference is the residual set

\[
[5,17.5)\cup[21.5,28.5)\cup[30.5,33.5)\cup[40.5,44.5),
\]

of total width 26.5 hours. Therefore

\[
I_H=26.5+4e^{\beta_{pt1}}+2e^{\beta_{pt2}}
+3e^{\beta_{35}}+4e^{\beta_{ft}}+25.5e^{\beta_{lh}},
\qquad \log I_H=\log(I_H).
\]

The S8 extension creates `working_f35` as (1\{33.5\le h<36.5,e=1\}) (`../MNL/experiments/JMP_SEMINAR_SPRINT/export/gpu_research_bundle_v1/spec/estimation_spec_S8_corrected_floor5_v1.yaml:22-32`), and the frozen RUM normalizer integrates it as a width-three band while identifying the residual reference (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/rum_benchmark_final/rum_final_config_v1.yaml:151-172`). Thus the 35-hour feature is a **continuous density elevation over ([33.5,36.5)), not an atom at 35**. The normalized conditional hours density is (p_H(h)=e^{H(h)}/I_H).

S8's hours coefficients are common across singles households and sexes. Clean couples splits all six employment/hours coefficients by spouse sex (`../MNL/experiments/JMP_SEMINAR_SPRINT/configs/estimation_spec_couples_clean_r240_v1.yaml:64-77`, `../MNL/experiments/JMP_SEMINAR_SPRINT/configs/estimation_spec_couples_clean_r240_v1.yaml:265-271`).

### (iii) Occupation density (g^{occ})

For (k\in\{1,2,3,4\}),

\[
g_g^{occ}(k)=e^{\xi_{k,g}},\qquad \xi_{1,g}=0,
\qquad
p_g^{occ}(k)=\frac{e^{\xi_{k,g}}}{S_{occ,g}},
\]

\[
S_{occ,g}=1+e^{\xi_{2,g}}+e^{\xi_{3,g}}+e^{\xi_{4,g}}.
\]

Category 1 is the omitted reference; the pre-normalization factor is a softmax numerator, not a probability (`../MNL/scripts/welfare/m08_qw_normalisation.py:360-364`). Within each final model, occupation coefficients are sex-specific; the clean-couples binding lists the male and female coordinates separately with category 1 as reference (`../MNL/experiments/JMP_SEMINAR_SPRINT/configs/estimation_spec_couples_clean_r240_v1.yaml:231-264`).

### (iv) Wage density (g^W)

For a worker,

\[
\phi_{LN}(w\mid\mu_i(k),\sigma)
=\frac{1}{w\sigma\sqrt{2\pi}}
\exp\left[-\frac{(\log w-\mu_i(k))^2}{2\sigma^2}\right],
\qquad w>0,
\]

\[
\mu_i(k)=\beta_{w0}+\beta_{wL}educL_i+\beta_{wH}educH_i
+\beta_{wx}x_i+\beta_{wx2}x_i^2+\delta_k,
\qquad \delta_1=0.
\]

The engine includes the (-\log w) Jacobian and sets the wage log-density to zero on non-working rows (`../MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py:249-259`; couples: `../MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py:461-472`). Hence

\[
\operatorname{median}(W\mid i,k)=e^{\mu_i(k)},\qquad
\operatorname{E}(W\mid i,k)=e^{\mu_i(k)+\sigma^2/2}.
\]

Within the original joint pooled specification, education/experience slopes and the single (\sigma) are shared across sex and household type, and occupation moves location only (`../MNL/scripts/bpool/specs/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml:163-177`; S8 LOC4 extension: `../MNL/experiments/JMP_SEMINAR_SPRINT/export/gpu_research_bundle_v1/spec/estimation_spec_S8_corrected_floor5_v1.yaml:22-25`). Within clean couples, the same slopes and (\sigma) are shared across spouses. The final singles and clean-couples runs are separate estimations, so the two runs do **not** impose equality of their numerical wage coefficients. The full-support (Z_i,log I_H,log S_{occ},log I_W) normalization above is the executed singles welfare normalization; both empirical estimation engines use the unnormalized kernel inside the sampled-set softmax.

**Sharing summary.** In final S8, the consumption curvature and employment/hours, market-access and wage blocks are shared across the two singles sex groups; leisure coefficients and occupation indices are sex-specific. In clean couples, leisure and all six employment/hours coefficients are spouse-sex-specific, occupation indices are spouse-sex-specific, while market-access slopes, wage slopes and (\sigma) are shared between spouses. Because S8 and clean couples are separately estimated frozen models, “shared” here means within a model, not equality between their two estimate vectors. The couples engine's sex/household routing is explicit (`../MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py:391-425`, `../MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py:432-472`), and its split set is frozen in the clean spec (`../MNL/experiments/JMP_SEMINAR_SPRINT/configs/estimation_spec_couples_clean_r240_v1.yaml:265-271`).

## 4. Proposal and sampled-set measure

### Singles proposal

There are (R=100) stochastic alternatives plus a deterministic observed row. For a stochastic row,

\[
q_i(j)=q_E(e)\,[q_O(k\mid dgn_i,educ3_i)q_H(h)q_W(w\mid i,k)]^e,
\]

with (q_E(0)=0.10) and (q_E(1)=0.90) (`../MNL/scripts/bpool/build_bpool_singles.py:114-136`, `../MNL/scripts/bpool/build_bpool_singles.py:172-177`).

The occupation probabilities, each renormalized by its displayed row sum, are

\[
\begin{array}{c|c|rrrr}
dgn&educ3&q_O(1)&q_O(2)&q_O(3)&q_O(4)\\\hline
0&0&.576687&.217791&.122699&.082822\\
0&1&.277525&.300273&.159236&.262966\\
0&2&.031634&.077329&.111599&.779438\\
1&0&.650155&.099071&.068111&.182663\\
1&1&.596091&.130293&.056460&.217155\\
1&2&.098259&.053483&.037313&.810945
\end{array}
\]

and the fallback is ((.40,.25,.15,.20)) (`../MNL/scripts/bpool/occ_draw_empirical.py:30-53`, `../MNL/scripts/bpool/occ_draw_empirical.py:81-90`).

The hours proposal is the six-component mixture

\[
q_H(h)=\sum_{b\in\{PT1,PT2,F35,FT,LH,BG\}}
\frac{\omega_b}{b_b-a_b}\mathbf1_{[a_b,b_b)}(h),
\]

with components/weights

\[
\begin{array}{c|c|c}
b&[a_b,b_b)&\omega_b\\\hline
PT1&[17.5,21.5)&.15\\
PT2&[28.5,30.5)&.10\\
F35&[33.5,36.5)&.24\\
FT&[36.5,40.5)&.20\\
LH&[44.5,70]&.10\\
BG&[5,70]&.21
\end{array}
\]

(`../MNL/scripts/bpool/hours_mixture_d1.py:43-66`). The final frozen frame uses the **exact marginal** density, summing every overlapping component (especially BG), not the density of the latent component that happened to generate the row (`../MNL/scripts/bpool/hours_mixture_d1.py:127-155`; frozen convention: `../MNL/outputs/p2a_singles2016/region_live_margqh_floor5_v1/fr_p2a_singles2016_regionlive_margqh_floor5_v1__mnlmeta.json:23-39`).

The wage proposal is lognormal with

\[
\mu_i^q(k)=2.2543504153383114
-0.0293861519368851\cdot educL_i+0.16073352777951916\cdot educH_i
+0.017552221412091448\cdot X_i-0.00019691062799954626\cdot X_i^2
+\delta_k^q+\delta_t^q,
\]

\[
(\delta_1^q,\delta_2^q,\delta_3^q,\delta_4^q)
=(0,-0.07970080810771316,0.025093195731062043,0.24145593748446914),
\quad \sigma_q=0.3770872353395109,
\]

with (\delta_{2016}^q=0), (\delta_{2015}^q=-0.0027457303228193247), and (\delta_{2017}^q=0.026646408899468097). These are the frozen W1 numbers (`../MNL/scripts/pilot/config/pilot_mincer_coefficients_v1.json:57-88`). Wages are generated as (\log W=\mu^q+\sigma_q z) from a scrambled Halton-normal sequence when available, and evaluated under the matching lognormal density (`../MNL/scripts/pilot/pilot_wage_draw.py:112-188`).

The observed row is copied from the data, inserted at column zero, and all its proposal log terms are set to zero (`../MNL/scripts/bpool/build_bpool_singles.py:221-230`). Therefore its value is **not** generated by the stochastic (q).

### Clean-couples proposal

First draw (Q\in\{NN,MO,WO,BB\}), where

\[
\pi_Q=(1-0.20)\widehat p_Q+0.20/4.
\]

(\widehat p_Q) is the survey-weighted observed quadrant share; the formula guarantees a 0.05 floor (`../MNL/experiments/JMP_PS1/runs/ps1h_couples_p1/build_couples_phase1.py:343-369`). The frozen probabilities are

\[
(\pi_{NN},\pi_{MO},\pi_{WO},\pi_{BB})=
(0.06729618150396371,0.1150655636428206,
0.09323208660198325,0.7244061682512324),
\]

and integrate to one in the frozen manifest (`../MNL/experiments/JMP_PS1/runs/ps1h_couples_p1/ps1h_stage_a_manifest_v1.json:632-672`). Conditional on working, each spouse gets the same empirical occupation proposal, a sex-specific exact-marginal hours mixture, and W1S wage proposal. The hours weights in order ((PT1,PT2,F35,FT,LH,BG)) are

\[
\omega_m=(.026484193190361965,.023365436253625006,.2549456875872686,
.31314453474633924,.17808957788836782,.20397057033403745),
\]

\[
\omega_f=(.03036498802185015,.04572438554499234,.2636805701526308,
.23482841576341562,.009481854393892056,.415919786123219).
\]

They are frozen in the Stage-A manifest (`../MNL/experiments/JMP_PS1/runs/ps1h_couples_p1/ps1h_stage_a_manifest_v1.json:287-303`); the executed redraw explicitly evaluates the marginal (q_H) after drawing (`../MNL/experiments/JMP_PS1/runs/ps1h_couples_p1/stage_a_recalibrate.py:278-293`).

The W1S wage proposal has

\[
\mu_{is}^q(k)=2.178615298514395-0.02440422645935793\cdot educL_{is}
+0.16900681071238574\cdot educH_{is}+0.016345217236971472\cdot X_{is}
-0.00018093601628012962\cdot X_{is}^2+\delta_k^q
+0.13579402377763483\mathbf1\{s=m\}+\delta_t^q,
\]

where ((\delta_2^q,\delta_3^q,\delta_4^q)=(-0.029166766233951907,
0.08391261184924317,0.25883289240374824)), the 2015/2017 shifts are (-0.0026342520098124435,0.027108954034875923), and (\sigma_q=0.371550899502261) (`../MNL/experiments/JMP_PS1/runs/ps1h_couples_p1/ps1h_stage_a_manifest_v1.json:67-110`). The proposal uses raw experience years, as the execution explicitly enforces (`../MNL/experiments/JMP_PS1/runs/ps1h_couples_p1/stage_a_recalibrate.py:296-313`).

The exact joint marginal is

\[
q_i(j_m,j_f)=\pi_Q
\prod_{s\in\{m,f\}}
\left[q_O(k_s\mid dgn_s,educ3_s)q_{H,s}(h_s)q_W(w_s\mid i,s,k_s)\right]^{e_s}.
\]

The code constructs its log exactly as this sum and again inserts the chosen pair deterministically with zero correction (`../MNL/experiments/JMP_PS1/runs/ps1h_couples_p1/stage_a_recalibrate.py:296-340`; frozen contract: `../MNL/experiments/JMP_SEMINAR_SPRINT/configs/estimation_spec_couples_clean_r240_v1.yaml:25-38`).

### Dominating measure and deterministic row

The stochastic proposal is a density with respect to

\[
\nu=\delta_{e=0}+\left(\#_k\otimes dh\otimes dw\right)_{e=1}
\]

for singles, and the corresponding product/joint-quadrant measure for couples. The sampled-set construction then adds the data-dependent deterministic measure (\delta_{j_i^\star}). The stochastic (q) is a density only on the former mixed job measure; `chosen_inclusion_probability=1` is an inclusion rule, not the value of that density (`../MNL/experiments/JMP_SEMINAR_SPRINT/export/gpu_research_bundle_v1/spec/estimation_spec_S8_corrected_floor5_v1.yaml:58-80`).

## 5. Likelihood and chosen-row correction

For the stored set (D_i=(j_i^\star,J_{i1},\ldots,J_{iR})), define the code's row index

\[
\eta_{ij}(\theta)=u_{ij}(\theta)+\log\widetilde g_{ij}(\theta)-\log q^{code}_{ij},
\]

where (q^{code}_{i0}=1) and stochastic rows carry the exact marginal proposal density. The actual criterion is

\[
\ell_i^{code}(\theta)=\eta_{i0}(\theta)
-\log\sum_{j=0}^{R}e^{\eta_{ij}(\theta)},
\qquad
Q(\theta)=-\sum_{i=1}^{G}\ell_i^{code}(\theta).
\]

The engine forms `u + log_h + log_w + log_market - log_prior`, chooses column zero, and returns the negative **sum** (`../MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py:273-279`; couples: `../MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py:474-489`).

### Derivation audit

For a Train-3.7.1-style conditional sampled-alternatives likelihood, Bayes' rule would give

\[
P(j\mid D_i)=
\frac{e^{v_i(j)}\pi(D_i\mid j)}
{\sum_{k\in D_i}e^{v_i(k)}\pi(D_i\mid k)}.
\]

If the same stated protocol included candidate (j) and drew every other member independently from (q), then

\[
\pi(D_i\mid j)\propto\prod_{k\in D_i\setminus\{j\}}q(k)
=\frac{\prod_{k\in D_i}q(k)}{q(j)},
\]

so the common product cancels and **every candidate**, including the observed one, receives (-\log q(j)). The executed construction instead gives the observed row deterministic inclusion and assigns it zero correction, while sampled rows receive (-\log q). It supplies no (\pi(D_i\mid j)) for the counterfactual event that each sampled row was the chosen alternative.

Nor is the criterion the standard simulated-integral likelihood. If

\[
J_i=\int e^{v_i(j)}\nu(dj),\qquad J_{ir}\sim q,
\]

then the usual importance estimate is

\[
\widehat J_i=\frac1R\sum_{r=1}^R\frac{e^{v_i(J_{ir})}}{q(J_{ir})},
\qquad \widehat\ell_i=v_i(j_i^\star)-\log\widehat J_i.
\]

The code instead uses a denominator (e^{v_i(j_i^\star)}+\sum_r e^{v_i(J_{ir})}/q(J_{ir})). Division by (R) would add only a parameter-invariant constant, but inclusion of (e^{v_i(j_i^\star)}) changes the finite-(R) gradient. The observed row has not been drawn from (q), so it has no importance weight under the stated proposal; the welfare implementation explicitly excludes it for that reason (`../MNL/experiments/JMP_PS1/runs/ps1_channelD/run_channelD_D_driver_diagnostic_v1.py:126-141`).

**UNRESOLVED L1 (chosen-row correction):** the coded likelihood cannot be derived from either construction with the currently frozen declarations. Resolution requires one of:

1. a candidate-indexed sampled-set law (\pi(D_i\mid j)) for **every** (j\in D_i), including ordering/replacement/duplicate rules and a density evaluable at (j_i^\star), which algebraically yields the exact coded zero/nonzero corrections; or
2. a target mixed measure that assigns a declared mass to the data-dependent chosen atom, its normalization relative to the continuous mass, and an importance/quadrature identity yielding the exact chosen term and stochastic terms in the denominator.

Calling deterministic inclusion probability one “(q=1)” is insufficient: inclusion probability and proposal density are different objects.

At finite (R=100), (q) changes every stochastic row's denominator weight, the self-normalized probabilities, and generally the optimizer. Even in a valid simulated-integral construction, exact (q) controls Monte Carlo variance and the finite-(R) bias introduced by the log; it does not disappear merely because the proposal is known.

## 6. Inference and weights

The objective is summed, not averaged. The combined male/female objective is the sum of the two group negative log likelihoods (`../MNL/scripts/ps1/run_ps1_battery_part1.py:188-229`). Let

\[
s_i=\frac{\partial\ell_i}{\partial\theta_I},\quad
H=\frac{\partial^2[-\sum_i\ell_i]}{\partial\theta_I\partial\theta_I'},\quad
M=\sum_{i=1}^{G}s_is_i'.
\]

On the interior coordinates (I),

\[
\widehat{\operatorname{Var}}_{model}=H^{-1},\qquad
\widehat{\operatorname{Var}}_{CR1}=
\frac{G}{G-K_I}H^{-1}MH^{-1}.
\]

The implementation obtains the exact JAX Hessian and household score Jacobian, excludes active-bound coordinates, and applies this sandwich (`../MNL/scripts/ps1/run_ps1_battery_part1.py:946-972`). Pinned and active-bound coordinates receive literal NA inference (`../MNL/scripts/ps1/run_ps1_battery_part1.py:993-1062`). For final S8, (G=1555), (K_I=39); there are 41 free coordinates and two lie on active bounds (`../MNL/experiments/JMP_SEMINAR_SPRINT/export/gpu_research_bundle_v1/spec/estimation_spec_S8_corrected_floor5_v1.yaml:102-108`, `../MNL/experiments/JMP_SEMINAR_SPRINT/export/gpu_research_bundle_v1/spec/estimation_spec_S8_corrected_floor5_v1.yaml:238-244`, `../MNL/experiments/JMP_SEMINAR_SPRINT/export/gpu_research_bundle_v1/spec/estimation_spec_S8_corrected_floor5_v1.yaml:299-305`).

Survey weights `dwt` do **not** enter estimation: neither the row criterion nor the combined objective multiplies by them. They do enter reported fit summaries (`../MNL/scripts/ps1/run_ps1_battery_part1.py:610-637`) and welfare distribution aggregation: levels and Ginis use the pooled survey-weight vector (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_singles_welfare/run_ss8_step1_states_v1.py:278-315`, `../MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_singles_welfare/run_ss8_step1_states_v1.py:343-349`).

The covariance interpretation inherits **UNRESOLVED L1**: the score/Hessian/sandwich arithmetic is fully established for the coded criterion, but its structural sampled-choice likelihood interpretation is not.

## 7. Welfare, RQMC, equivalization and Owen attribution

### Population objects

For coalition (S\subseteq\{P,A,B,D\}), let the coalition operator first substitute the relevant primitives and then normalize the resulting opportunity kernel:

\[
\widehat g_{i,S}(j)=
\frac{\widetilde g_{i,S}(j)}{\int_{\mathcal J}\widetilde g_{i,S}(a)\nu(da)}.
\]

The attained ex-ante value is

\[
J_{i,S}=\int_{\mathcal J}
\exp\{u_{i,S}(C_{i,S}(j)/\lambda_c,\ell_{i,S}(j))\}
\widehat g_{i,S}(j)\nu(dj),
\qquad V_{i,S}=\log J_{i,S}.
\]

The support is the non-employment atom plus (k\in\{1,2,3,4\}), (h\in[5,70]), (w>0). Normalization is over this full analytic support, after coalition substitution, never over realized sampled bounds (`../MNL/scripts/welfare/m08_normalisation.py:1-43`, `../MNL/scripts/welfare/m08_normalisation.py:266-272`). (P) replaces preference arguments/coefficients by their reference block; (A) replaces access/occupation arguments; (B) replaces wage-capacity arguments; and (D) selects the pre-priced common endowments/needs panel. A state containing (D) uses the D-bar panel; otherwise it uses the actual panel (`../MNL/experiments/JMP_PS1/runs/ps1_channelD/run_channelD_step345_owen_v1.py:195-204`). The final welfare run performs no new EUROMOD call (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_singles_welfare/run_ss8_step1_states_v1.py:2-13`).

The coalition-consistent W1 reference map is

\[
\Phi_{i,S}(m)=\log\int_{\mathcal J}
\exp\left\{L_{i,S}(j)+BC\!\left(\frac m{\lambda_c};\theta_{c,S}\right)\right\}
\widehat g_{i,S}(j)\nu(dj),
\]

where

\[
L_{i,S}(j)=u_{i,S}(j)-BC(C_{i,S}(j)/\lambda_c;\theta_{c,S}).
\]

W1 is the unique (m=W_{i,S}) satisfying

\[
\Phi_{i,S}(W_{i,S})=V_{i,S}.
\]

(m) is a flat consumption level in real-2016 euros/month at **every** alternative, including the non-employment atom. It replaces disposable consumption, ignores job pay, and does not change wages or rerun EUROMOD. The executed reference map applies one flat level to every row (`../MNL/scripts/welfare/m08_welfare_measures.py:245-278`, `../MNL/scripts/welfare/m08_welfare_measures.py:456-465`). The corrected implementation builds both (L_{i,S}) and (\widehat g_{i,S}) from the same coalition, so (\Phi) genuinely depends on (S) (`../MNL/experiments/JMP_PS1/runs/ps1_channelD/run_channelD_w1consistent_v1.py:21-31`, `../MNL/experiments/JMP_PS1/runs/ps1_channelD/run_channelD_w1consistent_v1.py:195-238`).

### RQMC estimator

The production ex-ante basis excludes the deterministic chosen row. There are eight accepted Owen-scrambled arms of (M=256) stochastic nodes each (`../MNL/experiments/JMP_PS1/runs/ps1_channelD/run_channelD_step345_owen_v1.py:128-138`; exclusion rule: `../MNL/experiments/JMP_PS1/runs/ps1_channelD/run_channelD_D_driver_diagnostic_v1.py:126-129`). Here the exact RQMC density is the frozen base/defensive mixture

\[
q^{RQMC}(j)=
\begin{cases}
0.75q_{base}(j)+0.25r_{def}(j),&j\text{ inside the defensive box},\\
0.75q_{base}(j),&j\text{ outside it},
\end{cases}
\]

where (q_{base}) combines its executed (q_E,q_{Occ},q_H,q_W) limbs. The node builder evaluates all four limbs and the piecewise mixture (`../MNL/scripts/rqmc/rqmc_nodes.py:211-235`); the mixture weight is frozen at 0.25 (`../MNL/scripts/welfare/m08_qw_streams.py:79-79`), and the branch formula is executed directly (`../MNL/scripts/welfare/m08_u6f_box.py:388-408`). For this exact proposal density,

\[
\widehat J_{i,S,r}=\frac1{256}\sum_{m=1}^{256}
\exp\{u_{i,S}(J_{irm})+\log\widehat g_{i,S}(J_{irm})-\log q_{ir}(J_{irm})\},
\]

\[
\overline J_{i,S}=\frac18\sum_{r=1}^{8}\widehat J_{i,S,r},
\qquad \widehat V_{i,S}=\log\overline J_{i,S}.
\]

The arrays construct `opp_hat=log_ghat-log_q` and log-sum the integrand (`../MNL/scripts/welfare/run_m08_u6e_functionals.py:239-252`, `../MNL/scripts/welfare/run_m08_u6e_functionals.py:299-303`). The measure code subtracts (\log(8\times256)) before inversion (`../MNL/scripts/welfare/m08_welfare_measures.py:396-421`), and the final runner independently checks the mean-over-scrambles identity **before** log/inversion (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_singles_welfare/run_ss8_step1_states_v1.py:356-380`). The same pre-log averaging is used inside (\Phi) and hence in the root solve.

### Jackknife band

For any fully recomputed scalar statistic (T), let (T_{(-r)}) omit scramble (r), including redoing (\overline J), inversion, equivalization, Gini and Owen attribution. The implemented rule is

\[
\bar T_{(-)}=\frac18\sum_{r=1}^{8}T_{(-r)},\qquad
se_{jack}=\left[\frac78\sum_{r=1}^{8}(T_{(-r)}-\bar T_{(-)})^2\right]^{1/2},
\]

\[
\text{band}=\left[T_{full}-2.364624251\cdot se_{jack},
T_{full}+2.364624251\cdot se_{jack}\right].
\]

There is no jackknife bias correction of the point estimate: it remains (T_{full}). This is the exact function used (`../MNL/experiments/JMP_PS1/runs/ps1_channelD/run_channelD_step345_owen_v1.py:327-335`), and the final state loop recomputes the full and eight leave-one-out versions (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_singles_welfare/run_ss8_step1_states_v1.py:430-440`).

### Equivalization

The modified-OECD scale is

\[
m_i^{OECD}=1+0.5(N_{i,14+}-1)+0.3N_{i,<14}.
\]

It is calculated from every person row (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_singles_welfare/run_ss9_step4a_equivalence_scale_v1.py:126-151`). Welfare is divided by the coalition-consistent scale: own (m_i^{OECD}) on the actual panel and the D-bar medoid scale (1) when (D) is equalized. The own-scale-in-all-states result is retained only as a diagnostic (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_singles_welfare/run_ss8_step1_states_v1.py:274-294`, `../MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_singles_welfare/run_ss8_step1_states_v1.py:340-349`). Survey weights enter the resulting level/Gini aggregation.

### Nested/grouped Owen rule

Let (I(S)) be the weighted Gini in coalition state (S), and (v(S)=I(\varnothing)-I(S)). The executed grouping is (\{\{P\},\{A,B,D\}\}). The group contributions are

\[
C_P=\tfrac12[I(\varnothing)-I(P)]
+\tfrac12[I(ABD)-I(ABDP)],
\]

\[
C_E=\tfrac12[I(\varnothing)-I(ABD)]
+\tfrac12[I(P)-I(ABDP)].
\]

For (i\in\{A,B,D\}),

\[
C_i=\sum_{Q\in\{\varnothing,\{P\}\}}\frac12
\sum_{T\subseteq\{A,B,D\}\setminus\{i\}}
\frac{|T|!(2-|T|)!}{3!}
\left[I(Q\cup T)-I(Q\cup T\cup\{i\})\right].
\]

The code enumerates all 16 states and implements these exact weights (`../MNL/experiments/JMP_PS1/runs/ps1_channelD/run_channelD_step345_owen_v1.py:185-233`).

## 8. RUM benchmark

The RUM replaces every household-indexed opportunity density by one household-invariant, normalized density

\[
\bar g(e=0)=\pi_0,
\]

\[
\bar g(1,k,h,w)=\pi_1\,\bar p(k)\,p_H(h)
\phi_{LN}(w\mid\bar\mu(k),\widehat\sigma),
\]

with

\[
\pi_0+\pi_1=1,\quad\sum_k\bar p(k)=1,
\quad\int_5^{70}p_H(h)dh=1,
\quad\int_0^\infty\phi_{LN}(w\mid\bar\mu(k),\widehat\sigma)dw=1.
\]

The implemented row formula and mixed-support unit-mass check are explicit (`../MNL/scripts/welfare/m08_rum_gbar.py:385-450`). Normalization cancels the household-specific centering constant, which is why the result is actually common (`../MNL/scripts/welfare/m08_rum_gbar.py:41-49`).

- **RUM-A:** retains the normalized reference employment margin and certified band density (p_H(h)=e^{H(h)}/I_H).
- **RUM-B:** sets (​\pi_0=\pi_1=1/2) and (p_H(h)=1/65) on ([5,70]).
- Both retain the common normalized occupation pmf (\bar p(k)) and the common reference Mincer lognormal. With occupation location shifts, (\bar\mu(k)=\bar X'\widehat\beta+\widehat\delta_k), so the marginal offered-wage density is the mixture (\sum_k\bar p(k)\phi_{LN}(w\mid\bar\mu(k),\widehat\sigma)) (`../MNL/scripts/welfare/m08_rum_gbar.py:139-169`).
- Moving from the engine's occupation indices to (\bar p) requires (S_{occ}=1/\bar p(1)) to be absorbed into the employment margin; the code asserts that identity (`../MNL/scripts/welfare/m08_rum_gbar.py:277-313`).

The preference block remains. RUM-A re-estimates the ten singles preference constants/curvatures. RUM-B additionally moves the work constant and all five hours-band constants, including F35, into utility and re-estimates them, for 16 free constants total (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/rum_benchmark_final/rum_final_config_v1.yaml:179-226`). The proposal is retained unchanged: the RUM index is

\[
\eta_{ij}^{RUM}=u_{ij}^{RUM}+\log\bar g(j)-\log q_{ij},
\]

and the same summed sampled-set objective is used (`../MNL/scripts/welfare/m08_rum_likelihood.py:110-123`, `../MNL/scripts/welfare/m08_rum_likelihood.py:167-205`). Thus the RUM also inherits **UNRESOLVED L1**.

The recorded likelihood comparison is **not** a likelihood-ratio test. The surviving opportunity coefficients are held at S8 values rather than re-optimized under the restriction, so (2(Q_{RUM}-Q_{S8})) is recorded only as a descriptive **upper bound** on the LR statistic for the freely maximized restriction (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/rum_benchmark_final/run_rb_step1_estimate_v1.py:451-510`). The fit artifact repeats that the comparison is descriptive provenance, not model selection (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/rum_benchmark_final/rb_step2_fit_v1.json:2-18`).

## 9. Matched-pair figure

The panels do not plot four choice probabilities:

1. Panel (a) plots the deterministic **preference** curve (\omega_iBC((80-h)/10;\theta_{\ell i})). It is neither (p^{opp}) nor (p^{choice}) (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/figE1_matched_households/make_e1_figures_v1.py:121-137`).
2. Panel (b) plots the **unconditional opportunity** hours density (p_i^{opp}(e=1,h)=\pi_i\phi_H(h)), and separately reports the non-employment atom (p_i^{opp}(e=0)=1-\pi_i). It is not the conditional (\phi_H(h)) alone and not a choice distribution (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/figE1_matched_households/make_e1_figures_v1.py:139-170`).
3. Panel (c) plots the **unconditional opportunity** occupation probabilities (p_i^{opp}(e=1,k)=\pi_i p_i^{occ}(k)), not (p_i^{occ}(k\mid e=1)) and not choice probabilities (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/figE1_matched_households/make_e1_figures_v1.py:172-195`).
4. Panel (d) plots the occupation-mixture wage-offer density **conditional on employment**, (\sum_kp_i^{occ}(k)\phi_{LN}(w\mid\mu_i(k),\sigma)); it is not multiplied by (\pi_i) and is not (p^{choice}) (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/figE1_matched_households/make_e1_figures_v1.py:197-222`).

Observed hours/occupation/wage appear only as markers. The figure code explicitly labels panels (b)--(d) the offer distribution rather than the choice distribution (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/figE1_matched_households/make_e1_figures_v1.py:241-253`).

Admissible employed pairs have the same observed employment state, occupation, model hours band and observed-wage quintile; the paper's headline pair is selected only from the employed stratum (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/figE1_matched_households/run_e1_matched_households_v1.py:548-580`). The forward rule restricts (d_{pref}) to at or below its admissible-set 10th percentile and maximizes total-variation opportunity distance (d_{opp}); the reverse rule restricts (d_{opp}) to its 10th percentile and maximizes (d_{pref}) (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/figE1_matched_households/run_e1_matched_households_v1.py:668-711`, `../MNL/experiments/JMP_SEMINAR_SPRINT/runs/figE1_matched_households/run_e1_matched_households_v1.py:720-749`). “Clean” additionally requires the maximized distance to be at least (1.5) times its admissible-set median. Same-sex rankings are reported separately but are not part of the headline admissibility rule.

## 10. Child-age construction versus model/frame counts

Three different objects must not be conflated:

1. **Utility/frame `n_children`:** all household members with age (<20), regardless of parent links:
   \[
   n_i^{model}=\sum_{p\in\mathcal H_i}\mathbf1\{A_p<20\}.
   \]
   This is what the final singles and clean-couples frames feed to the leisure shifter (cutoff: `../MNL/scripts/p2a/run_p2a_regionlive_rebuild.py:185-186`; singles count: `../MNL/scripts/p2a/run_p2a_regionlive_rebuild.py:781-783`; couples count: `../MNL/experiments/JMP_PS1/runs/ps1h_couples_p1/build_couples_phase1.py:721-725`).
2. **Parent-linked child-age construction:** a person is counted for a parent only when the household person row links through `idmother` or `idfather`. Its bands are ([0,3),[3,6),[6,9),[9,12),[12,18),[18,\infty)), and `n_children_total` sums **all linked offspring, including adult offspring** (`../MNL/scripts/bpool/build_bpool_estimation_ready.py:42-53`, `../MNL/scripts/bpool/build_bpool_estimation_ready.py:141-169`). It is not the final model's `n_children`.
3. **Welfare equivalence count:** all household members younger than 14, (N_{i,<14}), used only in the modified-OECD scale. The executed step explicitly treats disagreement with model `n_children` as legitimate and reports rather than reconciles it (`../MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_singles_welfare/run_ss9_step4a_equivalence_scale_v1.py:1-24`, `../MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_singles_welfare/run_ss9_step4a_equivalence_scale_v1.py:126-163`).

## UNRESOLVED register

- **B1 — field-level input units/time bases.** The execution establishes which fields are EUROMOD inputs, which vary across jobs, and the units of job inputs/output, but not a unit dictionary for every (r_i,d_i,z_i) field. Needed: the exact EUROMOD input data dictionary/version tied to the frozen France-2016 template.
- **B2 — exact policy executable (\tau).** “France 2016” is established; the EUROMOD release/model build and policy-file digest are not. Needed: executable/version and policy-system digests.
- **L1 — deterministic chosen-row likelihood correction.** The zero correction on the chosen row and (-\log q) on stochastic rows are coded, but no candidate-indexed sampled-set law or mixed-measure importance identity yields that combination. Needed: either the full (\pi(D_i\mid j)) protocol for every candidate or a normalized target measure with an explicit chosen-atom mass and exact estimator identity.
- **Inference consequence of L1.** The score, Hessian and sandwich are valid derivatives of the coded criterion, but a structural likelihood interpretation of those standard errors remains conditional on resolving L1.
