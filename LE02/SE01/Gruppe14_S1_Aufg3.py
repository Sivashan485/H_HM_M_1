import numpy as np
import timeit

def fact_rec(n):
    if n < 0 or np.trunc(n) != n:
        raise Exception('The factorial is defined only for positive integers')
    if n <= 1:
        return 1
    else:
        return n * fact_rec(n - 1)

def fact_for(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Vergleichen der Ausführungszeiten
n = 500
t1 = timeit.repeat("fact_rec(" + str(n) + ")", "from __main__ import fact_rec", number=100)
t2 = timeit.repeat("fact_for(" + str(n) + ")", "from __main__ import fact_for", number=100)

print("Durchschnittliche Ausführungszeit von fact_rec:", np.mean(t1))
print("Durchschnittliche Ausführungszeit von fact_for:", np.mean(t2), "\n")

# Vergleich der Ausführungszeiten
if np.mean(t1) < np.mean(t2):
    print("Die Rekursive Funktion ist schneller als die nicht Rekursive Funktion um einen Faktor von", np.mean(t2) / np.mean(t1), "\n")
else:
    print("Die nicht Rekursive Funktion ist schneller als die Rekursive Funktion um einen Faktor von", np.mean(t1) / np.mean(t2), "\n")

# Überprüfung der oberen Grenze für die Fakultät als ganze Zahl
print("Fakultät berechnet durch die Rekursive Funktion:")
for n in range(190, 201):
    try:
        print("Fakultät von", n, "als ganze Zahl:", fact_rec(n))
    except OverflowError:
        print("Fakultät von", n, "überschreitet die obere Grenze für ganze Zahlen")

# Überprüfung der oberen Grenze für die Fakultät als ganze Zahl
print("Fakultät berechnet durch die nicht Rekursive Funktion: ")
for n in range(190, 201):
    try:
        print("Fakultät von", n, "als ganze Zahl:", fact_for(n))
    except OverflowError:
        print("Fakultät von", n, "überschreitet die obere Grenze für ganze Zahlen")
        
# Überprüfung der oberen Grenze für die Fakultät als reelle Zahl
for n in range(170, 172):
    try:
        print("Fakultät von", n, "als reelle Zahl:", fact_rec(n))
    except OverflowError:
        print("Fakultät von", n, "überschreitet die obere Grenze für reelle Zahlen")
        

## Aufgabe 3 
# - die Methode mit der For-SChleife ist um den Faktor 10 
# schneller als die rekursive Methode
#