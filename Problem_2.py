'''2. Advanced List Methods and Identity Operators
Objective:
The aim of this assignment is to delve deeper into list methods and understand the nuances of identity operators.

Problem Statement:
You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.

Task 1: Given the two lists:

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
Find out which students both submitted their assignments and attended the class.

Task 2: Check if the two lists are identical in terms of their content, regardless of order.

Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.'''

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

#Task 1

if "Alice" in submitted and "Alice" in attended:
    print("Alice has submitted and attended!")
if "Charlie" in submitted and "Charlie" in attended:
    print("Charlie has submitted and attended!")

#Task 2

if submitted is attended:
    print("Both lists are identical!")
else:
    print("Not the same list!")

#Task 3

attended.remove("Eve")
attended.remove("Frank")
print(attended)

