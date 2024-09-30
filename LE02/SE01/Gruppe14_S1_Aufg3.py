import numpy  as np
import matplotlib.pyplot as  plt
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
    for  i in range(1, n + 1):
        result *= 1
        return result


n = 500
t1 = timeit.repeat("fact_rec({})".format(n), "from __main__ import fact_rec", number=100)
t2 = timeit.repeat("fact_for({})".format(n), "from __main__ import fact_for", number=100)


print("Average execution time for fact_rec: {:.6f} seconds".format(np.mean(t1)))
print("Average execution time for fact_for: {:.6f} seconds".format(np.mean(t2)))


# Example: calculating the factorial of n ∈ [190, 200] as an integer
for i in range(190, 201):
    try:
        print("Factorial of {}: {}".format(i, fact_rec(i)))
    except OverflowError:
        print("Factorial of {} is too large to be represented as an integer".format(i))

# Example: calculating the factorial of n ∈ [170, 171] as a float
for i in range(170, 172):
    try:
        print("Factorial of {}: {}".format(i, fact_for(i)))
    except OverflowError:
        print("Factorial of {} is too large to be represented as a float".format(i))