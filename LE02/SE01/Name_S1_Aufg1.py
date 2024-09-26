import numpy as np
import matplotlib.pyplot as plt

# Parameter
x = np.arange(-10, 10, 0.01)

# Funktion f(x)
def f(x):
    return x**5 - 5*x**4 - 30*x**3 + 110*x**2 + 29*x - 105

# Ableitungsfunktion f'(x)
def f_prime(x):
    return 5*x**4 - 20*x**3 - 90*x**2 + 220*x + 29

# Stammfunktion F(x)
def F(x):
    return (1/6)*x**6 - (5/5)*x**5 - (30/4)*x**4 + (110/3)*x**3 + (29/2)*x**2 - 105*x

# Daten für die Funktionen berechnen
f_x = f(x)
f_prime_x = f_prime(x)
F_x = F(x)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x, f_x, label='f(x)', color='blue')
plt.plot(x, f_prime_x, label="f'(x)", color='red')
plt.plot(x, F_x, label='F(x)', color='green')

# Achsenlimits setzen
plt.xlim(-10, 10)
plt.ylim(-1600, 1600)

# Achsen beschriften
plt.xlabel('x')
plt.ylabel('Funktionswerte')

# Titel und Legende hinzufügen
plt.title('Plot von f(x), f\'(x) und F(x)')
plt.legend()

# Gitternetz aktivieren
plt.grid(True)

# Plot anzeigen
plt.show()