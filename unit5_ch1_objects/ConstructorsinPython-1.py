#Define the class Person
class Person:
    #Create a new instance of Person
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.eyecolor = "[no eye color]"
        self.age = -1

#Creates a person with names David and Joyner
myPerson = Person("David", "Joyner")
print(myPerson.firstname)
print(myPerson.lastname)


