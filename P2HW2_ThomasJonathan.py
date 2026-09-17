# Jonathan Thomas
# 17Sept2026
# P2HW2
# Calculate Grades

# Get the Grades
grade1 = float(input("Enter grade #1: "))
grade2 = float(input("Enter grade #2: "))
grade3 = float(input("Enter grade #3: "))
grade4 = float(input("Enter grade #4: "))
grade5 = float(input("Enter grade #5: "))
grade6 = float(input("Enter grade #6: "))

# Put them all into a new list
grade_list = [grade1, grade2, grade3, grade4, grade5, grade6]

# Do some calculations -- minimum, maximum, and average
min_grade = min(grade_list)
max_grade = max(grade_list)
total     = sum(grade_list)
count     = len(grade_list)

#calc average (total / count)
average = total / count
print(average)
# all thats left is print results