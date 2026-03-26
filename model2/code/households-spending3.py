import numpy as np, math
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

n = np.linspace(0.1, 5, 200)
c = np.linspace(0.1, 5, 200)
N, C = np.meshgrid(n, c)

w = 57.77
t = 0.0326
p = 1
k = 0.1
alpha = 3.66
beta = math.e
gamma = 0.15

U = w \
    - (w * t * N) \
    - (p * C * N) \
    - (k * N) \
    + (alpha * np.log(beta)) \
    + (alpha * np.log(N)) \
    + (alpha * gamma * np.log(C))

nOptimal = (alpha * (1 - gamma)) / (w * t + k)
cOptimal = (gamma * (w * t + k)) / (p * (1 - gamma))

uOptimal = w \
    - (w * t * nOptimal) \
    - (p * cOptimal * nOptimal) \
    - (k * nOptimal) \
    + (alpha * np.log(beta)) \
    + (alpha * np.log(nOptimal)) \
    + (alpha * gamma * np.log(cOptimal))

# Figure (wider → prevents z-axis clipping)
fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, projection="3d")

# Smooth surface (no mesh lines)
surf = ax.plot_surface(
    N, C, U,
    cmap="jet",
    edgecolor='none',
    antialiased=True
)

ax.scatter(nOptimal, cOptimal, uOptimal+0.5,
           color='white', edgecolor='white',
           s=80, linewidth=2, depthshade=False)

# ax.text(nOptimal, cOptimal, uOptimal,
#         r'$(n^*, c^*)$',
#         fontsize=10, color='black')

ax.plot([nOptimal, nOptimal],
        [cOptimal, cOptimal],
        [U.min(), uOptimal],
        color='black', linestyle='--', linewidth=1.5)

# visible point on base plane
ax.scatter(nOptimal, cOptimal, U.min(),
           s=30, color='black',
           linewidth=2, depthshade=False)

ax.plot([nOptimal, nOptimal],
        [0,  cOptimal],
        [U.min(), U.min()],
        color='black', linestyle='--', linewidth=1.5)

ax.plot([nOptimal, 5],
        [cOptimal,  cOptimal],
        [U.min(), U.min()],
        color='black', linestyle='--', linewidth=1.5)

ax.text(nOptimal + 0.1, -0.78, U.min(), 
        r'$\mathbf{n^*=1.57}$', fontsize=11, color='red', zorder=5)

ax.text(4.1, cOptimal + 0.15, U.min(),
        r'$\mathbf{c^*=0.35}$', fontsize=11, color='red', zorder=5)


# Labels (tight but readable)
ax.set_xlabel("N", labelpad=2, fontsize=11)
ax.set_ylabel("C", labelpad=2, fontsize=11)
ax.set_zlabel("U", labelpad=6, fontsize=11)

# Clean z ticks
zmin, zmax = U.min(), U.max()
ax.set_zticks(np.linspace(int(zmin), int(zmax), 4))
ax.zaxis.set_major_formatter(FormatStrFormatter('%d'))

# Better viewing angle (important!)
ax.view_init(elev=25, azim=-60)

# Reduce box distortion (makes surface look more natural)
ax.set_box_aspect((1, 1, 0.7))

# Remove pane backgrounds (clean paper look)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# Light grid only (optional)
ax.grid(True, linestyle='-', linewidth=0.3, alpha=0.3)

# Tight margins WITHOUT clipping
plt.subplots_adjust(left=0, right=0.95, bottom=0, top=0.99)

plt.show()