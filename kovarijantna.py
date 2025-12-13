from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
def model(x, a, b):
    return a + b*x
x_data = np.array([...])
y_data = np.array([...])
popt, pcov = curve_fit(model, x_data, y_data)
# popt: best-fit values of a and b
# pcov: 2x2 covariance matrix
# Extract best-fit parameters and their uncertainties
a, b = popt
# Standard deviations (errors)
a_err, b_err = np.sqrt(np.diag(pcov))
print(f"a = {a:.4f} ± {a_err:.4f}")
print(f"b = {b:.4f} ± {b_err:.4f}")
# Calculate and print correlation coefficient
correlation_ab = pcov[0, 1] / (a_err * b_err)
print(f"Correlation (a, b) = {correlation_ab:.4f}")
# Compute residuals as difference between
# the data values and ones extracted from fit
y_fit = model(x_data, a, b)
residuals = y_data - y_fit
# Plot residuals
plt.figure()
plt.scatter(x_data, residuals, marker='o', color='red')
plt.axhline(0, color='black', linestyle='--')
plt.xlabel("x")
plt.ylabel("Residuals (y - fit)")
plt.title("Residuals of the Linear Fit")
plt.grid(True)
plt.show()