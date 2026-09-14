#!/usr/bin/env python
"""Static release checks for the current-results gallery."""
from __future__ import annotations
import ast
import base64
import html as html_lib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import retired_lineage_gate as rlg  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "reports/JMP_results_gallery_current.html"
NOR = ROOT / "reports/numbers_of_record_v5.json"
BUILD = Path(__file__).resolve().parent / "build.py"
DECOMP_FIGURE_BUILD = (ROOT.parent / "MNL_decomp/scripts/welfare/"
                       "run_preseminar_pab_decomposition_v1.py")
DECOMP_FIGURES = [
    ROOT.parent / "MNL_decomp/outputs/welfare/preseminar_pab_v1" / name
    for name in (
        "fig_preseminar_pab_architecture_v1.png",
        "fig_preseminar_pab_decomposition_singles_v1.png",
        "fig_preseminar_pab_decomposition_couples_v1.png",
    )
]

text = P.read_text(encoding="utf-8")
without_data = re.sub(r'data:image/png;base64,[A-Za-z0-9+/=]+', 'data:image/png;base64,…', text)
plain = re.sub(r"\s+", " ", html_lib.unescape(re.sub(r"<[^>]+>", " ", without_data))).strip()
nor = json.loads(NOR.read_text(encoding="utf-8"))
build_source = BUILD.read_text(encoding="utf-8")
build_executable = "\n".join(
    "" if line.lstrip().startswith("#") else line for line in build_source.splitlines()
)
gallery_registry = json.dumps(nor.get("gallery", {}), ensure_ascii=False, sort_keys=True)
decomp_figure_source = DECOMP_FIGURE_BUILD.read_text(encoding="utf-8")
decomp_literal_values = {}
for node in ast.parse(decomp_figure_source).body:
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id in {
                    "A_DEFINITION_NOTE", "DELTA_I_NOTE", "DELTA_I_NOTE_PLOT"}:
                decomp_literal_values[target.id] = ast.literal_eval(node.value)
decomp_figure_language = " ".join(decomp_literal_values.values())
generator_inputs = (("builder", build_executable),
                    ("gallery registry", gallery_registry),
                    ("DECOMP figure generator", decomp_figure_source))
checks = {}
checks["self_contained"] = "data:image/png;base64," in text and not re.search(r'<(?:img|script|link)[^>]+(?:src|href)=["\'](?!data:|#)', text)
checks["nine_sections"] = len(re.findall(r'<section id=', text)) == 9
figure_count = len(re.findall(r'<figure(?:\s|>)', text))
figcaption_count = len(re.findall(r'<figcaption(?:\s|>)', text))
standalone_count = text.count("<figcaption class=standalone>")
checks["captions_complete"] = figure_count + standalone_count == figcaption_count
checks["current_samples"] = f'{int(nor["entries"]["n_singles"]["value"]):,}' in text and f'{int(nor["entries"]["n_couples"]["value"]):,}' in text
forbidden = [r"[A-Fa-f0-9]{32,}", r"(?:[A-Za-z]:\\|\.\./|/runs/|/figures/)", r"\bR-\d+\b", r"\b(?:S11|S12|PRICE-D)\b", r"mission"]
checks["no_internal_paths_hashes_labels"] = not any(re.search(p, without_data) for p in forbidden)
# The retired four-factor decomposition kept an RQMC integration band and a
# CR1 parameter interval visually separate and explicitly "never merged".
# The current preliminary three-factor decomposition (DECOMP-2) instead
# reports two different uncertainty summaries -- a Monte Carlo range across
# simulation replications, and an independent second-seed check -- and the
# analogous guarantee is that neither is ever presented as a confidence
# interval.
checks["intervals_separate"] = ("MC range (min" in text and "Second-seed" in text
                                 and "never confidence intervals" in text)
headlines = " ".join(re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', without_data,
                                re.IGNORECASE | re.DOTALL))
checks["no_mae_headline"] = (
    "mean absolute error" not in headlines.lower()
    and not re.search(r'\bMAE\b', headlines)
)
checks["final_diagnostic_surface"] = all(x in plain for x in (
    "Extensive margin: observed work status by hard prediction",
    "Joint hours-state: observed state by unconditional modal state",
    "Conditional intensive margin: workers only",
    "Observed-state probability, scores, calibration, and simulated benchmark",
    "predictive/integration-node convergence",
    "Analytical reparameterisation (zero re-estimation)",
    "Independent re-estimation",
))
final_diag_match = re.search(
    r'<section id="final-diagnostics">(.*?)</section>', without_data,
    re.IGNORECASE | re.DOTALL,
)
final_diag_html = final_diag_match.group(1) if final_diag_match else ""
checks["node_language_exact"] = (
    "predictive/integration-node convergence" in plain
    and "observed participation is the dashed reference line" in plain
    and "posterior draw" not in final_diag_html.lower()
    and "confidence interval" not in final_diag_html.lower()
)
checks["registry_present"] = "gallery" in nor and bool(nor["gallery"].get("coefficients"))

# M1-GALLERY source-path gate. These are the actual retired inputs and figure
# assets, so this checks the executable builder and its gallery registry rather
# than relying on prose that can be renamed. The shared registry has other
# consumers; only its gallery subtree is an input to this build.
retired_source_paths = {
    "retired welfare-summary source": r"s12_principal_welfare_summary_v1\.csv",
    "retired W4 source": r"s12_w4_premise_audit_v1\.json",
    "retired welfare-distribution figure": r"figV02_welfare_distributions",
    "retired welfare-Lorenz figure": r"figV01_welfare_lorenz",
    "retired power-mean figure": r"figP07_w1_power_mean_weighting",
    "retired welfare source directory": r"s12_welfare_record",
    "mixed worked-example welfare source": r"v5_step4_worked_examples_v1\.json",
}
source_path_hits = []
for source_name, source_text in (("builder", build_executable),
                                 ("gallery registry", gallery_registry)):
    for label, pattern in retired_source_paths.items():
        if re.search(pattern, source_text, re.IGNORECASE):
            source_path_hits.append(f"{source_name}: {label}")
checks["no_retired_welfare_generator_paths"] = not source_path_hits

# Content-signature gates cover retired constructions that have no unique
# source file. They run on both visible output and generator inputs. Short
# state labels are scanned only after removing opaque base64 image payloads,
# where random byte encodings are not live text.
retired_signatures = {
    "W1-EA": r"\bW1-EA\b",
    "power-mean welfare": r"\bpower[- ]mean\b|sum_r\s+r_ir\s+C_ir\^beta_c",
    "proposal q as welfare primitive": (
        r"q\s*\^\s*W|-\s*log\s+q|common-proposal|"
        r"proposal.{0,180}(?:welfare|money metric|J and H)|"
        r"(?:welfare|money metric).{0,180}proposal"
    ),
    "one-euro welfare floor": (
        r"one[- ]euro.{0,100}floor|floor.{0,140}"
        r"(?:welfare|simulated nodes|utility evaluation)"
    ),
    "retired I-state labels": r"\bI(?:00|10|01|11)\b",
    "J/H construction": r"\bboth J and H\b|\bJ/H construction\b|q\s*\^\s*W",
    "old W4/W1 comparison": r"\bW4\s*/\s*W1\b|\bW4 comparison\b|\bMedian W4\b",
}
signature_hits = []
for source_name, source_text in (("rendered HTML", plain), *generator_inputs):
    for label, pattern in retired_signatures.items():
        if re.search(pattern, source_text, re.IGNORECASE | re.DOTALL):
            signature_hits.append(f"{source_name}: {label}")
checks["zero_retired_welfare_content_signatures"] = not signature_hits

four_factor_hits = []
for source_name, source_text in (("rendered HTML", plain), *generator_inputs):
    for hit in rlg.scan_four_factor(source_text):
        four_factor_hits.append(f"{source_name}: {hit}")
checks["no_four_factor_decomposition"] = not four_factor_hits

welfare_match = re.search(r'<section id="welfare">(.*?)</section>', without_data,
                          re.IGNORECASE | re.DOTALL)
welfare_html = welfare_match.group(1) if welfare_match else ""
welfare_plain = re.sub(r"\s+", " ", html_lib.unescape(
    re.sub(r"<[^>]+>", " ", welfare_html))).strip()
accepted_formula = "W1_F_i = C_obs_i * exp{[L_i(j_obs) - L_i(o)] / beta_c}"
welfare_reference = (
    "The money metric is derived from the Measure-1 reference-set principle. "
    "Under the current empirical specification its direct reference collapses "
    "to the universally available non-employment state; opportunity heterogeneity "
    "therefore affects the current welfare measure through attained bundles."
)
variance_language = (
    "Dispersion in consumption is quantitatively large relative to dispersion in "
    "log well-being: Var(log C) is roughly 100–127% of Var(log W), with the excess "
    "offset by a large negative covariance between consumption and the leisure "
    "valuation. DECOMP-2 holds household resources, needs and composition fixed, "
    "leaving important sources of dispersion outside the P/A/B allocation."
)
checks["section06_accepted_formula"] = accepted_formula in welfare_plain
checks["section06_only_accepted_construction"] = (
    bool(welfare_match)
    and welfare_plain.count(accepted_formula) == 1
    and not any(re.search(pattern, welfare_plain, re.IGNORECASE | re.DOTALL)
                for pattern in retired_signatures.values())
)
checks["welfare_reference_summary_M7"] = welfare_reference in welfare_plain
checks["welfare_worked_example_M8"] = all(x in welfare_plain for x in (
    "For a one-nat shortfall,", "Current nonworkers: W=C.",
    "Current workers: W<C under the maintained empirical domain.",
)) and "exp(\u22121/beta_c) < C_obs" in welfare_plain
checks["variance_language_M4"] = variance_language in plain
checks["access_definition_M5"] = (
    "A = local geographic/temporal access shifters (region, urban/rural, year)" in plain
    and "local labour-market access" not in plain.lower()
)
checks["decomp_figure_language_M4_M5"] = (
    variance_language in decomp_figure_language
    and "A = local geographic/temporal access shifters (region, urban/rural, year)"
        in decomp_figure_language
    and "local labour-market access" not in decomp_figure_source.lower()
)
checks["decomp_figures_embedded_from_current_inputs"] = all(
    f.exists() and base64.b64encode(f.read_bytes()).decode("ascii") in text
    for f in DECOMP_FIGURES
)

# LINEAGE-SWEEP-1: path-based, not string-based -- scans the build script and
# the rendered HTML for a READ of a retired welfare-decomposition artifact by
# its own filename, independent of how the surrounding prose is worded.
_lineage_violations = rlg.scan_files([BUILD, P])
checks["no_retired_lineage_path_reads"] = not _lineage_violations
if _lineage_violations:
    print(rlg.format_violations(_lineage_violations, ROOT))
if source_path_hits:
    print("retired welfare generator path hit(s): " + "; ".join(source_path_hits))
if signature_hits:
    print("retired welfare content-signature hit(s): " + "; ".join(signature_hits))
if four_factor_hits:
    print("four-factor content-signature hit(s): " + "; ".join(four_factor_hits))
failed = [k for k,v in checks.items() if not v]
for k,v in checks.items(): print(f'{"PASS" if v else "FAIL"}: {k}')
if failed: raise SystemExit("failed: " + ", ".join(failed))
