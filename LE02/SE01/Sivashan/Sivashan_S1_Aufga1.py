import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.01)
fx = x**5 - 5*x**4 - 30*x**3 + 110*x**2 + 29*x - 105
fx1 = 5*x**4 - 20*x**3 - 90*x**2 + 220*x + 29
Fx = (1/6)*x**6 - (5/5)*x**5 - (30/4)*x**4 + (110/3)*x**3 + (29/2)*x**2 - 105*x

plt.plot(x, fx, color="blue")
plt.plot(x, fx1, color = "green")
plt.plot(x, Fx, color="red")
plt.xlabel('x-Achse')
plt.ylabel('y-Achse')
plt.title('e')
plt.legend(['fx', 'fx 1' ,'FX'])
plt.ylim(-1600, 1600)
plt.xlim(-10, 10)

plt.grid()
plt.show()