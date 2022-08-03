#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 23:11:27 2022

@author: thaibinhbr97
"""

# Problem 6-2
# 10.0/10.0 points (graded)

# Consider the following hierarchy of classes:

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)


# You change your mind, and now want the behavior as described in Part 1, except that you want:

# >>> ae.say('the sky is blue')
# eric says: It is obvious that I believe that eric says: the sky is blue

# >>> ae.lecture('the sky is blue')
# It is obvious that I believe that eric says: the sky is blue

# Change the definition of ArrogantProfessor so that the behavior described above is achieved.

# Paste ONLY your ArrogantProfessor class in the box below. Do not leave any debugging print statements.

# For this question, you will not be able to see the test cases we run. This problem will test your ability to come up with your own test
# cases.


# Paste your class here
class ArrogantProfessor(Person):
    def say(self, stuff):
        return self.name + ' says: ' + 'It is obvious that I believe that ' + \
            self.name + ' says: ' + stuff
    def lecture(self, stuff):
        return 'It is obvious that I believe that ' + self.name + ' says: ' + \
            stuff