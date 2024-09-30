import numpy as np
import matplotlib.pyplot as plt
from dask.sizeof import sizeof
#a_n = [1,-5,-30,110,29,-105]

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

def calculate_polynomial(a_n, xmin, xmax, step=0.1):
    x = np.arange(xmin, xmax, step)
    p = polynom_fx(a_n, x)
    dp = polynom_fx_1(a_n, x)
    pint = polynom_Fx(a_n, x)
    return x, p, dp, pint
a_n = np.array([1,-5,-30,110,29,-105])
xmin = -10
xman = 10
x, p, dp, pint = calculate_polynomial(a_n, xmin, xman)



plt.plot(x, p, color = "green")
plt.plot(x, dp, color = "gray")
plt.plot(x, pint, color="red")

plt.xlabel('x-Achse')
plt.ylabel('y-Achse')
plt.title('e')
plt.legend(['fx', 'fx 1' ,'FX'])
plt.ylim(-1600, 1600)
plt.xlim(-10, 10)

plt.grid()
plt.show()