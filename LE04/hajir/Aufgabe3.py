import numpy as np
import matplotlib.pyplot as plt

# Define the function g(x)
def g(x):
    return 105 * (2 * np.e) ** (-x / 100)

# Create an array of x values from 0 to 100
x = np.linspace(0, 100, 500)

# Compute the corresponding y values
y = g(x)

# Plot the function normally
plt.figure()
plt.plot(x, y, label='g(x) = 105 * (2e)^(-x/100)')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.title('Normal Plot of g(x)')
plt.legend()
plt.grid(True)
plt.show()

# Plot the function using plt.semilogy
plt.figure()
plt.semilogy(x, y, label='g(x) = 105 * (2e)^(-x/100)')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.title('Semilog Plot of g(x)')
plt.legend()
plt.grid(True)
plt.show()