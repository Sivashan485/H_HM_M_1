import numpy as np
import matplotlib.pyplot as plt

# Parameters
detail = 1000  # Number of pixels in x and y direction
maxit = 120  # Maximum number of iterations
x_min, x_max = -2, 0.7  # Bounds for the x-axis
y_min, y_max = -1.4, 1.4  # Bounds for the y-axis

# Define the real and imaginary axis
a = np.linspace(x_min, x_max, detail, dtype=np.float64)
b = np.linspace(y_min, y_max, detail, dtype=np.float64)

# Create a grid for the complex plane
B = np.zeros((detail, detail))  # For storing color values
x, y = np.meshgrid(a, b)
C = x + y * 1j  # Create the complex plane
Z = np.zeros_like(C, dtype=np.complex128)  # Initial condition

# Mandelbrot iteration
for n in range(1, maxit + 1):
    Z = Z**2 + C  # Iteration formula
    expl = np.abs(Z) > 2  # Check where |Z| > 2
    Z[expl] = 0  # Remove exploded values from Z
    C[expl] = 0  # Remove exploded values from C
    B[expl] = n  # Save the iteration count

# Normalize the color values for display
B = B / np.max(B)

# Plot the Mandelbrot set
plt.figure(figsize=(10, 10))
plt.imshow(B, extent=[x_min, x_max, y_min, y_max], origin='lower', interpolation='bilinear', cmap='hot')
plt.colorbar(label="Iteration count")
plt.title("Mandelbrot Set")
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")

print("Displaying plot...")
plt.show()
print("Plot displayed.")