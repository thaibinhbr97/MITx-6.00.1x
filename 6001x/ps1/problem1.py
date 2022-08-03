#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 22:45:32 2022

@author: thaibinhbr97
"""

"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 

For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5
"""

# Paste your code into this box
s = 'azcbobobegghakl'
count = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count += 1
print(count)