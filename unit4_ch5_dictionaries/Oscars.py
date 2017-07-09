#Write a function called most_oscars, which takes in one
#parameter, a dictionary. This dictionary maps names to the
#number of Academy Awards for which they have been nominated.
#This function should return a tuple containing the name and
#number of nominations for the person who has the most
#nominations.
#
#You may assume there will not be a tie for the actor with
#the most nominations (although there may be other ties in
#the list).


#Write your function here!
def most_oscars(adictionary):
    highest = 0
    actor = None
    for name in adictionary:
        if adictionary[name] > highest:
            highest = adictionary[name]
            actor = name
    return actor, highest


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: ('Meryl Streep', 20)
nominees = {'Meryl Streep': 20, 'Robert De Niro': 7, 'Michael Caine': 6, 'Maggie Smith': 6}
print(most_oscars(nominees))




