from typing import Any

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
def calculate_average_grades(grades, students):

 sorted_students = sorted(students)
 average_grades = {}

 for i, student in enumerate(sorted_students):
    student_grades = grades[i]
    average = sum(student_grades) / len(student_grades)
    average_grades[student] = average

 return average_grades

result = calculate_average_grades(grades, students)
print(result)
