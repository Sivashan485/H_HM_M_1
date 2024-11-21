import numpy as np 

# Input matrices and vectors
I1 = np.eye(2)  # Identity matrix
A = np.array([[-0.926,  3.88], 
              [0.971, 1.848]])

b = np.array([[1], [9], [5]])

# a1 and e1 definitions
a1 = np.array([[-0.926], [0.971]])
e1 = np.array([[1], [0]])

# Calculate v1 (Householder vector)
v1 = a1 + (-1)*np.linalg.norm(a1)* e1

# Normalize v1 to get u1
u1 = v1 / np.linalg.norm(v1)

# Householder reflection matrix H1
H1 = I1 - (2 * (u1 @ u1.T))

# Set numpy print options for precision
np.set_printoptions(precision=3, suppress=True)

print("v1:")
print(v1)

print("\nu1:")
print(u1)

print("\nH1 (Householder reflection matrix):")
print(H1)

# Transform A using H1 to get H+ (apply H1 to the first column of A)
#H_plus = H1 @ A
print("\nH+ (Transformed A):")
#print(H_plus)


A_D = np.array([
    [1,-2,3],
    [-5,4,1],
    [2,-1,3]
])

Q1 = np.array([
    [-0.183,0.913,-0.365],
    [0.913,0.295,0.282],
    [-0.365,0.282,0.887]
])



Q2 = np.array([
    [1,0,0],
    [0,-0.69,0.724],
    [0,0.724,0.69]
])

R = Q2@Q1@A_D

print("Q")
Q = Q1.T@Q2.T
print (Q)

print("A")
print(R)
print("QT")
print(Q.T)
Qt__b = (Q.T@b)
print(Qt__b)
x = np.linalg.solve(R, Qt__b)
print(x)

A = np.array([
    [20, 30, 10],
    [10, 17, 6],
    [2,3,2]
])

B = np.array([
    [5720],[3300],[836]
])
print("inverse")
print(np.linalg.inv(A))