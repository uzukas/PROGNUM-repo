#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

s = np.random.choice(["R", "P", "S"]) # generates random number from 1 to 3
user_input = input("Choose Rock, Paper or Scissors: ") # asks for user input
    
if user_input == "Rock": 
    if s == "R":
        print('Computer picked "Rock", you draw.')
    elif s == "P":
        print('Computer picked "Paper", you lose...')
    elif s == "S":
        print('Computer picked "Scissors", you win!')
               
if user_input == "Paper":
    if s == "R":
        print('Computer picked "Rock", you win!.') 
    elif s == "P":
        print('Computer picked "Paper", you draw.')
    elif s == "S":
        print('Computer picked "Scissors", you lose...')
            
if user_input == "Scissors":
    if s == "R":
        print('Computer picked "Rock", you lose...')
    elif s == "P":
        print('Computer picked "Paper", you win!')
    elif s == "S":
        print('Computer picked "Scissors", draw.') # computes and prints result

