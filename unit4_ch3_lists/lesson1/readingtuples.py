myString = "Hello, world!"
myFloat = 5.1
myInteger = 5

#Creates myTuple as a tuple with the values
#of myString, myFloat, myInteger
myTuple = (myString, myFloat, myInteger)

#Prints the first element of myTuple
print(myTuple[0])
#Prints the second element of myTuple
print(myTuple[1])
#Prints the third element of myTuple
print(myTuple[2])

myString = "Hello, world!"
myFloat = 5.1
myInt1 = 5
myCharacter = "Q"
myInt2 = -1

myTuple = (myString, myFloat, myInt1, myCharacter,
           myInt2)

#Prints myTuple's values from #4 to the end
print(myTuple[3:])
#Prints the first two values of myTuple
print(myTuple[:2])
#Prints the second and third values of myTuple
print(myTuple[1:3])
#Prints the last three values of myTuple
print(myTuple[-3:])
#Prints all but the last three values of myTuple
print(myTuple[:-3])


myString = "Hello, world!"
myFloat = 5.1
myInt1 = 5
myCharacter = "Q"
myInt2 = -1

#Packs these five variables into myTuple
myTuple = (myString, myFloat, myInt1, myCharacter, myInt2)

#Unpacks myTuple into these variables
(myNewString, myNewFloat, myNewInt1, myNewCharacter,  myNewInt2) = myTuple

print(myNewString)
print(myNewFloat)
print(myNewInt1)
print(myNewCharacter)
print(myNewInt2)


