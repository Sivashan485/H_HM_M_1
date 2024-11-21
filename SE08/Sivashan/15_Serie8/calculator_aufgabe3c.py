import numpy as np

np.set_printoptions(precision=4)

A= np.array([
    [20000, 30000, 10000],
    [10000, 17000, 6000],
    [2000, 3000, 2000]
])

b= np.array([
    [5720000],
    [3300000],
    [836000]
])



A2= np.array([
    [19900, 29900, 9900],
    [9900, 16900, 5900],
    [1900, 2900, 1900]
])

b2= np.array([
    [5820000],
    [3400000],
    [936000]
])


A_disturbed = A - 100
b_disturbed = b + 100000

# Solve the disturbed system
x_disturbed = np.linalg.solve(A_disturbed, b_disturbed)

print("\nOLD A : \n",A)
print("\nOLD B : \n",b)
print("\nNEW A : \n",A_disturbed)
print("\nNEW b : \n",b_disturbed)
print("\n\n--------------------------------\n\n")

# Solve the original system for comparison
x_original = np.linalg.solve(A, b)

print(x_disturbed - x_original)
# Calculate the relative error
relative_error = np.linalg.norm(x_disturbed - x_original) / np.linalg.norm(x_original)
print("Lösung des exakten Gleichungssystems: \n", x_original)
print("\nLösung des gestörten Gleichungssystems:\n", x_disturbed)

print("relative error by python : ",relative_error)