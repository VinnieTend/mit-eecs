#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 01:06:42 2018
@author: angelichorsey

Finger Exercise

What would the code in figure 3.4 do if the statement x = 25 were replaced by
x = -25?

Answer: It would loop infinitely.

What would have to be changed to make the code in Figure 3.4 work for finding
an approximation to the cube root of both negative and positive numbers?
(Hint: think about changing low to ensure that the answer lies within the
region being searched.)

Answer: Shown below, but I feel like I am not doing it correctly based on the
hint above not being used.
"""

x = -8
epsilon = 0.001
numGuesses = 0
low = 0.0
high = max(1.0, abs(x))
ans = (high + low)/2.0
while abs(ans**3 - abs(x)) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**3 < abs(x):
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
if x < 0:
    ans -= ans * 2
print('numGuesses =', numGuesses)
print(ans, 'is close to cube root of', x)
