#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 23:11:48 2022

@author: thaibinhbr97
"""

# Problem 6-3
# 15.0/15.0 points (graded)

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

# You change your mind once more. You want to keep the behavior from Part 2, but now you would like:

# >>> pe.say('the sky is blue')
# Prof. eric says: I believe that eric says: the sky is blue 

# >>> ae.say('the sky is blue')
# Prof. eric says: It is obvious that I believe that eric says: the sky is blue 

# Change the Professor class definition in order to achieve this. You may have to modify your implmentation for a previous part to get
# this to work.

# Paste ONLY the Professor class in the box below. Do not leave any debugging print statements.

# For this question, you will not be able to see the test cases we run. This problem will test your ability to come up with your own test
# cases.


# Paste your class here
class Professor(Lecturer): 
    def say(self, stuff): 
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Person):
    def say(self, stuff):
        return 'Prof. ' + self.name + ' says: ' + 'It is obvious that I believe that ' + \
            self.name + ' says: ' + stuff
    def lecture(self, stuff):
        return 'It is obvious that I believe that ' + self.name + ' says: ' + \
            stuff