#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 11:40:06 2022

@author: thaibinhbr97
"""

def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
    
def fib_efficient(n,d):
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1,d) + fib_efficient(n-2,d)
        d[n] = ans
        return ans
    

numFibCalls = 0
argToUse = 5
print("")
print(fib(argToUse))
print("Using fib",numFibCalls,"times")

numFibCalls = 0
d = {1:1, 2:2}
print("")
print(fib_efficient(argToUse, d))
print("Using fib_efficient",numFibCalls,"times")