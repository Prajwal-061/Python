bill = 0
print("Welcome to the python pizza")
print(f"the available pizzas are:\n Small\n Medium\n Large")
size = input("enter the size of the pizza that you want (s/m/l)?:")
if size == 'S' or size == 's':
    print("price for small pizza is Rs 100")
    bill = bill + 100
elif size == "m" or size == 'M':
    print("Price for medium pizza is Rs 200")
    bill += 200
else:
    print("price for large pizza is Rs 300")
    bill += 300

pepperoni = input("Do you want pepperoni?(Y/N)")
if pepperoni == 'y' or pepperoni == 'Y':
    if size == "s" or size == 'S':
        print("Pepperoni for small pizza is Rs 30")
        bill = bill + 30
    else:
        bill = bill + 80
        print("Pepperoni for medium pizza and large pizza is Rs 80")

cheese = input("Do you want extra cheese(Y/N)?")
print("Extra cheese for any pizza is Rs 20")
if cheese == "Y" or cheese == 'y':
    bill = bill + 20

print(f"Your total bill is Rs {bill}")
