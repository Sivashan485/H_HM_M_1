
import numpy as np
def f(x):
    return np.exp(x**2) + x**(-3) - 10

def sekanten(x0,x1,tol):
    while (abs(x1-x0)>tol):
        f_x0 = f(x0)
        f_x1 = f(x1)
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        x0  = x1
        x1 = x2
    return x1
    
    


x0 = -1.0
x1 = -1.2
tole = 1e-4

root = sekanten( x0, x1, tole)
print("The root is:", root)