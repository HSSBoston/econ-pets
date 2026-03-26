import numpy as np, math
import matplotlib.pyplot as plt

# Grid
n = np.linspace(0.1, 5, 300)
c = np.linspace(0.1, 5, 300)
N, C = np.meshgrid(n, c)

# Parameters
w = 57.77
t = 0.0326
p = 1
k = 0.1
alpha = 3.66
beta = math.e
gamma = 0.15

# Utility
U = w \
    - (w * t * N) \
    - (p * C * N) \
    - (k * N) \
    + (alpha * np.log(beta)) \
    + (alpha * np.log(N)) \
    + (alpha * gamma * np.log(C))

# === Single panel only ===
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(N, C, U, cmap="jet")

ax.set_xlabel("N")
ax.set_ylabel("C")
ax.set_zlabel("U", labelpad=8)

# Optional: cleaner look for paper
# ax.view_init(elev=25, azim=-135)
ax.view_init(elev=28, azim=-60)

# Optimal point (kept for reference / print)
nOptimal = (alpha * (1 - gamma)) / (w * t + k)
cOptimal = (gamma * (w * t + k)) / (p * (1 - gamma))

uOptimal = w \
    - (w * t * nOptimal) \
    - (p * cOptimal * nOptimal) \
    - (k * nOptimal) \
    + (alpha * np.log(beta)) \
    + (alpha * np.log(nOptimal)) \
    + (alpha * gamma * np.log(cOptimal))

print(nOptimal, cOptimal, uOptimal)

plt.subplots_adjust(left=0.02, right=0.88, bottom=0.02, top=0.98)
plt.tight_layout(pad=0.1)
plt.show()