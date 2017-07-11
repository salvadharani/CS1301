class Person:
    def __init__(self, name, eyecolor, age):
        self.name = name
        self.eyecolor = eyecolor
        self.age = age

class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

myPerson1 = Person(Name("David", "Joyner"), "brown", 30)
myPerson2 = Person(myPerson1.name, myPerson1.eyecolor, myPerson1.age)
myPerson2.eyecolor = "blue"
print(myPerson1.eyecolor)  # ==> "brown"
print(myPerson2.eyecolor)  # ==> "blue"
myPerson2.name.firstname = "Vrushali"
print(myPerson1.name.firstname) # ==> Vrushali
print(myPerson2.name.firstname) # ==> Vrushali


class Person:
    def __init__(self, name, eyecolor, age):
        self.name = name
        self.eyecolor = eyecolor
        self.age = age

class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

myPerson1 = Person(Name("David", "Joyner"), "brown", 30)
myPerson2 = Person(Name(myPerson1.name.firstname, myPerson1.name.lastname),
                   myPerson1.eyecolor, myPerson1.age)
myPerson2.eyecolor = "blue"
print(myPerson1.eyecolor) # ==> "brown"
print(myPerson2.eyecolor) # ==> "blue"
myPerson2.name.firstname = "Vrushali"
print(myPerson1.name.firstname) # ==> David
print(myPerson2.name.firstname) # ==> Vrushali


