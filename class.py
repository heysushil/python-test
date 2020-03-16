# class Person:
#   def __init__(self, fname, lname, year):
#     self.firstname = fname
#     self.lastname = lname
#     self.year = 2019

#   def printname(self):
#     print('hello {} - {}'.format(self.firstname, self.lastname))

# #Use the Person class to create an object, and then execute the printname method:

# # y = Person("John", "Doe")
# # y.printname()


# # child class
# class Student(Person):
#     def __init__(self, fname, lname):
#         self.year = 2019
#         super().__init__(self, fname, lname, year) #super class

#     def printvalue(self):
#         print('hello')
#         # print('Hello {}, and {} year {}'.format(self.firstname,self.lastname, self.year))

# x = Student("Mike", "Olsen")
# # x.printname()
# x.printvalue()

import numpy
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
# print(next(myit))
# print(next(myit))


speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = numpy.median(speed)

print(x)
