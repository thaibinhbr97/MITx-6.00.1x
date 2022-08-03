#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 18:48:16 2022

@author: thaibinhbr97
"""

# =============================================================================
# Consider the following sequence of expressions:
# 
# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
# 
# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')
# We want to write some simple procedures that work on dictionaries to return information.
# 
# This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.
# 
# Example usage:
# 
# >>> biggest(animals)
# 'd'
# If there are no values in the dictionary, biggest should return None.
# =============================================================================

# First way
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    dic = {}
    for key,value in aDict.items():
        dic[key] = len(value)
    best = max(dic.values())
    for key,value in dic.items():
        if value == best:
            return key
    return None


# Second way
def biggest1(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    dic = {}
    for key,value in aDict.items():
        dic[key] = len(value)
    best = max(dic.values())
    words = []
    for k in dic:
        if dic[k] == best:
            words.append(k)
    if len(words) == 0:
        return None
    else:
        return words[0]