import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (5 / (2 * x**2)**(1/3))

def g(x):
    return 10**5 * (2 * np.e**(-x/100))

def h(x):
    return ((10**(2*x))/(2**(5*x)))**2

#x = np.logspace(-1, 2, num=1000)  

x = np.linspace(0, 100, 500)  

y_f = f(x)
y_g = g(x)
y_h = h(x)

plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.plot(x, y_f, label="f(x)")
plt.plot(x, y_g, label="g(x)")
plt.plot(x, y_h, label="h(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Scale")
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 2)
plt.semilogx(x, y_f, label="f(x)")
plt.semilogx(x, y_g, label="g(x)")
plt.semilogx(x, y_h, label="h(x)")
plt.xlabel("log(x)")
plt.ylabel("y")
plt.title("Semilog-X Scale")
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 3)
plt.semilogy(x, y_f, label="f(x)")
plt.semilogy(x, y_g, label="g(x)")
plt.semilogy(x, y_h, label="h(x)")
plt.xlabel("x")
plt.ylabel("log(y)")
plt.title("Semilog-Y Scale")
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 4)
plt.loglog(x, y_f, label="f(x)")
plt.loglog(x, y_g, label="g(x)")
plt.loglog(x, y_h, label="h(x)")
plt.xlabel("log(x)")
plt.ylabel("log(y)")
plt.title("Log-Log Scale")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
