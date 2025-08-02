height = int(input("enter your height in feet:"))
bill = 0
if height >= 3:
    print("You can ride")
    age = int(input("enter your age:"))
    if age <= 12:
        bill = 150
        print(f"You have to pay Rs {bill}")
    if 18 >= age > 12:
        bill = 250
        print(f"You have to pay Rs {bill}")
    if age > 18:
        bill = 500
        print(f"You have to pay Rs {bill}")
    want_photos = input("Do you want to take photos(Y/N)?")
    if want_photos == 'Y' or want_photos == 'y':
        print("Extra charge is Rs 50.")
        print(f"total charge is {bill+50}")
    else:
        print(f"total charge is {bill}")
else:
    print("You cannot ride")
