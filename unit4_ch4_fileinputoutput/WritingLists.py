myList = ["David", "Lucy", "Vrushali", "Ping",
          "Natalie", "Dana", "Addison", "Jasmine"]

outputfile = open("OutputFile.txt", "w")

for name in myList:
    outputfile.write(name + "\n")

# outputfile.writelines(myList) == > writes everything in one line
# outputfile.write('/n'.join(myList)) ==> fixes that

outputfile.close()

