from collections import namedtuple

# Create a named tuple type for representing a student
Student = namedtuple('Student', 'ID MARKS NAME CLASS')

# Read the number of students from input
n = int(input())

# Read the column names from input
columns = input().split()

# Find the index of each column name in the order 'ID', 'MARKS', 'NAME', 'CLASS'
id_index = columns.index('ID')
marks_index = columns.index('MARKS')
name_index = columns.index('NAME')
class_index = columns.index('CLASS')

total_marks = 0

# Iterate through each student record and calculate the total marks
for _ in range(n):
    student_data = input().split()

    # Create a student object using the named tuple type
    student = Student(ID=int(student_data[id_index]),
                      MARKS=int(student_data[marks_index]),
                      NAME=student_data[name_index],
                      CLASS=int(student_data[class_index]))

    total_marks += student.MARKS

# Calculate the average marks
average_marks = total_marks / n

# Print the average marks rounded to 2 decimal places
print('{:.2f}'.format(average_marks))
