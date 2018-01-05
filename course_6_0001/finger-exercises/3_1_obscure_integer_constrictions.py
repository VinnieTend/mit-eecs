#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 22:37:35 2018
@author: angelichorsey

Finger Exercise

Write a program that asks the user to enter an integer and prints two
integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the
integer entered by the user. If no such pair of integers exists, it should
print a message to that effect.

I'm modifying this exercise to require 1 < pwr < 6 considering it is always
possible to have root be equal to the integer entered and pwr equal 1.
"""

value = int(input('Enter an integer: '))
outputs = ''
for pwr in range(2, 6):
    root = 0
    while root**pwr <= abs(value):
        if abs(root)**pwr == abs(value):
            if value < 0 and pwr % 2 == 1:
                root -= root*2
            outputs = "root = {:d} and pwr = {:d}\n".format(root, pwr)
            break             
        root += 1

if len(outputs) == 0:
    print('No valid values for root and pwr.')
else:
    print(outputs)
