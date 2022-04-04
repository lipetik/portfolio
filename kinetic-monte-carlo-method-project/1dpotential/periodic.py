import matplotlib.pyplot as plt 
import numpy as np

x_max = 2
a = 100 # Periodicidade
barr = 0.2 # Tamanho da barreira
N = 100
x = np.linspace(0, a, N)

def heaviside(x):
    out = np.zeros_like(x)
    out[x >= 0] = 1.0
    return out

values = heaviside(x)

# def potential(x, a):
#     V_1 = 0
#     V_2 = 2
#     V = []
#     for i in range(len(x)):
#         V_x = 0
#         if x[i] < a/2 - barr:
#             V_x = V_1
#             V.append(V_x)
#         elif a/2 - barr <= x[i] <= a/2 + barr:
#             V_x = V_2
#             V.append(V_x)
#         else:
#             V_x = V_1
#             V.append(V_x)
# 
#     return(V)
# 
# 
# V = potential(x, a)
# new_V = V
# print(V)
# 
# new_x = x
# for i in range(len(x)):
#     new_x = np.append(new_x, x[i] + a)
#     new_V.append(V[i])


#plt.plot(new_x, new_V)
# plt.plot(x, V)
plt.plot(x, values)
plt.show()

