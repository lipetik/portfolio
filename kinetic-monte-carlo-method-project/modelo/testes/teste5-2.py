import numpy as np
import random as rand
from scipy import constants
import matplotlib.pyplot as plt


""" Variaveis """
prob_arr = np.array([])
R = 0
t = 0
time = np.array([])
rate = np.array([])
gamma_zero = 10**13
mol = constants.Avogadro
Delta = np.array([1.50, 1.63, 2.62, 2.72]) * 1.6022 * (10 ** -19)
temperatura = 400.0
N = np.array([1, 1, 1, 1]) * mol  # numero de mols

gamma = np.array([])
for i in range(len(N)):
    arg_exp = -Delta[i]/(constants.Boltzmann * temperatura)
    x = gamma_zero * np.exp(arg_exp)
    gamma = np.append(gamma, x)


for i in range(10 ** 6):
  #  gamma = np.array([])
  #  for i in range(len(N)):
  #      arg_exp = -Delta[i]/(constants.Boltzmann * temperatura)
  #      x = gamma_zero * np.exp(arg_exp)
  #      gamma = np.append(gamma, x)

    u = rand.uniform(0, 1)
    termo_soma = gamma * N
    R = termo_soma.sum()
    u_product = R * u
    for i in range(len(N) - 1):
        if termo_soma[i-1] < u_product < termo_soma[i]:
            # termo_soma[i] = R
            gamma[i] = R
    u = rand.uniform(0, 1)
    time_step = (1/R) * np.log(1/u)
    t = t + time_step
    time = np.append(time, t)
    rate = np.append(rate, R)

plt.plot(time, rate)
plt.xlabel('Time')
plt.ylabel('Rate')
plt.show()


















