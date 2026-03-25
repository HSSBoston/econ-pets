import matplotlib.pyplot as plt

plt.figure(figsize=(4, 4))

k = 0.1
alpha = 3.66
gamma = 0.15
wVals     = [30, 50, 70]
alphaVals = [alpha, alpha*1.5]
gammaVals = [gamma, gamma*2]
tVals     = []


for alpha in alphaVals:
    for gamma in gammaVals:
        for w in wVals:
            t = (alpha * (1 - gamma) - k)/w * 14.2 * 60
            tVals.append(t)
            print(round(t), "mins", "w:", w, "alpha:", alpha, "gamma:", gamma)
        plt.plot(wVals, tVals)
        for x, y in zip(wVals, tVals):
            plt.text(x, y, str(round(y)), ha="center", va="bottom")
        plt.text(15.1,
                 tVals[0],
                 "α=" + str(alpha) + "γ=" + str(round(gamma,2)),
                 fontsize="11",
                 ha="left",
                 va="bottom")
        tVals = []

#plt.xlim(0, 155)
plt.xticks([15, 30, 40, 50, 60, 70])
plt.xlabel("Wage ($w$)", fontsize=15)
# plt.yticks([10, 25, 50, 75, 100, 125, 150, 175, 200])
plt.ylabel("Caregiving time per pet ($t$, min)", fontsize=15)
plt.grid(True)
plt.show()
