{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "0eb22621-8c33-4d76-a82c-f3d3325930e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input apparent magnitude: \n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " -9999999999999999999999999999999999999999999\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input absolute magnitude: \n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your distance is 0.0pc!\n"
     ]
    }
   ],
   "source": [
    "# Sirius data\n",
    "print(\"Input apparent magnitude: \")\n",
    "apparentMagnitude = input()\n",
    "print(\"Input absolute magnitude: \")\n",
    "absoluteMagnitude = input()\n",
    "\n",
    "# The distance is related to the magnitudes as m-M=5.Log(d/10)\n",
    "# 1 Parsec = 3.26164 ly\n",
    "\n",
    "m = float(apparentMagnitude)\n",
    "M = float(absoluteMagnitude)\n",
    "\n",
    "d = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164\n",
    "\n",
    "print(f\"Your distance is {d}pc!\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Anaconda3-2020.07",
   "language": "python",
   "name": "anaconda3-2020.07"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
