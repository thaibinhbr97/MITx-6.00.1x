#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 11:10:22 2022

@author: thaibinhbr97
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    # Base case: if middle character of the string equals to the test character, return True
    # Recursive case: if test char < middle character of the string, consider lower half
    #                 else consider upper half
    low = 0
    high = len(aStr)
    mid = (low + high)/2
    if aStr == '':
        return False
    elif len(aStr) == 1:
        return aStr == char
    elif aStr[int(mid)] == char:
        return True
    else:
        if char < aStr[int(mid)]:
            high = int(mid)
        else:
            low = int(mid)
        mid = (low+high)/2
        return isIn(char, aStr[low:high])