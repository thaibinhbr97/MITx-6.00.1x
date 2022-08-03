#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 23:08:11 2022

@author: thaibinhbr97
"""

# Problem 4
# 20.0/20.0 points (graded)
# You are given the following definitions:
# A run of monotonically increasing numbers means that a number at position k+1 
# in the sequence is greater than or equal to the number at
# position k in the sequence.
# A run of monotonically decreasing numbers means that a number at position k+1 
# in the sequence is less than or equal to the number at
# position k in the sequence.
# Implement a function that meets the specifications below.

def index_match(L, subL):
    """
    Assume L is a list of integers, check whether the list L contains a sublist 
    subL
    Return the index where the list subL occurs in the list L if L contains subL
    and -1 if the list L does not contain the list subL
    """
    index = -1
    if subL == L:
        index = 0
    elif len(subL) > len(L):
        index = -1
    else:
        for i in range(len(L)):
            if L[i] == subL[0]:
                n = 1
                while (n < len(subL)) and L[i+n] == subL[n]:
                    n += 1
                if n == len(subL):
                    index = i
    return index
    

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    inc_L = [L[0]]
    inc_temp = [L[0]]
    dec_L = [L[0]]
    dec_temp = [L[0]]
    for i in range(1, len(L)):
        if L[i-1] >= L[i]:
            dec_temp.append(L[i])
        else:
            if len(dec_L) < len(dec_temp):
                dec_L = dec_temp[:]
            dec_temp = [L[i]]
    for j in range(1, len(L)):
        if L[j-1] <= L[j]:
            inc_temp.append(L[j])
        else:
            if len(inc_L) < len(inc_temp):
                inc_L = inc_temp[:]
            inc_temp = [L[j]]
    
    if len(inc_L) == len(dec_L):
        if index_match(inc_L, L) > index_match(dec_L, L):
            return sum(dec_L)
        elif index_match(inc_L, L) < index_match(dec_L, L):
            return sum(inc_L)
    elif len(inc_L) > len(dec_L):
        return sum(inc_L)
    else:
        return sum(dec_L)

# For example:
# If L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2] then the longest run of monotonically 
# increasing numbers in L is [3, 4, 5, 7, 7] and the longest
# run of monotonically decreasing numbers in L is [10, 4, 3]. Your function 
# should return the value 26 because the longest run of
# monotonically increasing integers is longer than the longest run of monotonically 
# decreasing numbers.
# If L = [5, 4, 10] then the longest run of monotonically increasing numbers in 
# L is [4, 10] and the longest run of monotonically
# decreasing numbers in L is [5, 4]. Your function should return the value 9 
# because the longest run of monotonically decreasing integers
# occurs before the longest run of monotonically increasing numbers.

# Test cases:
L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
L2 = [10, 4, 3]
L3 = [3, 4, 5, 7, 7]
L4 = L[:]
L5 = [3, 4, 10]
# print(index_match(L, L2))
# print(index_match(L, L3))
# print(index_match(L, L4))
# print(index_match(L, L5))

assert longest_run(L) == 26

L1 = [5, 4, 10]
assert longest_run(L1) == 9