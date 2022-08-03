#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 23:03:57 2022

@author: thaibinhbr97
"""

# Problem 5
# 10/10 points (graded)
# Write a Python function that returns the sum of the pairwise products of 
# listA and listB. You should assume that listA and listB have the same length 
# and are two lists of integer numbers. For example, if listA = [1, 2, 3] and 
# listB = [4, 5, 6], the dot product is 1*4 + 2*5 + 3*6, meaning your function 
# should return: 32

# Hint: You will need to traverse both lists in parallel.

# This function takes in two lists of numbers and returns a number.

# def dotProduct(listA, listB):
#     '''
#     listA: a list of numbers
#     listB: a list of numbers of the same length as listA
#     '''
#     # Your code here
    
 

# Paste your function here
def dotProduct(listA, listB):
    res = 0
    for i in range(len(listA)):
        res += listA[i] * listB[i]
    return res
        

# Tests
listA = [1,2,3]
listB = [4,5,6]
assert dotProduct(listA,listB) == 32

listC = [0,0,0]
listD = [0,0,0]
assert dotProduct(listC,listD) == 0

listE = [0,0,0]
listF = [10,0,10]
assert dotProduct(listC,listD) == 0
