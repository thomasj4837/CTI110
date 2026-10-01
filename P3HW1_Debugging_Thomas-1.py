# Thoms Jonathan
# 29Sept2026
# CTI 110
# Debugging
# Calculate Grades


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = sum(grades)
count = len(grades)
avg = sum / count

'''
# determine letter grade for average


if avg > 90:    
    print(f"Your grade is: A")
elif avg > 80:
    print('Your grade is: B')
else:
    print('Your grade is: F') 
''' 
    # TO DO: finish this
    #calc average (total / count)

print(f"Grades: {grades}")
print(f"{"Lowest Grade:":<25} {low}")
print(f"{"Highest Grade:":<25} {high}")
print(f"{"Sum of Grades:":<25} {sum}")
print(f"{"Average:":<25} {avg:.2f}")

# determine letter grade for average

letter_grade = ""
if avg >= 90:    
    letter_grade = "A"
elif avg >= 80:
    letter_grade = "B"
elif avg >= 70: 
    letter_grade = "C"
elif avg >= 60:
    letter_grade = "D"       
else:
    letter_grade = "F"

print(F"{"Your grade is: ":<25} {letter_grade}")


