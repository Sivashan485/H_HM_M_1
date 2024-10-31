import numpy as np
import matplotlib.pyplot as plt

# Part a: Numerical cancellation
def h(x):
    return np.sqrt(100 * x**2 - 200 * x + 99)

# Evaluate h(x) near 1.1
x_values = np.linspace(1.1, 1.3, 1000)
h_values = h(x_values)

# Plot h(x)
plt.figure()
plt.plot(x_values, h_values, label='h(x)')
plt.xlabel('x')
plt.ylabel('h(x)')
plt.title('Plot of h(x)')
plt.legend()
plt.show()

# Part b: Condition number plot
def condition_number(x):
    h_x = h(x)
    h_prime_x = (100 * x - 100) / h_x  # Derivative of h(x)
    return np.abs(h_prime_x * x / h_x)

# Compute condition number for x in [1.1, 1.3] with resolution 10^-7
x_values_fine = np.arange(1.1, 1.3, 1e-7)
condition_numbers = condition_number(x_values_fine)

# Semi-logarithmic plot of the condition number
plt.figure()
plt.semilogy(x_values_fine, condition_numbers, label='Condition number of h(x)')
plt.xlabel('x')
plt.ylabel('Condition number')
plt.title('Semi-logarithmic plot of the condition number of h(x)')
plt.legend()
plt.show()

# Part c: Comment on avoiding cancellation
"""
# Comment:
Auslöschung tritt auf, weil der Ausdruck unter der Wurzel für x nahe 1.1 sehr klein wird. Dies führt zu einer
Verlust an signifikanten Stellen bei der numerischen Berechnung. Die Kondition der Funktion h(x) ist in diesem
Bereich schlecht, was bedeutet, dass kleine Änderungen in x zu großen relativen Änderungen in h(x) führen.
Daher kann die Auslöschung in diesem Fall nicht durch algebraische Umformungen vermieden werden.
"""