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

# Keep only rows where each series exists
hh_df = df.dropna(subset=["hh"])
spending_df = df.dropna(subset=["spending"])

# Plot
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

# 
# # Plot
# plt.figure(figsize=(8, 5))
# 
# plt.plot(df["year"], df["hh"], marker='o', label="Households (hh)")
# plt.plot(df["year"], df["spending"], marker='o', label="Spending")
# 
# # Labels and title
# plt.xlabel("Year")
# plt.ylabel("Value")
# plt.title("Households and Spending Over Time")
# 
# # Legend
# plt.legend()
# 
# # Grid (optional but nice)
# plt.grid(True)
# 
# # Show plot
# plt.show()