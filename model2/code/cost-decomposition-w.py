import math
import numpy as np
import matplotlib.pyplot as plt

w0 = 57.77
t = 0.0326
p = 1.0
k = 0.1
alpha = 3.66
gamma = 0.15

wMin = 20
wMax = 80

def nStar(w):
    return alpha * (1.0 - gamma) / (w * t + k)

def cStar(w):
    return gamma * (w * t + k) / (p * (1.0 - gamma))

def monetaryExpenditure(w):
    return p * cStar(w) * nStar(w)

def timeOpportunityCost(w):
    return w * t * nStar(w)

def fixedCostComponent(w):
    return k * nStar(w)

def totalPetCost(w):
    return (
        monetaryExpenditure(w)
        + timeOpportunityCost(w)
        + fixedCostComponent(w)
    )

wGrid = np.linspace(wMin, wMax, 400)

nVals = nStar(wGrid)
cVals = cStar(wGrid)

monetaryVals = monetaryExpenditure(wGrid)
timeVals = timeOpportunityCost(wGrid)
fixedVals = fixedCostComponent(wGrid)
totalVals = totalPetCost(wGrid)

monetaryShareVals = monetaryVals / totalVals
timeShareVals = timeVals / totalVals
fixedShareVals = fixedVals / totalVals

baselineN = nStar(w0)
baselineC = cStar(w0)

baselineMonetary = monetaryExpenditure(w0)
baselineTime = timeOpportunityCost(w0)
baselineFixed = fixedCostComponent(w0)
baselineTotal = totalPetCost(w0)

baselineMonetaryShare = baselineMonetary / baselineTotal
baselineTimeShare = baselineTime / baselineTotal
baselineFixedShare = baselineFixed / baselineTotal

print("Baseline parameter values")
print(f"w = {w0:.2f}, t = {t}, p = {p}, k = {k}, alpha = {alpha}, gamma = {gamma}")
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
    wGrid,
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

ax1.axvline(w0, linestyle="--", linewidth=1)
ax1.text(
    w0 + 1,
    max(totalVals) * 0.9,
    f"Baseline w = {w0:.2f}",
    fontsize=10
)

ax1.set_xlabel("Hourly wage rate (w)", fontsize=12)
ax1.set_ylabel("Pet-related cost", fontsize=12)
ax1.set_title("Model 2: Expenditure Decomposition (Stacked Area)", fontsize=14)
ax1.legend()
ax1.grid(True, alpha=0.3)

plt.tight_layout()
# #plt.show()

#
# Figure 2: Line plot
#
fig2, ax2 = plt.subplots(figsize=(9, 6))

ax2.plot(wGrid, monetaryVals, label="Monetary", linewidth=2)
ax2.plot(wGrid, timeVals, label="Time cost", linewidth=2)
ax2.plot(wGrid, fixedVals, label="Fixed cost", linewidth=2)
ax2.plot(wGrid, totalVals, label="Total", linewidth=2.5, linestyle="--")

ax2.axvline(w0, linestyle="--", linewidth=1)

ax2.scatter(
    [w0, w0, w0, w0],
    [baselineMonetary, baselineTime, baselineFixed, baselineTotal],
    s=40
)

ax2.annotate(f"{baselineMonetary:.2f}", (w0, baselineMonetary), xytext=(5, 5), textcoords="offset points")
ax2.annotate(f"{baselineTime:.2f}", (w0, baselineTime), xytext=(5, 5), textcoords="offset points")
ax2.annotate(f"{baselineFixed:.2f}", (w0, baselineFixed), xytext=(5, 5), textcoords="offset points")
ax2.annotate(f"{baselineTotal:.2f}", (w0, baselineTotal), xytext=(5, 5), textcoords="offset points")

ax2.set_xlabel("Hourly wage rate (w)", fontsize=12)
ax2.set_ylabel("Pet-related cost", fontsize=12)
ax2.set_title("Model 2: Expenditure Decomposition (Line)", fontsize=14)
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

#
# Figure 3: Cost shares
#
fig3, ax3 = plt.subplots(figsize=(9, 6))

ax3.plot(wGrid, monetaryShareVals, label=r"Monetary share $pc^*n^*/\mathrm{total}$", linewidth=2)
ax3.plot(wGrid, timeShareVals, label=r"Time share $wt\,n^*/\mathrm{total}$", linewidth=2)
ax3.plot(wGrid, fixedShareVals, label=r"Fixed share $kn^*/\mathrm{total}$", linewidth=2)

ax3.axvline(w0, linestyle="--", linewidth=1)

ax3.scatter(
    [w0, w0, w0],
    [baselineMonetaryShare, baselineTimeShare, baselineFixedShare],
    s=40
)

ax3.annotate(f"{baselineMonetaryShare:.2f}", (w0, baselineMonetaryShare), xytext=(5, 5), textcoords="offset points")
ax3.annotate(f"{baselineTimeShare:.2f}", (w0, baselineTimeShare), xytext=(5, 5), textcoords="offset points")
ax3.annotate(f"{baselineFixedShare:.2f}", (w0, baselineFixedShare), xytext=(5, 5), textcoords="offset points")

ax3.set_xlabel("Hourly wage rate (w)", fontsize=12)
ax3.set_ylabel("Cost share", fontsize=12)
ax3.set_ylim(0, 1)
ax3.set_title("Model 2: Cost Shares", fontsize=14)
ax3.legend()
ax3.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# fig1.savefig("stackedArea.png", dpi=300)
# fig2.savefig("linePlot.png", dpi=300)
# fig3.savefig("costShares.png", dpi=300)