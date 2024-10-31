import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return x**7 - 14*x**6 + 84*x**5 - 280*x**4 + 560*x**3 - 672*x**2 + 448*x - 128

def f2(x):
    return (x-2)**7

x = np.linspace(1.99, 2.01, 501)

y1 = f1(x)
y2 = f2(x)

plt.plot(x, y1, label='f1(x) = x^7 - 14x^6 + 84x^5 - 280x^4 + 560x^3 - 672x^2 + 448x - 128')
plt.plot(x, y2, label='f2(x) = (x - 2)^7', linestyle='dashed')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Comparison of f1(x) and f2(x)')
plt.grid(True)
plt.show()