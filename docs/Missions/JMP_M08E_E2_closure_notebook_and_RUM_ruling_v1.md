DEPUTY DECISIONS — THIS MESSAGE SUPERSEDES THE EARLIER
RESULTS-PREVIEW-NOTEBOOK INSTRUCTION

Use the attached
FR_P2a_m08e_codex_reverification_v1.md
as the evidence basis.

The final artifacts are already in the M08E workspace. Do not ask the
PI to upload duplicate copies unless repository/workspace access
actually fails.

FINAL E3 MANIFEST:
C:\Users\hisham\Repo\MNL\outputs\p2a_singles2016\region_live_margqh_v1\e3_estimation_v2\attempts\20260819T214600Z_672360_410223ff1ccd4d12b85d48b36d60fb1e_margqh_v2_phase3equiv_tightened_E3_CONVERGED_SINGLE_OPTIMUM\e3_manifest.json

FINAL E4 MANIFEST:
C:\Users\hisham\Repo\MNL\outputs\p2a_singles2016\region_live_margqh_v1\e4_curvature_inference_v2\attempts\20260819T214723Z_763848_8304bf6f33d94beba38b05a498049d01_margqh_v2_p4p5equiv_E4_PASS\e4_manifest.json

FINAL NOTE FILENAMES:
FR_P2a_m08e_E3_reestimation_note_v2.md
FR_P2a_m08e_E4_curvature_inference_note_v2.md

AUTHENTICATED CONVERSION WORKSPACE:
C:\Users\hisham\AppData\Local\Temp\48\claude\c--Users-hisham-Repo-MNL\710215fa-6909-4394-acde-35df3766da59\scratchpad


1. M08E E2 CLOSURE

Authorize one bounded correction of R1 and R5.

R1 must be closed completely:

- remove the unverified public resolve() route, or make every public
  path accessor perform full hash verification before returning;
- replace split verify()+resolve() production calls with
  verified_path();
- move all pinned executable imports below successful pin
  verification;
- include every consumed convention document or module in the pin
  gate, or remove it from the executed dependency set;
- rerun the tampered-copy, missing-file, PENDING-path, PENDING-hash,
  unknown-key, and pre-gate-consumption probes.

R5:

- correct the E3 note so that it states that five E3 v2 attempt
  directories exist;
- use the actual classifications of the five directories;
- do not alter any numerical artifact, manifest, estimate, curvature
  result, or inference result.

Then commission one final fresh GPT-5.6 Codex read-only verification
of R1 and R5 only.

No re-estimation, curvature rerun, inference rerun, EUROMOD execution,
or reopening of R2/R3/R4/R6.

On ACCEPT, accept the corrected marginal/MIS RURO baseline and
continue autonomously.


2. WORKING SELF-CONTAINED NOTEBOOK — START NOW

Create:

MNL/notebooks/france/fr_singles_pipeline_v3_working.ipynb

Do not create:
MNL/notebooks/france/fr_singles_results_preview_v1.ipynb

Do not edit:
dclaborsupply-monorepo/notebooks/fr_singles_pipeline_v2.ipynb

The new v3 working notebook is the active, self-contained empirical
notebook. It must begin with data loading and cleaning and contain the
complete executable sequence:

data loading
-> data cleaning
-> sample restrictions and sample-flow table
-> France 2016 singles P2a construction
-> descriptives
-> alternative construction
-> pricing
-> common-opportunity RUM estimation
-> corrected marginal/MIS RURO estimation
-> curvature and inference
-> observed disposable-income inequality
-> W1-W6 welfare measurement
-> RUM-versus-RURO welfare comparison
-> RURO access/ability/preference decomposition
-> S-10
-> LOC4

“Self-contained” means that every section contains the executable call
that generates its object. It may call tested MNL or dclaborsupply
functions; it must not duplicate the full production implementation
inside notebook cells.

Expensive stages must have switches. When a switch is false, the same
section may load a hash-verified accepted checkpoint.

Required controls include:

RUN_DATA_CLEANING = True
RUN_SAMPLE_BUILD = True
RUN_ALTERNATIVE_BUILD = False
RUN_EUROMOD_PRICING = False
RUN_RUM_ESTIMATION = False
RUN_RURO_ESTIMATION = False
RUN_INFERENCE = False
RUN_WELFARE = False
RUN_DECOMPOSITION = False

The first executed notebook version must already produce:

- a progress and remaining-work dashboard;
- raw-data and variable-source inventory;
- complete sample-flow table;
- weighted and unweighted sample descriptives;
- final 1,555-household P2a sample composition;
- sex, education, employment, hours, wage, occupation, region and
  disposable-income descriptives;
- weighted observed-disposable-income inequality;
- weighted and unweighted Gini;
- weighted mean and median;
- p10, p25, p75 and p90;
- P90/P10 and P50/P10;
- CV-squared;
- domain-valid Theil-T, Theil-L and Atkinson indices;
- Lorenz curve;
- historical accepted joint-convention RURO estimation results;
- corrected marginal/MIS RURO candidate results;
- parameter and inference comparison between the two conventions.

Use dwt for population-facing statistics and report unweighted
household counts alongside them.

Do not call observed-income inequality “welfare inequality without
opportunities.” Label it:

OBSERVED DISPOSABLE-INCOME INEQUALITY — DESCRIPTIVE BENCHMARK

Use these status labels:

ACCEPTED_HISTORICAL
CANDIDATE_PENDING_R1_R5_CLOSURE
CURRENT_DESCRIPTIVE
NOT_YET_AVAILABLE

After the final R1/R5 ACCEPT, update the corrected RURO status to
ACCEPTED_CURRENT_BASELINE.

Run no new EUROMOD, welfare integration, or decomposition merely to
populate the first notebook version.

The notebook may write only aggregate development outputs under:

outputs/p2a_singles2016/notebook_dev_v3/

Before committing an executed notebook, scan it for household
identifiers and household-level displayed tables.


3. RUM VERSUS RURO BENCHMARK

The earlier W1/W4/W6 Ginis are superseded RURO-pipeline development
results. They are not a conventional RUM benchmark and must not be
used as the main RUM-versus-RURO comparison.

Design a proper common-opportunity RUM benchmark using the same:

- France 2016 singles sample;
- job-package support;
- EUROMOD disposable-income mapping;
- corrected marginal/MIS proposal convention;
- utility family;
- non-employment treatment;
- estimation and inference standards.

Replace heterogeneous household opportunity objects with one frozen
common opportunity measure and re-estimate the preference parameters.

Do not create the benchmark by setting g=1 while retaining the RURO
theta.

Commission and freeze the exact RUM estimand and common opportunity
measure now. Execute the RUM estimation only after final R1/R5 ACCEPT.

The eventual notebook and manuscript comparison must show:

- observed disposable-income inequality;
- common-opportunity RUM welfare inequality;
- corrected RURO welfare inequality;
- W1-W6 normative measure spread;
- welfare rank correlation between RUM and RURO;
- welfare-decile movements;
- corrected RURO access/ability/preference decomposition.


4. CORRECTED S-10 SET

The corrected W-4 diagnostic supersedes the historical coordinate set.

Mandatory coordinates:

beta_l0_sm
beta_l0_sf
beta_l_nkids_sf

Run exactly five Tier-1 scenarios later:

1. corrected baseline;
2. beta_l0_sm perturbed alone;
3. beta_l0_sf perturbed alone;
4. beta_l_nkids_sf perturbed alone;
5. all three perturbed jointly.

beta_w_pexp2 is removed from the mandatory corrected-baseline S-10
set.

Use the existing admissible perturbation rule and materiality
thresholds unless a coordinate’s relevant boundary direction differs,
in which case use the direction recorded by the corrected W-4
artifact.


5. ROUTING AND RETURN

Manage the E2 closure, notebook construction and RUM-design freeze
autonomously.

Every delegated action card must state exactly which files or
repository paths are provided to the recipient.

Return to the deputy only on:

- a valid final R1/R5 REJECT;
- an undefined or scientifically incoherent RUM benchmark estimand;
- a notebook disclosure problem;
- a generic package change required by Goal 1;
- or another existing M08 halt condition.