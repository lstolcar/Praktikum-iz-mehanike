import numpy as np
import matplotlib.pyplot as plt

l = np.array([2400, 2100, 1800, 1400, 1000])
sigma_r = 0.5  

r_data = {
    1: np.array([7.15, 6.64, 6.35, 5.83, 4.58]),
    2: np.array([12.61, 11.96, 11.20, 10.18, 8.71]),
    3: np.array([16.52, 15.56, 14.36, 12.92, 11.10]),
    4: np.array([19.62, 18.39, 17.08, 15.31, 13.28]),
    5: np.array([22.22, 20.89, 19.49, 17.50, 14.72]),
}


lambda_laser = 632.8e-6



r0 = []
sigma_r0 = []
n_values = []

plt.figure(figsize=(7, 5))

for n, r in r_data.items():

    popt, pcov = np.polyfit(
        l, r, 1,
        w=np.ones_like(r) / sigma_r,
        cov=True
    )

    a, intercept = popt
    sigma_intercept = np.sqrt(pcov[1, 1])

    r0.append(intercept)
    sigma_r0.append(sigma_intercept)
    n_values.append(n)

    l_fit = np.linspace(min(l), max(l), 200)
    plt.errorbar(l, r, yerr=sigma_r, fmt='o')
    plt.plot(l_fit, a * l_fit + intercept, label=f"n = {n}")

plt.xlabel("l [mm]", fontsize=25)
plt.ylabel(r"$r_n(l)$ [mm]",fontsize=25)
plt.title("Ekstrapolacija $r_n(0)$", fontsize=30)
plt.legend(fontsize=20)
plt.grid()
plt.show()

r0 = np.array(r0)
sigma_r0 = np.array(sigma_r0)
n_values = np.array(n_values)



r0_sq = r0**2
sigma_r0_sq = 2 * r0 * sigma_r0
x = n_values * lambda_laser
popt, pcov = np.polyfit(
    x, r0_sq, 1,
    w=1 / sigma_r0_sq,
    cov=True
)

R, C = popt
sigma_R = np.sqrt(pcov[0, 0])
sigma_C = np.sqrt(pcov[1, 1])

plt.figure(figsize=(7, 5))
plt.errorbar(x, r0_sq, yerr=sigma_r0_sq, fmt='o', label="Podaci")
plt.plot(x, R * x + C, label="Linearni fit")
plt.xlabel(r"$n\lambda$ [m]",fontsize=25)
plt.ylabel(r"$r_n^2$ [m$^2$]",fontsize=25)
plt.title(r"Ovisnost $r_n^2$ o $n\lambda$", fontsize=30)
plt.legend(fontsize=20)
plt.grid()
plt.show()

print("Ekstrapolirani polumjeri:")
for n, val, err in zip(n_values, r0, sigma_r0):
    print(f"n = {n}: r_n(0) = ({val:.3e} ± {err:.3e}) mm")

print("\nLinearni fit:")
print(r"$r_n^2 = R\,(n\lambda) + C$")
print(f"R = ({R:.3e} ± {sigma_R:.3e}) mm")
print(f"C = ({C:.3e} ± {sigma_C:.3e}) mm^2")


