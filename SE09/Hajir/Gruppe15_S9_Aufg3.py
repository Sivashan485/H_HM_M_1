""" import sys
import os

# Add the directory containing the SE09 module to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) """

from Gruppe15_S9_Aufg2 import Gruppe15_S9_Aufg2 as method
import numpy as np
import matplotlib.pyplot as plt

dxMax_values = []
dxObs_values = []
ratio_values = []

for _ in range(1000):
    A = np.random.rand(100, 100)
    b = np.random.rand(100, 1)
    A_tilde = A + np.random.rand(100, 100) / 1e5
    b_tilde = b + np.random.rand(100, 1) / 1e5

    _, _, dxMax, dxObs = method(A, A_tilde, b, b_tilde)

    dxMax_values.append(dxMax)
    dxObs_values.append(dxObs)
    ratio_values.append(dxMax / dxObs)

plt.semilogy(dxMax_values, label='dxMax')
plt.semilogy(dxObs_values, label='dxObs')
plt.semilogy(ratio_values, label='dxMax / dxObs')
plt.legend()
plt.show()

# dxMax ist eine realistische obere Schranke für dxObs in dieser Versuchsanordnung, 
# da dxMax die theoretische obere Schranke für den relativen Fehler darstellt.
