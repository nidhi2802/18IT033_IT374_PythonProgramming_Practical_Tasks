from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))
    @staticmethod
    def isAdult(name,age): 
        if age > 18:
            print(name,"is adult")
        else:
            print(name,"is not adult")    

person1 = Person.fromBirthYear('Nishi',  2000)
person1.display()
Person.isAdult('Mishti',17)