import numpy as np 

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

# Matrix A
A = np.array(
    [
        [-1, 2, 3, 2, 5, 4, 3, -1],
        [3, 4, 2, 1, 0, 2, 3, 8],
        [2, 7, 5, -1, 2, 1, 3, 5],
        [3, 1, 2, 6, -3, 7, 2, -2],
        [5, 2, 0, 8, 7, 6, 1, 3],
        [-1, 3, 2, 3, 5, 3, 1, 4],
        [8, 7, 3, 6, 4, 9, 7, 9],
        [-3, 14, -2, 1, 0, -2, 10, 5],
    ], dtype=float
)

# Vektor b
b = np.array([ -11, 103, 53, -20, 95, 78, 131, -26], dtype=float)
    
R, detA, x = gauss(A, b)

# Ausgabe
print("Dreiecksmatrix R:")
print(R)
print("Determinante von A:", detA)
print("Lösung x:", x)
