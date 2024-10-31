import numpy as np

def sekanten(f, x0, x1, tol):
    f = np.vectorize(f)
    x1 = x1
    x0 = x0
    while abs(x1 - x0) > tol:
        x2 = x1 - ((x1 - x0) / (f(x1) - f(x0))) * f(x1)
        x0 = x1
        x1 = x2        
        print(x1)
    return x1

sekanten(lambda x: np.exp(float(x)**2) + float(x)**-3 - 10, -1,-1.2, 1e-3)