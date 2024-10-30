import numpy as np
import matplotlib.pyplot as plt

x = np.logspace(-1, 2, 1000)

def f(x):
    return 5/ (2*x**2)**(1/3)

def g(x):
    return 10**5 * (2*np.e)**(-x/100)

def h(x):
    return (10**(2*x)/2**(5*x))**2


plt.semilogy(x, f(x))
plt.show()
plt.semilogy(x, g(x))
plt.show()
plt.semilogy(x, h(x))
plt.show()
