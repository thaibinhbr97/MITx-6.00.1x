#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 12:44:27 2022

@author: thaibinhbr97
"""

# =============================================================================
# Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...
# 
# Hints
# Ideas about the problem
# 
# Have the generator keep a list of the primes it's generated. A candidate number x is prime if (x % p) != 0 for all earlier primes p.
# =============================================================================

# My solution
def genPrimes():
    x = 2
    primes = []
    count = 0
    while True:
        for p in primes:
            if x % p == 0:
                count = 0 
                break
            else:
                count += 1
        if count == len(primes):
            primes.append(x)
            yield x
            count = 0
        x += 1
        
# Prof's solution
def genPrimes1():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
            
# Another version
def genPrimes2():
    primes = []
    prime = 2
    while True:
        for p in primes:
            if prime % p == 0:
                break
        else:
            primes.append(prime)
            yield prime
        prime += 1
        
# Another version using class
class genPrimes3():
    def __init__(self):
        self.prime = 2
        self.primes = []
    def __next__(self):
        while True:
            for p in self.primes:
                if self.prime % p == 0:
                    break
            else:
                self.primes.append(self.prime)
                return self.prime
            self.prime += 1
        
# Another version not considering even numbers
def genPrimes4():
    test = 1
    primes = [2]
    yield 2
    while True:
        test += 2
        for p in primes:
            if test % p == 0:
                break
        else: # else after a loop is not executed if there was a break
            primes.append(test)
            yield test

# Another version not considering even numbers
def genPrimes5():
    p = 3
    primes = [2, 3]
    yield 2
    yield 3
    while True:
        p += 2
        end = p ** 0.5
        for i in primes:
            if p % i == 0:
                break
            if i > end:
                primes.append(p)
                yield p
                break
            
def genPrimesFn():
    '''Function to print every 10th prime 
    number, until you've printed 20 of them.'''
    primes = []   # primes generated so far
    last = 1      # last number tried
    counter = 1
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            counter += 1
            if counter % 10 == 0:
                # Print every 10th prime
                print(last)
            if counter % (20*10) == 0:
                # Quit when we've printed the 10th prime 20 times (ie we've
                # printed the 200th prime)
                return
            
def genPrimesFn10000():
    '''Function to return 10000 prime numbers'''
    primes = []   # primes generated so far
    last = 1      # last number tried
    while len(primes) < 10000:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
    return primes

def genPrimesFnInteractive():
    '''Function to keep printing the prime number until the user stops the program.
    This way uses user input; you can also just run an infinite loop (while True)
    that the user can quit out of by hitting control-c'''
    primes = []   # primes generated so far
    last = 1      # last number tried
    user_input = 'y'    # Assume we want to at least print the first prime...
    while user_input != 'n':
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            print(last)
            user_input = input("Print the next prime? [y/n] ")
            while user_input != 'y' and user_input != 'n':
                print("Sorry, I did not understand your input. Please enter 'y' for yes, or 'n' for no.")
                user_input = input("Print the next prime? [y/n] ")
            
a = genPrimes()
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

print()

b = genPrimes4()
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())

print()

genPrimesFn()

# print(genPrimesFn10000())

# genPrimesFnInteractive()

def generator1():
    if True:
        yield 1 

def generator2():
    if False:   
        yield 1

g1 = generator1()
g2 = generator2()

print(type(g1))
print(type(g2))
# print(next(g1))
# print(next(g2))

def genOneMillion():
    maxNum = 1000000
    current = -1
    while current < maxNum:
        current += 1
        yield current

e = genOneMillion()
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))

