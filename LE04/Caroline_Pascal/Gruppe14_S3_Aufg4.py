import numpy as np
import matplotlib.pyplot as plt

# Define the function h(x) and its derivative h'(x)
def h(x):
    return np.sqrt(100 * x**2 - 200 * x + 99)

def h_prime(x):
    return (100 * x - 100) / np.sqrt(100 * x**2 - 200 * x + 99)

# Calculate the condition number
def condition_number(x):
    return np.abs(x * h_prime(x) / h(x))

# Generate x values
x = np.arange(1.1, 1.3, 1e-7)

# Calculate condition numbers
kappa = condition_number(x)

# Plot the function h(x)
plt.figure(figsize=(10, 12))

plt.subplot(2, 1, 1)
plt.plot(x, h(x), label='h(x)', color='blue')
plt.title('Behavior of h(x) near x = 1.1')
plt.xlabel('x')
plt.ylabel('h(x)')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True, which="both", ls="--")
plt.legend()

# Plot the condition number
plt.subplot(2, 1, 2)
plt.semilogy(x, kappa, label='Condition number of h(x)')
plt.xlabel('x')
plt.ylabel('Condition number (log scale)')
plt.title('Semi-Logarithmic Plot of the Condition Number of h(x)')
plt.grid(True, which="both", ls="--")
plt.legend()

plt.tight_layout()
plt.show()

# Antwort C
# Die nummerische Auslöschung tritt auf, weil der Ausdruck unter der Quadratwurzel
# in der Nähe von x = 1.1 sehr klein wird, was zu einem Verlust an signifikanten Stellen
# während der Subtraktion führt. Diese Auslöschung kann durch algebraische Transformationen
# gemildert werden, wenn die Konditionszahl gut ist. In diesem Fall ist die Konditionszahl
# jedoch in der Nähe von x = 1.1 hoch, was darauf hinweist, dass die Funktion empfindlich
# auf kleine Änderungen von x reagiert. Daher kann die Auslöschung nicht allein durch
# algebraische Transformationen vollständig vermieden werden.