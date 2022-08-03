#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 11:47:21 2022

@author: thaibinhbr97
"""

import math
def polysum(n,s):
    '''
    polysum takes n number of sides with each side s length and returns the sum
    of the area and square of the perimeter of the polygon. The sums is rounded
    to 4 decimal places
    polysum: Int Float -> Float
    '''
    area = (0.25*n*s**2)/math.tan(math.pi/n)
    perimeter = n*s
    return round(area + perimeter*2,4)