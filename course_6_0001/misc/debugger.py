#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 00:31:56 2018

@author: angelichorsey
"""


def demo(x):
    for i in range(5):
        print("i={}, x={}".format(i, x))
        x = x + 1


demo(0)
