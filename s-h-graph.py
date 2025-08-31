import matplotlib.pyplot as plt
import math

x = []
y = []
betaVals = [3/4, 1/2]

for beta in betaVals:
    for i in range(0, 101):
        x.append(i)
        y.append( i ** beta )
    plt.plot(x, y)
    x = []
    y = []

# 
# for x, y in zip(magnitude, luminosity):
#     plt.text(x, y, round(y, 2), ha="center", va="bottom")

plt.xlabel("s")
plt.ylabel("h (s^beta)")
plt.grid(True)
plt.show()
