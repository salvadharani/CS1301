#Write a function called "write_file" that accepts two
#parameters: a filename and some data that will either
#be an integer or a string to write. The function
#should open the file and write the data to the file.
#
#Hints:
#
# - Don't forget to close the file when you're done!
# - If the data isn't a string already, you may need
#   to convert it, depending on the approach you
#   choose.
# - Remember, this code has no print statements, so
#   when you run it, don't expect to see any output
#   on the right! You could add print statements if
#   you want a confirmation the code is done running.
# - You can put the variable for the filename in the
#   same place where we put text like OutputFile.txt
#   in the videos.


#Write your function here!
def write_file(filename, data):
    outputfle = open(filename, "w")
    outputfle.write(str(data))
    outputfle.close()


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print nothing. However, if you open WriteFileOutput.txt
#in the top left after running it, the contents of the
#file should be 1301.
write_file("WriteFileOutput.txt", 1301)

