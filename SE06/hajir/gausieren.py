import numpy as np

# Matrix A_4
m = np.array(
    [
        [20, 10, 0],
        [50, 30, 20],
        [200, 150, 100]
    ], dtype=float
)

# Vektor b
b = np.array([[150], [470], [2150]], dtype=float)


def gausieren(m, b):
    tauschCounter = 0
    n = len(m)

    for i in range(n):
        # Find the pivot row
        max_row = i
        for k in range(i + 1, n):
            if abs(m[k][i]) > abs(m[max_row][i]):
                max_row = k

        # Swap the pivot row with the current row
        if max_row != i:
            m[[i, max_row]] = m[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
            tauschCounter += 1

        # Eliminate the entries below the pivot
        for k in range(i + 1, n):
            factor = m[k][i] / m[i][i]
            m[k][i:] -= factor * m[i][i:]
            b[k] -= factor * b[i]

    # Rückwärtseinsetzen
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(m[i, i + 1:], x[i + 1:])) / m[i][i]

    return x, tauschCounter


print(gausieren(m, b))