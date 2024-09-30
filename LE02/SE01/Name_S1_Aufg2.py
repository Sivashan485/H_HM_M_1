import numpy as np
import matplotlib.pyplot as plt

# F
def polynom_fx(a_n, x):
    result = np.zeros_like(x)
    i = len(a_n)-1
    for a in a_n:
        if i>=0:
            result += a * x**i
        i = i -1
    return result

def polynom_fx_1(a_n, x):
    result = np.zeros_like(x)
    i = len(a_n) - 1
    for a in a_n:
        if (i >= 1):
            result += i*a*x**(i-1)
        i = i - 1
    return result

def polynom_Fx(a_n, x):
    result = np.zeros_like(x)
    i = len(a_n)
    for a in a_n:
        current_result = 0
        if (i >= 0):
            current_result = x ** (i)
            if i>=1:
                current_result = current_result * (1/i)*a
            result += current_result
        i = i - 1
    return result

