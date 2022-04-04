import numpy as np
# Gera as bases para um poço de potencial de tamanho a.
# x --> array de entrada
# n = 0,1,2,3 ...
# a --> tamanho do poço quadrado


def basis_sin(x, n, a):
    psi = []
    for i in range(len(n)):
        psi_n = np.sqrt(2/a) * np.sin((n[i] * np.pi * x)/a)
        psi.append(psi_n)
    return psi


def V(x,w,a):
    V = (1/2) * (w**2) * (x - a/2) ** 2
    # V = (x-1/2)**3
    return V



# Calcula a segunda derivada em relacao a n-esima base


def second_derivative(psi, h):
    der_psi = []
    first_term = (1/h**2) * (psi[0] - (2 * psi[1]) + psi[2])
    der_psi.append(first_term)
    for i in range(1, len(psi)-1):
        der_psi_i = (1/h**2) * (psi[i+1] - (2 * psi[i]) + psi[i-1])
        der_psi.append(der_psi_i)
    der_psi.append((1/h**2) * (psi[-3] - (2 * psi[-2]) + psi[-1]))
    return der_psi


