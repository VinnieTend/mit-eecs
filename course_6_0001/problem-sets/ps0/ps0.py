#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 23:41:05 2018
@author: angelichorsey

Problem Set 0

Write a program that does the following in order:
1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”.
4. Prints out the log (base 2) of “x”.
"""

import numpy

x = int(input('Enter a number for x: '))
y = int(input('Enter a number for y: '))

print('x raised to the power of y equals {:d}'.format(x**y))
print('log base 2 of x equals {:f}'.format(numpy.log2(x)))
