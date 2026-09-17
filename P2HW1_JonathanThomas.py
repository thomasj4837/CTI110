#CTI 110
# P2HW1 - Setup only
# 17Sept2026
# Talk about how to display this page

# Sample data - real program uses input()
"""
destination = "Raleigh"
budget      = 2000.00
expenses    = 1000.00
fuel        = 200.00
food        = 100.00
"""
# Get the user's trip info
budget = float( input("Enter budget: "))
destination = input("Enter your travel destination: ")
gas = float( input("Enter how much you will spend on gas: "))
accommodations = float( input("Enter how much you will spend on accommodations: "))
food = float( input("Enter how much do you need for food: "))


print(f"{"Destination:":<15} {destination:<15}")
print(f"{"Initial Budget:":<15} ${budget:<15.2f}")
print(f"{"Accomodations:":<15} ${accommodations:<15.2f}")
print(f"{"Gas:":<15} ${gas:<15.2f}")
print(f"{"Food:":<15} ${food:<15.2f}")

expenses = gas + accommodations + food
#print("expenses: ", expenses)
print(f"{"expenses:":<15} ${expenses:<15.2f}")

balance = budget - expenses  
#print("balance:", balance)
print(f"{"balance:":<15} ${balance:<15.2f}")
