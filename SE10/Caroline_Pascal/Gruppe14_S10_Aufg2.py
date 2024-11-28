import numpy as np
import matplotlib.pyplot as plt

'''
Aufgabe 2)
'''
b = np.array([19, 5, 34])
x_0 = np.array([1, -1, 3])
A = np.array([[8,5,2], [5, 9,1], [4, 2, 7]])

'''
a-posteriory error estimate
''' 
def a_posteriori(x_0, n, A, b): 
    L = np.tril(A, -1)
    R = np.triu(A, 1)
    D = np.diag(np.diag(A))
    B_norm = np.linalg.norm((-(np.linalg.inv(D + L) @ R)), np.inf)
    x_n = gauss_seidel(x_0, b, n, A)
    x_n_1 = gauss_seidel(x_0, b, n-1, A)
    a_abs = ((B_norm) / (1 - B_norm)) * np.linalg.norm(x_n - x_n_1, np.inf)
    return a_abs


'''
Iterative method
'''
def gauss_seidel(x_0, b, n, A):
    L = np.tril(A, -1)
    R = np.triu(A, 1)
    D = np.diag(np.diag(A))

    for i in range(n):
        x_next = -(np.linalg.inv(D + L)) @ R @ x_0 + (np.linalg.inv(D + L)) @ b
        x_0 = x_next
        
    return x_next


'''
Aufgabe 2d) 
''' 
tol = 10**-4

def number_of_iterations(x_0, n, tol, A):
    L = np.tril(A, -1)
    R = np.triu(A, 1)
    D = np.diag(np.diag(A))
    B_norm = np.linalg.norm((-(np.linalg.inv(D + L) @ R)), np.inf)
    
    x_1 = gauss_seidel(x_0, b, 1, A)
    n = (np.log((tol*(1 - B_norm)) / np.linalg.norm((x_1 - x_0), np.inf))) / (np.log(B_norm))
    
    return np.ceil(n)

'''
Aufgabe 2e)
'''
tol = 10**-4

def number_of_iterations_1e(x_0, tol, A):
    L = np.tril(A, -1)
    R = np.triu(A, 1)
    D = np.diag(np.diag(A))
    B_norm = np.linalg.norm((-(np.linalg.inv(D + L) @ R)), np.inf)
    
    x_2 = gauss_seidel(x_0, b, 2, A)
    x_3 = gauss_seidel(x_0, b, 3, A)
    n = (np.log((tol*(1 - B_norm)) / np.linalg.norm((x_3 - x_2), np.inf))) / (np.log(B_norm))
    
    return np.ceil(n)


'''
Prints:
'''
print('Solution: \n', gauss_seidel(x_0, b, 3, A))

print('A-posteriori error estimate: \n', a_posteriori(x_0, 3, A, b))
print('Number of iterations x0 -- x1: \n', number_of_iterations(x_0, 3, tol, A))
print('Number of iterations x2 -- x3: \n', number_of_iterations_1e(x_0, tol, A))
