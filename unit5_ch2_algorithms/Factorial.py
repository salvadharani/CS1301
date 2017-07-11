# Let's implement the factorial function we saw in the
# previous video in Python!
#
# Our factorial function should take as input a number, and
# it should return the product of that number times every
# number between itself and 1.

# Let's start with the function definition. This function
# definition creates the function factorial with one
# parameter, n.

def factorial(n):
    # What do we want to do inside the function? Well, there
    # are two cases. First, if n is 1, we just want to return
    # 1. After all, 1! is 1.

    if n == 1:
        return 1

    # What if n doesn't equal 1, though? Then we want to
    # return n times the factorial of (n - 1). After all,
    # 5! = 5 * 4!, 4! = 4 * 3!, etc.

    else:
        return n * factorial(n - 1)

        # If n is greater than 1, then it multiplies 1 by the
        # factorial of n - 1, as calculated with the same
        # function. Every time factorial() runs, n decreases
        # by 1, which guarantees that eventually, n will equal
        # 1.


# Now let's test it out! Run this file to see the results.
print("5! is", factorial(5))
print("10! is", factorial(10))

# Want to see more about how this works? Select the other
# file, FactorialwithPrints.py, from the drop-down in the
# top left to see a version of this that traces the output.