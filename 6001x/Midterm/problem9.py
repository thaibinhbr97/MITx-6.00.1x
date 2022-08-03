#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 23:05:58 2022

@author: thaibinhbr97
"""

# Problem 9
# 15/15 points (graded)
# Write a function to flatten a list. The list contains other lists, strings, 
# or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).

# def flatten(aList):
#    ''' 
#    aList: a list 
#    Returns a copy of aList, which is a flattened version of aList 
#    '''

# Paste your function here
def flatten_helper(L):
    for e in L:
        if type(e) == list:
            return flatten_helper(e)
        else:
            return e

def flatten(aList):
    result = []
    for i in L:
        if type(i) == list:
            for j in i:
                if type(j) == list:
                    result.append(flatten_helper(j))
                else:
                    result.append(j)
        else:
            result.append(i)
    return result

# def flatten1(aList):
#     newList = []
#     for item in aList:
#         if type(item) != list:
#             newList.append(item)
#         else:
#             newList.extend(flatten(item))
#     return newList
    
       
            
       
L = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]     
L1 = [[[3]]]
assert flatten_helper(L1) == 3
assert flatten(L) == [1,'a','cat',2,3,'dog',4,5]
