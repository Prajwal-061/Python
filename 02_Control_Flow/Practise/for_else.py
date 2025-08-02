tuple1 = (1, 2, 3, 4, 5, 6)
for i in tuple1:
    print(i)
    if i == 4:
        break
else:  # else block will be executed only when the for block will be successfully completed.
    print("successfully completed the else block")
print(" Out of for/else block")

number = (2, 4, 8, 56, 9)
for i in number:
    if i % 6 == 0:
        print(i)
        break
else:
    print("There is no number divisible by 6 in the tuple")
