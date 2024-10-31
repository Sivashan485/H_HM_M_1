#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:12:33 2024

@author: sivashan
"""

import numpy as np
import matplotlib.pyplot as plt

phi_values = np.linspace(0, np.pi, 400)
y_values = np.sin(phi_values) - phi_values + 0.5 * np.pi

plt.plot(phi_values, y_values, label=r"$\sin(\varphi) - \varphi + \frac{\pi}{2}$")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(np.pi / 2, color='red', linestyle='--', label=r'$\varphi = \frac{\pi}{2}$')
plt.xlabel(r"Winkel $\varphi$ (rad)")
plt.ylabel("Funktionswert")
plt.grid(True)
plt.legend()
plt.show()