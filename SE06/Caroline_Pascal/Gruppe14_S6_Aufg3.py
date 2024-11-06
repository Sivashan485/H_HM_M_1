import numpy as np

def gauss(A, b):
    n = len(b)
    A = np.copy(A)
    L = np.eye(n)
    b_copy = np.copy(b)
    detA = 1

    for i in range(n):
        # Pivot-Element finden
        max_row = np.argmax(np.abs(A[i:n, i])) + i
        if i != max_row:
            A[[i, max_row]] = A[[max_row, i]]
            b_copy[[i, max_row]] = b_copy[[max_row, i]]
            L[[i, max_row], :i] = L[[max_row, i], :i] 

        pivot = A[i, i]
        if pivot == 0:
            raise ValueError("Matrix ist singulär")

        # Elimination
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            L[j, i] = factor
            A[j, i:] -= factor * A[i, i:]
            b_copy[j] -= factor * b_copy[i]

        # Determinante aktualisieren
        detA *= pivot

    # Rückwärtseinsetzen
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b_copy[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    R = np.triu(A)

    return L, R, detA, x


A = np.array([[-1, 2, 3, 2, 5, 4, 3, -1],
              [3, 4, 2, 1, 0, 2, 3, 8],
              [2, 7, 5, -1, 2, 1, 3, 5],
              [3, 1, 2, 6, -3, 7, 2, -2],
              [5, 2, 0, 8, 7, 6, 1, 3],
              [-1, 3, 2, 3, 5, 3, 1, 4],
              [8, 7, 3, 6, 4, 9, 7, 9],
              [-3, 14, -2, 1, 0, -2, 10, 5]], dtype=float)

b = np.array([-11, 103, 53, -20, 95, 78, 131, -26], dtype=float)

L, R, detA, x = gauss(A, b)
print("Lower triangular matrix L:")
print(L)
print("\nUpper triangular matrix U:")
print(R)
print("\nDeterminant of A:")
print(detA)
print("\nSolution vector x:")
print(x)

# Berechnung mit np.linalg.solve
x_numpy = np.linalg.solve(A, b)
print("\nSolution vector x (numpy):")
print(x_numpy)

# vergleichen der Lösungen
print("\nDifference between custom and numpy solutions:")
print(np.abs(x - x_numpy))
 
# Aufgabe 3: Gauss-Algorithmus
# Die Unterschiede zwischen den Implementierungen sind nur sehr gering
# und somit nicht relevant für grössere Zahlen. 
# Somit ist eine Implementierung mit numpy einfacher, jedoch nicht immer 
# empfehlenswert.