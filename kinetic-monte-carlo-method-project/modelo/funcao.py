import numpy as np
import random as rand
from numba import jit, float64
from scipy import constants
# import matplotlib.pyplot as plt

# Funcoes a serem feitas
# 1) Calcular Gamma
# 2) Calcular R_n(soma de R_i) e R_i
# 3) Seleção do evento mais provavel
# 4) Time step
# 5) Temp step

# 1) Calcular Gamma
@jit(nopython=True)
def Gamma(Delta, gamma_zero, temperatura):
    arg_exp = -Delta/(constants.Boltzmann * temperatura) 
    gamma = gamma_zero * np.exp(arg_exp)
    return gamma

# Tem problema aqui

# 2) Calcular R_n(soma de R_i) e R_i
def R_sum(gamma, N):
    R_i = gamma * N
    R_n = R_i.sum()
    return R_n, R_i

# O problema esta aqui !!!!!!!


# 3) busca binária (escolhe o evento)
@jit(nopython=True)
def Probable_event(R_i, R_n, N, u, Mass):
    u_product = R_n * u
    for i in range(len(R_i)):
        if R_i[i-1] < u_product < R_i[i]:
            # print("O evento escolhido foi ", i)
            if i == 0:
               # print("O evento escolhido foi ", i)
                N[0] = N[0] - 1
                N[1] = N[1] + 4
                N[2] = N[2] + 4
                Mass = Mass - 1
            if i == 1:
               #  print("O evento escolhido foi ", i)
                N[1] = N[1] - 1
                # N[1] = N[1] + 4
                # N[2] = N[2] + 4
                Mass = Mass - 1
            if i == 2:
               # print("O evento escolhido foi ", i)
                N[2] = N[2] - 1
                # N[1] = N[1] + 4
                # N[2] = N[2] + 4
                Mass = Mass - 1
            if i == 3:
               # print("O evento escolhido foi ", i)
                N[3] = N[3] - 2
                N[1] = N[1] + 8
                N[2] = N[2] + 8
                Mass = Mass - 4
        else:
           # print("Nenhum evento foi escolhido ")
           #  N = N
           #  Mass = Mass
           pass

    return N, Mass


# 4) Time step
def Time_foward(t, R_n, u):
    u = rand.uniform(0, 1)
    # time_step = (1/R_n) * np.log(1/u)
    time_step = -(1/R_n) * np.log(u)
    t = t + time_step
    return t


# 5) Temp step
def Temp_foward(T, t, tempo_anterior, taxa_temp):
    time_diff = t - tempo_anterior
    if np.log(time_diff) >= 1:
        temp_step = np.log(taxa_temp) * np.log(time_diff)
        T = T + temp_step
        tempo_anterior = t
    if 0 < np.log(time_diff) < 1:
        temp_step = np.log(taxa_temp) * np.log(time_diff)
        T = T + temp_step
        tempo_anterior = t
    else:
        tempo_anterior = t
        T = T
    return T, tempo_anterior


