import numpy as np

def GausSeidel(L, D, R, b, x0, tol):
    x_old = x0
    n = 0
    while True:
        x = -np.linalg.inv(D + L) @ R @ x_old + np.linalg.inv(D + L) @ b
        if np.linalg.norm(x - x_old, np.inf) < tol:
            break
        x_old = x
        n += 1
    norm_x0 = np.linalg.norm(x0, np.inf)
    norm_R = np.linalg.norm(np.linalg.inv(D + L) @ R, np.inf)
    if norm_x0 == 0 or norm_R == 0:
        n2 = float('inf')
    else:
        n2 = int(np.ceil(np.log(tol / norm_x0) / np.log(norm_R)))
    return x, n, n2

def Jacobi(L, D, R, b, x0, tol):
    x_old = x0
    n = 0
    while True:
        x = -np.linalg.inv(D) @ (L + R) @ x_old + np.linalg.inv(D) @ b
        if np.linalg.norm(x - x_old, np.inf) < tol:
            break
        x_old = x
        n += 1
    norm_x0 = np.linalg.norm(x0, np.inf)
    norm_LR = np.linalg.norm(np.linalg.inv(D) @ (L + R), np.inf)
    if norm_x0 == 0 or norm_LR == 0:
        n2 = float('inf')
    else:
        n2 = int(np.ceil(np.log(tol / norm_x0) / np.log(norm_LR)))
    return x, n, n2

def S10_Aufg3a(A, b, x0, tol, opt):
    L = np.tril(A, -1)
    D = np.diag(np.diag(A))
    R = np.triu(A, 1)

    if opt == "Gauss":
        xn, n, n2 = GausSeidel(L, D, R, b, x0, tol)
    else:
        xn, n, n2 = Jacobi(L, D, R, b, x0, tol)

    return xn, n, n2