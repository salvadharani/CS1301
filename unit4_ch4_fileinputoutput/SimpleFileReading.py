inputfile = open("OutputFile.txt", "r")

print(inputfile.readline())
print(inputfile.readline())
print(inputfile.readline())

inputfile.close()

# prints lines with a blank space in between
# Blank space can be removed using parameter 'end = ""'

inputfile = open("OutputFile.txt", "r")

print(inputfile.readline(), end="")
inputfile.close()

# Also, this way

inputfile = open("OutputFile.txt", "r")

print(inputfile.readline().strip())
inputfile.close()

# Or a variable can be used to hold the lines (use .strip() if reading in strings,
#  if converting to int, no need for .strip():

inputfile = open("OutputFile.txt", "r")

line1 = inputfile.readline().strip() # use integer conversion if necessary
line2 = inputfile.readline().strip()
line3 = inputfile.readline().strip()

print(line1)
print(line2)
print(line3)

inputfile.close()