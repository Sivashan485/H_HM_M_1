import matplotlib
import numpy as np

import matplotlib.pyplot as plt

def f1(x):
    return x**7 - 14*x**6 + 84*x**5 - 280*x**4 + 560*x**3 - 672*x**2 + 448*x - 128

def f2(x):
    return (x-2)**7

def g(x):
    return x/(np.sin(1 + x) - np.sin(1))

def gc(x):
    return x / (2 * np.cos((2 + x) / 2) * np.sin(x / 2))

x = np.linspace(1.99, 2.01, 501)
x2 = np.arange(-10**-14, 10**(-14), 10**-17)



#Aufgabe 2a
#Die Funktion reagiert sehr empfindlich auf Rundungsfehler durch Gleitkommazahlen, 
#obwohl die beiden Funktionen identisch sind. (Fehlerfortpflanzung)
#Die starken Rundungsfehler könnten durch die Vorzeichenwechsel in f1(x) verursacht werden.
# Plot 1: f1(x) und f2(x)
plt.figure()
plt.title("Aufgabe 2a")
plt.plot(x, f1(x), label='f1(x)')
plt.plot(x, f2(x), label='f2(x)')
plt.legend()
plt.grid()
plt.show()


# Plot 2: g(x), gc(x) und g_new(x)
plt.figure()
plt.title("Aufgabe 2b")
plt.plot(x2, g(x2), label='g(x)')
plt.plot(x2, gc(x2), label='gc(x)')
plt.legend()
plt.grid()
plt.show()
#Bei der Funktion g(x) tritt eine Instabilität auf, es kommt zu einem Aussetzer.
#Durch Anwendung des Additionstheorems wird die Berechnung für kleine Werte von x stabiler.


# TODO lim-> 0 ??

 
plt.show()