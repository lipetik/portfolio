import numpy as np
import matplotlib.pyplot as plt


# Definir o espaco da base:
a = -10 
b = 10 
N = 100
# x = np.linspace(a, b, N+1)
step_size = 0.05
x = np.arange(a, b, step_size)
# n = [0, 1, 2]
n = np.linspace(0, 10, 11)


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


def V(x):
    V = x ** 2
    return V


def periodicf(li, lf, f, x):
    if x >= li and x <= lf:
        return f(x)
    elif x > lf:
        x_new = x-(lf-li)
        return periodicf(li, lf, f, x_new)
    elif x < (li):
        x_new = x+(lf-li)
        return periodicf(li, lf, f, x_new)

def V(x):
    V = x ** 2
    return V

def square(x):
    if x > 0:
        return 5
    else:
        return 0

# The periodic version of square function
def squareP(li, lf, x):
    return periodicf(li, lf, square, x)

def x2(li, lf, x):
    return periodicf(li, lf, V, x)

# y = [squareP(-2, 2, xi) for xi in x]
y = [x2(-2, 2, xi) for xi in x]
# print(y)
plt.plot(x, y)
# plt.legend()
plt.show()
