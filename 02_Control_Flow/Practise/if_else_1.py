"""number = int(input("enter the number:"))
if (number % 2 == 0):
    print("it is even")
else:
    print("it is odd")"""

# nested if
height = int(input("enter your height:"))
if height >= 3:
    print("you can ride bike")
    age = int(input("enter your age:"))
    if age < 18:
        print("you cannot ride the bike")
    else:
        print("you can ride bike")
else:
    print("you cannot ride the bike")
    print("bye bye")
