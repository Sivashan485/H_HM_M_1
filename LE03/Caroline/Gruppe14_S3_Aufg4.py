import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1.1, 1.3, 100)

def h(x):
    return np.sqrt(100*x**2 - 200*x + 99)

def h_ab(x):
    return (100*x - 100) / h(x)

def h_Kond(x):
    return np.abs(h_ab(x) * x / h(x))

plt.plot(x, h(x))
plt.show()
# 4a) Da das Resultat in der Wurzel sehr klein wird, gibt es eine Auslöschung (Subtrahieren von fast gleichen Zahlen) 

plt.plot(x, h_Kond(x))
plt.show()
# Je näher bei 0, desto grösser die Chance auf Auslöschung

# 4c) Nein, weil die Konditionszahl zu gross ist. Die Konditionszahl sollte kleiner als 1 sein, damit das Problem gut konditioniert ist.