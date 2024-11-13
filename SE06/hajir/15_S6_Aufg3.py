import numpy as np
import gausieren

m = np.array(
    [
        [-1, 2, 3, 2, 5, 4, 3, -1],
        [3, 4, 2, 1, 0, 2, 3, 8],
        [2, 7, 5, -1, 2, 1, 3, 5],
        [3, 1, 2, 6, -3, 7, 2, -2],
        [5, 2, 0, 8, 7, 6, 1, 3],
        [-1, 3, 2, 3, 5, 3, 1, 4],
        [8, 7, 3, 6, 4, 9, 7, 9],
        [-3, 14, -2, 1, 0, -2, 10, 5],
    ]
)

b = np.array([[-11], [103], [53], [-20], [95], [78], [131], [-26]])

x_gausieren, tauschCounter = gausieren(m.copy(), b.copy())

x_numpy = np.linalg.solve(m, b)

print("Solution using gausieren function:", x_gausieren)
print("Solution using numpy.linalg.solve:", x_numpy)
print("Are the solutions identical?", np.allclose(x_gausieren, x_numpy))

# Kommentar:
# Die Lösungen sind identisch, wenn np.allclose True zurückgibt.