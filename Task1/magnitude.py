{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e19642c4-3b21-4abd-ac32-682031064ecd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Sirius data\n",
    "print(\"Input apparent magnitude: \")\n",
    "apparentMagnitude = input()\n",
    "print(\"Input absolute magnitude NOW!: \")\n",
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
