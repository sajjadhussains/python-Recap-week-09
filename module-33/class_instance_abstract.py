# instance method
# static method
# class method
# abstract method

# class School:
#     school_name="Kushtia Zilla School"#class variable
#     def __init__(self,name) -> None:
#         self.name=name
#     def printName(self):
#         print(self.name)#instance variable
#     def change_name(self,name):
#         self.school_name=name
#     @classmethod
#     def change_school_name(cls):
#         cls.school_name="habijabi school"
#     @staticmethod
#     def greet():
#         print('hello students')

# s1=School('sajjad')
# s2=School('shuvo')
# s1.change_name('habijabi school')
# School.change_school_name()
# print(s2.school_name)
# School.greet()

# abstract class/method
# in abstract class,you can't create object
from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print('i am driving car')
    def stop(self):
        print('please stop this car')
class Bike(Vehicle):
    def go(self):
        print('I am riding a bike')
    def stop(self):
        print('please stop bike')

car=Car()
car.go()
bike=Bike()
bike.go()
car.stop()
bike.stop()
