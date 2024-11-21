import numpy as np
import matplotlib.pyplot as plt
from Gruppe14_S9_Aufg2 import Name_S9_Aufg2 as Aufg2

dxmax_vector = []
dxobs_vector = []
ratio_vector = []

for i in range(1000):
    A = np.random.rand(100, 100)
    b = np.random.rand(100, 1)
    A_tilde = A + np.random.rand(100, 100) / 1e5
    b_tilde = b + np.random.rand(100, 1) / 1e5

    x, x_tilde, dxmax, dxobs = Aufg2(A, A_tilde, b, b_tilde)
    dxmax_vector.append(dxmax)
    dxobs_vector.append(dxobs)
    ratio_vector.append(dxmax/dxobs)

plt.semilogy(dxmax_vector, label='dxmax')
plt.semilogy(dxobs_vector, label='dxobs')
plt.semilogy(ratio_vector, label='dxmax/dxobs')
plt.xlabel('Iteration')
plt.ylabel('Wert')
plt.legend()
plt.show()