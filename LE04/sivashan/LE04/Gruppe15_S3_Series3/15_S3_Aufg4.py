import numpy as np
import matplotlib.pyplot as plt

def h(x):
    return np.sqrt(100 * x**2 - 200 * x + 99)

def h_prime(x, dx=1e-7):
    return (h(x + dx) - h(x)) / dx

def condition_number(x):
    return np.abs(x * h_prime(x) / h(x))


x_values = np.linspace(1.05, 1.15, 100)
h_values = h(x_values)

# Erstellen des Plots
plt.figure(figsize=(10, 6))
plt.plot(x_values, h_values, label='h(x)', color='blue')
plt.title('Verhalten von h(x) in der Nähe von 1.1')
plt.xlabel('x')
plt.ylabel('h(x)')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Horizontale Linie bei y=0
plt.grid(True)
plt.legend()
plt.show()



x_values = np.arange(1.1, 1.3, 1e-7)

condition_values = condition_number(x_values)

plt.figure(figsize=(10, 6))
plt.semilogy(x_values, condition_values, label='Condition of h(x)')
plt.xlabel('x')
plt.ylabel('Condition Number (log scale)')
plt.title('Semilogarithmic Plot of the Condition of h(x)')
plt.legend()
plt.grid(True)
plt.show()

#A
#Eine Konditionierung ist hier wegen der Division durch Null nicht möglich. 
#f(x) = 100*(1.1)²-200*1.1+99 = 0

#C
#Die Auslöschung in der Funktion h(x) = sqrt(100x^2 - 200x + 99) kann nicht vermieden werden, wenn die Kondition schlecht ist.
#Bei x-Werten nahe bei 1 werden die Terme fast gleich, was zu einer kleinen Differenz führt. Diese Subtraktion erzeugt starke Auslöschung.
#Wenn der Konditionswert an einer Stelle schlecht ist, kann keine Verbesserung durch Umformungen erreicht werden.