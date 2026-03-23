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

plt.figure(figsize=(6,6))

# Plot contours (indifference curves)
contours = plt.contour(N, C, U, levels=10, cmap="jet")
plt.clabel(contours, inline=True, fontsize=10)

# Plot constraint
plt.plot(n, cUnderOptimalS, "k-", linewidth=2, label=r"$n$-$c$ combinations under $s^*$")

# Plot the optimal (n^*, c^*) point
plt.scatter(nOptimal, cOptimal,
            color="red", edgecolor="black",
            s=80, zorder=5)
plt.text(nOptimal, cOptimal + 0.05,
         r"  $\mathbf{(n^*,\,c^*)}$", fontsize=10)

plt.xlabel("Number of pets $n$")
plt.ylabel("Care intensity $c$")
plt.title("Optimal Pet Ownership Choice")

plt.legend(loc="lower right", bbox_to_anchor=(1, 0.25))
plt.xlim(0,3.5)
plt.ylim(0,3.5)

plt.tight_layout()
plt.show()