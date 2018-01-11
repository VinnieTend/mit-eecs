#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 23:18:16 2018
@author: angelichorsey

Finger Exercise

When the implementation of fib in Figure 4.7 is used to compute fib(5), how
 many times does it compute the value of fib(2) of the way to computing fib(5)?

Answer: 3 times

In []:fib(5)
fib(2) occurred
fib(2) occurred
fib(2) occurred
Out[]: 8
"""


def fib(n):
    """Assumes n int >= 0
    Returns Fibonacci of n"""
    if n == 2:
        print('fib(2) occurred')
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def testFib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))


fib(5)
