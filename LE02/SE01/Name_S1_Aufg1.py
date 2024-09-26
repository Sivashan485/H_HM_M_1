import numpy as np
import matplotlib.pyplot as plt

# Parameter
x = np.arange(-10, 10, 0.01)

# Funktion
f_x= x**5 - 5*x**4 - 30*x**3 + 110*x**2 + 29*x - 105

# Plot
plt.xlim()
plt.ylim()
plt.plot(x,f_x)    
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = x^5 - 5x^4 - 30x^3 + 110x^2 + 29x - 105')
plt.grid(True)
plt.show()
