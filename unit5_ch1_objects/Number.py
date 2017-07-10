#Write a class named "Number" with one attribute called
#"value" which defaults to 0 and another attribute called
#"even" which defaults to True.
#
#Next, create an instance of this class and assign it to
#a variable called "number_instance".
#
#Then, set the value attribute to 101 and the even
#attribute to False.


#Write your code here!
class Number:
    def __init__(self):
        self.value = 0
        self.even = True

number_instance = Number()
number_instance.value = 101
number_instance.even = False

#Note that this exercise does not print anything by
#default. You're welcome to add print statements to debug
#your code when running it. Note that the autograder
#will check both your value for number_instance and your
#definition of the class Number.


