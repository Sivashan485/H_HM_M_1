import numpy as np
import matplotlib.pyplot as plt

def gauss(A, b):
    # Dimension der Matrix A
    n = A.shape[0]
    # Kopie der Matrix A
    R = np.copy(A)
    # Kopie des Vektors b
    b_copy = np.copy(b)
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

# Given data
# Year = x: 1997 = 0, 1999 = 2, 2006 = 9, 2010 = 13
x_shifted = np.array([0, 2, 9, 13], dtype=float)
# Number in Days = y 
y = np.array([150, 104, 172, 152], dtype=float)

# Construct the Vandermonde matrix for a third-degree polynomial
A = np.vander(x_shifted, 4)
print("Matrix A: ", A)

# Vector b is simply the y values
b = y
print("Vector b: ", b)

# Solve the linear system to find polynomial coefficients using least squares
coefficients, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
print("Calculated Coefficients: ", coefficients)

# Generate a fine x-axis for plotting the polynomial
x_fine = np.arange(0, x_shifted[-1] + 1, 0.1)

# Evaluate the polynomial at the fine x points
y_fine = np.polyval(coefficients, x_fine)

# Convert the x-axis back to the original years for plotting
x_fine_years = x_fine + 1997
x_years = x_shifted + 1997  # Original years for data points

# Plot the data points and the polynomial
plt.figure(figsize=(10, 6))
plt.plot(x_fine_years, y_fine, label='Fitted Polynomial')
plt.scatter(x_years, y, color='red', label='Data Points')
plt.xlabel('Year')
plt.ylabel('Number of Days with Extreme UV Exposure')
plt.title('Polynomial Fit to UV Exposure Data')
plt.legend()
plt.grid(True)
plt.show()


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
