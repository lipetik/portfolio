import numpy as np
import matplotlib.pyplot as plt 
from scipy import integrate
from scipy.linalg import eig
import numpy.linalg as la
from numpy import column_stack, savetxt
# Minhas funçoes
# Potenciais
from funcoes import kronig_penney_potential
# Bases
from funcoes import Plane_wave, bloch_periodic
# Funcoes do algortimo
from funcoes import second_derivative, Plane_wave, bloch_periodic, derivative_matrix
from funcoes import integrand_matrix, matrix_Tmn, integrand_matrix_potential, matrix_Vmn, matrix_Hmn


# Parâmetros do problema
a = 0  # início do intervalo
b = 1  # final do intervalo
interval_number = 2000  # numero de divisoes do espaço

# step (h) do intervalo de x

h = (b-a)/interval_number
V_0 = 50

# Arrays declarados
# x = np.linspace(a, b, interval_number,dtype=np.cdouble)
x = np.linspace(a, b, interval_number)  # array com o intervalo
n = np.linspace(-15, 15, 31)  # numero de bases
K = np.linspace(-np.pi/b, np.pi/b, 100)


V_x = kronig_penney_potential(x, b, 0 * b, V_0)
psi_base = Plane_wave(x, n, b)
psi_bloch = bloch_periodic(x, K)
print(len(V_x))

# psi = list(psi_bloch[0] * psi_base)
energy0 = []
energy1 = []
energy2 = []
energy3 = []
for k in range(len(K)):
    #  matriz da segunda derivada da base
    psi = psi_base * psi_bloch[k]
    psi_der_arr = [[] for _ in range(len(n))]  # cria um array de arrays vazios

    for i in range(len(n)):
        psi_der = second_derivative(psi[i], h)
        psi_der_arr[i] = list(psi_der)

    psi_der_arr = np.asarray(psi_der_arr)

    # Matrix dos integrandos 
    shape = (len(n), len(n), interval_number)
    integrand_matrix = np.zeros(shape, dtype=np.cdouble)
    integrand_potential_matrix = np.zeros(shape, dtype=np.cdouble)

    # matrix do integrando de T_mn
    for i in range(len(n)):
        for j in range(len(n)):
            integrand_list = []
            for k in range(interval_number):
                integrand = (-0.5) * np.conjugate(psi[j][k]) * psi_der_arr[i][k]
                integrand_list.append(integrand)
            integrand_matrix[i][j] = list(integrand_list)

    # matrix do integrando do V_mn
    for i in range(len(n)):
        for j in range(len(n)):
            integrand_list = []
            for k in range(interval_number):
                integrand = np.conjugate(psi[i][k]) * V_x[k] * psi[j][k]
                integrand_list.append(integrand)
            integrand_potential_matrix[i][j] = list(integrand_list)




    ############### Matrizes T_mn e V_mn ########################
    # Criando a matrix da energia cinética
    shape_Tmn = (len(n), len(n))
    T_mn = np.zeros(shape_Tmn, dtype=np.cdouble)

    # Criando a matrix do potencial
    shape_Vmn = (len(n), len(n))
    V_mn = np.zeros(shape_Vmn, dtype=np.cdouble)

    #####################  Integrais ############################

    # Integral T_mn
    for i in range(len(n)):
        for j in range(len(n)):
            integral = integrate.simpson(integrand_matrix[i][j], x)
            T_mn[i][j] = integral

    # Integral V_mn
    for i in range(len(n)):
        for j in range(len(n)):
            integral = integrate.simpson(integrand_potential_matrix[i][j], x)
            V_mn[i][j] = integral

    ################ Criando H_mn ################################
    shape_Hmn = (len(n), len(n))
    H_mn = np.zeros(shape_Hmn, dtype=np.cdouble)

    for i in range(len(n)):
        for j in range(len(n)):
            H_mn[i][j] = T_mn[i][j] + V_mn[i][j]


    ################ Resolvendo a equação de autovalor ############
    print("Condiconamento da matriz =", la.cond(H_mn))
    print(la.det(H_mn) != 0)
    eig_values, eig_vecs = eig(H_mn)
    eig_values = sorted(eig_values)
    energy0.append(np.real(eig_values[0]))
    energy1.append(np.real(eig_values[1]))
    energy2.append(np.real(eig_values[2]))
    energy3.append(np.real(eig_values[3]))

data = column_stack([K,energy0,energy1,energy2,energy3])
label = ['k', 'n=0', 'n=1', 'n=2', 'n=3']
label_row = ','.join(label)
my_header = label_row
savetxt('b0.csv', data, delimiter=',', header=my_header)

# plt.plot(K, energy0, label="n = 0")
# plt.plot(K, energy1, label="n = 1")
# plt.plot(K, energy2, label="n = 2")
# plt.plot(K, energy3, label="n = 3")
# plt.show()


