import math
import numpy as np
import matplotlib.pyplot as plt

w0 = 57.77
t = 0.0326
p = 1.0
k = 0.1
alpha = 3.66
beta = math.e   # not used in the closed-form solutions here
gamma = 0.15

# ------------------------------------------------------------
# Closed-form solutions from Model 2
# n* = alpha(1-gamma) / (w t + k)
# c* = gamma(w t + k) / (p(1-gamma))
#
# Decomposition terms:
# monetary expenditure = p c* n*
# time opportunity cost = w t n*
# fixed cost = k n*
# total pet cost = p c* n* + w t n* + k n*
# ------------------------------------------------------------

def n_star(w: np.ndarray) -> np.ndarray:
    """Optimal pet quantity."""
    return alpha * (1.0 - gamma) / (w * t + k)

def c_star(w: np.ndarray) -> np.ndarray:
    """Optimal caregiving intensity."""
    return gamma * (w * t + k) / (p * (1.0 - gamma))

def monetary_expenditure(w: np.ndarray) -> np.ndarray:
    """p c* n*"""
    return p * c_star(w) * n_star(w)

def time_opportunity_cost(w: np.ndarray) -> np.ndarray:
    """w t n*"""
    return w * t * n_star(w)

def fixed_cost_component(w: np.ndarray) -> np.ndarray:
    """k n*"""
    return k * n_star(w)

def total_pet_cost(w: np.ndarray) -> np.ndarray:
    """Total pet-related cost."""
    return (
        monetary_expenditure(w)
        + time_opportunity_cost(w)
        + fixed_cost_component(w)
    )

# ------------------------------------------------------------
# Wage range for visualization
# You can adjust these as needed.
# ------------------------------------------------------------
w_min = 20
w_max = 80
w = np.linspace(w_min, w_max, 400)

# Compute components
n_vals = n_star(w)
c_vals = c_star(w)

monetary_vals = monetary_expenditure(w)
time_vals = time_opportunity_cost(w)
fixed_vals = fixed_cost_component(w)
total_vals = total_pet_cost(w)

# Reference values at the user's baseline wage
baseline_n = n_star(np.array([w0]))[0]
baseline_c = c_star(np.array([w0]))[0]
baseline_monetary = monetary_expenditure(np.array([w0]))[0]
baseline_time = time_opportunity_cost(np.array([w0]))[0]
baseline_fixed = fixed_cost_component(np.array([w0]))[0]
baseline_total = total_pet_cost(np.array([w0]))[0]

print("Baseline parameter values")
print(f"w = {w0:.2f}, t = {t}, p = {p}, k = {k}, alpha = {alpha}, gamma = {gamma}")
print()
print("Baseline optimal choices at w0")
print(f"n* = {baseline_n:.4f}")
print(f"c* = {baseline_c:.4f}")
print()
print("Baseline expenditure decomposition at w0")
print(f"Monetary expenditure p*c*n = {baseline_monetary:.4f}")
print(f"Time opportunity cost w*t*n = {baseline_time:.4f}")
print(f"Fixed cost k*n = {baseline_fixed:.4f}")
print(f"Total pet cost = {baseline_total:.4f}")

# ------------------------------------------------------------
# Figure 1: stacked area plot
# ------------------------------------------------------------
fig1, ax1 = plt.subplots(figsize=(9, 6))

ax1.stackplot(
    w,
    monetary_vals,
    time_vals,
    fixed_vals,
    labels=[
        r"Monetary expenditure $pc^*n^*$",
        r"Time opportunity cost $wt\,n^*$",
        r"Fixed cost $kn^*$"
    ],
    alpha=0.85
)

ax1.axvline(w0, linestyle="--", linewidth=1)
ax1.text(
    w0 + 0.8,
    total_vals.max() * 0.92,
    f"Baseline wage = {w0:.2f}",
    fontsize=10
)

ax1.set_xlabel("Hourly wage rate (w)", fontsize=12)
ax1.set_ylabel("Pet-related cost", fontsize=12)
ax1.set_title("Model 2: Expenditure Decomposition (Stacked Area)", fontsize=14)
ax1.legend(frameon=True)
ax1.grid(True, alpha=0.3)

plt.tight_layout()

# ------------------------------------------------------------
# Figure 2: line plot of components + total
# ------------------------------------------------------------
fig2, ax2 = plt.subplots(figsize=(9, 6))

ax2.plot(w, monetary_vals, label=r"Monetary expenditure $pc^*n^*$", linewidth=2)
ax2.plot(w, time_vals, label=r"Time opportunity cost $wt\,n^*$", linewidth=2)
ax2.plot(w, fixed_vals, label=r"Fixed cost $kn^*$", linewidth=2)
ax2.plot(w, total_vals, label="Total pet cost", linewidth=2.5, linestyle="--")

ax2.axvline(w0, linestyle="--", linewidth=1)
ax2.scatter(
    [w0, w0, w0, w0],
    [baseline_monetary, baseline_time, baseline_fixed, baseline_total],
    s=35,
    zorder=3
)

ax2.annotate(
    f"{baseline_monetary:.2f}",
    (w0, baseline_monetary),
    xytext=(6, 6),
    textcoords="offset points",
    fontsize=9
)
ax2.annotate(
    f"{baseline_time:.2f}",
    (w0, baseline_time),
    xytext=(6, 6),
    textcoords="offset points",
    fontsize=9
)
ax2.annotate(
    f"{baseline_fixed:.2f}",
    (w0, baseline_fixed),
    xytext=(6, 6),
    textcoords="offset points",
    fontsize=9
)
ax2.annotate(
    f"{baseline_total:.2f}",
    (w0, baseline_total),
    xytext=(6, 6),
    textcoords="offset points",
    fontsize=9
)

ax2.set_xlabel("Hourly wage rate (w)", fontsize=12)
ax2.set_ylabel("Pet-related cost", fontsize=12)
ax2.set_title("Model 2: Expenditure Decomposition (Line Plot)", fontsize=14)
ax2.legend(frameon=True)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# Optional: save figures
# Uncomment if you want image files.
# ------------------------------------------------------------
# fig1.savefig("model2_expenditure_decomposition_stacked_area.png", dpi=300, bbox_inches="tight")
# fig2.savefig("model2_expenditure_decomposition_lines.png", dpi=300, bbox_inches="tight")