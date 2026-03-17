import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def specificni_toplinski_kapacitet1():
    T=[[24,25,26,27,28,29,30,31,32],
       [25,26,27,28,29,30,31,32,33],
       [25,26,27,28,29,30,31,32,33]]
    t=[[0,190,410,624,825,1043,1266,1478,1706],
       [0,177,398,609,823,1042,1273,1505,1751],
       [0,150,303,456,608,763,927,1097,1263]]
    U=[9,9.5,10]
    I=[1.18,1.24,1.33]
    m=[0.499,0.574,0.466]
    mCAL=0.093
    cCAL=897
    Vt=1
    R=7.3
    cv_1=[[0 for _ in range(8)] for _ in range(3)]
    cv_avg=[0 for _ in range(3)]    
    cv_1_err=[[0 for _ in range(8)] for _ in range(3)]
    cv_1_err_avg=[0 for _ in range(3)]  
    for i in range(3):
        for j in range(1,9):
            cv_1[i][j-1] = I[i]*U[i]*t[i][j]/((T[i][j]-T[i][0])*m[i])-(mCAL*cCAL+Vt*1.9)/m[i]
            cv_1_err[i][j-1] = (I[i]*U[i])/((T[i][j]-T[i][0])*m[i])*5
    for i in range(3):
        cv_avg[i] = sum(cv_1[i])/8
        cv_1_err_avg[i] = sum(cv_1_err[i])/8
    print(cv_1)
    print(cv_avg)
    print(cv_1_err)
    print(cv_1_err_avg)
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def specificni_toplinski_kapacitet2_regresija():
    T = [np.array([24,25,26,27,28,29,30,31,32]),
         np.array([25,26,27,28,29,30,31,32,33]),
         np.array([25,26,27,28,29,30,31,32,33])]
    t = [np.array([0,190,410,624,825,1043,1266,1478,1706]),
         np.array([0,177,398,609,823,1042,1273,1505,1751]),
         np.array([0,150,303,456,608,763,927,1097,1263])]
    U = [9.0, 9.5, 10.0]  
    I = [1.18, 1.24, 1.33] 
    m = [0.499, 0.574, 0.466] 

    def linear_model(x, a, b):
        return a * x + b

    C_uk_list = []
    sigma_Cuk_list = []

    plt.figure(figsize=(10, 6))
    colors = ['blue', 'green', 'red']

    for i in range(3):
        fit_params, covariance_matrix = curve_fit(linear_model, t[i], T[i])
        a_fit, b_fit = fit_params
        sigma_a = np.sqrt(covariance_matrix[0,0]) 
        P = U[i] * I[i] 
        C_uk = P / a_fit
        sigma_Cuk = (P / (a_fit**2)) * sigma_a

        C_uk_list.append(C_uk)
        sigma_Cuk_list.append(sigma_Cuk)

        plt.scatter(t[i], T[i], color=colors[i], label=f'Set {i+1} (m={m[i]}kg)')
        plt.plot(t[i], linear_model(t[i], *fit_params), color=colors[i], linestyle='--')
        
        print(f"Set {i+1}: a = {a_fit:.5f} ± {sigma_a:.5f}, C_uk = {C_uk:.2f} ± {sigma_Cuk:.2f} J/K")

    print("-" * 30)

    def izracun_cv(i, j):
        delta_Cuk = C_uk_list[j] - C_uk_list[i]
        delta_m = m[j] - m[i]
        cv = delta_Cuk / delta_m
        sigma_cv = np.sqrt(sigma_Cuk_list[i]**2 + sigma_Cuk_list[j]**2) / abs(delta_m)
        
        return cv, sigma_cv

    for a in range(0, 2):
        for b in range(a+1, 3):
            cv_vode, s_cv_vode = izracun_cv(a, b)
            print(f"Specifični toplinski kapacitet vode (Set {a+1} & Set {b+1}):")
            print(f"cv = {cv_vode:.2f} ± {s_cv_vode:.2f} J/(kg K)")
            print("-" * 30)


    plt.xlabel('Vrijeme t [s]')
    plt.ylabel('Temperatura T [°C]')
    plt.title('Linearna regresija po setovima mjerenja')
    plt.legend()
    plt.grid(True)
    plt.show()




    


specificni_toplinski_kapacitet1()
specificni_toplinski_kapacitet2_regresija()