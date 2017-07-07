myInt1 = 12
myInt2 = 23
myInt3 = 34

# Open OutputFile.txt in write mode
outputFile = open("OutputFile.txt", "w")

# Write variables to outputFile
# This writes each variable in a line. Without the line breaks,
# the variables will be written in a single line.
# The linebreak must be concatenated as the write method only
# takes one argument.
outputFile.write(str(myInt1) + '\n')
outputFile.write(str(myInt2) + '\n')
outputFile.write(str(myInt3) + '\n')

# Close outputFile
outputFile.close()