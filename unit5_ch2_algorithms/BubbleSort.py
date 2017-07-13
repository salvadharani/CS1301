# We've written the function, bubbleSort, below. It takes in
# one list parameter, lst. However, there are two problems in
# our current code:
# - There's a missing line
# - There's a semantic error (the code does not raise an
#   error message, but it does not perform correctly)
#
# Find and fix these problems! Note that you should only need
# to change or add code where explicitly indicated.
#
# Hint: If you're stuck, use an example input list and trace
# the code and how it modifies your list on paper. For
# example, try writing out what happens to the following list:
#
#  [34, 16, 2, 78, 4, 6, 1]

def bubbleSort(lst):
    # Set swapOccurred to True to guarantee the loop runs once
    swapOccurred = True

    # Run the loop as long as a swap occurred the previous time
    while swapOccurred:

        # Start off assuming a swap did not occur
        swapOccurred = False

        # For every item in the list except the last one...
        for i in range(len(lst) - 1):

            # If the item should swap with the next item...
            if lst[i] > lst[i + 1]:
                # Then, swap them! But these lines aren't
                # quite right: fix this code!
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp

                # One more line is needed here; add it!
                swapOccurred = True

    return lst


# The line below will test your code. If it works, a sorted
# list will be printed. This is not used for grading, so
# feel free to change it.
print(bubbleSort([5, 3, 1, 2, 4]))


