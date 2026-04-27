import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
patm1 = 102200  
patm2 = 102100  
T_amb = 26.1 + 273.15  
T_std = 273.15  
p_std = 101325  
V_std_mol = 0.022414  
r = (11.4e-3) / 2  

def model_zero(x, a):
    return a * x

l1 = np.array([12.7, 11.7, 11.2, 10.8, 10.3, 9.9, 9.6, 9.4, 9.0, 8.8]) * 1e-2
h1 = np.array([0.4, 3.9, 8.0, 10.1, 15.0, 18.1, 19.9, 21.9, 25.2, 27.0]) * 10 

V1 = np.pi * r**2 * l1 + 1.01e-6 
p1 = patm1 + h1 * 133.3         
inv_p1 = 1 / p1
popt1, _ = curve_fit(model_zero, inv_p1, V1)
a_boyle = popt1[0]

ni = (p1 * V1 * T_std) / (p_std * V_std_mol * T_amb)
n_mean = np.mean(ni)
R1 = a_boyle / (n_mean * T_amb)

T_C = np.array([30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])
T_K = T_C + 273.15

l2 = np.array([12.8, 13.0, 13.2, 13.4, 13.6, 13.8, 14.0, 14.2, 14.4, 14.6, 14.8]) * 1e-2
h2 = np.array([0.2, 1.1, 2.5, 3.6, 4.7, 6.0, 7.5, 8.5, 9.6, 11.2, 12.7]) * 10

V2 = np.pi * r**2 * l2 + 1.01e-6
p2 = patm2 + h2 * 133.3

popt_p, _ = curve_fit(model_zero, T_K, p2)
c_slope = popt_p[0]

popt_V, _ = curve_fit(model_zero, T_K, V2)
b_slope = popt_V[0]

p_const = patm2
V_const = np.pi * r**2 * 12.5*1e-2 + 1.01e-6

R2 = b_slope * p_const / n_mean
R3 = c_slope * V_const / n_mean
V0 = b_slope * 273.15
p0 = c_slope * 273.15

alpha0 = b_slope / V0
beta0 = c_slope / p0

print("-" * 40)
print("JEDNADŽBE FITA (prolaz kroz ishodište):")
print(f"Boyle-Mariotte: V = {a_boyle:.4f} * (1/p)")
print(f"Gay-Lussac:     p = {c_slope:.2f} * T")
print(f"Charles:        V = {b_slope:.2e} * T")
print("-" * 40)
print(f"Srednji broj molova n: {n_mean:.6e} mol")
print(f"R1 (Boyle):     {R1:.3f} J/(mol K)")
print(f"R2 (Charles):   {R2:.3f} J/(mol K)")
print(f"R3 (Gay-Lussac): {R3:.3f} J/(mol K)")
print(f"alpha0:         {alpha0:.6f} K^-1")
print(f"beta0:          {beta0:.6f} K^-1")
print("-" * 40)

plt.figure(1)
plt.scatter(inv_p1, V1, color='blue', label='Mjerenja')
plt.plot(inv_p1, model_zero(inv_p1, a_boyle), color='red',  label=f'V = {a_boyle:.2f} * (1/p)')
plt.xlabel('1/p [Pa^-1]', fontsize=25)
plt.ylabel('V [m^3]', fontsize=25)
plt.title('Boyle-Mariotteov zakon (V vs 1/p)', fontsize=25)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.legend(fontsize=25)
plt.grid(True)

plt.figure(2)
plt.scatter(T_K, p2, color='orange', label='Mjerenja')
plt.plot(T_K, model_zero(T_K, c_slope), color='black', label=f'p = {c_slope:.2f} * T')
plt.xlabel('T [K]', fontsize=25)
plt.ylabel('p [Pa]', fontsize=25)
plt.title('Gay-Lussacov zakon (p vs T)', fontsize=25)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.legend(fontsize=25)
plt.grid(True)

plt.figure(3)
plt.scatter(T_K, V2, color='green', label='Mjerenja')
plt.plot(T_K, model_zero(T_K, b_slope), color='blue',  label=f'V = {b_slope:.2e} * T')
plt.xlabel('T [K]', fontsize=25)
plt.ylabel('V [m^3]', fontsize=25)
plt.title('Charlesov zakon (V vs T)', fontsize=25)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.legend(fontsize=25)
plt.grid(True)

plt.show()