import numpy as np
import matplotlib.pyplot as plt
import timeit

# Rekursive Fakultät
def fact_rec(n):
    if n < 0 or np.trunc(n) != n:
        raise Exception('The factorial is defined only for positive integers')
    if n <= 1:
        return 1
    else: 
        return n * fact_rec(n-1)
    
# Fakultät mit einer For-Schleife
def fact_for(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Define a range of n values
n_values = range(1, 501, 50)
t1_times = []
t2_times = []

# Collect execution times for each n
for n in n_values:
    t1 = timeit.repeat("fact_rec({})".format(n), "from __main__ import fact_rec", number=100)
    t2 = timeit.repeat("fact_for({})".format(n), "from __main__ import fact_for", number=100)
    t1_times.append(np.mean(t1))
    t2_times.append(np.mean(t2))

# Plot
plt.figure(figsize=(10, 6))
plt.plot(n_values, t1_times, label='fact_rec', color='blue')
plt.plot(n_values, t2_times, label='fact_for', color='red')
plt.xlabel('n')
plt.ylabel('Execution time (s)')
plt.title('Execution time of fact_rec and fact_for')
plt.legend()
plt.grid(True)
plt.show()