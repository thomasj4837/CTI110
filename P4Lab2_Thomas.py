# CTI 110
#P4lab2 - loops
# ThomasJ
# 08Oct2026



# Set up variables
# Start the Main Loop
again = "yes"
while again == "yes":


    # # Ask the user for their chosen integer (0-12)
    multiplier = int(input("Enter a number 0-12: "))
    # validate (loop) - number must be between 0 and 12
    while multiplier < 0 or multiplier > 12:
        print("That is not a valid answer.")
        multiplier = int(input("Enter a number 0-12: "))

    # print the times table header
    print("Multiplication Table")
    print("-"*20)
    # print the times table (loop)
    for number in range(1, 13):
        #print(multiplier, "*", number, "=", number*multiplier)
        print(f"{multiplier} * {number} = {number * multiplier}")
    # Finally, ask if they want to repeat
    again = input("Run again? (yes/no) ")

# outside the loop
print()
print("Exiting program... ")


