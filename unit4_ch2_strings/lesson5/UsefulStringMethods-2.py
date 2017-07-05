myStringToSplit = "My-string-to-split"
print(myStringToSplit)

#Splits myStringToSplit and assigns it
#to mySplitString
mySplitString = myStringToSplit.split("-")
print(mySplitString)

#Joins mySplitString using "-" and assigns
#it to myJoinedString
myJoinedString = "-".join(mySplitString)
print(myJoinedString)
