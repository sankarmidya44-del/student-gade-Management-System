
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
