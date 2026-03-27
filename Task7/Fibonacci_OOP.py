#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Fibonacci:
    def __init__ (self, n, m):
        self.n = n
        self.m = m
        
    def get_nth(self):
        a, b = 0, 1 
        for i in range (self.n):
            old_a = a 
            a = b
            b = old_a + b
        return a

    def get_divisible(self):
        results = []
        a, b = 0, 1
        for i in range(self.n):
            if a % self.m == 0:
                results.append(a)
            old_a = a
            a = b 
            b = old_a + b
        return results

fib = Fibonacci(100,7)
nth_term = fib.get_nth()
divisible_terms = fib.get_divisible()

print(f"100th term: {nth_term}")
print(f"terms divisible by 7: {divisible_terms}")

