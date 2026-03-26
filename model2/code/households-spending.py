import numpy as np
import matplotlib.pyplot as plt


everyYear = [2014, 2016, 2018, 2019, 2020, 2021, 2022, 2024]
numOfHouseholdsWithPetsYears = [2014, 2016, 2018, 2020, 2021, 2022, 2024]

numOfHouseholdsWithPets = [79.7, 84.6, 84.9, 90.5, 90.9, 86.9, 94]
petCareSpending = [58.04, 62, 90.5, 97.1, 103.6, 123.6, 136.8, 151.9]

fig, ax1 = plt.subplots(figsize=(4, 4))
ax2 = ax1.twinx()

ax1.plot(numOfHouseholdsWithPetsYears, numOfHouseholdsWithPets,
         color="red", marker="o", linewidth=3, markersize=8, zorder=5)
ax2.plot(everyYear, petCareSpending,
         color="blue", marker="o", linewidth=3, markersize=8)


ax1.set_xlabel("Years", fontsize=15, labelpad=0)
ax1.set_xticks([2014, 2016, 2018, 2020, 2022, 2024])
ax1.set_xticks([2015, 2017, 2019, 2021, 2023], minor=True)
ax1.set_ylabel("# of Households w/ Pets (M)", color="red", fontsize=15, labelpad=0)
ax1.set_yticks(np.arange(70,101,5))
ax2.set_ylabel("Pet Expenditure ($bn)", color="blue", fontsize=15, labelpad=0)
ax2.set_yticks(np.arange(50,151,10))

ax1.tick_params(axis='x', which='minor', direction='in', length=3)
ax1.tick_params(axis='x', which='major', direction='in', length=5)
ax2.tick_params(axis='both', direction='in')

ax1.yaxis.set_label_coords(-0.09, 0.5)

ax1.tick_params(axis='both', labelsize=12)
ax2.tick_params(axis='both', labelsize=12)

ax1.grid(axis='x', which='major', alpha=0.3)

# plt.tick_params(labelsize=16)
# plt.rcParams["font.size"] = 16

plt.tight_layout(pad=0.05)
plt.show()