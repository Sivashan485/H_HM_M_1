import numpy as np

def Name_S6_Aufg2(A, b):
    n = len(b)
    A = A.astype(float)  
    b = b.astype(float)  
    L = np.eye(n)  # Initialize L as an identity matrix

    # Gauss Elimination
    for i in range(n):
        # Pivot
        max_row = np.argmax(np.abs(A[i:n, i])) + i
        if i != max_row:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
            L[[i, max_row], :i] = L[[max_row, i], :i]  # Swap the rows in L as well

        # Elimination
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            L[j, i] = factor  # Store the factor in L
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    # Determinante Berechnen
    detA = np.prod(np.diag(A))

    # Rückwärtseinsetzen
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    U = np.triu(A)  # Ensure U is upper triangular

    return L, U, detA, x

# Example usage
if __name__ == "__main__":
    A = np.array([[-1, 2, 3, 2, 5, 4, 3, -1],
                  [ 3, 4, 2, 1, 0, 2, 3, 8],
                  [ 2, 7, 5, -1, 2, 1, 3, 5],
                  [ 3, 1, 2, 6, -3, 7, 2, -2], 
                  [ 5, 2, 0, 8, 7, 6, 1, 3],
                  [-1, 3, 2, 3, 5, 3, 1, 4],
                  [ 8, 7, 3, 6, 4, 9, 7, 9],
                  [-3, 14, -2, 1, 0, -2, 10, 5]], dtype=float)


    b = np.array([-11,103,53,-20,95,78,131,-26], dtype=float)

    L, U, detA, x = Name_S6_Aufg2(A, b)
    print("Lower triangular matrix L:")
    print(L)
    print("\nUpper triangular matrix U:")
    print(U)
    print("\nDeterminant of A:")
    print(detA)
    print("\nSolution vector x:")
    print(x)