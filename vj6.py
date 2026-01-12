import numpy as np
import matplotlib.pyplot as plt 

lista_kut_A=[90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25]
lista_I_A=[75,49,35,27,21,15.5,12,10.5,8,7,5.5,4,3.5,3.2]
lista_omjer_A=[]
for x in lista_I_A:
    lista_omjer_A.append(x/73)
lista_kut_B=[90, 85, 80, 75, 70, 65, 64, 63, 62, 61, 60, 59, 58 , 57, 56, 55, 54, 53, 52, 51, 50, 45, 40, 35, 30]
lista_I_B=[72,40,15,7.5,3,1,0.8,0.6,0.5,0.4,0.3,0.25,0.2,0.2,0.2,0.25,0.3,0.4,0.45,0.5,0.6,0.9,1.2,1.6,1.8]
lista_omjer_B=[]    
for y in lista_I_B:
    lista_omjer_B.append(y/90)
n = 1.54
lista_okomiti=[]
lista_paralelni=[]
for i in lista_kut_A:
    lista_okomiti.append((- (np.sqrt(n**2 - np.sin(np.radians(i))**2) - np.cos(np.radians(i)))**2 / (n**2 - 1))**2)
for j in lista_kut_B:
    lista_paralelni.append(((n**2 * np.cos(np.radians(j)) - np.sqrt(n**2 - np.sin(np.radians(j))**2)) / \
        (n**2 * np.cos(np.radians(j)) + np.sqrt(n**2 - np.sin(np.radians(j))**2)))**2)
plt.figure()
plt.scatter(lista_kut_A, lista_omjer_A, marker='o', color='blue', label='Podaci A',s=100)
plt.plot(lista_kut_A, lista_okomiti, color='orange', label='funkcija (8) za dobiveni n=1.54')
plt.xlabel('Kut (°)', fontsize=25)
plt.ylabel(' ζ^2', fontsize=25)
plt.title('Ovisnost omjera intenziteta upadnog i reflektiranog EM vala o kutu za situaciju 1.A', fontsize=25)
plt.legend(fontsize=15)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.grid(True)
plt.show()
plt.figure()
plt.scatter(lista_kut_B, lista_omjer_B, marker='o', color='red',    label='Podaci B',s=100)
plt.plot(lista_kut_B, lista_paralelni, color='orange', label='funkcija (9) za dobiveni n=1.54') 
plt.xlabel('Kut (°)', fontsize=25)          
plt.ylabel(' ζ^2', fontsize=25)
plt.title('Ovisnost omjera intenziteta upadnog i reflektiranog EM vala o kutu za situaciju 1.B', fontsize=25)
plt.legend(fontsize=15)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.grid(True)
plt.show()        