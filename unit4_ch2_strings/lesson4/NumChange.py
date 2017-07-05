#Write a function called "num_changer" that accepts a string
#of digits (0-9). You should make an integer from the digits
#of the even indices and another number from the digits in
#the odd indices. Return the sum of these two numbers. You
#can assume the given string will have a length of at least
#2 digits.
#
#For example, if the string was "123456", you would split
#this into two integers, 135 and 246. Adding them would give
#381. Or if the string was "13579", you would split this into
#159 and 37, then add them to get 196.
#
#Hint: You can do this with loops, but it's easier to do
#this with string slicing. Remember how we could pass a third
#argument to range() that would tell range how many numbers
#to skip? You can do something similar with string slices: if
#you include second colon in a string slice, the number
#that follows it lets you skip characters in the string. For
#example:
#
# "Hello, world!"[1:9] -> This gives "ello, wo".
# "Hello, world!"[1:9:2] -> This gives "el,w". Including :2
#    in the string slice skips every other letter.
# "Hello, world!" [::3] -> This gives "Hl r!". Leaving the
#    first two spots blank tells it to look at the entire
#    string, but putting :3 at the end says to only take
#    every third character (H, l, space, r, and !).
#
#Hint 2: Remember, Python is zero-indexed. That means the
#first number in the string is at position 0, and so it goes
#in the even list.


#Write your function here!
def num_changer(string):
    return int(string[0::2]) + int(string[1::2])


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 123456 -> 381
string_int = "123456"
result = num_changer(string_int)
print(string_int + " -> " + str(result))
