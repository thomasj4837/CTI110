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
print(f"Grades: {grade_list}")
print(f"{"Lowest Grade:":<25} {min_grade}")
print(f"{"Highest Grade:":<25} {max_grade}")
print(f"{"Sum of Grades:":<25} {total}")
print(f"{"Average:":<25} {average:.2f}")

