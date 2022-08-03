#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 15:00:50 2022

@author: thaibinhbr97
"""

"""
Newton-Raphson for square root
Find x such that x**2 - 24 is within epsilon of 0.01
"""
epsilon = 0.01
k = 30.0
guess = k/2.0
numGuesses = 0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (guess*guess - k)/(2*guess)
    numGuesses += 1
print('Square root of',k, 'is about',guess,'after', numGuesses,'guesses')

