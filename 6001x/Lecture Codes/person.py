#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 23:49:36 2022

@author: thaibinhbr97
"""
import datetime

class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]    
    def getLastName(self):
        """"retun self's last name"""
        return self.lastName
    def __str__(self):
        """return self's name"""
        return self.name
    def setBirthday(self, month, day, year):
        """set self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)
    def getAge(self):
        """return self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return(datetime.date.today() - self.birthday).days
    def __lt__(self, other):
        """
        return True if self's name in lexicographically less than other's name
        , and False otherwise
        """
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    
    
class MITPerson(Person):
    nextIdNum = 0
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    def getIdNum(self):
        return self.idNum
    
    #sorting MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.getIdNum() < other.getIdNum()
    def speak(self, utterance):
        return self.name + " says:" + utterance
    
class Student(MITPerson):
    pass
    
class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year
    def speak(self, utterance):
        return MITPerson.speak(self, " Yo Bro, " + utterance)
        
class Grad(Student):
    pass

class TransferStudent(Student):
    pass

def isStudent(obj):
    return isinstance(obj, Student)

class Professor(MITPerson):
    def __init__(self, person, department):
        MITPerson.__init__(self, person)
        self.department = department
    def speak(self, utterance):
        newUtterance = " In course " + self.department + " we say " + utterance
        return MITPerson.speak(self, newUtterance)
    def lecture(self, topic):
        return self.speak("it is obvious that " + topic)


p1 = Person('Mark Zuckerberg')
p1.setBirthday(5,14,84)
p2 = Person('Drew Houston')
p2.setBirthday(3,4,83)
p3 = Person('Bill Gates')
p3.setBirthday(10,28,55)
p4 = Person('Travis Kalanik')
p5 = Person('Steve Wozniak')


personList = [p1, p2, p3, p4, p5]

for e in personList:
    print(e)
    
personList.sort()

print()

for e in personList:
    print(e)
    
    
# example usage

m3 = MITPerson('Mark Zuckerberg')
Person.setBirthday(m3,5,14,84)
m2 = MITPerson('Drew Houston')
Person.setBirthday(m2,3,4,83)
m1 = MITPerson('Bill Gates')
Person.setBirthday(m1,10,28,55)



MITPersonList = [m1, m2, m3]

print()

for e in MITPersonList:
    print(e)
    
MITPersonList.sort()

print()

for e in MITPersonList:
    print(e)
    
p1 =  MITPerson('Eric')
p2 = MITPerson('John')
p3 = MITPerson('John')
p4 = Person('John')

# p1<p2
#p1<p4

#p4<p1


s1 = UG('Matt Damon', 2017)
s2 = UG('Ben Affleck', 2017)
s3 = UG('Arash Ferdowsi', 2018)
s4 = Grad('Drew Houston')
s5 = UG('Mark Zuckerberg', 2019)
s6 = TransferStudent('Brad')


print(s1.speak("where is the quiz?"))
print(s2.speak("i have no idea"))
print(isStudent(s1))
print(isStudent(s4))
print(isStudent(s6))

faculty = Professor("Stranger Prof", "Finance")
print(faculty.speak("hi there"))
print(faculty.lecture("money is a currency exchange"))
