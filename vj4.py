import numpy as np
import matplotlib as mt
import matplotlib.pyplot as plt

def lom():
    kutevi_kremena = np.array([[38.567],[38.650],[38.917],[39.250],[39.433],[39.533]])
    kutevi_vodena = np.array([[23.450],[23.667],[23.900],[24.050],[24.167]])
    kutevi_resetka = np.array([[24.450],[22.983],[20.833],[16.800],[16.050],[14.967]])

    g = (1/600)*10**6
    delta_kut = np.deg2rad(6/60)

    lista_n_kremena = []
    lista_n_pogreska_kremena = []
    lista_n_vodena = []
    lista_n_pogreska_vodena = []
    lista_lambda_resetka = []
    lista_lambda_pogreska_resetka = []

    for i in range(len(kutevi_kremena)):
        kut = float(kutevi_kremena[i])
        n_kremena = np.sin((np.deg2rad(60) + np.deg2rad(kut)) / 2) / np.sin(np.deg2rad(60) / 2)
        n_pogreska_kremena = 0.5 * (np.cos((np.deg2rad(60) + np.deg2rad(kut)) / 2) / np.sin(np.deg2rad(60) / 2)) * delta_kut

        lista_n_kremena.append(n_kremena)
        lista_n_pogreska_kremena.append(n_pogreska_kremena)

    for j in range(len(kutevi_vodena)):
        kut = float(kutevi_vodena[j])
        n_vodena = np.sin((np.deg2rad(60) + np.deg2rad(kut)) / 2) / np.sin(np.deg2rad(60) / 2)
        n_pogreska_vodena = 0.5 * (np.cos((np.deg2rad(60) + np.deg2rad(kut)) / 2) / np.sin(np.deg2rad(60) / 2)) * delta_kut

        lista_n_vodena.append(n_vodena)
        lista_n_pogreska_vodena.append(n_pogreska_vodena)

    for k in range(len(kutevi_resetka)):
        kut = float(kutevi_resetka[k])
        lambda_resetka = g * np.sin(np.deg2rad(kut))
        lambda_pogreska_resetka = g * np.cos(np.deg2rad(kut)) * delta_kut

        lista_lambda_resetka.append(lambda_resetka)
        lista_lambda_pogreska_resetka.append(lambda_pogreska_resetka)

    print(lista_n_kremena)
    print(lista_n_vodena)
    print(lista_lambda_resetka)
    print(lista_n_pogreska_kremena)
    print(lista_n_pogreska_vodena)
    print(lista_lambda_pogreska_resetka)

    plt.figure()
    plt.scatter(lista_lambda_resetka, lista_n_kremena, marker='o', color='red', label='Kremen',s=150)
    plt.errorbar(lista_lambda_resetka, lista_n_kremena, yerr=lista_n_pogreska_kremena, fmt='o', color='red', ecolor='red', elinewidth=3, capsize=5)
    plt.xlabel('Valna duljina λ (μm)', fontsize=14)
    plt.ylabel('Indeks loma n', fontsize=14)
    plt.title('Indeks loma kremene rešetke ovisno o valnoj duljini', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.show()

    plt.figure()
    plt.scatter(lista_lambda_resetka[:5], lista_n_vodena, marker='o', color='blue', label='Voda', s=150)
    plt.errorbar(lista_lambda_resetka[:5], lista_n_vodena, yerr=lista_n_pogreska_vodena, fmt='o', color='blue', ecolor='blue', elinewidth=3, capsize=5)
    plt.xlabel('Valna duljina λ (μm)', fontsize=14)
    plt.ylabel('Indeks loma n', fontsize=14)
    plt.title('Indeks loma vodene rešetke ovisno o valnoj duljini', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.show()

    plt.figure()
    plt.scatter(kutevi_resetka.astype(float), lista_lambda_resetka, marker='o', color='green', label='Resetka')
    plt.errorbar(kutevi_resetka.astype(float), lista_lambda_resetka, yerr=lista_lambda_pogreska_resetka, fmt='o', color='green', ecolor='green', elinewidth=3, capsize=0)
    plt.xlabel('Kut (°)', fontsize=14)
    plt.ylabel('Valna duljina λ (μm)', fontsize=14)
    plt.title('Valna duljina ovisno o kutu', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.show()

lom()
