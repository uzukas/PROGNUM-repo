#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Y = int(input("Type in a year starting from 1582"))
M = int(input("Type in a month from 1 to 12"))
D = int(input("Type in a day from 1 to 28-31, depending on the month"))

JD = 367*Y - 7*(Y+(M+9)//12)//4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5

print(f"The date {Y}-{M}-{D} in the Julian date is {JD}")

