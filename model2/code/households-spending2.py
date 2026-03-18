import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/hh-spending.csv")

# Preview columns (optional, helps debugging)
print(df.head())

# Plot
plt.figure(figsize=(8, 5))

plt.plot(df["year"], df["hh"], marker='o', label="Households (hh)")
plt.plot(df["year"], df["spending"], marker='o', label="Spending")

# Labels and title
plt.xlabel("Year")
plt.ylabel("Value")
plt.title("Households and Spending Over Time")

# Legend
plt.legend()

# Grid (optional but nice)
plt.grid(True)

# Show plot
plt.show()