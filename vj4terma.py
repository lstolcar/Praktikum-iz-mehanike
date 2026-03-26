import numpy as np
import matplotlib.pyplot as plt

def specificni_toplinski_kapacitet():
    # 1 bakar 2 celik 3 aluminij
    m=[0.138,0.127,0.071]
    mk=[0.070,0.072,0.072]
    mv=[[0.158,0.142,0.181],[0.157,0.149,0.199],[0.160,0.145,0.145]]
    T2=[[18,19,21],[19,21,22.5],[18,20,22]]
    T=[[23,25,26],[26,27,27.5],[24,26.5,29]]
    T1=100
    Vt=1
    ck=1.59*(10**3)
    cv=4184.4
    for i in range(3):
        spec_top_koef=[]
        relativna_greska=[]
        odsutpanje=[]
        for j in range(3):
            c=((mv[i][j]*cv+mk[i]*ck+Vt*1.9)*(T2[i][j]-T[i][j]))/((m[i])*(T[i][j]-T1))
            rel=((mv[i][j]*cv+mk[i]*ck+Vt*1.9)/(m[i]))*0.5*np.sqrt(((T2[i][j]-T1)**2)/((T[i][j]-T1)**4) +1/((T[i][j]-T1)**2))
            spec_top_koef.append(c)
            relativna_greska.append(rel**2)
        for k in range(3):
            odsutpanje.append((spec_top_koef[k]-(sum(spec_top_koef)/3))**2)
        print(spec_top_koef)
        print(sum(spec_top_koef)/3)
        print((1/3)*np.sqrt(sum(relativna_greska)))
        print(np.sqrt(sum(odsutpanje)/6))
        print(np.sqrt((1/3)*(np.sqrt(sum(relativna_greska)))**2+(sum(odsutpanje)/6)))
        print("------------------")

specificni_toplinski_kapacitet()