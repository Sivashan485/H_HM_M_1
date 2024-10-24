import numpy as np
import matplotlib.pyplot as plt


def fun(x):
    return 230 * x**4 - 18 * x**3 + 9 * x**2 - 221 * x - 9

def fixpunktFun(x):
    return (230 * x**4 - 18 * x**3 + 9 * x**2 - 9) / 221

x = np.linspace(-0.5, 0.5, 1000)

plt.plot(x, x, label='y=x')
plt.plot(x, fixpunktFun(x), label='fixpunktFun(x)')
plt.legend()
plt.show()

# Fixpunktiteration
x = 0.9
for i in range(100):
    x = fixpunktFun(x)
    print(x)
    
print(f'f(x) = {fun(x)}')
print(f'x = {x}')

print('alpha =', np.absolute((fixpunktFun(-0.5) - fixpunktFun(0.5)) / (-0.5 - 0.5)))



