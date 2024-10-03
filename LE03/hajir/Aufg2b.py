import numpy as np
import matplotlib.pyplot as plt

def g(x):
    return x / (np.sin(1 + x) - np.sin(1))

x_values = np.arange(-1e-14, 1e-14, 1e-17)

g_values = g(x_values)

plt.plot(x_values, g_values, label='g(x) = x * (sin(1 + x) - sin(1))')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.title('Plot of g(x) over the interval [-10^-14, 10^-14]')
plt.legend()
plt.grid(True)
plt.show()


# nein, die numerische berechnung des grenzwertes ist nicht stabil, da die Maschine 
# die Werte von x sehr klein annähert und somit die Genauigkeit der Maschine nicht 
# ausreicht, um den Grenzwert zu berechnen.