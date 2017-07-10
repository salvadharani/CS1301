#Write a class named "Phone". The Phone class should
#have an attribute called "storage" which defaults to
#128, and an attribute called "color" which defaults
#to "red".
#
#Hint: 'attribute' is another common word for
#'instance variable'.


#Write your class here!
class Phone:
    def __init__(self):
        self.storage = 128
        self.color = "red"

#The code below will test your class definition. It
#is not used for grading, so feel free to modify it.
#As written, it should print 128 and red.
newPhone = Phone()
print(newPhone.storage)
print(newPhone.color)


