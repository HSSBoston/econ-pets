import numpy as np, math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n = np.linspace(0.1, 10, 100) # generate 100 n values in n=[0,10]
c = np.linspace(0.1, 10, 100) # generate 100 c values in c=[0,10]
N, C = np.meshgrid(n, c)    # generate a grid of n and c values

w = 53.43
t = 0.0285
p = 1
alpha = 3.77
beta = math.e
gamma = 0.307

U = w \
    - (w * t * N)  \
    - (p * C * N)  \
    + (alpha * np.log(beta))  \
    + (alpha * np.log(N))  \
    + (alpha * gamma * np.log(C))

fig = plt.figure()
ax1 = fig.add_subplot(221, projection="3d")
ax1.plot_surface(N, C, U, cmap="jet")
ax1.set_xlabel("N")
ax1.set_ylabel("C")
ax1.set_zlabel("U")

ax2 = fig.add_subplot(222, projection="3d")
im = ax2.contour3D(N, C, U, levels=20, cmap="jet")
plt.colorbar(im, ax=ax2, cmap="jet")
ax2.set_xlabel("N")
ax2.set_ylabel("C")
ax2.set_zlabel("U")

ax3 = fig.add_subplot(223)
im = ax3.pcolormesh(N, C, U, cmap="jet")
plt.colorbar(im, ax=ax3, cmap="jet")
ax3.set_xticks(np.arange(0,10.5,0.5), labels=np.arange(0,10.5,0.5), fontsize=9,rotation=65)
ax3.set_yticks(np.arange(0,11,1))
ax3.set_xlabel("N")
ax3.set_ylabel("C")

ax4 = fig.add_subplot(224)
ax4.contour(N, C, U, levels=20, cmap="jet")
plt.colorbar(im, ax=ax4, cmap="jet")
ax4.set_xticks(np.arange(0,10.5,0.5), labels=np.arange(0,10.5,0.5), fontsize=9,rotation=65)
ax4.set_yticks(np.arange(0,11,1))
# ax4.colorbar()
ax4.set_xlabel("N")
ax4.set_ylabel("C")

nOptimal = (alpha * (1 - gamma)) / (w * t)
cOptimal = (gamma/(1 - gamma)) * ((w * t) / p)
uOptimal = w \
            - (w * t * nOptimal)  \
            - (p * cOptimal * nOptimal)  \
            + (alpha * np.log(beta))  \
            + (alpha * np.log(nOptimal))  \
            + (alpha * gamma * np.log(cOptimal))

print(nOptimal, cOptimal, uOptimal)


#ax2.plot_wireframe(N, C, U, cmap="viridis")
# ax.plot_wireframe(N, C, U)
#ax.contour3D(N, C, U)

plt.show()


