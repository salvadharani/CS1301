# Let's implement the Fibonacci function we saw in the
# previous video in Python!
#
# Like our Factorial function, our Fibonacci function
# should take as input one parameter, n, an integer. It
# should calculate the nth Fibonacci number. For example,
# fib(7) should give 13 since the 7th number in
# Fibonacci's sequence is 13.

# So, our function definition will basically be the same:

def fib(n):
    # What do we want to do inside the function? Once again,
    # there are really only two cases: either we're looking
    # for the first two Fibonacci numbers, or we're not.
    # What happens if we're looking for the first two? Well,
    # we already know that the 1st and 2nd Fibonacci numbers
    # are both 1, so if n == 1 or n == 2, we can go ahead
    # and return 1.

    if n == 1 or n == 2:
        return 1

    # What if n doesn't equal 1? For any value for n greater
    # than 2, the result should be the sum of the previous
    # two numbers. The previous Fibonacci number could then
    # be calculated with the same kind of function call,
    # decrementing n by 1 or 2.

    else:
        return fib(n - 1) + fib(n - 2)

        # If n is greater than 2, then it returns the sum of the
        # previous two fibonacci numbers, as calculated by the
        # same function.


# Now let's test it out! Run this file to see the results.
print("fib(5) is", fib(5))
print("fib(10) is", fib(10))

# Want to see more about how this works? Select the other
# file, FibonacciwithPrints.py, from the drop-down in the
# top left to see a version of this that traces the output.


