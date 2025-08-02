height = input("enter the heights of a people separated by comma:")
list_height = height.split(",")
length = len(list_height)
s = 0
print(list_height)
for i in list_height:
    s = s + float(i)
average = s / length
average = round(average)
print(f"the sum of the heights is {s}")
print(f"the average height is {average}")
