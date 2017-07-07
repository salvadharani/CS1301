#Write a function, called lucky_sevens, that takes in one
#parameter, a list of integers, and returns True if the list
#has three '7's  in a row and False if the list doesn't.
#
#For example:
#
#  lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]) -> True
#  lucky_sevens([4, 7, 7, 2, 8, 3, 7, 4, 3]) -> False
#
#Hint: As soon as you find one instance of three sevens, you
#could go ahead and return True -- you only have to find it
#once for it to be True! Then, if you get to the end of the
#function and haven't returned True yet, then you might
#want to return False.


#Write your function here!

def lucky_sevens_s(integer_list):
    if 7 in integer_list:
        integer_list_str = [str(x) for x in integer_list]
        joined_int_list = ''.join(integer_list_str)
        if '777' in joined_int_list:
            return True
    return False



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, then False
print(lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]))
print(lucky_sevens([4, 7, 7, 2, 8, 3, 7, 4, 3]))

# Solutions
def lucky_sevens(a_list):
    for i in range(len(a_list)-2):
        if a_list[i] == 7:
            if a_list[i+1] == 7:
                if a_list[i+2] == 7:
                    return True
    return False

def lucky_sevens2(a_list):
    a_list_str = map(str, a_list)
    a_list_as_one_string = "".join(a_list_str)
    return "777" in a_list_as_one_string


def lucky_sevens3(alist):
    consecutive_7s = 0
    for num in alist:
        if num == 7:
            consecutive_7s +=1
        else:
            consecutive_7s = 0
    if consecutive_7s == 3:
        return True