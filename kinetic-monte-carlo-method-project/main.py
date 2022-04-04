import numpy as np
import random as rand
import matplotlib.pyplot as plt
from funcoes import Gamma
from funcoes import Probable_event
from funcoes import Time_foward
from funcoes import Temp_foward
from funcoes import R_sum

# taxa_temp = np.array([700/60, 700/300, 700/600])
taxa_temp = np.array([np.log(700)/60, np.log(700)/300, np.log(700)/600])
gamma_zero = 10 ** 13

#   ######################### Arrays ##################

# 50% de O_2
Delta = np.array([1.23, 1.55, 1.63, 2.61]) * 1.6022 * (10 ** -19)

# 25% de O_2
# Delta = np.array([1.23, 1.51, 1.78, 2.62]) * 1.6022 * (10 ** -19)


Temperatura = [[], [], []]
Mass_arr = [[], [], []]
Tempo = ['1 min', '5 min', '10 min']

########## Main ##########################
for k in range(len(taxa_temp)):
    temperatura = 300
    t = np.longdouble(0)
    tempo_anterior = 0
    Mass, Massa_0 = 4 * 10 ** 4, 4 * 10 ** 4
    N = np.array([800, 0, 0, 800])
    for i in range(10 ** 5):
        gamma = Gamma(Delta, gamma_zero, temperatura)
        R_n, R_i = R_sum(gamma, N)
        u = rand.uniform(0, 1)
        N, Mass = Probable_event(R_i, R_n, N, u, Mass)
        Mass_arr[k].append(Mass)
        t = Time_foward(t, R_n, u)
        temperatura, tempo_anterior = Temp_foward(temperatura, t, tempo_anterior, taxa_temp[k])
        Temperatura[k].append(temperatura)

Mass_arr = np.asarray(Mass_arr)
Mass_arr = (Mass_arr/Massa_0) * 100
Temperatura = np.asarray(Temperatura)
temp_ticks = Temperatura

############## PLOT ###################
figname = 'Temperatura-massa'
for i in range(len(Temperatura)):
    plt.plot(Temperatura[i] - 273, Mass_arr[i], label='Tempo =' + str(Tempo[i]), lw=2.1)

plt.xscale("log")
plt.xlabel(r'Temperatura ($^{\circ}C$)', fontsize=19)
plt.ylabel(r'$\Delta$Massa ($\%$)', fontsize=19)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=14)
plt.savefig(f'{figname}', dpi=110, bbox_inches='tight')
plt.show()




