from Aufgabe2 import Name_S9_Aufg2
import numpy as np
import matplotlib.pyplot as plt



dx_max_values = []
dx_obs_values = []
ratios = []

for i in range(1000):
    A = np.random.rand(100, 100)
    b = np.random.rand(100, 1)

    eb = b + np.random.rand(100, 1) / 10**5
    eA = A + np.random.rand(100, 100) / 10**5
    x, xe, dx_max, dx_obs = Name_S9_Aufg2(A, eA, b, eb)
    dx_max_values.append(dx_max)
    dx_obs_values.append(dx_obs)
    ratios.append(dx_max / dx_obs)
plt.figure(figsize=(10, 6))

plt.semilogy(dx_max_values, label='dx_max')
plt.semilogy(dx_obs_values, label='dx_obs')
plt.semilogy(ratios, label='dx_max/dx_obs')
plt.legend()
plt.xlabel('Iteration')
plt.ylabel('Values')
plt.title('dx_max, dx_obs, and their ratio over iterations')
plt.show()

# Kommentar:
# In dieser Versuchsanordnung scheint dx_max eine realistische obere Schranke für dx_obs zu sein,
# da das Verhältnis dx_max/dx_obs in den meisten Fällen nahe bei 1 liegt.
