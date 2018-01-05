#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 23:50:40 2018
@author: angelichorsey

Finger Exercise

Let s be a string that contains a sequence of decimal numbers separated by
commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints the sum of
the numbers in s.
"""

value = input('Enter a list of decimal numbers delimeted by commas: ')
total = 0
for num in value.split(','):
    total += float(num)

print(total)
