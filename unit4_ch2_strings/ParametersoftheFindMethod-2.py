myString = "ABCDEABCDEABCDEFGHIJFGHIJABCDEABCDEFGHIJ"
findString = "CDE"
#Find findString in myString and assign its index to currentLocation
currentLocation = myString.find(findString)

#While currentLocation is positive; e.g. while findString is found
while currentLocation >= 0:
    #Print the index
    print(findString, "found at", currentLocation)
    #Get the next index, or -1 if there are no more
    currentLocation = myString.find(findString, currentLocation + 1)
