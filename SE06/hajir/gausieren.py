import numpy as np

# Matrix A_4
A = np.array([[1, -2, 3], [-5, 4, 1], [2, -1, 3]], dtype=float)
b = np.array([1, 9, 5], dtype=float)

def gausieren(A, b):
    tauschCounter = 0
    n = len(A)

    for i in range(n):
        # Find the pivot row
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k

        # Swap the pivot row with the current row
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
            tauschCounter += 1

        # Eliminate the entries below the pivot
        for k in range(i + 1, n):
            factor = A[k][i] / A[i][i]
            A[k][i:] -= factor * A[i][i:]
            b[k] -= factor * b[i]

    # Rückwärtseinsetzen
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i][i]

    return x, tauschCounter

print(gausieren(A, b))