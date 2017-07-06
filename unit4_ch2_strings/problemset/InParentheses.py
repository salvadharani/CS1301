#Write a function called "in_parentheses" that accepts a
#single argument, a string representing a sentence that
#contains some words in parentheses. Your function should
#return the contents of the parentheses.
#
#For example:
#
# in_parentheses("This is a sentence (words!)") -> "words!"
#
#If no text appears in parentheses, return an empty string.
#Note that there are several edge cases introduced by this:
#all of the following function calls would return an empty
#string:
#
# in_parentheses("No parentheses")
# in_parentheses("Open ( only")
# in_parentheses("Closed ) only")
# in_parentheses("Closed ) before ( open")
#
#You may assume, however, that there will not be multiple
#open or closed parentheses.


#Write your function here!
def in_parentheses(string):
    if "(" in string and ")" in string:
        openp = string.find("(")
        closep = string.find(")")
        if openp < closep:
            return string[openp+1:closep]
    return ""


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (including the blank lines):
#words!
#
#as he is doing right now
#
#
#!

print(in_parentheses("This is a sentence (words!)."))
print(in_parentheses("No parentheses here!"))
print(in_parentheses("David tends to use parentheses a lot (as he is doing right now). It tends to be quite annoying."))
print(in_parentheses("Open ( only"))
print(in_parentheses("Closed ) only"))
print(in_parentheses("Closed ) before ( open"))
print(in_parentheses("That's a lot of test cases(!)"))


# solution
def in_parentheses2(sentence):
    # First we check if both parentheses are present:

    if "(" in sentence and ")" in sentence:

        # Then we check if they're in the right order:

        if sentence.find("(") < sentence.find(")"):
            # If we get here, then it's a valid set,
            # and we can return the substring from
            # the index of ( to the index of ):

            return sentence[sentence.find("("): sentence.find(")")]

    # The only way to get to this next line is if the return
    # on line 25 did not run, so we can return a blank
    # string here:

    return ""

print("Solution")
print(in_parentheses2("This is a sentence (words!)."))
print(in_parentheses2("No parentheses here!"))
print(in_parentheses2("David tends to use parentheses a lot (as he is doing right now). It tends to be quite annoying."))
print(in_parentheses2("Open ( only"))
print(in_parentheses2("Closed ) only"))
print(in_parentheses2("Closed ) before ( open"))
print(in_parentheses2("That's a lot of test cases(!)"))

# Solution 2:
def in_parentheses3(sentence):
    try:
        return sentence[sentence.index("(") + 1:sentence.index(")")]
    except ValueError:
        return ""