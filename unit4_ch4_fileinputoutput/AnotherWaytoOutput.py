myList = ["David", "Lucy", "Vrushali", "Ping",
          "Natalie", "Dana", "Addison", "Jasmine"]

outputfile = open("outputfile.txt", "w")

for name in myList:
    print(name, file=outputfile) # this one already puts a line break (print does that)

outputfile.close()