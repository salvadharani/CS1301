# We've written a function below called countDown(). This
# function takes an int parameter, start, and prints every
# number from that start to 0. The way we've written it uses
# recursion. Below that function, write a function that does
# the exact same thing, but do not use recursion.
#
# The purpose of this exercise is for you to recognize some
# example instances in which you can use recursion, and what
# differences can be seen in the actual code.
#
# Make sure to actually print 0 as the last number!

def countDown(start):
    # If we've reached 0 already, print 0 but do not call
    # another copy
    if start <= 0:
        print(start)

    # If we haven't reached 0 yet, print the current number,
    # then call countDown with the current number minus 1.
    else:
        print(start)
        countDown(start - 1)


# Do not modify the code above.
# Fill in the function below to do the same as the function
# above, but without recursion. You could use for loops,
# while loops, or some other approach.

def countDown2(start):
    for i in range(start, -1, -1):
        print(i)


# Add your code here!

# Optionally, you may modify the code below to test your
# function and make sure it matches the output of
# countDown(). However, because our grader grades your
# program's output, you should delete or comment out
# anything below before submitting.


countDown(5)
print()
countDown2(5)