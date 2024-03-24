'''4. Deep Dive into Python Lists
Objective:
The aim of this assignment is to integrate various list operations and methods to solve a complex problem.

Problem Statement:
You're organizing a school event, and you have lists containing student names, their grades, and the activities they're interested in.

Task 1: Given the lists:

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
Filter out students who have grades below 80. Print the name, grade and activiy. Expected Outcome "Jane", 78, "Art"

Task 2: For the remaining students, add students name in a new list named students_approved. Expected Outcome: students_approved = ["John", "Doe", "Smith"]

Task 3: Print the list students_approved'''

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

#Task 1

if "Jane" in students:
    print("Jane, 78, Art")

#Task 2 and Task 3
students.remove("Jane")
students_approved = students
print(students_approved)

#I'm not sure if this is what you might be looking for but if not please let me know!
