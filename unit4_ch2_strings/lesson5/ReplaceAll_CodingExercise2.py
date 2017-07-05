#Write a function called "replace_all" that accepts three
#arguments:
#
# - target_string, a string in which to search.
# - find_string, a string to search for.
# - replace_string, a string to use to replace every instance
#   of the value of find.
#
#The arguments will be provided in this order. Your function
#should mimic the behavior of "replace", but you cannot use
#that function in your implementation. Instead, you should
#find the result using a combination of split() and join(),
#or some other method.
#
#Hint: This exercise can be complicated, but it can also
#be done in a single short line of code! Think carefully about
#the methods we've covered.


#Write your function here!
def replace_all(target_string, find_string, replace_string):
    return replace_string.join(target_string.split(find_string))


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "In case I don't see ya, bad afternoon, bad evening,
#and bad night!"
target = "In case I don't see ya, good afternoon, good evening, and good night!"
find = "good"
replace = "bad"
print(replace_all(target, find, replace))




