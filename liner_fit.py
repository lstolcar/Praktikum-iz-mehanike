import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# =====================
# 1. Example Data (ln(x), ln(y)) from Exercise 1.
# =====================
x_data = np.array([2.079, 1.946, 1.792, 1.609, 1.386, 1.099, 0.693])
y_data = np.array([2.996, 3.219, 3.689, 4.094, 4.500, 4.942, 5.704])
# if taking errors into account, i.e. weighted fit (w = 1/sigma_y**2)
# y_error = y_data * 0.10 #(for example, 10% error, input real values)

# =====================
# 2. Linear Fit Function
# =====================
def linear_model(x, a, b):
    return a * x + b

# ===========================
# 3. Perform the Fit
# ===========================

# Optional: define initial guess for parameters if known (e.g., a=-2, b=0)
initial_guess = [-2.0, 0.0]  # You can adjust or comment this if unknown

# Optional: include measurement uncertainties in y
# For example, assume 10% relative uncertainty:
# y_error = 0.1 * y_data

# --------------------------------------
# Fitting options:
# Choose ONE of the following by commenting/uncommenting
# --------------------------------------

# --- (1) Unweighted fit, no initial guess --- 
# fit_params, covariance_matrix = curve_fit(linear_model, x_data, y_data)

# --- (2) Unweighted fit, with initial guess ---
# fit_params, covariance_matrix = curve_fit(linear_model, x_data, y_data, p0=initial_guess)

# --- (3) Weighted fit, with initial guess ---
# fit_params, covariance_matrix = curve_fit(
#     linear_model,
#     x_data,
#     y_data,
#     sigma=y_error,         # Pass y-errors directly
#     absolute_sigma=True,   # Ensures proper uncertainty scaling
#     p0=initial_guess
# )

# --- (4) Weighted fit, without initial guess ---
#fit_params, covariance_matrix = curve_fit(
#    linear_model,
#    x_data,
#    y_data,
#    sigma=y_error,         # Comment out this line if not using weights
#    absolute_sigma=True    # Use only if sigma is defined
#    # p0=initial_guess     # Uncomment this line to use initial guess
#)

# Let's use the simplest option, no weights, no initial guess:
fit_params, covariance_matrix = curve_fit(linear_model, x_data, y_data)

# Extract fit parameters and their uncertainties
a_fit, b_fit = fit_params
a_error, b_error = np.sqrt(np.diag(covariance_matrix))

# Compute the correlation coefficient between a and b
correlation_ab = covariance_matrix[0, 1] / (a_error * b_error)

# =====================
# 4a. Evaluate Fit and Uncertainties
# =====================

# Evaluate the model in (x,y) mash grid using best-fit parameters
x_fit = np.linspace(min(x_data), max(x_data), 200)
y_fit = linear_model(x_fit, a_fit, b_fit)

# Compute residuals between data and model
residuals = y_data - linear_model(x_data, a_fit, b_fit)

# -------------------------
# Linear Error Propagation (with covariance term)
# -------------------------
# General formula for propagation of uncertainties:
# For any function y = f(a, b, ...), the variance is given by:
#
# note err = sigma, df/da = derivation
# err_y^2 = (df/da)^2 * err_a^2 + (df/db)^2 * err_b^2 + 2 * (df/da)(df/db) * Cov(a, b)
#
# In our case, for a linear model y = a*x + b:
#   df/da = x
#   df/db = 1
# so the expression becomes:
# 
# err_y(x)^2 = (x * err_a)^2 + err_b^2 + 2 * x * Cov(a, b)
#
# This equation gives the uncertainty in the fitted line y(x), 
# including the effect of correlation between parameters a and b.
# -------------------------

# err_y(x)^2 = (x * err_a)^2 + err_b^2 + 2 * x * Cov(a, b)
y_fit_error = np.sqrt((x_fit * a_error) ** 2 + b_error ** 2 + 2 * x_fit * covariance_matrix[0, 1])

# Note: if Cov(a, b) < 0 as is in this case, total uncertainty (shaded area) is reduced.
# This reflects anti-correlation between parameters: change in one is offset by the other.
# You can check the difference by commenting out y_fit_error and uncommenting the one below

#
# Note: +/- 1 sigma = 68.27 %, +/- 2 sigma = 95.45 %, +/- 3 sigma = 99.73 % 
#

# =====================
# 4b. Evaluate Fit and Uncertainties -> approx. formula (simplification)
#     without taking parameter correlation into account
# =====================

# 1-sigma confidence interval (approximate, assuming linear, independent, error propagation)
# err_y(x)^2 = (x * err_a)^2 + err_b^2

# y_fit_error = np.sqrt((x_fit * a_error) ** 2 + b_error ** 2)

# Note: For nonlinear models (e.g. Gaussian, exponential), 
# confidence intervals require more advanced methods 
# than simple linear error propagation.


# =====================
# 5. Plot: Data + Fit + Confidence Interval
# =====================

plt.figure(figsize=(10, 8))
plt.subplot(2, 1, 1)
plt.scatter(x_data, y_data, label='Data (log-log)', color='blue')
plt.plot(x_fit, y_fit, label=f'Fit: y = {a_fit:.2f}x + {b_fit:.2f}', color='orange')
plt.fill_between(x_fit, y_fit - y_fit_error, y_fit + y_fit_error, 
                 color='orange', alpha=0.2, label=r'Confidence Interval ($\pm$ 1$\sigma$)')
plt.xlabel('log(x)', fontsize=14)
plt.ylabel('log(y)', fontsize=14)
plt.title('Linear Fit with Confidence Interval', fontsize=16)
plt.legend(fontsize=12)
plt.grid(True)

# =====================
# 6. Plot: Residuals
# =====================

plt.subplot(2, 1, 2)
plt.scatter(x_data, residuals, color='red', label='Residuals')
plt.axhline(0, color='black', linestyle='--')
plt.xlabel('log(x)', fontsize=14)
plt.ylabel('Residuals', fontsize=14)
plt.title('Residual Plot', fontsize=16)
plt.legend(fontsize=12)
plt.grid(True)

plt.tight_layout()
plt.show()

# =====================
# 7. Print Results
# =====================

print(f" Fit results:")
print(f"   a (slope)     = {a_fit:.4f} ± {a_error:.4f}")
print(f"   b (intercept) = {b_fit:.4f} ± {b_error:.4f}")
print(f"   Correlation (a, b) = {correlation_ab:.4f}")