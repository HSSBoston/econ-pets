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

plt.figure(figsize=(9, 5))

plt.plot(hh_df["year"], hh_df["hh"],
         marker="o", linewidth=2, label="hh")

plt.plot(spending_df["year"], spending_df["spending"],
         marker="s", linewidth=2, label="spending")

plt.xlabel("Year")
plt.ylabel("Value")
plt.title("hh and spending over years")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
