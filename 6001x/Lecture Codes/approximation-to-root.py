#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 15:59:08 2022

@author: thaibinhbr97
"""

def findRoot(x, power, epsilon):
    """Assumes x and epsilon int or float, power an int,
    epsilon > 0 & power >= 1
    Returns float y such that y**power is within epsilon of x.
    If such a float does not exist, it returns None
    
    findRoot takes x, power, epsilon and returns y such that y**power <= x if
    exists and returns None otherwise.
    findRoot: Int/Float Int Int/Float -> Float
    requires: epsilon > 0 & power >= 1
    """
    #Negative number has no even-powered roots
    if x < 0 and power%2 == 0:
        return None
    
    low = min(-1.0, x)
    high = max(1.0, x)
    ans = (high+low)/2.0
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high+low)/2.0
    return ans
            

def testFindRoot():
    epsilon = 0.0001
    for x in [0.25, -0.25, 2, -2, 8, -8]:
        for power in range(1, 4):
            print('Testing x =', str(x), 'and power = ', power)
            result = findRoot(x, power, epsilon)
            if result == None:
                print('   No root')
                print('--------------------------------')
            else:
                print('   ', result**power, '~=', x)
                print('--------------------------------')
testFindRoot()