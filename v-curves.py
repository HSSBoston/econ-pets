import matplotlib.pyplot as plt
import numpy as np

wVals     = [50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300]
alphaVals = [7.5, 10, 12.5, 15, 17.5, 20]
betaVals  = [1/2]
vVals     = []

plt.figure(figsize=(6.4*1.5, 4.8*2))

for alpha in alphaVals:
    for beta in betaVals:
        for w in wVals:
            v = ( alpha * (1 - beta) * 16 * 60)/w
            vVals.append(v)
            print(round(v), "mins", "w:", w, "alpha:", alpha, "beta:", beta)
        plt.plot(wVals, vVals)
        for x, y in zip(wVals, vVals):
            plt.text(x, y, str(round(y)), ha="center", va="bottom")
        plt.text(1,
                 vVals[0],
                 "α=" + str(alpha) + ", β=" + str(round(beta,2)),
                 ha="left",
                 va="bottom")
        vVals = []

plt.xlim(0, 310)
plt.xlabel("w")
plt.ylabel("v")
plt.grid(True)
plt.show()
