import numpy as np
import matplotlib.pyplot as plt

everyYear = [2014, 2016, 2018, 2019, 2020, 2021, 2022, 2024]
numOfHouseholdsWithPetsYears = [2014, 2016, 2018, 2020, 2022, 2024]

numOfHouseholdsWithPets = [79.7, 84.6, 84.9, 90.5, 86.9, 94]
petCareSpending = [58.04, 62, 90.5, 97.1, 103.6, 123.6, 136.8, 151.9]

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(numOfHouseholdsWithPetsYears, numOfHouseholdsWithPets,
         color="red", marker="o", linewidth=3, markersize=8)
ax2.plot(everyYear, petCareSpending,
         color="blue", marker="o", linewidth=3, markersize=8)

ax1.set_xlabel("Years", fontsize=20)
ax1.set_ylabel("# of Households w/ Pets (M)", color="red", fontsize=20)
ax1.set_yticks(np.arange(50,101,10))
ax2.set_ylabel("Pet Expenditure ($bn)", color="blue", fontsize=20)
ax2.set_yticks(np.arange(50,151,10))

ax1.tick_params(axis='both', labelsize=16)
ax2.tick_params(axis='both', labelsize=16)

# plt.tick_params(labelsize=16)
# plt.rcParams["font.size"] = 16

plt.show()