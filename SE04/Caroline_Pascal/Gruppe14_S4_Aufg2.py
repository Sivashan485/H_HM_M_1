import numpy as np
import matplotlib.pyplot as plt

# Define the fixed-point iteration function
def fixed_point_iteration(alpha, k0, steps=100):
    k_values = [k0]
    for _ in range(steps):
        k_new = alpha * k_values[-1] * (1 - k_values[-1])
        k_values.append(k_new)
    return k_values

# Initial value k0 = 0.1 (10% of the children are infected)
k0 = 0.1

# Investigate the convergence for different values of α ∈ [0, 4]
alphas = np.linspace(0, 4, 100)
steps = 100
fixpoints = []

for alpha in alphas:
    k_values = fixed_point_iteration(alpha, k0, steps)
    fixpoints.append(k_values[-1])

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(alphas, fixpoints, label="Fixpoint")
plt.xlabel("α (Infection rate)")
plt.ylabel("Fixpoint k")
plt.title("Fixpoint behavior as a function of the infection rate α")
plt.grid(True)
plt.legend()
plt.show()

# (a)
# Die Fixpunktiteration konvergiert für einen attraktiven Fixpunkt für α > 1. 
# Für α ≤ 1 gibt es keinen attraktiven Fixpunkt.

# (b)
# Ein Fixpunkt in diesem Kontext bedeutet, dass der Anteil der infizierten Kinder 
# stabilisiert und sich im Laufe der Zeit nicht ändert.
# Das bedeutet, dass die Krankheit einen stabilen Zustand in der Bevölkerung erreicht hat.

# (c)
# Die Fixpunktgleichung lautet: k = α * k * (1 - k)
# Dies vereinfacht sich zu: k = α * k - α * k^2
# Umstellen ergibt: α * k^2 - α * k + k = 0
# Dies ist eine quadratische Gleichung in k: k^2 - k + k/α = 0
# Die Lösung der quadratischen Gleichung ergibt: k = 0 oder k = 1 - 1/α
# Daher ist der Fixpunkt k = 1 - 1/α für α > 1.
