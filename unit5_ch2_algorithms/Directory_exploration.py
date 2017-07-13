def ListFiles(dir):
    for file in dir:
        print(file)
    for folder in dir:
        ListFiles(folder)

# tail recursion - recursive call is closer to the end of the function, after some other reasoning or code
        #
        #  (vs. head recursion - recursive call is near the beginning of the function, before other reasoning or code)

# Exercise 1 5.2.3

# Below is the countdown function from before. It's an example of a head recursion:
# (see Exercise1_531.py -- shows this code in a tail recursion version)
def countDown(start):
    if start <= 0:
        print(start)
    else:
        countDown(start - 1)
        print(start)

countDown(5)
# counts from 0 to 5!