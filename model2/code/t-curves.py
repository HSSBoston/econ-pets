import matplotlib.pyplot as plt

# plt.figure(figsize=(6.4, 4.8*2.5))

k = 0.1
wVals     = [25, 50, 75]
alphaVals = [2.5, 3.5, 5.0]
gammaVals  = [0.15, 0.3, 0.45]
tVals     = []


for alpha in alphaVals:
    for gamma in gammaVals:
        for w in wVals:
            t = (alpha * (1 - gamma) - k)/w * 15 * 60
            tVals.append(t)
            print(round(t), "mins", "w:", w, "alpha:", alpha, "gamma:", gamma)
        plt.plot(wVals, tVals)
        for x, y in zip(wVals, tVals):
            plt.text(x, y, str(round(y)), ha="center", va="bottom")
        plt.text(5.1,
                 tVals[0],
                 "α=" + str(alpha) + "γ=" + str(round(gamma,2)),
                 fontsize="11",
                 ha="left",
                 va="bottom")
        tVals = []

#plt.xlim(0, 155)
plt.xticks([5, 25, 50, 75])
plt.xlabel("Hourly wage rate (w)", fontsize=20)
# plt.yticks([10, 25, 50, 75, 100, 125, 150, 175, 200])
plt.ylabel("Caregiving time per pet (min)", fontsize=20)
plt.grid(True)
plt.show()
