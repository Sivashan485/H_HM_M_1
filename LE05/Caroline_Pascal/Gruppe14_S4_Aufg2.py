import numpy as np
import matplotlib.pyplot as plt

# Fixpunktiteration basierend auf der Gleichung ki+1 = α * ki * (1 - ki)

# a) Untersuchen des Konvergenzverhaltens der Fixpunktiteration

def fixpunkt_iteration(alpha, k0, steps=100):
    k_values = [k0]
    for _ in range(steps):
        k_new = alpha * k_values[-1] * (1 - k_values[-1])
        k_values.append(k_new)
    return k_values

# Initialer Startwert k0 = 0.1 (10% der Kinder sind erkrankt)
k0 = 0.1

# Untersuchen der Konvergenz für verschiedene Werte von α ∈ [0,4]
alphas = np.linspace(0, 4, 100)
steps = 100
fixpunkte = []

for alpha in alphas:
    k_values = fixpunkt_iteration(alpha, k0, steps)
    fixpunkte.append(k_values[-1])

# Plotten der Ergebnisse
plt.figure(figsize=(10, 6))
plt.plot(alphas, fixpunkte, label="Fixpunkt")
plt.xlabel("α (Infektionsrate)")
plt.ylabel("Fixpunkt k")
plt.title("Fixpunktverhalten in Abhängigkeit von der Infektionsrate α")
plt.grid(True)
plt.axhline(0.5, color="r", linestyle="--", label="k = 0.5")
plt.legend()
plt.show()