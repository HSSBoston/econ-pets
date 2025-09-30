import numpy as np
import matplotlib.pyplot as plt

everyYear = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
everyTwoYears = [2018, 2020, 2022, 2024]
numOfHouseholdsWithPets = [74.4, 84.9, 90.5, 86.9]
petCareSpending = [90.5, 97.1, 103.6, 123.6, 136.8, 147, 151.9]

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(everyTwoYears, numOfHouseholdsWithPets, color="red", marker="o", linewidth=3, markersize=8)
ax2.plot(everyYear, petCareSpending, color="blue", marker="o", linewidth=3, markersize=8)

ax1.set_xlabel("Years", fontsize=16)
ax1.set_ylabel("# of Households with Pets (millions)", color="red", fontsize=15)
ax1.set_yticks(np.arange(50,101,10))
ax2.set_ylabel("Spending on Pets (billion USD)", color="blue", fontsize=16)

plt.show()