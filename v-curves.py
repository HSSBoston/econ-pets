import matplotlib.pyplot as plt
import numpy as np

wList     = [50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300]
alphaList = [7, 9, 11, 13, 15]
betaList  = [1/2, 3/4]
vList     = []

plt.figure(figsize=(6.4*1.5, 4.8*2))

for alpha in alphaList:
    for beta in betaList:
        for w in wList:
            v = (2 * alpha * (1 - beta) * 16 * 60)/w
            vList.append(v)
            print(round(v), "mins", "w:", w, "alpha:", alpha, "beta:", beta)
        plt.plot(wList, vList)
#         for x, y in zip(wList, vList):
#             plt.text(x, y, str(round(y)), ha="center", va="bottom")
        plt.text(5,
                 vList[0],
                 "α=" + str(alpha) + ", β=" + str(round(beta,2)),
                 ha="left",
                 va="bottom")
        vList = []

plt.xlim(0, 310)
plt.xlabel("w")
plt.ylabel("v")
plt.grid(True)
plt.show()
