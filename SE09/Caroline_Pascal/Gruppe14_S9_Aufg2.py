import numpy as np

def Gruppe14_S9_Aufg2(A, A_tilde, b, b_tilde):
    
    x = np.linalg.solve(A, b)
    x_tilde = np.linalg.solve(A_tilde, b_tilde)
    
    cond_A = np.linalg.cond(A, np.inf)
    
    