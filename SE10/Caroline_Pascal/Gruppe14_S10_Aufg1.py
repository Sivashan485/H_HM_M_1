import numpy as np
import matplotlib.pyplot as plt

'''
Aufgabe 1a - 1c)
'''
b = np.array([19, 5, 34])
n = 3
x_0 = np.array([1, -1, 3])
A = np.array([[8,5,2], [5, 9,1], [4, 2, 7]])

'''
LDR decomposition of A
'''
D = np.diag(np.abs(A))
D_inv = np.diag(1/D)
L = np.tril(A, -1)
R = np.triu(A, 1)
B_norm = np.linalg.norm(-D_inv @ (L + R), np.inf)

'''
a-posteriory error estimate
''' 
def a_posteriori(x_0, n, B_norm): 
    x_n = iterative_methode(x_0, b, n, D_inv, L, R)
    x_n_1 = iterative_methode(x_0, b, n-1, D_inv, L, R)
    a_abs = ((B_norm) / (1 - B_norm)) * np.linalg.norm(x_n - x_n_1, np.inf)
    return a_abs

'''
check for Diagonal dominance
'''
def is_diagonally_dominant(A):
    # Sum of non-diagonal elements
    S = np.sum(np.abs(A), axis=1) - D
    return np.all(D > S)

print("Is A diagonally dominant?", is_diagonally_dominant(A))

'''
Iterative method
'''
def iterative_methode(x_0, b, n, D_inv, L, R):
    
    for i in range(n):
        x_next = -D_inv @ (L + R) @ x_0 + D_inv @ b
        x_0 = x_next
        
    return x_next


'''
Aufgabe 1d) 
''' 
tol = 10**-4

def number_of_iterations(x_0, n, tol, B_norm, D_inv, L, R):
    x_1 = iterative_methode(x_0, b, 1, D_inv, L, R)
    n = (np.log((tol*(1 - B_norm)) / np.linalg.norm((x_1 - x_0), np.inf))) / (np.log(B_norm))
    
    return np.ceil(n)

'''
Aufgabe 1e)
'''
tol = 10**-4

def number_of_iterations_1e(x_0, n, tol, B_norm, D_inv, L, R):
    x_2 = iterative_methode(x_0, b, 2, D_inv, L, R)
    x_3 = iterative_methode(x_0, b, 3, D_inv, L, R)
    n = (np.log((tol*(1 - B_norm)) / np.linalg.norm((x_3 - x_2), np.inf))) / (np.log(B_norm))
    
    return np.ceil(n)


'''
Prints:
'''
print('D: \n', D)
print('Inverse of D: \n', D_inv)
print('L: \n',L)
print('R: \n',R)

print('Solution: \n', iterative_methode(x_0, b, n, D_inv, L, R))
print('B: \n', B_norm)

print('A-posteriori error estimate: \n', a_posteriori(x_0, n, B_norm))
print('Number of iterations: \n', number_of_iterations(x_0, n, tol, B_norm, D_inv, L, R))
print('Number of iterations for 1e: \n', number_of_iterations_1e(x_0, n, tol, B_norm, D_inv, L, R))
