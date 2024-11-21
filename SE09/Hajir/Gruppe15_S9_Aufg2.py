import numpy as np

def Gruppe15_S9_Aufg2(A, A_tilde, b, b_tilde):
    # Solve the linear systems
    x = np.linalg.solve(A, b)
    x_tilde = np.linalg.solve(A_tilde, b_tilde)
    
    # Calculate the condition number of A
    cond_A = np.linalg.cond(A, np.inf)
    
    # Calculate the norms
    norm_A_diff = np.linalg.norm(A - A_tilde, np.inf)
    norm_b_diff = np.linalg.norm(b - b_tilde, np.inf)
    norm_A = np.linalg.norm(A, np.inf)
    norm_b = np.linalg.norm(b, np.inf)
    
    # Check the condition for dxmax
    if cond_A * (norm_A_diff / norm_A) < 1:
        dxmax = (cond_A / (1 - cond_A * (norm_A_diff / norm_A))) * ((norm_A_diff / norm_A) + (norm_b_diff / norm_b))
    else:
        dxmax = float('NaN')
    
    # Calculate the actual relative error dxobs
    dxobs = np.linalg.norm(x - x_tilde, np.inf) / np.linalg.norm(x, np.inf)
    
    return x, x_tilde, dxmax, dxobs