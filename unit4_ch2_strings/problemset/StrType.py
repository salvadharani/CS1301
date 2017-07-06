#Write a function called 'string_type' which accepts one
#string argument and determines what type of string it is.
#
# - If the string is empty, return "empty".
# - If the string is a single character, return "character".
# - If the string represents a single word, return "word".
#   The string is a single word if it has no spaces.
# - If the string is a whole sentence, return "sentence".
#   The string is a sentence if it contains spaces, but
#   at most one period.
# - If the string is a paragraph, return "paragraph". The
#   string is a paragraph if it contains both spaces and
#   multiple periods (we won't worry about other
#   punctuation marks).
# - If the string is multiple paragraphs, return "page".
#   The string is a paragraph if it contains any newline
#   characters ("\n").
#
#Hint: think carefully about what order you should check
#these conditions in.
#
#Hint 2: remember, there exists a count() method that
#counts the number of times a string appears in another
#string. For example, "blah blah blah".count("blah")
#would return 3.


#Write your function here!
def string_type(string):
    if len(string) == 0:
        return "empty"
    elif len(string) == 1 and string != " ":
        return "character"
    elif len(string) > 1 and len(string.split()) == 1:
        return "word"
    elif "\n" in string and string.count(". ") > 1:
        return "page"
    elif string.count(". ") > 1:
        return "paragraph"
    elif string.count(".") == 1 or string.count("!") == 1 or string.count("?") == 1:
        return "sentence"



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#empty
#character
#word
#sentence
#paragraph
#page
print(string_type(""))
print(string_type("!"))
print(string_type("CS1301."))
print(string_type("This is too many cases!"))
print(string_type("There's way too many ostriches. Why are there so many ostriches. The brochure said there'd only be a few ostriches."))
print(string_type("Paragraphs need to have multiple sentences. It's true.\nHowever, two is enough. Yes, two sentences can make a paragraph."))

# Solution
#This problem is made easier by testing the string types in
#generally descending order. It's easy, for instance, to
#check for a page because if "\n" is in the string, the
#string is a page no matter what else. Similarly, if there
#are more than one period and a space, then it's a paragraph
#no matter what. Then, if there's a space, then it's a
#sentence as long as neither of the earlier cases were True.
#
#Then, the "character" and "empty" conditions are easy to
#test (length is 1 or 0, respectively). If none of those
#conditions are true, then we have a string greater than
#length 2 with no spaces, so it must be a word!

def string_type_s(input_string):
    if "\n" in input_string:
        return "page"

    elif input_string.count(".") > 1 and " " in input_string:
        return "paragraph"

    elif " " in input_string:
        return "sentence"

    elif len(input_string) == 0:
        return "empty"

    elif len(input_string) == 1:
        return "character"

    else:
        return "word"