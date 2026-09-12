# JMP measure map v1 — MEASURE-MAP-1R

Date: 2026-09-11. Status: **audit return, uncommitted; not an acceptance ruling**.
Authority: Appendix A, R4 of [JMP_W1_fork_ruling_v1.md](JMP_W1_fork_ruling_v1.md), as reissued in the task.

**Finding:** the stored objects called W1–W6 below use an inclusive attained value. Their executed class is **DIFFERENT OBJECT** relative to the corresponding observed-bundle theory measure. W1-EA is retired under R2. Literal W1-F and W4 agree to machine precision in all three authorized household checks. **NO stored artifact identified in the audited production lineages holds literal observed-bundle W1-F/W4 for the full sample.**

Only the deterministic checks in §4 were computed. Stored household values were read, not rerun. No sample-wide welfare vector, inequality statistic, decomposition, estimation, pricing, draw, or code change was produced. Repository output is limited to this report. Household levels and exact reproduction code are retained only in the restricted artifact outside both repositories (Appendix A), following the user's BASELINE_F1 §2 instruction.

## 1. Preconditions and source conventions

Repository HEADs recorded before the audit:

| Repository | HEAD |
|---|---|
| MNL | `aa36e816e46568ff448810e5b89c28ea616a2476` |
| Job_Market_paper | `f6346232ef6696c623b053085991349f2bb5c462` |

The active engine is in the nested `MNL/dclaborsupply-monorepo` checkout, inspected read-only at `55bb0d0ea7a1ad2d683f8b2b2a9f7bfb3d5118df` (clean when inspected). Appendix C records the initial dirty files, including untracked files. Both top-level worktrees were already dirty.

Fresh SHA-256, read from the actual file bytes:

| File | SHA-256 |
|---|---|
| MNL/scripts/welfare/m08_welfare_measures.py | `ccb8a2c9ddece225522201d8b667e69530c8c23c90d3f192c6a2523a19c21335` |
| Job_Market_paper/Theory_other_project/jobs_and_wellbeing.tex | `d8687d3cfb71ce00f81613286e784c71c0e643721987bebf0d57226afe2a02d1` |

Both digests have 64 hexadecimal characters. The earlier 63-character m08 digest is discarded. All line references below were established by rereading the current files, not copied from the earlier return.

Paths in the evidence ledger are relative to `C:/Users/hisham/Repo`. Line ranges identify the exact code inspected. “Attainment” and “reference” always refer to the two sides of the executed equation; neither an inclusive attainment nor an inclusive reference is relabelled literal.

## 2. R4 table

Notation: \(b_i(c)=\beta_c BC(c/\lambda_c;\theta_c)\), \(u_i(c,j)=b_i(c)+L_i(j)\);
\(\operatorname{LSE}_D f=\log\sum_{j\in D}\exp f_j\) and
\(\operatorname{LME}_D f=\operatorname{LSE}_D f-\log |D|\).
\(a_{ij}\) is the **as-executed** opportunity/proposal term, not a claim that all required proposal factors were correctly included.
\(T_i=\operatorname{LSE}_{D_i}[u_i(C_{ij},j)+a_{ij}]-\log n_i\).
For S12, \(r_{ij}=a_{ij}-\log g^W_{ij}+\log q^W_{ij}\); for the older common-core W1, \(r=a\). S12 singles' omitted base-proposal factor is preserved, not repaired (E3 below).
In the theory column \(u_i(z)\) means the utility of the given attained bundle; step 3 uses \(z=z_{\rm obs}\).

The permitted class vocabulary is exactly: **LITERAL MATCH**, **NUMERICAL APPROXIMATION TO THE SAME OBJECT**, **SMOOTHED ANALOGUE**, **DIFFERENT OBJECT**, **NOT IMPLEMENTED**. A log-mean reference fed an inclusive target is classed **DIFFERENT OBJECT**, not merely **SMOOTHED ANALOGUE**. The latter would conceal the attained-side substitution.

| Welfare object | Theory definition from authoritative manuscript | Exact mathematical object implemented in code | Executed class | Code path/function | Reference domain | Whether epsilon enters | Whether opportunity density enters | Whether proposal density enters | Whether the object depends directly on A | Whether the object is needed in the revised JMP | Attained side actually passed | Reusable for a literal computation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| W1 (stored W1 / W1-EA) | \(u(z)=\max_{j\in A}u(w,j)\), equivalently \(\min_{j\in A}m_i(j)\); T:258–266 | Solve \(b_i(w)+\operatorname{LSE}_{D_i}(L_i+r_i)-\log n_i=T_i\). S12 log form: \(w=\lambda_c\exp\{[\operatorname{LSE}(u+a)-\operatorname{LSE}(L+r)]/\beta_c\}\). F4A omits the same \(-\log n\) on both sides. | **DIFFERENT OBJECT** | E1–E4; WM.R_replace; S12.single_vectors / couples_run; F4A.GroupState.R_replace | Sampled own/common nodes, including home states; **LSE, not max**. Working-only historical variant keeps home consumption in F4A; S12 working-only diagnostic instead excludes home from H. | **integrated**, attained and reference LSE (E1–E4) | **yes**, attained and reference (E1–E4) | **yes**, as-executed numerical weights; S12 H removes wage proposal with wage density but this does not make it a max (E3) | Own support/kernel enters both sides; code supplies quadrature support, not a recovered literal realized A. | **W1-F: primary. W1-EA: retired (DIFFERENT OBJECT)**, R1–R2. | Inclusive value; never \(u(z_{\rm obs})\). | **yes for W1-F via the W4 home-reference primitive** under R1; **no for R_replace/W1-EA itself**. |
| W2 | Choose \(t\) with \(u(z)=\max_{j\in A}u(y(j)-t,j)\); \(W2=\max_A y-t\); T:270–283 | \(s\) solves \(\operatorname{LSE}_{D_i^{+}(s)}[u(C_{ij}+s,j)+a_{ij}]-\log n_i=T_i\); \(W2=\max_{D_i}C_{ij}+s\). | **DIFFERENT OBJECT** | E1, E2, E5; WM.R_shift / compute_measures:437–463; U6F._w2_trajectory16 | Own sampled nodes surviving positive shifted consumption; **LSE**; final anchor is a consumption max, not a utility max. | **integrated**, both sides (E1, E2, E5) | **yes**, both sides (E1, E2, E5) | **yes**, both sides' stored numerical weights (E2, E5) | Yes through own reference support/anchor and executed target. | **no current ruling requires**, R4 reissue §7. | Inclusive value \(T_i\), via ba.v_logsum. | **no**: changing the target alone leaves LSE and the disposable-income substitution. |
| W3 | \(u(z)=\max_{j\in A}u(y(j)+w,j)\); T:294–302 | Shared-core W3 is the shift \(s\) in W2's equation. It is zero at baseline when attained and reference arrays coincide. S12 additionally solves a wage-free-kernel LSE using gross node earnings, and a household-resource variant (§3). | **DIFFERENT OBJECT** | E1, E2, E5, E6; WM.R_shift; U6F._w3_identity16; S12.solve_w3_theory / w3_record | Own nodes, **LSE**. S12 gross-resource variants are separately defined. | **integrated**, both sides (E1, E2, E5, E6) | **yes**, both sides (same evidence) | **yes**, numerical weights on both sides, with S12 wage-free reference convention (E3, E6) | Yes through own reference support and executed target. | **no current ruling requires**. | Inclusive value; baseline zero is an internal same-functional identity, not observed-bundle equality. | **no**: R_shift does not take the theoretical max. |
| W4 | \(u(w,o)=u(z)\); T:306–310 | \(b_i(w)+L_i(o)=T_i\). F4A instead uses the unnormalised attained LSE. S12 premise audit further subtracts the log mass of H's kernel from \(T_i\). | **DIFFERENT OBJECT** | E1, E3, E4, E7; WM.R_single_node; F4C:257–267; S12:355–356,762 | Singleton home **state** o: no set smoothing in the reference. | **integrated in attainment**; no epsilon in singleton reference (E1, E3, E4, E7) | **yes in attainment**; no in singleton reference (same evidence) | **yes in attainment**; no in singleton reference (E2–E4); unit-mass correction does not change this classification. | No reference dependence at fixed target; the executed inclusive target carries own support/access. Theory W4 has no direct A dependence at fixed z. | **as the empirical identity W1-F = W4**, R1; stored ex-ante levels are not that identity. | Inclusive value: F4A LSE; F4C/M08/S12 LSE minus log(node count); corrected S12 also minus log mass. | **yes**, R_single_node plus direct/numerical inversion against \(u(z_{\rm obs})\). **Not** the unmodified theta_c=0 analytic wrapper (E1). |
| W5 | \(u(z)=\max_{j\in\bar A}u(y(j)+w,j)\); T:314–328 | \(w\) solves \(\operatorname{LSE}_{\bar D^{+}(w)}[L_i(j)+b_i(\bar C_j+w)+\bar a_j]-\log n_{\bar D}=T_i\). | **DIFFERENT OBJECT** | E1, E2, E5; WM.R_abar / AbarReference; U6F._w5_diagnostic16 | Type-conditioned median donor's priced alternative set; **weighted LME, not max**. Construction implementer-declared, not ratified. | **integrated**, attained and reference (E1, E2, E5) | **yes**, attained plus donor reference weights (E1, E5) | **yes**, attained and reference numerical weights (E2, E5) | No own-A reference argument once donor/type is fixed; executed attainment carries own support/access. Theory fixes \(\bar A\), independent of own A at fixed z. | **no current ruling requires**. | Inclusive value \(T_i\), passed explicitly at U6F:706–712. | **no**: LME, shifted disposable income, and donor-set construction remain. |
| W6 | \(u(z)=\max_{j\in\mathcal J}u(w,j)\), equivalently \(\min_{j\in\mathcal J}m_i(j)\); T:335 | \(b_i(w)+\operatorname{LME}_{D_J}L_i=T_i\), where the reference has uniform node weights. | **DIFFERENT OBJECT** where executed; **NOT IMPLEMENTED** in F4A and S12 | E1, E4, E5, E8; WM.R_universal; F4C.R_w6; P2a.compute_measures | F4C/P2a six-hour grid \(\{0,20,30,35,39,48\}\), **LME, not max**; includes home, omits 5h. Not the ruled market universe. | **integrated** in attained LSE and uniform reference LSE (E1, E4, E8) | **yes in attainment**; **no in uniform reference** (same evidence) | **yes in attainment**; **no in fixed uniform reference** (E2, E4, E8) | Reference fixed independently of own A; executed inclusive target carries own support/access. Theory has no direct A dependence at fixed z. | **Dense-law M / literal Measure 6 on the market universe: sensitivity**, R1. | Inclusive value \(T_i\). F4A's W6 column is null, not a computation. | **no** for R_universal/R_w6; a literal minimum must replace LME and use the stated universe. |

**Full-sample production status of revised objects:** W1-F, observed-bundle W4, and literal market-universe Measure 6 are **NOT IMPLEMENTED** in the audited stored production results. The three new checks in §4 are **LITERAL MATCH** to the stated definitions, confined to those households and universes; they are not a distribution artifact.

“Depends directly on A” needs this distinction: the theory treats z as an argument and holds it fixed. The executed paths replace that argument by an environment-dependent inclusive value. Consequently, absence of A/g/q from W4's singleton reference or W6's uniform reference does **not** imply their executed outputs are independent of access, epsilon, or proposal weights.

## 3. Execution ledger and mathematical evidence

**T — authoritative theory:** `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.tex`, measures at 258–335. W1/W2/W3/W5/W6 compare with a preference **maximum**; W4 compares with the singleton home bundle. A minimum of equal-pay equivalents follows because b is increasing. No equality proof turns the code's sums into these maxima.

**E1 — shared measure core:** `MNL/scripts/welfare/m08_welfare_measures.py`.
- 65–70: Box–Cox including log branch; 73–95: LSE primitives.
- 193–196: leisure separated from consumption and opportunity stored separately.
- 255–265: shifted disposable consumption, finite/positive-domain mask; 267–275: R_shift is weighted LSE.
- 283–287: R_replace is weighted LSE over L + b(w) + opp.
- 289–293: R_single_node is exactly L(home) + b(w), with no opp/q/epsilon argument.
- 295–303: R_universal is uniform LSE minus log(n_j), with no opp in the reference.
- 305–326: R_abar includes abar.opp and subtracts log(abar.n_alts).
- 338–351: Abar's construction explicitly described as implementer's binding, not ratified; 372–389 recovers the individual's leisure coefficient.
- 405–430: compute_measures **always** changes V_is to V_actual = V_is − log S, and solves against V_actual.
- 437–463: W3 shift and W2 = max consumption + shift; 465–474: W1; 478–489: W4; 495–520: W5; 523–535: W6.

The W4 wrapper's line 485 evaluates \(1/\theta_c\) without the log-limit branch. It cannot be claimed as an unchanged ready-to-run literal W4 wrapper at accepted \(\theta_c=0\). The reusable component is **R_single_node**, independently inverted in §4. Passing u_obs as V_is to compute_measures without adjusting its −log S would also be wrong.

**E2 — where the attained inclusive value and weights originate:** `MNL/scripts/welfare/run_m08_u6e_functionals.py`, BasisArrays:
178–180 constructs the chosen-row-aware wage proposal correction;
249–251 stores u and **log_ghat minus corr_vec** as opp_hat;
294–303 builds the reference with those arrays;
307–311 forms ba.v_logsum = LSE(u + opp_hat);
332–347 supplies that value to compute_measures.
`MNL/scripts/welfare/m08_normalisation_tests.py`:109–129 separately returns log_ghat, log_q, and opp_hat = log_ghat − log_q.

These are **distinct returned fields**. BasisArrays uses `a['log_ghat']`, not `a['opp_hat']`, at 250–251. Thus this path must not be described as necessarily including the full base-proposal correction: the wage correction is explicit; the base factor is absent there. Proposal density nevertheless enters the executed weights, and also determines the stored quadrature nodes. No proposal repair was performed.

`MNL/scripts/welfare/run_m08_welfare_decomposition.py`:425–433 likewise forms LSE(u + opp); 545–572 passes it through measures_with_abar; 1093–1112 does so for the baseline family. These are execution call sites, not merely function signatures.

The epsilon labels in the table follow the mathematical LSE operation: at the fixed random-utility scale it is an inclusive value with shocks integrated out. Absence of an explicit epsilon draw argument is **not** exclusion of epsilon. Numerical quadrature approximates that inclusive object, not the manuscript maximum. Proposal weights are numerical, not normative theory primitives.

**E3 — S12, accepted S11 parameters:** `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/run_s12_welfare_record_v1.py`.
- 303–305 loads singles S11 theta; 269–270 binds estimated beta_c; 691–692 loads couples S11 theta.
- 338–359: single_vectors forms attained = LSE(u+op), H = LSE(u−beta log c+op_reference), W1 = lambda exp((attained−H)/beta), W4 = lambda exp((attained−log n−L_home)/beta).
- 374–382 explicitly constructs wage-free reference weights \(r=a-\log g^W+\log q^W\).
- 67 and 341–344 use common columns 1…2048, excluding the chosen anchor. **The selected observed row is not the attained target.**
- 740–747 uses couples V from welfare_core and removes beta log c and structural wage density, adding proposal wage density for the reference.
- 755–763 constructs L_home and the same W1/W4 inclusive formula for couples.
- 607–611 and 794–797 assemble only W1_EA_raw and W1_EA_equivalized in principal household distributions; 974 persists the combined parquet. No W4/W6 household column is written there.
- 956–964 caches the singles return; the inspected v5 cache contains the principal W1 distribution and W4 summary dictionary, not a household W4 vector.
- 926–927 explicitly withholds the original W4 summaries as kernel-scale-dependent. This status is preserved.

Stored S12 W1 distribution: `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/s12_principal_welfare_distributions_v1.parquet`; SHA-256 in Appendix B. W4 summaries: `s12_welfare_record_v1.json` in the same directory; unit-mass-corrected summaries in `s12_w4_premise_audit_v1.json`. **No S12 W6 call exists.**

**E4 — original and completed fastlane results:**
`MNL/scripts/welfare/fastlane/run_f4a_singles_measure_core.py`:53–65 binds the pooled staged input and historical parameters; 197–202 constructs u, V and opp=V−u; 237–242 maps the external **V_i_IS_staged** to each household; 262–275 supplies the reference functions. Calls at 597–598 (W3), 627 (W4), and 681–682 (W1/working-only) use **gs.V_target**, not chosen utility. Output at 723–752 stores that target and solved values; W6 is null with BLOCKED_PENDING_GRID_RATIFICATION.

`MNL/scripts/welfare/fastlane/run_f4c_final_singles_measures.py`:47–50 sets the six-node grid; 196–199 replaces attained target with V_target−log n; 257–267 solves W4; 317–324 solves W6 using **uniform log-mean**, and 405–423 persists the targets and measures. F4A/F4C files are named and hashed in Appendix B. `run_f5_singles_measure_family.py`:314 reads F4C for its subsequent report; it does not replace the attained side with an observed bundle. F4A→F4C changes W4 normalization and adds W6, not theoretical correspondence.

**E5 — stored M08/U6F W2–W6 execution:**
`MNL/scripts/welfare/run_m08_u6f_functionals16.py`:252,337 calls measures_on (E2) for its family results; 667–668 sends ba.v_logsum to W3; 706–712 sends ba.v_logsum to W5 per donor type; 736–737 sends ba.v_logsum to W2. Lines 1633–1636 put W3_validation_identity, W5_signed_diagnostic and W2_compatibility_finding into the stored record. The inspected record is:

`MNL/outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/attempts/20260825T164802Z_500708_1759e2e09f0941609ea183ae51ea8f20_u6ffn16_U6F_FUNCTIONALS16_DONE/u6f_functionals16_v1.json`.

Its step3_functionals contains those W2/W5 diagnostics and W1/W4/W6 results. SHA-256 is in Appendix B. This is an **aggregate record**, not a literal household W1-F distribution; no numbers from those aggregates were computed or reproduced here.

**E6 — W3 exceptions in S12:** S12:156–187 solves
\[
 \operatorname{LSE}_j[L_j+r_j+\beta_c\log((y_j^{gross}+w)/\lambda_c)]
 =\operatorname{LSE}_j[u_j+a_j],
\]
with invalid shifted nodes omitted. Gross node earnings are hours × wage × 52/12 (409–414); couples baseline auxiliary data follow the same call. S12:190–215 also reports
\[
w=\lambda_c\exp\{[\operatorname{LSE}(u+a)-\operatorname{LSE}(L+r)]/\beta_c\}
 -ils\_origy_i.
\]
These appear as theory_strict_y_node_plus_w and household_resource_ils_origy_plus_w in `s12_W3_v1.csv`. The label “theory_strict” is a stored name, **not a LITERAL MATCH finding**: the reference remains LSE and attainment remains inclusive. The shared-core zero identity must not be generalized to these differently defined S12 diagnostics.

O-1 provenance is independently verified: `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md`:162–167 records PI ratification R-85; `JMP_M08_singles_welfare_execution_contract_v5.md`:919–938 explicitly applies the disposable-income shift to W2/W5 and W3 in its validation role. That operationalization does not prove equality to the current manuscript's pre-tax-pay primitive, nor authorize retaining W2/W3/W5 in the revised JMP.

**E7 — S12 W4 normalization and 119 couples:**
`MNL/experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/run_s12_w4_premise_audit_v1.py`:27–41 forms log mass and subtracts it from attained LSE−log n before home inversion. Thus even “unit-mass-corrected W4” uses an inclusive target. Lines 181–200 construct the consumption_raw>0 mask, identify neither-work nodes, and count households with no positive-consumption neither-work bundle. The stored count is **119** at `s12_w4_premise_audit_v1.json`:174,186; this count was read, not recomputed.

**E8 — P2a household family and earlier couples W1:**
`MNL/scripts/welfare/run_p2a_singles_welfare.py`:121–122 sets V_target to the engine inclusive value; 172–185 forms/normalizes it; 191–222 passes it to W3/W1/W4 and uniform-LME W6; 422–428 persists the family. The storage path and hash are in Appendix B.
`MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_couples_welfare/cw_states_lib_v1.py`:205–229 computes W1 from LSE(V) and LSE(V−log c) at beta_c=1, theta_c=0. It is the older R240 inclusive object used by the identity audit, not literal observed-bundle W1-F.

## 4. Authorized one-household deterministic checks

### Parameters and consumption binding

The accepted tables were identified independently of REC-1. The acceptance/certification memo is
`MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_report_v1.md`:3–12, which separately certifies singles and couples as **SPECIFICATIONS OF RECORD FOR WELFARE**. Its machine record starts with S11_WELFARE_SPECIFICATIONS_OF_RECORD_CERTIFIED. The adoption record is `Job_Market_paper/docs/Missions/JMP_current_state_dashboard_v1.md`:25,27,32 (R-291/R-286: S11 model of record; prior parameters historical). The September 11 fork ruling controls welfare status and supersedes older dashboard welfare claims; this audit uses the dashboard only for **parameter provenance**.

| Candidate/source table | Male theta_l | Female theta_l | theta_c; beta_c | Provenance disposition |
|---|---:|---:|---|---|
| S11 singles: s11_singles_parameter_table_v1.csv | -1.6262666488391833 (sm) | -0.927353434570206 (sf) | 0; 2.038731824410903 | Accepted singles; used for both checked singles. |
| S11 couples: s11_couples_parameter_table_v1.csv | -0.9761092135887932 (m) | -1.6863074228063055 (f) | 0; 2.101720268206207 | Accepted couples; used for checked couple. |
| Older couples: couples_clean_baseline/r240_step3_parameter_table_v1.csv | -1.032063120736749 | -1.866863037689599 | 0; 1 in old couples W1 evaluator | Historical R240; not the S11 accepted corrected scale. This resolves the two candidate couples tables for this audit. |
| F4A/F4C: scripts/bpool/specs/theta_hat_realdata_901_v1.csv | -1.8616120265204585 (sm) | -1.349085275197915 (sf) | 0.007580978321100435; 1 | Historical pooled singles parameters; not comparable at fixed S11 theta. |
| P2a: scripts/welfare/configs/theta_hat_p2a_singles2016_v1.csv | -2.3406522921782837 (sm) | -1.984587929836038 (sf) | 0.093458702516659; 1 | Historical P2a singles parameters. |

The S11 singles table also carries a **pinned, unused couples-female** theta_l_f = -2.131739110508045; it must not be substituted for either S11 singles-female theta_l_sf or accepted couples-female theta_l_f. Similarly the historical pooled/P2a files carry inactive couples coordinates. No couples parameter is inferred from a singles table. Full table paths and **separate fresh hashes**, including S11 theta arrays, are in Appendix B.

Chosen rows come from:
- `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/singles_engine_ready_criterion_a_v1.parquet`, source_idhh = H-S1 and H-S2, is_chosen = 1.
- `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/couples_engine_ready_criterion_a_v1.parquet`, source_idhh = H-C1, is_chosen = 1.

**C_obs = consumption = consumption_raw = household EUROMOD-priced disposable consumption after the stored take-up rule; raw, not OECD-equivalised.** The engine argument is c_norm = C_obs/c_scale. This is a numerical normalization of raw consumption, not household equivalisation. Builder evidence: `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s4_corrected_frame/build_s4_corrected_frame_v1.py`:581–589 binds consumption to ils_dispy_takeup without flooring; 848 states resident-member aggregation. Active loader `MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/data/loader.py`:581–604 and 654–678 takes c_norm. Active engine `.../likelihood/engine_numpy.py`:528–587 and 1458–1463 evaluates it. S12:607–611 applies OECD equivalisation **after** calculating W1.

The relevant normalizers in the accepted estimation frames are lambda_c = 1938.238719107138 (singles), 4247.875047307145 (couples), and lambda_l = 10 hours. Leisure is 80 − hours. Coefficients include the stored household age, squared-age, and applicable child shifters. At log consumption lambda_c cancels from W1-F. E2 is **resolved as a code/data identification in this return: raw consumption**; the Deputy's E2 ruling remains outside this audit. No ambiguous raw/equivalised branch was found, so no second normative C_obs was invented. The checked couple's m_oecd is 2.1; the two singles' m_oecd is 1.

Neither prescribed household is a nonworker. A read-only selection of is_chosen=1, working=0 singles found the lowest source_idhh **H-S2**, which was added. No welfare was calculated for the remaining sample.

### E2 frozen consumption contract

| Binding | Frozen value |
|---|---|
| Source paths and selection | The separately hashed accepted criterion-A singles/couples parquet files above; source_idhh and is_chosen=1. |
| Source column entering estimated utility | **c_norm**, loaded into data.consumption. The backing euro-valued C_obs column is **consumption**, identical to **consumption_raw** on these accepted chosen rows. |
| Preprocessing | Household sum of resident members' EUROMOD **ils_dispy_takeup**, with stored take-up treatment already applied; consumption=consumption_raw; strictly positive estimation domain; **no EUR1 floor**. Then c_norm=consumption/c_scale. Builder:581–589,848; loader:581–604,654–678. |
| Equivalisation | **None before utility or in literal C_obs.** c_scale division is numerical normalization, not modified-OECD equivalisation. S12 applies m_oecd only to the resulting welfare output (607–611,794–797). |
| Units | C_obs and equivalent consumption: **stored EUR per household per month**; c_norm: dimensionless. This audit applies no annualisation, deflation or currency conversion. Leisure: weekly hours divided by its stored normalization. |
| Parameter regime | Separate accepted S11 tables/hashes; theta_c=0 and beta_c estimated separately for singles/couples. |
| Estimation utility call path | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s10_criterion_a_iid_r100/s10_estimation_lib_v1.py:108–119,155–162`: SinglesObjective/CouplesObjective → `dclaborsupply.data.loader.load_singles/load_couples` → `dclaborsupply.likelihood.engine_jax.build_jax_singles_ll/build_jax_couples_ll`. Active engine file `MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py:303–308,519–530` transforms data.consumption and forms utility; the accepted consumption term is beta_c log(c_norm). |
| Audit utility call path | Same chosen consumption/c_norm and household leisure/age/child shifters → full S11 leisure coefficients → WM.box_cox → beta_c log(C_obs/c_scale)+L_obs → independent WM.R_single_node inversion. No opportunity/proposal/shock term enters the literal calculation. |

This freezes the measured consumption argument for E2; it does not introduce a different normative equivalisation convention.

### Literal references and results

For each selected household, use
\[
m_i(j)=C_i^{obs}\exp\{[L_i(j^{obs})-L_i(j)]/\beta_c\}.
\]
(a) is m_i(o). (b) is an **independent numerical inversion** of the existing WM.R_single_node against u_obs; it does not just assign W4 = W1.

The market universe for (c) is: single market jobs with hours in [5,70], any occupation/wage in structural support; for couples, at least one spouse works, each working spouse has hours in [5,70], and the other spouse may be at home. The neither-work state o is excluded from this **market** universe. No household-specific g, q, epsilon or kappa enters the literal computation. The current L has no wage or occupation term.

For the checked households all leisure coefficients are positive. Each spouse's leisure term strictly falls with their hours; hence the single maximum is 5h and the couples maximum must be among (5,0), (0,5), (5,5). Evaluating all three gives the literal minimum on the full stated continuous market universe, not merely a quadrature approximation. This argument and calculation are confined to the selected households.

Per the user's BASELINE_F1 §2 instruction, household levels are retained **only in the restricted artifact outside the repository** (Appendix A). This report contains pass/fail results, differences and ratios.

| Household | (a)=(b) machine precision | W1-F / C_obs | Worker/nonworker criterion | b − a (EUR/month) | W4 utility residual | Dense M − market Measure 6 | Market Measure 6 / W1-F |
|---|---|---:|---|---:|---:|---:|---:|
| H-S1 (singles) | PASS | 0.6304345043711471 | PASS: worker, 0 < ratio < 1 | 0.000000000000000e+0 | 0 | 0 | 1.009109531428580 |
| H-S2 (singles) | PASS | 1.000000000000000 | PASS: nonworker, ratio = 1 exactly | -5.684341886080801e-14 | 0 | 0 | 1.011420950227280 |
| H-C1 (couples) | PASS | 0.4808435094822490 | PASS: worker, 0 < ratio < 1 | -1.364242052659392e-12 | 0 | 0 | 1.013685498341964 |

The independent W4 inversion has zero utility residual in float64 for all three checks. Differences b−a are within a few floating-point ulps. No household levels are displayed here.

For couple H-C1, the equal-pay equivalent at (5,0) exceeds the minimum by 16.419421020850 EUR/month; at (5,5) the excess is 53.512101589431 EUR/month. The minimum is at **(0,5)**: the woman works 5h; the man is at home. Dense-law M uses that configuration for L(5h), not both spouses at 5h. No sample-wide corner count was calculated.

On the historical singles six-node reference grid {0,20,30,35,39,48}, which includes home, literal Measure 6 / W1-F = **1** for both checked singles. The couples Cartesian extension also gives ratio **1** for the checked couple; it is a deterministic comparison universe, not a claimed implemented couples W6 grid. Stored W6 instead uses a mean of exponentials.

### Stored-versus-literal differences and ratios

S12 baseline state is I00. Both stored singles reference arms agree at baseline for these households. The F4A/F4C pooled keys are 20000_H-S1 and 20000_H-S2, corresponding to source households H-S1 and H-S2 with year_tag=2. This was verified against idorighh in `C:/Users/hisham/MNL/EUROMOD-STORAGE/new_data/fr_p3a_bpool_engine_ready_staged_threeB1__singles.parquet` and F4A:166–178. Full side-by-side levels are restricted; differences below use accepted S11 literal benchmarks.

| Household / artifact | Stored W1 − literal F | Stored W1 / literal F | Stored W4 − literal W4 | Stored W4 / literal W4 | Stored W6 − literal market M6 | Stored W6 / literal market M6 |
|---|---:|---:|---:|---:|---:|---:|
| H-S1 / S12 I00 | 2288.964801511282 | 1.90753836343005 | not persisted per household | not available | NOT IMPLEMENTED | not available |
| H-S2 / S12 I00 | 1910.853416346580 | 5.24217714675763 | not persisted per household | not available | NOT IMPLEMENTED | not available |
| H-C1 / S12 I00 | -747.472252608102 | 0.718738901018888 | not persisted per household | not available | NOT IMPLEMENTED | not available |
| H-S1 / F4A | -894.075335961011 | 0.645513261433511 | 4087855.563274350017 | 1621.77011642249 | NOT IMPLEMENTED | not available |
| H-S1 / F4C | -894.075335961011 | 0.645513261433511 | 46207.524917412527 | 19.3205532535992 | 50434.975293290045 | 20.8161546233874 |
| H-S2 / F4A | 818.768018234541 | 2.81770037708671 | 3718581.844894440845 | 8256.41236486863 | NOT IMPLEMENTED | not available |
| H-S2 / F4C | 818.768018234541 | 2.81770037708671 | 43711.478490793925 | 98.0413708965529 | 48339.319032440726 | 107.103573225910 |
| H-S1 / P2a | -1041.314638162410 | 0.587135205438848 | 5880.958753646906 | 3.33170718883945 | 6190.369568729857 | 3.43222723589166 |
| H-S2 / P2a | 539.493324091835 | 2.19769848943536 | 1631.246538941956 | 4.62143779791214 | 1734.566399913076 | 4.80732903797976 |

Differences are EUR/month and ratios are dimensionless. Historical comparisons include parameter/input-generation differences as well as object definitions; they are not a controlled smoothing-effect estimate. **No stored value is called literal.** Relative to literal Measure 6 on the home-including six-node grid, F4C's W6 gaps are 50457.95106780108 and 48344.46350449004 EUR/month for singles H-S1 and H-S2.

S12 W4 was executed (E3/E7), but its per-household values were not retained in the inspected distribution, JSON summaries, or v5 singles cache. A summary cannot identify a selected household's W4. Couples H-C1 has no stored W4/W6 row in these lineages; F4A/F4C/P2a are singles files. Missing entries remain explicitly unavailable; no rerun or invented value fills them.

## 5. What welfare_identity_check_v1.md verifies

`MNL/docs/corr/welfare_identity_check_v1.md`, §§1–2, verifies the **production J/H identity**, where
\[
\log J=\operatorname{LSE}_j\{L_j+BC(C_j/\lambda_c;\theta_c)+a_j\},\quad
\log H=\operatorname{LSE}_j\{L_j+a_j\},
\]
and
\[
W=\lambda_c[1+\theta_c(\log J-\log H)]^{1/\theta_c}
\quad\text{with }\beta_c=1.
\]
For old couples, theta_c=0, so this is lambda_c exp(log J−log H), equivalently an opportunity-weighted arithmetic consumption mean. Old singles use **theta_c = 0.168019403191226**, beta_c=1; old couples use **theta_c=0**, beta_c=1. The report excludes the chosen anchor from the common quadrature support. It verifies closed form against the inclusive-value evaluator and stored W, not u_obs against the home reference.

**It predates the identified-scale baseline in model/input generation**: its recorded HEAD is 1cf57ddc87544ebef447f594556c35890bd5635e and it uses final S8 singles / R240 couples, superseded by S11 (theta_c=0, beta_c estimated). The identity MD/JSON are untracked in the initial inventory; a precise original authorship date is not inferred from file timestamps. Its numerical agreement is not evidence for an S11 observed-bundle distribution.

**Does any stored artifact hold literal observed-bundle W1-F/W4 for the full sample? NO.** This conclusion covers the traced fastlane F4A/F4C→F5, P2a, M08/U6, final S8/R240, and S12 production lineages and the searched welfare producers. There is no positive path/hash witness. The authoritative checks here cover three households only. The existence of a home inversion function, a J/H identity report, or preference-figure observed bundles is not a stored full-sample literal welfare distribution.

## 6. The 119 couples and the consumption floor

| Question | Finding | Evidence |
|---|---|---|
| (a) Does their nonpositive home consumption enter literal W1-F at the observed bundle? | **No.** F uses positive observed C_obs, L_obs, L(o), beta_c. It never evaluates priced C(o). o is a universally available behavioural state under R1, not an assertion that home is a market job in J. | R1; §4 explicit formula and its argument list; engine utility separation E1. |
| (b) Does the floor enter executed W1-EA / W4? | **Yes in attained utility over the priced node sets.** Those sets include neither-work nodes whose nonpositive consumption was replaced by EUR1. In separable log W1's equal-pay H reference, consumption cancels algebraically; nevertheless the node remains in H's domain, and floor/domain choices affect the inclusive numerator. The home **leisure** reference for W4 does not itself use C(o), but its attained inclusive target does. Unit-mass normalization does not remove this attained-side exposure. | cw_engine_ready_v1.py:110–114; S12:741–747,759–762; premise audit:182–200. |
| (c) Does it matter for counterfactual choice sets? | **Yes.** Whether nonpositive priced nodes are retained with a floor or excluded changes the available positive-consumption domain and potentially choice. R5 must specify that domain and attainment operator. No counterfactual was run here. | Corrected estimation builder:581–589 versus welfare builder:110–114; R5. |

The count refers to the **priced common-support home bundle**, not 119 nonpositive observed bundles. In the accepted estimation builder consumption is not floored; the likelihood uses the positive-domain mask. In the historical welfare builder `MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_couples_welfare/cw_engine_ready_v1.py`:110–114 uses max(consumption_raw, DCM_MIN_POSITIVE). Historical singles flooring is in `MNL/scripts/bpool/harmonise_bpool_engine_ready.py`:106–108. These data-domain floors are distinct from lower bounds used by the equivalent-income solver. No floor sensitivity was recomputed.

## 7. R4 final statement

The R4 correspondence table is §2; its executed classes apply to the stored lineages, not to hypothetical function inputs.

- **W1 — EXECUTED CLASS: DIFFERENT OBJECT. REUSABLE FOR LITERAL: yes**, via the W4 singleton primitive for R1's W1-F; **W1-EA itself: no**.
- **W2 — EXECUTED CLASS: DIFFERENT OBJECT. REUSABLE FOR LITERAL: no.**
- **W3 — EXECUTED CLASS: DIFFERENT OBJECT. REUSABLE FOR LITERAL: no.**
- **W4 — EXECUTED CLASS: DIFFERENT OBJECT. REUSABLE FOR LITERAL: yes**, the home-reference primitive with u_obs, not the unchanged wrapper.
- **W5 — EXECUTED CLASS: DIFFERENT OBJECT. REUSABLE FOR LITERAL: no.**
- **W6 — EXECUTED CLASS: DIFFERENT OBJECT where executed; NOT IMPLEMENTED in F4A/S12. REUSABLE FOR LITERAL: no.**

Needed in revised JMP, without any additional decision: **W1-F primary; W4 as the empirical identity; dense-law M / Measure 6 on the market universe sensitivity; W1-EA retired (DIFFERENT OBJECT); W2/W3/W5: no current ruling requires.** W1-F=W4 is an empirical-domain coincidence under the current preferences and universal behavioural availability of home, not a general Haydar–Maniquet theorem.

## Appendix A. Restricted reproducibility record

Household levels and exact reproduction code are stored only at:

`C:/Users/hisham/MNL/EUROMOD-STORAGE/restricted/measure_map_1r/20260911/household_checks_v1.json`

SHA-256: `5556ee82fa1ad90f67eb60bae2373c912ad172194d24122f7162073446bd8578`.

This path is outside both repositories, under restricted storage. It contains the three-household side-by-side levels, model inputs, historical stored values, source hashes, E2 binding, and exact reproduction code as JSON text. It is not a full-sample welfare artifact.

The checks ran through an in-memory here-string using `MNL/.venv/Scripts/python.exe -B -`. Welfare evaluation selected source_idhh and is_chosen=1 first. Nonworker selection used is_chosen=1, working=0, ordered by source_idhh. W4 used WM.R_single_node in 160-step float64 bisection. No computation was rerun to apply the data-discipline correction.

## Appendix B. Fresh artifact hashes

All SHA-256 entries below were computed from local bytes in this audit. Hashes identify historical artifacts; they do not certify literal correspondence.

| Path | SHA-256 |
|---|---|
| `MNL/scripts/welfare/m08_welfare_measures.py` | `ccb8a2c9ddece225522201d8b667e69530c8c23c90d3f192c6a2523a19c21335` |
| `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.tex` | `d8687d3cfb71ce00f81613286e784c71c0e643721987bebf0d57226afe2a02d1` |
| `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv` | `cee4a136f9ce69753965beaa779753bed59e75972490ebb0f2b6114f790413ab` |
| `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv` | `fc1794b437c74ac4e6ab240aaa7c71b7c38ee21512395a175b38c785a5e061c9` |
| `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_theta_hat_v1.npy` | `8ed736215222265dc2a194df2d77fc92df0707baa21339eb51723b01f49926c9` |
| `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_theta_hat_v1.npy` | `0838f36373eda7b391de671f8fdf14a957b23db37221d8753dbfd1c1581c3570` |
| `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_report_v1.md` | `a715fcd11c77bf589c71907fbaa1d7df00202c5819ddfc5b43fe018b8c307814` |
| `MNL/experiments/JMP_SEMINAR_SPRINT/runs/couples_clean_baseline/r240_step3_parameter_table_v1.csv` | `c4aee66a2adf8b08f1314913b52ee3c2218a7f5c0cd1b9c42f1ec82e4a21cc8c` |
| `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/singles_engine_ready_criterion_a_v1.parquet` | `641ceb0ed47b38111c4bac25deb9dd0d1f5942b931a694cd4cc1cec13d429128` |
| `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/couples_engine_ready_criterion_a_v1.parquet` | `50b8289e97ceef16d767ce5799d9f0a712100c4db051444be630b1a56b34345d` |
| `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/engine_metadata_criterion_a_v1.json` | `709cc8cc604db66484a3eb9e4c52a8123cefc83517294d26bc2cc88169e352d7` |
| `MNL/outputs/welfare/fastlane/singles_measures_F4A_v1.parquet` | `ddfbd867871b69ddcb708862503826c56e7b122e062012f72e1c066272c5782f` |
| `MNL/outputs/welfare/fastlane/singles_measures_F4C_v1.parquet` | `dd163e2ec87b43ca97a5613bd0983fd6de720889d7e34ed0f048b9d71e827a4b` |
| `MNL/outputs/welfare/fastlane/F4C_manifest_v1.json` | `5bd2a37c071a4a3b1adce14540d004a22ccdb0807cfdb2d87366305aaee9de85` |
| `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/s12_principal_welfare_distributions_v1.parquet` | `8205b55dbb65278a40b196111deb0a9c6c3b96c7a9932f7c65d69d64e3814447` |
| `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/s12_w4_premise_audit_v1.json` | `3f65e92655363e3522548a19d76afedd946a730afcd6f725efe44d383cc1e142` |
| `MNL/docs/corr/welfare_identity_check_v1.md` | `159cad6686e9622d4ef23212322858674b291fa5244c152eb31719d12a9b968d` |
| `MNL/docs/corr/welfare_identity_check_v1.json` | `ec2414449f0f105e4e3b2313f64fc6ce5170031b1cf00359c3404ba07326fbb7` |
| `MNL/scripts/bpool/specs/theta_hat_realdata_901_v1.csv` | `c72e92b16170a7dd2dc8ec0b76dc3f522a1fc6d6182a5eba8f8cad34cef76269` |
| `Job_Market_paper/docs/Missions/JMP_current_state_dashboard_v1.md` | `1ffa1500907ada28835dda8f7ac089562dba79c343eb5af51d668283c9ed0479` |
| `MNL/scripts/welfare/configs/theta_hat_p2a_singles2016_v1.csv` | `0684ee52a3c290749c0e9c30c272db1956990a84a6f4a77f328305e91f0d417c` |
| `MNL/outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/attempts/20260825T164802Z_500708_1759e2e09f0941609ea183ae51ea8f20_u6ffn16_U6F_FUNCTIONALS16_DONE/u6f_functionals16_v1.json` | `1a6f586605e05da6b2057a85af7116ffb6b6fd536992ae60be2c4514b96c3a9d` |
| `C:/Users/hisham/MNL/EUROMOD-STORAGE/outputs/welfare/p2a_singles2016/singles_measures_p2a_v1.parquet` | `63d66877a2f832dcc13c6067133137079bffd433e13eee644ce7c3e584014512` |

## Appendix C. Initial dirty-file inventory and end-of-task scope

Initial `git status --porcelain=v1 --untracked-files=all` output, recorded before calculations. The list is repository-relative; spaces and quotation marks are Git's own rendering. No dirty file was reverted or edited.

```text
 M experiments/JMP_SEMINAR_SPRINT/figures/captions/figD06_occupation_isco_and_model.md
 M experiments/JMP_SEMINAR_SPRINT/figures/captions/figD07_observed_wages_annualised.md
 M experiments/JMP_SEMINAR_SPRINT/figures/captions/figD09_resource_components.md
 M experiments/JMP_SEMINAR_SPRINT/figures/figD06_occupation_isco_and_model.csv
 M experiments/JMP_SEMINAR_SPRINT/figures/figD07_observed_wages_annualised.csv
 M experiments/JMP_SEMINAR_SPRINT/figures/figD07_observed_wages_annualised_paper.pdf
 M experiments/JMP_SEMINAR_SPRINT/figures/figD07_observed_wages_annualised_paper.png
 M experiments/JMP_SEMINAR_SPRINT/figures/figD07_observed_wages_annualised_slide.pdf
 M experiments/JMP_SEMINAR_SPRINT/figures/figD07_observed_wages_annualised_slide.png
 M experiments/JMP_SEMINAR_SPRINT/figures/figD09_resource_components.csv
 M experiments/JMP_SEMINAR_SPRINT/figures/figD09_resource_components_paper.pdf
 M experiments/JMP_SEMINAR_SPRINT/figures/figD09_resource_components_paper.png
 M experiments/JMP_SEMINAR_SPRINT/figures/figD09_resource_components_slide.pdf
 M experiments/JMP_SEMINAR_SPRINT/figures/figD09_resource_components_slide.png
 M experiments/JMP_SEMINAR_SPRINT/runs/couples_reprice_target_only/cpl_b_reprice_batched_switch_record_v1.json
 M experiments/JMP_SEMINAR_SPRINT/runs/couples_reprice_target_only/run_couples_reprice_batched_switch_v1.py
 M experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_common_v1.py
 M experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_descriptives_continuous_v1.csv
 M experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_funnel_v1.csv
 M experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_occupation_v1.csv
 M experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_resource_components_v1.csv
 M experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_step1_funnel_v1.json
 M experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_step2_descriptives_v1.json
 M experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/make_fd_figures_v1.py
 M experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/run_fd_step1_funnel_v1.py
 M experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/run_fd_step2_descriptives_v1.py
 M experiments/JMP_SEMINAR_SPRINT/runs/nested_endowments/ne_step1_gate_v1.json
 M experiments/JMP_SEMINAR_SPRINT/runs/nested_endowments/run_ne_step1_gate_v1.py
 M experiments/JMP_SEMINAR_SPRINT/tables/fd_descriptives_continuous_v1.csv
 M experiments/JMP_SEMINAR_SPRINT/tables/fd_descriptives_continuous_v1.md
 M experiments/JMP_SEMINAR_SPRINT/tables/fd_occupation_v1.csv
 M experiments/JMP_SEMINAR_SPRINT/tables/fd_occupation_v1.md
 M experiments/JMP_SEMINAR_SPRINT/tables/fd_resource_components_v1.csv
 M experiments/JMP_SEMINAR_SPRINT/tables/fd_resource_components_v1.md
 M experiments/JMP_SEMINAR_SPRINT/tables/fd_sample_funnel_v1.csv
 M experiments/JMP_SEMINAR_SPRINT/tables/fd_sample_funnel_v1.md
?? "Data/documentation/DOCSILC065 operation 2015 VERSION july2014.pdf"
?? docs/corr/fr2016_drd_field_dictionary_v1.csv
?? docs/corr/fr2016_source_audit_evidence_v1.json
?? docs/corr/fr2016_source_to_estimation_sample_audit_v1.md
?? docs/corr/run_s12_consumption_floor_audit_v1.py
?? docs/corr/s12_consumption_floor_audit_v1.csv
?? docs/corr/s12_consumption_floor_audit_v1.json
?? docs/corr/s12_consumption_floor_audit_v1.md
?? docs/corr/target_integrability_checks_v1.json
?? docs/corr/target_model_and_integrability_v1.md
?? docs/corr/welfare_finite_sum_examples_v1.csv
?? docs/corr/welfare_finite_sum_examples_v1.md
?? docs/corr/welfare_identity_check_v1.json
?? docs/corr/welfare_identity_check_v1.md
?? docs/corr/welfare_integrator_chosen_row_v1.md
?? "docs/jmp_methodology/JMP_sampled_alternatives_criterion_audit_v1 - Copy.md"
?? docs/jmp_methodology/JMP_sampled_alternatives_criterion_audit_v1.md
?? docs/jmp_methodology/evidence/ss34_criterion_audit_v1/README.md
?? docs/jmp_methodology/evidence/ss34_criterion_audit_v1/audit_frame.json
?? docs/jmp_methodology/evidence/ss34_criterion_audit_v1/audit_frame.py
?? docs/jmp_methodology/evidence/ss34_criterion_audit_v1/audit_halton.json
?? docs/jmp_methodology/evidence/ss34_criterion_audit_v1/audit_halton.py
?? docs/jmp_methodology/evidence/ss34_criterion_audit_v1/run_decomp.py
?? docs/jmp_methodology/evidence/ss34_criterion_audit_v1/run_toy.py
?? docs/jmp_methodology/evidence/ss34_criterion_audit_v1/ss34_decomp_results.json
?? docs/jmp_methodology/evidence/ss34_criterion_audit_v1/ss34_toy_results.json
?? docs/jmp_methodology/evidence/ss34_criterion_audit_v1/tables.py
?? docs/jmp_methodology/evidence/ss34_criterion_audit_v1/toy_sampler.py
?? docs/jmp_methodology/evidence/ss34_criterion_audit_v1/toy_world.py
?? experiments/JMP_PS1/education_counts_raw.csv
?? experiments/JMP_PS1/runs/ps1_channelD/_baseline_full_snapshot.parquet
?? experiments/JMP_PS1/runs/ps1_channelD/channelD_reference_profile_v1.parquet
?? experiments/JMP_PS1/runs/ps1_channelD/cs_common_correction_frame_v1.parquet
?? experiments/JMP_PS1/runs/ps1_channelD/cs_common_nodes_v1.parquet
?? experiments/JMP_PS1/runs/ps1_channelD/cs_common_priced_rows_v1.parquet
?? experiments/JMP_PS1/runs/ps1_channelD/cs_common_slotmap_v1.parquet
?? experiments/JMP_PS1/runs/ps1_laneA_fourcell/operator_accounting_v1.json
?? experiments/JMP_PS1/runs/ps1c_fit_suite/calibration_curves.csv
?? experiments/JMP_PS1/runs/ps1c_fit_suite/category_shares.csv
?? experiments/JMP_PS1/runs/ps1c_fit_suite/chosen_prob_deciles.csv
?? experiments/JMP_PS1/runs/ps1c_fit_suite/chosen_rank_deciles.csv
?? experiments/JMP_PS1/runs/ps1c_fit_suite/confusion_long.csv
?? experiments/JMP_PS1/runs/ps1c_fit_suite/cube_top_misallocation.csv
?? experiments/JMP_PS1/runs/ps1c_fit_suite/post_estimation_comparison.html
?? experiments/JMP_PS1/runs/ps1h_couples_p1/ps1h_couples_engine_ready_v1.parquet
?? experiments/JMP_PS1/runs/ps1h_couples_p1/ps1h_couples_frame_v1.parquet
?? experiments/JMP_PS1/runs/ps1h_couples_p1/ps1h_couples_frame_v2.parquet
?? experiments/JMP_PS1/runs/ps1h_couples_p1/ps1h_couples_priced_v1.parquet
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/00_manifest/BUNDLE_MANIFEST_v1.json
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/00_manifest/README_FIRST.md
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/00_manifest/secure_env_protocol_v1.md
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/00_manifest/verify_manifest.py
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_array_inventory_v1.csv
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_bounds_pins_v1.json
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_columns_documentation_v1.md
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_record_v1.json
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_starts_v1.csv
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_terms_v1.json
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_theta_of_record_v1.csv
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/02_estimator/mnl_s8_numpy.py
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/02_estimator/selftest_s8_negll.py
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/bmo_mapping_disclosures_v1.json
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/fap2009_to_loc4_T_v2.csv
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/tension_z_matrix_22x4_v2_full.csv
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/tension_z_matrix_22x4_v2_hc090.csv
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/v2_audit_and_rebuild_v1.json
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/v2_fap_audit_and_map_v1.csv
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/04_join/join_db040f_v1.py
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/05_run/education_inventory_v1.py
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/05_run/export_pack_v1.py
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/05_run/lfs_desired_hours_v1.py
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/05_run/run_r1_estimations_v1.py
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/06_out/.keep
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/06_out/join_diagnostics_v1.json
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/06_out/selftest_v1.json
?? experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/07_export/.keep
?? experiments/JMP_PS1/runs/ps1r1_bmo/source/DARES_FAP2009_intro_et_table_de_correspondance.pdf
?? experiments/JMP_PS1/runs/ps1r1_bmo/source/Matrice_PCS2020_ISCO08.csv
?? experiments/JMP_PS1/runs/ps1r1_bmo/source/Matrice_PCS2020_ISCO08.xlsx
?? experiments/JMP_PS1/runs/ps1r1_bmo/source/ResMetBE16.xlsx
?? experiments/JMP_PS1/runs/ps1r1_bmo/source/ResmetBE15.xls
?? experiments/JMP_PS1/runs/ps1r1_bmo/source/donnees_consolidees_2015.zip
?? experiments/JMP_PS1/runs/ps1r1_bmo/source/donnees_consolidees_2016.zip
?? experiments/JMP_PS1/runs/ps1r1_bmo/source/matrice_P2003_P2020.csv
?? experiments/JMP_PS1/runs/ps1r1_bmo/source/matrice_P2020_P2003.csv
?? experiments/JMP_PS1/runs/ps1r1_bmo/source/table_passage_PCS2003_PCS2020.xlsx
?? experiments/JMP_PS1/runs/ps1s16a_qw_proposal/geometry/ps1s16a_geometry_ARM_HRS_v1.parquet
?? experiments/JMP_PS1/runs/ps1s16a_qw_proposal/geometry/ps1s16a_geometry_ARM_OCC_v1.parquet
?? experiments/JMP_PS1/runs/ps1s16a_qw_proposal/geometry/ps1s16a_geometry_ARM_OCCxHRS_v1.parquet
?? experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_arm_hrs_parameter_table_v1.csv
?? experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_arm_occ_parameter_table_v1.csv
?? experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_arm_occxhrs_parameter_table_v1.csv
?? experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_frozen_parameter_table_v1.csv
?? experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_proposal_fits_v1.json
?? experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_redraw_v1.json
?? experiments/JMP_PS1/runs/ps1s16b_gw_structural/ps1s16b_b_h_parameter_table_v1.csv
?? experiments/JMP_PS1/runs/ps1s16b_gw_structural/ps1s16b_b_nl_parameter_table_v1.csv
?? experiments/JMP_PS1/runs/ps1s8a_acceptance/ps1s8a_hours_grid_v1.csv
?? experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/outputs/figS11_leisure_normalization.csv
?? experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/outputs/figS11_leisure_normalization.pdf
?? experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/outputs/figS11_leisure_normalization.png
?? experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/outputs/figS11_leisure_normalization_caption.txt
?? experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/render_s11_normalization_figure_v1.py
?? experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/run_s11_normalization_figure_v1.py
?? experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/_s2_hours_audit.err
?? experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/s2_hours_5_10_coverage_audit_v1.json
?? no_gsur_setup/requirements.txt
?? no_gsur_setup/setup.ps1
?? outputs/p2a_singles2016/region_live_margqh_floor5_v1/fr_p2a_singles2016_regionlive_margqh_floor5_v1__geometry_meta.json
?? outputs/p2a_singles2016/region_live_margqh_floor5_v1/fr_p2a_singles2016_regionlive_margqh_floor5_v1__mnlmeta.json
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S1/ps1_s1_hours_grid_v1.csv
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S1/ps1_s1_manifest_v1.json
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S1/ps1_s1_parameter_table_v1.csv
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S1/ps1_s1_spec_v1.json
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S2/ps1_s2_hours_grid_v1.csv
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S2/ps1_s2_manifest_v1.json
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S2/ps1_s2_parameter_table_v1.csv
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S2/ps1_s2_spec_v1.json
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S3/ps1_s3_hours_grid_v1.csv
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S3/ps1_s3_manifest_v1.json
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S3/ps1_s3_parameter_table_v1.csv
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S3/ps1_s3_spec_v1.json
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S4/ps1_s4_hours_grid_v1.csv
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S4/ps1_s4_manifest_v1.json
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S4/ps1_s4_parameter_table_v1.csv
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S4/ps1_s4_spec_v1.json
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S6/ps1_s6_hours_grid_v1.csv
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S6/ps1_s6_manifest_v1.json
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S6/ps1_s6_parameter_table_v1.csv
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S6/ps1_s6_spec_v1.json
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S7/ps1_s7_hours_grid_v1.csv
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S7/ps1_s7_manifest_v1.json
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S7/ps1_s7_parameter_table_v1.csv
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S7/ps1_s7_spec_v1.json
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/ps1_battery_part1_manifest_20260829T132034Z.json
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/ps1_model_comparison_part1_20260829T132034Z.csv
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_item2_invariance_v1/ps1_item2_derivation_note_v1.md
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_item2_invariance_v1/ps1_item2_manifest_v1.json
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_item2_invariance_v1/ps1_item2_result_block_v1.md
?? outputs/p2a_singles2016/region_live_margqh_v1/ps1_item2_invariance_v1/ps1_item2_verification_table_v1.csv
?? outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/margqh_v2_20260823T202801Z_262600_80d94f8b9c994b4890d52d4a2ab735df_u6r_smoke/RESTRICTED_DO_NOT_PUBLISH.txt
?? outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/margqh_v2_20260823T202850Z_133812_15108f9f85704ddc81c6729efb88e98b_u6resume2/RESTRICTED_DO_NOT_PUBLISH.txt
?? outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/margqh_v2_20260823T203836Z_194344_736992b537f341aeb18d124f5716f41c_u6resume3/RESTRICTED_DO_NOT_PUBLISH.txt
?? outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/margqh_v2_20260823T213827Z_671796_47f3785e9c8946b48fd41cc09b9f48ed_u6resume4/RESTRICTED_DO_NOT_PUBLISH.txt
?? outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/normalisation_v1_20260818T074210Z_535880_837a2a554a744991b320ffc7ffaf9129_normsmoke/RESTRICTED_DO_NOT_PUBLISH.txt
?? outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/normalisation_v1_20260818T074322Z_686888_47fdba224d9e40f0a61b12e63acd05b8_normsmoke2/RESTRICTED_DO_NOT_PUBLISH.txt
?? outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/normalisation_v1_20260818T074423Z_472652_4f7193670e4542ae8229155aa77e8132_m08normfull/RESTRICTED_DO_NOT_PUBLISH.txt
?? scripts/corr/build_fr2016_source_audit_v1.py
?? scripts/corr/check_target_integrability_v1.py
?? scripts/corr/check_welfare_finite_sum_examples_v1.py
?? scripts/corr/check_welfare_identity_v1.py
?? scripts/ps1/append_s16_model_comparison.py
?? scripts/ps1/ps1_s16_bands.py
?? scripts/ps1/run_ps1_s16a_diag.py
?? scripts/ps1/run_ps1_s16a_price.py
?? scripts/ps1/run_ps1_s16a_qw_proposal.py
?? scripts/ps1/run_ps1_s16b_gw_structural.py

--- Job_Market_paper (preceding entries: MNL) ---
 M "Literature/md_extractions/__bbox_tmp_Bargain et al_2010_\303\242\342\202\254\305\223Making work pay\303\242\342\202\254\302\235 in a rationed labor market.html"
 M beamer/build/verification_v4.json
 M manuscript/JMP_working_paper_for_seminar_v5.aux
 M manuscript/JMP_working_paper_for_seminar_v5.log
 M manuscript/tables/v5/v5_benchmark.csv
 M manuscript/tables/v5/v5_coefficients_preferences.csv
 M manuscript/tables/v5/v5_full_coefficients_singles.csv
 M reports/JMP_research_story_report_v2.html
?? Literature/JMP_core_bibliography.bib
?? Literature/core_papers/aaberge_colombino_2018.md
?? Literature/core_papers/aaberge_colombino_strom_1999.md
?? Literature/core_papers/aaberge_dagsvik_strom_1995.md
?? Literature/core_papers/audoly_et_al_2025.md
?? Literature/core_papers/bargain_et_al_2013.md
?? Literature/core_papers/bargain_et_al_2014.md
?? Literature/core_papers/capeau_decoster_dekkers_2015.md
?? Literature/core_papers/dagsvik_jia_2016.md
?? Literature/core_papers/dagsvik_strom_2006.md
?? Literature/core_papers/decoster_haan_2015.md
?? Literature/core_papers/fleurbaey_maniquet_2006.md
?? Literature/core_papers/fleurbaey_maniquet_2018_jel.md
?? Literature/core_papers/haydar_maniquet_2026_wip.md
?? Literature/core_papers/jacquet_jia_thoresen_2026.md
?? Literature/core_papers/jia_thoresen.md
?? Literature/core_papers/sastre_trannoy_2002.md
?? Literature/core_papers/shorrocks_1982.md
?? Literature/core_papers/shorrocks_2013.md
?? Literature/corpus_index.md
?? Theory_other_project/jobs_and_wellbeing.agent.md
?? Theory_other_project/jobs_and_wellbeing.tex
?? docs/JMP_W1_theory_to_implementation_bridge_v1.md
?? docs/Missions/JMP_welfare_walkthrough_mission_v1.md
?? docs/normative/JMP_W1_fork_ruling_v1.md
?? docs/normative/W1_latent_set_identification_note_v1.md
?? reports/JMP_reference_profiles_v1.csv
?? reports/JMP_reference_profiles_v1.md
?? reports/JMP_reference_profiles_v1.tex
?? reports/JMP_v5_review_and_modular_revision_plan_v1.md
?? reports/figure_modules/v5_labour_market_opportunity_composition/build_figure.py
?? reports/figure_modules/v5_labour_market_opportunity_composition/evidence.md
?? reports/figure_modules/v5_labour_market_opportunity_composition/v5_labour_market_opportunity_composition.csv
?? reports/figure_modules/v5_labour_market_opportunity_composition/v5_labour_market_opportunity_composition.pdf
?? reports/figure_modules/v5_labour_market_opportunity_composition/v5_labour_market_opportunity_composition.png
?? reports/figure_modules/v5_labour_market_opportunity_composition/v5_labour_market_opportunity_composition.tex
?? reports/leisure_curvature_vs_normalizer.pdf
?? reports/leisure_intercept_vs_normalizer.pdf
```

During the audit, before this report was written, two additional **external concurrent** untracked Job_Market_paper files appeared: `docs/normative/fork_derived_numerals_v1.csv` and `docs/normative/scripts/fork_derived_numerals_v1.py`. This task did not create, execute, or use them for parameter provenance. The pre-report MNL status was unchanged. Final verification is recorded below.

Final checks: **PASS** — MNL's full porcelain status is unchanged from the recorded pre-report status, and both top-level HEADs remain the initial HEADs. The only repository addition made by this task is this untracked report. The restricted JSON is outside `C:/Users/hisham/Repo`; its hash matches Appendix A. **PASS** — the report's R4 table has all 13 columns, no trailing whitespace, and the checked household levels/reproduction code have been removed from it. The authorized household-check differences and ratios remain; their levels are restricted. No commit was made. A repository-wide whitespace check encountered pre-existing unrelated dirty artifacts; report-specific formatting checks pass.
