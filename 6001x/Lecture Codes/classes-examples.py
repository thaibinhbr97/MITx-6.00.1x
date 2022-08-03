#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 23:38:01 2022

@author: thaibinhbr97
"""

# # Fraction class example
# class fraction(object):
#     def __init__(self, numer, denom):
#         self.numer = numer
#         self.denom = denom
#     def __str__(self):
#         return str(self.numer) + ' / ' + str(self.denom)
#     def getNumer(self):
#         return self.numer
#     def getDenom(self):
#         return self.denom
#     def __add__(self, other):
#         numer_new = self.getNumer() * other.getDenom() + other.getNumer() * \
#             self.getDenom()
#         denom_new = self.getDenom() * other.getDenom()
#         return fraction(numer_new, denom_new)
#     def __sub__(self, other):
#         numer_new = self.getNumer() * other.getDenom() - other.getNumer() * \
#             self.getDenom()
#         denom_new = self.getDenom() * other.getDenom()
#         return fraction(numer_new, denom_new)
#     def convert(self):
#         return self.getNumer() / self.getDenom()
    
    
# one_half = fraction(1,2)
# print(one_half)

# two_thirds = fraction(2,3)
# print(two_thirds)

# print(one_half.getNumer())
# # Equivalent to
# print(fraction.getNumer(one_half))

# print(two_thirds.getDenom())
# # Equivalent to
# print(fraction.getDenom(two_thirds))

# try_add = one_half + two_thirds
# print(try_add)

# try_sub = one_half - two_thirds
# print(try_sub)

# print(try_add.convert())

class intSet(object):
    def __init__(self):
        self.vals = []
    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
    def member(self, e):
        return e in self.vals
    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def intersect(self, other):
        result = ''
        self.vals.sort()
        other.vals.sort()
        for e in self.vals:
            if other.member(e):
                result += str(e) + ','
        result = '{' + result[:-1] + '}'
        return result
            
    def __len__(self):
        temp_string = self.__str__()[1:-1]
        if temp_string == '':
            return 0
        result = temp_string.split(',')
        return len(result)
    
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result += str(e) + ','
        result = '{' + result[:-1] + '}'
        return result
        # return '{' + ','.join([str(e) for e in self.vals]) + '}'
    def __eq__(self, other):
        return self.__str__() == other.__str__()
    
    
    

a = intSet()
a.insert(3)
print(a)
print(a.member(3))
a.remove(3)     
print(a)   
a.insert(1) 
a.insert(2)
a.insert(3)
# print(a)

# Remove raise an exception when an element is not in the list
# a.remove(5)
a.insert(3)
print(a)

b = intSet()
b.insert(2)
b.insert(3)
b.insert(4)
print(b)

c = intSet()
c.insert(2)
c.insert(3)
print(c)

print(a == b)
print(a == c)

assert a.intersect(b) == c

d = intSet()
print(d)
assert a.intersect(d) == d

e = intSet()
e.insert(4)
print(e)
assert a.intersect(e) == d
assert b.intersect(e) == e

assert len(a) == 3
assert len(b) == 3
assert len(c) == 2
assert len(d) == 0
assert len(e) == 1



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        