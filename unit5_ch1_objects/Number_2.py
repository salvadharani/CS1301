#Rewrite the "Number" class from 5.1.2 Coding Exercise 2.
#This time, however, require arguments for value and
#even in the constructor. Then, inside the constructor,
#create new instance variables called value and even that
#copy the values of the arguments passed into the
#constructor.
#
#In other words, rewrite the Number class such that value
#and even behave the way studentName and enrolled behaved
#in the exercise above, and the way firstname and lastname
#behaved in video 5.1.4.1.
#
#Then, as before, create an instance of this class and
#assign it to a variable called "number_instance". value
#should again be set to 101 and even should be set to
#False.
#
#Hint: Remember, the way you initialize the instance will
#have to change, too, based on the changes to the
#constructor that we're requiring.


#Write your code here!
class Number:
    def __init__(self, value, even):
        self.value = value
        self.even = even

number_instance = Number(value=101, even=False)
print(number_instance.value)
print(number_instance.even)

#Note that this exercise does not print anything by
#default. You're welcome to add print statements to debug
#your code when running it. Note that the autograder
#will check both your value for number_instance and your
#definition of the class Number.


