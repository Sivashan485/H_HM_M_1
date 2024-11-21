# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:26:09 2020

Höhere Mathematik 1, Serie 8, Gerüst für Aufgabe 2

Description: calculates the QR factorization of A so that A = QR
Input Parameters: A: array, n*n matrix
Output Parameters: Q : n*n orthogonal matrix
                   R : n*n upper right triangular matrix            
Remarks: none
Example: A = np.array([[1,2,-1],[4,-2,6],[3,1,0]]) 
        [Q,R]=Serie8_Aufg2(A)

@author: knaa
"""

import numpy as np
import timeit

np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)

def Serie8_Aufg2(A):
    
    A = np.copy(A)                       #necessary to prevent changes in the original matrix A_in
    A = A.astype('float64')              #change to float
    
    n = np.shape(A)[0]
    
    if n != np.shape(A)[1]:
        raise Exception('Matrix is not square') 
    
    Q = np.eye(n)
    R = A
    
    for j in np.arange(0,n-1):
        a = np.copy(R[j:,j]).reshape(n-j,1)     
        e = np.eye(n-j)[:,0].reshape(n-j,1)
        length_a = np.linalg.norm(a)
        if a[0] >= 0: 
            sig = length_a
        else: 
            sig = -length_a 
        v = a + sig * e
        u = v / np.linalg.norm(v)
        H = np.eye(n-j) - 2 * np.dot(u, u.T)
        Qi = np.eye(n)
        Qi[j:,j:] = H
        R = np.dot(Qi, R)
        Q = np.dot(Q, Qi)
        
    return(Q,R)

# Kontrolle der Lösung aus Aufgabe 1
A = np.array([[1,-2, 3],[-5,4,1],[2,-1,3]])
Q, R = Serie8_Aufg2(A)
print("Q:\n", Q)
print("R:\n", R)

# Laufzeitvergleich
t1 = timeit.repeat("Serie8_Aufg2(A)", "from __main__ import Serie8_Aufg2, A", number=100)
t2 = timeit.repeat("np.linalg.qr(A)", "from __main__ import np, A", number=100)
avg_t1 = np.average(t1)/100
avg_t2 = np.average(t2)/100
print("Average time for Serie8_Aufg2: ", avg_t1)
print("Average time for np.linalg.qr: ", avg_t2)

# Laufzeitvergleich für eine 100x100 Matrix
Test = np.random.rand(100,100)
t3 = timeit.repeat("Serie8_Aufg2(Test)", "from __main__ import Serie8_Aufg2, Test", number=100)
t4 = timeit.repeat("np.linalg.qr(Test)", "from __main__ import np, Test", number=100)
avg_t3 = np.average(t3)/100
avg_t4 = np.average(t4)/100
print("Average time for Serie8_Aufg2 (100x100): ", avg_t3)
print("Average time for np.linalg.qr (100x100): ", avg_t4)

# Kommentar
"""
d)
Die Laufzeit der selbst implementierten QR-Zerlegung ist im Vergleich zur numpy.linalg.qr-Funktion deutlich langsamer.
Dies liegt daran, dass numpy.linalg.qr in C implementiert ist und optimierte Algorithmen verwendet.
Für größere Matrizen wird dieser Unterschied noch deutlicher.
"""
