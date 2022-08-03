#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 21:39:09 2022

@author: thaibinhbr97
"""

def search3(L, e):
    # Test if the list is empty - if it is, e cannot be in it!
    # Run this test first - so that we don't throw an error trying
    #  to access L[0].
    print("List L: " + str(L))
    if L == []:
        return False
    
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)
    
print(search3([], 4))
print(search3([1, 2, 3], 4))
print(search3([1, 2, 3], 3))

print()

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


print(search([], 4))
print(search([1, 2, 3], 4))
print(search([1, 2, 3], 3))