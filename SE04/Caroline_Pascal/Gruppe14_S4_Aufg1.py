import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9

def F(x):
    return (230*x**4 + 18*x**3 + 9*x**2 - 9)/221

x = np.linspace(-2, 2, 100)


plt.figure(figsize=(10, 6)) 
plt.plot(x, f(x), label="f(x)")
plt.plot(x, F(x), label="F(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("f(x) and F(x)")
plt.grid(True)
plt.legend()
plt.show()
