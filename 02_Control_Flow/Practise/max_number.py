numbers = input("enter the numbers separated by comma:")
list_number = numbers.split(",")
print(list_number)
maximum = int(list_number[0])
count = 0
for i in list_number:
    count = count + 1;
print(f"the length of list is {count}")
for i in range(count):
    if int(list_number[i]) > maximum:
        maximum = int(list_number[i])
print(f"the largest number is {maximum}")
