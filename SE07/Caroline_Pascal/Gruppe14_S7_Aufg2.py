import scipy as sp
import scipy.linalg as la
import numpy as np

# Matrix
A = [[0.8, 2.2, 3.6],
     [2.0, 3.0, 4.0],
     [1.2, 2.0, 5.8]];

# Vektor
b = [2.4, 1.0, 4.0]

# LU-Zerlegung
P, L_scipy, U_scipy = la.lu(A)

# Print the result
print("\nScipy computed P:")
print(P)
print("\nScipy computed L:")
print(L_scipy)
print("\nScipy computed U:")
print(U_scipy)


# Es sind keine Unterschiede zu finden. Die LR-Zerlegung 
# wird genau gleich berechnet.