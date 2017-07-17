#Write a function called linear() that takes two parameters
#- a list of strings and a string. Write this function so
#that it returns the first index at which the string is
#found within the list if the string is found, or False if
#it is not found. You do not need to worry about searching
#for the search string inside the individual strings within
#the list: for example, linear(["bobby", "fred"], "bob")
#should return False, but linear(["bob", "fred"], "bob")
#should return 0.
#
#Use a linear search algorithm (not as scary as it sounds).
#Do not use the list method index -- in this exercise,
#you're actually implementing the way the index method
#works!


#Write your code here!

def linear(list_of_strings, astring):
    if astring not in list_of_strings:
        return False
    else:
        i = 0
        while i <= len(list_of_strings) - 1:
            if list_of_strings[i] == astring:
                return i
            else:
                i += 1


#Feel free to add code below to test your function.


print(linear(["bobby", "fred"], "bob"))
print(linear(["bob", "fred"], "bob"))
