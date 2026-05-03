import matplotlib.pyplot as plt

plt.figure(figsize=(4, 4))

k = 0.1
alpha = 3.66
gamma = 0.15
wVals     = [30, 50, 70]
alphaVals = [alpha, alpha*1.5]
gammaVals = [gamma, gamma*2]
tVals     = []



for i, alpha in enumerate(alphaVals):
    for j, gamma in enumerate(gammaVals):
        for w in wVals:
            t = (alpha * (1 - gamma) - k)/w * 14.2 * 60
            tVals.append(t)
            print(round(t), "mins", "w:", w, "alpha:", alpha, "gamma:", gamma)
        if i==0 and j==0:
            plt.plot(wVals, tVals, label="Baseline",
                     linewidth=2, color="black")
        elif i==0 and j==1:
            plt.plot(wVals, tVals, label="Higher γ",
                     linewidth=2, color="red")
        elif i==1 and j==0:
            plt.plot(wVals, tVals, label="Higher α",
                     linewidth=2, color="blue")
        elif i==1 and j==1:
            plt.plot(wVals, tVals, label="Higher α γ",
                     linewidth=2, color="green")
            
        for x, y in zip(wVals, tVals):
            plt.text(x, y, str(round(y)), ha="center", va="bottom", fontsize="11")
        tVals = []

#plt.xlim(0, 155)
plt.xticks([30, 40, 50, 60, 70])
plt.xticks(fontsize=12)
plt.xlabel("Wage ($w$)", fontsize=15, labelpad=0)
# plt.yticks([10, 25, 50, 75, 100, 125, 150, 175, 200])
plt.ylabel("Caregiving time per pet ($t$, min)", fontsize=15, labelpad=0)
plt.yticks(fontsize=12)

plt.grid(True, alpha=0.3)
plt.legend(
    loc='upper right', bbox_to_anchor=(1.0,1.0),
    fontsize=15,
    handlelength=1.0,
    handletextpad=0.3,
    labelspacing=0.15,
    borderpad=0,
    frameon=False
)
plt.tight_layout(pad=0.1)
plt.show()
