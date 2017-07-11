# Problem 5.1.2

#Write a class called "Burrito". A Burrito should have the
#following attributes (instance variables):
#
# - meat
# - to_go
# - rice
# - beans
# - extra_meat (default: False)
# - guacamole (default: False)
# - cheese (default: False)
# - pico (default: False)
# - corn (default: False)
#
#The constructor should let any of these attributes be
#changed when the object is instantiated. The attributes
#with a default value should be optional.
#
#Hint: Notice that we haven't specified types for the
#non-optional attributes: that's because the types for
#those won't matter!
#
#Hint 2: Think about how we can have default values for
#the last five arguments that can be overridden when the
#object is instantiated.


#Write your code here!

class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False, corn=False):
        self.set_meat(meat)
        self.set_to_go(to_go)
        self.set_rice(rice)
        self.set_beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)

#The code below will test your class. If it is written
#correctly, this will print True, then False. Note,
#though, that we'll test your code against more complex
#test cases when you submit.

# newBurrito = Burrito("Tofu", True, True, True)
# print(newBurrito.to_go)
# print(newBurrito.guacamole)

# Problem 5.1.3

#Copy your Burrito class from the last exercise. Now,
#write a getter and a setter method for each attribute.
#each setter should accept a value as an argument. If the
#value is a valid value, it should set the corresponding
#attribute to the given value. Otherwise, it should set the
#attribute to False. Edit the constructor to use these new
#setters and getters.
#
#Valid values for each setter are as follows:

# - set_meat: "chicken", "pork", "steak", "tofu", False
# - set_to_go: True, False
# - set_rice: "brown", "white", False
# - set_beans: "black", "pinto", False
# - set_extra_meat: True, False
# - set_guacamole: True, False
# - set_cheese: True, False
# - set_pico: True, False
# - set_corn: True, False

#Make sure you name each setter with the format:
#"set_some_attribute" and "get_some_attribute"
#
#For example, the getter for meat would be get_meat. The
#getter for to_go would be get_to_go.
#
#Hint: Your code is going to end up *very* long. This
#will be the longest program you've written so far, but
#it isn't the most complex. Complexity and length are
#often very different!
#
#Hint 2: Checking for valid values will be much easier
#if you make a list of valid values for each attribute
#and check the new value against that.


#Write your code here!

    def get_meat(self):
        return self.meat

    def get_to_go(self):
        return self.to_go

    def get_rice(self):
        return self.rice

    def get_beans(self):
        return self.beans

    def get_extra_meat(self):
        return self.extra_meat

    def get_guacamole(self):
        return self.guacamole

    def get_cheese(self):
        return self.cheese

    def get_pico(self):
        return self.pico

    def get_corn(self):
        return self.corn


    def set_meat(self, meat):
        if meat in ["chicken", "pork", "steak", "tofu"]:
            self.meat = meat
            # print("{} added".format(self.meat))
        else:
            self.meat = False
            # print("No meat")

    def set_to_go(self, to_go):
        if type(to_go) == bool:
            self.to_go = to_go
            # print("to go {}".format(self.to_go))
        else:
            print("invalid value")

    def set_rice(self, rice):
        if rice in ["brown", "white"]:
            self.rice = rice
            # print("{} rice added".format(self.rice))
        else:
            self.rice = False
            # print("no rice")

    def set_beans(self, beans):
        if beans in ["black", "pinto"]:
            self.beans = beans
            # print("{} beans added".format(self.beans))
        else:
            self.beans = False
            # print("no beans")

    def set_extra_meat(self, extra_meat):
        if type(extra_meat) == bool:
            self.extra_meat = extra_meat
            # print("extra meat {}".format(self.extra_meat))
        else:
            print("invalid value")

    def set_guacamole(self, guacamole):
        if type(guacamole) == bool:
            self.guacamole = guacamole
            # print("guacamole {}".format(self.guacamole))
        else:
            print("invalid value")

    def set_cheese(self, cheese):
        if type(cheese) == bool:
            self.cheese = cheese
            # print("cheese {}".format(self.cheese))
        else:
            print("invalid value")

    def set_pico(self, pico):
        if type(pico) == bool:
            self.pico = pico
            # print("pico {}".format(self.pico))
        else:
            print("invalid value")

    def set_corn(self, corn):
        if type(corn) == bool:
            self.corn = corn
            # print("corn {}".format(self.corn))
        else:
            print("invalid value")

#Feel free to add code below to test out the class that
#you've written. It won't be used for grading.

order1 = Burrito("chicken", to_go=False, rice="brown", beans="black", extra_meat=True, guacamole=False, cheese=True, pico=True, corn=True)
print("Meat", order1.meat)
print("To go", order1.to_go)
print("Rice", order1.rice)
print("Beans", order1.beans)
print("Extra meat", order1.extra_meat)
print("Cheese", order1.cheese)
print("Pico", order1.pico)
print("Corn", order1.corn)
print("Guacamole", order1.guacamole)


