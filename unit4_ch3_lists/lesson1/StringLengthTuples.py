#Write a function called string_length. string_length should
#have on parameter, a string. It should return a 2-tuple:
#the first item in the 2-tuple should be the string itself,
#and the second item should be the length of the string as
#given by the len() function.


#Write your function here!
def string_length(string):
    return (string, len(string))


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
print(string_length("Hello, world!"))
print(string_length("CS1301"))
print(string_length("Some people pronounce it 'toople'. Others pronounce it 'tuhple'. Either is correct."))



