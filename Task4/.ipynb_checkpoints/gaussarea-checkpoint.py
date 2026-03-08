#!/usr/bin/env python
# coding: utf-8

# In[9]:


import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

A = float(input("Input the amplitude: "))
x0 = float(input("Input the x coordinate of the peak"))
sig = float(input("Input the width of the peak: "))
z0 = float(input("Input the offset in y"))

x = np.linspace(-10, 10, 200)

def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

y = gauss(x, A, x0, sig, z0)
integral, err = sp.integrate.quad(gauss, -np.inf, np.inf, args=(A, x0, sig, z0))

plt.plot(x, y, label=np.round(integral, 2))
plt.fill_between(x, y)
plt.legend()
area = A*sig * np.sqrt(2*np.pi)

print(f"{integral}, {area}") # almost same

