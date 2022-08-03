#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 22:59:30 2022

@author: thaibinhbr97
"""

# Problem 4
# 10/10 points (graded)
# Implement a function called closest_power that meets the specifications below.

# def closest_power(base, num):
#     '''
#     base: base of the exponential, integer > 1
#     num: number you want to be closest to, integer > 0
#     Find the integer exponent such that base**exponent is closest to num.
#     Note that the base**exponent may be either greater or smaller than num.
#     In case of a tie, return the smaller value.
#     Returns the exponent.
#     '''
#     # Your code here

#For example,
# closest_power(3,12) returns 2
# closest_power(4,12) returns 2
# closest_power(4,1) returns 0

 

# Paste your function here
def closest_power(base, num):
    power = 0
    left = 0
    right = 0
    while base**power != num:
        if base**power > num:
            right = base**power
            left = base**(power-1)
            if abs(right-num) >= abs(left-num):
                return power-1
            else:
                return power
        power += 1
    return power


assert closest_power(3,12) == 2
assert closest_power(4,12) == 2
assert closest_power(4,1) == 0
assert closest_power(4,2) == 0
assert closest_power(4,3) == 1
assert closest_power(10,100) == 2
