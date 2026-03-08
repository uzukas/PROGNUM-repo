#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import time

user_input = "Whatever"
win = 0
draw = 0
loss = 0

while user_input != "Exit":

    s = np.random.choice(["R", "P", "S"]) # generates random number from 1 to 3
    user_input = input("Choose Rock, Paper or Scissors: ") # asks for user input

    if user_input == "Scisors":
        while win < win + 100:
            win+=1
            time.sleep(0.1)
            print("You win!")
            print(f"Wins: {win}, Loses: {loss}, Draws: {draw}")
            print("----------------------------------------------")

    if user_input == "Rock": 
        if s == "R":
            print('Computer picked "Rock", you draw.')
            draw += 1
        elif s == "P":
            print('Computer picked "Paper", you lose...')
            loss += 1
        elif s == "S":
            print('Computer picked "Scissors", you win!')
            win += 1
                   
    if user_input == "Paper":
        if s == "R":
            print('Computer picked "Rock", you win!.')
            win += 1
        elif s == "P":
            print('Computer picked "Paper", you draw.')
            draw += 1
        elif s == "S":
            print('Computer picked "Scissors", you lose...')
            loss += 1
                
    if user_input == "Scissors":
        if s == "R":
            print('Computer picked "Rock", you lose...')
            loss += 1
        elif s == "P":
            print('Computer picked "Paper", you win!')
            win += 1
        elif s == "S":
            print('Computer picked "Scissors", draw.')
            draw += 1# computes and prints result
            
    print(f"Wins: {win}, Loses: {loss}, Draws: {draw}")
    print("----------------------------------------------")


# In[ ]:




