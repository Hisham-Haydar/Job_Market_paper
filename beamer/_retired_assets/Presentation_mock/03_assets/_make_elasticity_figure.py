"""Generate elasticity stacked-bar figure for JMP presentation."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = r"c:\Users\hisham\Desktop\Job_Market_paper\Presentation_mock\03_assets"

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.8,
    "xtick.major.size": 3,
    "ytick.major.size": 3,
})

C_EXT = "#2c5f8a"   # dark blue  – extensive margin (bottom)
C_INT = "#e07b3a"   # orange     – intensive margin (top)

groups    = ["Low\neducation", "Medium\neducation", "High\neducation"]
extensive = [0.30, 0.22, 0.14]
intensive = [0.13, 0.11, 0.09]
totals    = [0.43, 0.33, 0.23]

x = np.arange(len(groups))
w = 0.45

fig, ax = plt.subplots(figsize=(7.0, 5.0))

b1 = ax.bar(x, extensive, width=w, color=C_EXT, zorder=3,
            label="Extensive margin (participation)")
b2 = ax.bar(x, intensive, width=w, bottom=extensive, color=C_INT, zorder=3,
            label="Intensive margin (hours | employed)")

# segment labels
for i, (e, n) in enumerate(zip(extensive, intensive)):
    ax.text(i, e / 2,       f"{e:.2f}", ha="center", va="center",
            fontsize=10, fontweight="bold", color="white")
    ax.text(i, e + n / 2,   f"{n:.2f}", ha="center", va="center",
            fontsize=10, fontweight="bold", color="white")

# total label above each bar
for i, t in enumerate(totals):
    ax.text(i, t + 0.008, f"Total = {t:.2f}", ha="center", va="bottom",
            fontsize=9, color="#333333", fontweight="bold")

ax.set_xticks(x)
ax.set_xticklabels(groups, fontsize=11)
ax.set_ylabel("Uncompensated elasticity", fontsize=10)
ax.set_ylim(0, 0.58)
ax.yaxis.grid(True, linestyle="--", linewidth=0.5, alpha=0.65, zorder=0)
ax.set_axisbelow(True)

ax.legend(frameon=False, fontsize=10, loc="upper right")
ax.set_title(
    "Behavioral-validation elasticities from the estimated structural model",
    fontsize=11, fontweight="bold", pad=12
)

fig.tight_layout()
fig.savefig(f"{OUT}/figure_elasticities.png", dpi=180, bbox_inches="tight")
print("Saved figure_elasticities.png")
