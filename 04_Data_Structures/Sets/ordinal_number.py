# cardinal number
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(list_1)):
    if i == 0:
        print(f"{i + 1}st")
    elif i == 1:
        print(f"{i + 1}nd")
    elif i == 2:
        print(f"{i + 1}rd")
    else:
        print(f"{i + 1}th")
