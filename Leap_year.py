# Write a program that works out whether if a given year is a leap 
# year

## Input
year = int(input("Which year do you want to check? "))

## Evaluation and result
if year % 4 == 0 and year % 100 != 0 and year % 400 == 0 :
    print(f"{year} is a leap year")
elif year % 4 == 0 and year % 100 == 0 :
    print(f"{year} is not a leap year")
elif year % 4 == 0 :
     print(f"{year} is a leap year")
else :
    print(f"{year} is not a leap year")
