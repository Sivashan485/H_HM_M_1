# Name_S2_Aufg3.py

import math
import matplotlib.pyplot as plt

def calculate_side_length(s_n):
    return math.sqrt(2 - 2 * math.sqrt(1 - (s_n ** 2) / 4))

# Initial number of sides
n = 6
s_n = 1  # Initial side length for hexagon

# Lists to store the number of sides and corresponding perimeter
sides = []
perimeters = []

# Calculate perimeters for increasing values of n
for i in range(20):  # Adjust range for larger n
    sides.append(n)
    perimeter = n * s_n
    perimeters.append(perimeter)
    
    # Calculate the side length for the next polygon with 2n sides
    s_n = calculate_side_length(s_n)
    n *= 2

# Plot the results
plt.plot(sides, perimeters, marker='o')
plt.xlabel('Number of sides (2n)')
plt.ylabel('Perimeter (2n * s2n)')
plt.title('Perimeter of inscribed polygons as a function of number of sides')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()



# Name_S2_Aufg3.py

import math
import matplotlib.pyplot as plt

def calculate_side_length_new(s_n):
    return math.sqrt((s_n ** 2) / (2 * (1 + math.sqrt(1 - (s_n ** 2) / 4))))

# Initial number of sides
n = 6
s_n = 1  # Initial side length for hexagon

# Lists to store the number of sides and corresponding perimeter
sides = []
perimeters = []

# Calculate perimeters for increasing values of n
for i in range(20):  # Adjust range for larger n
    sides.append(n)
    perimeter = n * s_n
    perimeters.append(perimeter)
    
    # Calculate the side length for the next polygon with 2n sides
    s_n = calculate_side_length_new(s_n)
    n *= 2

# Plot the results
plt.plot(sides, perimeters, marker='o')
plt.xlabel('Number of sides (2n)')
plt.ylabel('Perimeter (2n * s2n)')
plt.title('Perimeter of inscribed polygons as a function of number of sides (New Formula)')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()