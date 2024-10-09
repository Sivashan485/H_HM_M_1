import numpy as np
import matplotlib.pyplot as plt

def g(x):
    return np.sin(x) / x

def g_new(x):
    a = x
    b = 0
    numerator = np.sin(a) - np.sin(b)
    denominator = 2 * np.cos((a + b) / 2) * np.sin((a - b) / 2)
    return numerator / denominator

x = np.linspace(-10, 10, 400)
x = x[x != 0] 

plt.plot(x, g(x), label='g(x) = sin(x) / x')

plt.plot(x, g_new(x), label='g_new(x) using sine addition theorem')

plt.xlabel('x')
plt.ylabel('g(x)')
plt.legend()
plt.title('Comparison of g(x) and g_new(x)')

plt.show()
