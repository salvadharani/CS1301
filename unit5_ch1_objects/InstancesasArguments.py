class Person:
    def __init__(self, name, eyecolor, age):
        self.name = name
        self.eyecolor = eyecolor
        self.age = age

class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

def capitalizeName(name):
    name.firstname = name.firstname.upper()
    name.lastname = name.lastname.upper()

myPerson = Person(Name("David", "Joyner"), "brown", 30)
capitalizeName(myPerson.name)
print(myPerson.name.firstname) # => DAVID
print(myPerson.name.lastname) # => JOYNER



def capitalizeString(instring):
    instring = instring.upper()
    return instring

myPerson = Person(Name("David", "Joyner"), "brown", 30)
capitalizeString(myPerson.name.firstname)
capitalizeString(myPerson.name.lastname)
print(myPerson.name.firstname) # => David
print(myPerson.name.lastname) # => Joyner


print(capitalizeString("Alona"))

# Any operations we make on mutable objects, like name, propagate back out to the code
# that called that function. Any operations we make to immutable types, like just the plain string,
# do not propagate out to our main funciton or to our main code.