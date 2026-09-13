"""Generate slide-ready figures for JMP presentation assets."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUT = r"c:\Users\hisham\Desktop\Job_Market_paper\Presentation_mock\03_assets"

# ── shared style ──────────────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.8,
    "xtick.major.size": 3,
    "ytick.major.size": 3,
})

C_OBS  = "#2c5f8a"   # dark blue  – observed / opportunity
C_PRED = "#e07b3a"   # orange     – predicted / preference
C_RES  = "#aac4de"   # light blue – residual
C_GREY = "#6b6b6b"

# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 1 — Model fit: observed vs predicted labour-supply shares
# ═════════════════════════════════════════════════════════════════════════════
states   = ["Non-\nemployment", "1–15\nhours", "16–24\nhours",
            "25–34\nhours",    "35–44\nhours", "45+\nhours"]
observed  = [22.4, 6.1, 8.5, 13.7, 38.6, 10.7]
predicted = [22.1, 6.3, 8.6, 13.4, 38.4, 11.2]

x   = np.arange(len(states))
w   = 0.35

fig, ax = plt.subplots(figsize=(8.5, 4.8))
ax.bar(x - w/2, observed,  width=w, color=C_OBS,  label="Observed",  zorder=3)
ax.bar(x + w/2, predicted, width=w, color=C_PRED, label="Predicted", zorder=3)

ax.set_xticks(x)
ax.set_xticklabels(states, fontsize=10)
ax.set_ylabel("Share of sample (%)", fontsize=10)
ax.set_ylim(0, 47)
ax.yaxis.grid(True, linestyle="--", linewidth=0.5, alpha=0.7, zorder=0)
ax.set_axisbelow(True)

# annotate bars with value labels
for i, (o, p) in enumerate(zip(observed, predicted)):
    ax.text(i - w/2, o + 0.6, f"{o:.1f}", ha="center", va="bottom",
            fontsize=8, color=C_OBS, fontweight="bold")
    ax.text(i + w/2, p + 0.6, f"{p:.1f}", ha="center", va="bottom",
            fontsize=8, color=C_PRED, fontweight="bold")

ax.legend(frameon=False, fontsize=10, loc="upper right")
ax.set_title("Labour-Supply Distribution: Observed vs. Model-Predicted Shares",
             fontsize=11, fontweight="bold", pad=10)

fig.tight_layout()
fig.savefig(f"{OUT}/figure_fit.png", dpi=180, bbox_inches="tight")
plt.close(fig)
print("Saved figure_fit.png")


# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 2 — Shapley decomposition of baseline welfare Gini (stacked bar)
# ═════════════════════════════════════════════════════════════════════════════
#   Baseline welfare Gini = 0.186
#   Residual (common component after both equalizations) = 0.097
#   Opportunity component  = 0.039
#   Preference component   = 0.050

residual    = 0.097
opportunity = 0.039
preference  = 0.050
total       = residual + opportunity + preference   # 0.186

fig, ax = plt.subplots(figsize=(5.0, 5.5))

bar_x = 0.4
bar_w = 0.5

b1 = ax.bar(bar_x, residual,    width=bar_w, bottom=0,
            color=C_RES,  label=f"Residual / common  (0.097, 52.2%)", zorder=3)
b2 = ax.bar(bar_x, opportunity, width=bar_w, bottom=residual,
            color=C_OBS,  label=f"Opportunity (0.039, 21.0%)",        zorder=3)
b3 = ax.bar(bar_x, preference,  width=bar_w, bottom=residual + opportunity,
            color=C_PRED, label=f"Preference  (0.050, 26.9%)",        zorder=3)

# horizontal reference line at total Gini
ax.axhline(total, color="black", linewidth=1.0, linestyle="--", zorder=4)
ax.text(bar_x + bar_w/2 + 0.02, total + 0.002,
        f"Baseline Gini = {total:.3f}", va="bottom", fontsize=9, color="black")

# segment midpoint labels
for val, bottom, label in [
    (residual,    0,                       f"0.097"),
    (opportunity, residual,                f"0.039"),
    (preference,  residual + opportunity,  f"0.050"),
]:
    mid = bottom + val / 2
    ax.text(bar_x, mid, label, ha="center", va="center",
            fontsize=10, fontweight="bold", color="white")

ax.set_xlim(0, 1.1)
ax.set_ylim(0, 0.22)
ax.set_xticks([])
ax.set_ylabel("Welfare Gini (Gini points)", fontsize=10)
ax.yaxis.grid(True, linestyle="--", linewidth=0.5, alpha=0.6, zorder=0)
ax.set_axisbelow(True)
ax.legend(frameon=False, fontsize=9, loc="upper right",
          title="Component (Gini pts, % of baseline)", title_fontsize=8)
ax.set_title("Shapley Decomposition of Welfare Inequality:\nOpportunity vs. Preference Heterogeneity",
             fontsize=11, fontweight="bold", pad=10)

fig.tight_layout()
fig.savefig(f"{OUT}/figure_decomposition_shares.png", dpi=180, bbox_inches="tight")
plt.close(fig)
print("Saved figure_decomposition_shares.png")


# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 3 — Sensitivity to responsibility for opportunities
# ═════════════════════════════════════════════════════════════════════════════
stances   = ["Region × education\n(baseline)", "Education\nonly", "Region\nonly"]
shapley   = [0.039, 0.031, 0.026]
pct_gini  = [21.0,  16.7,  14.0]

x = np.arange(len(stances))
w = 0.42

fig, ax1 = plt.subplots(figsize=(7.0, 4.8))
ax2 = ax1.twinx()
ax2.spines["right"].set_visible(True)
ax2.spines["top"].set_visible(False)

bars = ax1.bar(x, shapley, width=w, color=C_OBS, zorder=3, label="Shapley opportunity component (left axis)")

for i, (s, p) in enumerate(zip(shapley, pct_gini)):
    ax1.text(i, s + 0.001, f"{s:.3f}", ha="center", va="bottom",
             fontsize=10, fontweight="bold", color=C_OBS)

# right-axis markers for % of baseline Gini
ax2.plot(x, pct_gini, marker="D", color=C_PRED, linewidth=1.8,
         markersize=8, zorder=4, label="Share of baseline Gini (right axis)")
for i, p in enumerate(pct_gini):
    ax2.text(i + 0.23, p + 0.4, f"{p:.1f}%", ha="left", va="bottom",
             fontsize=9, color=C_PRED, fontweight="bold")

ax1.set_xticks(x)
ax1.set_xticklabels(stances, fontsize=10)
ax1.set_ylabel("Shapley opportunity component (Gini points)", fontsize=9, color=C_OBS)
ax1.set_ylim(0, 0.055)
ax1.tick_params(axis="y", colors=C_OBS)
ax1.yaxis.grid(True, linestyle="--", linewidth=0.5, alpha=0.6, zorder=0)
ax1.set_axisbelow(True)

ax2.set_ylabel("Share of baseline welfare Gini (%)", fontsize=9, color=C_PRED)
ax2.set_ylim(0, 30)
ax2.tick_params(axis="y", colors=C_PRED)

# combined legend
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, frameon=False, fontsize=8.5, loc="upper right")

ax1.set_title("Sensitivity of Opportunity Contribution to Responsibility Assumptions",
              fontsize=11, fontweight="bold", pad=10)

fig.tight_layout()
fig.savefig(f"{OUT}/figure_responsibility_sensitivity.png", dpi=180, bbox_inches="tight")
plt.close(fig)
print("Saved figure_responsibility_sensitivity.png")
print("All figures done.")
