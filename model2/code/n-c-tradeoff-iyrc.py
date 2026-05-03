import numpy as np, math
import matplotlib.pyplot as plt

alpha = 3.66
beta = math.e
gamma = 0.15
w = 57.77
p = 1
t = 0.0326
k = 0.1

n = np.linspace(0.1, 3.5, 200)
c = np.linspace(0.1, 3.5, 200)
N, C = np.meshgrid(n, c)

U = w \
    - (w * t * N)  \
    - (p * C * N)  \
    - (k * N) \
    + (alpha * np.log(beta))  \
    + (alpha * np.log(N))  \
    + (alpha * gamma * np.log(C))

nOptimal = (alpha * (1 - gamma)) / (w * t + k)
cOptimal = (gamma * (w * t + k)) / (p * (1 - gamma))

# n-c relationship under w-α = s^*
cUnderOptimalS = (alpha/n - (w*t + k)) / p

uOptimal = w \
            - (w * t * nOptimal)  \
            - (p * cOptimal * nOptimal)  \
            - (k * nOptimal) \
            + (alpha * np.log(beta))  \
            + (alpha * np.log(nOptimal))  \
            + (alpha * gamma * np.log(cOptimal))

print(nOptimal, cOptimal, uOptimal)

plt.figure(figsize=(4,4))

# Plot contours (indifference curves)
contours = plt.contour(N, C, U, levels=10, cmap="jet")
plt.clabel(contours, inline=True, fontsize=12)

# Plot constraint
plt.plot(n, cUnderOptimalS, "k-", linewidth=2, label=r"$n$-$c$ combinations under $s^*$")

# Plot the optimal (n^*, c^*) point
plt.scatter(nOptimal, cOptimal,
            color="red", edgecolor="black",
            s=80, zorder=5)
plt.text(nOptimal, cOptimal + 0.05,
         r"  $\mathbf{(n^*,c^*)}$", fontsize=12)

plt.xlabel("Number of pets ($n$)", fontsize=15, labelpad=0)
plt.ylabel("Caregiving intensity ($c$)", fontsize=15, labelpad=0)

plt.legend(
    loc="lower right",
    bbox_to_anchor=(1.0, 0.5),
    fontsize=12,
    frameon=True,
    handlelength=1.0,
    borderpad=0.2,
    labelspacing=0.2,
    handletextpad=0.4,
    borderaxespad=0.2
)

# plt.xlim(0,3.5)
plt.ylim(0,3.5)

ax = plt.gca()
ax.set_xticks([0, 1, 2, 3])
ax.set_xticks([0.5, 1.5, 2.5, 3.5], minor=True)
ax.tick_params(axis='x', which='major', direction='in', length=5)
ax.tick_params(axis='x', which='minor', direction='in', length=3)
ax.grid(axis='x', which='major', linestyle='-', linewidth=0.6, alpha=0.5)
ax.grid(axis='x', which='minor', linestyle='-', linewidth=0.3, alpha=0.2)

ax.set_yticks([0, 1, 2, 3])
ax.set_yticks([0.5, 1.5, 2.5, 3.5], minor=True)
ax.tick_params(axis='y', which='major', direction='out', length=5)
ax.tick_params(axis='y', which='minor', direction='out', length=3)
ax.grid(axis='y', which='major', linestyle='-', linewidth=0.6, alpha=0.5)
ax.grid(axis='y', which='minor', linestyle='-', linewidth=0.3, alpha=0.2)

plt.subplots_adjust(left=0.14, right=0.98, bottom=0.12, top=0.98)

plt.tight_layout(pad=0.05)
plt.show()
