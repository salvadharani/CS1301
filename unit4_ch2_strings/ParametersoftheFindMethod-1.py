myString = "ABCDEABCDEABCDE"

# Prints the first index of "CDE' in myString --> 2
print(myString.find("CDE"))

# Prints the first index of "CDE" in myString after index 5 --> 7
print(myString.find("CDE", 5))

# Prints the frist index of 'CDE' in myString after 13 --> -1
print(myString.find("CDE", 13))

# Prints the first index of "CDE" in myString between 4 and 10 --> 7
print(myString.find("CDE", 4, 10))

# Prints the first index of "CDE" in myString between 3 and 6 --> -1
print(myString.find("CDE", 3, 6)


      