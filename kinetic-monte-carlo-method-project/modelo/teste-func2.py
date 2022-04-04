import numpy as np
import random as rand
from scipy import constants
import matplotlib.pyplot as plt
# from funcao import R_sum
from funcao import Gamma
from funcao import Probable_event
from funcao import Time_foward

# Quantidades
R = 0
gamma_zero = 10 ** 13
mol = constants.Avogadro
Temperatura = [400, 500, 600, 700, 800]
t = 0

# Arrays
# Delta = np.array([1.83, 1.55, 1.63, 2.61]) * 1.6022 * (10 ** -19)
Delta = np.array([1.23, 1.55, 1.63, 2.61]) * 1.6022 * (10 ** -19)

N = np.array([10000, 0, 0, 10000])  # * (10 ** 5)
# N = 10**5

# Empty arrays
time = [[], [], [], [], []]
rate = [[], [], [], [], []]

############## MAIN FUNCTION #####################

# gamma = Gamma(Delta, gamma_zero, temperatura)
# print(type(gamma))
# print(gamma * N)

for j in range(len(Temperatura)):
    temperatura = Temperatura[j]
    gamma = Gamma(Delta, gamma_zero, temperatura)
    for i in range(10 ** 4):
        R_i = gamma * N
        R_n = R_i.sum()
        u = rand.uniform(0, 1)
        N = Probable_event(R_i, R_n, N, u)
        t = Time_foward(t, R_n, u)
        time[j].append(t)
        rate[j].append(R_n)
#    print("-----------------------------------")
#    print("Gamma = ", gamma)
#    print("N = ", N)
#    print("R_i = ", R_i)
#    print('R_n = ', R_n)
#    print("-----------------------------------")

for i in range(len(Temperatura)):
    plt.plot(time[i], rate[i], label='Temperatura =' + str(Temperatura[i]) + ' K')
    plt.xlabel('Time')
    plt.ylabel('Rate')
    plt.legend()
plt.show()





