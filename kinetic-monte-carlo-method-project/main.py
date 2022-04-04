import numpy as np
import matplotlib.pyplot as plt
from funcoes import basis_sin, V, second_derivative
from scipy import integrate
from scipy.linalg import eig
import numpy.linalg as la

''' Funcoes necessárias:
1) Set de bases, potencial
2) segunda derivada
3) Matrizes
4) Funçao que escreve as matrizes
5) Resolver a equação de autovalor
'''


############################ Parametros ######################
# definindo o espaço, x =[a,b] , e a divisão nos intervalos (interval_number)
w = 50  # frequencia do oscilador harmonico
a = 0  # inicio do intervalo
b = 1   # final do intervalo
interval_number = 10000  # numero de divisoes do espaço
h = (b-a)/interval_number

# Array
x = np.linspace(a, b, interval_number) # espaço
n = np.linspace(1, 30, 30) # basis



#########  Chamando as funcoes ###################

psi = basis_sin(x, n, b)
V_x = V(x, w, b)
der_V = second_derivative(V_x, h)


########## Criando as Matrizes para integrar #########################

#  matriz da segunda derivada da base
psi_der_arr = [[] for _ in range(len(n))] # cria um array de arrays vazios

for i in range(len(n)):
    psi_der = second_derivative(psi[i], h)
    psi_der_arr[i] = list(psi_der)

psi_der_arr = np.asarray(psi_der_arr)

# Matrix dos integrandos 
shape = (len(n), len(n), interval_number)
integrand_matrix = np.zeros(shape)
integrand_potential_matrix = np.zeros(shape)

# matrix do integrando de T_mn
for i in range(len(n)):
    for j in range(len(n)):
        integrand_list = []
        for k in range(interval_number):
            integrand = (-0.5) * psi[j][k] * psi_der_arr[i][k]
            integrand_list.append(integrand)
        integrand_matrix[i][j] = list(integrand_list)

# matrix do integrando do V_mn
for i in range(len(n)):
    for j in range(len(n)):
        integrand_list = []
        for k in range(interval_number):
            integrand = psi[i][k] * V_x[k] * psi[j][k]
            integrand_list.append(integrand)
        integrand_potential_matrix[i][j] = list(integrand_list)




############### Matrizes T_mn e V_mn ########################
# Criando a matrix da energia cinética
shape_Tmn = (len(n), len(n))
T_mn = np.zeros(shape_Tmn)

# Criando a matrix do potencial
shape_Vmn = (len(n), len(n))
V_mn = np.zeros(shape_Vmn)

#####################  Integrais #####################

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

################ Criando H_mn ######################
shape_Hmn = (len(n), len(n))
H_mn = np.zeros(shape_Hmn)

for i in range(len(n)):
    for j in range(len(n)):
        H_mn[i][j] = T_mn[i][j] + V_mn[i][j]


################ Resolvendo a equação de autovalor ##############
print("Condiconamento da matriz =", la.cond(H_mn))
print(la.det(H_mn) != 0)
eig_values, eig_vecs = eig(H_mn)


############# Construindo a funcao de onda fina ###########
psi_final = []
psi_final = [[] for _ in range(len(n))]
for i in range(len(eig_vecs[0])):
    psi_list = []
    psi_final_element = eig_vecs[0][i] * psi[i]
    psi_list.append(psi_final_element)
    psi_final[i] = list(psi_list)

psi_teste = []
for i in range(9):
    psi_teste_element = psi_final[i][0]
    psi_teste.append(psi_teste_element)

eig_values = sorted(eig_values)

for i in range(10):
    print("Energia = " + str(eig_values[i])+" | " + str(((i) + 0.5)*w))

############## Plot ##############################
# plt.plot(psi_teste[0] ** 2, label="n ="+str(0))
# plt.plot(psi_teste[1] ** 2, label="n ="+str(1))
# plt.plot(psi_teste[2] ** 2, label="n ="+str(2))
# plt.plot(psi_teste[3] ** 2, label="n ="+str(3))
# # plt.bar(np.arange(0, 10, 1), eig_values[0:10])
# plt.legend()
# plt.show()





