import matplotlib.pyplot as plt
import numpy as np

wList     = [50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300]
alphaList = [7, 9, 11, 13, 15]
betaList  = [1/2, 3/4]
vList     = []

xMin =   
xMax = 

magnitude = np.linspace(xMin, xMax, N)
luminosity = 51 * 100**(-magnitude/5)
plt.plot(magnitude, luminosity)


for x, y in zip(magnitude, luminosity):
    plt.text(x, y, round(y, 2), ha="center", va="bottom")

plt.xlabel("Apparent Magnitude")
plt.ylabel("Luminosity")
plt.grid(True)
plt.show()
