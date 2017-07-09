#Recall in coding problem 4.4.3 that you wrote a function
#called "reader" that read a .cs1301 file and returned a
#list of lists.
#
#Let's revise that problem. Instead of a list of lists,
#that's return a dictionary of dictionaries.
#
#Write a function called "reader" that takes one parameter,
#a filename as a string corresponding to a .cs1301 file,
#and reads in that .cs1301 file.
#
#Each line of the .cs1301 file will have five items, each
#separated by a space: the first, third, and fourth will
#represent integers, the second will be a string, and the
#fifth will represent a float. (Note: when reading the
#file, these will all be strings; you can assume each of
#these strings can be converted to the corresponding data
#type, however.)
#
#The function should return a dictionary of dictionaries
#representing the file contents.
#
#The keys of the top-level dictionary should be the
#assignment names. Then, the value for each of those keys
#should be a dictionary with four keys: "number", "grade",
#"total", and "weight". The values corresponding to each of
#those four keys should be the values from the file,
#converted to the corresponding data types (ints or floats).
#
#For example, if the input file read:
#
# 1 exam_1 90 100 0.6
# 2 exam_2 95 100 0.4
#
#Then reader would return this dictionary of dictionaries:
#
# {"exam_1": {"number": 1, "grade": 90, "total": 100, "weight": 0.6},
#  "exam_2": {"number": 2, "grade": 95, "total": 100, "weight": 0.4}}
#
#Hint: Although the end result is pretty different, this
#should only dictate a minor change to your original
#Problem 4.4.3 code!


#Write your function here!
def reader(filename):
    grades = {}
    filein = open(filename)
    for line in filein:
        grade = line.strip().split()
        grades[grade[1]] = {'total': int(grade[3]), 'number': int(grade[0]), 'grade': int(grade[2]), 'weight': float(grade[4])}
    filein.close()
    return grades



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{'assignment_1': {'total': 100, 'number': 1, 'grade': 85, 'weight': 0.25}, 'test_1': {'total': 100, 'number': 2, 'grade': 90, 'weight': 0.25}, 'exam_1': {'total': 100, 'number': 3, 'grade': 95, 'weight': 0.5}}
print(reader("sample.cs1301"))


# answer = {
#           'homework_1': {'weight': 0.1, 'total': 30, 'grade': 26, 'number': 3},
#           'test_1': {'weight': 0.07, 'total': 50, 'grade': 4, 'number': 9},
#           'assignment_2': {'weight': 0.15, 'total': 75, 'grade': 26, 'number': 6},
#           'quiz_3': {'weight': 0.06, 'total': 90, 'grade': 8, 'number': 8},
#           'assignment_1': {'weight': 0.13, 'total': 65, 'grade': 7, 'number': 1},
#           'quiz_2': {'weight': 0.13, 'total': 45, 'grade': 21, 'number': 7},
#           'quiz_1': {'weight': 0.13, 'total': 80, 'grade': 68, 'number': 4},
#           'exam_1': {'weight': 0.14, 'total': 70, 'grade': 57, 'number': 2},
#           'exam_2': {'weight': 0.09, 'total': 40, 'grade': 3, 'number': 5}
#           }
#
# myanswer = {
#     'homework_1': {'weight': '0.1', 'total': '30', 'grade': '26', 'number': '3'},
#     'test_1': {'weight': '0.07', 'total': '50', 'grade': '4', 'number': '9'},
#     'assignment_2': {'weight': '0.15', 'total': '75', 'grade': '26', 'number': '6'},
#     'quiz_3': {'weight': '0.06', 'total': '90', 'grade': '8', 'number': '8'},
#     'assignment_1': {'weight': '0.13', 'total': '65', 'grade': '7', 'number': '1'},
#     'quiz_2': {'weight': '0.13', 'total': '45', 'grade': '21', 'number': '7'},
#     'quiz_1': {'weight': '0.13', 'total': '80', 'grade': '68', 'number': '4'},
#     'exam_1': {'weight': '0.14', 'total': '70', 'grade': '57', 'number': '2'},
#     'exam_2': {'weight': '0.09', 'total': '40', 'grade': '3', 'number': '5'}
# }