#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 18:26:21 2022

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

class Grades(object):
    """
    A mapping from students to list of grades
    """
    def __init__(self):
        """
        Create empty grade books
        """
        self.students = [] # list of Student objects
        self.grades = {} # maps idNum -> list of grades
        self.isSorted = True # true if self.students is sorted
    def addStudent(self, student):
        """
        Assume: student is of type Student
        Add student to the grade book
        """
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
    def addGrade(self, student, grade):
        """
        Assume: grade is a float
        Add grade to the list of grades for student
        """
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')
    def getGrades(self, student):
        """
        Return a list of grades for student
        """
        try:
            # return a copy of student's grade
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')
    def allStudents(self):
        """
        Return a list of students in the grade book
        """
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        # return a copy of lists of students
        return self.students[:]
def gradeReport(course):
    """
    Assume: course is of type Grades
    """
    report = []
    for s in course.allStudents():
        total = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            total += g
            numGrades += 1
        try:
            average = total/numGrades
            report.append(str(s) + '\'s mean grade is ' + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)


ug1 = UG('Matt Damon', 2018)
ug2 = UG('Ben Affleck', 2019)
ug3 = UG('Drew Houston', 2017)
ug4 = UG('Mark Zuckerberg', 2017)
g1 = Grad('Bill Gates')
g2 = Grad('Steve Wozniak')

six00 = Grades()
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)
six00.addStudent(ug4)
six00.addStudent(ug3)


six00.addGrade(g1, 100)
six00.addGrade(g2, 25)
six00.addGrade(ug1, 95)
six00.addGrade(ug2, 85)
six00.addGrade(ug3, 75)

print()

print(gradeReport(six00))

six00.addGrade(g1, 90)
six00.addGrade(g2, 45)
six00.addGrade(ug1, 80)
six00.addGrade(ug2, 75)

print()

print(gradeReport(six00))

print()
for s in six00.allStudents():
    print(s)
