import matplotlib.pyplot as plt
import math

plt.figure(figsize=(6.4*1.5, 4.8*1.5))
plt.rcParams["font.size"] = 14

xMax = 15
xVals = []
yVals = []
betaVals = [3/4, 2/3, 1/2, 1/3, 1/4]

for beta in betaVals:
    for s in range(1, xMax+1):
        xVals.append(s)
        yVals.append( math.log(math.e * (s ** beta), math.e) )
    plt.plot(xVals, yVals)
    for x, y in zip(xVals, yVals):
        plt.text(x, y, str(round(y,1)), ha="center", va="bottom")    
    plt.text(xMax+0.5,
             yVals[len(yVals)-1],
             "β=" + str(round(beta,2)),
             ha="left",
             va="bottom")
    xVals = []
    yVals = []

plt.xlim(0, 17)
plt.xlabel("S", fontsize=30)
plt.ylabel("ln(e * s^beta)", fontsize=30)
plt.grid(True)
plt.show()
