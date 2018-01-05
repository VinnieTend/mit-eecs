#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 21:29:24 2018
@author: angelichorsey

Finger Exercise

Write a program that examines three variables - x, y, and z - and prints the
largest odd number among them. If none of them are odd, it should print a
message to that effect.
"""

# Read input values and split into a list
values = input("Enter three integers seperated by commas (e.g., \"1,2,3\"): ")
values = values.split(",")

# Cast values as int and catch any ValueError exceptions
# (not sure if using a loop would be more pythonic though)
try:
    values = list(map(int, values))
except(ValueError):
    print("Values must be integers!")

# Set x, y, and z
x, y, z = values

if x > y and x > z and x % 2 == 1:
    print("x is the largest odd integer at", x)
elif y > z and y % 2 == 1:
    print("y is the largest odd integer at", y)
elif z % 2 == 1:
    print("z is the largest odd integer at", z)
else:
    print("No integers are odd; x,y,z =", values)
