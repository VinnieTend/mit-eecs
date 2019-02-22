#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 11:45:52 2019

@author: angelichorsey

Finger excercise: Implement a function that satisfies the specification
"""

def findAnEven(L):
    """
    Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even number
    """
    
    for i in L:
        if i % 2 == 0:
            return i
    raise ValueError('L contains no even numbers.')
            