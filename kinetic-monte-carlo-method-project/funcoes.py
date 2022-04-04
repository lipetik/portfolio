import numpy as np
from scipy import integrate
# Gera as bases para um poço de potencial de tamanho a.
# x --> array de entrada
# n = 0,1,2,3 ...
# a --> tamanho do poço quadrado

#########################  BASES #######################
def basis_sin(x, n, a):
    psi = []
    for i in range(len(n)):
        psi_n = np.sqrt(2/a) * np.sin((n[i] * np.pi * x)/a)
        psi.append(psi_n)
    return psi


# Gera a base periodica de ondas planas
def Plane_wave(x, n, a):
    z = 0 + 1j
    psi = []
    for i in range(len(n)):
        k_n = (2 * np.pi * n[i])/a
        exp_term = k_n * x * z
        psi_n = (1/np.sqrt(a)) * np.exp(exp_term)
        psi.append(psi_n)
    return psi

# Gera funçao de onda K
def bloch_periodic(x, K):
    z = 0 + 1j
    psi = []
    for i in range(len(K)):
        exp_term = K[i] * x * z
        psi_n = np.exp(exp_term)
        psi.append(psi_n)
    return psi

########### POTENCIAIS ##################################


def harmonic_oscilator_potential(x, w, a):
    V = (1/2) * (w**2) * (x - a/2) ** 2
    # V = (x-1/2)**3
    return V

# Potencial do modelo de kronig penney 0 < x < a, b é o tamanho da barreira
def kronig_penney_potential(x, a, b, V_0):
    V = []
    for i in range(len(x)):
        if 0 < x[i] < (a-b)/2:
            V.append(0)
        elif (a-b)/2 <= x[i] <= (a+b)/2:
            V.append(V_0)
        else:
            V.append(0)
    return V


######### FUNCOES PARA CONSTRUIR O ALGORITMO ################

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


''' FUNCOES PARA A PARTE CINETICA '''

# Cria a matriz da segunda derivada
def derivative_matrix(psi, n, h):
    psi_der_arr = [[] for _ in range(len(n))] # cria um array de arrays vazios
    for i in range(len(n)):
        psi_der = second_derivative(psi[i], h)
        psi_der_arr[i] = list(psi_der)
    psi_der_arr = np.asarray(psi_der_arr)
    return psi_der_arr


# Cria a matrix do integrando (energia cinética)
def integrand_matrix(psi, psi_der_arr, n, interval_number):
    shape = (len(n), len(n), interval_number)
    integrand_matrix = np.zeros(shape)
    # matrix do integrando de T_mn
    for i in range(len(n)):
        for j in range(len(n)):
            integrand_list = []
            for k in range(interval_number):
                integrand = (-0.5) * psi[j][k] * psi_der_arr[i][k]
                integrand_list.append(integrand)
            integrand_matrix[i][j] = list(integrand_list)
    return integrand_matrix


#Cria a matrix T_mn
def matrix_Tmn(integrand_matrix, x, n):
    shape_Tmn = (len(n), len(n))
    T_mn = np.zeros(shape_Tmn)
    # Integral T_mn
    for i in range(len(n)):
        for j in range(len(n)):
            integral = integrate.simpson(integrand_matrix[i][j], x)
            T_mn[i][j] = integral
    return T_mn




''' FUNCOES PARA A PARTE DO POTENCIAL '''

# Calcula a matrix do integrando do V_mn


def integrand_matrix_potential(psi, V_x, n, interval_number):
    shape = (len(n), len(n), interval_number)
    integrand_potential_matrix = np.zeros(shape)
    # matrix do integrando do V_mn
    for i in range(len(n)):
        for j in range(len(n)):
            integrand_list = []
            for k in range(interval_number):
                integrand = psi[i][k] * V_x[k] * psi[j][k]
                integrand_list.append(integrand)
            integrand_potential_matrix[i][j] = list(integrand_list)
    return integrand_potential_matrix




def matrix_Vmn(integrand_potential_matrix, x, n):
    # Criando a matrix do potencial
    shape_Vmn = (len(n), len(n))
    V_mn = np.zeros(shape_Vmn)
    # Integral V_mn
    for i in range(len(n)):
        for j in range(len(n)):
            integral = integrate.simpson(integrand_potential_matrix[i][j], x)
            V_mn[i][j] = integral
    return V_mn


################ Criando H_mn ######################
def matrix_Hmn(T_mn, V_mn, n):
    shape_Hmn = (len(n), len(n))
    H_mn = np.zeros(shape_Hmn)
    for i in range(len(n)):
        for j in range(len(n)):
            H_mn[i][j] = T_mn[i][j] + V_mn[i][j]
    return H_mn








