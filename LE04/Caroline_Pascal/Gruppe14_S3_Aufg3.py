import numpy as np
import matplotlib.pyplot as plt

# Funktion
def f(x):
    return 5 * (2 * x**2)**(1/3)

def g(x):
    return 10**5 * (2 * np.e)**(-x / 100)

def h(x):
    return ((10**(2 * x)) / (2**(5 * x)))**2


# Generate x Values
x = np.linspace(0.1, 100, 500)

# Plot the functions
plt.figure(figsize=(12,8))

# plot functions
plt.subplot(2,2,1)
plt.plot(x, f(x), label='f(x) = 5*(2x^2)^(1/3)')
plt.plot(x, g(x), label='g(x) = 10^5 * (2e)^(-x/100)')
plt.plot(x, h(x), label='h(x) = (10^(2x))/(2^(5x))^2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Scale')
plt.legend()

# Plot loglog
plt.subplot(2, 2, 2)
plt.loglog(x, f(x), label='f(x) = 5*(2x^2)^(1/3)')
plt.loglog(x, g(x), label='g(x) = 10^5 * (2e)^(-x/100)')
plt.loglog(x, h(x), label='h(x) = (10^(2x))/(2^(5x))^2')
plt.xlabel('log(x)')
plt.ylabel('log(y)')
plt.title('Log-Log Scale')
plt.legend()

# Plot semilog x
plt.subplot(2, 2, 3)
plt.semilogx(x, f(x), label='f(x) = 5*(2x^2)^(1/3)')
plt.semilogx(x, g(x), label='g(x) = 10^5 * (2e)^(-x/100)')
plt.semilogx(x, h(x), label='h(x) = (10^(2x))/(2^(5x))^2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Semi-Log Plot x-Axis')
plt.legend()

# Plot semilog y
plt.subplot(2, 2, 4)
plt.semilogy(x, f(x), label='f(x) = 5*(2x^2)^(1/3)')
plt.semilogy(x, g(x), label='g(x) = 10^5 * (2e)^(-x/100)')
plt.semilogy(x, h(x), label='h(x) = (10^(2x))/(2^(5x))^2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Semi-Log Plot y-Axis')
plt.legend()
plt.legend()

plt.tight_layout()
plt.show()