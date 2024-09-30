import numpy as np
import matplotlib.pyplot as  plt

#  Berechnung der Koeffizienten
import numpy as np

def Name_S1_Aufg2(a, xmin, xmax):
    # Überprüft ob das array a nicht leer ist oder nur einen Koeffizienten hat
    if a.size == 0 or a.ndim != 1:
        raise Exception('Fehler: Input array a is empty or has more than one dimension')

    # Bestimmt den Grad des Polynoms
    n = a.size - 1

    # Generiert ein Array mit den x-Werten
    x = np.linspace(xmin, xmax, 100)  

    # Inizialisiert Arrays für die Werte der Funktionen und der Ableitung
    p = np.zeros_like(x)
    dp = np.zeros_like(x)
    pint = np.zeros_like(x)

    # Berechnet die Funktion
    for i in range(n + 1):
        p += a[i] * x**i

    # Berechnet die Ableitung
    for i in range(1, n + 1):
        dp += i * a[i] * x**(i - 1)

    # Berechnet die Stammfunktion
    for i in range(n + 1):
        pint += a[i] / (i + 1) * x**(i + 1)

    return x, p, dp, pint

# Beispielkoefffzienten
a = np.array([2, 1, 3]) # p(x)=2x2^2 + 1x + 3
xmin = -5
xmax = 5

# Funktion aufrufen
x, p, dp, pint = Name_S1_Aufg2(a, xmin, xmax)

# Grafik erstellen 
plt.figure(figsize=(12, 8))

# Polynome plotten 
plt.subplot(3, 1, 1)
plt.plot(x, p, label='p(x)')
plt.title('Polynom p(x)')
plt.xlabel('x')
plt.ylabel('p(x)')
plt.grid()
plt.legend()

#  Ableitung plotten 
plt.subplot(3, 1, 2)
plt.plot(x, dp, label="p'(x)", color='orange')
plt.title('Ableitung p\'(x)')
plt.xlabel('x')
plt.ylabel('p\'(x)')
plt.grid()
plt.legend()

# Stammfunktion plotten
plt.subplot(3, 1, 3)
plt.plot(x, pint, label='P(x)', color='green')
plt.title('Stammfunktion P(x)')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
