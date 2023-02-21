# Build an automatic pizza order program

## Inputs            
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

## Size cost
if size == "S" :
    size_cost = 15
elif size == "M" :
    size_cost = 20
else :
    size_cost = 25

## Pepperoni
if add_pepperoni == "Y" and size == "S":
    pepperoni_cost = 2
elif  add_pepperoni == "Y" and (size == "M" or size == "L") :
    pepperoni_cost = 3
else :
    pepperoni_cost = 0

## Extra cheese
if  extra_cheese == "Y" :
    cheese_cost = 1
else :
    cheese_cost = 0

## Final bill
final_bill = size_cost + pepperoni_cost + cheese_cost

## Output
print(f"Your final bill is: ${final_bill}")