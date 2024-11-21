import numpy as np

def iterations():
    for i in range(1000):
        A = np.array.rand(100, 100)
        b = np.array.rand(100, 1)
        A_tilde = A + np.random.rand(100, 100) / 1e5
        b_tilde = b + np.random.rand(100, 1) / 1e5