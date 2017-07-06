#Write a function called unpack_and_reverse that will
#accept one parameter, a tuple with at least three items.
#The function should return a new tuple with only the first
#three items, but listed in reverse order.
#
#For example:
#
# a_tuple = ("a", "b", "c", "d", "e")
# unpack_and_reverse(a_tuple) -> ("c", "b", "a")
#
#However, to do this, you should not access any value in
#the tuple directly (e.g. with a_tuple[1]). Instead, you
#should use tuple unpacking to unpack them into variables.
#You also should not touch any items past the third item
#in the tuple: use tuple slicing instead to only access
#the first three.


#Write your function here!
def unpack_and_reverse(tuple):
    a, b, c = tuple[:3]
    return c, b, a


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#('c', 'b', 'a')
#('h', 'g', 'f')
#('k', 'j', 'i')
print(unpack_and_reverse(("a", "b", "c", "d", "e")))
print(unpack_and_reverse(("f", "g", "h")))
print(unpack_and_reverse(("i", "j", "k", "l", "m", "n", "o", "p", "q", "r")))
