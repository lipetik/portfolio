import numpy as np
import scipy as scp
import matplotlib.pyplot as plt
from scipy import constants

# gamma zero é a frequencia de ocorrencia de cada evento
gamma_zero = 10**(13)  # segundo^-1 

Delta = np.array([1.55, 1.63, 2.61]) * 1.6022 * (10**-19)
temperatura = np.linspace(311, 700, 1000)  # escrever o linspace para a a temperatura
Gamma = [[], [], []]
mol = constants.Avogadro
N = np.array([1, 1, 1]) * mol
R = []

for i in range(0, len(Delta), 1):
    for j in range(len(temperatura)):
        arg_exp = - Delta[i]/(constants.Boltzmann * temperatura[j])
        gamma = gamma_zero * np.exp(arg_exp)
        Gamma[i].append(gamma)
        # R.append(Gamma[i:] * N[i])
     #   R = R + (Gamma[i:] * N[i])

# print(Gamma)
# for i in range(len(Gamma[:])):
#     for j in range(len(Gamma[:2])):
#         print(Gamma[j])


# Plotando Gamma
plot_gamma = np.array(Gamma)
fig, ax = plt.subplots()
plt.ylabel("Gamma")
plt.xlabel("Temperatura")
ax.plot(temperatura, plot_gamma[0, :])
ax.plot(temperatura, plot_gamma[1, :])
ax.plot(temperatura, plot_gamma[2, :])
plt.show()


