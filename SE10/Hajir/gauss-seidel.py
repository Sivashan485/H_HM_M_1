import numpy as np

A = np.array([[8,5,2], [5,9,1], [4,2,7]])
b = np.array([19,5,34])
xStart = np.array([1,-1,3])

def gauss_seidel(A, xStart, b, n):
    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    R = np.triu(A, 1)
    for i in range(n):
        xNext = -(np.linalg.inv(D + L)) @ R @ xStart + (np.linalg.inv(D + L)) @ b
        xStart = xNext
    return xNext

print(gauss_seidel(A, xStart, b, 3))
print("")



def a_posteriori(A, xStart, b, n):
    L = np.tril(A, -1)
    R = np.triu(A, 1)
    D = np.diag(np.diag(A))
    B_norm = np.linalg.norm((-(np.linalg.inv(D + L)) @ R), np.inf)
    x_n = gauss_seidel(A, xStart, b, n)
    x_n_1 = gauss_seidel(A, xStart, b, n-1)
    
    return (B_norm/(1-B_norm)) * np.linalg.norm(x_n - x_n_1, np.inf)
    
print("absoluter Fehler" , a_posteriori(A, xStart, b, 3))
print("")



def a_priori_iterations(A, xStart, b, epsilon):
    L = np.tril(A, -1)
    R = np.triu(A, 1)
    D = np.diag(np.diag(A))
    B_norm = np.linalg.norm((-(np.linalg.inv(D + L)) @ R), np.inf)
    
    x_next = gauss_seidel(A, xStart, b, 1)
    
    n = (np.log((epsilon * (1 - B_norm)) / np.linalg.norm((x_next - xStart), np.inf))) / (np.log(B_norm))
    return np.ceil(n)

print("Anzahl Iterationen", a_priori_iterations(A, xStart, b, 0.0001))
print("")

print ("Anzahl Iterationen bei x0 = x2", a_priori_iterations(A, gauss_seidel(A, xStart, b, 2), b, 0.0001))
print ("")
