# Write a program that works out whether a given number is an odd or even number

## Input
from re import S


number = int(input("Which number do you want to check? "))

## Evaluation and result
module_result = number % 2
if module_result == 0 :
    result = print(f"{number} is an even number")
else :
    print(f"{number} is an odd number")
