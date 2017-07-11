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
myPerson2 = myPerson1
myPerson2.eyecolor = "blue"
print("myPerson1's eyecolor: " + myPerson1.eyecolor)
# would print "blue"
print("myPerson2's eyecolor: " + myPerson2.eyecolor)
# would print "blue"
