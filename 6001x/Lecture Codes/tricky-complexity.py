#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 10:21:34 2022

@author: thaibinhbr97
"""

def h(n):
    """
    Assume n an int >= 0
    This function adds up digits of a number together. It converts to string.
    It iterates over a length of string, not magnitude of input n, so it is like
    dividing n by 10 each iteration.
    O(log(n))
    """
    answer = 0
    s = str(n)
    for c in s:
        answer += int(c)
    return answer

