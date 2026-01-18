import numpy as np
import matplotlib.pyplot as plt 
def dif_konst1():
    boje=[404.656 , 435.405 , 491.604 , 546.074 , 576.960 , 578.966]
    kut1=[ 7+(5.5/60) , 7+(38.5/60) , 8+(36/60) , 9+(30.5/60) , 10+(5/60) , 10+(7/60)]
    kut2=[ 14+(13.5/60) , 15+(18.5/60) , 17+(21.5/60) , 19+(18.5/60) , 20+(29/60) , 20+(31.5/60)]
    kut=[]
    boje_z=[]
    delta_kut = np.deg2rad(4/60)
    Theta_po_lambdi=[]
    dTheta=[]
    lista_pogresaka_polyfit=[]
    for i in range (len(kut1)):
        kut.append(np.sin(np.deg2rad(kut1[i])))
        boje_z.append(boje[i]*(10**(-6)))
        Theta_po_lambdi.append(300/np.cos(np.deg2rad(kut1[i])))
        dTheta.append((300*np.sin(np.deg2rad(kut1[i])))/((np.cos(np.deg2rad(kut1[i])))**2)*delta_kut)
        lista_pogresaka_polyfit.append((np.cos(np.deg2rad(kut1[i])) * delta_kut))
    for j in range (len(kut2)):
        kut.append(np.sin(np.deg2rad(kut2[j])))
        boje_z.append((2*boje[j])*(10**(-6)))
        Theta_po_lambdi.append(600/np.cos(np.deg2rad(kut2[j])))
        dTheta.append((600*np.sin(np.deg2rad(kut2[j])))/((np.cos(np.deg2rad(kut2[j])))**2)*delta_kut)
        lista_pogresaka_polyfit.append((np.cos(np.deg2rad(kut2[j])) * delta_kut))
    print(Theta_po_lambdi)
    print(dTheta)
    p, cov = np.polyfit(boje_z, kut, 1, w=1/np.array(lista_pogresaka_polyfit), cov=True )

    plt.figure()
    plt.scatter( boje_z, kut, marker='o', color='blue', label='Podaci',s=100)
    x = np.linspace(min(boje_z), max(boje_z), 200)
    plt.plot(x, np.polyval(p, x), color='orange', label='Prilagođena linija')
    plt.ylabel('sin(θ)', fontsize=25)
    plt.xlabel('z·λ (mm)', fontsize=25)
    plt.title('Difrakcijska konstanta rešetke', fontsize=25)
    plt.legend(fontsize=15)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid(True)  
    plt.show()
    print(f'Difrakcijska konstanta rešetke je {p[0]} linija, a pogreska je { np.sqrt(np.diag(cov))}')

def dif_konst2():
    boje=[ 435.405 , 546.074 , 576.960 ]
    kut1=[ 1+(17/60) , 1+(36/60) , 1+(41/60) ]
    kut2=[ 2+(30.5/60) , 3+(9.5/60) , 3+(21/60) ]
    kut=[]
    boje_z=[]
    delta_kut = np.deg2rad(4/60)
    Theta_po_lambdi=[]
    dTheta=[]   
    lista_pogresaka_polyfit=[]
    for i in range (len(kut1)):
        kut.append(np.sin(np.deg2rad(kut1[i])))
        boje_z.append(boje[i]*(10**(-6)))
        Theta_po_lambdi.append(50/np.cos(np.deg2rad(kut1[i])))
        dTheta.append((50*np.sin(np.deg2rad(kut1[i])))/((np.cos(np.deg2rad(kut1[i])))**2)*delta_kut)
        lista_pogresaka_polyfit.append(np.cos(np.deg2rad(kut1[i])) * delta_kut)
    for j in range (len(kut2)):
        kut.append(np.sin(np.deg2rad(kut2[j])))
        boje_z.append((2*boje[j])*(10**(-6)))
        Theta_po_lambdi.append(100/np.cos(np.deg2rad(kut2[j])))
        dTheta.append((100*np.sin(np.deg2rad(kut2[j])))/((np.cos(np.deg2rad(kut2[j])))**2)*delta_kut)
        lista_pogresaka_polyfit.append(np.cos(np.deg2rad(kut2[j])) * delta_kut)
    print(Theta_po_lambdi)
    print(dTheta)
    p, cov = np.polyfit(boje_z, kut, 1, w=1/np.array(lista_pogresaka_polyfit), cov=True )
    plt.figure()
    plt.scatter( boje_z, kut, marker='o', color='blue', label='Podaci',s=100)
    x = np.linspace(min(boje_z), max(boje_z), 200)
    plt.plot(x, np.polyval(p, x), color='orange', label='Prilagođena linija')
    plt.ylabel('sin(θ)', fontsize=25)
    plt.xlabel('z·λ (mm)', fontsize=25)
    plt.title('Difrakcijska konstanta rešetke', fontsize=25)
    plt.legend(fontsize=15)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid(True)  
    plt.show()
    print(f'Difrakcijska konstanta rešetke je {p[0]} linija, a pogreska je { np.sqrt(np.diag(cov))}')
def dif_konst3():
    boje=[ 435.405 , 546.074 , 576.960 ]
    kut1=[ (17.5/60) , (20.5/60) , (23.5/60) ]
    kut2=[ (32.5/60) , (40.5/60) , (44/60) ]
    kut3=[0, (58.5/60) , (63.5/60) ]
    kut=[]
    boje_z=[]
    delta_kut = np.deg2rad(4/60)
    Theta_po_lambdi=[]
    dTheta=[]
    lista_pogresaka_polyfit=[]
    for i in range (len(kut1)):
        kut.append(np.sin(np.deg2rad(kut1[i])))
        boje_z.append(boje[i]*(10**(-6)))
        Theta_po_lambdi.append(10/np.cos(np.deg2rad(kut1[i])))
        dTheta.append((10*np.sin(np.deg2rad(kut1[i])))/((np.cos(np.deg2rad(kut1[i])))**2)*delta_kut)
        lista_pogresaka_polyfit.append(np.cos(np.deg2rad(kut1[i])) * delta_kut)
    for j in range (len(kut2)):
        kut.append(np.sin(np.deg2rad(kut2[j])))
        boje_z.append((2*boje[j])*(10**(-6)))
        Theta_po_lambdi.append(20/np.cos(np.deg2rad(kut2[j])))
        dTheta.append((20*np.sin(np.deg2rad(kut2[j])))/((np.cos(np.deg2rad(kut2[j])))**2)*delta_kut)
        lista_pogresaka_polyfit.append(np.cos(np.deg2rad(kut2[j])) * delta_kut)
    for k in range (len(kut3)):
        kut.append(np.sin(np.deg2rad(kut3[k])))
        if kut3[k]==0:
            boje_z.append(0)
            Theta_po_lambdi.append(30/np.cos(np.deg2rad(kut3[k])))
            dTheta.append((30*np.sin(np.deg2rad(kut3[k])))/((np.cos(np.deg2rad(kut3[k])))**2)*delta_kut)
            lista_pogresaka_polyfit.append(np.cos(np.deg2rad(kut3[k])) * delta_kut)
        else:   
            boje_z.append((3*boje[k])*(10**(-6)))
            Theta_po_lambdi.append(30/np.cos(np.deg2rad(kut3[k])))
            dTheta.append((30*np.sin(np.deg2rad(kut3[k])))/((np.cos(np.deg2rad(kut3[k])))**2)*delta_kut)
            lista_pogresaka_polyfit.append(np.cos(np.deg2rad(kut3[k])) * delta_kut)
    print(Theta_po_lambdi)
    print(dTheta)   
    p, cov = np.polyfit(boje_z, kut, 1, w=1/np.array(lista_pogresaka_polyfit), cov=True )
    plt.figure()
    plt.scatter( boje_z, kut, marker='o', color='blue', label='Podaci',s=100)
    x = np.linspace(min(boje_z), max(boje_z), 200)
    plt.plot(x, np.polyval(p, x), color='orange', label='Prilagođena linija')
    plt.ylabel('sin(θ)', fontsize=25)
    plt.xlabel('z·λ (mm)', fontsize=25)
    plt.title('Difrakcijska konstanta rešetke', fontsize=25)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.legend(fontsize=15)
    plt.grid(True)  
    plt.show()
    print(f'Difrakcijska konstanta rešetke je {p[0]} linija, a pogreska je { np.sqrt(np.diag(cov))}')

dif_konst1()
dif_konst2()
dif_konst3()
