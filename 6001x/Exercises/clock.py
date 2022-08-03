#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 23:34:55 2022

@author: thaibinhbr97
"""

# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self):
#         time = '6:30'
#         print(self.time)

# clock = Clock('5:30')
# clock.print_time()


# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self, time):
#         print(time)

# clock = Clock('5:30')
# clock.print_time('10:30')

# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self):
#         print(self.time)

# boston_clock = Clock('5:30')
# paris_clock = boston_clock
# paris_clock.time = '10:30'
# boston_clock.print_time()


class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8

w2 = Wild(X, Y)
print(w2.getX())

print(w2.getY())

w3 = Wild(17, 18)
print(w3.getX())

print(w3.getY())
 
w4 = Wild(X, 18)
print(w4.getX())

print(w4.getY())

X = w4.getX() + w3.getX() + w2.getX()
print(X)

print(w4.getX())

Y = w4.getY() + w3.getY()
Y = Y + w2.getY()
print(Y)

print(w2.getY())