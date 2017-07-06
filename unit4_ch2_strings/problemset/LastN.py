#Write a function called "last_n" that accepts two arguments:
#a string search_string and an integer n. The function should
#return the last n characters from search_string. If
#search_string is shorter than n characters, then it should
#return the entire value of search_string.


#Write your function here!
def last_n(search_string, n):
    try:
        return search_string[-n:]
    except IndexError:
        return search_string


#The code below will test your function. If your function
#works correctly, this should print 789, saur, and 1.
print(last_n("123456789", 3))
print(last_n("Bulbasaur", 4))
print(last_n("1", 5))

# Solution:

#There are a lot of complicated approaches we could take
#here, but the simplest is just a string slicing operation.
#If we want to start n characters from the end, then we grab
#a slice that starts at -n and goes until the end.

def last_n2(search_string, n):
    return search_string[-n:]

#We also don't need any special reasoning to handle instances
#where search_string is shorter than n characters; by
#default, Python just grabs the entire string if that is the
#case.


print(last_n2("123456789", 3))
print(last_n2("Bulbasaur", 4))
print(last_n2("1", 5))
