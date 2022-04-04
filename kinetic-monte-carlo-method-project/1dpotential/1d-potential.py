import numpy as np
import matplotlib.pyplot as plt 
from scipy.linalg import eigh_tridiagonal


N = 2000  #  numero de vezes que o espaco foi dividido
# N = 10
dy = 1/N  # 1 = dy * N
y = np.linspace(0, 1, N+1)

#  Definindo o potencial

def mL2V(y):
    return 1000*(y-1/2)**2

#def mL2V(y):
#    return 1000*(y-1/2)**3

V = mL2V(y)
# plt.plot(y, V)
# plt.show()

# Defindo a diagonal principal da matriz

d = 1/dy**2 + mL2V(y)[1:-1]  # nao pegamos o primeiro nem o ultimo ponto que pertencem as condicoes de contorno
e =-1/(2*dy**2) * np.ones(len(d)-1)

w, v = eigh_tridiagonal(d, e)
#  print(v.T[0])
print(v)
for i in range(4):
    plt.plot(v.T[i] ** 2, label="n = " + str(i))
plt.legend()
plt.show()
