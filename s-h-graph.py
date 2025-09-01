import matplotlib.pyplot as plt
import math

plt.figure(figsize=(6.4*1.5, 4.8*1.5))

xMax = 15
xVals = []
yVals = []
betaVals = [3/4, 2/3, 1/2, 1/3, 1/4]

for beta in betaVals:
    for s in range(0, xMax+1):
        xVals.append(s)
        yVals.append( s ** beta )
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
plt.xlabel("s")
plt.ylabel("h (s^beta)")
plt.grid(True)
plt.show()
