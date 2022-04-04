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

############################

for i in range(10 ** 4):
    gamma = np.array([])
    for i in range(len(N)):
        arg_exp = -Delta[i]/(constants.Boltzmann * temperatura)
        x = gamma_zero * np.exp(arg_exp)
        gamma = np.append(gamma, x)

    for i in range(len(N)):
        termo_soma = gamma[i] * N[i]
        R = R + gamma[i] * N[i]
    prob_arr = gamma * N
    u = rand.uniform(0, R)
    u_product = R * u

    for i in range(len(N)-1):
        if prob_arr[i-1] < u_product and u_product < prob_arr[i]:
            gamma[i] = R

    u = rand.uniform(0, 1)
    time_step = (1/R) * np.log(1/u)
    t = t + time_step
    time = np.append(time, t)
    rate = np.append(rate, R)

    print('-----------------------------')
    print('time step = ', time_step)
    print('time = ', t)
    print('R depois = ', R)
    print('u*R = ', u_product)
    print('Gamma array = ', gamma)
    print('Prob_arr = ', prob_arr)
    print('-----------------------------')


plt.plot(time, rate)
plt.xlabel('Time')
plt.ylabel('Rate')
plt.show()


