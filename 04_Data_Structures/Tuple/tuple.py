tuple_1 = (1, 2, 3, 4, 5, 6)
print(tuple_1[0])
tuple_2 = (45, "Prajwal", "rijan")
print(type(tuple_2))

# nesting of tuple
tuple_3 = (tuple_1, tuple_2)
print(tuple_3)
print(tuple_3[0])
print(len(tuple_3))

# concatenation of tuple
tuple_3 = tuple_1 + tuple_2
print(tuple_3)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
list3 = [list1, list2]
print(list3)
