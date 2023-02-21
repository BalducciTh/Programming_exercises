# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left 
# if we live until 90 years old

age = input("What is your current age in years? ")
years_left = 90 - int(age)
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12
print(f"You have {days_left} days left, which are {weeks_left} weeks or {months_left} months")