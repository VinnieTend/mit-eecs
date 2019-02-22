#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 11:38:30 2019

@author: angelichorsey

Finger Exercise: Implement a function that meets the specification below. 
use a try-except block.
"""

def sumDigits(s):
    """
    Assumes s is a string
    Returns the sum of the decimal digits in s
    E.g., if s is 'a2b3c' it returns 5
    """
    sum = 0
    for char in s:
        try:
            sum += int(char)
        except ValueError:
            continue
    return sum