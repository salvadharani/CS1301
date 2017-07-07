def save(filename, inList):
    outputFile = open(filename, "w")

    for item in inList:
        print(item, file=outputFile)

    outputFile.close()

def load(filename):
    inputFile = open(filename, "r")
    inList = []

    for line in inputFile:
        inList.append(line.strip())
    inputFile.close()
    return inList

myList = ["David", "Lucy", "Vrusali", "Ping", "Natalie"]

save("OutputFile.txt", myList)
newList = load("OutputFile.txt")

print(newList)