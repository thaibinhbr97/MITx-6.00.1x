#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 23:33:59 2022

@author: thaibinhbr97
"""

def genSubsets(L):
    if len(L) == 0:
        return [[]] # list of empty list
    smaller = genSubsets(L[:-1]) # all subsets without the last element
    extra = L[-1:] # create a list of just last element
    new = []
    for small in smaller:
        new.append(small + extra) # for all smaller solutions, add one with last element
    return smaller + new # combine those with last element and those without

L1 = [1,2,3]
print(genSubsets(L1))

# If not understand, try using PythonTutor for illustration.

    