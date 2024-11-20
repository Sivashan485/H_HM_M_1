import numpy as np

def householder_reflection(A):
    m, n = A.shape
    Q = np.eye(m)
    R = A.copy()
    
    for i in range(n):
        x = R[i:, i]
        e = np.zeros_like(x)
        e[0] = np.linalg.norm(x) * (1 if x[0] >= 0 else -1)
        u = x + e
        u = u / np.linalg.norm(u)
        
        H = np.eye(m)
        H[i:, i:] -= 2.0 * np.outer(u, u)
        
        R = H @ R
        Q = Q @ H.T
    
    return Q, R

A = np.array([[1, -2, 3], [-5, 4, 1], [2, -1, 3]])
b = np.array([1, 9, 5])

Q, R = householder_reflection(A)

np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)

print("Q:\n", Q)
print("R:\n", R)

x = np.linalg.solve(R, Q.T @ b)
print("x =", x)
