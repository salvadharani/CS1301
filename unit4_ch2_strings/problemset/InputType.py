#Recall that input from a user is always in the form of a string.
#Write a function called "input_type" that gets user input and
#determines what kind of string the user entered. The user input
#will be supplied as an argument to the function like normal.
#
#  - Your function should return "integer" if the string only
#    contains characters 0-9.
#  - Your function should return "float" if the string only
#    contains the numbers 0-9 and at most one period.
#  - You should return "boolean" if the user enters "True" or
#    "False".
#  - Otherwise, you should return "string".


#Write your function here!

def input_type(user_input):
    if "." in user_input and user_input.replace(".", "").isdigit():
        return "float"
    elif user_input.isdigit():
        return "integer"
    elif user_input in ["True", "False"]:
        return "boolean"
    else:
        return "string"



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#string
#boolean
#float
#integer
print(input_type(""))
print(input_type("False"))
print(input_type("7.432621"))
print(input_type("2788"))


# Solution
def input_type_s(user_input):
    if user_input == "True" or user_input == "False":
        return "boolean"
    try:
        int(user_input)
        return "integer"
    except:
        try:
            float(user_input)
            return "float"
        except:
            return "string"