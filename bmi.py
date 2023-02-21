# Write a program that interprets the Body Mass Index (BMI) based on a 
# user's weight and height.

## Inputs
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

## BMI calculation
height_float = float(height)
weight_float = float(weight)
bmi = round(weight_float / (height_float ** 2), 2)

## Classification
if bmi < 18.5 :
    print(f"Your BMI is {bmi}. You are underweithed")
elif bmi >= 18.5 and bmi < 25 :
    print(f"Your BMI is {bmi}. You have a normal weight")
elif bmi >= 25 and bmi < 30 :
    print(f"Your BMI is {bmi}. You present overweight")
elif bmi >= 30 and bmi < 35 :
    print(f"Your BMI is {bmi}. You present obesity class 1")
else :
    print (f"Your BMI is {bmi}. You present obesity class II")
