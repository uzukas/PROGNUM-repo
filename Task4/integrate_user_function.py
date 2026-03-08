#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from numpy import sin, cos, exp, pi
import scipy as sp

error = True

def f(x):
    return eval(func) # runs the code through a function to output a result

while error:
    func = input("Please enter a function of x using numbers, operators:(+, -, *, **, /), functions:(sin, cos, exp, pi): ")

    try:
        x = 1
        test = f(x)
        error = False
    except NameError:
        print("Please try again using only the specified functions and operators")
    except SyntaxError:
        print("Please make sure your syntax is correct.")        # defines the function and handles exceptions if incorrectly input function

error = True

while error:
    x1 = input("Enter the bottom bound for the integral")
    x2 = input("Enter the top bound for the integral")

    try:
        x1 = float(x1)
        x2 = float(x2)
        result, err = sp.integrate.quad(f, x1, x2)
        error = False
    except ValueError:
        print("Please only use numbers for the bounds.") # same thing but with bounds

print(f"The area of your integral from {x1} to {x2} is {result}")

# it feels like this part is unrelated to what i did above so I will do it in this section

def const_func(x):
    return x**4 + exp(sin(x) + cos(x))

mc_int, mc_err = sp.integrate.quad(const_func, 0, pi)

x_rand = np.random.uniform(0, pi, 10000)
y_rand = const_func(x_rand)

integral_mc = (pi - 0) * np.mean(y_rand)

print(f"The area OF A NON IMPUTED INTEGRAL THATS FOR SOME REASON HERE is: {mc_int}, {integral_mc} using 2 different methods")

