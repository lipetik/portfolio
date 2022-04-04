import numpy as np
import random as rand
import matplotlib.pyplot as plt
from funcao import Gamma
from funcao import Probable_event
from funcao import Time_foward
from funcao import Temp_foward
from funcao import R_sum

taxa_temp = np.array([700/60, 700/300, 700/600])
# taxa_temp = np.array([700/600, 700/1200, 700/1800])
gamma_zero = 10 ** 13

#   ######################### Arrays ##################

# 50% de O_2
Delta = np.array([1.23, 1.55, 1.63, 2.61]) * 1.6022 * (10 ** -19)

# 25% de O_2
# Delta = np.array([1.23, 1.51, 1.78, 2.62]) * 1.6022 * (10 ** -19)


Temperatura = [[], [], []]
Mass_arr = [[], [], []]
Tempo = ['1 min', '5 min', '10 min']
# Tempo = ['10 min', '20 min', '30 min']

for k in range(len(taxa_temp)):
    temperatura = 300
    t = 0
    tempo_anterior = 0
    Mass, Massa_0 = 8 * 10 ** 6, 8 * 10 ** 6 
    N = np.array([800, 0, 0, 800])
    for i in range(5 * 10 ** 5):
        gamma = Gamma(Delta, gamma_zero, temperatura)
        R_n, R_i = R_sum(gamma, N)
        # R_i = gamma * N
        # R_n = R_i.sum()
        u = rand.uniform(0, 1)
        N, Mass = Probable_event(R_i, R_n, N, u, Mass)
        Mass_arr[k].append(Mass)
        t = Time_foward(t, R_n, u)
        temperatura, tempo_anterior = Temp_foward(temperatura, t, tempo_anterior, taxa_temp[k])
        Temperatura[k].append(temperatura)

Mass_arr = np.asarray(Mass_arr)
Mass_arr = (Mass_arr/Massa_0) * 100

######## PLOT ###################
figname = 'Temperatura-massa'
for i in range(len(Temperatura)):
    plt.plot(Temperatura[i], Mass_arr[i], label='Tempo =' + str(Tempo[i]), lw=2.1)

plt.xlabel('Temperatura (k)', fontsize=19)
plt.ylabel('Massa (%)', fontsize=19)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=14)
plt.savefig(f'{figname}', dpi=110, bbox_inches='tight')
plt.show()




