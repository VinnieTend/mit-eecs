#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 22:19:18 2018
@author: angelichorsey

Finger Exercise

Write a function isIn that accepts two string as arguments and returns True if
 either string occurs anywhere in the other, and False otherwise.
Hint: you might want to use the built-in str operation in.
"""


def isIn(a, b):
    if a in b or b in a:
        return True
    else:
        return False


print(isIn('What am I doing?', 'What'))
