import numpy as np
import matplotlib.pyplot as plt

# Koeffizienten der quadratischen Gleichung
a = 1
b = 4
c = 16

# Diskriminante berechnen
D = b**2 - 4*a*c

# Lösungen der quadratischen Gleichung
w1 = (-b + np.sqrt(D * 1j)) / (2*a)
w2 = (-b - np.sqrt(D * 1j)) / (2*a)

# Rücksubstitution
z1 = np.sqrt(w1)
z2 = -np.sqrt(w1)
z3 = np.sqrt(w2)
z4 = -np.sqrt(w2)

# Lösungen in der Gaußschen Zahlenebene plotten
solutions = [z1, z2, z3, z4]

plt.figure()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.scatter([z.real for z in solutions], [z.imag for z in solutions], color='red')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.title('Lösungen der Gleichung $z^4 + 4z^2 + 16 = 0$ in der Gaußschen Zahlenebene')
plt.show()