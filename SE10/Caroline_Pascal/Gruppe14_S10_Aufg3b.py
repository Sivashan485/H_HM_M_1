import numpy as np
import timeit
import matplotlib.pyplot as plt
from Gruppe14_S10_Aufg3a import Name_S10_Aufg3a
from Gruppe14_S6_Aufg2 import gauss

dim = 3000
A = np.diag(np.diag(np.ones((dim, dim)) * 4000)) + np.ones((dim, dim))
dum1 = np.arange(1, int(dim / 2 + 1), dtype=np.float64).reshape((int(dim / 2), 1))
dum2 = np.arange(int(dim / 2), 0, -1, dtype=np.float64).reshape((int(dim / 2), 1))
x = np.append(dum1, dum2, axis=0)
b = A @ x
x0 = np.zeros((dim, 1))
tol = 1e-4


def jacobi_method():
    Name_S10_Aufg3a(A, b, x0, tol, "Jacobi")

jacobi_time = timeit.timeit(jacobi_method, number=1)

def gauss_seidel_method():
    Name_S10_Aufg3a(A, b, x0, tol, "Gauss")

gauss_seidel_time = timeit.timeit(gauss_seidel_method, number=1)

def linalg_solve_method():
    np.linalg.solve(A, b)

linalg_solve_time = timeit.timeit(linalg_solve_method, number=1)


def AugabeS6():
    gauss(A, b)

gaus_time = timeit.timeit(AugabeS6, number=1)

# Print the results
print(f"Jacobi method time: {jacobi_time:.6f} seconds")
print(f"Gauss-Seidel method time: {gauss_seidel_time:.6f} seconds")
print(f"np.linalg.solve method time: {linalg_solve_time:.6f} seconds")
print(f"Selfmade Gauss method time: {gaus_time:.6f} seconds")

# 64bit CPU
#Jacobi method time: 80.534246 seconds
#Gauss-Seidel method time: 19.357203 seconds
#np.linalg.solve method time: 0.392417 seconds
#Selfmade Gauss method time: 21.381685 seconds




x_gauss_seidel, _, _ = Name_S10_Aufg3a(A, b, x0, tol, "Gauss")
x_jacobi, _, _ = Name_S10_Aufg3a(A, b, x0, tol, "Jacobi")
_,_,x_gauss = gauss(A, b)  
x_gauss = x_gauss.reshape(-1, 1)  
x_exact = x
print("GAUSS", x_gauss)
print("GAUS SEIDEL", x_gauss_seidel)
print("JACOBI", x_jacobi)

error_gauss_seidel = np.abs(x_exact - x_gauss_seidel)
error_jacobi = np.abs(x_exact - x_jacobi)
error_gauss = np.abs(x_exact - x_gauss)

plt.figure(figsize=(12, 6))
plt.plot(error_gauss_seidel, label='Gauss-Seidel')
plt.plot(error_jacobi, label='Jacobi')
plt.plot(error_gauss, label='Gauss')
plt.xlabel('Index')
plt.ylabel('Absolute Error')
plt.title('Absolute Error of Solutions')
plt.legend()
plt.show() 

# Wir stellen fest, dass die Gauss-Seidel-Methode den geringsten absoluten Fehler aufweist, 
# gefolgt von der Jacobi-Methode. Die selbstgemachte Gauss-Methode hat den größten Fehler.
