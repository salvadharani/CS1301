#Write a function called modify_dict. modify_dict takes one
#parameter, a dictionary. The dictionary's keys are people's
#last names, and the dictionary's values are people's first
#names. For example, the key "Joyner" would have the value
#"David".
#
#modify_dict should delete any key-value pair for which the
#key's first letter is not capitalized. For example, the
#key-value pair "joyner":"David" would be deleted, but the
#key-value pair "Joyner":"david" would not be deleted. Then,
#return the modified dictionary.
#
#Remember, the keyword del deletes items from lists and
#dictionaries. For example, to remove the key "key!" from
#the dictionary my_dict, you would write: del my_dict["key!"]
#Or, if the key was the variable my_key, you would write:
#del my_dict[my_key]
#
#Hint: If you try to delete items from the dictionary while
#looping through the dictionary, you'll run into problems!
#We should never change the number if items in a list or
#dictionary while looping through those items. Think about
#what you could do to keep track of which keys should be
#deleted so you can delete them after the loop is done.
#
#Hint 2: To check if the first letter of a string is a
#capital letter, use string[0].isupper().


#Write your function here!
def modify_dict(dictionary):
    modified = {}
    for name in dictionary:
        if name == name.title():
            modified[name] = dictionary[name]
    return modified




#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#  {'Diaddigo':'Joshua', 'Elliott':'jackie'}
my_dict = {'Joshua':'Diaddigo', 'joyner':'David', 'Elliott':'jackie', 'murrell':'marguerite'}
print(modify_dict(my_dict))






