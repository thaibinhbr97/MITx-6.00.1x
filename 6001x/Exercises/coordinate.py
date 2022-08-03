#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 09:05:57 2022

@author: thaibinhbr97
"""

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    def __eq__(self, other):
        return self.getX() == other.getX() and self.getY() == other.getY()
    def __repr__(self):
        return 'Coordinate' + '(' + str(self.getX()) + ',' + str(self.getY()) \
            + ')'
    
a = Coordinate(3,4)
b = Coordinate(5,6)
c = Coordinate(3,4)
print(a)
print(a == b)
print(a == c)

print(repr(a))
# Same idea
print(a.__repr__())

print(eval(repr(a)))
# Same idea
print(eval(a.__repr__()))

print(eval(repr(a)) == a)
    