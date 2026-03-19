# The first CSV row must have the header. Its column labels must be
# "year", "hh", and "spending" for the first, second, and third columns.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/hh-spending.csv")
print(df.head())

# Make "year", "hh" and "spending" numeric
df["year"]     = pd.to_numeric(df["year"], errors="coerce")
# df = df.sort_values("year").reset_index(drop=True)
df["hh"]       = pd.to_numeric(df["hh"], errors="coerce")
df["spending"] = pd.to_numeric(df["spending"], errors="coerce")

# Remove rows that have empty cells and make yy-hh data frame
hhDf       = df.dropna(subset=["hh"])
# Remove rows that have empty cells and make yy-spending data frame
spendingDf = df.dropna(subset=["spending"])

# plt.figure(figsize=(9, 5))

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# plt.plot(hh_df["year"], hh_df["hh"],
#          marker="o", linewidth=2, label="hh")
# 
# plt.plot(spending_df["year"], spending_df["spending"],
#          marker="s", linewidth=2, label="spending")

ax1.plot(numOfHouseholdsWithPetsYears, numOfHouseholdsWithPets,
         color="red", marker="o", linewidth=3, markersize=8)
ax2.plot(everyYear, petCareSpending,
         color="blue", marker="o", linewidth=3, markersize=8)

ax1.set_xlabel("Years", fontsize=20)
ax1.set_ylabel("# of Households w/ Pets (M)", color="red", fontsize=20)
ax1.set_yticks(np.arange(70,101,5))
ax2.set_ylabel("Pet Expenditure ($bn)", color="blue", fontsize=20)
ax2.set_yticks(np.arange(50,151,10))

ax1.tick_params(axis='both', labelsize=16)
ax2.tick_params(axis='both', labelsize=16)

# plt.tick_params(labelsize=16)
# plt.rcParams["font.size"] = 16

plt.show()



# plt.xlabel("Year")
# plt.ylabel("Value")
# plt.title("hh and spending over years")
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()
