"""Build the V13 decomposition figures from certified records only.

Figures (written to manuscript/figures/v13/, 256-colour palette PNG):
  fig_v13_architecture.png           conceptual map of the decomposition
  fig_v13_att_decomposition.png      attained-bundle Shapley contributions
  fig_v13_ea_decomposition.png       ex-ante Shapley contributions
  fig_v13_central_result.png         access and earnings under both perspectives

Sources, read directly:
  MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_{singles,couples}.csv
  MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_{singles,couples}.csv
  MNL_wea/docs/wea_sprint_1/stage4/stage4_certification_and_results_v1.json

No stored image is reused and nothing is recomputed: the only arithmetic is the
ratio of a Shapley contribution to its own baseline Gini, stated as a derived
value. Every number printed on a figure is written, with its source pointer and
the exact printed text, to reports/v13_figure_values.json.
"""
from __future__ import annotations

import csv
import io
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402
from PIL import Image  # noqa: E402

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
WORKSPACE = ROOT.parent
DECOMP = WORKSPACE / "MNL_decomp/outputs/welfare/preseminar_pab_v1"
WEA = WORKSPACE / "MNL_wea/docs/wea_sprint_1/stage4/stage4_certification_and_results_v1.json"
FIG_DIR = ROOT / "manuscript/figures/v13"
VALUES = ROOT / "reports/v13_figure_values.json"

ACCESS = "Local labour-market access"
ACCESS_DEF = "local unemployment exposure, region, urban or rural location, year"
PREF = "Systematic preferences"
EARN = "Systematic earning opportunities"
COLOURS = {"P": "#5b6f95", "A": "#d0762f", "B": "#3f8f5a"}
SCALES = (("unequivalised", "Raw household"), ("equivalised", "Equivalised"))
POPS = (("singles", "Single-adult households"), ("couples", "Couple households"))

values: dict[str, dict] = {}


def record(key: str, value: float, fmt: str, source: str, units: str) -> str:
    text = format(value, fmt)
    values[key] = {"value": value, "format": fmt, "text": text, "source": source, "units": units}
    return text


def rows(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def save_palette(fig, path: Path) -> None:
    buffer = io.BytesIO()
    fig.savefig(buffer, dpi=170, format="png")
    plt.close(fig)
    image = Image.open(buffer).convert("RGB")
    image.quantize(colors=256, method=Image.Quantize.MEDIANCUT,
                   dither=Image.Dither.NONE).save(path, optimize=True)


def att_inputs() -> dict:
    out = {}
    for pop, _ in POPS:
        shap = rows(DECOMP / f"shapley_PAB_{pop}.csv")
        coal = rows(DECOMP / f"coalition_values_{pop}.csv")
        for scale, _ in SCALES:
            base = next(r for r in coal if r["scale"] == scale and r["coalition"] == "EMPTY")
            phi = {f: float(next(r for r in shap if r["scale"] == scale and r["factor"] == f)
                            ["gini_point_contribution"]) for f in ("P", "A", "B")}
            out[(pop, scale)] = {"baseline": float(base["I_S_gini"]), "phi": phi,
                                 "csv_shapley": f"shapley_PAB_{pop}.csv", "csv_coalition": f"coalition_values_{pop}.csv"}
    return out


def ea_inputs(record_json: dict) -> dict:
    return {(pop, scale): {"baseline": record_json["results"][pop][scale]["gini_EMPTY"],
                           "phi": record_json["results"][pop][scale]["phi"]}
            for pop, _ in POPS for scale, _ in SCALES}


def architecture() -> None:
    fig, ax = plt.subplots(figsize=(13.5, 6.6))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis("off")

    def box(x, y, w, h, text, face, edge="#3b4a54", style="-", weight="normal", size=10.5, hatch=None):
        patch = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.4,rounding_size=1.2",
                               linewidth=1.4, facecolor=face, edgecolor=edge, linestyle=style, hatch=hatch)
        ax.add_patch(patch)
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=size,
                weight=weight, wrap=True, color="#17252b")

    def arrow(x0, y0, x1, y1, style="-"):
        ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=14,
                                     linewidth=1.3, color="#3b4a54", linestyle=style))

    box(1, 44, 21, 10, "Systematic preferences\n(age profiles; child-related\nshifter for women)", "#dde3ef")
    box(1, 27, 21, 13, "Local labour-market access\n(local unemployment exposure,\nregion, urban or rural\nlocation, year)", "#f6e1d0")
    box(1, 12, 21, 10, "Systematic earning\nopportunities (education- and\nexperience-related wage offers)", "#d9ecdf")
    ax.text(11.5, 57.5, "Channels that can be equalised", ha="center", fontsize=11, weight="bold")

    box(28, 27, 17, 13, "Coalition S:\nequalise the chosen\nchannels to a common\nreference profile", "#ffffff")
    for y in (49, 33.5, 17):
        arrow(22.6, y, 27.5, 33.5)

    box(28, 2, 17, 12, "HELD FIXED\nhousehold resources,\nneeds and composition", "#eeeeee",
        edge="#7a7a7a", style="--", weight="bold", hatch="//")
    arrow(36.5, 14.6, 36.5, 26.4, style="--")

    box(50, 27, 15, 13, "Counterfactual\nhousehold\n(estimated coefficients\nunchanged)", "#ffffff")
    arrow(45.6, 33.5, 49.5, 33.5)

    box(70, 43, 13, 11, "ATT: counterfactual\nattained bundle", "#fbf3e6")
    box(70, 13, 13, 11, "EA: counterfactual\nopportunity prospect", "#e8f1f7")
    arrow(65.6, 36, 69.5, 48)
    arrow(65.6, 31, 69.5, 18.5)
    box(86, 43, 13, 11, "Attained-bundle\nmoney-metric\nwell-being", "#fbf3e6")
    box(86, 13, 13, 11, "Ex-ante\nmoney-metric\nwell-being", "#e8f1f7")
    arrow(83.6, 48.5, 85.5, 48.5)
    arrow(83.6, 18.5, 85.5, 18.5)

    ax.text(92.5, 38.5, "Household-weighted Gini I(S)\nfor each perspective and scale",
            ha="center", va="center", fontsize=10)
    ax.text(92.5, 30.5, "Repeat for all 8 coalitions,\nthen Shapley allocation:\naverage over all 3! orders",
            ha="center", va="center", fontsize=10, weight="bold")
    arrow(92.5, 42.4, 92.5, 40.6)
    arrow(92.5, 24.6, 92.5, 26.4)
    fig.tight_layout()
    save_palette(fig, FIG_DIR / "fig_v13_architecture.png")


def decomposition(inputs: dict, perspective: str, name: str, source_of, preliminary: bool,
                  digits: int, status_line: str) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 7.0), sharey=False)
    for ax, (pop, pop_label) in zip(axes, POPS):
        baseline_texts = []
        for offset, (scale, scale_label) in zip((-0.19, 0.19), SCALES):
            data = inputs[(pop, scale)]
            base_text = record(f"{perspective}_{pop}_{scale}_baseline_gini", data["baseline"], ".4f",
                               source_of(pop, scale, "baseline"), "Gini")
            baseline_texts.append(f"{scale_label.lower()} {base_text}")
            for i, factor in enumerate(("P", "A", "B")):
                value = data["phi"][factor]
                text = record(f"{perspective}_{pop}_{scale}_phi_{factor.lower()}", value, f"+.{digits}f",
                              source_of(pop, scale, factor), "Gini points")
                bar = ax.bar(i + offset, value, width=0.36, color=COLOURS[factor],
                             alpha=1.0 if scale == "unequivalised" else 0.55,
                             edgecolor="#17252b", linewidth=0.6,
                             hatch=None if scale == "unequivalised" else "..")
                ax.annotate(text, (i + offset, value), xytext=(0, 3 if value >= 0 else -11),
                            textcoords="offset points", ha="center", fontsize=8.5)
        ax.axhline(0, color="#17252b", linewidth=0.8)
        ax.set_xticks(range(3))
        ax.set_xticklabels(["Systematic\npreferences",
                            "Local labour-market access\n(local unemployment exposure,\nregion, urban or rural\nlocation, year)",
                            "Systematic earning\nopportunities"], fontsize=8.8)
        ax.set_title(f"{pop_label}\nbaseline Gini: {baseline_texts[0]}; {baseline_texts[1]}", fontsize=10.5)
        ax.set_ylabel("Shapley contribution, Gini points")
        ax.spines[["top", "right"]].set_visible(False)
        if pop == "couples" or perspective == "att":
            p_raw, p_eq = inputs[(pop, "unequivalised")]["phi"]["P"], inputs[(pop, "equivalised")]["phi"]["P"]
            if (p_raw > 0) != (p_eq > 0):
                ax.text(0, ax.get_ylim()[1] * 0.92, "Preference contribution\nchanges sign with\nequivalisation",
                        ha="center", va="top", fontsize=8.5, color="#5b3a8a")
    handles = [plt.Rectangle((0, 0), 1, 1, facecolor="#9aa6b2", edgecolor="#17252b"),
               plt.Rectangle((0, 0), 1, 1, facecolor="#9aa6b2", alpha=0.55, hatch="..", edgecolor="#17252b")]
    fig.legend(handles, ["Raw household", "Equivalised"], loc="upper right", frameon=False, fontsize=9.5)
    badge = "PRELIMINARY. " if preliminary else ""
    fig.text(0.01, 0.015, badge + status_line + " Household resources, needs and composition are held fixed; "
             "contributions are signed and are not causal effects.", fontsize=9, color="#8a2d1f" if preliminary else "#17252b")
    fig.tight_layout(rect=(0, 0.05, 1, 0.97))
    save_palette(fig, FIG_DIR / name)


def central(att: dict, ea: dict, record_json: dict) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(13.5, 8.6), sharey="row")
    for r, (pop, pop_label) in enumerate(POPS):
        for c, (scale, scale_label) in enumerate(SCALES):
            ax = axes[r, c]
            groups = (("att", "Attained-bundle\nwelfare (ATT)", att[(pop, scale)],
                       f"comparison_W1F.{pop}.{scale}.W1F_phi.{{f}} / W1F_gini_EMPTY"),
                      ("ea", "Ex-ante\nwelfare (EA)", ea[(pop, scale)],
                       f"results.{pop}.{scale}.phi.{{f}} / gini_EMPTY"))
            orderings = []
            for g, (tag, label, data, pointer) in enumerate(groups):
                for k, factor in enumerate(("A", "B")):
                    share = 100 * data["phi"][factor] / data["baseline"]
                    text = record(f"central_{tag}_{pop}_{scale}_{factor.lower()}_pct_baseline", share, ".1f",
                                  "derived " + str(WEA.relative_to(WORKSPACE)).replace("\\", "/") + "::"
                                  + pointer.format(f=factor) + " * 100", "percent of own baseline Gini")
                    x = g + (k - 0.5) * 0.36
                    ax.bar(x, share, width=0.34, color=COLOURS[factor], edgecolor="#17252b", linewidth=0.6)
                    ax.annotate(text + "%", (x, share), xytext=(0, 3), textcoords="offset points",
                                ha="center", fontsize=9)
                orderings.append("access > earnings" if data["phi"]["A"] > data["phi"]["B"] else "earnings > access")
            ax.set_xticks([0, 1])
            ax.set_xticklabels([groups[0][1], groups[1][1]], fontsize=9.5)
            ax.spines[["top", "right"]].set_visible(False)
            verdict = ("REVERSAL: " if orderings[0] != orderings[1] else "No reversal: ") + \
                f"ATT {orderings[0]}; EA {orderings[1]}"
            ax.set_title(f"{pop_label}, {scale_label.lower()}\n{verdict}", fontsize=10.5,
                         color="#8a2d1f" if orderings[0] != orderings[1] else "#17252b")
            if c == 0:
                ax.set_ylabel("% of own baseline Gini")
    handles = [plt.Rectangle((0, 0), 1, 1, facecolor=COLOURS["A"]), plt.Rectangle((0, 0), 1, 1, facecolor=COLOURS["B"])]
    fig.legend(handles, [f"{ACCESS} ({ACCESS_DEF})", EARN], loc="upper center", ncol=2, frameon=False, fontsize=10)
    fig.text(0.01, 0.012, "Same operators and allocation rule under both perspectives; household resources, needs and "
             "composition held fixed.\nThe attained-bundle counterfactual is preliminary; the ex-ante calculation "
             "passed its numerical checks. Neither perspective is designated primary.", fontsize=9)
    fig.tight_layout(rect=(0, 0.05, 1, 0.95))
    save_palette(fig, FIG_DIR / "fig_v13_central_result.png")


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    record_json = json.loads(WEA.read_text(encoding="utf-8"))
    att = att_inputs()
    ea = ea_inputs(record_json)
    for (pop, scale), data in att.items():
        certified = record_json["comparison_W1F"][pop][scale]
        if abs(certified["W1F_gini_EMPTY"] - data["baseline"]) > 1e-12 or any(
                abs(certified["W1F_phi"][f] - data["phi"][f]) > 1e-12 for f in ("P", "A", "B")):
            raise SystemExit(f"attained-bundle CSV disagrees with the certified comparison record: {pop} {scale}")

    decomp_rel = str(DECOMP.relative_to(WORKSPACE)).replace("\\", "/")
    wea_rel = str(WEA.relative_to(WORKSPACE)).replace("\\", "/")

    def att_source(pop, scale, what):
        if what == "baseline":
            return f"{decomp_rel}/coalition_values_{pop}.csv::scale={scale},coalition=EMPTY,I_S_gini"
        return f"{decomp_rel}/shapley_PAB_{pop}.csv::scale={scale},factor={what},gini_point_contribution"

    def ea_source(pop, scale, what):
        if what == "baseline":
            return f"{wea_rel}::results.{pop}.{scale}.gini_EMPTY"
        return f"{wea_rel}::results.{pop}.{scale}.phi.{what}"

    architecture()
    decomposition(att, "att", "fig_v13_att_decomposition.png", att_source, True, 4,
                  "Attained-bundle welfare, exact Shapley allocation of the change in the Gini.")
    decomposition(ea, "ea", "fig_v13_ea_decomposition.png", ea_source, False, 4,
                  "Ex-ante welfare, exact Shapley allocation; the calculation passed its numerical checks.")
    att_certified = {(pop, scale): {"baseline": record_json["comparison_W1F"][pop][scale]["W1F_gini_EMPTY"],
                                    "phi": record_json["comparison_W1F"][pop][scale]["W1F_phi"]}
                     for pop, _ in POPS for scale, _ in SCALES}
    central(att_certified, ea, record_json)
    VALUES.write_text(json.dumps({"figures": sorted(p.name for p in FIG_DIR.glob("fig_v13_*.png")),
                                  "values": values}, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {len(values)} source-bound figure values and 4 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
