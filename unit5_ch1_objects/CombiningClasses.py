#Defines the class Person
class Person:
    def __init__(self, name, eyecolor, age):
        self.name = name
        self.eyecolor = eyecolor
        self.age = age

#Defines the class Name
class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

#Creates a person with eyecolor "brown", age 30, and
#a name with firstname "David", lastname "Joyner",
myPerson = Person(Name("David", "Joyner"), "brown", 30)
print(myPerson.name.firstname)
print(myPerson.name.lastname)
print(myPerson.eyecolor)
print(myPerson.age)


