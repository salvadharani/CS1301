#Copy both your code and ours from the previous exercise.
#You should copy your Burrito class and our Meat, Rice, and
#Beans classes into this exercise.
#
#In this exercise, you won't edit any of your code from the
#Burrito class. Instead, you're just going to write a
#function to use instances of the Burrito class.
#
#Write a function called total_cost. total_cost should take
#as input a list of instances of Burrito, and return the
#total cost of all those burritos together as a float.
#
#Hint: Don't reinvent the wheel. Use the work that you've
#already done. The function can be written in only five
#lines, including the function declaration.
#
#Hint 2: The exercise here is to write a function, not a
#method. That means this function should *not* be part of
#the Burrito class.


#Paste your previous code here.

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


# Write your new function here.

def total_cost(burrito_list):
    total = 0
    for burrito in burrito_list:
        total += burrito.get_cost()
    return total


#You can add code below to test your function. We'd suggest
#creating a couple instances of Burrito, adding them to a
#list, then passing that list to total_cost and printing the
#result.



# order = Burrito(meat=False, to_go=True, beans="pinto", rice="brown", extra_meat=True,
#                 guacamole=True, cheese=False, pico=False, corn=False)
#
# print(order.meat.value)
# print(order.to_go)
# print(order.beans.value)
# print(order.rice.value)
# print(order.extra_meat)
# print(order.guacamole)
# print(order.cheese)
# print(order.pico)
# print(order.corn)
#
# print(order.get_cost())