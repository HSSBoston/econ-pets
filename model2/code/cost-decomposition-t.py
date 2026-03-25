import math
import numpy as np
import matplotlib.pyplot as plt

w = 57.77
t0 = 0.0326
p = 1.0
k = 0.1
alpha = 3.66
gamma = 0.15

tMin = 0.005
tMax = 0.08

def nStar(t):
    return alpha * (1.0 - gamma) / (w * t + k)

def cStar(t):
    return gamma * (w * t + k) / (p * (1.0 - gamma))

def monetaryExpenditure(t):
    return p * cStar(t) * nStar(t)

def timeOpportunityCost(t):
    return w * t * nStar(t)

def fixedCostComponent(t):
    return k * nStar(t)

def totalPetCost(t):
    return (
        monetaryExpenditure(t)
        + timeOpportunityCost(t)
        + fixedCostComponent(t)
    )

tGrid = np.linspace(tMin, tMax, 400)

nVals = nStar(tGrid)
cVals = cStar(tGrid)

monetaryVals = monetaryExpenditure(tGrid)
timeVals = timeOpportunityCost(tGrid)
fixedVals = fixedCostComponent(tGrid)
totalVals = totalPetCost(tGrid)

monetaryShareVals = monetaryVals / totalVals
timeShareVals = timeVals / totalVals
fixedShareVals = fixedVals / totalVals

baselineN = nStar(t0)
baselineC = cStar(t0)

baselineMonetary = monetaryExpenditure(t0)
baselineTime = timeOpportunityCost(t0)
baselineFixed = fixedCostComponent(t0)
baselineTotal = totalPetCost(t0)

baselineMonetaryShare = baselineMonetary / baselineTotal
baselineTimeShare = baselineTime / baselineTotal
baselineFixedShare = baselineFixed / baselineTotal

print("Baseline parameter values")
print(f"w = {w:.2f}, t = {t0}, p = {p}, k = {k}, alpha = {alpha}, gamma = {gamma}")
print()

print("Baseline optimal choices")
print(f"n* = {baselineN:.4f}")
print(f"c* = {baselineC:.4f}")
print()

print("Baseline expenditure decomposition")
print(f"Monetary (pc*n*) = {baselineMonetary:.4f}")
print(f"Time cost (wtn*) = {baselineTime:.4f}")
print(f"Fixed cost (kn*) = {baselineFixed:.4f}")
print(f"Total cost (pc*n* + wtn* + kn*) = {baselineTotal:.4f}")
print()

print("Baseline cost shares")
print(f"Monetary share = {baselineMonetaryShare:.4f}")
print(f"Time share = {baselineTimeShare:.4f}")
print(f"Fixed share = {baselineFixedShare:.4f}")

#
# Figure 1: Stacked area plot
#
fig1, ax1 = plt.subplots(figsize=(9, 6))

ax1.stackplot(
    tGrid,
    monetaryVals,
    timeVals,
    fixedVals,
    labels=[
        r"Monetary $pc^*n^*$",
        r"Time $wt\,n^*$",
        r"Fixed $kn^*$"
    ],
    alpha=0.85
)

ax1.axvline(t0, linestyle="--", linewidth=1)
ax1.text(
    t0 + 0.001,
    max(totalVals) * 0.9,
    f"Baseline t = {t0:.4f}",
    fontsize=10
)

ax1.margins(x=0)
ax1.set_xlim(tMin, tMax)
ax1.set_xlabel("Caregiving time per pet (t)", fontsize=12)
ax1.set_ylabel("Pet-related cost", fontsize=12)
ax1.set_title("Model 2: Expenditure Decomposition vs. t (Stacked Area)", fontsize=14)
ax1.legend()
ax1.grid(True, alpha=0.3)

plt.tight_layout(pad=0.1)
# plt.show()

#
# Figure 2: Line plot
#
fig2, ax2 = plt.subplots(figsize=(9, 6))

ax2.plot(tGrid, monetaryVals, label="Monetary", linewidth=2)
ax2.plot(tGrid, timeVals, label="Time cost", linewidth=2)
ax2.plot(tGrid, fixedVals, label="Fixed cost", linewidth=2)
ax2.plot(tGrid, totalVals, label="Total", linewidth=2.5, linestyle="--")

ax2.axvline(t0, linestyle="--", linewidth=1)

ax2.scatter(
    [t0, t0, t0, t0],
    [baselineMonetary, baselineTime, baselineFixed, baselineTotal],
    s=40
)

ax2.annotate(f"{baselineMonetary:.2f}", (t0, baselineMonetary), xytext=(5, 5), textcoords="offset points")
ax2.annotate(f"{baselineTime:.2f}", (t0, baselineTime), xytext=(5, 5), textcoords="offset points")
ax2.annotate(f"{baselineFixed:.2f}", (t0, baselineFixed), xytext=(5, 5), textcoords="offset points")
ax2.annotate(f"{baselineTotal:.2f}", (t0, baselineTotal), xytext=(5, 5), textcoords="offset points")

ax2.margins(x=0)
ax2.set_xlim(tMin, tMax)
ax2.set_xlabel("Caregiving time per pet (t)", fontsize=12)
ax2.set_ylabel("Pet-related cost", fontsize=12)
ax2.set_title("Model 2: Expenditure Decomposition vs. t (Line)", fontsize=14)
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout(pad=0.1)
# plt.show()

#
# Figure 3: Cost shares
#
fig3, ax3 = plt.subplots(figsize=(9, 6))

ax3.plot(tGrid, monetaryShareVals, label=r"Monetary cost $pc^*n^*$", linewidth=2)
ax3.plot(tGrid, timeShareVals, label=r"Opportunity cost $wt\,n^*$", linewidth=2)
ax3.plot(tGrid, fixedShareVals, label=r"Overhead $kn^*$", linewidth=2)

ax3.axvline(t0, linestyle="--", linewidth=1)

ax3.scatter(
    [t0, t0, t0],
    [baselineMonetaryShare, baselineTimeShare, baselineFixedShare],
    s=40
)

ax3.annotate(f"{baselineMonetaryShare:.2f}", (t0, baselineMonetaryShare), xytext=(5, 5), textcoords="offset points")
ax3.annotate(f"{baselineTimeShare:.2f}", (t0, baselineTimeShare), xytext=(5, 5), textcoords="offset points")
ax3.annotate(f"{baselineFixedShare:.2f}", (t0, baselineFixedShare), xytext=(5, 5), textcoords="offset points")

ax3.set_xlabel("Caregiving time per pet (t)", fontsize=12)
ax3.set_ylabel("Cost share", fontsize=12)

ax3.margins(x=0)
ax3.set_xlim(tMin, tMax)
ax3.set_ylim(0, 1)
# ax3.set_title("Model 2: Cost Shares vs. t", fontsize=14)
ax3.legend()
ax3.grid(True, alpha=0.3)

plt.tight_layout(pad=0.1)
plt.show()

# fig1.savefig("stackedAreaVsT.png", dpi=300, bbox_inches="tight", pad_inches=0)
# fig2.savefig("linePlotVsT.png", dpi=300, bbox_inches="tight", pad_inches=0)
# fig3.savefig("costSharesVsT.png", dpi=300, bbox_inches="tight", pad_inches=0)