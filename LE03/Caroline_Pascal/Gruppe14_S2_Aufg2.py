import numpy as np 
import matplotlib.pyplot as plt

def f1(x):
    return x**7 - 14*x**6 + 84*x**5 - 280*x**4 + 560*x**3 - 672*x**2 + 448*x - 128

def f2(x):
    return (x - 2)**7

def g1(x):
    return x / (np.sin(1 + x) - np.sin(1))

def g2(x):
    return

x1 = np.linspace(1.99, 2.01, 501)
x2 = np.arange((-1e-14), 1e-14, 1e-17)

# Plot f1 and f2
plt.plot(x1, f1(x1), label='f1(x)')
plt.plot(x1, f2(x1), label='f2(x)')
plt.legend()
plt.grid()
plt.show()

# Plot g
plt.plot(x2, g1(x2), label='g1(x)')
plt.plot(x2, g2(x2), label='g2(x)')
plt.legend()
plt.grid()
plt.show()
