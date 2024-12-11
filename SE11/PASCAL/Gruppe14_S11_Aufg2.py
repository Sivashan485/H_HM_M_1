import numpy as np
import matplotlib.pyplot as plt

# Koeffizienten der quadratischen Gleichung
a = 1
b = 4
c = 16

# Diskriminante berechnen
D = b**2 - 4*a*c

# Lösungen der quadratischen Gleichung
u1 = (-b + np.sqrt(D * 1j)) / (2*a)
u2 = (-b - np.sqrt(D * 1j)) / (2*a)

# Rücksubstitution
z1 = np.sqrt(u1)
z2 = -np.sqrt(u1)
z3 = np.sqrt(u2)
z4 = -np.sqrt(u2)

# Lösungen ausgeben
print("Z1: ", z1)
print("Z2: ", z2)
print("Z3: ", z3)
print("Z4: ", z4)

# Lösungen in der Gaußschen Zahlenebene plotten
solutions = [z1, z2, z3, z4]

plt.figure()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.scatter([z.real for z in solutions], [z.imag for z in solutions], color='red')
for z in solutions:
    plt.quiver(0, 0, z.real, z.imag, angles='xy', scale_units='xy', scale=1, color='blue')
plt.ylabel('Re(z)')
plt.xlabel('Im(z)')
plt.title('Lösungen der Gleichung $z^4 + 4z^2 + 16 = 0$ in der Gaußschen Zahlenebene')
plt.show()