import numpy as np

A = np.array([[8,5,2], [5,9,1], [4,2,7]])
b = np.array([19,5,34])
xStart = np.array([1,-1,3])
n = 3

D = np.diag(np.diag(A))
Di = np.diag(1/np.diag(A))
L = np.tril(A, -1)
R = np.triu(A, 1)

B_norm = np.linalg.norm((-Di @ (L + R)), np.inf)


def jacobi(A, xStart, b, n):    
    for i in range(n):
        xNext = -Di @ (L + R) @ xStart + Di @ b
        xStart = xNext
    return xNext
    
print(jacobi(A, xStart, b, n))




def a_posteriori(A, xStart, b, n):
    x_n = jacobi(A, xStart, b, n)
    x_n_1 = jacobi(A, xStart, b, n-1)
    
    return (B_norm/(1-B_norm)) * np.linalg.norm(x_n - x_n_1, np.inf)
    

print("absoluter Fehler" , a_posteriori(A, xStart, b, n))

def a_priori_iterations(A, xStart, b, epsilon):
    B_norm = np.linalg.norm((-Di @ (L + R)), np.inf)
    x_1 = jacobi(A, xStart, b, 1)
    n = (np.log((epsilon * (1 - B_norm)) / np.linalg.norm((x_1 - xStart), np.inf))) / (np.log(B_norm))
    return np.ceil(n)

    

print("Anzahl Iterationen", a_priori_iterations(A, jacobi(A, xStart, b, 2), b, 0.0001))