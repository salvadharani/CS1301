myList = [ ]
inputfile = open("OutputFile.txt", "r")

for line in inputfile:
    myList.append(line.strip())

print(myList)

inputfile.close()

