# Copy your Burrito class from the last exercise. Below,
# We've given you three additional classes named "Meat",
# "Rice" and "Beans." We've gone ahead and built getters
# and setters in these classes to check if the incoming
# values are valid, so you'll be able to remove those
# from your original code.
#
# First, edit the constructor of your Burrito class.
# Instead of calling setters to set the values of the
# attributes self.meat, self.rice, and self.beans, it
# should instead create new instances of Meat, Rice, and
# Beans. The arguments to these new instances should be
# the same as the arguments you were sending to the
# setters previously (e.g. self.rice = Rice("brown")
# instead of set_rice("brown")).
#
# Second, modify your getters and setters from your
# original code so that they still return the same value
# as before. get_rice(), for example, should still
# return "brown" for brown rice, False for no rice, etc.
# instead of returning the instance of Rice.
#
# Third, make sure that your get_cost function still
# works when you're done changing your code.
#
# Hint: When you're done, creating a new instance of
# Burrito with Burrito("pork", True, "brown", "pinto")
# should still work to create a new Burrito. The only
# thing changing is the internal reasoning of the
# Burrito class.
#
# Hint 2: Notice that the classes Meat, Beans, and Rice
# already contain the code to validate whether input is
# valid. So, your setters in the Burrito class no
# longer need to worry about that -- they can just pass
# their input to the set_value() methods for those
# classes.
#
# Hint 3: This exercise requires very little actual
# coding: you'll only write nine lines of new code, and
# those nine lines all replace existing lines of code
# in the constructor, getters, and setters of Burrito.
#
# You should not need to modify the code below.

class Meat:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["chicken", "pork", "steak", "tofu"]:
            self.value = value
        else:
            self.value = False


class Rice:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["brown", "white"]:
            self.value = value
        else:
            self.value = False


class Beans:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["black", "pinto"]:
            self.value = value
        else:
            self.value = False

# Write your code here!

class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False, corn=False):
        self.meat = Meat(meat)
        self.rice = Rice(rice)
        self.beans = Beans(beans)
        self.set_to_go(to_go)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)

    def get_meat(self):
        return self.meat.get_value()

    def get_to_go(self):
        return self.to_go

    def get_rice(self):
        return self.rice.get_value()

    def get_beans(self):
        return self.beans.get_value()

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
        return self.meat.set_value(meat)

    def set_to_go(self, to_go):
        if type(to_go) == bool:
            self.to_go = to_go
        else:
            print("invalid value")

    def set_rice(self, rice):
        return self.rice.set_value(rice)

    def set_beans(self, beans):
        return self.beans.set_value(beans)

    def set_extra_meat(self, extra_meat):
        if type(extra_meat) == bool:
            self.extra_meat = extra_meat
        else:
            print("invalid value")

    def set_guacamole(self, guacamole):
        if type(guacamole) == bool:
            self.guacamole = guacamole
        else:
            print("invalid value")

    def set_cheese(self, cheese):
        if type(cheese) == bool:
            self.cheese = cheese
        else:
            print("invalid value")

    def set_pico(self, pico):
        if type(pico) == bool:
            self.pico = pico
        else:
            print("invalid value")

    def set_corn(self, corn):
        if type(corn) == bool:
            self.corn = corn
        else:
            print("invalid value")


    def get_cost(self):
        self.price = 5.00
        if self.meat.get_value() in ["chicken", "pork", "tofu"]:
            self.price += 1.00

        if self.meat.get_value() == "steak":
            self.price += 1.50

        if self.extra_meat == True and self.meat.get_value() != False:
            self.price += 1.00

        if self.guacamole == True:
            self.price += 0.75

        return self.price

# You may add code below to test your program;
# it will not be used for grading.

order = Burrito(meat=False, to_go=True, beans="pinto", rice="brown", extra_meat=True,
                guacamole=True, cheese=False, pico=False, corn=False)

print(order.meat.value)
print(order.to_go)
print(order.beans.value)
print(order.rice.value)
print(order.extra_meat)
print(order.guacamole)
print(order.cheese)
print(order.pico)
print(order.corn)

print(order.get_cost())