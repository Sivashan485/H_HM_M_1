import  numpy as np 

np.set_printoptions(precision=3)

I = np.array([[1,0,0], 
              [0,1,0], 
              [0,0,1]])


v = np.array([[np.sqrt(30) + 1], [-5], [2]])
u = (1 / np.linalg.norm(v)) * v

A = np.array([[1,-2,3],[-5,4,1],[2, -1 , 3 ]])

result = I - 2*u*u.T;
print(result)

print("Q1 * A ")
print(result*A)
