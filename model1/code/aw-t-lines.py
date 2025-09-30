import matplotlib.pyplot as plt

#plt.figure(figsize=(6.4, 4.8*2.5))

petExpenditureRatios = [0.05, 0.06, 0.07, 0.08, 0.09, 0.10]
gammaVals  = [0.2, 0.3, 0.4, 0.5, 0.6]
tVals     = []

for gammaVal in gammaVals:
    for petExpRatio in petExpenditureRatios:
        t = (petExpRatio * (1 - gammaVal) * 15 * 60)
        tVals.append(t)
        print(round(t), "mins", "alpha/w:", petExpRatio, "gamma:", gammaVal)
    plt.plot(petExpenditureRatios, tVals)
    for x, y in zip(petExpenditureRatios, tVals):
        plt.text(x, y, str(round(y)), ha="center", va="bottom")
#     plt.text(1,
#              vVals[0],
#              "α=" + str(alpha) + "β=" + str(round(beta,2)),
#              ha="left",
#              va="bottom")
    tVals = []


#plt.xlim(0, 155)
#plt.xticks([0, 25, 50, 75, 100, 125, 150])
plt.xlabel("α/w", fontsize=20)
plt.ylabel("Time Spent for a Pet (minutes)", fontsize=17)
plt.grid(True)
plt.show()
