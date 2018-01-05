#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 22:09:24 2018
@author: angelichorsey

Finger Exercise

Replace the comment in the following code with a while loop.

numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
#concatenate X to toPrint numXs times
print(toPrint)
"""

numXs = int(input('How many times should I print the letter X? '))
toPrint = ''

#####
while len(toPrint) < numXs:
    toPrint += 'X'
#####

print(toPrint)
