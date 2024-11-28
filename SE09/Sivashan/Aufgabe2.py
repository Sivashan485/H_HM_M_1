import numpy as np 

def Name_S9_Aufg2(A, Ae, b, eb):
    A_norm = np.linalg.norm(A, np.inf)
    A_norm_inv = np.linalg.norm(np.linalg.inv(A), np.inf)
    cond_A = np.linalg.cond(A, np.inf)
    AtoAe = np.linalg.norm(A - Ae, np.inf) / A_norm
    btoEb = np.linalg.norm(b - eb, np.inf) / np.linalg.norm(b, np.inf)
    
    if cond_A * AtoAe < 1:
        dx_max = cond_A * (AtoAe + btoEb) / (1 - cond_A * AtoAe)
    else:
        dx_max = np.nan

    x = np.linalg.solve(A, b)
    xe = np.linalg.solve(Ae, eb)

    dx_obs = np.linalg.norm(x - xe, np.inf) / np.linalg.norm(x, np.inf)

    return x, xe, dx_max, dx_obs

