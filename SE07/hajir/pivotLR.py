import scipy as sp
import numpy as np

A = np.array([[0.8, 2.2, 3.6], [2.0, 3.0, 4.0], [1.2, 2.0, 5.8]])
b = np.array([2.4, 1.0, 4.0])

# Perform LU decomposition
P, L, U = sp.linalg.lu(A)

# Solve for x using the LU decomposition
lu, piv = sp.linalg.lu_factor(A)
x = sp.linalg.lu_solve((lu, piv), b)

print("L:\n", L)
print("U:\n", U)
print("x:\n", x)