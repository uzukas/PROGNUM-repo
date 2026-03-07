#!/usr/bin/env python
# coding: utf-8

# In[1]:


fibonacci = [1, 2]

fibonacci_calculated = 0

n_loop = 98

while n_loop > 0:
    fibonacci_calculated += fibonacci[-2]
    fibonacci_calculated += fibonacci[-1]
    fibonacci.append(fibonacci_calculated)
    fibonacci_calculated = 0
    n_loop -= 1

print(fibonacci)

print(f"The 100th number in the fibonacci sequence is {fibonacci[len(fibonacci)-1]}")

