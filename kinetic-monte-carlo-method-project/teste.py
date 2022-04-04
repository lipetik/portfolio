import numpy as np
import matplotlib.pyplot as plt
from funcoes import basis_sin, V, second_derivative, Plane_wave, bloch_periodic
from scipy import integrate
import numpy.linalg as la
from scipy.linalg import eigh_tridiagonal, eig


# Parâmetros do problema
a = 0 # início do intervalo
b = 1 # final do intervalo
interval_number = 2000 # numero de divisoes do espaço

# step (h) do intervalo de x 

h = (b-a)/interval_number


# Arrays declarados
# x = np.linspace(a, b, interval_number, dtype=np.cdouble) # array com o intervalo
x = np.linspace(a, b, interval_number) # array com o intervalo
n = np.linspace(1, 10, 10) # numero de bases
K = np.linspace(-np.pi/b, np.pi/b, 100)


# psi= Plane_wave(x, n, b)
z = 0 + 1j
# print(z * 10)
k_n = (2 * np.pi * n[0])/b
exp_term = k_n * x * z
# np.exp(10)
psi_n = (1/np.sqrt(b)) * np.exp(exp_term)

# print(exp_term)
