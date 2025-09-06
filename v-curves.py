import matplotlib.pyplot as plt

plt.figure(figsize=(6.4, 4.8*2.5))

wVals     = [25, 50, 75, 100, 125, 150]
alphaVals = [2.5, 5, 7.5, 10, 12.5, 15]
betaVals  = [0.5]
vVals     = []

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
                 "α=" + str(alpha) + "β=" + str(round(beta,2)),
                 ha="left",
                 va="bottom")
        vVals = []

wVals     = [25, 50, 75, 100, 125, 150]
alphaVals = [2.5, 5, 7.5, 10, 12.5, 15]
betaVals  = [0.6]
vVals     = []

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
                 vVals[0]-6,
                 "α=" + str(alpha) + "β=" + str(round(beta,2)),
                 ha="left",
                 va="bottom")
        vVals = []

wVals     = [25, 50, 75, 100, 125, 150]
alphaVals = [2.5, 5, 7.5, 10, 12.5, 15]
betaVals  = [0.7]
vVals     = []

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
                 vVals[0]+6,
                 "α=" + str(alpha) + "β=" + str(round(beta,2)),
                 ha="left",
                 va="bottom")
        vVals = []

#plt.xlim(0, 155)
plt.xticks([0, 25, 50, 75, 100, 125, 150])
plt.xlabel("w ($/hr)", fontsize=20)
plt.ylabel("v^*' (minutes)", fontsize=20)
plt.grid(True)
plt.show()
