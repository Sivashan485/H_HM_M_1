import numpy as np
import matplotlib.pyplot as plt

# given data
# Year = x: 1997 = 0, 1999 = 2, 2006 = 9, 2010 = 13
x_shifted = np.array([0, 2, 9, 13])
# Number in Days = y 
y = np.array([150, 104, 172, 152])

# 3rd degree polynomial
#f(x) = ax**3 + bx**2 + cx + d
#
# x = 0 
#f(0) = a(0)**3 + b(0)**2 + c(0) + d = 150
# x = 2
#f(2) = a(2)**3 + b(2)**2 + c(2) + d = 104
# x = 9
#f(9) = a(9)**3 + b(9)**2 + c(9) + d = 172
# x = 13
#f(13) = a(13)**3 + b(13)**2 + c(13) + d = 152
#
#A = np.array([[   0,   0,  0, 1],  = 150
#              [   8,   4,  2, 1],  = 104
#              [ 729,  81,  9, 1],  = 172
#              [2197, 169, 13, 1]]) = 152
# b = np.array([150, -46, 22, 2])
#
#b = np.array([150, 104, 172, 152])

# Given data
# Construct the Vandermonde matrix for a third-degree polynomial
A = np.vander(x_shifted, 4)
print("Matrix A: ", A)

b = y
print("Vector b: ", b)

# Solve the linear system to find polynomial coefficients
coefficients = np.linalg.solve(A, y)
print("Calculated Coefficients: ", coefficients)

# Gauss
def gauss(A, b):
    # Kopie der Matrix A
    R = np.copy(A)
    # L Matrix
    L = np.eye(n)
    # Kopie des Vektors b
    b_copy = np.copy(b)
    # Dimension der Matrix A
    n = R.shape[0]
    # Determinante von A initialisieren
    detA = 1


    for i in range(n):
        # Pivot-Element finden
        pivot = R[i, i]
        # Wenn Pivot-Element 0 ist, dann ist die Matrix singulär
        if pivot == 0:
            raise ValueError("Matrix ist singulär")

        # Zeile i durch das Pivot-Element dividieren
        R[i, :] /= pivot
        b_copy[i] /= pivot

        # Alle Zeilen unterhalb der i-ten Zeile eliminieren
        for j in range(i+1, n):
            factor = R[j, i]
            R[j, :] -= factor * R[i, :]
            b_copy[j] -= factor * b_copy[i]

        # Determinante aktualisieren 
        detA *= pivot

    # Rückwärtseinsetzen
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = b_copy[i]
        for j in range(i+1, n):
            x[i] -= R[i, j] * x[j]
      
    return R, detA, x

A = np.vander(x_shifted, 4)
print("Matrix A: ", A)

b = y
print("Vector b: ", b)
    
R, detA, x = gauss(A, b)

# Ausgabe
print("Dreiecksmatrix R:")
print(R)
print("Determinante von A:", detA)
print("Lösung x:", x)
