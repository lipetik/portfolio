import numpy as np
import random as rand
from scipy import constants

""" Variaveis """
prob_arr = np.array([])
R = 0
gamma = np.array([])
t = 0
gamma_zero = 10**13
Delta = np.array([1.50, 1.63, 2.62, 2.72]) * 1.6022 * (10 ** -19)
temperatura = 600.0
N = np.array([1, 1, 1, 1]) * 6.02 * (10 ** 23)  # numero de mols



#######################################
""" Calculo do gamma """


for i in range(len(N)):
    arg_exp = -Delta[i]/(constants.Boltzmann * temperatura)
    x = gamma_zero * np.exp(arg_exp)
    gamma = np.append(gamma, x)


####################################
""" Calculo da soma das probabilidades """

for i in range(len(N)):
    termo_soma = gamma[i] * N[i]
    R = R + gamma[i] * N[i]

""" o array com cada termo da soma das probabilidades """
prob_arr = gamma * N


""" Encontrar a transição ocorrida """
print("R antes = ", R)
u = rand.uniform(0, 1)
print("Probalidade antes = ", u)
u_product = R * u

for i in range(len(N)-1):
    if prob_arr[i-1] < u_product < prob_arr[i]:
        prob_arr[i] = R
        # R = prob_arr[i]


""" time step foward """
u = rand.uniform(0, 1)
print("Probalidade depois = ", u)
time_step = (R ** (-1)) * np.log(1/u)
t = t + time_step
print('time = ', t)


print('R depois = ', R)
print('u*R = ', u_product)
print('Gamma array = ', gamma)
print('Prob_arr = ', prob_arr)



