import numpy as np
import timeit

# Funktion zur QR-Zerlegung mittels Gramm-Schmidt-Verfahren (bereits implementiert)
def qr_decomposition(A):
    """
    QR-Zerlegung mittels Gramm-Schmidt-Verfahren
    :param A: Input-Matrix (m x n)
    :return: Q (orthogonal), R (obere Dreiecksmatrix)
    """
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    
    for j in range(n):
        v = A[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]
    
    return Q, R

# Gegebene Matrix A aus Aufgabe 1
A = np.array([
    [20000, 30000, 10000],
    [10000, 17000, 6000],
    [2000, 3000, 2000]
])

# Laufzeitmessung für die gegebene Matrix
def my_qr_test():
    qr_decomposition(A)

def numpy_qr_test():
    np.linalg.qr(A)

# Zeitmessung für beide Methoden
t1 = timeit.repeat("my_qr_test()", globals=globals(), number=100)
t2 = timeit.repeat("numpy_qr_test()", globals=globals(), number=100)

avg_t1 = np.mean(t1) / 100  # Durchschnittliche Zeit pro Lauf meiner QR-Zerlegung
avg_t2 = np.mean(t2) / 100  # Durchschnittliche Zeit pro Lauf von numpy.linalg.qr

# Test mit zufälliger 100 x 100 Matrix
random_matrix = np.random.rand(100, 100)

# Laufzeitmessung mit zufälliger Matrix
def my_qr_test_random():
    qr_decomposition(random_matrix)

def numpy_qr_test_random():
    np.linalg.qr(random_matrix)

t3 = timeit.repeat("my_qr_test_random()", globals=globals(), number=10)
t4 = timeit.repeat("numpy_qr_test_random()", globals=globals(), number=10)

avg_t3 = np.mean(t3) / 10  # Durchschnittliche Zeit pro Lauf meiner QR-Zerlegung für die große Matrix
avg_t4 = np.mean(t4) / 10  # Durchschnittliche Zeit pro Lauf von numpy.linalg.qr für die große Matrix


print("Durchschnittliche Laufzeit für meine QR-Zerlegung (A):", avg_t1)
print("Durchschnittliche Laufzeit für numpy.linalg.qr (A):", avg_t2)
print("Durchschnittliche Laufzeit für meine QR-Zerlegung (große Matrix):", avg_t3)
print("Durchschnittliche Laufzeit für numpy.linalg.qr (große Matrix):", avg_t4)


"""
Effizienz: Die Funktion numpy.linalg.qr ist deutlich schneller und skaliert besser bei größeren Matrizen.
Komplexität: Meine Implementierung verwendet das Gramm-Schmidt-Verfahren, welches nicht optimal für große Matrizen ist, während numpy.linalg.qr optimierte Algorithmen (z. B. Householder-Transformationen) nutzt.
Empfehlung: Für reale Anwendungen sollte numpy.linalg.qr verwendet werden, da es stabiler und effizienter ist.    
"""