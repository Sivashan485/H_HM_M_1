#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:54:52 2024

@author: sivashan
"""

import numpy as np
import matplotlib.pyplot as plt

def iterate_k(alpha, k):
    return alpha * k * (1 - k)

k0 = 0.1


def fixpunkt_iteration(k0, alpha, steps=50):
    k_values = [k0]
    for i in range(steps):
        k_next = iterate_k(k_values[-1], alpha)
        k_values.append(k_next)
    return k_values

alphas = np.linspace(0, 4, 100) 
steps = 50

plt.figure(figsize=(10, 6))

for alpha in [0.5, 1.0, 2.0, 2.5, 3.0, 3.5, 4.0]:
    k_values = fixpunkt_iteration(k0, alpha, steps)
    plt.plot(k_values, label=f'α = {alpha}')

plt.xlabel('Iterationsschritt')
plt.ylabel('Anteil erkrankter Kinder k')
plt.title('Konvergenzverhalten der Fixpunktiteration für verschiedene α')
plt.legend()
plt.grid(True)
plt.show()


# Aufgabe b 
# Ein Fixpunkt ist ein stabiler Zustand, in dem sich die Anzahl der erkrankten Kinder nicht mehr ändert. 
# In diesem Kontext bedeutet ein Fixpunkt, dass die Anzahl der kranken Kinder gleich bleibt. 
# Es gibt kein weiteres Ansteigen der Krankheit.


# Aufgabe C 
# k+1 = F(x) = a*ki(1-ki) = aki - aki² 
# F'(x) = a - aki  | F'(x) < 1
# a - aki < 1
# a < 1/(1-ki)
# Fixpunkt = ki = (a-1)/a 