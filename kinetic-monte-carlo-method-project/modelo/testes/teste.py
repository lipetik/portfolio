import numpy as np
from scipy import constants
from numpy import random as rand

gamma = []
gamma_zero = 10**(13)
Delta = np.array([1.55, 1.63, 2.61]) * 1.6022 * (10 ** -19)
temperatura = 400
N = [10**24, 10**24, 10**24]
R = 0
t = 0 

for i in range(len(Delta)):
    arg_exp = -Delta[i]/(constants.Boltzmann * temperatura)
    gamma.append(gamma_zero * np.exp(arg_exp))

for i in range(len(Delta)):
    R = R + gamma[i] * N[i]

chi = rand.uniform(0, 1) 
# time_step = -np.log(chi/R)

print("R =", R)
# print("chi = ", chi)
# print('time step = ', time_step)

# Fazer um for com o acrescimo t+delta(t)
for i in range(10):
    chi = rand.uniform(0, 1) 
    time_step = -np.log(chi/R)
    t = t + time_step
    print("--------------------------------")
    print("this is time step = ", i)
    print("time =", t)
    print("chi = ", chi)
    print('time step = ', time_step)
    print("--------------------------------")









