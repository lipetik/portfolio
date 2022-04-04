import numpy as np
import random as rand
from scipy import constants
import matplotlib.pyplot as plt
# from funcao import R_sum
from funcao import Gamma
from funcao import Probable_event
from funcao import Time_foward
from funcao import Temp_foward

""" Condições iniciais """
# Quantidades
gamma_zero = 10 ** 13
temperatura = 300 # muda 
t = 0 # muda
tempo_anterior = 0 # muda
Mass, Massa_0 = 2 * 10 ** 4, 2 * 10 ** 4 
#   ######################### Arrays ##################

# 50% de O_2
Delta = np.array([1.23, 1.55, 1.63, 2.61]) * 1.6022 * (10 ** -19)
# 25% de O_2
# Delta = np.array([1.23, 1.51, 1.78, 2.62]) * 1.6022 * (10 ** -19)

N = np.array([900, 0, 0, 900])
taxa_temp = np.array([700/60, 700/300, 700/600])
#   ################# Empty arrays ####################
time = np.array([])
rate = np.array([])
Temperatura = np.array([])
Mass_arr = np.array([])

#  ############# MAIN FUNCTION #####################

# gamma = Gamma(Delta, gamma_zero, temperatura)
# print(type(gamma))
# print(gamma * N)


for i in range(10 ** 5):
    gamma = Gamma(Delta, gamma_zero, temperatura)
    R_i = gamma * N
    R_n = R_i.sum()
    u = rand.uniform(0, 1)
    N, Mass = Probable_event(R_i, R_n, N, u, Mass)
    Mass_arr = np.append(Mass_arr, Mass)
    t = Time_foward(t, R_n, u)
    temperatura, tempo_anterior = Temp_foward(temperatura, t, tempo_anterior, taxa_temp[0])
    time = np.append(time, t)
    rate = np.append(rate, R_n)
    Temperatura = np.append(Temperatura, temperatura)

    print("-----------------------------------")
    print("Gamma = ", gamma)
#    print("N = ", N)
#    print('Total evento', N.sum())
#    print('time = ', t)
#    print("R_i = ", R_i)
#    print('R_n = ', R_n)
    print("Temperatura = ", temperatura)
    print("-----------------------------------")

Mass_arr = Mass_arr/Massa_0
# Mass_arr = np.log(Mass_arr)
# time = np.log(time)


#  ############ PLOT ############################
# xmin = 10 ** -7
# xmax = 10 ** 6
# figname = 'Temperatura-' + str(temperatura) + 'K'
# plt.xscale("log")
# plt.yscale("log")
plt.plot(Temperatura, Mass_arr, label='Tempo = ' + str(temperatura) + ' K', lw=2.1, color='orangered')
#plt.xlim(xmin, xmax)
plt.xlabel('Time', fontsize=19)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.ylabel('Mass %', fontsize=19)
plt.legend(fontsize=14)
# plt.savefig(f'{figname}', dpi=110, bbox_inches='tight')
plt.show()





