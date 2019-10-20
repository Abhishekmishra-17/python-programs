# Python program to demonstrate the use of class method and static method. 
from datetime import date 
  
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
    @classmethod
    def fromBirthYear(cls, name, year): 
        return cls(name, date.today().year - year) 
    @staticmethod
    def isAdult(age): 
        return age > 18
  
person1 = Person('MKA', 18) 
person2 = Person.fromBirthYear('IHBA',2001) 
  
print(person1.age)
print(person2.age)
print(Person.isAdult(22)) 
