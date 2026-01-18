import math as mt
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

lista_n2=[np.log(14),np.log(13),np.log(12),np.log(11),np.log(10),np.log(9),np.log(8),np.log(7),np.log(6),np.log(5),np.log(4)]
lista_n1_2=[np.log(10),np.log(9),np.log(8),np.log(7),np.log(6),np.log(5),np.log(4),np.log(3)]
lista_n1=[np.log(7),np.log(6),np.log(5),np.log(4),np.log(3),np.log(2)]
lista_m2=[np.log(22e-3),np.log(24e-3),np.log(27e-3),np.log(35e-3),np.log(41e-3),np.log(53e-3),np.log(66e-3),np.log(92e-3),np.log(122e-3),np.log(180e-3),np.log(302e-3)]
lista_m1_2=[np.log(23e-3),np.log(32e-3),np.log(39e-3),np.log(49e-3),np.log(73e-3),np.log(108e-3),np.log(165e-3),np.log(316e-3)]
lista_m1=[np.log(18e-3),np.log(29e-3),np.log(40e-3),np.log(75e-3),np.log(134e-3),np.log(321e-3)]
lista_m=[np.log(180e-3),np.log(108e-3),np.log(40e-3)]
lista_L=[np.log(2),np.log(1.5),np.log(1)]
def linearn_fit(x,a,b):
    return a*x + b
fit2, covarijanca2 = curve_fit(linearn_fit, lista_n2, lista_m2)
fit1_2, covarijanca1_2 = curve_fit(linearn_fit, lista_n1_2, lista_m1_2)
fit1, covarijanca1 = curve_fit(linearn_fit, lista_n1, lista_m1)
fit, covarijanca = curve_fit(linearn_fit, lista_L, lista_m)

a2, b2 = fit2
a1_2, b1_2 = fit1_2
a1, b1 = fit1
a, b = fit

a2_err, b2_err = np.sqrt(np.diag(covarijanca2))
a1_2_err, b1_2_err = np.sqrt(np.diag(covarijanca1_2))
a1_err, b1_err = np.sqrt(np.diag(covarijanca1))
a_err, b_err = np.sqrt(np.diag(covarijanca))

korelacija_ab2 = covarijanca2[0, 1] / (a2_err * b2_err)
korelacija_ab1_2 = covarijanca1_2[0, 1] / (a1_2_err * b1_2_err)
korelacija_ab1 = covarijanca1[0, 1] / (a1_err * b1_err)
korelacija_ab= covarijanca[0, 1] / (a_err * b_err)

x2_fit = np.linspace(min(lista_n2), max(lista_n2), 100)
y2_fit = linearn_fit(x2_fit, a2, b2)

x1_2_fit = np.linspace(min(lista_n1_2), max(lista_n1_2), 100)
y1_2_fit = linearn_fit(x1_2_fit, a1_2, b1_2)

x1_fit = np.linspace(min(lista_n1), max(lista_n1), 100)
y1_fit = linearn_fit(x1_fit, a1, b1)

x_fit= np.linspace(min(lista_L), max(lista_L), 100)
y_fit= linearn_fit(x_fit, a, b)

residuali2 = lista_m2 - linearn_fit(np.array(lista_n2), a2, b2)
residuali1_2 = lista_m1_2 - linearn_fit(np.array(lista_n1_2), a1_2, b1_2)
residuali1 = lista_m1 - linearn_fit(np.array(lista_n1), a1, b1)
residuali= lista_m - linearn_fit(np.array(lista_L), a, b)

y2_fit_error = np.sqrt((x2_fit * a2_err) ** 2 + b2_err ** 2)
y1_2_fit_error = np.sqrt((x1_2_fit * a1_2_err) ** 2 + b1_2_err ** 2)
y1_fit_error = np.sqrt((x1_fit * a1_err) ** 2 + b1_err ** 2)
y_fit_error = np.sqrt((x_fit * a_err) ** 2 + b_err ** 2)

plt.scatter(lista_n2, lista_m2, label='Podaci (log-log)', color='blue')
plt.plot(x2_fit, y2_fit, label=f'Fit: y = {a2:.2f}x + {b2:.2f}', color='orange')
plt.fill_between(x2_fit, y2_fit - y2_fit_error, y2_fit + y2_fit_error, 
                 color='orange', alpha=0.2, label=r'Interval pouzdanosti ($\pm$ 1$\sigma$)')
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.xlabel('log(n)', fontsize=25)
plt.ylabel('log(m)', fontsize=25)
plt.title('Linearna regresija s intervalom pouzdanosti', fontsize=30)
plt.legend(fontsize=25)
plt.grid(True)
plt.show()

plt.scatter(lista_n1_2, lista_m1_2, label='Podaci (log-log)', color='green')
plt.plot(x1_2_fit, y1_2_fit, label=f'Fit: y = {a1_2:.2f}x + {b1_2:.2f}', color='orange')
plt.fill_between(x1_2_fit, y1_2_fit - y1_2_fit_error, y1_2_fit + y1_2_fit_error, 
                 color='orange', alpha=0.2, label=r'Interval pouzdanosti ($\pm$ 1$\sigma$)')
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.xlabel('log(n)', fontsize=25)
plt.ylabel('log(m)', fontsize=25)
plt.title('Linearna regresija s intervalom pouzdanosti', fontsize=30)
plt.legend(fontsize=25)
plt.grid(True)
plt.show()

plt.scatter(lista_n1_2, lista_m1_2, label='Podaci (log-log)', color='green')
plt.plot(x1_2_fit, y1_2_fit, label=f'Fit: y = {a1_2:.2f}x + {b1_2:.2f}', color='orange')
plt.fill_between(x1_2_fit, y1_2_fit - y1_2_fit_error, y1_2_fit + y1_2_fit_error, 
                 color='orange', alpha=0.2, label=r'Interval pouzdanosti ($\pm$ 1$\sigma$)')
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.xlabel('log(n)', fontsize=25)
plt.ylabel('log(m)', fontsize=25)
plt.title('Linearna regresija s intervalom pouzdanosti', fontsize=30)
plt.legend(fontsize=25)
plt.grid(True)
plt.show()

plt.scatter(lista_n1, lista_m1, label='Podaci (log-log)', color='red')
plt.plot(x1_fit, y1_fit, label=f'Fit: y = {a1:.2f}x + {b1:.2f}', color='orange')
plt.fill_between(x1_fit, y1_fit - y1_fit_error, y1_fit + y1_fit_error, 
                 color='orange', alpha=0.2, label=r'Interval pouzdanosti ($\pm$ 1$\sigma$)')
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.xlabel('log(n)', fontsize=25)   
plt.ylabel('log(m)', fontsize=25)
plt.title('Linearna regresija s intervalom pouzdanosti', fontsize=30)
plt.legend(fontsize=25)
plt.grid(True)
plt.show()

plt.scatter(lista_L, lista_m, label='Podaci (L vs m)', color='purple')
plt.plot(x_fit, y_fit, label=f'Fit: y = {a:.2f}x + {b:.2f}', color='orange')
plt.fill_between(x_fit, y_fit - y_fit_error, y_fit + y_fit_error, 
                 color='orange', alpha=0.2, label=r'Interval pouzdanosti ($\pm$ 1$\sigma$)')
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.xlabel('log(L)', fontsize=25)        
plt.ylabel('log(m)', fontsize=25)
plt.title('Linearna regresija s intervalom pouzdanosti', fontsize=30)
plt.legend(fontsize=25)
plt.grid(True)
plt.show()

print(f" Fit rezultati za L=2m:")
print(f" a2 = {a2:.2f} ± {a2_err:.2f}")
print(f" b2 = {b2:.2f} ± {b2_err:.2f}")
print(f" Korelacija ab2 = {korelacija_ab2:.4f}")

print(f" Fit rezultati za L=1.5m:")
print(f" a1_2 = {a1_2:.2f} ± {a1_2_err:.2f}")
print(f" b1_2 = {b1_2:.2f} ± {b1_2_err:.2f}")
print(f" Korelacija ab1_2 = {korelacija_ab1_2:.4f}")

print(f" Fit rezultati za L=1m:")
print(f" a1 = {a1:.2f} ± {a1_err:.2f}")
print(f" b1 = {b1:.2f} ± {b1_err:.2f}")
print(f" Korelacija ab1 = {korelacija_ab1:.4f}")

print(f" Fit rezultati za n=5:")
print(f" a = {a:.2f} ± {a_err:.2f}")    
print(f" b = {b:.2f} ± {b_err:.2f}")
print(f" Korelacija ab = {korelacija_ab:.4f}")