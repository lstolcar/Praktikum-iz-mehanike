import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# --------------------------------------------------
# PODACI
# --------------------------------------------------

s = np.array([50,55,60,65,70,75,80,85,90,95,100])
U_thermo = np.array([2.14,1.80,1.53,1.28,1.10,0.95,0.82,0.73,0.68,0.60,0.54])

I_sc = np.array([76.1,65.7,60.8,53.8,47.9,42.4,37.8,33.0,30.0,25.9,23.7])
U_oc = np.array([1.95,1.90,1.86,1.84,1.81,1.77,1.74,1.69,1.66,1.62,1.58])

data = {
    "60 cm": (np.array([1.79,1.76,1.73,1.70,1.67,1.61,1.51,1.39,1.16,0.85]),
              np.array([17.4,19.1,22.3,26.0,29.7,34.1,39.1,44.7,50.8,57.5])),

    "70 cm": (np.array([1.64,1.61,1.59,1.56,1.49,1.37,1.25,1.01,0.72,0.31]),
              np.array([15.9,17.9,19.5,23.0,25.8,29.8,35.0,40.6,45.7,46.3])),

    "80 cm": (np.array([1.54,1.52,1.50,1.46,1.39,1.34,1.19,1.02,0.79,0.43]),
              np.array([15.0,16.0,17.2,18.4,21.0,23.5,27.8,31.7,34.5,36.5]))
}

# temperatura
U_35 = np.array([1.64,1.61,1.59,1.56,1.49,1.37,1.25,1.01,0.72,0.31])
I_35 = np.array([15.9,17.9,19.5,23.0,25.8,29.8,35.0,40.6,45.7,46.3])

U_60 = np.array([1.39,1.38,1.34,1.33,1.28,1.26,1.21,0.98,0.69,0.43])
I_60 = np.array([14.2,15.2,16.5,17.7,20.9,25.7,29.4,35.2,40.2,43.5])

# --------------------------------------------------
# INTENZITET
# --------------------------------------------------

S = 0.16
A = np.pi*(1.25e-2)**2
J = (U_thermo*10)/(S*A)

# --------------------------------------------------
# LOG-LOG FIT
# --------------------------------------------------

log_s = np.log(s)
log_J = np.log(J)

p, cov = np.polyfit(log_s, log_J, 1, cov=True)
m, log_b = p
dm, dlogb = np.sqrt(np.diag(cov))
b = np.exp(log_b)

print("\n--- LOG-LOG FIT ---")
print(f"log(J) = ({m:.3f} ± {dm:.3f}) log(s) + ({log_b:.3f} ± {dlogb:.3f})")

plt.figure()
plt.scatter(log_s, log_J, color='black')
plt.plot(log_s, m*log_s + log_b)
plt.xlabel("log(s)", fontsize=25)
plt.ylabel("log(J)", fontsize=25)
plt.title("log(J) vs log(s)", fontsize=25)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.grid()
plt.show()

# --------------------------------------------------
# LINEARNI FITOVI
# --------------------------------------------------

def linear(x,a,b):
    return a*x+b

# Uoc
popt, pcov = curve_fit(linear, J, U_oc)
aU,bU = popt
daU, dbU = np.sqrt(np.diag(pcov))

print("\nU(J) = ({:.4f} ± {:.4f})J + ({:.4f} ± {:.4f})".format(aU,daU,bU,dbU))

plt.figure()
plt.scatter(J,U_oc,color='black')
plt.plot(J,linear(J,*popt))
plt.xlabel("J[W/m²]", fontsize=25)
plt.ylabel("U[V]", fontsize=25)
plt.title("U vs J", fontsize=25)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.grid()
plt.show()

# Isc
popt, pcov = curve_fit(linear, J, I_sc)
aI,bI = popt
daI, dbI = np.sqrt(np.diag(pcov))

print("I(J) = ({:.4f} ± {:.4f})J + ({:.4f} ± {:.4f})".format(aI,daI,bI,dbI))

plt.figure()
plt.scatter(J,I_sc,color='black')
plt.plot(J,linear(J,*popt))
plt.xlabel("J[W/m²]", fontsize=25)
plt.ylabel("I[mA]", fontsize=25)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.title("Isc vs J", fontsize=25)
plt.grid()
plt.show()

# --------------------------------------------------
# MODEL
# --------------------------------------------------

def model(U,Iks,a,b):
    return Iks - a*(np.exp(b*U)-1)

# --------------------------------------------------
# I-U FITOVI (KAO PDF)
# --------------------------------------------------

for label,(U,I) in data.items():

    popt, pcov = curve_fit(model,U,I,p0=[max(I),0.01,1],maxfev=10000)
    Iks,a,bp = popt
    dIks,da,db = np.sqrt(np.diag(pcov))

    print(f"\n--- {label} ---")
    print(f"I(U) = Iks - ({a:.4f} ± {da:.4f}) (e^({bp:.3f} ± {db:.3f})U - 1)")

    U_fit = np.linspace(min(U),max(U),300)

    plt.figure()
    plt.scatter(U,I,color='black')
    plt.plot(U_fit,model(U_fit,*popt))
    plt.xlabel("U [V]", fontsize=25)
    plt.ylabel("I [mA]", fontsize=25)
    plt.xticks(fontsize=25)
    plt.yticks(fontsize=25)
    plt.title(f"I-U ({label})", fontsize=25)
    plt.grid()
    plt.show()

# --------------------------------------------------
# TEMPERATURA
# --------------------------------------------------

for U,I,label in [(U_35,I_35,"35°C"),(U_60,I_60,"60°C")]:

    popt, pcov = curve_fit(model,U,I,p0=[max(I),0.01,1],maxfev=10000)
    Iks,a,bp = popt
    dIks,da,db = np.sqrt(np.diag(pcov))

    print(f"\n--- TEMPERATURA {label} ---")
    print(f"I(U) = Iks - ({a:.4f} ± {da:.4f}) (e^({bp:.3f} ± {db:.3f})U - 1)")

# zajednički graf
plt.figure()

for U,I,label in [(U_35,I_35,"35°C"),(U_60,I_60,"60°C")]:
    popt,_ = curve_fit(model,U,I,p0=[max(I),0.01,1],maxfev=10000)
    U_fit = np.linspace(min(U),max(U),300)
    plt.scatter(U,I)
    plt.plot(U_fit,model(U_fit,*popt),label=label)

plt.xlabel("U [V]", fontsize=25)
plt.ylabel("I [mA]", fontsize=25)
plt.title("Temperaturna ovisnost", fontsize=25)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.legend(fontsize=25)
plt.grid()
plt.show()
# --------------------------------------------------
# MAKSIMALNA SNAGA, Umax I EFIKASNOST
# --------------------------------------------------

def dP(U, Iks, a, b):
    return Iks + a - a*np.exp(b*U)*(1 + b*U)

def bisekcija(f, a, b, args=(), tol=1e-6):
    while abs(b - a) > tol:
        c = (a + b) / 2
        if f(a,*args)*f(c,*args) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

print("\n--- MAKSIMALNA SNAGA I ISKORISTIVOST ---")

A_bat = (4*2.5*5)*1e-4
indeksi_udaljenosti = {"60 cm": 2, "70 cm": 4, "80 cm": 6}
for i, (label, (U, I)) in enumerate(data.items()):

    # fit ponovno (da imamo parametre)
    popt, _ = curve_fit(model, U, I, p0=[max(I),0.01,1], maxfev=10000)
    Iks, a, b_param = popt

    # maksimum snage (bisekcija)
    Umax = bisekcija(dP, min(U), max(U), args=(Iks, a, b_param))

    # struja u maksimumu
    Imax = model(Umax, Iks, a, b_param)

    # maksimalna snaga
    Pmax = Umax * Imax

    # ulazna snaga
    pravi_indeks = indeksi_udaljenosti[label]
    J_val = J[pravi_indeks]
    Pin = J_val * A_bat

    # iskoristivost
    eta = Pmax / Pin

    print(f"\n--- {label} ---")
    print(f"U_max = {Umax:.3f} V")
    print(f"I_max = {Imax:.3f} mA")
    print(f"P_max = {Pmax:.3f} mW")
    print(f"Pin = {Pin:.3f} mW")
    print(f"η = {eta:.4f}")

    