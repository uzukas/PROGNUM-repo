{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0af7c687-8cc6-4eca-bc90-46ff9a05e239",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "For f(x)=ax^2 + bx + c, a= 1\n",
      "For f(x)=ax^2 + bx + c, b= 6\n",
      "For f(x)=ax^2 + bx + c, c= 9\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You have a single root of x = -3.0\n"
     ]
    }
   ],
   "source": [
    "import math as m\n",
    "\n",
    "a = float(input(\"For f(x)=ax^2 + bx + c, a=\"))\n",
    "b = float(input(\"For f(x)=ax^2 + bx + c, b=\"))\n",
    "c = float(input(\"For f(x)=ax^2 + bx + c, c=\"))\n",
    "\n",
    "d = b**2 - 4*a*c\n",
    "\n",
    "x1 = 0\n",
    "x2 = 0\n",
    "\n",
    "if d > 0:\n",
    "    x1 = (-b + m.sqrt(d))/(2*a)\n",
    "    x2 = (-b - m.sqrt(d))/(2*a)\n",
    "    print(f\"There are two real roots x1 = {x1}, x2 = {x2}\")\n",
    "elif d == 0:\n",
    "    x1 = (-b)/(2*a)\n",
    "    print(f\"You have a single root of x = {x1}\")\n",
    "else:\n",
    "    print(\"No real answer\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
