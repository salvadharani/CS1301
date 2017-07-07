#Write a function called "append_to_file" that accepts
#two parameters: a filename and some data that will
#be an integer or a string to write. The function
#should open the file and add the data to the end of
#the file. Each new call to append_to_file should add
#the new contents on a new line.
#
#Hints:
#
# - Don't forget to close the file when you're done!
# - If the data isn't a string already, you may need
#   to convert it.
# - Remember, this code has no print statements, so
#   when you run it, don't expect to see any output
#   on the right! You could add print statements if
#   you want a confirmation the code is done running.
# - You can put the variable for the filename in the
#   same place where we put text like OutputFile.txt
#   in the videos.


#Write your function here!
def append_to_file0(filename, data):
    outputfile = open(filename, "a")
    outputfile.write(str(data) + '\n')
    outputfile.close()

def append_to_file(filename, data):
    outputfile = open(filename, "a")
    print(str(data), file = outputfile)
    outputfile.close()
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print nothing. However, if you open AppendToFileOutput.txt
#in the top left after running it, the contents of the
#file should be another instance of 1301 every time you
#run this file.
append_to_file("AppendToFileOutput.txt", 1301)




