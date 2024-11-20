import numpy as np

def inverse_matrix(A):
    """
    Berechnet die Inverse einer Matrix A mit dem Gauss-Jordan-Verfahren.
    """
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
    return inverse_A

# Beispiel
A = np.array([[20000, 30000, 10000], 
              [10000, 17000, 6000],
              [2000, 3000, 2000]], dtype=float)
inverse_A = inverse_matrix(A)
print("Matrix A:")
print(A)
print("Inverse von A:")
print(inverse_A)