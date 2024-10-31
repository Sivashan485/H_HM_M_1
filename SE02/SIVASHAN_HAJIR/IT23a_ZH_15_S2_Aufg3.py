import matplotlib.pyplot as plt
import numpy as np
import math
def s2n(s_n):
    return math.sqrt(2 - 2 * math.sqrt(1 - (s_n**2) / 4))

def calculateSumLength(n, s_n):
    return n * s_n

n_values = []
length_sums = []

n = 6
s_n = 1
iterations = 500

for i in range(iterations):
    n_values.append(n)
    length_sums.append(calculateSumLength(n, s_n))
    
    # Update s_n to s_2n for the next iteration
    s_n = s2n(s_n)
    n = 2*n_values[-1]


# Plot the results
plt.plot(n_values, length_sums)
plt.title('Sum of Side Lengths as a Function of Number of Edges (2n)')
plt.xlabel('Number of Edges (log scale)')
plt.ylabel('Sum of Side Lengths')
plt.grid(True)
plt.xscale('log')
plt.legend()
plt.show()


def s2n_b(s_n):
    #Da die Verwendung der Wurzel und der Division numerisch stabiler ist, insbesondere bei größeren Werten von sn2.
    return math.sqrt((s_n**2) / (2 * (1 + math.sqrt(1 - (s_n**2) / 4))))

n_values = []
length_sums = []
n = 6
s_n = 1


for i in range(iterations):
    n_values.append(n)
    length_sums.append(calculateSumLength(n, s_n))
    
    # Update s_n to s_2n for the next iteration
    s_n = s2n_b(s_n)
    n = 2*n_values[-1]

# Plot the results
plt.plot(n_values, length_sums)
plt.title('Sum of Side Lengths as a Function of Number of Edges (2n)')
plt.xlabel('Number of Edges (log scale)')
plt.ylabel('Sum of Side Lengths')
plt.grid(True)
plt.xscale('log')
plt.legend()
plt.show()