import random

size = int(input("enter the total no of payers available:"))
names = input("enter the total names of payer separated by comma:")
list = names.split(",")
print(list)
length = len(list)
a = random.randint(0, (length - 1))
print(a)
print(list[a], " will pay the bill.")
