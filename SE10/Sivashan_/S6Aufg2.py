import numpy as np

def gausieren(m, b):
    tauschCounter = 0

    for i in range(0, len(m)):
        # Spalte i
        i = 0
        j = i + 1
        while [i < len(m)]:
            # Tausche Zeilen
            while m[j][i] != 0:
                if j == len(m) - 1:
                    return "Nicht reguläre Matrix"
                j += 1

            m[[i, j]] = m[[j, i]]
            b[[i, j]] = b[[j, i]]
            tauschCounter += 1
            j = i + 1

            # Elimination
            for j in range(i + 1, len(m)):
                lamda = m[i][i] / m[j][i]
                m[j][i] = lamda * m[j][i] - m[i][i]
                j += 1
            i += 1
            
    # Rückwärtseinsetzen
    x = np.zeros(len(m))
    x[len(m) - 1] = b[len(m) - 1] / m[len(m) - 1][len(m) - 1]
    for i in range(len(m) - 2, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, len(m)):
            x[i] -= m[i][j] * x[j]
        x[i] /= m[i][i]
        
    return x, tauschCounter
    
