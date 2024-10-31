import timeit


def fact_rec(n):
    import numpy as np
    if n < 0 or np.trunc(n) != n:
        raise Exception('The factorial is defined only for positive integers')
    if n <=1:
        return 1
    else:
        return n*fact_rec(n-1)

def fact_for(n):
    import numpy as np
    liste = []
    if n < 0 or np.trunc(n) != n:
        raise Exception('The factorial is defined only for positive integers')
    i = 0
    result = 1
    for x in range(n):
        if n==0:
            return 0
        else:
            result = 1
            i  = i+1
            liste.append(i)
            for ax in liste:
                result *=ax
    return result
print (fact_rec(100))
print (fact_for(100))


t1 = timeit.repeat("fact_rec(500)", "from __main__ import fact_rec", number=100)

avg_t1 = sum(t1) / len(t1)

print(f"Average execution time for fact_rec: {avg_t1:.6f} seconds")
