#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 23:04:20 2022

@author: thaibinhbr97
"""

# Problem 6
# 15/15 points (graded)
# Implement a function that meets the specifications below.

# def deep_reverse(L):
#     """ assumes L is a list of lists whose elements are ints
#     Mutates L such that it reverses its elements and also 
#     reverses the order of the int elements in every element of L. 
#     It does not return anything.
#     """
#     # Your code here
# For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]



# Paste your function here

    
def deep_reverse(L):
    for subList in L:
        subList.reverse()
    L.reverse()
        

L = [[1, 2], [3, 4], [5, 6, 7]]
deep_reverse(L)
assert L == [[7, 6, 5], [4, 3], [2, 1]]