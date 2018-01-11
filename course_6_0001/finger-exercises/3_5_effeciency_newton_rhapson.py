#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 17:21:23 2018
@author: angelichorsey

Finger Exercise

Add some code to the implementation of Newton-Raphson that keeps track of the
number of iterations used to find the root. Use that code as part of a program
that compares the efficiency of Newton-Raphson and bisection search.
(You should discover that Newton-Raphson is more effecient.)
"""

# Newton-Raphson for square root
# Find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.01
k = 
guess = k/2.0
steps = 0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (guess**2 - k)/(2*guess)
    steps += 1

epsilon = 0.01
num_guesses = 0
low = 0
high = k
guess = (high + low)/2.0
while abs(guess**2 - k) >= epsilon:
    if guess**2 < k:
        # look only in upper half search space
        low = guess
    else:
        # look only in lower half search space
        high = guess
    # next guess is halfway in search space
    guess = (high + low)/2.0
    num_guesses += 1

print('Bisection guesses:', num_guesses)
print(guess, 'is close to the cube root of', k)

print('Newton-Raphson guesses:', steps)
print('Square root of', k, 'is about', guess)

if num_guesses < guess:
    print('Bisection wins!')
else:
    print('Newton-Raphson wins!')
