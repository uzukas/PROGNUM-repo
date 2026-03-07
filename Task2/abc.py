#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

a = float(input("ax^2 + bx + c, input a: "))
b = float(input("ax^2 + bx + c, input b: "))
c = float(input("ax^2 + bx + c, input c: "))

D = b**2 - 4 * a * c

if D > 0:
    x1 = (-b + np.sqrt(D))/(2*a)
    x2 = (-b - np.sqrt(D))/(2*a)
    print(f"You have two real roots, x1 = {x1}, x2 = {x2}")
elif D == 0:
    x = (-b/(2*a))
    print(f"You have one real root, x = {x}")
elif D < 0:
    print("There are no real roots")

