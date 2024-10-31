# Sekantenverfahren

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


def sekantenVerfahren(f, x0, x1, tol):
        
    while abs( x1 - x0) > tol:
        x2 = x1 - ((x1 - x0) / (f(x1) - f(x0))) * f(x1)
        x0 = x1
        x1 = x2
        
        print (x1)
    return x1


