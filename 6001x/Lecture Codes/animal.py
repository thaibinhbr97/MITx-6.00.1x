#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 17:57:27 2022

@author: thaibinhbr97
"""
import random

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, new_age):
        self.age = new_age
    def set_name(self, new_name=""):
        self.name = new_name
    def __str__(self):
        return "Animal:" + str(self.get_name()) + ":" +str(self.get_age())
    
class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "Cat:" + str(self.get_name()) + ":" +str(self.get_age())
    
class Rabbit(Animal):
    def speak(self):
        print("meep")
    def __str__(self):
        return "Rabbit:" + str(self.get_name()) + ":" +str(self.get_age())

# This Rabbit class uses class variables for example
class idRabbit(Rabbit):
    tag = 1 # class variable
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1 # instance variable
        self.parent2 = parent2 # instance variable
        self.rid = idRabbit.tag # instance variable
        idRabbit.tag += 1    
    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        return idRabbit(0, self, other)
    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid and \
            self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent1.rid == other.parent2.rid and \
            self.parent2.rid == other.parent1.rid
        return parents_same or parents_opposite
    

    
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self, other):
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than",  other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)
    def __str__(self):
        return "Person:" + str(self.get_name()) + ":" +str(self.get_age())        
    
class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, new_major):
        self.major = new_major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("I have homework")
        elif 0.25 <= r < 0.5:
            print("I need to sleep")
        elif 0.5 <= r < 0.75:
            print("I should eat")
        else:
            print("I am playing video games")
    def __str__(self):
        return "Student:" + str(self.get_name()) + ":" + str(self.get_age()) \
            + ":" + str(self.major)
    
    

animal1 = Animal(3)
animal1.set_name("Tony")
print(animal1)

cat1 = Cat(2)
cat1.set_name("Pussy")
cat1.speak()
print(cat1)
print(Cat.__str__(cat1))
print(Animal.__str__(cat1))



brad = Person("Brad", 24)
mai = Person("Mai", 19)
brad.speak()
brad.add_friend("Mai")
mai.add_friend("Brad")
print(brad.get_friends())
print(mai.get_friends())
brad.age_diff(mai)
Person.age_diff(mai, brad)
print(mai)

david = idRabbit(3)
david.set_name("David")
molly = idRabbit(2)
molly.set_name("Molly")
jack = idRabbit(1, david, molly)
jack.set_name("Jack")
print(jack)
print(jack.get_parent2())
lily = david + molly
lily.set_name("Lily")
print(lily)
print(lily.get_parent1())
print(lily.get_parent2())
print(lily == jack) # check if they have the same parents
