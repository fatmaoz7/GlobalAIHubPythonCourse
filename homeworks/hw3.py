# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 21:41:36 2021

@author: fatma oz
"""

students={}
students_with_passing_grade={}
i=1;
n=5
students_grade_list_sorted=[]
while i<=n:
    name=input("Please enter student name")
    midterm=float(input("Please enter midterm grade of student"))
    project=float(input("Please enter project grade of student"))
    final=float(input("Please enter final grade of student"))
    students[name]=midterm,project,final
    passing_grade=students[name][0]*0.3+students[name][1]*0.3+students[name][2]*0.4;
    students_with_passing_grade[name]="Passing grade", passing_grade
    i+=1
    # passingGrades=[passing_grade for passing_grade in students_with_passing_grade.items()]
    students_grade_list_sorted.append(students_with_passing_grade[name][1])


print(students_with_passing_grade)
print(students)
# print(passingGrades)
print(sorted(students_grade_list_sorted,reverse=True))
                                                                             