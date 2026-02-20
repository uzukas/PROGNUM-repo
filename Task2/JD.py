{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a199fd63-6db0-44ae-933f-3000735eba38",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Type in a year starting from 1582 1700\n",
      "Type in a month from 1 to 12 1\n",
      "Type in a day from 1 to 28-31, depending on the month 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The date 1700-1-4 in the Julian date is 2341975.5\n"
     ]
    }
   ],
   "source": [
    "Y = int(input(\"Type in a year starting from 1582\"))\n",
    "M = int(input(\"Type in a month from 1 to 12\"))\n",
    "D = int(input(\"Type in a day from 1 to 28-31, depending on the month\"))\n",
    "\n",
    "JD = 367*Y - 7*(Y+(M+9)//12)//4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5\n",
    "\n",
    "print(f\"The date {Y}-{M}-{D} in the Julian date is {JD}\")"
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
