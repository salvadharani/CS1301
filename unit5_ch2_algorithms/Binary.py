#Recall in Worked Example 5.2.5 that we showed you the code
#for two versions of binary_search: one using recursion, one
#using loops.
#
#In this problem, we want to implement a new version of
#binary_search, called binary_year_search. binary_year_search
#will take in two parameters: a list of instances of Date,
#and a year as an integer. It will return True if any date
#in the list occurred within that year, False if not.
#
#For example, imagine if listOfDates had three instances of
#date: one for January 1st 2016, one for January 1st 2017,
#and one for January 1st 2018. Then:
#
#  binary_year_search(listOfDates, 2016) -> True
#  binary_year_search(listOfDates, 2015) -> False
#
#You should not assume that the list is pre-sorted, but you
#should know that the sort() method works on lists of dates.
#
#Instances of the Date class have three attributes: year,
#month, and day. You can access them directly, you don't
#have to use getters (e.g. myDate.month will access the
#month of myDate).
#
#You may copy the code from Worked Example 5.2.5 and modify
#it instead of starting from scratch.
#
#Don't move this line:
from datetime import date


#Write your code here!
def binary_year_search(listOfDates, year):
    listOfDates.sort()
    if len(listOfDates) == 0:
        return False
    else:
        mid = len(listOfDates) // 2
        if listOfDates[mid].year == year:
            return True
        elif year < listOfDates[mid].year:
            return binary_year_search(listOfDates[:mid], year)
        else:
            return binary_year_search(listOfDates[mid + 1:], year )


#The lines below will test your code. If it's working
#correctly, they will print True, then False.
listOfDates = [date(2016, 11, 26), date(2014, 11, 29),
               date(2008, 11, 29), date(2000, 11, 25),
               date(1999, 11, 27), date(1998, 11, 28),
               date(1990, 12, 1), date(1989, 12, 2),
               date(1985, 11, 30)]

print(binary_year_search(listOfDates, 2016))
print(binary_year_search(listOfDates, 2007))

#print(binary_year_search(listOfDates))

