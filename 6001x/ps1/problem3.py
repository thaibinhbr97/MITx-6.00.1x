#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 22:48:55 2022

@author: thaibinhbr97
"""

"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. 

For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc
"""

s = 'azcbobobegghakl'
sub_str = s[0]
temp = s[0]
for i in range(0,len(s)-1):
    if s[i] <= s[i+1]:
        temp += s[i+1]
    else:
        temp = s[i+1]
    if len(temp) > len(sub_str):
        sub_str = temp
print('Longest substring in alphabetical order is: ', sub_str)