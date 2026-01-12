import numpy as np
import matplotlib.pyplot as plt


a1 = [1/66, 1/60, 1/57, 1/54, 1/51, 1/73, 1/83, 1/77, 1/70, 1/62]
b1 = [1/(300-66), 1/(350-60), 1/(400-57), 1/(450-54), 1/(500-51),
      1/(250-73), 1/(200-83), 1/(220-77), 1/(270-70), 1/(330-62)]

a2 = [1/167, 1/157, 1/139, 1/132, 1/125, 1/163, 1/148, 1/136, 1/134, 1/123]
b2 = [1/(400-167), 1/(450-157), 1/(500-139), 1/(550-132), 1/(600-125),
      1/(420-163), 1/(470-148), 1/(520-136), 1/(570-134), 1/(820-123)]

a3 = [1/194, 1/189, 1/186, 1/184, 1/203, 1/209, 1/215, 1/240, 1/256, 1/247]
b3 = [1/(1000-194), 1/(1050-189), 1/(1100-186), 1/(1150-184), 1/(950-203),
      1/(900-209), 1/(850-215), 1/(700-240), 1/(600-256), 1/(650-247)]

a4 = [-1/59, -1/61, -1/78, -1/90, -1/85, -1/80, -1/101, -1/96, -1/91, -1/86]
b4 = [1/86, 1/100, 1/113, 1/155, 1/133, 1/119, 1/172, 1/160, 1/145, 1/131]

a5 = [-1/90, -1/85, -1/80, -1/101, -1/96, -1/91, -1/86]
b5 = [1/155, 1/133, 1/119, 1/172, 1/160, 1/145, 1/131]




def pogreska_f(a_mm, b_mm, sigma=0.5):
    a = np.array(a_mm)
    b = np.array(b_mm)
    f = (a * b) / (a + b)
    sigma_f = (f**2) * sigma * np.sqrt(1/a**2 + 1/b**2)
    return f, sigma_f

def sigma_B(a_mm, b_mm):
    a = np.array(a_mm)
    b = np.array(b_mm)
    return 0.5*np.sqrt(1/a**2 + 1/b**2)



a1_mm = [66, 60, 57, 54, 51, 73, 83, 77, 70, 62]
b1_mm = [300-66, 350-60, 400-57, 450-54, 500-51, 250-73, 200-83, 220-77, 270-70, 330-62]

a2_mm = [167,157,139,132,125,163,148,136,134,123]
b2_mm = [400-167,450-157,500-139,550-132,600-125,420-163,470-148,520-136,570-134,820-123]

a3_mm = [194,189,186,184,203,209,215,240,256,247]
b3_mm = [1000-194,1050-189,1100-186,1150-184,950-203,900-209,850-215,700-240,600-256,650-247]

a4_mm = [59,61,78,90,85,80,101,96,91,86]
b4_mm = [86,100,113,155,133,119,172,160,145,131]

a5_mm = [90,85,80,101,96,91,86]
b5_mm = [155,133,119,172,160,145,131]



def nacrtaj_graf(a, b, boja, naslov, oznaka, broj_grafa):
    plt.figure(figsize=(10, 6))
    # Korištenje polyfit s cov=True za dobivanje kovarijancijske matrice
    koeficijenti, kovarijanca = np.polyfit(a, b, 1, cov=True)
    A, B = koeficijenti
    
    # Standardna pogreška nagiba iz kovarijancijske matrice
    SE_b = np.sqrt(kovarijanca[0, 0])

    plt.scatter(a, b, marker='o', color=boja, label=f'Podaci za {oznaka}', s=100)

    x_fit = np.linspace(min(a), max(a), 100)
    y_fit = A * x_fit + B
    plt.plot(x_fit, y_fit, color='orange', linewidth=2, label='Linearna regresija')

    plt.xlabel('1/a (1/mm)', fontsize=25)
    plt.ylabel('1/b (1/mm)', fontsize=25)
    plt.title(naslov, fontsize=30)
    plt.legend(fontsize=25)
    plt.xticks(fontsize=25)
    plt.yticks(fontsize=25)
    plt.grid(True, alpha=0.3)

    jednadzba = f"1/b = {A:.3f}±{SE_b:.3f}·(1/a) + {B:.3f}"
    plt.text(0.05, 0.95, jednadzba, transform=plt.gca().transAxes,
             fontsize=14, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    plt.tight_layout()
    plt.savefig(f'graf_{broj_grafa}.png', dpi=300, bbox_inches='tight')
    plt.show()

    return A, B, SE_b


A1, B1, SE_b1 = nacrtaj_graf(a1, b1, 'blue', 'Jednadžba leće: konvergentna leća +50', 'konvergentnu leću +50', 1)
A2, B2, SE_b2 = nacrtaj_graf(a2, b2, 'red', 'Jednadžba leće: konvergentna leća +100', 'konvergentnu leću +100', 2)
A3, B3, SE_b3 = nacrtaj_graf(a3, b3, 'green', 'Jednadžba leće: konvergentna leća +150', 'konvergentnu leću +150', 3)
A4, B4, SE_b4 = nacrtaj_graf(a4, b4, 'purple', 'Jednadžba leće: divergentna leća -200', 'divergentnu leću -200', 4)
A5, B5, SE_b5 = nacrtaj_graf(a5, b5, 'orange', 'Jednadžba leće: divergentna leća -200', 'divergentnu leću -200', 5)


print("=" * 60)
print("REZULTATI EKSPERIMENTA")
print("=" * 60)

f1 = 1/B1
f2 = 1/B2
f3 = 1/B3
f4 = 1/B4
f5 = 1/B5


f1_i, sf1_i = pogreska_f(a1_mm, b1_mm)
f2_i, sf2_i = pogreska_f(a2_mm, b2_mm)
f3_i, sf3_i = pogreska_f(a3_mm, b3_mm)
f4_i, sf4_i = pogreska_f(a4_mm, b4_mm)
f5_i, sf5_i = pogreska_f(a5_mm, b5_mm)

sf1 = np.sqrt(np.sum(sf1_i**2)) / len(sf1_i)
sf2 = np.sqrt(np.sum(sf2_i**2)) / len(sf2_i)
sf3 = np.sqrt(np.sum(sf3_i**2)) / len(sf3_i)
sf4 = np.sqrt(np.sum(sf4_i**2)) / len(sf4_i)
sf5 = np.sqrt(np.sum(sf5_i**2)) / len(sf5_i)

sB1 = np.mean(sigma_B(a1_mm, b1_mm))
sB2 = np.mean(sigma_B(a2_mm, b2_mm))
sB3 = np.mean(sigma_B(a3_mm, b3_mm))
sB4 = np.mean(sigma_B(a4_mm, b4_mm))
sB5 = np.mean(sigma_B(a5_mm, b5_mm))


print(f"\n1. Konvergentna leća +50:")
print(f"   - Nagib: A = {A1:.3f} ± {SE_b1:.3f}")
print(f"   - Odsječak na y-osi: B = {B1:.6f} ± {sB1:.6f} mm⁻¹")
print(f"   - Žarišna duljina: f = {f1:.2f} ± {sf1:.2f} mm")

print(f"\n2. Konvergentna leća +100:")
print(f"   - Nagib: A = {A2:.3f} ± {SE_b2:.3f}")
print(f"   - Odsječak na y-osi: B = {B2:.6f} ± {sB2:.6f} mm⁻¹")
print(f"   - Žarišna duljina: f = {f2:.2f} ± {sf2:.2f} mm")

print(f"\n3. Konvergentna leća +150:")
print(f"   - Nagib: A = {A3:.3f} ± {SE_b3:.3f}")
print(f"   - Odsječak na y-osi: B = {B3:.6f} ± {sB3:.6f} mm⁻¹")
print(f"   - Žarišna duljina: f = {f3:.2f} ± {sf3:.2f} mm")

print(f"\n4. Divergentna leća -200:")
print(f"   - Nagib: A = {A4:.3f} ± {SE_b4:.3f}")
print(f"   - Odsječak na y-osi: B = {B4:.6f} ± {sB4:.6f} mm⁻¹")
print(f"   - Žarišna duljina: f = {f4:.2f} ± {sf4:.2f} mm")

print(f"\n5. Divergentna leća -200 (drugi skup):")
print(f"   - Nagib: A = {A5:.3f} ± {SE_b5:.3f}")
print(f"   - Odsječak na y-osi: B = {B5:.6f} ± {sB5:.6f} mm⁻¹")
print(f"   - Žarišna duljina: f = {f5:.2f} ± {sf5:.2f} mm")

print("\n" + "=" * 60)
print("ANALIZA ODSTUPANJA")
print("=" * 60)

teorijske = [50, 100, 150, -200, -200]
eksperimentalne = [f1, f2, f3, f4, f5]
oznake = ['+50', '+100', '+150', '-200','-200 (drugi skup)']

for i in range(5):
    pogreska = abs((eksperimentalne[i] - teorijske[i]) / teorijske[i] * 100)
    print(f"\nLeća {oznake[i]}:")
    print(f"  Teorijska f = {teorijske[i]:.2f} mm")
    print(f"  Eksperimentalna f = {eksperimentalne[i]:.2f} mm")
    print(f"  Odstupanje = {pogreska:.2f} %")
    if i == 0:
        print(f"  Jednadžba: 1/b = {A1:.3f}±{SE_b1:.3f}·(1/a) + {B1:.3f} ± {sB1:.3f}")
    elif i == 1:
        print(f"  Jednadžba: 1/b = {A2:.3f}±{SE_b2:.3f}·(1/a) + {B2:.3f} ± {sB2:.3f}")
    elif i == 2:
        print(f"  Jednadžba: 1/b = {A3:.3f}±{SE_b3:.3f}·(1/a) + {B3:.3f} ± {sB3:.3f}")
    elif i == 3:
        print(f"  Jednadžba: 1/b = {A4:.3f}±{SE_b4:.3f}·(1/a) + {B4:.3f} ± {sB4:.3f}")
    else:
        print(f"  Jednadžba: 1/b = {A5:.3f}±{SE_b5:.3f}·(1/a) + {B5:.3f} ± {sB5:.3f}")