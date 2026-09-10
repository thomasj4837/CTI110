# Thomas Jonathan
# 9/10/2026
# P1HW2
# Calculate Travel Budget

# Get the user's trip info
budget = int( input("Enter budget: "))
destination = input("Enter your travel destination: ")
gas = int( input("Enter how much you will spend on gas: "))
accommodations = int( input("Enter how much you will spend on accommodations: "))
food = int( input("Enter how much do you need for food: "))

print("Travel Expenses")
print("location: ", destination)
print("Initial Budget: ", budget)
print("gas: ", gas)
print("accommodations: ", accommodations)
print("food: ", food)

expenses = gas + accommodations + food
print("expenses: ", expenses)

balance = budget - expenses
print("balance:", balance)