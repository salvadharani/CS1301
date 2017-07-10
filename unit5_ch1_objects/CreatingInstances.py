#Define the class Name
class Name:
    def __init__(self):
        self.firstname = "[no first name]"
        self.lastname = "[no last name]"

#Define the class Person
class Person:
    def __init__(self):
        self.name = Name()
        self.eyecolor = "[no eye color]"
        self.age = -1

#Create a new Person and assign it to myPerson
myPerson = Person()
#Print myPerson's name's firstname
print(myPerson.name.firstname)
#Change myPerson's name's firstname to David
myPerson.name.firstname = "David"
#Print myPerson's name's firstname
print(myPerson.name.firstname)

# ------------------------------------------------
#Define the class Person
class Person:
    #Create a new instance of Person
    def __init__(self):
        #Person's default values
        self.firstname = "[no first name]"
        self.lastname = "[no last name]"
        self.eyecolor = "[no eye color]"
        self.age = -1

#Create two new Persons and assign them to
#myPerson1 and myPerson2
myPerson1 = Person()
myPerson2 = Person()
myPerson1.firstname = "David"
myPerson2.firstname = "Vrushali"

print("myPerson1: " + myPerson1.firstname)
print("myPerson2: " + myPerson2.firstname)


