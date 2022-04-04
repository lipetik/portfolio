# Python 3
###############################################################################
# Exercicio 1
def findSqrt(num, x_0=10, maxiter=100, epsilon=1e-6):
    # seu código aqui

    i = 0
    x = x_0
    erro = 1
    while erro > epsilon: 
        i = i + 1
        valor_anterior = x
        x = x - ((x**2) - num) / (2*x)
        erro = abs(x - valor_anterior)
        print('-----------------------------------')
        print('Esta é a iteração de numero ', i)
        print('erro = ', erro)
        print('x = ', x)
#        print('O erro convergiu antes de 100 iteraçoes!')
        if i == maxiter:
            print('Verifique se o erro convergiu numeo maximo de iteracoes alancado!')
            break

numero = float(input('digite o numero que se deseja calcular a raiz quadrada: '))
findSqrt(numero)


###############################################################################
# Exercicio 2
import math
import numpy as np

# Pode-se escolher aqui a funcao e o intervalo e o numero n de iteracoes
a = 0
b = math.pi
# f = lambda x: (math.sin(x))
f = lambda x: (3/2)*((math.sin(x))**3)
n = [10, 20, 120, 200, 500]

# Teste 
# a = 0
# b = 1
# f_x = lambda x: x




def Simpson(f, a, b, n=500):
    teste = 0
    h = (b - a)/(n)
    m = int(n/2)
    sum_1 = 0
    sum_2 = 0
    for i in range(1, m, 1):
        sum_1 = sum_1 + f(a + ((2*i)-1)*h)
    for i in range(1, m-1, 1):
        sum_2 = sum_2 + f(a + (a + 2 * i * h))
    integral = (h/3) * (f(a) + f(b) + (4*sum_1) + (2*sum_2))
    print(integral)

for i in range(len(n)):
    print('Esta é a integral para n = ', n[i])
    Simpson(f, a, b, int(n[i]))

# Exercicio 2 (Solução alternativa)
import numpy as np


def Simpson(f, a, b, n):
    h = (b-a)/n # distancia entre intervalo de x consecutivos
    soma1 = sum(f[1:n-1:2])  # soma no intervalo de 1 até n-1 
    soma2 = sum(f[:n-2:2])  # soma até n-2
    integral = (h/3) * (f[0] + f[n-1] + 4*soma1 + 2*soma2)
    print(integral)


n = [10, 20, 120, 200, 500]  # lista com os valores de n pedidos
a = 0  # intervalo
b = np.pi   # intervalo


for i in range(len(n)):
    x = np.linspace(a, b, int(n[i])) # gera valores no intervalo [a,b] com intervalos iguais
    # f = np.sin(x) # funcao que queremos calcular a integral
    f = ((np.sin(x))**3) * (3/2)
    print('Esta é a integral para n = ', n[i])
    Simpson(f, a, b, int(n[i]))


###############################################################################
# Exercicio 3

import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable


massa_e = 9.0194 * (10**-31)  # massa do eletron em kg
carga_e = 1.6022 * (10**-19)  # carga do eletron em Coulumb
permissividade = 8.8542 * (10**-12)  # permissividade eletrica do vacuo
planck = 6.6261 * (10**-34)  # constante de planck


alpha = (massa_e * (carga_e**4))/(8 * (permissividade**2) * (planck**2))
alpha = alpha * 6.242 * (10**18)


n = np.linspace(1, 20, 20)

Energia = []

for i in range(len(n)):
    E_n = -(alpha)*(1/(n[i]**2)) # * (1.6022e-19)
    Energia.append(E_n)


t = PrettyTable(['N', 'Energia (eV)'])
for i in range(len(n)):
    t.add_row([n[i], Energia[i]])
print(t)

# Eletron se movendo de nivel de energia
var_energia = [] 
lista_diferenca = []

tabela = PrettyTable(['Transição de níveis', 'Energia (eV)'])
for i in range(1, 6, 1):
    for j in range(1, 6, 1):
        if i!= j:
            if j>i:
                diferenca = f'{i}--{j}'
                lista_diferenca.append(diferenca)
                delta_e = - alpha * ((1/(i**2)) - (1/(j**2)))
                var_energia.append(delta_e)
                # print(f'diferenca {i} {j} {delta_e}')

for i in range(len(lista_diferenca)):
     tabela.add_row([lista_diferenca[i], var_energia[i]])
print(tabela)


