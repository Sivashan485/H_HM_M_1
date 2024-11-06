#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:17:32 2024

@author: sivashan
"""

import numpy as np


# Matrix A_4
A_4 = np.array([
    [-1,  2,  3,  2,  5,  4,  3, -1],
    [ 3,  4,  2,  1,  0,  2,  3,  8],
    [ 2,  7,  5, -1,  2,  1,  3,  5],
    [ 3,  1,  2,  6, -3,  7,  2, -2],
    [ 5,  2,  0,  8,  7,  6,  1,  3],
    [-1,  3,  2,  3,  5,  3,  1,  4],
    [ 8,  7,  3,  6,  4,  9,  7,  9],
    [-3, 14, -2,  1,  0, -2, 10,  5]
])

# Vektor b
b = np.array([-11, 103, 53, -20, 95, 78, 131, -26])


def Name_S6_Aufg2(A, b):
    n = len(b)
    A = A.astype(float)
    b = b.astype(float)
    
    #Spalte zu Spalte
    for i in range(n):
        # Pivoting
        max_row = np.argmax(np.abs(A[i:n, i])) + i
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]
        
        # Elimination
        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]
    
    # Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    
    # Determinant
    detA = np.prod(np.diag(A))
    
    # Upper triangular matrix
    A_triangle = np.triu(A)
    
    return A_triangle, detA, x




# Example usage
A_triangle, detA, x = Name_S6_Aufg2(A_4, b)
print("Upper triangular matrix:\n", A_triangle)
print("Determinant of A:", detA)
print("Solution vector x:", x)

