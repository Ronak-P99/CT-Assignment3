'''Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!

Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!

1. Python List Transformation
Objective:
The aim of this assignment is to practice advanced list operations and transformations.

Problem Statement:
You've been given a list of numerical grades from a class exam. You need to process and analyze these grades.

Task 1: Given the list of grades: 
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

Sort the grades in descending order and display the sorted list.

Task 2: Calculate the average grade and display it.

Task 3: Replace any grade below 80 with the value Failed.'''

#Task 1

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
grades.reverse()
print(grades)

#Task 2

grades_avg = sum(grades) / 10
print(f"Average grade equals:", grades_avg)

#Task 3
grades[-1] = 'Failed'
grades[-2] = 'Failed'
grades[-3] = 'Failed'
print(grades)





    