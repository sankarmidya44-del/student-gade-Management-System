# student-gade-Management-System
#1. Problem Statement

#Develop a Student Grade Management System that accepts a student's details (name, roll number, and marks in three subjects), calculates the total marks and average percentage, assigns a grade based on the average, and displays the complete student report.

#The grading criteria are:

#Average Marks	Grade
#90–100	A
#80–89	B
#70–79	C
#60–69	D
#Below 60	F
#2. Algorithm
#Start.
#Input the student's name.
#Input the roll number.
#Input marks for three subjects.
#Calculate:
#Total = Subject1 + Subject2 + Subject3
#Average = Total / 3
#Determine the grade:
#If Average ≥ 90 → Grade = A
#Else if Average ≥ 80 → Grade = B
#Else if Average ≥ 70 → Grade = C
#Else if Average ≥ 60 → Grade = D
#Else → Grade = F
#Display:
#Student Name
#Roll Number
#Subject Marks
#Total
#Average
#Grade
#Stop.
#3. Flowchart
#              START
#                 │
#                 ▼
#      Enter Name & Roll No.
#                 │
#                 ▼
#     Enter Marks of 3 Subjects
#                 │
#                 ▼
#   Calculate Total and Average
#                 │
#                 ▼
#       Is Average ≥ 90 ?
#          /             \
#        Yes             No
#        │                │
#   Grade = A      Is Average ≥ 80?
#                     /         \
#                   Yes         No
#                   │            │
#              Grade = B   Is Average ≥ 70?
#                              /       \
#                            Yes       No
#                            │          │
#                       Grade = C  Is Average ≥ 60?
#                                     /      \
#                                   Yes      No
#                                   │         │
#                              Grade = D  Grade = F
#                                      │
#                                      ▼
#                          Display Student Report
#                                      │
#                                      ▼
#                                    STOP
# Input student details   #

name = input("Enter Student Name: ")
roll = int(input("Enter Roll Number: "))

# Input marks
m1 = float(input("Enter Marks in Subject 1: "))
m2 = float(input("Enter Marks in Subject 2: "))
m3 = float(input("Enter Marks in Subject 3: "))

# Calculate total and average
total = m1 + m2 + m3
average = total / 3

# Determine grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Display result
print("\n========== Student Report ==========")
print("Student Name :", name)
print("Roll Number  :", roll)
print("Subject 1    :", m1)
print("Subject 2    :", m2)
print("Subject 3    :", m3)
print("Total Marks  :", total)
print("Average      :", round(average, 2))
print("Grade        :", grade)
print("====================================")

# 5. Input
# Student Name : Sankar Midya
# Roll Number  : 101
# Subject 1    : 85
# Subject 2    : 90
# Subject 3    : 88
#
# 6. Output
# ----- Student Report -----
#
# Name      : Sankar Midya
# Roll No   : 101
# Subject 1 : 85
# Subject 2 : 90
# Subject 3 : 88
#Author:Sankar

# Total     : 263
# Average   : 87.67
#
# Grade     : B
