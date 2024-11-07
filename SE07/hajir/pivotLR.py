import scipy as sp
import numpy as np
from scipy.linalg import lu, lu_solve, lu_factor

A = np.array([[0.8, 2.2, 3.6], [2.0, 3.0, 4.0], [1.2, 2.0, 5.8]])
b = np.array([2.4, 1.0, 4.0])

# Perform LU decomposition
P, L, U = lu(A)

# Solve for x using the LU decomposition
lu, piv = lu_factor(A)
x = lu_solve((lu, piv), b)

print("L:\n", L)
print("U:\n", U)
print("x:\n", x)