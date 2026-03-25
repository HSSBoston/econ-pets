import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Model 2: baseline parameters
# ============================================================
alpha = 3.66
gamma = 0.15
w = 57.77
t = 0.0326
p = 1.0
k = 0.1

# Alternative scenarios
wHigh = 70.0
alphaHigh = 5.0

# ============================================================
# Closed-form solutions
# ============================================================
def nStar(alpha, gamma, w, t, k):
    """Optimal pet quantity"""
    return alpha * (1.0 - gamma) / (w * t + k)

def cStar(gamma, w, t, p, k):
    """Optimal caregiving intensity"""
    return gamma * (w * t + k) / (p * (1.0 - gamma))

# ============================================================
# Marginal benefit and marginal cost
# ============================================================
def mbN(n, alpha):
    """Marginal benefit of one more pet"""
    return alpha / n

def mcN(w, t, p, c, k):
    """Marginal cost of one more pet"""
    return w * t + p * c + k

# ============================================================
# Equilibria
# ============================================================
n0 = nStar(alpha, gamma, w, t, k)
c0 = cStar(gamma, w, t, p, k)
mc0 = mcN(w, t, p, c0, k)

nW = nStar(alpha, gamma, wHigh, t, k)
cW = cStar(gamma, wHigh, t, p, k)
mcW = mcN(wHigh, t, p, cW, k)

nA = nStar(alphaHigh, gamma, w, t, k)
cA = cStar(gamma, w, t, p, k)
mcA = mcN(w, t, p, cA, k)

# ============================================================
# Plot 1: MB vs MC
# ============================================================
nGrid = np.linspace(1, 3, 500)

plt.figure(figsize=(4, 4))
plt.plot(nGrid, mbN(nGrid, alpha), label='MB(n): baseline',
         linewidth=2.5, color="black")
plt.plot(nGrid, mbN(nGrid, alphaHigh), label='MB(n): higher α (5)',
         linewidth=2.5, color="blue")

plt.axhline(mc0, label='MC(n): baseline', linewidth=2.5,
             linestyle='--', color="black")
plt.axhline(mcW, label='MC(n): higher w (70)', linewidth=2.5,
            linestyle='--', color="red")

# Equilibrium points
plt.scatter([n0], [mc0], s=80, zorder=5, color="black")
plt.scatter([nW], [mcW], s=80, zorder=5, color="red")
plt.scatter([nA], [mcA], s=80, zorder=5, color="blue")

plt.annotate(f'n*={n0:.2f}', (n0, mc0), xytext=(-30, -20), textcoords='offset points',
             fontsize="11", fontweight='bold', color="black", )
plt.annotate(f'higher w\nn*={nW:.2f}', (nW, mcW), xytext=(-15, 11), textcoords='offset points',
             fontsize="11", color="red", zorder=5)
plt.annotate(f'higher α\nn*={nA:.2f}', (nA, mcA), xytext=(3, 3), textcoords='offset points',
             fontsize="11", color="blue", zorder=5)

plt.xlabel('Number of pets (n)', fontsize=20)
plt.ylabel('Marginal value', fontsize=20)
# plt.title('Model 2: Marginal Benefit and Marginal Cost for Pet Quantity', fontsize=14)
plt.xlim(1.0, 2.5)
plt.xticks([1.0, 1.5, 2.0, 2.5])
# plt.ylim(0, max(mcW, mcA, mc0, mbN(0.1, alphaHigh)) * 1.05)
plt.ylim(1, 5)
plt.grid(True, alpha=0.3)
# plt.legend(handlelength=1.5)
plt.legend()
plt.tight_layout(pad=0.1)
plt.show()

#plt.savefig('figure1.png', bbox_inches='tight', pad_inches=0.02)

# ============================================================
# Plot 2: MC decomposition
# ============================================================
timeCost0 = w * t
careCost0 = p * c0
overheadCost0 = k

timeCostW = wHigh * t
careCostW = p * cW
overheadCostW = k

labels = ['Baseline', 'Higher wage']
x = np.arange(len(labels))
barWidth = 0.6

plt.figure(figsize=(8, 6))
plt.bar(x, [timeCost0, timeCostW], barWidth, label='Opportunity cost: wt')
plt.bar(x, [careCost0, careCostW], barWidth,
        bottom=[timeCost0, timeCostW], label='Monetary care cost: pc*')
plt.bar(x, [overheadCost0, overheadCostW], barWidth,
        bottom=[timeCost0 + careCost0, timeCostW + careCostW],
        label='Overhead cost: k')

totals = [
    timeCost0 + careCost0 + overheadCost0,
    timeCostW + careCostW + overheadCostW
]

plt.plot(x, totals, marker='o', linewidth=2, label='Total MC = MB at optimum')

for i, total in enumerate(totals):
    plt.text(x[i], total + 0.05, f'{total:.2f}', ha='center')

plt.xticks(x, labels)
plt.ylabel('Marginal cost at optimum', fontsize=12)
plt.title('Model 2: Decomposition of Marginal Cost at Equilibrium', fontsize=14)
plt.grid(True, axis='y', alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# ============================================================
# Summary
# ============================================================
print('--- Baseline ---')
print(f'n*  = {n0:.4f}')
print(f'c*  = {c0:.4f}')
print(f'MB = MC at optimum = {mc0:.4f}')
print(f'  wt   = {timeCost0:.4f}')
print(f'  pc*  = {careCost0:.4f}')
print(f'  k    = {overheadCost0:.4f}')

print('\n--- Higher wage ---')
print(f'n*  = {nW:.4f}')
print(f'c*  = {cW:.4f}')
print(f'MB = MC at optimum = {mcW:.4f}')
print(f'  wt   = {timeCostW:.4f}')
print(f'  pc*  = {careCostW:.4f}')
print(f'  k    = {overheadCostW:.4f}')

print('\n--- Higher alpha ---')
print(f'n*  = {nA:.4f}')
print(f'c*  = {cA:.4f}')
print(f'MB = MC at optimum = {mcA:.4f}')