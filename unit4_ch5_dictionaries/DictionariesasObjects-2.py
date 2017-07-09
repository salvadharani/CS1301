ANSWER_KEY = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "A"}

students = {}
students["David"] = {"1": "A", "2": "B", "3": "A", "4": "B", "5": "C"}
students["Terra"] = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "A"}
students["Lugos"] = {"1": "A", "2": "C", "3": "C", "4": "D", "5": "A"}

# For each student and their answers
for (student, answers) in students.items():
    grade = 0  # Start grade at 0
    # For each question and answer
    for (question, answer) in answers.items():
        # If the answer matches ANSWER_KEY's answer...
        if answer == ANSWER_KEY[question]:
            grade += 1  # Increment their grade
    # Create a new key "grade" and assign it their grade
    students[student]["grade"] = grade
# For each student and their answers
for (student, answers) in students.items():
    # Print the name and grade
    print(student, ": ", answers["grade"], sep="", end="; ")


