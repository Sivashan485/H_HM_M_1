import numpy as np

# Die Schwierigkeit ist, dass es beim Newton-Verfahren noch das f'(x) als Argument braucht.
def sekantenVerfahren(f, x0, x1, tol):
    while abs(x1 - x0) > tol:
        temp_x2 = x1 - ((x1 - x0) / (f(x1) - f(x0))) * f(x1)
        x0 = x1
        x1 = temp_x2
    return x1

def f(x):
    return np.exp(x**2) + x**(-3) - 10

print(sekantenVerfahren(f, -1.0, -1.2, 1e-4))