import random

choose = ['rock', 'paper', 'scissors']
print("Welcome to the Rock Paper Scissors Game")
user_choice = int(input(" 0 for Rock\n 1 for Paper\n 2 for Scissors\n enter your choice:"))
print(f" user choice={user_choice} for {choose[user_choice]}")
computers_choice = random.randint(0, 2)
print(f"computer choice={computers_choice} for {choose[computers_choice]}")
if 0 <= user_choice <= 2:
    if user_choice == computers_choice:
        print("It is Draw")
    elif computers_choice == 0 and user_choice == 2:
        print("You loose")
    elif computers_choice == 2 and user_choice == 0:
        print("You win")
    elif computers_choice > user_choice:
        print("You lose")
    else:
        print("You win")
else:
    print("You have entered invalid number. Please enter valid choice")
