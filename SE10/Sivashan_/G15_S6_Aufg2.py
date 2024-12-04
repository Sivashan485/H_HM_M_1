import numpy as np

def gausieren(A, b):
    n = len(A)
    tauschCounter = 0

    # Forward elimination
    for i in range(n):
        # Pivoting
        max_row = i + np.argmax(np.abs(A[i:, i]))
        if A[max_row, i] == 0:
            return None, None, 0  # No unique solution
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
            tauschCounter += 1

        # Elimination
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    # Calculate determinant
    detA = (-1) ** tauschCounter * np.prod(np.diag(A))

    return A, detA, x