#Define the class Person
class Person:
    #Create a new instance of Person
    def __init__(self, firstname="[no first name]",
                 lastname="[no last name"):
        self.firstname = firstname
        self.lastname = lastname
        self.eyecolor = "[no eye color]"
        self.age = -1

myPerson1 = Person()
print(myPerson1.firstname)
myPerson2 = Person(firstname = "David")
print(myPerson2.firstname)
myPerson3 = Person("Vrushali")  # positional parameter (assumes the first parameter)
print(myPerson3.firstname)


# Here, the keyword parameter is used to override the positional parameter