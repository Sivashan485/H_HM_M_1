# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 14:43:17 2020

Höhere Mathematik 1, Serie 11, Aufgabe 3 (Gerüst)

@author: knaa
"""
import numpy as np
import matplotlib.pyplot as plt


detail = 1000                       #number of pixels in x and y direction
maxit = 120                         #maximum n for iterations (influences how detailed the structures are shown when zooming in)
x_min = -2                          #minimim value of x-interval
x_max = 0.7                         #maximum value of x-interval
y_min = -1.4                        #minimim vale of y-interval
y_max = 1.4                         #minimim vale of y-interval

a = np.linspace(x_min,x_max,detail,dtype=np.float64)  #define real axis [x_min,x_max]
b = np.linspace(y_min,y_max,detail,dtype=np.float64)  #define imaginary axis [y_min,y_max]

B = np.zeros((detail,detail))         #for color values n 

[x,y] = np.meshgrid(a,b)              #to create the complex plane with the axes defined by a and b
C = np.array(x+y*1j, np.complex128)   #creating the plane
Z = np.zeros(C.shape, np.complex128)  #initial conditions (first iteration), Z has same dimension as C
for n in np.arange(1,maxit+1):        #start iteration
  Z = Z**2 + C                        #calculating Z
  expl = np.where(np.abs(Z) > 2)      #finding exploded values (i.e. with an absolute value > 2)
  Z[expl] = 0                         #removing from iteration
  C[expl] = 0                         #removing from plane
  B[expl] = n                         #saving color value n

plt.figure(1)
B = B/np.max(np.max(B))               #deviding by max value for correct color
plt.imshow(B,extent=[x_min,x_max,y_min,y_max],origin='lower',interpolation='bilinear')   #display image
plt.colorbar()
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()

