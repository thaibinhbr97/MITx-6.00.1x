#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 15:18:34 2022

@author: thaibinhbr97

Write a function isIn that accepts two strings as arguments and
returns True if either string occurs anywhere in the other, and False otherwise.
Hint: you might want to use the built-in str operation in.
"""

def isIn(s1,s2):
    if s1 in s2 or s2 in s1:
        return True
    else:
        return False
    
print(isIn('hello','hell')) # True
print(isIn('hello','hello')) # True
print(isIn('hello','helloo')) # True
print(isIn('hello','hell0')) # False
print(isIn('hello','h')) # True

