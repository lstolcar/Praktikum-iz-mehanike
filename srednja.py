import numpy as np
import matplotlib as mt

def srednja():
    br_ele=int(input('Unesite broj elemenata cija se srednja vrijednost racuna: '))
    pogreska_zbog_uredaja=float(input('Unesite pogresku: '))
    lista_brojeva=[]
    lista_sd_brojnik=[]
    for i in range(0,br_ele):
        x=float(input('Unesite broj: '))
        lista_brojeva.append(x)

    srednja_vrijednost=sum(lista_brojeva)/br_ele
    print(srednja_vrijednost)
    for j in range(0,br_ele):
        y=(lista_brojeva[j]-srednja_vrijednost)**2
        lista_sd_brojnik.append(y)
    sd=np.sqrt(sum(lista_sd_brojnik)/(br_ele*(br_ele-1)))
    print(sd)
    error=np.sqrt((pogreska_zbog_uredaja**2)+sd**2)
    print(error)
    print(('Vaš rezultat je {}+-{}').format(srednja_vrijednost,error))




srednja()