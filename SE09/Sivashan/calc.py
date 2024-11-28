import numpy as np 
from sympy import symbols, Eq, solve


F = (10**(-7))
condA = 60003

A = np.array([
    [1 ,0 ,2],
    [0,1,0],
    [10**(-4), 0, 10**(-4)]
])

AF = np.array([
    [1 + F,0 + F ,2+F],
    [0+F,1+F,0+F],
    [10**(-4)+F, 0 +F, 10**(-4)+F]
])



ARL = np.linalg.norm((A-AF), np.inf)/np.linalg.norm((A),np.inf)
x = symbols('x')
equation = Eq(0.01, condA / (1 - condA * ARL) * (ARL + x))
solution = solve(equation, x)
print(f"Solution for x: {solution}")



