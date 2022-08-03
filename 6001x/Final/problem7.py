#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 23:12:37 2022

@author: thaibinhbr97
"""

# Problem 7
# 20.0/20.0 points (graded)
# Write a function called general_poly, that meets the specifications below.

# For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because 
# 1 * 10^3 + 2 * 10^2 + 3 * 10^1 + 4 * 10^0

# So in the example the function only takes one argument with general_poly([1, 2, 3, 4]) 
# and it returns a function that you can apply to a
# value, in this case x = 10 with general_poly([1, 2, 3, 4])(10).

# Paste your code here
def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def apply(x):
        total = 0
        length = len(L)
        for i in range(length):
            total += L[i] * 10**(length-i-1)
        return total
    return apply


assert general_poly([1, 2, 3, 4])(10) == 1234