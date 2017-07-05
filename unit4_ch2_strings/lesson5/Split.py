myString = "This is my text. It has thirteen words. It also has three sentences."
# splits based on separation of strings
print(myString.split())
# split based on period
print(myString.split("."))
# split based on period and avoids printing a space at the end
print(myString.split(". "))

# inputs comma-separated values
names = input("Enter a list of names: ")
# splits names based on comma
print(names.split(","))
