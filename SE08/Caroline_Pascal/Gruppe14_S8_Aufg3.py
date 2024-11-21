import numpy as np

def inverse_matrix_and_errors(A, delta_b):
    n = A.shape[0]
    # Erstellen einer erweiterten Matrix [A | I]
    augmented_matrix = np.hstack((A, np.eye(n)))
    
    for i in range(n):
        # Pivot-Element finden
        pivot = augmented_matrix[i, i]
        if pivot == 0:
            raise ValueError("Matrix ist singulär und hat keine Inverse.")
        
        # Zeile i durch das Pivot-Element dividieren
        augmented_matrix[i, :] /= pivot
        
        # Alle anderen Zeilen eliminieren
        for j in range(n):
            if i != j:
                factor = augmented_matrix[j, i]
                augmented_matrix[j, :] -= factor * augmented_matrix[i, :]
    
    # Die rechte Hälfte der erweiterten Matrix ist die Inverse von A
    inverse_A = augmented_matrix[:, n:]
    
    # Absoluter Fehler in x berechnen
    delta_x = inverse_A @ delta_b
    
    # Relative Fehler berechnen
    x = np.linalg.solve(A, np.ones(n))  # Berechne x für relative Fehlerberechnung
    relative_error = np.abs(delta_x / x)
    
    return inverse_A, delta_x, relative_error

# Beispiel mit einer 3x3-Matrix
"""
A = np.array([[20000, 30000, 10000], 
              [10000, 17000, 6000],
              [2000, 3000, 2000]], dtype=float)
inverse_A = inverse_matrix(A)
"""

A = np.array([[20100, 30000, 10000], 
              [10010, 17000, 6000],
              [1916, 3000, 2000]], dtype=float)

delta_b = np.array([100000, 100000, 100000], dtype=float)

inverse_A, delta_x, relative_error = inverse_matrix_and_errors(A, delta_b)
print("Matrix A:")
print(A)
print("Inverse von A:")
print(inverse_A)
print("Absoluter Fehler in x:")
print(delta_x)
print("Relativer Fehler:")
print(relative_error)