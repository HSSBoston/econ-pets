import numpy as np
import matplotlib.pyplot as plt

w = 57.77
t = 0.0326
p = 1.0
alpha0 = 3.66
gamma0 = 0.15
k0 = 0.1

# Total monetary expenditure:
# E = p c* n* + k n*
#   = alpha * gamma + alpha * k * (1 - gamma) / (w t + k)
#
def monetaryExpenditure(alpha, gamma, w, t, k):
    return alpha * gamma + alpha * k * (1.0 - gamma) / (w * t + k)

alphaVals = np.linspace(0.5, 6.0, 300)
gammaVals = np.linspace(0.01, 0.5, 300)
kVals = np.linspace(0.01, 1.0, 300)

expAlpha = monetaryExpenditure(alphaVals, gamma0, w, t, k0)
expGamma = monetaryExpenditure(alpha0, gammaVals, w, t, k0)
expK = monetaryExpenditure(alpha0, gamma0, w, t, kVals)

# Calibrated-point values
expAlpha0 = monetaryExpenditure(alpha0, gamma0, w, t, k0)
expGamma0 = monetaryExpenditure(alpha0, gamma0, w, t, k0)
expK0 = monetaryExpenditure(alpha0, gamma0, w, t, k0)

# Shared y-axis limits
yMin = 0
yMax = 1.05 * max(expAlpha.max(), expGamma.max(), expK.max())

fig, axes = plt.subplots(1, 3, figsize=(5, 4), sharey=True)
# fig, axes = plt.subplots(1, 3, figsize=(5.2, 2.6), sharey=True)

# Panel (a): expenditure vs alpha
#
axes[0].plot(alphaVals, expAlpha, linewidth=2)
axes[0].scatter([alpha0], [expAlpha0], color='black', s=30, zorder=5)
axes[0].annotate(f'({alpha0:.2f}, {expAlpha0:.2f})',
                 (alpha0, expAlpha0),
                 xytext=(-55, 10),
                 textcoords='offset points',
                 fontsize=10)

# axes[0].set_title(r'(a) vs. $\alpha$', fontsize=9)
axes[0].set_xlabel(r'$\alpha$', fontsize=15)
axes[0].set_ylabel('Total expenditure', fontsize=15, labelpad=0)
# axes[0].set_xlim(alphaVals.min(), alphaVals.max())
axes[0].set_xticks([0, 2, 4, 6])
# axes[0].set_ylim(yMin, yMax)
axes[0].set_yticks([0, 1, 2])
axes[0].set_yticks([0.25, 0.5, 0.75, 1.25, 1.5, 1.75], minor=True)
axes[0].tick_params(axis='y', which='both', direction='in')
axes[0].tick_params(axis='y', which='minor', length=3)
axes[0].tick_params(axis='y', which='major', length=5)
axes[0].tick_params(axis='both', labelsize=12)

# Panel (b): expenditure vs gamma
#
axes[1].plot(gammaVals, expGamma, linewidth=2)
axes[1].scatter([gamma0], [expGamma0], color='black', s=30, zorder=5)
axes[1].annotate(f'({gamma0:.2f}, {expGamma0:.2f})',
                 (gamma0, expGamma0),
                 xytext=(4, -15),
                 textcoords='offset points',
                 fontsize=10)

# axes[1].set_title(r'(b) vs. $\gamma$', fontsize=9)
axes[1].set_xlabel(r'$\gamma$', fontsize=15)
# axes[1].set_xlim(gammaVals.min(), gammaVals.max())
axes[1].set_xticks([0.1, 0.2, 0.3, 0.4, 0.5])
axes[1].tick_params(labelleft=False)

# Panel (c): expenditure vs k
#
axes[2].plot(kVals, expK, linewidth=2)
axes[2].scatter([k0], [expK0], color='black', s=30, zorder=5)
axes[2].annotate(f'({k0:.2f}, {expK0:.2f})',
                 (k0, expK0),
                 xytext=(4, -15),
                 textcoords='offset points',
                 fontsize=10)

# axes[2].set_title(r'(c) vs. $k$', fontsize=9)
axes[2].set_xlabel(r'$k$', fontsize=15)
# axes[2].set_xlim(kVals.min(), kVals.max())
axes[2].set_xticks([0.25, 0.5, 0.75, 1])
axes[2].tick_params(labelleft=False)

# Style cleanup for compact paper figure
#
for ax in axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, alpha=0.25)
    ax.set_yticks([0, 1, 2])
    ax.set_yticks([0.5, 1.5], minor=True)
    ax.tick_params(axis='y', which='both', direction='in')
    ax.tick_params(axis='y', which='minor', length=3)
    
plt.tight_layout(pad=0.05)
plt.subplots_adjust(left=0.09, right=0.995, top=0.98, bottom=0.14, wspace=0.0)

# plt.savefig('monetary_expenditure_three_panel.png',
#             dpi=300,
#             bbox_inches='tight',
#             pad_inches=0.02)

plt.show()