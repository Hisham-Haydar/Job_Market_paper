"""Build the R7 slide-native fit and kernel figures."""
from pathlib import Path
import importlib.util
import json

import matplotlib.pyplot as plt
import numpy as np


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("slide_figures_r6_base",
                                              HERE / "make_slide_figures_r6.py")
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
base.POSFIT = HERE.parents[1] / "MNL_posfit/outputs/positive_fit_diagnostics_v3b"
base.OUT = HERE / "figures/r7"
original_finish = base.finish


def finish_v7(fig, name):
    original_finish(fig, name.replace("_r6", "_r7"))


base.finish = finish_v7
manifest = {}
base.calibration(manifest)
base.fitext(manifest)
base.kernel(manifest, base.ACCESS_BLOCK, "kernelacc_r7", base.ACC,
            "single-adult estimates, log access index; bars are 1.96 x CR1 robust s.e.")
base.kernel(manifest, base.WAGE_BLOCK, "kernelwage_r7", base.EARN,
            "single-adult estimates, log wage-offer density; bars are 1.96 x CR1 robust s.e.")

corrected_path = (HERE.parents[1] / "MNL_posfit/experiments/JMP_SEMINAR_SPRINT/"
                  "runs/bandfix2_recompute/new_results_v1.json")
corrected = json.loads(corrected_path.read_text(encoding="utf-8"))
rows = [row for row in corrected["moments"]
        if row["model"] in ("SINGLES", "COUPLES")
        and row["moment"] == "hours::h_36_5_37_5"]
order = [("singles", "male"), ("singles", "female"),
         ("couples", "male"), ("couples", "female")]
by = {(row["sample"], row["sex"]): row for row in rows}
labels = ["single men", "single women", "coupled men", "coupled women"]
observed = np.array([100 * by[key]["observed"] for key in order])
predicted = np.array([100 * by[key]["predicted"] for key in order])
x = np.arange(4)
fig, ax = plt.subplots(figsize=(13, 5.5))
width = .34
ax.bar(x - width/2, observed, width, color=base.DEEPRED, label="observed")
ax.bar(x + width/2, predicted, width, color=base.ACC, label="predicted")
for index, (obs, pred) in enumerate(zip(observed, predicted)):
    ax.text(index, max(obs, pred) + .25, f"gap {obs-pred:.1f} pp",
            ha="center", fontsize=15)
ax.set_xticks(x, labels)
ax.set_ylabel("share at the observed 37-hour mass point (%)")
ax.set_title("37-hour mass point: observed and corrected prediction")
ax.legend(frameon=False)
ax.grid(axis="y", alpha=.22)
for side in ("top", "right", "left"):
    ax.spines[side].set_visible(False)
finish_v7(fig, "hours37_r7")
manifest["bandfix2_recompute/new_results_v1.json"] = base.sha256(corrected_path)
base.OUT.mkdir(parents=True, exist_ok=True)
(base.OUT / "r7_source_manifest.json").write_text(
    json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
print("wrote figures/r7/r7_source_manifest.json")
