#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 22:15:51 2018
@author: angelichorsey

Finger Exercise

Write a program that asks the user to input 10 integers, and then prints the
largest odd number that was entered. If no odd number was entered, it should
print a message to that effect
"""

print('Enter 10 integers.')
largest = int(input('First: '))
for i in range(9):
    new = int(input('Next: '))
    if new > largest and new % 2 == 1:
        largest = new

if largest % 2 == 1:
    print(largest)
else:
    print('No odd integers were entered.')
