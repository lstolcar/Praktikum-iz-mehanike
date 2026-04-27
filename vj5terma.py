import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def toplina_ukupna():
    t=[20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400]
    T=[1.3, 1.5, 1.7,1.9,2.1,2.3,2.5,2.7,2.9,3.1,3.3,3.6,3.8,4.0,4.2,4.4,4.5,4.7,4.9,5.1,5.3]
    T1=[15.3,15.3,15.7,15.8,15.8,16.0,16.2,16.3,16.4,16.5,16.6,16.7,16.9,16.9,17.0,17.2,17.2,17.4,17.4,17.6,17.7]
    T2=[47.6,47.7,47.7,47.7,47.8,47.8,47.7,47.8,48.1,48.3,48.2,48.2,48.1,48.3,48.3,48.4,48.5,48.3,48.5,48.6,48.6]
    cv=4184.4
    mv=0.3
    C=97
    Q_lista=[]
    for i in range(20):
        Q=(cv*mv+C)*(T[i+1]-T[0])
        Q_lista.append(Q)
    plt.plot(t,Q_lista)
    plt.xlabel("t (s)", fontsize=25)
    plt.ylabel("Q (J)", fontsize=25)
    plt.title("Toplina ukupna predana", fontsize=25)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid()
    plt.show()
    print(f"Ukupna toplina predana do t=400s iznosi: {Q_lista[-1]:.2f} J")
    sigma_ukupna=(T[-1]-T[0])*9
    T_okolina = [0.9, 1.1, 1.3, 1.5, 1.6, 1.8, 2, 2.2, 2.4, 2.5, 2.7]
    t_okolina = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600]
    
    cv = 4184.4
    mv = 0.3
    C = 97
    l=0.315
    A=4.91e-4
    
    
    Q_okolina_lista = []
    for i in range(10):
        Q_okolina = (cv * mv + C) * (T_okolina[i+1] - T_okolina[0])
        Q_okolina_lista.append(Q_okolina)
    

    t_np = np.array(t_okolina)
    Q_np = np.array(Q_okolina_lista)

    
    def linear_model(x, a, b):
        return a * x + b

    
    popt, pcov = curve_fit(linear_model, t_np, Q_np)
    a_fit, b_fit = popt
    a_error, b_error = np.sqrt(np.diag(pcov))

    
    t_test = 400 
    sigma_reg = np.sqrt((t_test * a_error)**2 + b_error**2)
    print(f"Nagib (a): {a_fit:.4f} +/- {a_error:.4f} J/s")
    print(f"Odsječak (b): {b_fit:.4f} +/- {b_error:.4f} J")
    print(f"Ukupna statistička pogreška u t={t_test}s iznosi: {sigma_reg:.2f} J")
    print(f"Ukupan iznos topline predane od okoline do t={t_test}s iznosi: {linear_model(t_test, *popt):.2f} J")


    plt.figure(figsize=(8, 5))
    plt.scatter(t_okolina, Q_okolina_lista, color='blue', label='Mjereni podaci') # scatter je bolji za točke
    
    
    t_range = np.linspace(min(t_okolina), max(t_okolina ), 100)
    plt.plot(t_range, linear_model(t_range, *popt), color='orange', 
             linestyle='--', label=f'Fit: Q = {a_fit:.2f}t + {b_fit:.2f}')

    plt.xlabel("t (s)", fontsize=25)
    plt.ylabel("Q (J)", fontsize=25)
    plt.title("Toplina predana od okoline s linearnom regresijom", fontsize=25)
    plt.legend()
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    plt.grid(True)
    plt.show()

    plt.plot(t_okolina, Q_okolina_lista)
    plt.xlabel("t (s)", fontsize=25)
    plt.ylabel("Q (J)", fontsize=25)
    plt.title("Toplina predana od okoline", fontsize=25)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid()
    plt.show()


    Q_stap=Q_lista[-1]-linear_model(t_test, *popt)
    print(f"Ukupna toplina predana od štapa do t={t_test}s iznosi: {Q_stap:.2f} J")
    kappa=(Q_stap*l)/(A*(T2[-1]-T1[-1])*t_test)
    print(f"Termička provodnost štapa iznosi: {kappa:.2f} W/(m·K)")
    
    
    Q_ok_400 = linear_model(t_test, *popt)
    sigma_C_okolina = (Q_ok_400 / (cv * mv + C)) * 9 
    
    
    sigma_stap = np.sqrt(sigma_ukupna**2 + sigma_C_okolina**2 + sigma_reg**2)
    
    sigma_kappa = (l / (A * (T2[-1] - T1[-1]) * t_test)) * sigma_stap
    
    print(f"Ukupna statistička pogreška u t={t_test}s iznosi: {sigma_stap:.2f} J")
    print(f"Ukupna statistička pogreška u termičkoj provodnosti štapa iznosi: {sigma_kappa:.2f} W/(m·K)")
    print(f"linearna regresija: Q = {a_fit:.2f}t + {b_fit:.2f} J")
toplina_ukupna()