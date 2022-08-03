#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 22:47:47 2022

@author: thaibinhbr97
"""

"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 

For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
"""
# Paste your code into this box 

s = 'azcbobobegghakl'
sub_string = 'bob'
count = 0
for i in range(len(s)):
    if s[i:i+len(sub_string)] == sub_string:
        count += 1
print(count)