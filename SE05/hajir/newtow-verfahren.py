import numpy as np
import sympy as sp

def newton(f, x0, max_iter=100):
    x = sp.Symbol('x')
    f_prime = sp.diff(f, x)
    f = sp.lambdify(x, f)
    f_prime = sp.lambdify(x, f_prime)
    
    x = x0
    for i in range(max_iter):
        x = x - f(x) / f_prime(x)
        print(x)
    return x

f = sp.sympify('exp(x**2) + x**-3 - 10')
newton(f, 2, 4)