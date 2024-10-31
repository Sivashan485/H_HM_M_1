import numpy as np

# Define A-Matrix
A = np.array([[-1, 2, 3, 2, 5, 4, 3, -1],
                  [ 3, 4, 2, 1, 0, 2, 3, 8],
                  [ 2, 7, 5, -1, 2, 1, 3, 5],
                  [ 3, 1, 2, 6, -3, 7, 2, -2], 
                  [ 5, 2, 0, 8, 7, 6, 1, 3],
                  [-1, 3, 2, 3, 5, 3, 1, 4],
                  [ 8, 7, 3, 6, 4, 9, 7, 9],
                  [-3, 14, -2, 1, 0, -2, 10, 5]], dtype=float)

# Define b-Vector
b = np.array([-11,103,53,-20,95,78,131,-26], dtype=float)

# 
def gaussian_elimination_script_based(A, b):
    n = A.shape[0]
    A = A.astype(float)
    b = b.astype(float)
    detA = 1  # Initialize determinant multiplier

    # Forward elimination following script guidelines
    for i in range(n):
        # Check for zero pivot and perform row swapping if necessary
        if A[i, i] == 0:
            found = False
            for j in range(i + 1, n):
                if A[j, i] != 0:
                    A[[i, j]] = A[[j, i]]  # Swap rows in A
                    b[[i, j]] = b[[j, i]]  # Swap rows in b
                    detA *= -1  # Row swap changes determinant sign
                    found = True
                    break
            if not found:
                # If no pivot found in the column, matrix is singular
                raise ValueError("Matrix is singular; no unique solution exists.")

        # Update determinant with pivot element
        detA *= A[i, i]

        # Elimination step according to the script
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    # Backward substitution to find solution vector x
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    # Extract the upper triangular matrix after elimination
    A_triangle = np.triu(A)

    return A_triangle, detA, x

# Execute with the sample matrix and vector
A_triangle_script, detA_script, x_script = gaussian_elimination_script_based(A, b)
A_triangle_script, detA_script, x_script



A_triangle, detA, x = gaussian_elimination_script_based(A, b)
print("Lower triangular matrix L:")
print(A_triangle)
print("\nDeterminant of A:")
print(detA)
print("\nSolution vector x:")
print(x)