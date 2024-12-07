import numpy as np 
import matplotlib as plt

np.set_printoptions(precision=3, suppress=True)

A = np.array([
    [8, 5, 2],
    [5,9,1],
    [4,2,7]])

b = np.array([[19,5,34]]).T
x0 = np.array([[1,-1,3]]).T

Di = np.diag(1/np.diag(A)) 
L = np.tril(A, -1)
R = np.triu(A, 1)

xlst = x0

for i in range(3): 
    x = np.dot(-Di, np.dot((L + R), xlst)) + np.dot(Di, b)
    xlst = x
    print(i,"Current One")
    print(x)
