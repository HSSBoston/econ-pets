import matplotlib.pyplot as plt

plt.figure(figsize=(6.4, 4.8*2.5))

wVals     = [25, 50, 75, 100, 125, 150]
alphaVals = [2.5, 5, 7.5, 10, 12.5, 15]
gammaVals  = [0.2, 0.3, 0.4]
tVals     = []

for alpha in alphaVals:
    for beta in gammaVals:
        for w in wVals:
            v = ( alpha * (1 - beta) * 15 * 60)/w
            tVals.append(v)
            print(round(v), "mins", "w:", w, "alpha:", alpha, "beta:", beta)
        plt.plot(wVals, tVals)
        for x, y in zip(wVals, tVals):
            plt.text(x, y, str(round(y)), ha="center", va="bottom")
        plt.text(1,
                 tVals[0],
                 "α=" + str(alpha) + "γ=" + str(round(beta,2)),
                 ha="left",
                 va="bottom")
        tVals = []

wVals     = [25, 50, 75, 100, 125, 150]
alphaVals = [2.5, 5, 7.5, 10, 12.5, 15]
gammaVals  = [0.6]
tVals     = []

for alpha in alphaVals:
    for beta in gammaVals:
        for w in wVals:
            v = ( alpha * (1 - beta) * 15 * 60)/w
            tVals.append(v)
            print(round(v), "mins", "w:", w, "alpha:", alpha, "beta:", beta)
        plt.plot(wVals, tVals)
        for x, y in zip(wVals, tVals):
            plt.text(x, y, str(round(y)), ha="center", va="bottom")
        plt.text(1,
                 tVals[0]-6,
                 "α=" + str(alpha) + "β=" + str(round(beta,2)),
                 ha="left",
                 va="bottom")
        tVals = []

wVals     = [25, 50, 75, 100, 125, 150]
alphaVals = [2.5, 5, 7.5, 10, 12.5, 15]
gammaVals  = [0.7]
tVals     = []

for alpha in alphaVals:
    for beta in gammaVals:
        for w in wVals:
            v = ( alpha * (1 - beta) * 15 * 60)/w
            tVals.append(v)
            print(round(v), "mins", "w:", w, "alpha:", alpha, "beta:", beta)
        plt.plot(wVals, tVals)
        for x, y in zip(wVals, tVals):
            plt.text(x, y, str(round(y)), ha="center", va="bottom")
        plt.text(1,
                 tVals[0]+6,
                 "α=" + str(alpha) + "β=" + str(round(beta,2)),
                 ha="left",
                 va="bottom")
        tVals = []

#plt.xlim(0, 155)
plt.xticks([0, 25, 50, 75, 100, 125, 150])
plt.xlabel("Hourly wage rate (w)", fontsize=20)
plt.ylabel("Time Spent for Pet Care (min)", fontsize=20)
plt.grid(True)
plt.show()
