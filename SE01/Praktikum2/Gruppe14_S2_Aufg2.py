import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1.99, 2.01001, 0.00004)

function1 = x**7 - 14*x**6 + 84*x**5 - 280*x**4 + 560*x**3 - 672*x**2 + 448*x - 128
function2 = (x - 2)**7

plt.plot(x, function1, label="f1")
plt.plot(x, function2, label="f2")
plt.legend()
plt.show()
