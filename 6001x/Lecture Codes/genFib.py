#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 23:50:52 2022

@author: thaibinhbr97
"""

def genTest():
    yield 1
    yield 2
for n in genTest():
    print(n)
    
def genFib():
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next
        


# for n in genFib():
#     print(n)
    