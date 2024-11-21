import numpy as np

def Gruppe14_S9_Aufg2(A, A_tilde, b, b_tilde):
    
    #solve the linear systems
    x = np.linalg.solve(A, b)
    x_tilde = np.linalg.solve(A_tilde, b_tilde)
    
    #calculate the condition of A
    cond_A = np.linalg.cond(A, np.inf)
    
    
    # Calculate the norms
    norm_A_tilde = np.linalg.norm(A_tilde - A, np.inf)
    norm_b_tilde = np.linalg.norm(b_tilde - b, np.inf)
    norm_A = np.linalg.norm(A, np.inf)
    norm_b = np.linalg.norm(b, np.inf)
    
    # check the condition
    if cond_A * (norm_A_tilde / norm_A) < 1:
        dxmax = (cond_A / (1 - cond_A * (norm_A_tilde / norm_A))) * ((norm_A_tilde / norm_A) + (norm_b_tilde / norm_b))
    else:
        dxmax = float('NaN')
        
    # Calculate relative error
    rel_error = np.linalg.norm(x - x_tilde, np.inf) / np.linalg.norm(x, np.inf)
        
    return x, x_tilde, dxmax, rel_error