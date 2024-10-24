import numpy as np

def newton_raphson(f, f_prime, x0, tolerance=1e-3, max_iterations=100):
    x = x0
    for i in range(max_iterations):
        fx = f(x)
        fpx = f_prime(x)
        print(f'Iteration {i+1}: x = {x}, f(x) = {fx}, f\'(x) = {fpx}')
        if abs(fx) < tolerance:
            return x
        x = x - fx / fpx
    raise ValueError('Max iterations reached without convergence')

def f(x):
    return (np.pi / 3) * (15 * x**2 - x**3) - 471

def f_prime(x):
    return (np.pi / 3) * (2 * 15 * x - 3 * x**2)

try:
    root = newton_raphson(f, f_prime, 9)
    print(f'Die Wurzel ist: {root}')
except ValueError as error:
    print(error)