# Calculate how to split a bill that includes the tip

# Greeting
print("Welcome to the bill calculator")

# Inputs
bill_total = input("What was the total bill? ")
tip_percentage = input("How much tip would you like to give? 10, 12, or 15 per cent? ")
persons = input("How many people to split the bill? ")

# Calculation
tip_percentage = 1 + (float(tip_percentage) / 100)
tip_split = round((float(bill_total) * tip_percentage) / int(persons), 2)

# Output
print(f"Each person should pay: ${tip_split}")